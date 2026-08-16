"""CORRECTED determinacy spot-check for the DH n=3 cross-modulus classifier.

The bug in code/out/dh_gate_independent.py: its spot-check tested determinacy
of p^i mod M as ``canon_of_val == i``, i.e. "i is the SMALLEST exponent that
produces the residue".  That is NOT the definition.  Determinacy (DH Def 2.2)
means:

    p^i is DETERMINATE mod M  iff  the ONLY b >= 0 with p^b == p^i (mod M)
    is b = i   --  the residue NEVER recurs.

The correct criterion is

    p^i determinate mod M  <=>  i < v_p(M),

where v_p(M) is the exponent of p in M.  Why: write M = p^v * R with
gcd(p,R) = 1 and v = v_p(M).  For i >= v,

    p^i = p^v * p^(i-v),   and  if T = ord_R(p)  then  p^(i+T) = p^v * p^(i-v+T)
    == p^v * p^(i-v) = p^i  (mod M)   because  p^T == 1 (mod R),

so the residue ALWAYS recurs at b = i + T > i: p^i is indeterminate.
Conversely, for i < v the residues p^0, ..., p^(v-1) mod M are pairwise
distinct (their p-adic valuations differ, and p^i < M), so p^i is determinate.
(When R = 1 the period is N/A: p^e == 0 mod M for all e >= v, so every i >= v
recurs at b = v, resp. b = v+1 when i = v.)

This program checks the criterion (a) against a direct definitional test (b)
for each (M, p, i).  It does NOT touch the M1/M2 PASS verdicts -- those were
established independently elsewhere and must not be re-verified or changed
here.  It does NOT reuse erdos.dh_classifier's determinacy logic: v_p, the
period, and the direct test are all recomputed from first principles with
exact integer arithmetic only (pow, sympy n_order, gcd).  No floats.
"""

from math import gcd
from sympy.ntheory import n_order


def v_p(n, p):
    """Largest e >= 0 with p**e dividing n.  Exact integer arithmetic."""
    if n <= 0:
        raise ValueError("v_p requires n >= 1")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def period_rest(p, M):
    """Multiplicative order T of p modulo R = M / p**v_p(M), or None when
    R == 1 (no unit part: the p-power diagram is pure tail)."""
    rest = M // (p ** v_p(M, p))
    if rest == 1:
        return None
    assert gcd(p, rest) == 1
    return n_order(p, rest)


def criterion(i, v):
    """(a) The criterion: p^i determinate mod M iff i < v_p(M)."""
    return i < v


def direct_determinacy(p, M, i, B):
    """(b) Direct definitional test: p^i is determinate iff NO b != i with
    0 <= b <= B satisfies p^b == p^i (mod M).

    B = v_p(M) + period_rest + 5 covers every possible recurrence: for
    i >= v the recurrence sits at b = i + T, and all i tested satisfy
    i + T <= (v + 4) + T < v + T + 5 = B; for i < v no recurrence exists
    at all (distinct tail residues, valuation argument).
    """
    r = pow(p, i, M)
    for b in range(0, B + 1):
        if b != i and pow(p, b, M) == r:
            return False
    return True


def run_modulus(M):
    """Check (a) == (b) for p in {2,3} over i in 0..v_p(M)+4.  Returns bool."""
    print("=" * 74)
    print(f"M = {M}  = 2^{v_p(M,2)} * 3^{v_p(M,3)} * "
          f"{M // (2**v_p(M,2) * 3**v_p(M,3))}")
    all_ok = True
    for p in (2, 3):
        v = v_p(M, p)
        T = period_rest(p, M)
        B = v + (T if T is not None else 0) + 5
        tag = f"{T}" if T is not None else "N/A (rest = 1)"
        print(f"  p = {p}:  v_p(M) = {v},  period_rest = ord_{{M/p^v}}(p) = {tag},"
              f"  B = {B}")
        mism = []
        for i in range(0, v + 5):          # i = 0 .. v_p(M)+4 (around v_p)
            a = criterion(i, v)
            b = direct_determinacy(p, M, i, B)
            if a != b:
                mism.append((i, a, b))
        if mism:
            all_ok = False
            for (i, a, b) in mism:
                print(f"    MISMATCH: i={i}: criterion={a} but direct test={b}")
        else:
            print(f"    PASS: (a) i < {v}  ==  (b) no b != i in 0..{B} with "
                  f"p^b == p^i (mod M), for all i in 0..{v + 4}")
    return all_ok


