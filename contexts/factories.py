from contexts.algebraic_expression import AlgebraicExpressionContext
from contexts.binary_operation import BinaryOperationContext
from contexts.code_group import CodeGroupContext
from contexts.context import Context
from contexts.function import FuncContext
from contexts.general import GeneralContext
from contexts.group import GroupContext
from contexts.let import LetContext
from contexts.number import NumberContext
from contexts.string import StringContext
from contexts.types import ContextType
from contexts.var_function import VarFunctionContext
from contexts.variable import VarContext

ContextsFactory = {
    ContextType.algebraic_expression: AlgebraicExpressionContext,
    ContextType.binary_operation: BinaryOperationContext,
    ContextType.generic_context: Context,
    ContextType.function: FuncContext,
    ContextType.varFunction: VarFunctionContext,
    ContextType.general: GeneralContext,
    ContextType.group: GroupContext,
    ContextType.let: LetContext,
    ContextType.number: NumberContext,
    ContextType.string: StringContext,
    ContextType.variable: VarContext,
    ContextType.code_group: CodeGroupContext
    }


def create_ctx(ctx_type: ContextType, *args):
    return ContextsFactory[ctx_type](*args)
