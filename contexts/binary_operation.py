from contexts.generic_context import Context

from Lexer import Rule
from tree.node import TreeNode
from contexts.types import ContextType


class BinaryOperationContext(Context):
    def __init__(self, operation: Rule):
        super().__init__()
        self.operation = operation

    @staticmethod
    def get_type():
        return ContextType.binary_operation

    def __repr__(self):
        return self.operation.value

    def to_tree_node(self, builder) -> TreeNode:
        return builder.create_binary_expression(self.operation)

