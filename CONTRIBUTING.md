# 🤝 Contributing to Medical Study Prompt Generator

First off, thank you for considering contributing to this project! It's people like you that make this tool better for medical students everywhere.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct

This project and everyone participating in it is governed by our commitment to:

- **Be respectful** - Treat everyone with respect and professionalism
- **Be collaborative** - Work together to improve the project
- **Be constructive** - Provide helpful feedback and suggestions
- **Be inclusive** - Welcome contributors of all backgrounds and skill levels

---

## 🎯 How Can I Contribute?

### 🐛 Reporting Bugs

**Before submitting a bug report:**
- Check the [documentation](README.md)
- Search existing [issues](https://github.com/blakeyoung81/CSV-Image-Prompt-Generator/issues)

**When submitting a bug report, include:**
- **Description** - Clear description of the bug
- **Steps to Reproduce** - Exact steps to reproduce the behavior
- **Expected Behavior** - What you expected to happen
- **Actual Behavior** - What actually happened
- **Environment** - OS, Python version, dependencies versions
- **Screenshots** - If applicable
- **Error Messages** - Full error messages and stack traces

### 💡 Suggesting Enhancements

**Before submitting an enhancement:**
- Check if it's already been suggested
- Make sure it aligns with project goals

**When suggesting an enhancement:**
- **Clear title** - Descriptive one-line summary
- **Detailed description** - What and why
- **Use cases** - When would this be useful
- **Mockups** - UI changes (if applicable)
- **Alternatives** - What alternatives you considered

### 🔨 Code Contributions

We welcome code contributions! Here are areas where help is needed:

**High Priority:**
- [ ] OCR integration for scanned PDFs
- [ ] Batch processing multiple exams
- [ ] Export to Anki format
- [ ] Mobile-responsive web interface
- [ ] Docker containerization

**Medium Priority:**
- [ ] Additional AI model support (Claude, Gemini)
- [ ] Question topic categorization
- [ ] Progress persistence (resume interrupted runs)
- [ ] Custom prompt templates

**Good First Issues:**
- [ ] Add more unit tests
- [ ] Improve error messages
- [ ] Documentation improvements
- [ ] UI/UX enhancements
- [ ] Code refactoring

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git
- OpenAI API key (for testing)

### Setting Up Your Environment

1. **Fork the repository**
   ```bash
   # Click 'Fork' on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/CSV-Image-Prompt-Generator.git
   cd CSV-Image-Prompt-Generator
   ```

3. **Create a development branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Set up environment**
   ```bash
   echo 'OPENAI_API_KEY=sk-test-key' > .env
   ```

6. **Test the installation**
   ```bash
   python3 test_setup.py
   ```

---

## 📝 Coding Standards

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

**Line Length:**
- Maximum 100 characters (not 79)

**Imports:**
```python
# Standard library imports
import os
import sys

# Third-party imports
from flask import Flask
import openai

# Local application imports
from generate_study_prompts import MedicalPromptGenerator
```

**Docstrings:**
```python
def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
    
    Returns:
        type: Description of return value
    
    Raises:
        ExceptionType: When this exception is raised
    """
    pass
```

**Naming Conventions:**
- `snake_case` for functions and variables
- `PascalCase` for classes
- `UPPER_CASE` for constants
- `_private` for internal methods

### Code Quality

**Before submitting:**
- [ ] Code follows PEP 8
- [ ] All functions have docstrings
- [ ] No debugging print statements
- [ ] No commented-out code
- [ ] Error handling is present
- [ ] Code is DRY (Don't Repeat Yourself)

### Testing

**Add tests for:**
- New features
- Bug fixes
- Edge cases

**Run tests:**
```bash
python3 -m pytest tests/
```

---

## 💬 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
feat(web): add dark mode toggle to web interface

Add a theme switcher in the navigation bar that allows
users to toggle between light and dark modes. Preference
is saved to localStorage.

Closes #42
```

```bash
fix(pdf): resolve image scaling issue for portrait images

Portrait orientation images were being cut off when rendered.
Fixed by calculating aspect ratio correctly before scaling.

Fixes #38
```

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update documentation** - If you changed functionality
2. **Add tests** - If you added features
3. **Run linters** - Ensure code quality
4. **Test thoroughly** - Manual and automated tests
5. **Update CHANGELOG** - Add entry for your changes

### Submitting a Pull Request

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template

3. **PR Title Format**
   ```
   [Type] Brief description
   ```
   Examples:
   - `[Feature] Add OCR support for scanned PDFs`
   - `[Fix] Resolve API key validation error`
   - `[Docs] Update installation instructions`

4. **PR Description Should Include:**
   - **What** - What changes you made
   - **Why** - Why you made these changes
   - **How** - How you implemented the changes
   - **Testing** - How you tested the changes
   - **Screenshots** - For UI changes
   - **Closes** - Reference to issues (e.g., "Closes #42")

### Review Process

1. **Automated checks** - CI/CD runs automatically
2. **Code review** - Maintainers review your code
3. **Feedback** - Address any requested changes
4. **Approval** - PR is approved
5. **Merge** - Maintainer merges your PR

### After Your PR is Merged

1. **Delete your branch**
   ```bash
   git branch -d feature/your-feature-name
   ```

2. **Update your fork**
   ```bash
   git checkout main
   git pull upstream main
   git push origin main
   ```

3. **Celebrate!** 🎉 You're now a contributor!

---

## 🎨 UI/UX Contributions

### Design Guidelines

**Colors:**
- Primary: `#667eea` (Purple)
- Secondary: `#764ba2` (Dark Purple)
- Success: `#10b981` (Green)
- Warning: `#f59e0b` (Orange)
- Error: `#dc2626` (Red)

**Typography:**
- Headers: `Helvetica-Bold`
- Body: `Helvetica`
- Code: `Courier New`

**Spacing:**
- Base unit: 8px
- Small: 8px
- Medium: 16px
- Large: 24px
- XLarge: 32px

### Accessibility

Ensure your UI contributions:
- [ ] Have proper color contrast (WCAG AA)
- [ ] Support keyboard navigation
- [ ] Include ARIA labels where appropriate
- [ ] Work on mobile devices
- [ ] Are readable at different zoom levels

---

## 📚 Documentation Contributions

### Types of Documentation

1. **Code Comments** - Explain complex logic
2. **Docstrings** - Function/class documentation
3. **README** - Project overview
4. **Guides** - Step-by-step tutorials
5. **API Docs** - Function reference

### Documentation Style

**Be:**
- **Clear** - Use simple language
- **Concise** - Get to the point
- **Complete** - Cover all aspects
- **Correct** - Test your examples
- **Consistent** - Match existing style

**Include:**
- Code examples
- Screenshots
- Expected output
- Common pitfalls
- Related links

---

## 🐛 Issue Labels

| Label | Description |
|-------|-------------|
| `bug` | Something isn't working |
| `enhancement` | New feature or request |
| `documentation` | Documentation improvements |
| `good first issue` | Good for newcomers |
| `help wanted` | Extra attention needed |
| `question` | Further information requested |
| `wontfix` | This will not be worked on |
| `duplicate` | This issue already exists |

---

## 💡 Tips for Success

1. **Start small** - Make focused, incremental changes
2. **Communicate** - Ask questions if unclear
3. **Be patient** - Reviews take time
4. **Stay positive** - Feedback is for improvement
5. **Learn** - Every contribution is a learning opportunity

---

## 🙏 Recognition

Contributors are recognized in:
- **Contributors section** - README.md
- **Release notes** - When features are released
- **Hall of Fame** - For significant contributions

---

## 📞 Getting Help

**Need help contributing?**

- 💬 **Discussions** - Ask questions
- 📧 **Email** - Contact maintainers
- 📖 **Docs** - Check existing documentation
- 🐛 **Issues** - Search for similar issues

---

## 🎉 Thank You!

Your contributions make this project better for medical students worldwide. Every bug report, feature request, documentation improvement, and code contribution is valuable.

**Happy Contributing!** 🚀

---

<div align="center">

**Made with ❤️ by the community, for the community**

</div>
