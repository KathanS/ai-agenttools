from __future__ import annotations
import os
import json

from semantic_kernel.functions import kernel_function


class FileIOTools:
    """Filesystem operations for reading, writing, and managing files and directories."""

    @kernel_function(description="Ensure a directory exists; create it if missing.")
    def ensure_dir(self, path: str) -> str:
        try:
            os.makedirs(path, exist_ok=True)
            return json.dumps({"status": "ok", "path": os.path.abspath(path)})
        except Exception as e:
            return json.dumps({"error": str(e), "path": path})

    @kernel_function(description="Write text content to a file (UTF-8). Creates parent dirs if needed.")
    def write_file(self, path: str, content: str) -> str:
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            return json.dumps({"status": "ok", "path": os.path.abspath(path)})
        except Exception as e:
            return json.dumps({"error": str(e), "path": path})

    @kernel_function(description="Append text to a file (UTF-8). Creates file and parent dirs if needed.")
    def append_file(self, path: str, content: str) -> str:
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "a", encoding="utf-8") as f:
                f.write(content)
            return json.dumps({"status": "ok", "path": os.path.abspath(path)})
        except Exception as e:
            return json.dumps({"error": str(e), "path": path})

    @kernel_function(description="Read up to max_bytes of a text file (UTF-8).")
    def read_file(self, path: str, max_bytes: int = 500000) -> str:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read(max_bytes)
            return json.dumps({"status": "ok", "content": content, "path": os.path.abspath(path)})
        except Exception as e:
            return json.dumps({"error": str(e), "path": path})
