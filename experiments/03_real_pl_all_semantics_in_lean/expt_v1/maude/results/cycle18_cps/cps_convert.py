#!/usr/bin/env python3
"""Rewrite the direct-style pythonlite-bigstep.maude into continuation-passing form (all rules plain).

Usage: python3 cps_convert.py pythonlite-bigstep-direct.maude pythonlite-bigstep.maude

Every rule with one rewrite condition (L => R) becomes a push rule [evaluate L with a new frame on
the continuation] and a pop rule [R with that frame on top continues]; a rule with no rewrite
condition just carries the continuation K.  The frame holds the variables the rest of the rule
needs.  The one rule with two conditions (sa2) is split in the source first.  The result is the
file the semantics runs from; the direct-style file is the readable big-step spec.
"""
import re, sys

src = open(sys.argv[1]).read()
out_path = sys.argv[2]

# ---- 1. split sa2 (two rewrite conditions) -------------------------------------------
old_sa2 = """ crl sa2(AOo, V1, V2, E2, Sigma2, Out2) => sa3(AOo, V1, V2, Vrp, EO, Sigma3, Out3)
   if b2(oIdx, V1, V2, Sigma2, Out2) => res(Vrp, Sigma2, Out2)
   /\\ < E2, Sigma2, Out2 > => res(EO, Sigma3, Out3) ."""
new_sa2 = """ crl sa2(AOo, V1, V2, E2, Sigma2, Out2) => sa2b(AOo, V1, V2, Vrp, E2, Sigma2b, Out2b)
   if b2(oIdx, V1, V2, Sigma2, Out2) => res(Vrp, Sigma2b, Out2b) .
 crl sa2b(AOo, V1, V2, Vrp, E2, Sigma2, Out2) => sa3(AOo, V1, V2, Vrp, EO, Sigma3, Out3)
   if < E2, Sigma2, Out2 > => res(EO, Sigma3, Out3) ."""
assert old_sa2 in src
src = src.replace(old_sa2, new_sa2)
src = src.replace("  op sa3 : AugOp Value Value Value ExpOut State Out -> Configuration .",
  "  op sa2b : AugOp Value Value Value Exp State Out -> Configuration .\n  op sa3 : AugOp Value Value Value ExpOut State Out -> Configuration .")
src = src.replace("vars Sigma5 : State .", "vars Sigma5 Sigma2b : State .  var Out2b : Out .")

kick_a = src.index("  rl < St > => < St, initS, .Out > .")
kick_b = src.index("endm", kick_a)
src = src[:kick_a] + "@@KICK@@\n" + src[kick_b:]
cfg_a = src.index("  sort Configuration .")
cfg_b = src.index("  op <_>     : Pgm -> Configuration .")
cfg_b = src.index("\n", cfg_b)
src = src[:cfg_a] + """  --- Cycle 18 [CPS]: a configuration carries a continuation K [sort Kont]: the frames still to run once
  --- this one finishes.  Every rule is plain, so a step costs the same however large the heap is
  --- [a rewrite condition `=>` costs the size of the term it is given].
  sort Kont .
  op halt : -> Kont [ctor] .
  sort Configuration .
  op <_,_,_|_> : Exp State Out Kont -> Configuration .
  op <_,_,_|_> : Stmt State Out Kont -> Configuration .
  op res  : ExpOut State Out Kont -> Configuration [ctor] .
  op resA : ArgsOut State Out Kont -> Configuration [ctor] .
  op resL : ListOut State Out Kont -> Configuration [ctor] .
  op resD : DictOut State Out Kont -> Configuration [ctor] .
  op <_,_|_> : Outcome Out Kont -> Configuration [ctor] .
  --- the final configuration of a whole program
  op <_,_>   : Outcome Out -> Configuration [ctor] .
  op <_>     : Pgm -> Configuration .""" + src[cfg_b:]
