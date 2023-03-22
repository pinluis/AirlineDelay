# Install poetry on your device

## Install poetry on your device

```bash
curl -sSL https://install.python-poetry.org | python
```

## Configure Poetry to use local virtual envs

```bash
poetry config virtualenvs.in-project true
```

## Install dependencies

```bash
poetry install
```

Check if you have a virtual environment. If so you wil see a folder called `.venv` in your project folder.
