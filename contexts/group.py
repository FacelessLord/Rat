from finq import FINQ
from tree.node import TreeNode
from contexts.generic_context import Context
from contexts.types import ContextType


class GroupContext(Context):
    def __init__(self):
        super().__init__()
        self.track_commas = True

    @staticmethod
    def get_type():
        return ContextType.group

    def to_tree_node(self, builder) -> TreeNode:
        children_nodes = FINQ(self.children).map(lambda ctx: ctx.to_tree_node(builder)).to_list()
        return builder.create_group_node(children_nodes)
