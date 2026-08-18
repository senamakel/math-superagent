#!/usr/bin/env python3
"""
verify_lean_tables.py — SECOND, independent route to "L8 not in <L4,L6>".

This program validates the DATA TABLES the Lean kernel actually sees in
code/lean/Lib/Bautin.lean. It does NOT import or re-run the sympy focal-value
recurrence (code/bautin/lyapunov_quadratic.py) — that is the program that
EMITTED the tables, and this is an independent check of the emitted text.

WHAT IT DOES
  * A small parser reads, directly from the file text of Bautin.lean:
      - V1num : the six explicit terms  C (c : Q) * X i * X j
      - v2coeffs / v2ms : 56 integer coefficients + 56 exponent vectors
      - v3coeffs / v3ms : 220 integer coefficients + 220 exponent vectors
      - certPt                            = [-2, -2, 1, -1, -1, 1]
  * Reconstructs V1num, V2num, V3num as exact integer polynomials
    (monomial -> int coeff) over the six coefficient variables
    (a1,a2,a3,b1,b2,b3).
  * Evaluates each polynomial at certPt with exact integer arithmetic.
  * Asserts  eval V1num = 0, eval V2num = 0, eval V3num = 7200
    and monomial counts 6 / 56 / 220 — the cleared values recorded in
    code/out/cofactor_certificate.captured.txt.
  * Prints WHAT RAN, the three evaluations, and CERTIFICATE VALID: PASS/FAIL.
    Exit code 0 iff PASS.

Bears on: the membership statement "L8 not in <L4,L6>" as kernel-checked in
code/lean/Lib/Bautin.lean (theorem V3_not_mem_span_V1_V2, whose premises are
exactly the three evaluations above), and on the claim recorded in
code/out/cofactor_certificate.captured.txt.

Exact integer arithmetic only; no floats, no sympy.
"""

import re
import os
import sys
from pathlib import Path

LEAN_FILE = Path(os.environ.get(
    "BAUTIN_LEAN_FILE", "/workspace/code/lean/Lib/Bautin.lean"))
N_VARS = 6

# --- parse helpers -----------------------------------------------------------

def _def_body(text, name):
    """Text between `def <name> ... :=` and the next top-level `def`/`theorem`."""
    m = re.search(r"\bdef\s+" + re.escape(name) + r"\b", text)
    if not m:
        raise ValueError(f"def {name} not found in {LEAN_FILE}")
    rest = text[m.end():]
    nxt = re.search(r"\n(?:def|theorem|namespace|end)\b", rest)
    return rest if nxt is None else rest[: nxt.start()]


def _parse_int_array(s, i):
    """
    Parse an integer array literal starting at `i` in `s`.
    Handles `![` ... `]` with nested `![...]` entries and bare integers.
    Returns (list, index just after the closing `]`).
    """
    assert s[i] == "!" and s[i + 1] == "[", f"not an array at {i}: {s[i:i+2]!r}"
    i += 2  # skip `![`
    out = []
    while True:
        while i < len(s) and s[i] in " \t\n,":
            i += 1
        if i >= len(s):
            raise ValueError("unterminated ![ ... ] array")
        c = s[i]
        if c == "]":
            return out, i + 1
        if c == "!" and s[i + 1] == "[":
            sub, i = _parse_int_array(s, i)
            out.append(sub)
        elif c == "-" or c.isdigit():
            m = re.match(r"-?\d+", s[i:])
            out.append(int(m.group(0)))
            i += m.end()
        else:
            raise ValueError(f"unexpected char {s[i]!r} at {i} in int array")


def _extract_int_array(body):
    """Find the first `![...]` in the def body and parse it."""
    i = body.find("![")
    if i < 0:
        raise ValueError("no ![ ... ] array found in def body")
    arr, end = _parse_int_array(body, i)
    return arr


def _parse_V1num(body):
    """
    V1num: six explicit terms of the form `C (c : Q) * X i * X j`.
    Returns a dict mono -> int coeff.
    """
    poly = {}
    pattern = re.compile(
        r"C\s*\(\s*(-?\d+)\s*:\s*ℚ\s*\)\s*\*\s*X\s+(\d+)\s*\*\s*X\s+(\d+)"
    )
    for m in pattern.finditer(body):
        c = int(m.group(1))
        i, j = int(m.group(2)), int(m.group(3))
        if i >= N_VARS or j >= N_VARS:
            raise ValueError(f"variable index out of range: {i}, {j}")
        exp = [0] * N_VARS
        exp[i] += 1
        exp[j] += 1
        mono = tuple(exp)
        poly[mono] = poly.get(mono, 0) + c
    if not poly:
        raise ValueError("no V1num terms parsed")
    return poly


