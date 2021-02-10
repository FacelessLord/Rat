from tree.builder import TreeBuilder
from tree.node import TreeNode
from contexts.generic_context import Context
from contexts.types import ContextType
from finq import FINQ


class GeneralContext(Context):
    @staticmethod
    def get_type():
        return ContextType.general

    def to_tree_node(self, builder) -> TreeNode:
        return builder.create_code(FINQ(self.children).map(lambda v: v.to_tree_node(builder)).to_list())

    def __repr__(self):
        return FINQ(self.children).map(repr).join_str('; ')

    def create_tree_list(self, builder: TreeBuilder):
        return FINQ(self.children).map(lambda ctx: ctx.to_tree_node(builder)).to_list()
