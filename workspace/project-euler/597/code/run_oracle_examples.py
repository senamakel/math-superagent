#!/usr/bin/env python3
"""Drive code/brute.py against every worked example in the PE597 statement.

Reproduces exactly what the naive oracle must give if the reading of the
definition is right:
  * the five n=3,L=160 bump-pattern rows (their new orders and parities are
    forced by the bump chains; we feed speed vectors that realize each pattern
    and check brute's reported order+parity);
  * the five row probabilities, whose forced total must be 1 and whose even
    rows must sum to 56/135 (MC over true Exp(1) speeds);
  * the two given values p(3,160)=56/135 and p(4,400)=0.5107843137 by MC.

This is the naive oracle check only; no efficient method here.
"""
import random
import math
from brute import simulate_order, parity_of_new_order, outcome_parity

N = 3
L = 160


def realize_speeds(n, L, desired_edges):
    """Return speeds realizing exactly the given bump edges under brute.
    We just try small random Exp draws until geometry matches."""
    for _ in range(200000):
        v = [random.expovariate(1.0) for _ in range(n)]
        above = simulate_order(n, L, v)
        # edges realized: for each a, the boats it directly bumped = neigh in edges
        # we don't have direct edges exposed; reconstruct from above chains is
        # ambiguous, so instead check the full race outcome (order+parity) which
        # is what the table lists.  We instead pick by outcome parity/order below.
        _ = above
    return None


def race_outcome(n, L, v):
    above = simulate_order(n, L, v)
    par, order = parity_of_new_order(n, above)
    return par, tuple(order)


# --- Five rows: choose speeds to force each pattern, then check order+parity ---
# Labels A=0 (lowest, pos 0), B=1 (pos 40), C=2 (pos 80). Finish L=160:
# finish times fA=160/v0, fB=120/v1, fC=80/v2. Catch a->b requires v_a>v_b at
# time 40(b-a)/(v_a-v_b) before the finish of a and not pre-empted.
rows = {
    "none":                (["A", "B", "C"], 0),
    "B bumps C":           (["A", "C", "B"], 1),
    "A bumps B":           (["B", "A", "C"], 1),
    "B bumps C then A bumps C": (["C", "A", "B"], 0),
    "A bumps B then B bumps C": (["C", "B", "A"], 1),
}
names = ["A", "B", "C"]

# hand-picked speed triples that realize each desired bump set
trials = {
    "none":
        # all finish in order A,B,C with no catch occurring: make speeds such that
        # no trailing boat catches ahead before its own finish.
        [[0.5, 0.9, 1.3], [0.4, 0.7, 1.0], [0.3, 0.6, 1.2]],
    "B bumps C":
        # B catches C (v1>v2, catch before B's finish 120/v1); A must not catch B.
        [[0.5, 1.2, 0.4], [0.3, 1.5, 0.5], [0.6, 2.0, 0.7]],
    "A bumps B":
        # A catches B before A's finish; B then must not catch C after (or we don't
        # mind A also later catching C? we want ONLY A bumps B).  Make B slow enough
        # that after being bumped it doesn't catch C, and A not reach C.
        [[1.2, 0.5, 1.5], [1.5, 0.6, 1.8], [1.0, 0.2, 2.0]],
    "B bumps C then A bumps C":
        # B bumps C, then A (nearest rowing is now C, B out) bumps C.
        [[0.7, 1.2, 0.4], [0.5, 1.6, 0.3]],
    "A bumps B then B bumps C":
        # A bumps B, then B (still rowing) bumps C.
        [[1.2, 1.5, 0.4], [1.6, 2.2, 0.5]],
}
names = {0: "A", 1: "B", 2: "C"}

def try_find(name, expected_order, expected_par):
    for v in trials[name]:
        par, order = race_outcome(N, L, v)
        o = [names[i] for i in order]
        if tuple(o) == tuple(expected_order) and par == expected_par:
            return True, v, (par, o)
    # fall back to random search
    for _ in range(200000):
        v = [random.expovariate(1.0) for _ in range(N)]
        par, order = race_outcome(N, L, v)
        o = [names[i] for i in order]
        if tuple(o) == tuple(expected_order) and par == expected_par:
            return True, v, (par, o)
    return False, None, None

print("=== Part A: realize each bump row, check order + parity ===")
allok = True
for name, (exp_order, exp_par) in rows.items():
    ok, v, got = try_find(name, exp_order, exp_par)
    if ok:
        print(f"  [OK] {name!r:34} -> new order {got[1]}  parity {'even' if got[0]==0 else 'odd'}"
              f"   (speeds {[round(x,4) for x in v]})")
    else:
        print(f"  [FAIL] {name!r}: could not realize in 200k random draws")
        allok = False
print("Part A:", "ALL PASS" if allok else "SOME FAIL")

# --- Part B: Monte Carlo the row probabilities (they must sum to 1; even rows 56/135)
print("\n=== Part B: MC over true Exp(1) speeds, n=3,L=160 ===")
NMC = 3_000_000
random.seed(12345)
counts = {}
even_rows = 0
for _ in range(NMC):
    v = [random.expovariate(1.0) for _ in range(N)]
    par, order = parity_of_new_order(N, simulate_order(N, L, v))
    key = tuple(names[i] for i in order)
    counts[key] = counts.get(key, 0) + 1
    if par == 0:
        even_rows += 1
tot = 0
print(f"  row probabilities (N={NMC}):")
for key in rows:
    c = counts.get(tuple(rows[key][0]), 0)
    exp = {"('A', 'B', 'C')": 4/15, "('A', 'C', 'B')": 8/45,
           "('B', 'A', 'C')": 1/3, "('C', 'A', 'B')": 4/27,
           "('C', 'B', 'A')": 2/27}[str(tuple(rows[key][0]))]
    mc = c / NMC
    tot += mc
    print(f"    {str(tuple(rows[key][0])):22} MC {mc:.6f}  exact {exp:.6f}  "
          f"diff {(mc-exp):+.6f}")
print(f"  sum of row probs = {tot:.6f}  (must be 1)")
print(f"  P(even) = {even_rows/NMC:.6f}   exact 56/135 = {56/135:.6f}")
print(f"  P(odd)  = {(1-even_rows/NMC):.6f}   exact 79/135 = {79/135:.6f}")

# --- Part C: MC the second given value ---
print("\n=== Part C: MC p(4,400) (given 0.5107843137) ===")
NMC4 = 3_000_000
random.seed(999)
even = 0
for _ in range(NMC4):
    v = [random.expovariate(1.0) for _ in range(4)]
    if outcome_parity(4, 400, v) == 0:
        even += 1
p = even / NMC4
se = (p * (1 - p) / NMC4) ** 0.5
print(f"  MC p(4,400) = {p:.6f} +/- {se:.6f}   given 0.5107843137 (within {abs(p-0.5107843137)/se:.1f} SE)")
