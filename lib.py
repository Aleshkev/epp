from typing import *
import re
import dataclasses
import enum


class TokenType(enum.Enum):
    operator = enum.auto()
    directive_begin = enum.auto()
    word = enum.auto()
    error = enum.auto()


@dataclasses.dataclass
class Token:
    lexeme: str = ""
    type: TokenType = TokenType.operator
    had_space_before: bool = False
    containing_directive: Optional[str] = None

    previous: Optional["Token"] = None

    def __repr__(self):
        return (f"{self.lexeme!r} as {self.type.name}" + (f" in #{self.containing_directive}" if
                                                          self.containing_directive else "") +
                f", after <{self.previous.type.name if self.previous else None}>")


def any_of(l):
    return re.compile("(" + "|".join(re.escape(s) for s in l) + ")")


Re = type(re.compile(""))


def tokenize(s: str, raise_errors: bool = True):
    s = "\n" + s + "\n"
    s = re.sub(r"\t+", " ", s)
    s = re.sub(r"\\\n", "", s, re.DOTALL)
    s = re.sub(r"\n +", "\n", s)

    i, n = 0, len(s)

    tokens: List[Token] = []

    def try_eat(e: Re, token_type: Optional[TokenType] = None,
                lexeme_group=0, custom_finalizer=None):
        """Tries to eat a token matching the expression, appends it and moves cursor if successful."""
        nonlocal i
        m = e.search(s, i, i + 2048)
        if not m or m.start(0) != i:
            return False
        if token_type is not None:
            tokens.append(Token(m.group(lexeme_group), token_type, s[i - 1] in " \n"))
        i = m.end(0)
        if custom_finalizer is not None:
            custom_finalizer(m)
        return True

    while i < n:
        # Whitespace, comments.
        if try_eat(re.compile(r"[ \n]+")): continue
        if try_eat(re.compile(r"//.*")): continue
        if try_eat(re.compile(r"/\*.*?\*/", re.DOTALL)): continue

        # # Preprocessor directives.
        if s[i - 1] == "\n":
            def finalize(m):
                j = len(tokens) - 1
                tokens.extend(tokenize(m.group(2)))
                for token in tokens[j:]:
                    token.containing_directive = m.group(1)[1:].lstrip()

            if try_eat(re.compile(r"(# *[a-zA-Z]*)(.*)"), TokenType.directive_begin, lexeme_group=1,
                       custom_finalizer=finalize): continue

        # Generic identifiers and numbers.
        if try_eat(re.compile(r"\.?(\d\.|\w)+"), TokenType.word): continue

        # Operators.
        short_operators = any_of("()[].!~*&/%<>^|?:=,;!@#$%^&*()-+=[]{};:,.<>/?~")
        long_operators = any_of(["->", "++", "--", "<<", ">>", "<=", ">=", "==", "!=", "&&", "||", "+=", "-=",
                                 "*=", "/=", "%=", "&=", "^=", "|=", "...", "##", "::"])
        if try_eat(long_operators, TokenType.operator): continue  # Always prefer longer operator.
        if try_eat(short_operators, TokenType.operator): continue

        # String and character literals.
        string = r'"(\\\\|\\"|[^\n"])*"\w*'
        if try_eat(re.compile(string), TokenType.word): continue
        if try_eat(re.compile(string.replace('"', "'")), TokenType.word): continue

        if raise_errors:
            raise SyntaxError(f"Error while parsing at {i} at: {s[i:i + 64]}")
        else:
            try_eat(re.compile(".", re.DOTALL), TokenType.error)

    tokens = set_previous_infos(tokens)

    return tokens


def set_previous_infos(tokens: List[Token]):
    for i, token in enumerate(tokens):
        token.previous = tokens[i - 1] if i > 0 else None
    return tokens


def serialize(tokens: List[Token]):
    def is_after_directive(token: Token):
        return token.containing_directive is None and token.previous.containing_directive is not None

    def requires_newline(token: Token):
        return is_after_directive(token) or token.type == TokenType.directive_begin

    def requires_space(token: Token):
        # This is terrible. Please send help.
        return ((token.type == TokenType.word and token.previous.type != TokenType.operator) or
                (token.type == TokenType.operator and token.lexeme[0] == token.previous.lexeme[-1] and
                 len(token.lexeme) >= len(token.previous.lexeme)) or
                (token.previous.type == TokenType.directive_begin) or
                (token.previous.previous is not None and token.previous.previous.type == TokenType.directive_begin and
                 token.containing_directive == "define" and token.had_space_before))

    s = [tokens[0].lexeme]
    for current_token in tokens[1:]:
        if requires_newline(current_token):
            s.append("\n")
        elif requires_space(current_token):
            s.append(" ")
        s.append(current_token.lexeme)
    return "".join(s).strip()


def rename_tokens(tokens: List[Token], operators: bool = False):
    def should_be_renamed(token):
        if token.type == TokenType.word:
            return token.containing_directive is None
        if operators and token.type == TokenType.operator and not token.containing_directive:
            return True
        return False

    originals = sorted(list(set(token.lexeme for token in tokens if should_be_renamed(token))))
    replacements = [f"var_{i}" for i, original in enumerate(originals)]
    original_to_replacement = {original: replacement for original, replacement in zip(originals, replacements)}

    defines = tokenize("\n".join(f"#define {renamed} {original}" for original, renamed in zip(originals, replacements)))
    tokens = set_previous_infos(tokens)

    for i, token in enumerate(tokens):
        if should_be_renamed(token):
            tokens[i] = Token(original_to_replacement[token.lexeme], TokenType.word, token.had_space_before,
                              token.containing_directive, token.previous)
            if i + 1 < len(tokens):
                tokens[i + 1].previous = tokens[i]

    return defines + tokens
