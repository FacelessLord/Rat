from typing import Tuple, Callable

from Lexer import Rule
from contexts.generic_context import Context


def algebraic_expression_stepper(ctx, token: Tuple[str, Rule],
                                 super_stepper: Callable[[Context, Tuple[str, Rule]], Tuple[Context, bool]]) \
        -> Tuple["Context", bool]:
    if token[1] == Rule.lparen:
        ctx.nesting += 1
        return ctx, True
    if token[1] == Rule.rparen:
        if ctx.nesting == 0:
            return ctx.parent, True
        ctx.nesting -= 1
        return ctx, True
    return super_stepper(ctx, token)
