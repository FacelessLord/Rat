from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode


class CodeNode(TreeNode):
    def interpret(self, variable_storage: VariableStorage):
        result = None
        for c in self.children:
            result = c.interpret(variable_storage)
        return result
