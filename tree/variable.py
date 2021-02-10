from contexts.types import ContextType
from sr_collections.variable import Variable
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode


class VariableNode(TreeNode):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def interpret(self, variable_storage: VariableStorage):
        if variable_storage.variable_bound(self.name):
            a = self.get(variable_storage)
            return a

    def initialize(self, variable_storage: VariableStorage, value):
        variable_storage.create_variable(self.name, value)

    def set(self, variable_storage: VariableStorage, value):
        variable_storage.set_value(self.name, value)

    def get(self, variable_storage: VariableStorage):
        a = variable_storage.get_value(self.name)
        return a

    @staticmethod
    def get_type():
        return ContextType.variable
