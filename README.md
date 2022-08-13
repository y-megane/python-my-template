# python-my-template
My python template repository with lint, format, testing and ci

## About

Setup followings.

- Logging
- Linting and Formating
- Unit Testing with pytest

## Setup

```bash
poetry init --python ^3.9
poetry add isort black flake8 mypy pytest pytest-cov --dev
echo -e '\n[tool.black]\nline-length = 120' >> pyproject.toml
echo -e '\n[tool.isort]\nprofile = "black"'  >> pyproject.toml
echo -e '\n[tool.pytest.ini_options]\nmarkers = ["unit", "integration"]'  >> pyproject.toml
echo -e '[flake8]\nextend-ignore = E203, F401\nmax-line-length = 120' >> .flake8

```


## Lint and Format

```bash
poetry run isort .
poetry run black .
poetry run flake8 .
poetry run mypy .
```

## Test

```bash
poetry run pytest -m unit --cov
```
