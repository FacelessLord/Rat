from typing import Tuple, Callable

from Rules import Rule
from contexts.context import Context
from contexts.factories import create_ctx
from contexts.types import ContextType


def variable_stepper(ctx:Context, token: Tuple[str, Rule],
                         super_stepper: Callable[[Context, Tuple[str, Rule]],
                                                 Tuple[Context, bool]]) -> Tuple["Context", bool]:
    if token[1] == Rule.lparen:
        fctx = create_ctx(ContextType.varFunction)
        ctx.wrap_with(fctx)
        return fctx, False
    else:
        return ctx.parent, False
