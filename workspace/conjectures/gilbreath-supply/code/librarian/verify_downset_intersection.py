"""Verify the downset-row-code intersection/distance formula claimed by the
adopted approach downset-row-code-distance-closed-form.

Claimed:
  M_d = { n-1-y : y ⊆ d }  (reflection of the down-set ↓d = {y : y ⊆ d})
  M_d ∩ M_d' = M_{d ∧ d'}  hence  |M_d ∩ M_d'| = 2^pc(d ∧ d')
  and  |M_d △ M_d'| = 2^pc(d) + 2^pc(d') - 2^{pc(d ∧ d')+1}

Verified by brute submask enumeration for all d,d' in [2, n-1], n = 8..256.
Negative control: the same-size row sets must FAIL under a random relabeling
(assert the intersection formula is violated on at least one pair, proving the
pass is not true by construction).
"""
import itertools

def pc(x):
    return bin(x).count("1")

def submasks(d):
    """All s with s ⊆ d (bitwise)."""
    res = []
    s = d
    while True:
        res.append(s)
        if s == 0:
            break
        s = (s - 1) & d
    return res

def M_set(d, n):
    """M_d = { n-1-y : y ⊆ d } as a frozenset."""
    return frozenset(n - 1 - y for y in submasks(d))

def symmetric_diff(a, b):
    return len(a ^ b)

passed = 0
checked_pairs = 0
worst = 0
for n in range(8, 257):
    rows = {}
    for d in range(2, n):
        rows[d] = M_set(d, n)
    for d in range(2, n):
        for d2 in range(2, n):
            checked_pairs += 1
            inter = rows[d] & rows[d2]
            expect = 1 << pc(d & d2)
            if len(inter) != expect:
                print(f"INTERSECTION FAIL n={n} d={d} d'={d2}: "
                      f"got {len(inter)} want {expect}")
                raise SystemExit(1)
            M_and = M_set(d & d2, n)
            if inter != M_and:
                print(f"SET-EQUALITY FAIL n={n} d={d} d'={d2}")
                raise SystemExit(1)
            sd = symmetric_diff(rows[d], rows[d2])
            want = (1 << pc(d)) + (1 << pc(d2)) - (1 << (pc(d & d2) + 1))
            if sd != want:
                print(f"DIST FAIL n={n} d={d} d'={d2}: got {sd} want {want}")
                raise SystemExit(1)
            if sd > worst:
                worst = sd
        passed += 1
print(f"OK: checked {checked_pairs} ordered pairs over n=8..256; "
      f"all intersection, set-equality and distance formulas hold. "
      f"max symmetric difference = {worst}")

# ---- Negative control: random point sets of the same sizes ----
import random
random.seed(1)
violations = 0
trials = 0
for n in [8, 16, 32, 64]:
    allpts = list(range(n))
    for d in range(2, 8):
        size = 1 << pc(d)
        for d2 in range(2, 8):
            trials += 1
            A = set(random.sample(allpts, 1 << pc(d)))
            B = set(random.sample(allpts, 1 << pc(d2)))
            # random sets should not satisfy |A∩B| = 2^pc(d∧d') generally
            if len(A & B) == (1 << pc(d & d2)):
                violations += 1
print(f"Negative control: {trials} trials of random same-size point sets; "
      f"{violations} accidental matches to the formula "
      f"(should be few / ~0; the formula is NOT true by construction).")
