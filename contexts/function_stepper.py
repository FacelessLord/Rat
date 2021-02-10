from typing import Tuple, Callable

from Lexer import Rule
from contexts.generic_context import Context


def func_stepper(ctx, token: Tuple[str, Rule],
                 super_stepper: Callable[[Context, Tuple[str, Rule]], Tuple[Context, bool]]) -> Tuple["Context", bool]:
    if len(ctx.children) > 0:
        return ctx.parent, False
    return super_stepper(ctx, token)
