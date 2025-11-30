# Contributing to AI AgentTools

Thank you for your interest in contributing to AI AgentTools! This guide will help you get started.

## How to Contribute

### Reporting Bugs
- Open an issue on GitHub
- Describe the bug and how to reproduce it
- Include your Python version and OS

### Suggesting Features
- Open an issue with your feature request
- Explain the use case and benefits
- Discuss implementation approach if possible

### Contributing Code

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-agenttools.git
   cd ai-agenttools
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Install dependencies**
   ```bash
   pip install -e .[all]
   ```

5. **Make your changes**
   - Follow existing code style
   - Add docstrings to all functions
   - Use type hints (Annotated)
   - Handle exceptions properly

6. **Test your changes**
   - Test all affected functionality
   - Ensure no breaking changes

7. **Commit and push**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Describe what you changed and why
   - Reference any related issues

## Development Setup

### Project Structure
```
agenttools/
  ├── file_io_tools.py      # File operations
  ├── excel_tools.py        # Excel operations
  ├── word_tools.py         # Word documents
  ├── powerpoint_tools.py   # PowerPoint presentations
  ├── pdf_tools.py          # PDF operations
  ├── csv_tools.py          # CSV/data manipulation
  ├── web_tools.py          # Web scraping
  └── shell_tool.py         # Shell commands
examples/
  └── chat_demo.py          # Usage example
```

### Adding New Tools

1. Create new file in `agenttools/` directory
2. Follow the pattern of existing tools:
   ```python
   from typing import Annotated
   from semantic_kernel.functions import kernel_function
   
   class YourTool:
       @kernel_function(
           name="function_name",
           description="Clear description for AI"
       )
       def your_function(
           self,
           param: Annotated[type, "Description"]
       ) -> Annotated[str, "Return description"]:
           try:
               # Implementation
               return "Success message"
           except Exception as err:
               return f"Error: {str(err)}"
   ```

3. Add to `__init__.py`
4. Update `README.md` with new tool documentation
5. Add dependencies to `pyproject.toml` if needed

## Publishing (Maintainers Only)

### Automatic Publishing via GitHub Releases (Recommended)

The project is configured to automatically publish to PyPI when you create a new GitHub release.

**One-time setup:**

1. **Add PyPI API Token to GitHub Secrets**
   - Go to https://pypi.org/manage/account/token/
   - Create a new API token with upload permissions
   - Go to your GitHub repo → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI token (starts with `pypi-`)
   - Click "Add secret"

**To publish a new version:**

1. **Update version numbers**
   - `pyproject.toml` - `version = "x.y.z"`
   - `agenttools/__init__.py` - `__version__ = "x.y.z"`

2. **Commit and push changes**
   ```bash
   git add .
   git commit -m "Bump version to x.y.z"
   git push
   ```

3. **Create a GitHub Release**
   - Go to your repo → Releases → "Create a new release"
   - Tag version: `vx.y.z` (e.g., `v0.2.0`)
   - Release title: `vx.y.z` or descriptive title
   - Describe the changes
   - Click "Publish release"

4. **Done!** GitHub Actions will automatically:
   - Build the package
   - Upload to PyPI
   - You can monitor progress in the "Actions" tab

### Manual Publishing

If you prefer to publish manually:

1. **Update version** in both:
   - `pyproject.toml` - `version = "x.y.z"`
   - `agenttools/__init__.py` - `__version__ = "x.y.z"`

2. **Clean old builds**
   ```powershell
   Remove-Item -Recurse -Force dist, build, *.egg-info
   ```

3. **Build the package**
   ```powershell
   pip install build twine
   python -m build
   ```

4. **Test on TestPyPI** (optional but recommended)
   ```powershell
   python -m twine upload --repository testpypi dist/*
   pip install --index-url https://test.pypi.org/simple/ ai-agenttools
   ```

5. **Upload to PyPI**
   ```powershell
   python -m twine upload dist/*
   ```
   
   Use `__token__` as username and your API token as password.

### Version Numbering

Follow semantic versioning:
- **Major (1.0.0)**: Breaking changes
- **Minor (0.2.0)**: New features, backward compatible  
- **Patch (0.2.1)**: Bug fixes

## Code Style

- Use descriptive variable names
- Exception handling: `Exception as err` (not `Exception as e`)
- Add docstrings to all public functions
- Use type hints with `Annotated`
- Keep functions focused and single-purpose

## Questions?

Open an issue on GitHub or contact the maintainer.

## License

By contributing, you agree that your contributions will be licensed under the CC BY-NC 4.0 License.