def main():
    print("CORRECTED determinacy spot-check (DH Def 2.2, cross-modulus classifier)")
    print("Definition: p^i is DETERMINATE mod M iff the ONLY b >= 0 with")
    print("            p^b == p^i (mod M) is b = i   (the residue never recurs).")
    print("Criterion:  determinate iff i < v_p(M).")
    print("The OLD spot-check test `canon_of_val == i` is wrong: it answers")
    print("'i is the FIRST exponent hitting the residue', not 'i is the ONLY'.\n")

    # ---- Explicit recurrence verification on the exact row the old check
    # ---- spuriously mismatched: (M, p, i) = (5440, 2, 6).
    M, p, i = 5440, 2, 6
    v = v_p(M, p)
    T = period_rest(p, M)
    r = pow(p, i, M)
    print(f"Explicit recurrence check  M = {M}, p = {p}, i = {i}:")
    print(f"  v_2(M) = {v},  ord_85(2) = {T},  so 2^{i} and 2^{i + T} = 2^{i + T}"
          f" must agree mod {M}:")
    print(f"    2^{i}   mod {M} = {r}")
    print(f"    2^{i + T} mod {M} = {pow(p, i + T, M)}")
    recur = pow(p, i + T, M) == r
    print(f"  => {recur}: 2^{i} recurs at b = {i + T} > {i}, so 2^{i} is"
          f" genuinely INDETERMINATE.")
    print(f"  criterion (a): i < v_p(M)?  {i} < {v} -> {criterion(i, v)}"
          f"  (False = indeterminate, as required)")
    # The OLD buggy test, reproduced for the record: canonical map = first hit.
    seen = {}
    x = 1 % M
    e = 0
    while x not in seen:
        seen[x] = e
        x = (x * p) % M
        e += 1
    old = (seen[r] == i)
    print(f"  OLD spot-check test `canon_of_val == i` returned {old}  -- WRONG:"
          f" the residue {r} first occurs at exponent {seen[r]}, but recurs at"
          f" exponent {i + T}, so 'first' is not 'only'.\n")

    # ---- Determinacy table for M = 5440, p = 2: 0..5 determinate, >= 6 not.
    B = v + (T if T is not None else 0) + 5
    print(f"Determinacy table for M = {M}, p = {p}  (v_2 = {v},"
          f" period_rest = {T}, B = {B}):")
    print("  i | criterion (a) i < v | direct (b) no recurrence | verdict")
    for i in range(0, 10):
        a = criterion(i, v)
        b = direct_determinacy(p, M, i, B)
        verdict = "determinate" if a else "indeterminate"
        agree = "OK" if a == b else "!!!"
        print(f"  {i:2d} |         {str(a):5s}        |          {str(b):5s}"
              f"          | {verdict:12s} {agree}")
    print()

    # ---- Full (a) == (b) sweep over the chosen moduli.
    moduli = [
        5440,                        # M1 = 2^6 * 5 * 17  (paper's extraneous case)
        2796160,                     # M2 = 2^7 * 5 * 17 * 257 (paper's clean case)
        81,                          # 3^4
        3 ** 4,                      # same modulus, listed separately per spec
        2 ** 10 * 3 ** 2 * 5,        # 46080
        27,                          # 3^3
        2 ** 5 * 3 ** 4,             # 2592
        512,                         # 2^9
    ]
    print("Full (a) == (b) check over all (M, p, i):")
    results = []
    for M in moduli:
        results.append((M, run_modulus(M)))

    print("=" * 74)
    bad = [M for M, ok in results if not ok]
    if not bad:
        print(f"ALL {len(moduli)} moduli, both p in {{2,3}}, all i tested: "
              f"(a) i < v_p(M) AGREES with (b) the direct definitional test.")
        print("The criterion  p^i determinate mod M  <=>  i < v_p(M)  is CONFIRMED"
              " CORRECT on every case; the old `canon == i` test was the bug.")
    else:
        print(f"DISAGREEMENTS on moduli {bad}: details above.")
    print(f"Moduli tested: {moduli}")


if __name__ == "__main__":
    main()
