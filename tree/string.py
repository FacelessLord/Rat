from contexts.types import ContextType
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode


class StringNode(TreeNode):
    def __init__(self, text: str):
        super().__init__()
        self.value = text

    def interpret(self, variable_storage: VariableStorage):
        vs = self.value.replace('\\"', '"')
        return vs

    @staticmethod
    def get_type():
        return ContextType.string
