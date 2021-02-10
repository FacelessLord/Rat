from typing import List, Dict

from Logger import warn
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode
from tree.variable import VariableNode


class LetFunctionNode(TreeNode):
    def __init__(self, modifiers: List[str], func_args: List[TreeNode]):
        super().__init__()
        self.func_args = func_args
        self.modifiers = modifiers

    def interpret(self, variable_storage: VariableStorage):
        # give variable storage in interpretation stage
        variable: VariableNode = self.children[0]

        def func(sub_variable_storage: VariableStorage):
            return self.children[1].interpret(sub_variable_storage)

        func.func_args = self.func_args
        func.func_modifiers = self.modifiers
        variable.initialize(variable_storage, func)

        return func
