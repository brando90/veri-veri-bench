# pythonlite — Big-step semantics in Maude (CS522 framework)

**TLDR:** End-to-end implementation of `pythonlite` (a curated Python subset) as a CS522-style big-step / Kahn operational semantics in Maude. Includes a Python → Maude AST parser (`parse.py`), a CPython-vs-Maude differential test harness (`run_diff_test.sh`), and a 7-program test corpus under `tests/`. Current status: **7 / 7 corpus programs match CPython output exactly** (see `results/results_summary_<TS>.md`).

---

## How to run

```bash
cd experiments/03_real_pl_all_semantics_in_lean/expt_v1/maude
./run_diff_test.sh                     # runs every tests/*.py through both CPython
                                       # and the Maude semantics, diffs the outputs
maude -no-prelude -no-banner run_bigstep_tests.maude   # rewrites the hand-written
                                                       # test programs in pythonlite-programs.maude
```

## What's in this directory

| File / dir                         | What it is |
|------------------------------------|------------|
| `pythonlite-syntax.maude`          | AST: integer / boolean / identifier expressions; `+`, `-`, `*`, `//`, `%`, comparisons, short-circuit `and`/`or`/`not`; statements `pass`, `:=`, `print`, `;`, `ifelse`, `while`. Indentation desugared at parse time. |
| `pythonlite-state.maude`           | Variable state (`Id -> Int`) and output buffer (`Out` = list of `Int`). Lookup of unbound = `undefined` (operational analogue of `NameError`). |
| `pythonlite-bigstep.maude`         | Big-step / Kahn-style semantics: judgments `< E, σ, out > => < val, out' >`, `< S, σ, out > => < σ', out' >`, `< Pgm > => < σ, out >`. Output buffer threading mirrors HW3 IMP++. Floor-division & floor-mod (Python semantics, not Maude's truncating ones) defined in `PYTHONLITE-FLOORDIV`. Short-circuit `and`/`or` rules. |
| `pythonlite-programs.maude`        | 7 hand-written Maude AST programs matching the `tests/*.py` files. |
| `run_bigstep_tests.maude`          | Loads the semantics + programs and rewrites each program. |
| `parse.py`                         | Reads a real Python source file via `ast.parse` and emits an equivalent Maude `Pgm` constant. The parser is the layer that converts indentation-based Python into the Maude desugared AST. |
| `extract_out.py`                   | Extracts the `Out` integer-list portion from Maude's `result Configuration:` output for diffing. |
| `run_diff_test.sh`                 | The end-to-end driver. For each `tests/*.py`: run CPython → capture stdout; run `parse.py` → run Maude on the auto-generated AST → extract `Out` → diff. |
| `tests/`                           | Real Python source files. `01_smoke.py`, `02_arith.py`, `03_if.py`, `04_factorial.py` (5! = 120), `05_collatz.py` (steps from 27 = 111), `06_fizzbuzz.py` (sentinel ints in place of strings), `07_shortcirc.py` (validates short-circuit and division-by-zero protection). |
| `builtins.maude`                   | Verbatim copy of `cs522/HW1-Maude/builtins.maude` — Maude prelude (`PL-INT`, `PL-BOOL`, `PL-ID`, etc.). |
| `results/`                         | Test-run outputs: `last_run.json` (most recent machine-readable summary), `results_summary_<TS>.md` (timestamped human-readable summary). |

## Scope (pythonlite v1)

Included:
- Integers (Python `int`), booleans (`True` / `False`), identifiers.
- Arithmetic: `+`, `-`, `*`, `//`, `%`, unary `-`. Floor-div and floor-mod follow Python semantics (sign of divisor for `%`; toward-`-inf` for `//`).
- Comparisons: `<`, `<=`, `>`, `>=`, `==` (encoded `eqq` in Maude), `!=` (encoded `neq`).
- Boolean operators `and`, `or`, `not` — short-circuit at the semantic level (separate rules for the early-exit and right-eval cases).
- Statements: `pass`, `x = e` (encoded `:=` in Maude), `print(e)`, sequencing, `if/else`, `while`.
- Programs print integers to a captured output buffer for differential testing.

Excluded (out of scope for v1, listed in `../language_candidates.md`):
- Strings, floats, lists, dicts, tuples, classes.
- Functions, closures, recursion.
- Exceptions; division-by-zero is currently *stuck* (rule does not apply) rather than raising. v2 should add a `< error, σ, out >` configuration mirroring CS522 HW1 Ex. 56.
- For-loops; replaced by while loops with manual indexing.
- Modules / imports.
- I/O beyond integer `print`.

## Why Maude (and not Lean) for this v1

The user's target is *the CS522 framework*. CS522 uses Maude's rewriting logic as its semantics-implementation language, and the reference HW solutions in `cs522/HW{1..6}-Maude/` are all Maude. Doing the v1 in Maude lets us reuse `cs522/HW1-Maude/builtins.maude` verbatim, reuse the `< Cfg >` configuration shape and `=>` rule format from `cs522/HW1-Maude/imp/0-imp-original/1-imp-bigstep/imp-semantics-bigstep.maude`, and execute the resulting semantics directly — Maude *is* an interpreter for its own definitions. The Lean port lives one level up under `Imp/Real/Pythonlite/` and is a follow-up: this experiment establishes the shape of the answer; the Lean port is the kernel-checked verification of it.

## Verification: how we decide it's "correct"

Per `../verification_spec.md`, the contract has three layers. This v1 implements layer **(a)** in full and layers (b) and (c) partially:

- **(a) Differential testing vs reference interpreter** — fully implemented. `run_diff_test.sh` runs every `tests/*.py` through both CPython 3 and the Maude big-step semantics and diffs the integer outputs. Current pass rate: **7 / 7**.
- **(b) Cross-framework equivalence theorems inside Lean** — deferred until the Lean port lands at `Imp/Real/Pythonlite/`. Big-step is the reference judgment; small-step / denotational / MSOS / RSEC / CHAM / K / λ ports must each prove `↔ BigStep` (forward direction at minimum, no `sorry`).
- **(c) Stepan + Roșu textbook spot-check** — Maude rules are written to mirror `cs522/HW1-Maude/imp/0-imp-original/1-imp-bigstep/imp-semantics-bigstep.maude` shape-by-shape; cross-check in PR review.

## Known limitations / TODOs

- `pythonlite-syntax.maude` emits a few benign `bad format length` warnings on the `format (...)` operator attributes (lines 69, 70, 77, 79). These affect only Maude's pretty-printer; rules and rewriting are unaffected. Fix: trim the `format` attributes on `_:=_`, `print(_)`, `ifelse(_){_}else{_}`, `while(_){_}`.
- Scoping is lexical and the State is a cell store plus a heap (cycle 16): every variable is a cell `cell(A, X)` of one activation `A` (fresh id from the counter `nxtC`, parent pointer to the defining activation), and lists / dicts are heap objects `hp(N)` that variables hold as `ref(N)`. This fixes the cycle-15 limits (closure state across activations, late binding, sibling closures, activation-id collision, two parameters aliasing one list, parameter mutated then rebound, list returned and mutated through the alias, call result as argument, subscript-target snapshot); repros in `results/cycle15_qa_repros/` all pass, tests `58`-`73` (`72`: separately made functions never compare equal; `73`: `==` on self-containing containers terminates).
- Cycle 17: `x += e` / `x *= e` on a name change a list in place in its heap object (aliases see it; `augAdd` / `augMul`), reading a function-local name before its assignment raises `UnboundLocalError` (also for `xs.append(..)` and `xs[i] = ..` on such a name), and call-heavy programs are faster than cycle 15 (tail-call rules, dead activations that created no closure are dropped from the cell store). Tests `74`-`77`; QA programs in `results/cycle17_qa_programs/`.
- Still open after cycle 17: `+=` on a subscript target (`a[0] += [9]`) still copies instead of changing the inner list in place; tuple `+` and `*` are unsupported; `xs += (2, 3)` and `xs += "bc"` (list `+=` with a non-list iterable) get stuck; the `except ... as e` variable is not deleted after the handler; a closure reading a variable that its enclosing function assigns only later reads the global instead of raising; dict `==` is order-sensitive, `True == 1` is False, negative indexes, `IfExp` and slice-fresh syntax are unsupported, a dict key mutated after use; scale: heap objects are never freed, so programs that build many lists across calls still blow up (tree build depth 6 about 0.7 s, depth 8 about 13 s, depth 10 about 5 min).
- Cycle 18 (the list under "Still open after cycle 17" above is superseded except for what is repeated here): `a[i] += [x]` and `d[k] += [x]` (parse.py emits `augSub`) evaluate the name, the index, the old item and the right side in CPython's order, change a list item in place and store the result back, so aliases of the inner list see it; tuple `+` and `*` build a new tuple (`t += u`, `t *= n` rebind); list `+=` takes any iterable (list, tuple, string, dict keys) and `*=` repeats; `except ... as e` deletes `e` when the handler ends (also on return / raise / break / continue, also for a parameter), so a later read raises `UnboundLocalError` in a function and `NameError` at top level; a closure reading a variable its enclosing function assigns only later raises `NameError` instead of reading the global, and a never-assigned global raises `NameError`; negative list and tuple indexes; the conditional expression `a if c else b` (`ifExp`); `//` and `%` with negative operands (the builtin `/Int` only divides non-negative numbers, so they used to stay unevaluated). The heap is one binding `hpt |-> heapV(tree)`, a binary tree indexed by address, instead of one State binding per object. Tests `78`-`87`; QA programs in `results/cycle18_qa_programs/` (113 programs and `extract_repr.py`, which prints lists / tuples / dicts the way CPython does).
- Still open after cycle 18: dict `==` is order-sensitive, `True == 1` is False, a dict key mutated after use, a tuple item `t[0] += [2]` is stuck (TypeError is not modelled), heap objects are never freed, and the scale limit: with rewrite conditions every step costs the size of the whole configuration, so a tree build is depth 8 about 5 s, depth 10 about 280 s.
- Cycle 18, evaluator speed: `pythonlite-bigstep.maude` is now in continuation-passing form [generated from the direct-style spec `results/cycle18_cps/pythonlite-bigstep-direct.maude` by `results/cycle18_cps/cps_convert.py`; the direct-style file is the readable spec, the two agree on every test]. The cost of a Maude rewrite condition `=>` grows with the size of the term it is given, so in the direct style a step cost grew with the whole heap; with explicit continuations every rule is plain and a tree build is depth 8 about 0.4 s, depth 10 about 1.2 s, depth 13 about 23 s (direct style: 5.6 s, 281 s, not measured). The "scale" limit in the lines above no longer holds; heap objects are still never freed.
- Cycle 19: `1 // 0` and `1 % 0` (also `x //= 0`, `xs[i] %= 0`) raise `ZeroDivisionError`; an index outside `-len..len-1` raises `IndexError` (list, tuple, string; read, `xs[i] = v`, `xs[i] += v`, also when the list shrank while the right side ran) and a missing dict key raises `KeyError` (`d[k]`, `d[k] += 1`; a key whose value is None, 0, "" or [] is present); these are values caught by `except ... as e` like every other raise [the class name is the raised value; messages are not modelled]. `bool` is an int in operators (`True + 1`, `-True`, `xs[True]`, `xs[True] = v`, `xs[True:]`), `True == 1`, `[True] == [1]`, and in dict keys (`d[True]` finds key `1`, `{1: 'a', True: 'b'}` is `{1: 'b'}`). Dict `==` / `!=` ignore insertion order, also nested in lists, tuples and dicts: `==` compares `canon(deep(v))`, where `canon` turns True / False into 1 / 0 and sorts every dict by key (ints, strings, None, tuples, functions by id). `t[0] += [x]`, `t[0] = v` on a tuple and `s[0] = c` on a string raise `TypeError` (`t[0] += [x]` extends the inner list first, as CPython does). String `<`, `<=`, `>`, `>=` use Maude's own string order (character code), not the equal-length placeholder. Tests `88`-`93`; QA programs in `results/cycle19_qa_programs/` (96 that pass; `open/` holds the 4 below). The rule `sa2` has one rewrite condition now, so `cps_convert.py` no longer splits it.
- Still open after cycle 19: `range(True, 3)` binds the loop variable to `True` (the parser copies the start value); `for k in d` over a dict is unsupported; exception messages (`print(e)`) are not modelled, so `print(e)` shows the class name; non-ASCII text (Maude compares bytes as signed chars, so it sorts before ASCII); unhashable keys (a list as a dict key) do not raise; heap objects are never freed; a dict key mutated after use. Cycle 18's "still open" line above is superseded.
- A raise inside list / tuple / dict literals, slices and function-position expressions propagates (`55`).
- Division-by-zero is silently stuck rather than producing `< error, σ, out >`. Add an error configuration in v2.
- The output extractor (`extract_out.py`) assumes pythonlite's "one `|->` binding per variable" state shape and splits on the first top-level `,`. If a future v2 introduces grouped IMP-style `(x,y) |-> 0` declarations, the extractor must switch to a depth counter that ignores `|->`'s `>` glyph.
- No formal proof of determinism yet. Add `crl` → `rl` reduction proof or Lean port + `unique` lemma.

## Reproducing manually (one test)

```bash
# pick a test file
PROG=tests/04_factorial.py
# convert to maude
python3 parse.py "$PROG" mypgm > /tmp/mypgm.maude
# run
cat > /tmp/run.maude <<EOF
in builtins.maude
in pythonlite-syntax.maude
in pythonlite-state.maude
in pythonlite-bigstep.maude
in /tmp/mypgm.maude
mod RUN is including PYTHONLITE-SEMANTICS-BIGSTEP + MYPGM-PROG . endm
rewrite < mypgm > .
quit
EOF
maude -no-prelude -no-banner /tmp/run.maude
# expected:  result Configuration: < 'acc |-> 120 & 'i |-> 6 & 'n |-> 5,120 >
# the trailing "120" is the printed factorial of 5.
python3 "$PROG"
# expected:  120
```
