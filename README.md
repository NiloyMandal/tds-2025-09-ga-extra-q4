# Q4 - GitHub Actions Workflow with Status Badge

![CI](https://github.com/NiloyMandal/tds-2025-09-ga-extra-q4/actions/workflows/ci.yml/badge.svg)

This project demonstrates a GitHub Actions CI/CD workflow with a status badge for continuous integration visibility.

## Features

- ✅ GitHub Actions workflow for CI/CD
- ✅ Python testing with pytest
- ✅ Code linting with flake8
- ✅ Status badge in README
- ✅ Automated testing on push and pull requests

## Project Structure

```
Q4/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow
├── calculator.py           # Main application code
├── test_calculator.py      # Test cases
├── requirements.txt        # Python dependencies
└── README.md              # This file with status badge
```

## Calculator Application

This project includes a simple calculator module with basic arithmetic operations:

- Addition
- Subtraction
- Multiplication
- Division (with zero-division error handling)

## Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest test_calculator.py

# Run linting
flake8 .
```

## GitHub Actions Workflow

The CI workflow automatically:

1. **Triggers on**: Push to main/master branch and pull requests
2. **Sets up**: Python 3.9 environment
3. **Installs**: Dependencies from requirements.txt
4. **Runs**: Test suite with pytest
5. **Lints**: Code with flake8 for syntax errors and style issues
6. **Validates**: Python file structure

## How to Update the Status Badge

1. Go to your repository's **Actions** tab
2. Click on your **CI** workflow
3. Click the **three dots (•••)** in the upper right
4. Select **"Create status badge"**
5. Copy the Markdown and replace the badge URL in this README

### Current Badge Template:

```markdown
![CI](https://github.com/username/repo/actions/workflows/ci.yml/badge.svg)
```

### Current Repository Badge:

```markdown
![CI](https://github.com/NiloyMandal/tds-2025-09-ga-extra-q4/actions/workflows/ci.yml/badge.svg)
```

## Status Badge States

- 🟢 **Green**: All checks passed
- 🔴 **Red**: Some checks failed
- 🟡 **Yellow**: Workflow is running
- ⚪ **Gray**: No workflow runs yet

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests locally
5. Push changes (triggers CI)
6. Create a pull request

The status badge will show the current state of your main branch builds!
