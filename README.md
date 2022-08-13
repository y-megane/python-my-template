# python-my-template
My python template repository with lint, format, testing and ci

```bash
poetry init --python ^3.9
poetry add isort black flake8 mypy pytest --dev
echo -e '\n[tool.black]\nline-length = 120' >> pyproject.toml
echo -e '\n[tool.isort]\nprofile = "black"'  >> pyproject.toml
echo -e '\n[tool.pytest.ini_options]\nmarkers = ["unit", "integration"]'  >> pyproject.toml
echo -e '[flake8]\nextend-ignore = E203, F401\nmax-line-length = 120' >> .flake8

```
