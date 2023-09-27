# Surgeon

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
import surgeon as sg

even_odd_enum = (
    sg.EnumBuilder("EvenOdd", scoped=True)
    .add_member("Even")
    .add_member("Odd")
    .build()
)

get_even_odd_function = (
    sg.FunctionBuilder("GetEvenOdd", "EvenOdd")
    .add_specifier("inline")
    .add_argument("int", "value", sg.literals.integer(0))
    .add_statement(
        sg.statements.return_(
            sg.operators.other.conditional(
                sg.operators.arithmetic.remainder(
                    sg.literals.identifier("value"),
                    sg.literals.integer(2),
                ),
                sg.literals.identifier("EvenOdd::Odd"),
                sg.literals.identifier("EvenOdd::Even"),
            )
        )
    )
    .build()
)

document = (
    sg.DocumentBuilder(pragma_once=True)
    .add_declaration(even_odd_enum.definition)
    .add_declaration(get_even_odd_function.definition)
    .build()
)
formatter = sg.ClangFormatter(configuration_style="google")
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

The "factory" API allows you to create any `Surgeon` element:

- `sg.document(...) -> Document`
- `sg.declarations.[specific declaration type](...) -> Declaration`
- `sg.literals.[specific literal type](...) -> Literal`
- `sg.operators.[specific operator type](...) -> Operator`
- `sg.statements.[specific statement type](...) -> Statement`

Some elements are awkward to create this way - such as functions, which contain arguments, internal statements, specifiers, and so on. For those elements, you should use a builder.

### Builder API

There are several builders:

- `sg.ClassBuilder`
- `sg.EnumBuilder`
- `sg.FunctionBuilder`
- `sg.NamespaceBuilder`
- `sg.DocumentBuilder`
- `sg.CompoundStatementBuilder`
- `sg.FunctionCallOperatorBuilder`
- `sg.VariableDeclarationBuilder`

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
