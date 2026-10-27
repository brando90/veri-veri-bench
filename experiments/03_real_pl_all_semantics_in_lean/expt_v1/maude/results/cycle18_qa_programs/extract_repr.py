#!/usr/bin/env python3
"""QA18 helper: like extract_out.py but renders listV / tupV / dictV values
(as printed by print(container)) the way CPython's print would."""
import re
import sys

TOK = re.compile(r'\s*("(?:\\.|[^"\\])*"|-?\d+|[A-Za-z_][A-Za-z0-9_]*|::|[(),-])')


def tokenize(s):
    pos, out = 0, []
    s = s.strip()
    while pos < len(s):
        m = TOK.match(s, pos)
        if not m:
            raise ValueError("bad token at " + s[pos:pos + 30])
        out.append(m.group(1))
        pos = m.end()
    return out


class P:
    def __init__(self, toks):
        self.t, self.i = toks, 0

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None

    def eat(self, x=None):
        v = self.t[self.i]
        if x is not None and v != x:
            raise ValueError(f"expected {x} got {v}")
        self.i += 1
        return v

    def val(self):
        tk = self.eat()
        if tk.startswith('"'):
            inner = tk[1:-1]
            return ("str", inner.replace('\\\\', '\x00').replace('\\"', '"')
                    .replace('\\n', '\n').replace('\\t', '\t').replace('\x00', '\\'))
        if re.fullmatch(r"-?\d+", tk):
            return ("int", int(tk))
        if tk == "(":
            v = self.val()
            self.eat(")")
            return v
        if tk == "-":
            k, v = self.val()
            return ("int", -v)
        if tk in ("true", "false"):
            return ("bool", tk == "true")
        if tk == "none":
            return ("none", None)
        if tk in ("nil", "nilD"):
            return (tk, None)
        # constructor application
        args = []
        if self.peek() == "(":
            self.eat("(")
            args.append(self.val())
            while self.peek() == ",":
                self.eat(",")
                args.append(self.val())
            self.eat(")")
        return (tk, args)


def flat(v):
    out = []
    while v[0] == "cons":
        out.append(v[1][0])
        v = v[1][1]
    return out


def flatd(v):
    out = []
    while v[0] == "consD":
        out.append((v[1][0], v[1][1]))
        v = v[1][2]
    return out


def rep(v, top):
    k, x = v
    if k == "str":
        return x if top else repr(x)
    if k == "int":
        return str(x)
    if k == "bool":
        return "True" if x else "False"
    if k == "none":
        return "None"
    if k == "listV":
        return "[" + ", ".join(rep(e, False) for e in flat(x[0])) + "]"
    if k == "tupV":
        es = [rep(e, False) for e in flat(x[0])]
        return "(" + es[0] + ",)" if len(es) == 1 else "(" + ", ".join(es) + ")"
    if k == "dictV":
        return "{" + ", ".join(rep(a, False) + ": " + rep(b, False) for a, b in flatd(x[0])) + "}"
    if k == "ref":
        return "[...]"
    return "<" + k + ">"


def main():
    raw = sys.stdin.read()
    m = re.search(r"^result\s+\S+\s*:\s*(?P<term>.+?)(?=^[^ \t])", raw, re.M | re.S)
    if not m:
        return 2
    term = re.sub(r"\s+", " ", m.group("term").strip())
    if not (term.startswith("<") and term.endswith(">")):
        return 3
    inside = term[1:-1].strip()
    depth, split = 0, -1
    instr = False
    for i, ch in enumerate(inside):
        if ch == '"' and (i == 0 or inside[i - 1] != "\\"):
            instr = not instr
        if instr:
            continue
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        elif ch == "," and depth == 0:
            split = i
            break
    if split == -1:
        return 0
    out_str = inside[split + 1:].strip()
    if out_str == ".Out":
        return 0
    p = P(tokenize(out_str))
    while p.peek() is not None:
        print(rep(p.val(), True))
        if p.peek() == "::":
            p.eat("::")
    return 0


if __name__ == "__main__":
    sys.exit(main())
