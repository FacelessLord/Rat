from contexts.generic_context import Context

from contexts.types import ContextType
from tree.node import TreeNode


class NumberContext(Context):
    def __init__(self, number: float):
        super().__init__()
        self.value = number

    @staticmethod
    def get_type():
        return ContextType.number

    def to_tree_node(self, builder) -> TreeNode:
        return builder.create_number(self.value)

    def __repr__(self):
        return f'{self.value}'
