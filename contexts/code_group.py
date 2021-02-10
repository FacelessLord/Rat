from contexts.context import Context
from contexts.types import ContextType
from finq import FINQ
from tree.builder import TreeBuilder
from tree.node import TreeNode


class CodeGroupContext(Context):
    def to_tree_node(self, builder: TreeBuilder) -> TreeNode:
        return builder.create_code_group_node(FINQ(self.children)
                                              .map(lambda e: e.to_tree_node(builder))
                                              .to_list())

    @staticmethod
    def get_type():
        return ContextType.code_group
