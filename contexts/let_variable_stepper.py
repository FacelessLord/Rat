from typing import Tuple, Callable

from Lexer import Rule
from contexts.factories import create_ctx
from contexts.generic_context import Context
from contexts.let import type_var, type_func
from contexts.types import ContextType

function_types = [Rule.mut, Rule.parallel, Rule.pure]


def let_variable_stepper(ctx, token: Tuple[str, Rule],
                         super_stepper: Callable[[Context, Tuple[str, Rule]],
                                                 Tuple[Context, bool]]) -> Tuple["Context", bool]:
    if ctx.state == 1:
        if token[1] in function_types:
            ctx.type = type_func
            ctx.modifiers.append(token[0])
            return ctx, True
        if token[1] == Rule.fn:
            ctx.type = type_func
            ctx.state += 1
            return ctx, True
    elif ctx.state == 2:
        if ctx.type == type_var and token[1] == Rule.eq:
            ctx.state += 1
            return ctx, True
        if ctx.type == type_func and token[1] == Rule.var:
            ctx.collect(create_ctx(ContextType.variable, token[0]))
            return ctx, True

    elif ctx.state == 4:
        if ctx.type == type_var:
            return ctx.parent, False
        if ctx.type == type_func and token[1] == Rule.arrow:
            ctx.state += 1
            return ctx, True
    elif ctx.state == 6 and ctx.type == type_func:
        return ctx.parent, False

    return super_stepper(ctx, token)
