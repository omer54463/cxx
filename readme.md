# Surgeon

A C/C++ source generation library.

## Current Unsupported Features

This is a list of language features this library doesn't currently support.
This is not due to any inherent difficulty - other things were prioritized.

- Structured binding - `auto [a, b] = ...;`
- Multiple-variable simple declaration - `int a=5, b=2;`
- Exception handling - `try`, `catch`, `throw`
- Templates and template specializations - `template <typename T>`

## Development Setup

Install dev-dependencies and pre-commit hook.

```
pip3 install -e .[dev]
pre-commit install
```
