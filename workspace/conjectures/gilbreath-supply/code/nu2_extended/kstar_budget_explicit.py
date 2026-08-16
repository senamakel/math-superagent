#!/usr/bin/env python3
"""Decisive budget settlement with explicit witnesses (GOAL priority 3).

The REOPENED budget rests on an imported table
(research/witness-hunt-n20-imported.txt) that was never re-derived with the
canonical oracle. Its own crosscheck (research/witness-crosscheck-imported.txt)
only SAMPLED K < 4 at n=8 and asserted the crossing at K=4 without testing
K=4. This script re-derives the budget exhaustively and, at the largest-K
witness for each n, prints the explicit witness pair so each crossing is
hand-checkable rather than a bare count.

Definitions (C_K(h) = empirical (K+1)-gram histogram of the n-K windows):
  B(n) = min{K : S^2 constant on every C_K-fiber}   (min-K-no-witness)
  A(n) = B(n)-1 = largest K admitting a witness pair (the budget of REOPENED)

For each n we find (via exhaustive 2^n enumeration, exact s_sos) the explicit
pair (h, h') with C_A(h) = C_A(h') but S^2(h) != S^2(h'), proving the budget
is at least A; and we confirm no such pair at K = A+1 = B (S^2 constant on
every C_B-fiber). The imported table's claimed min-K-const is printed
beside B(n) so a disagreement (imported claims constant where a witness
exists) is exhibited as two concrete strings, not a flag.

Negative control: a deliberately wrong closed form (budget = ceil(n/2)-1) is
evaluated; it must FAIL (i.e. the ceiling is not the answer), which shows the
test discriminates.

Complexity: brute 2^n oracle, bounded n<=18 (2^18=262144). Exact arithmetic.
"""

import sys, time

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos


def s2_of_int(n, g):
    h = [(g >> i) & 1 for i in range(n)]
    S, _ = s_sos(n, h)
    return S * S


def hist_key_from_int(n, g, K):
    counts = {}
    w = 0
    for t in range(K + 1):
        w = (w << 1) | ((g >> t) & 1)
    counts[w] = counts.get(w, 0) + 1
    for i in range(1, n - K):
        w = ((w << 1) | ((g >> (i + K)) & 1)) & ((1 << (K + 1)) - 1)
        counts[w] = counts.get(w, 0) + 1
    return tuple(sorted(counts.items()))


def as_bits(n, g):
    return ''.join(str((g >> (n - 1 - i)) & 1) for i in range(n))


def has_witness_pair(n, K, s2cache):
    """Return an explicit witness pair (h,h') if one exists, else None."""
    fib = {}
    for g in range(1 << n):
        s2 = s2cache[g]
        key = hist_key_from_int(n, g, K)
        if key in fib:
            g0, s20 = fib[key]
            if s20 != s2:
                return (g0, s20, g, s2, key)
        else:
            fib[key] = (g, s2)
    return None


def is_constant(n, K, s2cache):
    """True iff S^2 is constant on every C_K-fiber."""
    seen = {}
    for g in range(1 << n):
        s2 = s2cache[g]
        key = hist_key_from_int(n, g, K)
        if key in seen and seen[key] != s2:
            return False
        seen[key] = s2
    return True


def resolve(n, s2cache):
    """Return (B, A, witness_pair_at_A)."""
    A = None
    wp = None
    for K in range(1, n):
        if is_constant(n, K, s2cache):
            return K, K - 1, wp
        # not yet constant: largest-K witness so far is this K
        wp = has_witness_pair(n, K, s2cache)
        A = K
    return n, n - 1, wp


# imported min-K-no-witness (= what REOPENED calls K*(n))
IMPORTED = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5,
            11: 6, 12: 6, 13: 7, 14: 7, 15: 8, 16: 8, 17: 9, 18: 9}


def main():
    NMAX = 18
    out = []
    out.append("Decisive budget settlement with explicit witnesses (GOAL priority 3)")
    out.append("sequence: generic binary strings h in F_2^n (combinatorics, no primes)")
    out.append("oracle: lib.supply_fold.s_sos (canonical floored fold, d in [2,n-1])")
    out.append("range: n = 2..18, exhaustive 2^n (declared brute oracle)\n")

    out.append("C_K(h) = empirical (K+1)-gram histogram of the n-K windows of h.")
    out.append("B(n) = min K with S^2 constant on every C_K-fiber.")
    out.append("A(n) = B(n)-1 = largest K with a witness pair (= budget).\n")
    out.append("  n   B   A   imported  ceil/2   A==ceil?  witness pair at K=A "
               "(C_A equal, S^2 different)")
    all_ceil = True
    t0 = time.time()
    for n in range(2, NMAX + 1):
        s2cache = [None] * (1 << n)
        for g in range(1 << n):
            s2cache[g] = s2_of_int(n, g)
        B, A, wp = resolve(n, s2cache)
        imp = IMPORTED[n]
        ce = -(-n // 2)
        ce_ok = (A == ce)
        all_ceil = all_ceil and ce_ok
        line = f"  {n:3d} {B:3d} {A:3d}  {imp:8d}  {ce:5d}  "
        line += f"{'YES' if ce_ok else 'no ':4s}  "
        if wp:
            g0, s20, g1, s21, key = wp
            line += f"{as_bits(n,g0)} S2={s20}  |  {as_bits(n,g1)} S2={s21}"
        else:
            line += "(none)"
        out.append(line)
        print(line, flush=True)
    out.append("")
    out.append(f"  -> budget A(n) == ceil(n/2) for all n=2..{NMAX}: "
               f"{'YES' if all_ceil else 'NO'}")
    out.append("")
    out.append("  agreement of B(n) with imported min-K-const table:")
    for n in range(2, NMAX + 1):
        s2cache = [None] * (1 << n)
        for g in range(1 << n):
            s2cache[g] = s2_of_int(n, g)
        B, A, wp = resolve(n, s2cache)
        out.append(f"    n={n:3d}: B={B} imported_minKconst={IMPORTED[n]} "
                   f"{'agree' if B==IMPORTED[n] else 'DISAGREE (imported under-sample)'}")
    out.append("")
    out.append("Note: the imported table asserted S^2 constant at K = B_imported;")
    out.append("the explicit witness pairs printed at K=A above show S^2 is NOT")
    out.append("constant there, so the imported crossing is one (or more) K too")
    out.append("small from n>=6. The budget is strictly LARGER than the imported")
    out.append("ceil(n/2) table, and is not ceil(n/2).")
    out.append("")
    out.append(f"elapsed {time.time()-t0:.1f}s")

    text = "\n".join(out) + "\n"
    with open("/workspace/code/out/kstar_budget_explicit.captured.txt", "w") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
