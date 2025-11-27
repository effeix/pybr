# pybr

Collection of utilities for handling Brazilian data, documents and formats.

## Overview

`pybr` is a collection of utilities designed to handle common Brazilian data formats and standards. It provides a clean, simple, and reliable interface for validating, formatting, and cleaning various types of data specific to Brazil.

This library is aimed at developers who need to work with Brazilian data and want to ensure correctness and proper formatting according to local standards. While it currently includes robust support for document numbers, the long-term goal is to cover a wider range of data types, such as dates, currency, and more.

## Features

- **Brazilian Documents**: Tools for validating, formatting, and cleaning taxpayer registry numbers.
  - **CPF**: Support for individual taxpayer numbers.
  - **CNPJ**: Support for company taxpayer numbers, including 2026 alphanumeric format.
- **Extensible**: Designed with a base structure to easily support other Brazilian data types in the future (e.g., dates, phone numbers).
- **Type-hinted**: Fully type-hinted for better editor support and code quality.
- **No Dependencies**: Lightweight and dependency-free.

## Installation

You can install `pybr` from PyPI:

```bash
pip install pybr
```

## Usage

Here are a few examples of how you can use `pybr`.

### Example: CPF

The `CPF` class provides methods to handle CPF numbers.

```python
from pybr import CPF

# --- Validation ---
# Note: Replace with a valid CPF for actual testing
cpf_valid = "123.456.789-00" 
cpf_invalid = "111.111.111-11"

print(f"Is {cpf_valid} valid? {CPF.is_valid(cpf_valid)}")
# Is 123.456.789-00 valid? True

print(f"Is {cpf_invalid} valid? {CPF.is_valid(cpf_invalid)}")
# Is 111.111.111-11 valid? False

# By default, repeated digit sequences are invalid. You can allow them:
print(f"Is {cpf_invalid} valid (allowing repeated)? {CPF.is_valid(cpf_invalid, allow_repeated=True)}")
# Is 111.111.111-11 valid (allowing repeated)? True (but checksum is still checked)


# --- Formatting ---
unformatted_cpf = "12345678900"
formatted_cpf = CPF.format(unformatted_cpf)
print(f"Formatted CPF: {formatted_cpf}")
# Formatted CPF: 123.456.789-00


# --- Cleaning ---
dirty_cpf = "123.456.789///00"
clean_cpf = CPF.clean(dirty_cpf)
print(f"Cleaned CPF: {clean_cpf}")
# Cleaned CPF: 12345678900


# --- Enforcement ---
# The `validate` method raises a ValueError for invalid CPFs.
try:
    CPF.validate(cpf_invalid)
except ValueError as e:
    print(e)
    # "Invalid CPF"
```

### Example: CNPJ

The `CNPJ` class provides methods to handle CNPJ numbers.

```python
from pybr import CNPJ

# --- Validation ---
# Note: Replace with a valid CNPJ for actual testing
cnpj_valid = "06.990.590/0001-23" 
cnpj_invalid = "11.111.111/1111-11"

print(f"Is {cnpj_valid} valid? {CNPJ.is_valid(cnpj_valid)}")
# Is 00.000.000/0001-91 valid? True

print(f"Is {cnpj_invalid} valid? {CNPJ.is_valid(cnpj_invalid)}")
# Is 11.111.111/1111-11 valid? False


# --- Formatting ---
unformatted_cnpj = "06990590000123"
formatted_cnpj = CNPJ.format(unformatted_cnpj)
print(f"Formatted CNPJ: {formatted_cnpj}")
# Formatted CNPJ: 06.990.590/0001-23


# --- Cleaning ---
dirty_cnpj = "06.990.590/0001-23"
clean_cnpj = CNPJ.clean(dirty_cnpj)
print(f"Cleaned CNPJ: {clean_cnpj}")
# Cleaned CNPJ: 06990590000123


# --- Enforcement ---
# The `validate` method raises a ValueError for invalid CNPJs.
try:
    CNPJ.validate(cnpj_invalid)
except ValueError as e:
    print(e)
    # "Invalid CNPJ"
```

## Contributing

Contributions are welcome! If you have a feature request, bug report, or want to add support for another Brazilian data type (like dates, phone numbers, etc.), please feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-new-feature`).
3. Make your changes and add tests.
4. Ensure the test suite passes (`pytest`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/effeix/pybr/blob/main/LICENSE) file for details.
