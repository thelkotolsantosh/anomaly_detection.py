# Contributing to Login Anomaly Detection

Thank you for your interest in contributing to the Login Anomaly Detection project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions with other contributors and maintainers.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   bash
   git clone https://github.com/yourusername/login-anomaly-detection.git
   cd login-anomaly-detection
   
3. **Create a virtual environment**:
   bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
4. **Install development dependencies**:
   bash
   pip install -r requirements.txt
   pip install -e ".[dev]"
   

## Development Workflow

### Creating a Feature Branch

Create a new branch for your feature:
bash
git checkout -b feature/your-feature-name


Use descriptive branch names:
- `feature/add-visualization` for new features
- `fix/threshold-calculation` for bug fixes
- `docs/update-readme` for documentation changes

### Code Style

Follow these guidelines:

1. **PEP 8 Compliance**: Use `black` for formatting
   bash
   black anomaly_detection.py
   

2. **Linting**: Check with `flake8`
   bash
   flake8 anomaly_detection.py
   

3. **Type Hints**: Use type annotations where possible
   python
   def detect_anomalies(df: pd.DataFrame, std_multiplier: float = 2) -> tuple:
       ...
   

4. **Docstrings**: Use Google-style docstrings
   python
   def my_function(param1: int) -> str:
       """
       Brief description of function.
       
       Longer description can go here if needed.
       
       Args:
           param1 (int): Description of param1
           
       Returns:
           str: Description of return value
       """
   

### Testing

1. **Write Tests**: Add tests for any new functionality in `test_anomaly_detection.py`
   
2. **Run Tests**: Ensure all tests pass
   bash
   pytest test_anomaly_detection.py -v
   

3. **Coverage**: Check test coverage
   bash
   pytest --cov=anomaly_detection test_anomaly_detection.py
   

### Commit Messages

Write clear, descriptive commit messages:


git commit -m "Add isolation forest method for anomaly detection

- Implement IsolationForest wrapper
- Add tests for new method
- Update documentation with examples"


Guidelines:
- Use imperative mood ("Add feature" not "Added feature")
- Start with a short summary (50 chars max)
- Leave a blank line after the summary
- Wrap detailed description at 72 characters
- Reference issues when relevant: "Fixes #123"

## Making a Pull Request

1. **Push to Your Fork**:
   bash
   git push origin feature/your-feature-name
   

2. **Open a Pull Request** on GitHub with:
   - Clear title describing the change
   - Description of what you changed and why
   - Reference to any related issues (e.g., "Fixes #42")
   - Screenshots or examples if applicable

3. **PR Checklist**:
   - [ ] Code follows PEP 8 style guidelines
   - [ ] All tests pass locally
   - [ ] New tests added for new functionality
   - [ ] Documentation updated if needed
   - [ ] No unnecessary dependencies added
   - [ ] Commits are clean and well-described

4. **Review Process**:
   - Maintainers will review your PR
   - Address any feedback or suggestions
   - Update your branch if necessary
   - Once approved, your PR will be merged

## Reporting Issues

When reporting bugs:

1. **Check existing issues** to avoid duplicates
2. **Include details**:
   - Python version
   - Operating system
   - Versions of pandas and numpy
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Error messages or tracebacks

3. **Create a minimal example** that reproduces the issue

Example issue:

Title: Anomaly detection fails with empty DataFrame

Description:
When calling detect_anomalies() with an empty DataFrame, 
the function crashes with a ZeroDivisionError.

Steps to reproduce:
1. Create empty DataFrame with 'logins' column
2. Call detect_anomalies(empty_df)

Expected: Return empty anomalies DataFrame and stats with count=0
Actual: ZeroDivisionError at line X

Environment:
- Python 3.9
- pandas 1.3.0
- numpy 1.20.0


## Feature Requests

Suggest enhancements by:

1. **Describing the use case** - Why would this be useful?
2. **Providing examples** - How would you use this feature?
3. **Discussing alternatives** - Are there other ways to solve this?

## Documentation

Help improve documentation:

- Fix typos and grammar
- Clarify confusing sections
- Add examples
- Improve API reference
- Create tutorials

Edit `README.md` or create new `.md` files for detailed documentation.

## Project Structure


login-anomaly-detection/
├── anomaly_detection.py          # Core module
├── test_anomaly_detection.py     # Unit tests
├── requirements.txt              # Dependencies
├── setup.py                      # Package setup
├── README.md                     # Main documentation
├── CONTRIBUTING.md               # This file
├── LICENSE                       # MIT License
└── .gitignore                    # Git ignore rules


## Areas for Contribution

- **Features**: New detection methods, visualization, persistence
- **Bug fixes**: Issues labeled as bugs on GitHub
- **Documentation**: Tutorials, examples, API docs
- **Tests**: Increase coverage, edge cases
- **Performance**: Optimize algorithms, reduce memory usage

## Questions?

- Open an issue with the `question` label
- Check existing documentation
- Review closed issues for solutions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🎉
