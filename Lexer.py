import re
from typing import List, Tuple

from Rules import Rule, rules
from finq import FINQ


class Lexer:
    def __init__(self, regexps: List[Tuple[re.Pattern, str]]):
        self.regexps = regexps

    def _lex(self, text: str):
        text += ' '
        while len(text) > 0:
            for rexp in self.regexps:
                match = rexp[0].match(text)
                if match:
                    yield match.group(1), rexp[1]
                    text = text[len(match.group(1)):]
                    break
            else:
                yield text[0], Rule.unknown
                text = text[1:]
        yield text, Rule.EOF

    def get_tokens(self, text: str):
        return FINQ(lexer._lex(text)).filter(lambda t: t[1] != Rule.space).to_list()


lexer = Lexer(rules)
