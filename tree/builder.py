from typing import List, Any, Dict, Union

from Lexer import Rule
from sr_collections.variable import Variable
from sr_collections.variable_storage import VariableStorage
from tree.algebraic_expression import AlgebraicExpressionNode
from tree.binary_expression import BinaryExpressionNode
from tree.code import CodeNode
from tree.code_group import CodeGroupNode
from tree.function import FunctionNode
from tree.group import GroupNode
from tree.let_func import LetFunctionNode
from tree.let_variable import LetVariableNode
from tree.node import TreeNode
from tree.number import NumberNode
from tree.string import StringNode
from tree.var_func import VarFunctionNode
from tree.variable import VariableNode


# noinspection PyMethodMayBeStatic
class TreeBuilder:
    def create_variable(self, name: str):
        return VariableNode(name)

    def create_function(self, name: Rule, arg):
        node = FunctionNode(name)
        node.children = [arg]
        return node

    def create_number(self, value: float):
        return NumberNode(value)

    def create_string(self, value: str):
        return StringNode(value)

    def create_let_variable(self, variable: TreeNode, value: TreeNode):
        node = LetVariableNode()
        node.children = [variable, value]
        return node

    def create_binary_expression(self, operation: Rule):
        return BinaryExpressionNode(operation)

    def create_algebraic_expression(self, operands: List[TreeNode]):
        node = AlgebraicExpressionNode()
        node.children = operands
        return node

    def create_group_node(self, elements: List[TreeNode]):
        node = GroupNode()
        node.children = elements
        return node

    def create_code_group_node(self, elements: List[TreeNode]):
        node = CodeGroupNode()
        node.children = elements
        return node

    def create_let_func_node(self, modifiers: List[str], func_var: TreeNode, func_args: List[TreeNode], code: TreeNode):
        node = LetFunctionNode(modifiers, func_args)
        node.children = [func_var, code]
        return node

    def create_var_function(self, func_var: TreeNode, args: TreeNode):
        node = VarFunctionNode()
        node.children = [func_var, args]
        return node

    def create_code(self, children: List[TreeNode]):
        node = CodeNode()
        node.children = children
        return node
