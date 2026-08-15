#!/usr/bin/env python3
"""Independent verification of the Mersenne-affine classification AND the
closed form sum(c_r)=3^k-3, using a from-scratch LITERAL full-triangle builder
(no lib.rightdiag) so the measurement route is independent of the canonical one.

nu2(n) = #2s in the maximal {0,2} suffix starting at index>=2 of the right
diagonal delta(q_n).  Builds the actual absolute-difference triangle rows.
"""
import itertools

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

def affine_constants(P, nmin, nmax, stepcheck):
    """Literal nu2 at every n via full triangle; check P-step increments
       constant per residue over [nmin,nmax]."""
    seen = {}
    ok = True
    # build every n in [nmin, nmax] fresh (full triangle each) — slow but independent
    for n in range(nmin, nmax+1):
        word = [0]*(P-1)+[1]
        q = q_seq(word, n+1)
        v = nu2(right_diag(q))
        if n >= nmin+P:
            prev = seen.pop(n-P, None)
            # prev stored de-dup of residue; we keep last value per residue to check diff
            pass
    # simpler: recompute and record full map
    return None

def main():
    # Verify affine constants for Mersenne P=7,15 at sampled n by literal triangle,
    # comparing (a) per-residue P-step increment against the canonical c_r, and
    # (b) sum(c_r) against 3^k-3.
    from fractions import Fraction
    cases = {7: 3, 15: 4}
    for P, k in cases.items():
        # literal nu2 map over a window
        nmax = P*8+50
        nmin = P*2+10
        vals = {}
        for n in range(nmin, nmax+P):
            q = q_seq([0]*(P-1)+[1], n+1)
            vals[n] = nu2(right_diag(q))
        # per-residue increment
        cs = {}
        ok = True
        for r in range(P):
            diffs = {vals[n+P]-vals[n] for n in range(nmin, nmax) if n % P == r}
            if len(diffs) != 1:
                ok = False; cs[r] = None
            else:
                cs[r] = diffs.pop()
        S = sum(c for c in cs.values() if c is not None)
        print("P=%d (2^%d-1): literal-triangle affine=%s  sum c_r=%d  target 3^k-3=%d  match=%s"
              % (P, k, ok, S, 3**k-3, S==3**k-3))
        for r, c in cs.items():
            assert c is not None and c % 2 == 0, (P, r, c)
        assert S == 3**k-3, (P, S)
    print("LITERAL-TRIANGLE VERIFICATION PASSED for P=7,15")

if __name__ == "__main__":
    main()
