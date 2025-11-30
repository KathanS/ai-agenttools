import asyncio
import os
import sys
import uuid
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.mcp import MCPStdioPlugin
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatPromptExecutionSettings
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior

from agenttools import FileIOTools, ExcelTools, ShellTool

load_dotenv()

async def main():
    kernel = Kernel()

    kernel.add_service(
        AzureChatCompletion(
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            service_id="chat"
        )
    )

    kernel.add_plugin(FileIOTools(), plugin_name="file_io_tools")
    kernel.add_plugin(ExcelTools(), plugin_name="excel_tools")
    kernel.add_plugin(ShellTool(), plugin_name="shell_tool")

    # Create a per-run sandbox directory using SANDBOX_ROOT_DIR
    sandbox_root_dir = os.getenv("SANDBOX_ROOT_DIR")
    base_dir = os.path.join(sandbox_root_dir, f"sandbox{uuid.uuid4().hex}")
    os.makedirs(base_dir, exist_ok=True)
    print(f"Sandbox directory: {base_dir}")

    tools = []
    for pname, plugin in kernel.plugins.items():
        for fname, func in plugin.functions.items():
            tools.append(f"{pname}.{fname}: {func.description}")
    system_msg = (
        "You are a helpful AI assistant.\n"
        "You have these tools available:\n" + "\n".join(tools) +
        f"\nUse this base_dir for all file reads/writes: {base_dir}\n"
        "Do not write outside base_dir. Always call the correct tool instead of guessing."
    )

    chat_history = ChatHistory(system_message=system_msg)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        chat_history.add_user_message(user_input)

        execution_settings = OpenAIChatPromptExecutionSettings(
            service_id="chat",
            max_tokens=1000,
            temperature=0.7,
            function_choice_behavior=FunctionChoiceBehavior.Auto()
        )

        chat_completion = kernel.get_service("chat")
        response = await chat_completion.get_chat_message_contents(
            chat_history, 
            settings=execution_settings,
            kernel=kernel
        )

        assistant_message = str(response[0]) if response else "No response"
        chat_history.add_assistant_message(assistant_message)
        print(f"Agent: {assistant_message}\n")

if __name__ == "__main__":
    asyncio.run(main())
