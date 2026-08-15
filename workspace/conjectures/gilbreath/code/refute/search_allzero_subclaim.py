#!/usr/bin/env python3
"""Refutation assault on the current-rung candidate proof (R-intruder-4-always).

The candidate proof's load-bearing sub-claim is:
  In any 2-then-odds triangle with g_1=2, the all-zero leading block
  A_k = (1, 0, 0, ..., 0, 4, ...) is UNREACHABLE.

We test this sub-claim directly: enumerate finite 2-then-odds gap sequences
(g_1 = 2, even gaps in a bounded set), build the EXACT triangle, and check
whether any all-zero block (1, 0^n, 4, ...) ever appears with n >= 1.

Two independent questions:
  Q2 (all-zero block reachable WITHOUT any hypothesis constraint, i.e. in the
      wider 2-then-odds g_1=2 class): if found, refutes the unconditional
      unreachability; the candidate proof would need the intruder-4 hypothesis
      to do the excluding.
  Q2b (all-zero block reachable WITH intruder-4-always-everywhere): this is
      the strongest refutation — it would refute the rung's sub-claim exactly
      as used.

We also compute, for each death, whether the intruder-4-everywhere hypothesis
held up to death (Q1: refutes the rung outright).
"""
import itertools, sys


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
    """Return (hyp_holds_up_to_row, allzero_with4_list, death_info)."""
    hyp = True
    allzero = []
    death = None
    for k in range(len(rows) - 1):
        row = rows[k]
        b = blocklen(row)
        if b >= 1 and b + 1 < len(row):
            if row[b + 1] != 4:
                hyp = False
        if b >= 1 and all(v == 0 for v in row[1:1+b]):
            if b + 1 < len(row) and row[b + 1] == 4:
                allzero.append((k, row[:b+2]))
        if rows[k+1][0] != 1:
            death = (k+1, rows[k+1][0])
            break
    return hyp, allzero, death


def main():
    show_deaths = "-d" in sys.argv[1:]
    az_any = 0
    az_hyp = 0
    death_hyp = 0
    for maxg, nmax in [(4, 11), (6, 8), (8, 7)]:
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
            print(f"[gaps<={maxg} ngap={ngap}] allzero-block-with-intruder4: "
                  f"{n_allzero} rows; deaths {n_death} (intruder4-everywhere "
                  f"deaths: {n_death_hyp})")
            if show_deaths and n_death:
                pass
            az_any += n_allzero
            az_hyp += n_death_hyp  # note: this counts hyp-deaths, not allzero-under-hyp
            death_hyp += n_death_hyp
    print("\nTotals: allzero-block rows (unconstrained):", az_any)
    print("deaths with intruder-4-everywhere:", death_hyp)


if __name__ == "__main__":
    main()