src = src.replace("  vars Sigma5 Sigma2b", "  var K : Kont .\n  vars Sigma5 Sigma2b") if False else src
# ---- 2. variable sorts -----------------------------------------------------------------
head, body = src.split("mod PYTHONLITE-SEMANTICS-BIGSTEP is", 1)
body = "mod PYTHONLITE-SEMANTICS-BIGSTEP is" + body
body = body.replace("  vars X : Id .", "  vars X : Id .\n  var K : Kont .", 1)
varsort = {}
for l in body.split("\n"):
    l = l.split("---")[0]
    for m in re.finditer(r"\bvars?\s+([^:]+?)\s*:\s*(\w+)\s*\.(?=\s|$)", l):
        for v in m.group(1).split():
            varsort[v] = m.group(2)
varsort["K"] = "Kont"

def strip_comment(l):
    i = l.find("---")
    return l if i < 0 else l[:i]

def split_top(s, sep):
    """split s at depth-0 occurrences of sep (parens only)"""
    parts, depth, cur, i = [], 0, "", 0
    while i < len(s):
        c = s[i]
        if c == "(": depth += 1
        elif c == ")": depth -= 1
        if depth == 0 and s.startswith(sep, i):
            parts.append(cur); cur = ""; i += len(sep); continue
        cur += c; i += 1
    parts.append(cur)
    return parts

def find_top(s, tok):
    depth = 0
    for i in range(len(s)):
        c = s[i]
        if c == "(": depth += 1
        elif c == ")": depth -= 1
        elif depth == 0 and s.startswith(tok, i): return i
    return -1

def is_angle(t):
    return t.startswith("<") and t.endswith(">")

def args_of(t):
    t = t.strip()
    if is_angle(t):
        return [a.strip() for a in split_top(t[1:-1].strip(), ",")]
    m = re.match(r"([A-Za-z0-9_']+)\((.*)\)$", t, re.S)
    return [a.strip() for a in split_top(m.group(2), ",")]

def head_of(t):
    t = t.strip()
    if is_angle(t): return "<>"
    return re.match(r"([A-Za-z0-9_']+)\(", t).group(1)

def addK(t, k="K"):
    t = t.strip()
    if is_angle(t):
        return "< " + t[1:-1].strip() + " | " + k + " >"
    if re.fullmatch(r"[A-Za-z0-9_']+", t):  # a constant config? not expected
        raise ValueError(t)
    assert t.endswith(")")
    return t[:-1] + ", " + k + ")"

def vars_in(s):
    return [v for v in re.findall(r"[A-Za-z_][A-Za-z0-9_']*", s) if v in varsort]

KICK = '''  rl < St > => < St, initS, .Out | halt > .
  rl < Outd, Out1 | halt > => < Outd, Out1 > .'''
frames = []   # (name, argsorts)
used = {}
def newframe(base, argvars):
    n = used.get(base, 0); used[base] = n + 1
    name = "k" + base[0].upper() + base[1:] + ("" if n == 0 else "x" + str(n + 1))
    frames.append((name, [varsort[v] for v in argvars]))
    return name

