from contexts.types import ContextType
from finq import FINQ
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode


class GroupNode(TreeNode):
    def interpret(self, variable_storage: VariableStorage):
        return FINQ(self.children).map(lambda c: c.interpret(variable_storage)).to_list()

    @staticmethod
    def get_type():
        return ContextType.group
