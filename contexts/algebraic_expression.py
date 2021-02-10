from contexts.generic_context import Context

from contexts.types import ContextType

from finq import FINQ
from tree.builder import TreeBuilder
from tree.node import TreeNode


class AlgebraicExpressionContext(Context):
    def __init__(self):
        super().__init__()
        self.track_commas = True
        self.nesting = 0

    @staticmethod
    def get_type():
        return ContextType.algebraic_expression

    def to_tree_node(self, builder: TreeBuilder) -> TreeNode:
        operands = FINQ(self.children).map(lambda ctx: ctx.to_tree_node(builder)).to_list()
        return builder.create_algebraic_expression(operands)

    def collect(self, ctx: "Context"):
        if ctx.get_type() == ContextType.binary_operation:
            self.set_position_empty()
        super(AlgebraicExpressionContext, self).collect(ctx)
        if ctx.get_type() == ContextType.binary_operation:
            self.set_position_empty()

    def set_position_empty(self, ignore_empty: bool = False):
        if not self.position_filled and not ignore_empty and self.track_commas:
            raise ValueError("Two operations together")
        self.position_filled = False

    def __repr__(self):
        return FINQ(self.children).map(repr).join_str(' ')
