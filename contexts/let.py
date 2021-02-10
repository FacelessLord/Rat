from tree.node import TreeNode
from contexts.generic_context import Context
from contexts.types import ContextType
from finq import FINQ

type_func = 'Function'
type_var = 'Variable'


class LetContext(Context):
    state = 1
    type = type_var
    modifiers = None

    def __init__(self):
        super().__init__()
        self.modifiers = []

    @staticmethod
    def get_type():
        return ContextType.let

    def to_tree_node(self, builder) -> TreeNode:
        if self.type == type_var:
            return builder.create_let_variable(self.children[0].to_tree_node(builder),
                                               self.children[1].to_tree_node(builder))
        elif self.type == type_func:
            return builder.create_let_func_node(self.modifiers,
                                                self.children[0].to_tree_node(builder),
                                                FINQ(self.children[1].children)
                                                .map(lambda v: v.to_tree_node(builder))
                                                .to_list(),
                                                self.children[2].to_tree_node(builder))

    def collect(self, ctx: "Context"):
        if self.type == type_var:
            if self.state == 1:
                if ctx.get_type() == ContextType.variable:
                    super(LetContext, self).collect(ctx)
                    self.state += 1
                else:
                    raise ValueError(f"Expected VarContext, got {ctx}")
            elif self.state == 3:
                super(LetContext, self).collect(ctx)
                self.state += 1
            else:
                raise ValueError(f"Error parsing let variable at {self.state}-th child '{ctx}'")
        elif self.type == type_func:
            if self.state == 2:
                if ctx.get_type() == ContextType.variable:
                    super(LetContext, self).collect(ctx)
                    self.state += 1
                else:
                    raise ValueError(f"Function name have to be valid Id, not {ctx}")
            elif self.state == 3:
                if ctx.get_type() == ContextType.group:
                    super(LetContext, self).collect(ctx)
                    self.state += 1
                else:
                    raise ValueError(f"Function args have to be defined \n{ctx}")
            elif self.state == 5:
                super(LetContext, self).collect(ctx)
                self.state += 1

    def __repr__(self):
        if self.type == type_var:
            return "let" + ' '.join([''] + self.modifiers) + (' fn ' if self.type == type_func else ' ') \
                   + repr(self.children[0]) + (' => ' if self.type == type_func else ' = ') + repr(self.children[1])
        if self.type == type_func:
            return "let" + ' '.join([''] + self.modifiers) + (' fn ' if self.type == type_func else ' ') \
                   + repr(self.children[0]) + repr(self.children[1]) + (
                       ' => ' if self.type == type_func else ' = ') + repr(self.children[2])