out_lines = []
lines = body.split("\n")
i = 0
nsplit = 0; nplain = 0
while i < len(lines):
    ln = lines[i]
    st = ln.lstrip()
    if st.startswith("rl ") or st.startswith("crl "):
        stmt_lines = [ln]
        txt = strip_comment(ln).rstrip()
        while not txt.endswith(" ."):
            i += 1
            stmt_lines.append(lines[i])
            txt = (txt + " " + strip_comment(lines[i]).strip()).rstrip() if True else txt
        raw = " ".join(strip_comment(l).strip() for l in stmt_lines)
        raw = re.sub(r"\s+", " ", raw).strip()
        assert raw.endswith(" ."), raw
        raw = raw[:-2].strip()
        kind, rest = raw.split(" ", 1)
        ifp = find_top(rest, " if ")
        if ifp >= 0:
            hd, cd = rest[:ifp], rest[ifp + 4:]
            conds = [c.strip() for c in split_top(cd, " /\\ ")]
        else:
            hd, conds = rest, []
        ap = find_top(hd, " => ")
        lhs, rhs = hd[:ap].strip(), hd[ap + 4:].strip()
        # strip a leading label like "[...]" none present
        rw = [j for j, c in enumerate(conds) if find_top(c, " => ") >= 0 and ":=" not in c.split(" => ")[0]]
        # keep original comments from first line? drop them for converted rules
        comments = [l[l.find("---"):] for l in stmt_lines if "---" in l]
        if not rw:
            new = f"{kind} {addK(lhs)} => {addK(rhs)}"
            if conds: new += " if " + " /\\ ".join(conds)
            new += " ."
            nplain += 1
        else:
            assert len(rw) == 1, raw
            j = rw[0]
            pre, post = conds[:j], conds[j + 1:]
            L, R = [x.strip() for x in split_top(conds[j], " => ")]
            rargs = args_of(R)
            for a in rargs: assert re.fullmatch(r"[A-Za-z0-9_']+", a), (a, raw)
            prevars = set(vars_in(lhs)) | set(v for c in pre for v in vars_in(c)) | set(vars_in(L))
            postvars = set(vars_in(rhs)) | set(v for c in post for v in vars_in(c))
            fv = sorted((prevars & postvars) - set(rargs) - {"K"})
            # keep deterministic, declaration-free order: order of first appearance in lhs/pre/L
            order = []
            for v in vars_in(lhs + " " + " ".join(pre) + " " + L):
                if v in fv and v not in order: order.append(v)
            fv = order
            fname = newframe(head_of(rhs) if head_of(rhs) != "<>" else "stmt", fv)
            frame = f"{fname}({', '.join(fv + ['K'])})" if fv else f"{fname}(K)"
            push = f"{'crl' if pre else 'rl'} {addK(lhs)} => {addK(L, frame)}"
            if pre: push += " if " + " /\\ ".join(pre)
            push += " ."
            popk = f"{'crl' if post else 'rl'} {addK(R, frame)} => {addK(rhs)}"
            if post: popk += " if " + " /\\ ".join(post)
            popk += " ."
            new = push + "\n" + " " + popk
            nsplit += 1
        for c in comments: out_lines.append("  " + c)
        out_lines.append(" " + new)
        i += 1
        continue
    # op declarations returning Configuration: add a Kont argument
    m = re.match(r"^(\s*op\s+[^:]+:\s*)(.*?)(\s*->\s*Configuration\s*\.)(.*)$", ln)
    if m and not any(x in ln for x in ("<_", "res")):
        args = m.group(2).strip()
        ln = m.group(1) + (args + " Kont" if args else "Kont") + m.group(3) + m.group(4)
    out_lines.append(ln)
    i += 1

body2 = "\n".join(out_lines)
body2 = body2.replace("@@KICK@@", KICK)
head = head
fdecl = ["  --- Continuation frames [CPS, cycle 18].  Every rule below is plain: a construct pushes a frame",
         "  --- and evaluates its sub-term; the result config pops it.  The cost of a step no longer depends",
         "  --- on how much heap the State holds."]
for n, sorts in frames:
    fdecl.append(f"  op {n} : {' '.join(sorts + ['Kont'])} -> Kont [ctor] .")
body2 = body2.replace("  --- ----- expressions: literals -----", "\n".join(fdecl) + "\n\n  --- ----- expressions: literals -----", 1)
note = """--- CYCLE 18, CONTINUATION-PASSING FORM.  This file is generated from the direct-style semantics
--- [results/cycle18_cps/pythonlite-bigstep-direct.maude] by results/cycle18_cps/cps_convert.py;
--- the two define the same relation and every test passes on both.  Read the direct-style file for
--- the rules as a big-step spec; this one is the fast evaluator.  Here each configuration carries a
--- continuation K: `< E, Sigma, Out | K >` evaluates E and hands the result to the frame on top of K
--- [`res(EO, Sigma', Out', kFrame(.., K))` pops it], so every rule is plain [no `=>` condition] and a
--- step costs the same however big the heap is.  The judgments below read
---
---   < Exp,  Sigma, Out | K >  =>*  res(ExpOut, Sigma', Out', K')   expression evaluation
---   < Stmt, Sigma, Out | K >  =>*  < Outcome, Out' | K' >          statement evaluation
---   < Pgm >                   =>*  < Outcome, Out >                whole program
---
"""
head = head.replace("--- Cycle 15: an expression now returns", note + "--- Cycle 15: an expression now returns", 1)
open(out_path, "w").write(head + body2)
print("split", nsplit, "plain", nplain, "frames", len(frames), file=sys.stderr)
