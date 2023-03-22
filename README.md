# Install poetry on your device

## Install poetry on your device

```bash
curl -sSL https://install.python-poetry.org | python
```

If you are not using a container, you can also install poetry with pip:

```bash
pip install poetry
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

## Work with Poetry

To install a new dependency:

```bash
poetry add <package>
```

To remove a dependency:

```bash
poetry remove <package>
```

## Start virtual environment

```bash
poetry shell
```

You can exit the virtual environment with `exit`.
