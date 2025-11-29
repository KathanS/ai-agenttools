# Publishing Guide for AgentTools

## Quick Start - Publish to PyPI

### 1. Update your details in pyproject.toml
Edit the author name, email, and GitHub URLs

### 2. Install build tools
```powershell
pip install build twine
```

### 3. Build the package
```powershell
python -m build
```

### 4. Create PyPI account
- Go to https://pypi.org/account/register/
- Verify email
- Set up 2FA (recommended)

### 5. Upload to PyPI
```powershell
python -m twine upload dist/*
```

You'll be prompted for your PyPI username and password.

### 6. Done!
Your package is now live at https://pypi.org/project/agenttools/

Users can install with:
```bash
pip install agenttools
```

## Test First (Recommended)

Test on TestPyPI before publishing to real PyPI:

```powershell
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Test install
pip install --index-url https://test.pypi.org/simple/ agenttools
```

## Updating Later

1. Update version in `pyproject.toml` (e.g., 0.1.0 -> 0.1.1)
2. Rebuild: `python -m build`
3. Upload: `python -m twine upload dist/*`
