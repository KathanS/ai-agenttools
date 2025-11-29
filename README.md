# AgentTools

Semantic Kernel plugins for file I/O, Excel operations, and shell commands.

## Installation

```bash
pip install agenttools
```

For Excel support:
```bash
pip install agenttools[excel]
```

## Usage

```python
from agenttools import FileIOTools, ExcelTools, ShellTool
from semantic_kernel import Kernel

kernel = Kernel()
kernel.add_plugin(FileIOTools(), plugin_name="file_io_tools")
kernel.add_plugin(ExcelTools(), plugin_name="excel_tools")
kernel.add_plugin(ShellTool(), plugin_name="shell_tool")
```

## Features

### FileIOTools
- `ensure_dir` - Create directories
- `write_file` - Write text files
- `append_file` - Append to files
- `read_file` - Read text files

### ExcelTools
- `create_workbook` - Create Excel files
- `read_sheet` - Read Excel data
- `write_cell` - Write to cells
- `write_rows` - Write multiple rows
- And more...

### ShellTool
- `run_shell` - Execute shell commands with safety checks

## License

**CC BY-NC 4.0** - Free for non-commercial use. For commercial licensing, please contact the author.

This software is provided for personal, educational, and research use only. Commercial use requires a separate license.
