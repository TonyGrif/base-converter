# Decimal to Base-X Converter 
Python script to convert decimal (base-10) integers and floats to their base-x equivalent.

## Requirements
* [Python 3.9+](https://www.python.org/)

## Running Instructions
This program can be run with the following command: `./main.py [args]` in which args is a non-zero base number and a non-zero amount of real numbers (integers or floats).

Invalid input will not be checked for and will result in undefined behavior.

## Sample Execution & Output
When this program is run with `./main.py 2 0.25 -0.142857 0.75 0.8`, the following output will be created:

```
|   Base 10   |    Base 2   |
| ----------- | ----------- |
|     0.25    |     0.01    |
|  -0.142857  | -0.00100100 |
|     0.75    |     0.11    |
|     0.8     |  0.11001100 |
```

When this program is run with `./main.py 60 0.25 -0.142857 0.75 0.8`, the following output will be created:

```
|   Base 10   |   Base 60   |
| ----------- | ----------- |
|     0.25    |     0.15    |
|  -0.142857  |   -0.83417  |
|     .75     |     0.45    |
|     0.8     |     0.48    |
```

## Development
Install all dependency groups with:

```bash
poetry install --with test,dev,docs
```

### Testing
Run the test suite with [pytest](https://pytest.org):

```bash
poetry run pytest --cov
```

Run tests across all supported Python versions with [tox](https://tox.wiki):

```bash
poetry run tox
```

### Linting & Formatting
```bash
poetry run black .          # Format
poetry run isort .          # Sort Imports
poetry run ruff check .     # Lint
poetry run flake8           # Additional Lint Checks
poetry run mypy             # Type Checking
```

### Documentation
Build the HTML API docs with [Sphinx](https://www.sphinx-doc.org):

```bash
poetry run make -C docs html
```

The output is written to `docs/_build/html/`.

To remove the build artifacts:

```bash
poetry run make -C docs clean
```
