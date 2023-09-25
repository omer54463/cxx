# Surgeon

A C/C++ source generation package.

## Current Unsupported Features

This is a list of language features this package doesn't currently support.
This is not due to any inherent difficulty - other things were prioritized.

- Initializer list - `int arr[3] = { 0, 1, 2 };`
- For-range loop - `for (auto a : vec) { ... }`
- Structured binding - `auto [a, b] = ...;`
- Multiple-variable simple declaration - `int a=5, b=2;`
- Multiple-type typedef declaration - `typedef int INT, *PINT;`
- Typedef-specifier for declaration - `typedef struct { ... } S;`
- Exception handling - `try`, `catch`, `throw`
- Template and template specialization - `template <typename T>`
- New operator - `new`
- Delete operator - `delete`
- Float/decimal literals - `0.123`

## Development Setup

Install dev-dependencies and pre-commit hook.

```cmd
pip3 install -e .[dev]
pre-commit install
```