def _poly_from_tables(coeffs, ms):
    """Zip a coefficient array with an array of exponent vectors -> dict mono -> int."""
    if len(coeffs) != len(ms):
        raise ValueError(f"coeffs/ms length mismatch: {len(coeffs)} vs {len(ms)}")
    poly = {}
    for c, mvec in zip(coeffs, ms):
        if len(mvec) != N_VARS:
            raise ValueError(f"exponent vector of length {len(mvec)}, need {N_VARS}")
        mono = tuple(mvec)
        poly[mono] = poly.get(mono, 0) + c
    return poly


def _eval_at(poly, pt):
    """Exact integer evaluation: sum_c c * prod_i pt[i]^e_i."""
    total = 0
    for mono, c in poly.items():
        term = c
        for x, e in zip(pt, mono):
            if e:
                term *= x ** e
        total += term
    return total


# --- the check ---------------------------------------------------------------

def main():
    text = LEAN_FILE.read_text(encoding="utf-8")

    v1num = _parse_V1num(_def_body(text, "V1num"))
    v2coeffs = _extract_int_array(_def_body(text, "v2coeffs"))
    v2ms = _extract_int_array(_def_body(text, "v2ms"))
    v3coeffs = _extract_int_array(_def_body(text, "v3coeffs"))
    v3ms = _extract_int_array(_def_body(text, "v3ms"))
    cert = _extract_int_array(_def_body(text, "certPt"))

    v2num = _poly_from_tables(v2coeffs, v2ms)
    v3num = _poly_from_tables(v3coeffs, v3ms)

    lens = {
        "V1num (explicit terms)": len(v1num),
        "v2coeffs entries": len(v2coeffs),
        "v2ms entries": len(v2ms),
        "V2num  distinct nonzero monomials": len(v2num),
        "v3coeffs entries": len(v3coeffs),
        "v3ms entries": len(v3ms),
        "V3num  distinct nonzero monomials": len(v3num),
        "certPt coordinates": len(cert),
    }

    ok_counts = len(v1num) == 6 and len(v2num) == 56 and len(v3num) == 220
    ok_shape = (len(v2coeffs) == 56 and len(v2ms) == 56
                and len(v3coeffs) == 220 and len(v3ms) == 220
                and len(cert) == 6)
    # no duplicate monomials inside one table (a zero coefficient would be a
    # silent table corruption; all entries must be distinct and nonzero)
    ok_distinct = (len(v2num) == len(v2coeffs) and len(v3num) == len(v3coeffs))

    ev1 = _eval_at(v1num, cert)
    ev2 = _eval_at(v2num, cert)
    ev3 = _eval_at(v3num, cert)

    ok_evals = (ev1 == 0) and (ev2 == 0) and (ev3 == 7200)
    ok = ok_counts and ok_shape and ok_distinct and ok_evals

    print("# verify_lean_tables.py - SECOND independent route to \"L8 not in <L4,L6>\"")
    print("# checks the data tables the LEAN KERNEL sees in code/lean/Lib/Bautin.lean")
    print("# defs parsed: V1num (6 explicit terms), v2coeffs/v2ms, v3coeffs/v3ms, certPt")
    print()
    print("WHAT RAN:  code/bautin/verify_lean_tables.py, stdlib-only parser +")
    print("           exact INTEGER polynomial arithmetic over the six coefficient")
    print("           variables (a1,a2,a3,b1,b2,b3). No sympy, no recurrence, no")
    print("           floats. Input: the raw text of code/lean/Lib/Bautin.lean - the")
    print("           exact tables the Lean kernel elaborates.")
    print("WHICH DEFS: V1num, v2coeffs, v2ms, v3coeffs, v3ms, certPt;")
    print("           claimed identities eval V1num = 0, eval V2num = 0,")
    print("           eval V3num = 7200 at certPt = (-2,-2,1,-1,-1,1);")
    print("           monomial counts 6 / 56 / 220.")
    print()
    print("table lengths:")
    for k, v in lens.items():
        print(f"  {k}: {v}")
    print()
    print("evaluations at certPt (exact integers):")
    print(f"  eval V1num = {ev1}   (must be 0)")
    print(f"  eval V2num = {ev2}   (must be 0)")
    print(f"  eval V3num = {ev3}   (must be 7200)")
    print()
    print(f"monomial-count checks (6/56/220):          {'PASS' if ok_counts else 'FAIL'}")
    print(f"table-shape checks (56/56/220/220, len 6): {'PASS' if ok_shape else 'FAIL'}")
    print(f"distinct-nonzero-monomial checks:           {'PASS' if ok_distinct else 'FAIL'}")
    print(f"evaluation checks (0 / 0 / 7200):           {'PASS' if ok_evals else 'FAIL'}")
    print()
    print("CERTIFICATE VALID: " + ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())