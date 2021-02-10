from contexts.function_stepper import func_stepper
from contexts.generic_stepper import generic_stepper
from contexts.let_variable_stepper import let_variable_stepper
from contexts.types import ContextType
from contexts.var_func_stepper import var_func_stepper
from contexts.variable_stepper import variable_stepper


def join(a, b):
    return lambda ctx, token: b(ctx, token, a)


ContextSteppers = {
    ContextType.algebraic_expression: generic_stepper,
    ContextType.binary_operation: generic_stepper,
    ContextType.generic_context: generic_stepper,
    ContextType.function: join(generic_stepper, func_stepper),
    ContextType.general: generic_stepper,
    ContextType.group: generic_stepper,
    ContextType.let: join(generic_stepper, let_variable_stepper),
    ContextType.number: generic_stepper,
    ContextType.string: generic_stepper,
    ContextType.variable: join(generic_stepper, variable_stepper),
    ContextType.varFunction: join(generic_stepper, var_func_stepper),
    ContextType.code_group: generic_stepper
    }


def get_ctx_stepper(name: ContextType):
    return ContextSteppers[name]
