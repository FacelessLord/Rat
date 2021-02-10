from contexts.types import ContextType
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode


class NumberNode(TreeNode):
    def __init__(self, number: float):
        super().__init__()
        self.value = number

    def interpret(self, variable_storage: VariableStorage):
        return self.value

    @staticmethod
    def get_type():
        return ContextType.number
