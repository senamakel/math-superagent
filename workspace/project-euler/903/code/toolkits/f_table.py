"""F(d) table for the PE 903 structure Q(n) = sum_{d|n!} phi(n!/d) * F(d).

F(d) = sum_{pi in S_n} rank(pi^d), where rank is the 1-based position of a
permutation in the lexicographic list of all n! permutations and pi^d is the
d-th iterate, (pi^{k+1})(j) = pi(pi^k(j)), pi^1 = pi.  For every i with
gcd(i, n!) = d the value of sum_pi rank(pi^i) is the same (machine-verified
for n <= 6 by toolkits/f_literal.py), so the divisor d determines F.

Method: pi^d is read off the cycle decomposition of pi -- pi^d(j) is the
element d positions ahead of j along pi's cycle (so a k-cycle becomes
gcd(k, d) cycles of length k/gcd(k, d)).  Cycle decompositions are computed
once per permutation; each (pi, d) then costs O(n).

Time  O(tau(n!) * n! * n),  space O(n!).
Exact integer arithmetic throughout.

Correctness: cross-validated against the literal repeated-composition power
orbit route (toolkits/f_literal.py) for n = 4, 5, 6 in fdtable.py; F(1) =
n!(n!+1)/2 and sum_d phi(n!/d)*F(d) = Q(n) match the known values
(4808, 597876, 133103808).  rank(2,1,3) = 3 reproduces the statement example.
"""

import itertools
from math import factorial


def f_table(n):
    """Return {divisor d of n! : F(d)}, exact integers, d = i-value's gcd."""
    nf = factorial(n)
    perms = list(itertools.permutations(range(1, n + 1)))
    rank = {p: r for r, p in enumerate(perms, start=1)}

    # cycle decompositions, once per permutation (0-based indices, pi-direction)
    cycles_of = {}
    for pi in perms:
        seen = [False] * n
        cycles = []
        for s in range(n):
            if not seen[s]:
                cyc = []
                c = s
                while not seen[c]:
                    seen[c] = True
                    cyc.append(c)
                    c = pi[c] - 1
                cycles.append(cyc)
        cycles_of[pi] = cycles

    divs = [d for d in range(1, nf + 1) if nf % d == 0]
    out = {}
    for d in divs:
        total = 0
        for pi in perms:
            arr = [0] * n
            for cyc in cycles_of[pi]:
                k = len(cyc)
                for pos, node in enumerate(cyc):
                    arr[node] = cyc[(pos + d) % k] + 1  # back to 1-based
            total += rank[tuple(arr)]
        out[d] = total
    return out
