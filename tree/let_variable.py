from typing import Dict

from contexts.types import ContextType
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode
from tree.variable import VariableNode


class LetVariableNode(TreeNode):
    def __init__(self):
        super().__init__()

    def interpret(self, variable_storage: VariableStorage):
        value = self.children[1].interpret(variable_storage)
        variable: VariableNode = self.children[0]

        if self.children[1].get_type() == ContextType.group:
            if len(value) == 1:
                variable.initialize(variable_storage, value[0])
                return value[0]

        variable.initialize(variable_storage, value)
        return value

    @staticmethod
    def get_type():
        return ContextType.let
