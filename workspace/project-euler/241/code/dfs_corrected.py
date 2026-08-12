"""Corrected denominator-cancellation DFS for PE241 (hemiperfect numbers).

Ground truth: OEIS A159907 b-file prefix (research/sources/A159907_bterm.full.md).
This solver must reproduce, for any LIMIT, exactly the b-file terms <= LIMIT.

FORCING LEMMA (correct version).  At a node with reduced residual
Q = num/den  (Q = (r/2)*n/sigma(n)), any completion c satisfies
den | c  (from num*c = den*sigma(c) and gcd(num,den)=1).  Primes are added in
nondecreasing order, so all primes of c are >= the next chosen prime q.
Therefore, if d = smallest prime factor of den, every live next-prime choice
q must satisfy  q <= d  (if q > d then d | c is impossible).  So the search
tries q in [current pointer .. d] and BREAKS when q exceeds d.  This is the
opposite of "skip p < d": a next prime *smaller* than d stays legal (its
sigma(p^e) factors may be absorbed by the numerator, and the d is still
cleared later by adding d itself).

When den == 1 the residual is an integer num >= 2 and the next prime is
unbounded (capped at MAXP for practical purposes; all known solutions far
below any cap in effect).

Exponent loops: e >= 1 always (sound: p^e must cancel p^v_p(den) and any
surplus stays in the numerator for later sigma-factors to absorb).
Prunes: Q' < 1 (monotone in e; break), n*p^e > LIMIT (break), and
"completion too big": n*p^e*(den'/gcd) > LIMIT (skip that e, don't break --
the gcd can jump non-monotonically).
"""
import sys
from math import gcd
from sympy import primerange

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 10**18
MAXP = 10**6
PRIMES = list(primerange(2, MAXP + 1))


def sigma_pe(p, e):
    return (p ** (e + 1) - 1) // (p - 1)


def min_factor(x):
    if x < 2:
        return x
    for p in PRIMES:
        if p * p > x:
            return x
        if x % p == 0:
            return p
    return x


solutions = {}
nodes = 0
den1_nodes = 0


def dfs(r, idx, n, num, den):
    global nodes, den1_nodes
    g = gcd(num, den)
    if g != 1:
        num //= g
        den //= g
    if num == 1 and den == 1:
        solutions.setdefault(r, set()).add(n)
        return
    if num < den:
        return
    if n > LIMIT:
        return
    nodes += 1

    if den == 1:
        den1_nodes += 1
        # free choice: any prime >= pointer, any exponent >= 1
        for i in range(idx, len(PRIMES)):
            p = PRIMES[i]
            e = 1
            pe = p
            while n * pe <= LIMIT:
                sp = sigma_pe(p, e)
                num2, den2 = num * pe, den * sp
                if num2 < den2:
                    break
                if n * pe * (den2 // gcd(num2, den2)) > LIMIT:
                    e += 1
                    pe *= p
                    continue
                dfs(r, i + 1, n * pe, num2, den2)
                e += 1
                pe *= p
        return

    d = min_factor(den)
    for i in range(idx, len(PRIMES)):
        p = PRIMES[i]
        if p > d:
            break
        e = 1
        pe = p
        while n * pe <= LIMIT:
            sp = sigma_pe(p, e)
            num2, den2 = num * pe, den * sp
            if num2 < den2:
                break
            if n * pe * (den2 // gcd(num2, den2)) > LIMIT:
                e += 1
                pe *= p
                continue
            dfs(r, i + 1, n * pe, num2, den2)
            e += 1
            pe *= p


# OEIS A159907 b-file ground truth
BTERMS = [2,24,4320,4680,26208,8910720,17428320,20427264,91963648,197064960,
8583644160,10200236032,21857648640,57575890944,57629644800,206166804480,
17116004505600,1416963251404800,15338300494970880,75462255348480000,
88898072401645056,301183421949935616,6219051710415667200]

def main():
    for r in range(3, 27, 2):
        dfs(r, 0, 1, r, 2)
    allsol = set()
    for r in sorted(solutions):
        sols = sorted(s for s in solutions[r] if s <= LIMIT)
        allsol.update(sols)
        print(f"r/2 = {r}/2 : {len(sols)} solutions, sum={sum(sols)}")
    allsol = sorted(allsol)
    expected = sorted(n for n in BTERMS if n <= LIMIT)
    print(f"\nLIMIT = {LIMIT}")
    print("solutions:", allsol)
    print("count =", len(allsol), " sum =", sum(allsol))
    print("expected count =", len(expected), " sum =", sum(expected))
    print("sets equal:", allsol == expected)
    if allsol != expected:
        print("  only-in-solver:", sorted(set(allsol) - set(expected)))
        print("  only-in-bfile: ", sorted(set(expected) - set(allsol)))
    print("nodes =", nodes, " den==1 nodes =", den1_nodes)


if __name__ == "__main__":
    main()