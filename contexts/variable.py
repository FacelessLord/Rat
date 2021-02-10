from contexts.generic_context import Context
from tree.builder import TreeBuilder

from tree.node import TreeNode
from contexts.types import ContextType


class VarContext(Context):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @staticmethod
    def get_type():
        return ContextType.variable

    def to_tree_node(self, builder: TreeBuilder) -> TreeNode:
        return builder.create_variable(self.name)

    def __repr__(self):
        return f'var_{self.name}'
