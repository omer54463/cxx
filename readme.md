# Cxx

A C/C++ source generation package.

## Usage

First, some context:

- Documents contain declarations.
- Declarations contain other declarations, statements and expressions.
- Some statements contain other statements and expressions.
- Expressions are either operators or literals. Operators contain other expressions.

The general usage flow is:

- Populate a `Document` with `Declaration`s of your choice.
- Format it as a string with any `DocumentFormatter` subclass.

### Simple Example

```python
import cxx

even_odd_enum = (
    cxx.EnumBuilder("EvenOdd", scoped=True)
    .add_member("Even")
    .add_member("Odd")
    .build()
)

get_even_odd_function = (
    cxx.FunctionBuilder("GetEvenOdd", "EvenOdd")
    .add_specifier("inline")
    .add_argument("int", "value", cxx.literals.integer(0))
    .add_statement(
        cxx.statements.return_(
            cxx.operators.other.conditional(
                cxx.operators.arithmetic.remainder(
                    cxx.literals.identifier("value"),
                    cxx.literals.integer(2),
                ),
                cxx.literals.identifier("EvenOdd::Odd"),
                cxx.literals.identifier("EvenOdd::Even"),
            )
        )
    )
    .build()
)

document = (
    cxx.DocumentBuilder(header=True)
    .add_declaration(even_odd_enum.definition)
    .add_declaration(get_even_odd_function.definition)
    .build()
)
formatter = cxx.ClangFormatter(configuration_style="google")
print(formatter.format(document))
```

Output:

```cpp
#pragma once

enum class EvenOdd {
  Even,
  Odd,
};

inline EvenOdd GetEvenOdd(int value = 0) {
  return value % 2 ? EvenOdd::Odd : EvenOdd::Even;
}
```

### "Factory" API

The "factory" API allows you to create any element:

- `cxx.document(...) -> Document`
- `cxx.declarations.[specific declaration type](...) -> Declaration`
- `cxx.literals.[specific literal type](...) -> Literal`
- `cxx.operators.[specific operator type](...) -> Operator`
- `cxx.statements.[specific statement type](...) -> Statement`

Some elements are awkward to create this way - such as functions, which contain arguments, internal statements, specifiers, and so on. For those elements, you should use a builder.

### Builder API

There are several builders:

- `cxx.ClassBuilder`
- `cxx.EnumBuilder`
- `cxx.FunctionBuilder`
- `cxx.NamespaceBuilder`
- `cxx.DocumentBuilder`
- `cxx.CompoundStatementBuilder`
- `cxx.FunctionCallOperatorBuilder`
- `cxx.VariableDeclarationBuilder`

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

Install and configure poetry:

```txt
pip3 install poetry
poetry config virtualenvs.in-project true
```

Install development dependencies and pre-commit hook

```txt
poetry install --with dev
pre-commit install
```

Run the tests:

```txt
poetry run pytest
```
