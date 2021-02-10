from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode


class CodeGroupNode(TreeNode):
    def interpret(self, variable_storage: VariableStorage):
        result = None
        sub_storage = variable_storage.sub_storage()
        for instruction in self.children:
            result = instruction.interpret(sub_storage)
        return result
