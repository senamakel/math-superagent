#!/usr/bin/env python3
"""Drift guard for the shared descent-core region of link_a.lean.

Directive 53 asked for link_a.lean to *import* runAbs (and countTwo) from
descent_lemma.lean rather than redefine it, so two files cannot agree by
convention.  In this container cross-file `import` cannot pass `lean_check`
(the kernel's lean resolves modules against a fixed read-only path that does
not include /workspace; see code/lean/link_a.lean header).  The honest
alternative: runAbs, countTwo, and the descent core live ONCE in link_a.lean,
and this program machine-checks that the shared definitions are byte-identical
to descent_lemma.lean, so a silent edit to one cannot leave the other stale.

It verifies, over the exact source text of both files:

  * def runAbs      -- byte-identical
  * def countTwo    -- byte-identical
  * lemma dist_even_even, absorbing, run_absorb, dist_even_two,
    run_high_even, run_inv_even, even_le_two, theorem descent_backward
    -- byte-identical (bodies as written in the file)

Returns exit 0 iff every check passes; prints each check.  Any diff is a
mismatch and must be fixed by re-syncing the regions, never by relaxing this
guard.

Usage: from /workspace,  python3 code/lean/link_a_drift_guard.py
"""

import re
import sys

DESCENT = "code/lean/descent_lemma.lean"
LINK = "code/lean/link_a.lean"


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def definition(text, name, is_def):
    """Return the source text of the named def/lemma/theorem block.

    A block starts at the line whose stripped form begins with
    '<kind> <name>' (kind collected from is_def keys) and ends at the last
    '--' comment line that belongs to it -- here we take the whole run of
    tab-indented Lean source lines following the signature until the next
    blank-line-separated comment group or a top-level line that is not
    indented.  To keep byte-comparison simple and robust, we compare the
    *reproduced* canonical block: the signature line plus every source line
    that is indented (continuation / tactics) until a non-indented,
    non-blank line that starts a new top-level construct.
    """
    kind = is_def.get(name)
    if kind is None:
        return None
    lines = text.split("\n")
    start = None
    for i, ln in enumerate(lines):
        stripped = ln.strip()
        if stripped == f"{kind} {name}" or stripped.startswith(f"{kind} {name} "):
            start = i
            break
    if start is None:
        return None
    # Collect signature + indented body up to the next top-level construct.
    out = [lines[start].strip()]
    for ln in lines[start + 1:]:
        s = ln.strip()
        if s == "":
            continue
        if ln[:1] in (" ", "\t"):
            out.append(ln.rstrip())
        else:
            # A non-indented source line: it is either the first line of the
            # next construct (stop) or a stray comment; stop the block.
            break
    return "\n".join(out)


def check_blocks(name, desc, link):
    if desc != link:
        print(f"FAIL  {name}")
        print(f"  descent_lemma.lean:\n{desc}")
        print(f"  link_a.lean:\n{link}")
        return False
    print(f"OK    {name}  (byte-identical)")
    return True


def main():
    desc = read(DESCENT)
    link = read(LINK)

    # defs (with their exact signature spellings)
    defs = {
        "runAbs": "def",
        "countTwo": "def",
    }
    # lemmas / theorems (name -> kind)
    stmts = {
        "dist_even_even": "lemma",
        "absorbing": "lemma",
        "run_absorb": "lemma",
        "dist_even_two": "lemma",
        "run_high_even": "lemma",
        "run_inv_even": "lemma",
        "even_le_two": "lemma",
        "descent_backward": "theorem",
    }

    all_ok = True
    for name, kind in {**defs, **stmts}.items():
        db = definition(desc, name, {name: kind})
        lb = definition(link, name, {name: kind})
        if db is None or lb is None:
            print(f"SKIP  {name}  (definition not found in one file: "
                  f"descent={db is not None}, link={lb is not None})")
            all_ok = False
            continue
        if not check_blocks(name, db, lb):
            all_ok = False

    print()
    if all_ok:
        print("DRIFT GUARD: PASS -- shared descent-core region is byte-identical "
              "between descent_lemma.lean and link_a.lean")
        return 0
    print("DRIFT GUARD: FAIL -- one or more shared definitions differ; "
          "re-sync the regions, do not silence this guard")
    return 1


if __name__ == "__main__":
    sys.exit(main())
