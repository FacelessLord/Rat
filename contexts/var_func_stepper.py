from typing import Tuple, Callable

from Rules import Rule
from contexts.context import Context
from contexts.factories import create_ctx
from contexts.types import ContextType


def var_func_stepper(ctx:Context, token: Tuple[str, Rule],
                         super_stepper: Callable[[Context, Tuple[str, Rule]],
                                                 Tuple[Context, bool]]) -> Tuple["Context", bool]:
    if len(ctx.children) == 2:
        return ctx.parent, False
    return super_stepper(ctx, token)
