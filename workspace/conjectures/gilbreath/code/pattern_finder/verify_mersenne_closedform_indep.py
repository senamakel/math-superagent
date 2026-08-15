#!/usr/bin/env python3
"""Independent exact verification of Mersenne-period affine nu2 closed form.

For the P-periodic mod-4 switch word h (period P = 2^k - 1, canonical pattern
[0]*(P-1)+[1], i.e. k-1 stays then a switch), nu2(n) is claimed to be affine
in n per residue class of n mod P, with per-residue constants c_r whose sum is
exactly 3^k - 3, and min c_r = 2.

All computation here is literal full-triangle absolute differencing from first
principles (no lib.rightdiag, no lib.gilbreath).  nu2 is counted on the right
diagonal as described in dyadic_mersenne_indep.py (the run's own convention):
the maximal {0,2} suffix of the right diagonal of the difference triangle.

c_r is measured exactly: c_r = nu2(n+P) - nu2(n) for n ≡ r (mod P), which is
constant (that IS the affine-in-P property) for n large enough that the O(1)
transient has died.  We check constancy across two consecutive P-spaced values
AND accumulate sum of c_r vs 3^k - 3.
"""
import sys

def q_seq(word, n_terms):
    q = [2, 3]
    P = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % P]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]

def right_diag(q):
    row = list(q)
    n = len(row) - 1
    diag = [row[n]]
    for k in range(1, n + 1):
        nxt = [abs(row[i] - row[i+1]) for i in range(len(row)-1)]
        row = nxt
        diag.append(row[n - k])
    return diag

def nu2(diag):
    body = diag[:-1]
    i = len(body)
    while i > 2 and body[i-1] in (0, 2):
        i -= 1
    return body[i:].count(2)

def literal_nu2(word, n):
    return nu2(right_diag(q_seq(word, n+1)))

def main():
    for k, P in [(2,3),(3,7),(4,15),(5,31)]:
        word = [0]*(P-1)+[1]
        # window over which we measure c_r exactly
        nmin = P*6 + 5
        nmax = nmin + P*3
        # values at n and n+P for each residue
        v = {}
        for n in range(nmin, nmax+P+1):
            v[n] = literal_nu2(word, n)
        cs = {}
        ok = True
        for r in range(P):
            ns = [n for n in range(nmin, nmax) if n % P == r]
            diffs = {v[n+P]-v[n] for n in ns}
            if len(diffs) != 1:
                ok = False
                cs[r] = None
            else:
                cs[r] = diffs.pop()
        S = sum((c or 0) for c in cs.values())
        m = min(c for c in cs.values() if c is not None)
        print(f"P={P:3d} (2^{k}-1): affine={ok}  min c_r={m}  sum c_r={S}  "
              f"target 3^{k}-3={3**k-3}  match={S==3**k-3}")
        assert ok and S == 3**k-3 and m == 2, (P, S, m)
    print("INDEPENDENT LITERAL-TRIANGLE: Mersenne affine nu2 closed form CONFIRMED (P=3,7,15,31)")

if __name__ == "__main__":
    main()
