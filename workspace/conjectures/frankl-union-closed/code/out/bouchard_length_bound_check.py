"""Oracle check of Bouchard (arXiv:2511.10608) Theorem 1 — CORRECTED reading.

Length definition (from the source, verified in §1 + proof base case):
    ell = (maximum size of an inclusion-chain of members) - 1
A chain is a subfamily of A totally ordered by inclusion (X1,X2 in chain
implies X1 subset X2 or X2 subset X1); its SIZE is the number of members in
it. So ell = (max |chain|) - 1, NOT "size of largest member set" (the largest
member of the equality family is [n], which would make ell=n and the bound 2^n
never tight — that gloss is wrong and superseded).

Theorem under test:
  For any union-closed family A on universe [n] with length ell (by the chain
  definition),   |A| <= sum_{i=0}^{ell} C(n,i),
  with equality iff A = { S subset [n] : |S| >= n - ell }.

We check BOTH the bound and the equality-iff over ALL union-closed families
for n = 1..4 (exhaustive: 2^(2^n) subfamilies, 65536 at n=4 — the sanctioned
oracle bound, since UC itself is only machine-verified to n<=12 and the oracle
enumeration is exponential by design).

Oracle: lib.uc.decide_union_closed. Exact integers only.

Also printed: the base cases {[n]} (ell=0) and {[n], empty} (ell=1) from the
proof, and whether the "largest member set size" reading is distinct (it would
give ell=1 for {[n]} and fail the ell=0 base case, and ell=n for the equality
family, confirming that reading is wrong).
"""

from math import comb
from lib.uc import decide_union_closed


def pop(s):
    return bin(s).count("1")


def max_chain_length(F):
    """Longest chain A1 < A2 < ... < Ak of distinct members, |chain|=k.
    dp[s] = longest chain length ENDING at s."""
    present = sorted(F, key=pop)
    if not present:
        return 0
    dp = {}
    for s in present:
        best = 1
        for t in present:
            if t != s and (t & s) == t and pop(t) < pop(s):
                # t proper subset of s, both in F
                best = max(best, dp[t] + 1)
        dp[s] = best
    return max(dp.values())


def all_union_closed(n):
    """Enumerate all union-closed families on [n] (excluding empty and {empty})."""
    masks = list(range(1 << n))
    for sub in range(1, 1 << len(masks)):
        fam = {m for i, m in enumerate(masks) if (sub >> i) & 1}
        if not fam:
            continue
        if fam == {0}:
            continue
        if decide_union_closed(fam):
            yield fam


def ell_chain(A):
    """Correct reading: (max chain size) - 1."""
    return max_chain_length(A) - 1


def ell_maxmember(A, n):
    """WRONG reading kept for contrast: size of largest member set."""
    return max((pop(s) for s in A), default=0)


def bound_of(n, ell):
    return sum(comb(n, i) for i in range(ell + 1))


def equality_family(n, ell):
    return {m for m in range(1 << n) if pop(m) >= n - ell}


# base cases from the proof
print("=== base cases (proof) ===")
for A, name in [({1}, "{[n]}"), ({1, 0}, "{[n], empty}")]:
    ell = ell_chain(A)
    nA = max((pop(s) for s in A))
    print(f"  {name}: ell(chain-1)={ell}  bound=sum C({nA},0..{ell})={bound_of(nA, ell)}  |A|={len(A)}  match={len(A)==bound_of(nA,ell)}")

print()
print("=== Theorem 1 oracle check, correct (chain-1) reading ===")
for n in [1, 2, 3, 4]:
    vb = 0
    ve = 0
    example = None
    for A in all_union_closed(n):
        ell = ell_chain(A)
        b = bound_of(n, ell)
        big = equality_family(n, ell)
        if len(A) > b:
            vb += 1
            if example is None:
                example = ("bound", len(A), b, ell)
        is_big = (A == big)
        is_eq = (len(A) == b)
        if is_eq != is_big:
            ve += 1
            if example is None:
                example = ("eq-iff", len(A), b, ell, is_big, is_eq)
    print(f"  n={n}: bound-violations={vb}  equality-iff-violations={ve}" + (f"  e.g. {example}" if example else ""))

print()
print("=== comparison: WRONG 'largest member size' reading ===")
for n in [1, 2, 3, 4]:
    vb = 0
    ve = 0
    for A in all_union_closed(n):
        ell = ell_maxmember(A, n)
        b = bound_of(n, ell)
        if len(A) > b:
            vb += 1
        if (len(A) == b) != (A == equality_family(n, ell)):
            ve += 1
    print(f"  n={n}: bound-violations={vb}  equality-iff-violations={ve}")

print()
print("exit 0")
