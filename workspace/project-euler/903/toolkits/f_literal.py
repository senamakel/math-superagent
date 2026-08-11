"""Independent oracle for the F(d) table: literal power orbits.

For every i in 1..n! the literal value F_i = sum_{pi} rank(pi^i) is computed
by walking each permutation's power orbit once with repeated composition
(pi^{k+1}(j) = pi(pi^k(j))) and using periodicity: pi^i = pi^((i-1) mod ord(pi)
+ 1), ord(pi) = lcm of cycle lengths.  All i are then grouped by
g = gcd(i, n!); the function asserts F_i is constant on each group (this is
the independence claim behind "F(d)") and returns {g : F(g)}.

This uses a different power semantics (composition walk, like brute.py/psid.py)
than toolkits/f_table.py (cycle raising), so agreement of the returned dict
with f_table(n) cross-checks both implementations.

Time  O(n! * max_i ord-ish) dominated by n! * n! rank lookups in the i-loop,
space O(n! * n) for the orbit store.  Exact integer arithmetic.

Verified in fdtable.py: f_literal(n) == f_table(n) for n = 4, 5, 6, and the
group-constant assumption is asserted for every i in 1..n!.
"""

import itertools
from math import factorial, gcd


def f_by_gcd(n):
    """Return {g : F(g)} over g | n!, from the literal per-i computation."""
    nf = factorial(n)
    perms = list(itertools.permutations(range(1, n + 1)))
    rank = {p: r for r, p in enumerate(perms, start=1)}

    # orbit[t] = pi^(t+1) for t = 0..ord(pi)-1, visit order
    orbits = {}
    for pi in perms:
        seen = []
        sset = set()
        cur = pi
        while cur not in sset:
            sset.add(cur)
            seen.append(cur)
            cur = tuple(pi[v - 1] for v in cur)
        orbits[pi] = seen

    groups = {}
    for i in range(1, nf + 1):
        Fi = 0
        for pi in perms:
            orb = orbits[pi]
            Fi += rank[orb[(i - 1) % len(orb)]]
        g = gcd(i, nf)
        groups.setdefault(g, []).append(Fi)

    out = {}
    for g, vals in groups.items():
        uniq = set(vals)
        assert len(uniq) == 1, f"F_i not constant on gcd class {g}: {uniq}"
        out[g] = uniq.pop()
    return out
