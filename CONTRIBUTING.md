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

## Publishing

The package is automatically published to PyPI when the version number is updated in `pyproject.toml` and pushed to the `main` branch.

**To release a new version:**

1. Update the version number in both:
   - `pyproject.toml` → `version = "x.y.z"`
   - `agenttools/__init__.py` → `__version__ = "x.y.z"`

2. Commit and push the changes to `main`:
   ```bash
   git add pyproject.toml agenttools/__init__.py
   git commit -m "Bump version to x.y.z"
   git push
   ```

3. The GitHub Actions workflow will automatically:
   - Create a new release with tag `vx.y.z`
   - Build the package
   - Publish to PyPI

Monitor the publish workflow at: https://github.com/KathanS/ai-agenttools/actions

### Version Numbering

Follow semantic versioning:
- **Major (1.0.0)**: Breaking changes
- **Minor (0.2.0)**: New features, backward compatible  
- **Patch (0.2.1)**: Bug fixes

## Code Style

- Use descriptive variable names
- Add docstrings to all public functions
- Use type hints with `Annotated`
- Keep functions focused and single-purpose

## Questions?

Open an issue on GitHub or contact the maintainer.

## License

By contributing, you agree that your contributions will be licensed under the CC BY-NC 4.0 License.
