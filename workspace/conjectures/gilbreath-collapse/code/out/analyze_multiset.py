"""Extract and dump exact structural sequences of the S2_char multiset for n=2..40.

For each n reports:
  num_distinct_sets  a(n)
  max_run_count      (multiplicity-weighted) largest run count present
  count_at_max_run   multiplicity of sets attaining max_run_count
  max_size           largest |M_d △ M_{d'}|
  max_multiplicity   largest multiplicity of a single set
  bulk1runs          multiplicity-weighted fraction of pairs whose A has <=1 run?? no -- compute shares.
Full distribution over run_count and over size is printed for n in a few sample values.
"""
from collections import Counter
from lib.collapse import S2_char, run_count


def main():
    from math import comb
    rows = []
    for n in range(2, 41):
        c = S2_char(n)
        by_runs = Counter()
        by_size = Counter()
        for A, mult in c.items():
            by_runs[run_count(A)] += mult
            by_size[len(A)] += mult
        num = len(c)
        maxrun = max(by_runs) if by_runs else 0
        maxsize = max(by_size) if by_size else 0
        maxmult = max(c.values()) if c else 0
        # predicted closed form
        pred = 1 + comb(n - 2, 2) if n >= 3 else 0
        ok = (num == pred)
        rows.append((n, num, pred, ok, maxrun, maxsize, maxmult,
                     by_runs.get(maxrun, 0)))
        print(f"n={n:2d} distinct={num:5d} pred={pred:5d} ok={ok} "
              f"maxrun={maxrun} maxsize={maxsize} maxmult={maxmult} "
              f"mult_at_maxrun={by_runs.get(maxrun,0)}")
    # collapse check: what fraction of pairs (by multiplicity) have A with FEW runs?
    print("\nBulk concentration: for selected n, multiplicity share of pairs by run_count")
    for n in [8, 12, 16, 20, 24, 32, 40]:
        c = S2_char(n)
        by_runs = Counter()
        for A, mult in c.items():
            by_runs[run_count(A)] += mult
        total = sum(by_runs.values())
        order = sorted(by_runs)
        cum = 0
        parts = []
        for r in order:
            cum += by_runs[r]
            parts.append(f"r={r}:{by_runs[r]}")
        print(f"n={n} total_pairs={total} " + " ".join(parts))
        # share with run_count <= 2
        le2 = sum(v for r, v in by_runs.items() if r <= 2)
        print(f"   share run_count<=2: {le2}/{total} = {le2/total:.3f}   "
              f"share run_count>=4: {total-le2 if False else sum(v for r,v in by_runs.items() if r>=4)}")
    print("\nmax_run_count raw sequence:")
    print([r[4] for r in rows])
    print("distinct-sets sequence:")
    print([r[1] for r in rows])


if __name__ == "__main__":
    main()
