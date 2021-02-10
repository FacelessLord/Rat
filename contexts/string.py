from contexts.generic_context import Context

from contexts.types import ContextType
from tree.builder import TreeBuilder
from tree.node import TreeNode


class StringContext(Context):
    def __init__(self, text: str):
        super().__init__()
        self.value = text

    @staticmethod
    def get_type():
        return ContextType.number

    def to_tree_node(self, builder: TreeBuilder) -> TreeNode:
        return builder.create_string(self.value)

    def __repr__(self):
        return f'"{self.value}"'
