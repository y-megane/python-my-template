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
poetry add pre-commit pytest pytest-cov --dev
poetry run pre-commit install
```

pre-commitの設定を変更した場合、以下のコマンドで反映する。

```bash
poetry run pre-commit autoupdate
```


## Lint and Format

コミットするとpre-commit hookで自動実行される。
手動で実行する場合は以下。

```bash
poetry run pre-commit run --all-files
```

## Test

```bash
poetry run pytest -m unit --cov
```
