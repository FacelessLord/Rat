from typing import Tuple, Iterable

from Lexer import Rule
from contexts.general import GeneralContext
from contexts.steppers import get_ctx_stepper
from contexts.types import ContextType
from tree.builder import TreeBuilder


def _parse_ctx_tree(tokens: Iterable[Tuple[str, Rule]]):
    ctx = GeneralContext()
    for token in tokens:
        ctx, token_consumed = get_ctx_stepper(ctx.get_type())(ctx, token)

        while not token_consumed:
            ctx, token_consumed = get_ctx_stepper(ctx.get_type())(ctx, token)

    return ctx


def build_tree(tokens: Iterable[tuple[str, Rule]], builder: TreeBuilder):
    ctx_tree = _parse_ctx_tree(tokens)
    print(ctx_tree)
    if ctx_tree.get_type() == ContextType.general:
        return ctx_tree.to_tree_node(builder)
