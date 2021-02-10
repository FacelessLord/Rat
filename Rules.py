import re
from enum import Enum

from finq import FINQ, First


class Rule(Enum):
    # types
    number = 'number'
    string = 'string'

    # operations
    plus = 'plus'
    minus = 'minus'
    mult = 'mult'
    div = 'div'
    pow = 'pow'

    # builtin functions
    int = 'int'
    float = 'float'
    str = 'str'
    type = 'type'
    input = 'input'
    print = 'print'
    cos = 'cos'
    sin = 'sin'
    tan = 'tan'
    cot = 'cot'
    exp = 'exp'
    ln = 'ln'
    fact = 'fact'

    # common
    var = 'var'
    unknown = 'unknown'
    alg_expr = 'alg_expr'

    # control characters
    then = 'then'
    catch = 'catch'
    arrow = 'arrow'
    eq = 'eq'
    comment = 'comment'
    lparen = 'lparen'
    rparen = 'rparen'
    lbrace = 'lbrace'
    rbrace = 'rbrace'
    space = 'space'
    comma = 'comma'
    semicolon = 'semicolon'
    line_break = 'line_break'
    EOF = 'EOF'

    # keywords
    let = 'let'
    fn = 'fn'
    mut = 'mut'
    parallel = 'parallel'
    pure = 'pure'


def literal_rule(literal: Rule):
    return re.compile(f'({literal.value})'), literal


# types
re_number = re.compile('(-?((\d*(\.\d+))|(\d+)))'), Rule.number
re_string = re.compile('^(?=")("(.*?[^\\\\]|)(\\\\\\\\)*?(?=")")'), Rule.string

type_rules = [re_number, re_string]

# operations
re_plus = re.compile('(\\+)'), Rule.plus
re_minus = re.compile('(-)'), Rule.minus
re_mult = re.compile('(\\*)'), Rule.mult
re_div = re.compile('(/)'), Rule.div
re_power = re.compile('(\\^)'), Rule.pow

operation_rules = [re_plus, re_minus, re_mult, re_div, re_power]

# builtin functions
re_int = literal_rule(Rule.int)
re_float = literal_rule(Rule.float)
re_str = literal_rule(Rule.str)
re_type = literal_rule(Rule.type)
re_input = literal_rule(Rule.input)
re_print = literal_rule(Rule.print)
re_cos = literal_rule(Rule.cos)
re_sin = literal_rule(Rule.sin)
re_tan = literal_rule(Rule.tan)
re_cot = literal_rule(Rule.cot)
re_exp = literal_rule(Rule.exp)
re_ln = literal_rule(Rule.ln)
re_fact = re.compile('(!)'), Rule.fact

math_function_rules = [re_int, re_float, re_str, re_type, re_input, re_print, re_cos, re_sin, re_tan, re_cot, re_exp,
                       re_ln, re_fact]

# common
re_var = re.compile('((\\\\)?[a-zA-Z][a-zA-Z0-9_]*)'), Rule.var
re_alg_expr = re.compile('(\\$\\()'), Rule.alg_expr
common_rules = [re_var, re_alg_expr]

# control characters
re_then = re.compile('(&)'), Rule.then
re_catch = re.compile('(\\|)'), Rule.catch
re_arrow = re.compile('(=>)'), Rule.arrow
re_eq = re.compile('(=)'), Rule.eq
re_comment = re.compile('^(#.*)$'), Rule.comment
re_lparen = re.compile('(\\()'), Rule.lparen
re_rparen = re.compile('(\\))'), Rule.rparen
re_lbrace = re.compile('({)'), Rule.lbrace
re_rbrace = re.compile('(})'), Rule.rbrace
re_space = re.compile('(\\s|$)', re.MULTILINE), Rule.space
re_comma = re.compile('(,)'), Rule.comma
re_semicolon = re.compile('(;)'), Rule.semicolon
re_line_break = re.compile('(\n)'), Rule.line_break
re_eof = re.compile('(\0)'), Rule.EOF

control_character_rules = [re_then, re_catch, re_arrow, re_eq, re_comment, re_lparen, re_rparen, re_lbrace, re_rbrace,
                           re_space, re_comma, re_semicolon, re_line_break, re_eof]

# keywords
keywords = [Rule.let, Rule.fn, Rule.mut, Rule.parallel, Rule.pure]
keyword_rules = FINQ(keywords).map(literal_rule).to_list()

rules = [*control_character_rules,
         *keyword_rules,
         *math_function_rules,
         *common_rules,
         *type_rules,
         *operation_rules]
