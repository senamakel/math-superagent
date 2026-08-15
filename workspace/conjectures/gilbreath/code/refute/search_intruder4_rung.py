#!/usr/bin/env python3
"""Refutation search for the current rung R-intruder-4-always.

For finite 2-then-odds triangles (g_1 = 2, even gaps in a bounded set),
compute the exact triangle and ask:

  Q-a (refutes the rung itself): does any triangle DIE (A_k(0) != 1) while
       ALL live intruders (rows where a nonempty {0,2} block has an intruder)
       equal 4?
  Q-b (refutes the candidate proof's unreachability sub-claim): does an
       all-zero leading block (1, 0^n, 4, ...) ever appear in the
       UNCONSTRAINED class?

The first is a genuine counterexample to the rung; the second is a
counterexample to the hand proof's unreachability step (the rung may still
hold if the intruder-4 hypothesis alone is what excludes all-zero).

Exhaustive over the stated gap classes and finite prefixes; a small-instance
oracle, not a proof.
"""
import itertools


def blocklen(row):
    b = 0
    for v in row[1:]:
        if v in (0, 2):
            b += 1
        else:
            break
    return b


def build(gaps):
    x = 3
    row0 = [2, 3]
    for g in gaps:
        x += g
        row0.append(x)
    rows = [row0]
    for _ in range(1, len(row0)):
        p = rows[-1]
        rows.append([abs(p[i] - p[i+1]) for i in range(len(p)-1)])
    return rows


def examine(maxg, ngap):
    choices = list(range(2, maxg + 1, 2))
    n_allzero = 0
    n_death = 0
    n_death_hyp = 0
    ex_allzero = None
    ex_death_hyp = None
    for rest in itertools.product(choices, repeat=ngap - 1):
        gaps = (2,) + rest
        rows = build(gaps)
        hyp = True
        death = None
        for k in range(len(rows) - 1):
            row = rows[k]
            b = blocklen(row)
            if b >= 1 and b + 1 < len(row) and row[b + 1] != 4:
                hyp = False
            if b >= 1 and all(v == 0 for v in row[1:1+b]) \
                    and b + 1 < len(row) and row[b + 1] == 4:
                n_allzero += 1
                if ex_allzero is None:
                    ex_allzero = (k, gaps, row[:b+2])
            if rows[k+1][0] != 1:
                death = (k+1, rows[k+1][0])
                break
        if death is not None:
            n_death += 1
            if hyp:
                n_death_hyp += 1
                if ex_death_hyp is None:
                    ex_death_hyp = (gaps, death)
    return n_allzero, n_death, n_death_hyp, ex_allzero, ex_death_hyp


def main():
    tot_allzero = 0
    for maxg, nmax in [(4, 11), (6, 8), (8, 7)]:
        for ngap in range(2, nmax + 1):
            na, nd, ndh, eaz, edh = examine(maxg, ngap)
            tot_allzero += na
            print(f"[gaps<={maxg} ngap={ngap}] allzero(with4)={na} "
                  f"deaths={nd} death+intruder4-everywhere={ndh}")
            if ndh:
                print("  *** RUNG REFUTED: death with intruder-4-everywhere ***")
                print("  example gaps:", edh[0], "death at", edh[1])
                return
            if eaz and na:
                print(f"  (all-zero example: row {eaz[0]} gaps={eaz[1]} "
                      f"block={eaz[2]})")
    print("\nTotals: all-zero-block rows in the unconstrained class:",
          tot_allzero)
    print("No death with intruder-4-everywhere in the searched classes "
          "(gaps<=8, g_1=2, ngap<=7..11). Small oracle, not a proof.")


if __name__ == "__main__":
    main()
