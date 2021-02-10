import math

from Lexer import Rule
from contexts.types import ContextType
from finq import FINQ
from sr_collections.variable_storage import VariableStorage
from tree.node import TreeNode
from tree.variable import VariableNode


def printf(*t):
    d = FINQ(t)
    print(">", *d)


mapping = {
    Rule.int: int,
    Rule.float: float,
    Rule.str: str,
    Rule.type: lambda o: str(type(o)),
    Rule.input: input, Rule.print: printf,
    Rule.cos: math.cos, Rule.sin: math.sin, Rule.tan: math.tan,
    Rule.cot: lambda x: 1 / math.tan(x), Rule.ln: math.log, Rule.exp: math.exp
}


class FunctionNode(TreeNode):
    def __init__(self, name: Rule):
        super().__init__()
        self.name = name

    def interpret(self, variable_storage: VariableStorage):
        arg = self.children[0].interpret(variable_storage)
        if self.name in mapping:
            if self.children[0].get_type() == ContextType.group:
                return mapping[self.name](*arg)
            return mapping[self.name](arg)
        raise ValueError(f"Function '{self.name}' doesn't exist")

    @staticmethod
    def get_type():
        return ContextType.function
