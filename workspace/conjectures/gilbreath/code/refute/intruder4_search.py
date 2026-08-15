#!/usr/bin/env python3
"""Attack R-intruder-4-always.

Claim: For a 2-then-odds triangle with g_1=2 (A_1=(1,2,g2,g3,...) all even),
IF the block-boundary intruder y_k = A_k(b_k+1) = 4 at EVERY row where the
leading {0,2} block is nonempty and finite, THEN A_k(0)=1 for all k (the
leading block never dies).

Equivalent: there is NO input where all intruders are 4 yet the block dies.

Hunt: enumerate 2-then-odds inputs (even gaps in {2,4,6,...}) over a depth
window, compute the triangle, track b_k and y_k, and report any input where
(a) every intruder with nonempty block equals 4, BUT (b) the block dies
(b_k = 0, i.e. A_k(1) not in {0,2}) before width runs out.

Also report intruder values at death row, to understand the death mode.
"""
from itertools import product

def child(row):
    return [abs(row[i]-row[i+1]) for i in range(len(row)-1)]

def block_len(row):
    n = 0
    for x in row[1:]:
        if x in (0,2):
            n += 1
        else:
            break
    return n

def run_triangle(gaps, depth):
    """gaps = [g1, g2, ...] even, g1 must be 2. A_1 = (1,2,g2,g3,...)."""
    row = [1, 2] + list(gaps[1:])
    for k in range(depth):
        b = block_len(row)
        yield k, row, b
        row = child(row)

def check(gaps, depth):
    """Return (violated_hyp, died, first_death_row, intruders_log)."""
    log = []
    died_at = None
    hyp_violated = False
    for k, row, b in run_triangle(gaps, depth):
        if b < 0:
            break
        # intruder at y_k = row[b+1] if block nonempty and finite (b >= 1)
        if b >= 1 and b + 1 < len(row):
            y = row[b+1]
            log.append((k, b, y))
            if y != 4:
                hyp_violated = True
        # death: row[1] not in {0,2} while previous was fine
        if len(row) >= 2 and row[1] not in (0, 2):
            if died_at is None:
                died_at = k
    return hyp_violated, died_at, log

def main():
    # search odd-factor even-gap alphabets
    best = None
    n_hyp_holds_death = 0
    for m in (3, 4, 5):                      # gaps in {2,4,...,2m}
        gapsyms = range(2, 2*m+1, 2)
        depth = 14
        for n_gaps in (3, 4, 5, 6, 7):
            for gaps in product(gapsyms, repeat=n_gaps):
                g = list(gaps)
                g[0] = 2 if len(g) > 0 else 2   # force g_1 = 2
                if len(g) < 1 or g[0] != 2:
                    g = [2] + list(g[1:])
                hyp_violated, died_at, log = check(g, depth)
                if not hyp_violated and died_at is not None:
                    n_hyp_holds_death += 1
                    if n_hyp_holds_death <= 5:
                        print(f"COUNTEREXAMPLE: gaps={g} death at row {died_at}")
                        for ent in log:
                            print(f"   row {ent[0]}: b={ent[1]} intruder={ent[2]}")
    print(f"\nTotal inputs where hypothesis holds AND block dies: {n_hyp_holds_death}")
    if n_hyp_holds_death == 0:
        print("No counterexample found in this search space (hypothesis-vs-death).")

if __name__ == "__main__":
    main()
