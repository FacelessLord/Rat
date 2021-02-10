from Lexer import Rule
from contexts.generic_context import Context
from contexts.types import ContextType
from tree.node import TreeNode

mapping = {
    'int': Rule.int,
    'float': Rule.float,
    'str': Rule.str,
    'type': Rule.type,
    'input': Rule.input,
    'print': Rule.print,
    'cos': Rule.cos,
    'sin': Rule.sin,
    'tan': Rule.tan,
    'cot': Rule.cot,
    'exp': Rule.exp,
    'ln': Rule.ln}


class FuncContext(Context):
    def __init__(self, func_name: str):
        super().__init__()
        self.func_name = func_name

    @staticmethod
    def get_type():
        return ContextType.function

    def __repr__(self):
        return f"{self.func_name}({self.children[0]})"

    def to_tree_node(self, builder) -> TreeNode:
        return builder.create_function(mapping[self.func_name], self.children[0].to_tree_node(builder))
