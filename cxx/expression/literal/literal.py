from cxx.expression.expression import Expression


class Literal(Expression):
    def __post_init__(self) -> None:
        if type(self) == Literal:
            raise TypeError("Don't use this class - use a subclass.")
