from __future__ import annotations
import json
import subprocess

from semantic_kernel.functions import kernel_function


class ShellTool:
    """Shell command execution with safety checks."""

    @kernel_function(description="Run a shell command (with a small disallow list) and return JSON {exit_code, stdout, stderr}. Optionally run in a given working directory (cwd).")
    def run_shell(self, command: str, timeout_sec: int = 600, cwd: str | None = None) -> str:
        cmd_lc = (command or "").strip().lower()
        deny_patterns = [
            "remove-item -recurse",
            "rm -rf",
            "rd /s",
        ]
        if any(p in cmd_lc for p in deny_patterns):
            return json.dumps({
                "error": "Command blocked by safety policy",
                "command": command,
                "reason": "matches disallowed destructive pattern",
            })
        try:
            proc = subprocess.run(
                ["bash", "-c", command],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout_sec,
                cwd=cwd or None,
            )
            return json.dumps({
                "exit_code": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
                "cwd": cwd or "",
            })
        except Exception as e:
            return json.dumps({"error": str(e)})
