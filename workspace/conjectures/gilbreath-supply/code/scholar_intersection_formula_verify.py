#!/usr/bin/env python3
"""Scholar verification of the load-bearing intersection formula of the adopted
downset-row-code-distance-closed-form line.

Claims under test (from research/approaches/downset-row-code-distance-closed-form.md,
flagged there as "NEW to this run, checked only by hand on 5 pairs at n=5,7"):

  (R) reflection:   M_d = { n-1-y : y subseteq d }           (translated down-set)
  (I) intersection: M_d ∩ M_{d'} = M_{d∧d'}                  (bitwise AND index)
  (S) size:         |M_d ∩ M_{d'}| = 2^{popcount(d∧d')}
  (D) distance:     |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d∧d')+1}

where M_d = { n-1-d+o : o subseteq d } is the depth-d row of the SUPPLY fold
Phi_n (d in [2,n-1]), and triangle is symmetric difference.

Every equality is checked by brute-force set construction and set algebra, for
ALL ordered pairs (d,d') in [2,n-1], for n = 8..256. All exact integer/set
arithmetic. Negative control: random point sets of the same sizes must FAIL (I).

No primes, no floats — pure set combinatorics of the fold.
"""
import random

def submasks(d):
    i = d
    while True:
        yield i
        if i == 0:
            break
        i = (i - 1) & d

def M_d(n, d):
    """Row M_d of Phi_n as a frozenset of positions in [0,n-1]."""
    return frozenset(n - 1 - d + o for o in submasks(d))

def popcount(x):
    return bin(x).count("1")

def verify_all(n):
    """Return a dict of per-property booleans for a single n."""
    rows = {d: M_d(n, d) for d in range(2, n)}
    ok = {k: True for k in ("R", "I", "S", "D")}
    for d in range(2, n):
        # (R) reflection
        reflected = frozenset(n - 1 - y for y in range(d + 1) if (y & d) == y)
        if reflected != rows[d]:
            ok["R"] = False
        for dp in range(2, n):
            inter = rows[d] & rows[dp]
            # (I) intersection indexed by bitwise AND
            if inter != rows[d & dp]:
                ok["I"] = False
            # (S) size formula
            if len(inter) != (1 << popcount(d & dp)):
                ok["S"] = False
            # (D) symmetric-difference formula
            sy = rows[d] ^ rows[dp]
            expect = (1 << popcount(d)) + (1 << popcount(dp)) - (1 << (popcount(d & dp) + 1))
            if len(sy) != expect:
                ok["D"] = False
    return ok

def random_fail_controls(n, trials=200):
    """Random point sets of the same card sizes must FAIL formula (I)."""
    failed = 0
    card = {d: len(M_d(n, d)) for d in range(2, n)}
    for _ in range(trials):
        d = random.randrange(2, n)
        dp = random.randrange(2, n)
        A = frozenset(random.sample(range(n), card[d]))
        B = frozenset(random.sample(range(n), card[dp]))
        # random sets: intersection size is NOT 2^{pc(d∧d')}
        if len(A & B) == (1 << popcount(d & dp)):
            failed += 1
    return failed

random.seed(17)
print("=== Intersection-formula verification (all d,d' in [2,n-1]) ===")
print(f"{'n':>4}  {'R-refl':>7} {'I-inter':>8} {'S-size':>7} {'D-dist':>7}")
all_ok = True
for n in [8, 16, 24, 32, 48, 64, 96, 128, 160, 192, 224, 256]:
    ok = verify_all(n)
    line = f"{n:>4}  " + "  ".join(f"{str(ok[k]):>7}" for k in ("R", "I", "S", "D"))
    print(line)
    if not all(ok.values()):
        all_ok = False
print()
print("ALL n in {8..256}: R,I,S,D all True:", all_ok)

print()
print("=== Negative control: random sets must FAIL (I) ===")
n = 64
failed = random_fail_controls(n, trials=200)
print(f"n={n}: of 200 random-set pairs, # for which |A&B|==2^{{pc(d∧d')}} = {failed}  "
      f"(expect 0..few; the formula must NOT hold generically)")

print()
print("=== Cross-check with lib.downset_rows row_dist (independent route) ===")
from lib.downset_rows import row_mask, row_dist
n = 128
agree = 0
for d in range(2, n):
    for dp in range(2, n):
        expect = (1 << popcount(d)) + (1 << popcount(dp)) - (1 << (popcount(d & dp) + 1))
        if row_dist(row_mask(n, d), row_mask(n, dp)) == expect:
            agree += 1
totalpairs = (n - 2) * (n - 2)
print(f"n={n}: distance formula agrees with lib.downset_rows.row_dist on "
      f"{agree}/{totalpairs} ordered pairs")
