from surgeon.expression.expression import Expression
from surgeon.expression.operator.cast_mode import CastMode
from surgeon.expression.operator.operator import Operator


class CastOperator(Operator):
    type: str
    operand: Expression
    mode: CastMode
