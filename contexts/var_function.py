from contexts.context import Context
from contexts.types import ContextType
from finq import FINQ
from tree.builder import TreeBuilder
from tree.node import TreeNode


class VarFunctionContext(Context):
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_type() -> ContextType:
        return ContextType.varFunction

    def to_tree_node(self, builder: TreeBuilder) -> TreeNode:
        return builder.create_var_function(self.children[0].to_tree_node(builder),
                                           self.children[1].to_tree_node(builder))

    def __repr__(self):
        return f"{repr(self.children[0])}{repr(self.children[1])}"
