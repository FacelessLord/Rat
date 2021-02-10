from tree.node import TreeNode
from contexts.context import Context
from contexts.types import ContextType


class GenericContext(Context):
    def to_tree_node(self, builder) -> TreeNode:
        pass

    @staticmethod
    def get_type() -> ContextType:
        return ContextType.generic_context
