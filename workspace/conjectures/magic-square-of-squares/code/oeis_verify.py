#!/usr/bin/env python3
"""Scholar verification of the OEIS catalogue summaries.

Standalone, exact integer arithmetic, no sympy.  Facts:

A006339(n) = min h with h^2 a sum of two squares in exactly n ways
             (counting the degenerate (0,h) representation).
A046112(n) = min r with 8n-4 lattice points on x^2+y^2 = r^2.
For h = prod p_i^{a_i}, the count including the axis representation is
    ( prod_{p_i = 1 mod 4} (2 a_i + 1) + 1 ) / 2
so  A006339(n) = A046112(n) = min h with prod(2 a_i + 1) = 2n - 1.
(2 and p = 3 mod 4 primes never appear in a minimal h.)

This is the SAME function as this run's |S(e)| = #{d>0: e^2 +/- d squares}
= (prod(2a+1) - 1)/2  (ap_structure2.py; verified vs x-loop e<=1500).
Consequences (checked here against the run's own exhaustive output
pattern_seq_output.txt):
  A088959 record-holder list 1,5,25,65,325,1105,5525,27625,32045,160225,
     801125,1185665,5928325  ==  the run's S3 record-holder e's (e <= 10^7);
  A088111 record values 0,1,2,4,7,13,22,31,40,67,94,121,202 == the run's
     S2 record |S(e)| values.

Routes:
  A  exact backtracking over products of primes 1 mod 4, prod exactly 2n-1;
  B  brute force: count primitive Pythagorean triples with hypotenuse | h
     by sieving h <= NB; compare R(h) = (prod-1)/2 on the whole range;
  C  full sweep e <= 10^7 via a product sieve, recovering the record lists.
The OEIS term lists and the run's S2/S3 lists are embedded ONLY as
comparison literals.
"""
import math

# ---------- primes 1 mod 4 ----------
def primes_1mod4(limit):
    out = []
    for p in range(5, limit + 1, 4):
        if all(p % q for q in range(3, math.isqrt(p) + 1, 2)):
            out.append(p)
    return out

PRIMES = primes_1mod4(4000)

# ---------- route A ----------
def min_h_for_exact_prod(T, bound=1 << 96):
    """min h (product of prime powers, all primes 1 mod 4) with
    prod(2 a_i + 1) == T, or None."""
    best = [None]
    def rec(idx, h, prod):
        if prod == T:
            if best[0] is None or h < best[0]:
                best[0] = h
            return
        if prod > T or (best[0] is not None and h >= best[0]):
            return
        for j in range(idx, len(PRIMES)):
            p = PRIMES[j]
            if h * p > bound:
                break
            hh, a = h * p, 1
            while hh <= bound and prod * (2 * a + 1) <= T:
                rec(j + 1, hh, prod * (2 * a + 1))
                a += 1
                if hh > bound // p:
                    break
                hh *= p
    rec(0, 1, 1)
    return best[0]

def routeA():
    return [min_h_for_exact_prod(2 * n - 1) for n in range(1, 31)]

# ---------- route B ----------
def R_by_triples(NB):
    R = [0] * (NB + 1)
    for u in range(2, math.isqrt(NB) + 1):
        for v in range(1, u):
            if (u - v) % 2 == 0 or math.gcd(u, v) != 1:
                continue
            s = u * u + v * v
            if s > NB:
                break
            for k in range(s, NB + 1, s):
                R[k] += 1
    return R

def prod_1mod4(h):
    prod, x, d = 1, h, 2
    while d * d <= x:
        if x % d == 0:
            a = 0
            while x % d == 0:
                x //= d
                a += 1
            if d % 4 == 1:
                prod *= 2 * a + 1
        d += 1
    if x > 1 and x % 4 == 1:
        prod *= 3
    return prod

# ---------- route C: record sweep e <= 10^7 ----------
def record_sweep(N):
    prod = [1] * (N + 1)
    for p in PRIMES:
        if p > N:
            break
        pk = p
        a = 1
        while pk <= N:
            for m in range(pk, N + 1, pk):
                prod[m] *= (2 * a + 1)
            pk *= p
            a += 1
    S = [(v - 1) // 2 for v in prod]
    records, holders, best = [], [], -1
    for e in range(1, N + 1):
        if S[e] > best:
            best = S[e]
            records.append(S[e])
            holders.append(e)
    return S, records, holders

# ---------- comparison literals ----------
A006339_LISTED = [1,5,25,125,65,3125,15625,325,390625,1953125,1625,48828125,
    4225,1105,6103515625,30517578125,40625,21125,3814697265625,203125,
    95367431640625,476837158203125,5525,11920928955078125,274625,5078125,
    1490116119384765625,528125,25390625,186264514923095703125]
A046112_LISTED = [1,5,25,125,65,3125,15625,325,390625,1953125,1625,48828125,
    4225,1105,6103515625,30517578125,40625,21125,3814697265625,203125,
    95367431640625,476837158203125,5525,11920928955078125,274625]
S2_RUN = [0,1,2,4,7,13,22,31,40,67,94,121,202]          # pattern_seq_output.txt
S3_RUN = [1,5,25,65,325,1105,5525,27625,32045,160225,     # pattern_seq_output.txt
          801125,1185665,5928325]
A088959_LISTED = [1,5,25,65,325,1105,5525,27625,32045,160225,
                  801125,1185665,5928325,29641625,48612265]

def main():
    a6 = routeA()
    print("A006339 computed (n=1..30):")
    print(a6)
    print("matches OEIS::A006339 listed:", a6 == A006339_LISTED)
    for i, (c, l) in enumerate(zip(a6, A006339_LISTED), 1):
        if c != l:
            print(f"  MISMATCH A006339({i}): computed {c}, listed {l}")
    print("A006339 == A046112 (first 25 identity):",
          a6[:25] == A046112_LISTED)

    NB = 60000
    R = R_by_triples(NB)
    bad = [h for h in range(1, NB + 1) if R[h] != (prod_1mod4(h) - 1) // 2]
    print(f"Route B (primitive-triple count) vs formula, h <= {NB}:",
          "mismatches:", len(bad), bad[:5])
    Rtot = [R[h] + 1 for h in range(NB + 1)]   # include axis representation
    min_eq = {}
    for h in range(1, NB + 1):
        if Rtot[h] not in min_eq:
            min_eq[Rtot[h]] = h
    for n in range(1, 31):
        v = min_eq.get(n)
        if v is not None and v == a6[n - 1]:
            print(f"  A006339({n}) = {a6[n-1]}  [brute-force OK]")
        elif v is not None:
            print(f"  A006339({n}) = {a6[n-1]}  [brute gives {v} MISMATCH]")

    N = 10_000_000
    S, records, holders = record_sweep(N)
    print(f"\nRecord sweep e <= {N}: {len(records)} records")
    print("record values:", records)
    print("record holders:", holders)
    print("S2 (run) == records:", S2_RUN == records)
    print("S3 (run) == holders:", S3_RUN == holders)
    print("A088959 first 13 == holders:",
          A088959_LISTED[:13] == holders)
    print("A088111 first 13 == records:", S2_RUN == records)
    print("max |S(e)| e<=1e7 =", records[-1], "at e =", holders[-1])

if __name__ == "__main__":
    main()