#!/usr/bin/env python3
"""Run the R-intruder-4-always refutation oracles.

Attack the current open rung: For a 2-then-odds triangle with g_1 = 2, if the
block-boundary intruder value is 4 at every row where the leading block is
nonempty and finite, then A_k(0) = 1 for all k (leading block never dies).

Two sub-questions (both small-instance oracles, exact integer arithmetic):
  Q1: does any triangle within the searched gap classes DIE (A_k(0) != 1)
      while ALL live intruders equal 4?   -> refutes the rung
  Q2: is the all-zero leading block (1, 0^n, 4, ...) ever reached in the
      unconstrained 2-then-odds g_1=2 class?  -> refutes the candidate proof's
      unreachability step (rung may still hold via the intruder-4 hypothesis)
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


def scan(rows):
    """Return (hyp_holds_all_live, allzero_with4_list, death_info_or_None)."""
    hyp = True
    allzero = []
    death = None
    for k in range(len(rows) - 1):
        row = rows[k]
        b = blocklen(row)
        live = b >= 1 and b + 1 < len(row)
        if live:
            if row[b + 1] != 4:
                hyp = False
            if all(v == 0 for v in row[1:1 + b]) and row[b + 1] == 4:
                allzero.append((k, row[:b + 2]))
        if rows[k + 1][0] != 1:
            death = (k + 1, rows[k + 1][0])
            break
    return hyp, allzero, death


def main():
    classes = [(4, 12), (6, 9), (8, 8), (10, 7)]
    tot_allzero = 0
    death_hyp = 0
    for maxg, nmax in classes:
        choices = list(range(2, maxg + 1, 2))
        for ngap in range(2, nmax + 1):
            n_allzero = 0
            n_death = 0
            n_death_hyp = 0
            ex_allzero = None
            ex_death_hyp = None
            for rest in itertools.product(choices, repeat=ngap - 1):
                gaps = (2,) + rest
                rows = build(gaps)
                hyp, allzero, death = scan(rows)
                if allzero:
                    n_allzero += len(allzero)
                    if ex_allzero is None:
                        ex_allzero = allzero[0]
                if death is not None:
                    n_death += 1
                    if hyp:
                        n_death_hyp += 1
                        if ex_death_hyp is None:
                            ex_death_hyp = (gaps, death)
            tot_allzero += n_allzero
            print(f"[gaps<={maxg} ngap={ngap}] allzero-with-intruder4={n_allzero}"
                  f" deaths={n_death} death+intruder4-everywhere={n_death_hyp}")
            if n_death_hyp:
                print("  *** RUNG REFUTED *** example gaps", ex_death_hyp[0],
                      "death", ex_death_hyp[1])
                return 1
            if ex_allzero and n_allzero:
                pass
    print("\nTotals: all-zero-block rows (unconstrained class):", tot_allzero)
    print("Deaths with intruder-4-everywhere:", death_hyp)
    print("=> no counterexample to R-intruder-4-always in these finite classes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
