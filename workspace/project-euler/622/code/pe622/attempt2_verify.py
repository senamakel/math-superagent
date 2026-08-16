#!/usr/bin/env python3
"""
PE622 — fresh, obviously-correct verification and computation (attempt 2).

Problem: out-faro (perfect riffle) shuffle on an even deck of size n preserves
the top and bottom cards.  s(n) = minimum number of consecutive out-faro
shuffles needed to restore the deck.  s(52)=8, s(86)=8, and the sum of even n
with s(n)=8 is 412 (n in {18,52,86,256}).  Find the sum of all even n with
s(n)=60.

This script is completely self-contained and deliberately simple:

Part A — DIRECT SIMULATION.  Implement the out-faro shuffle exactly as the
problem describes it: split the even deck into two equal halves, top half in
the left hand, bottom half in the right hand, then interleave so the top card
of the right half goes just after the top card of the left half, the 2nd right
card just after the 2nd left card, etc.  This fixes the top and bottom cards.
s(n) is the number of such shuffles until the deck returns to its original
order.  Reproduce every stated worked example with this simulation only.

Part B — cross-check: for every even deck size 2..80, confirm that the
brute-force out-shuffle order equals ord_{n-1}(2), the multiplicative order of
2 mod (n-1).  Confirm that the s(n)=8 set is {18,52,86,256} with sum 412.

Part C — structural answer with EXACT integer arithmetic, no search over n:
  ord_m(2) = 60  <=>  2^60 == 1 (mod m)  and  2^(60/p) != 1 (mod m) for each
                       prime p | 60  (p in {2,3,5}).
The first condition forces m | 2^60 - 1 = N.  So m ranges over the divisors of
N (a 60-bit number — 4608 of them), not over all integers up to any bound.
Each qualifying m is odd, so n = m + 1 is even.  ANSWER = sum over qualifying
m of (m+1) = (sum of m) + (count of m).

No published PE622 answer is used anywhere; the number is derived only from the
reduction reproduced and cross-checked in Parts A and B.
"""
from math import gcd


# ---------------------------------------------------------------------------
# Part A: direct simulation of the out-faro shuffle
# ---------------------------------------------------------------------------
def out_shuffle(deck):
    """One perfect out-shuffle of an even-length deck, per the problem text.

    Split into two equal halves (top half left, bottom half right), then
    interleave exactly: right's top card just after left's top card, right's
    2nd just after left's 2nd, etc.  The top and bottom deck positions are
    preserved (they are the first card of the left half and the last card of
    the right half).
    """
    n = len(deck)
    assert n % 2 == 0
    half = n // 2
    top = deck[:half]      # left hand
    bot = deck[half:]      # right hand
    out = []
    for i in range(half):
        out.append(top[i])
        out.append(bot[i])
    return out


def s_oracle(n):
    """Brute-force: minimum out-faro shuffles to restore an even deck of n."""
    original = list(range(n))
    deck = list(original)
    count = 0
    while True:
        deck = out_shuffle(deck)
        count += 1
        if deck == original:
            return count


print("=" * 72)
print("PART A: direct simulation — reproduce every stated worked example")
print("=" * 72)
sim_52 = s_oracle(52)
sim_86 = s_oracle(86)
print("s(52) [direct simulation] =", sim_52)
print("s(86) [direct simulation] =", sim_86)
assert sim_52 == 8
assert sim_86 == 8

# Sum of all even n with s(n)=8 by direct simulation (true sum is 412).
sim_vals8 = []
sim_sum8 = 0
for n in range(2, 500, 2):
    if s_oracle(n) == 8:
        sim_vals8.append(n)
        sim_sum8 += n
print("even n with s(n)=8 [direct simulation] =", sim_vals8)
print("sum of even n with s(n)=8 [direct simulation] =", sim_sum8)
assert sim_vals8 == [18, 52, 86, 256]
assert sim_sum8 == 412
print("Worked examples reproduced by DIRECT SIMULATION: 8, 8, 412.\n")


# ---------------------------------------------------------------------------
# Part B: cross-check the reduction s(n) == ord_{n-1}(2) on small even decks
# ---------------------------------------------------------------------------
def ord_mod(a, m):
    """Smallest r>0 with a^r == 1 (mod m); None if gcd(a,m) != 1. Exact ints."""
    if m == 1:
        return 1
    if gcd(a, m) != 1:
        return None
    r, val = 0, 1
    while True:
        r += 1
        val = (val * a) % m
        if val == 1:
            return r


print("=" * 72)
print("PART B: cross-check s(n) == ord_{n-1}(2) on even decks 2..80")
print("=" * 72)
for n in range(2, 82, 2):
    bf = s_oracle(n)
    od = ord_mod(2, n - 1)
    assert bf == od, (n, bf, od)
    if n <= 20:
        print(f"  n={n:3d}: s(n)={bf}  ord_{n-1}(2)={od}  match={bf==od}")
print("All even n in 2..80 match: brute-force out-shuffle order == ord_{n-1}(2).")
print()


# ---------------------------------------------------------------------------
# Part C: structural answer via exact divisor enumeration of 2^60-1
# ---------------------------------------------------------------------------
print("=" * 72)
print("PART C: answer — enumerate divisors of 2^60 - 1 with ord_m(2)=60")
print("=" * 72)
N = 2**60 - 1
print("N = 2^60 - 1 =", N)

# Factor N exactly (trial division is fine; N is a 60-bit number).
def factorint(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

fac = factorint(N)
print("factorisation of N:", fac)

# Prime divisors of 60.
primes60 = [p for p in (2, 3, 5) if 60 % p == 0]
print("prime divisors of 60:", primes60)


def enumerate_divisors(fac):
    """All divisors of a number given by its {prime: exponent} factorisation."""
    items = list(fac.items())
    divs = [1]
    for p, e in items:
        new = []
        pe = 1
        for _ in range(e + 1):
            for d in divs:
                new.append(d * pe)
            pe *= p
        divs = new
    return divs


divisors_N = enumerate_divisors(fac)


def has_order_60(m):
    """True iff ord_m(2) == 60, checked via the two exact criteria."""
    if m <= 1:
        return False
    if N % m != 0:                      # 2^60 == 1 (mod m)  <=>  m | 2^60-1
        return False
    for p in primes60:
        if pow(2, 60 // p, m) == 1:     # a proper divisor power already == 1
            return False                # -> order < 60
    return True


good = [m for m in divisors_N if has_order_60(m)]
S = sum(good)          # sum of qualifying m
C = len(good)          # count of qualifying m

print("total divisors of N:", len(divisors_N))
print("count C of m with ord_m(2)=60:", C)
print("sum S of those m:", S)
answer = S + C
print("ANSWER = S + C =", answer)

# Independent check of the ord criterion on every divisor, via direct
# multiplicative-order iteration (different algorithm from the 60/p test).
def ord_mod(a, m):
    if m == 1:
        return 1
    if gcd(a, m) != 1:
        return None
    r, val = 0, 1
    while True:
        r += 1
        val = (val * a) % m
        if val == 1:
            return r

direct_good = [m for m in divisors_N if m > 1 and ord_mod(2, m) == 60]
direct_S = sum(direct_good)
direct_C = len(direct_good)
print("independent direct-ord route: C =", direct_C, " S =", direct_S)
assert sorted(good) == sorted(direct_good)
assert C == direct_C and S == direct_S
print("Two independent routes agree exactly.\n")
print("FINAL ANSWER =", answer)
