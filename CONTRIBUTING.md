# Contributing to GitHub Activity

Thank you for your interest in contributing to GitHub Activity! This document provides guidelines and steps for contributing to the project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Prerequisites

- Python installed on your system
- Basic knowledge of Git and GitHub
- Understanding of the GitHub API

### Getting Started

1. **Fork the Repository**
   - Visit the [GitHub Activity repository](https://github.com/P-Nelly/github-activity)
   - Click the "Fork" button in the top right corner

2. **Clone Your Fork**
   ```sh
   git clone https://github.com/YOUR-USERNAME/github-activity
   cd github-activity
   ```

3. **Create a New Branch**
   ```sh
   git checkout -b feature/your-feature-name
   ```
   
   Name your branch according to what you're working on:
   - `feature/` - for new features
   - `fix/` - for bug fixes
   - `docs/` - for documentation changes

4. **Make Your Changes**
   - Write clean, readable code
   - Follow Python PEP 8 style guidelines
   - Add comments where necessary
   - Test your changes thoroughly

5. **Commit Your Changes**
   ```sh
   git add .
   git commit -m "Brief description of your changes"
   ```
   
   Commit messages should be:
   - Clear and concise
   - Written in present tense
   - Descriptive of what changes were made

6. **Push to GitHub**
   ```sh
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Fill out the PR template
   - Submit the PR

## Development Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Keep functions focused and single-purpose
- Add docstrings for functions and classes

### Testing
- Add tests for new features
- Ensure all existing tests pass
- Test edge cases and error conditions

### Documentation
- Update README.md if adding new features
- Add inline comments for complex logic
- Update docstrings as needed

## Project Scope

Current project priorities are aligned with the roadmap:
1. Authentication implementation for increased API rate limits
2. Filtering options for specific event types
3. Additional event type support

## Getting Help

- Check existing [Issues](https://github.com/P-Nelly/github-activity/issues)
- Join project [Discussions](https://github.com/P-Nelly/github-activity/discussions)
- Review the [README.md](README.md) documentation

## License

By contributing to GitHub Activity, you agree that your contributions will be licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 