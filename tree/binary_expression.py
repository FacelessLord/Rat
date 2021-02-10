from Lexer import Rule
from contexts.types import ContextType
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode

mapping = {
    Rule.plus: "+",
    Rule.minus: "-",
    Rule.mult: "*",
    Rule.div: "/",
    Rule.pow: "**"
    }


class BinaryExpressionNode(TreeNode):
    def __init__(self, operation: Rule):
        super().__init__()
        self.operation = operation

    def interpret(self, variable_storage: VariableStorage):
        return mapping[self.operation]

    @staticmethod
    def get_type():
        return ContextType.binary_operation
