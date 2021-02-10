from enum import Enum


class ContextType(Enum):
    algebraic_expression = "ctxAlgebraicExpression"
    binary_operation = "ctxBinaryOperation"
    generic_context = "ctxGeneric"
    function = "ctxFunction"
    varFunction = "ctxVarFunction"
    general = "ctxGeneral"
    group = "ctxGroup"
    let = "ctxLetVarContext"
    number = "ctxNumber"
    string = "ctxString"
    variable = "ctxVar"
    code_group = "ctxCodeGroup"

    def __str__(self):
        return self.value
