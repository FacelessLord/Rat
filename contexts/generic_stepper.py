from typing import Tuple

from Lexer import Rule
from Logger import warn, err
from contexts.generic_context import Context
from contexts.types import ContextType
from contexts.factories import create_ctx


def generic_stepper(self: Context, token: Tuple[str, Rule]) -> Tuple[Context, bool]:
    if token[1] == Rule.lparen:
        ctx = create_ctx(ContextType.group)
        self.collect(ctx)
        return ctx, True
    if token[1] == Rule.lbrace:
        ctx = create_ctx(ContextType.code_group)
        self.collect(ctx)
        return ctx, True
    elif token[1] == Rule.alg_expr:
        ctx = create_ctx(ContextType.algebraic_expression)
        self.collect(ctx)
        return ctx, True
    elif token[1] == Rule.number:
        ctx = create_ctx(ContextType.number, float(token[0]))
        self.collect(ctx)
        return self, True
    elif token[1] == Rule.string:
        ctx = create_ctx(ContextType.string, token[0][1:-1])
        self.collect(ctx)
        return self, True
    elif token[1] == Rule.var:
        ctx = create_ctx(ContextType.variable, token[0])
        self.collect(ctx)
        return ctx, True
    elif token[1] == Rule.let:
        ctx = create_ctx(ContextType.let)
        self.collect(ctx)
        return ctx, True
    elif token[1] == Rule.comma:
        self.set_position_empty()
        return self, True
    elif token[1] in built_in_pref_funcs:
        ctx = create_ctx(ContextType.function, token[0])
        self.collect(ctx)
        return ctx, True
    elif token[1] in built_in_operations:
        if self.get_type() != ContextType.algebraic_expression:
            err(f"Can't use binary operations outside of algebraic expression. Error occurred near '{token[0]}'")
            exit()
        ctx = create_ctx(ContextType.binary_operation, token[1])
        self.collect(ctx)
        return self, True
    elif token[1] in [Rule.rparen, Rule.rbrace]:
        return self.parent, True
    elif token[1] == Rule.EOF:
        if self.get_type() != ContextType.general:
            return self.parent, False
        return self, True
    if token[1] not in [Rule.comment]:
        warn(f"Hang token '{token}'")
    return self, True


built_in_pref_funcs = [Rule.int, Rule.float, Rule.str, Rule.type, Rule.input, Rule.print, Rule.cos, Rule.sin, Rule.tan,
                       Rule.cot, Rule.ln, Rule.exp]
built_in_operations = [Rule.plus, Rule.minus, Rule.mult, Rule.div, Rule.pow]
