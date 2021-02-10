import math

import Parser
from Lexer import lexer
from sr_collections.variable import Variable
from sr_collections.variable_storage import VariableStorage
from tree.builder import TreeBuilder

with open('test.pat', 'rt') as f:
    program = ''.join(f.readlines())

tokens = lexer.get_tokens(program)
print(tokens)
builder = TreeBuilder()
variable_storage = VariableStorage({'\\Pi': Variable('\\Pi', math.pi), "\\e": Variable('\\E', math.e)})

tree = Parser.build_tree(tokens, builder)
tree.interpret(variable_storage)
