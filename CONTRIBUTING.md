# Contributing to AI Boardroom

Thank you for your interest in contributing to AI Boardroom! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues
- Use the GitHub issue tracker to report bugs
- Describe the issue in detail
- Include steps to reproduce the problem
- Mention your environment (OS, Python version, etc.)

### Suggesting Features
- Open an issue with the label "enhancement"
- Describe the feature and its benefits
- Explain how it fits into the project's goals

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/SANJAYSAHU1975/ai_boardroom.git
   cd ai_boardroom
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Make your changes**
   - Write clean, documented code
   - Follow PEP 8 style guidelines
   - Add tests for new features
   - Update documentation as needed

5. **Run tests**
   ```bash
   python -m unittest test_app.py
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Describe your changes in detail

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Comment complex logic

## Testing

- Write unit tests for new features
- Ensure all tests pass before submitting
- Aim for good test coverage
- Test edge cases and error conditions

## Documentation

- Update README.md if you add new features
- Add docstrings to new functions and classes
- Update API documentation for new endpoints
- Include usage examples where appropriate

## Pull Request Guidelines

- One feature per pull request
- Keep changes focused and atomic
- Write clear commit messages
- Update tests and documentation
- Reference related issues

## Community

- Be respectful and constructive
- Follow the code of conduct
- Help others in discussions
- Share knowledge and ideas

Thank you for contributing to AI Boardroom!
