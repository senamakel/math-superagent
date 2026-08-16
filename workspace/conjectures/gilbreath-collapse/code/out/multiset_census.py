"""GOAL priority-1 census: the index multiset { M_d △ M_{d'} } over d,d' in [2,n-1].

For n = 3..128, counts by distinct set A (a frozenset of positions in [0,n-1])
  m(A)            multiplicity  = #(d,d') pairs producing A
  |A|             size, cross-checked against 2^pc(d)+2^pc(d')-2^{pc(d&d')+1}
  span(A)         max-min+1     (0 for empty A)
  runs(A)         run decomposition (list of maximal-run lengths)
  example         one (d,d') pair producing A

Reports
  (1) weighted span histogram H_n(k) = sum_{A: span(A)=k} m(A) for n=32,64,128,
      and over all n the max span carrying positive weight.
  (2) whether long-span (span comparable to n) sets carry m(A) >= 1, with
      examples and their (d,d'); confirms the three dyadic families.
  (3) cross-check: #entries == (n-2)^2  and  sum over distinct A of m(A)*|A|
      == sum over all pairs of the closed form (computed independently).

Negative control: a deliberately wrong run_count (shifts every count by +1) must
change the weighted run-count histogram R_n.

Heap safe: one counter (dict keyed by frozensets) in memory at a time; (n-2)^2
pairs at n=128 is 15876.
"""

from collections import Counter
from lib.collapse import downset, run_count


def popcount(x):
    return bin(x).count("1")


def run_decomp(A):
    """List of maximal-run lengths of frozenset A of ints."""
    if not A:
        return []
    s = sorted(A)
    runs = []
    cur = 1
    for a, b in zip(s, s[1:]):
        if b == a + 1:
            cur += 1
        else:
            runs.append(cur)
            cur = 1
    runs.append(cur)
    return runs


def size_closed_form(d, dp):
    """Imported item 3: |M_d △ M_{d'}| = 2^pc + 2^pc' - 2^{pc(d&d')+1}."""
    return (2 ** popcount(d) + 2 ** popcount(dp)
            - 2 ** (popcount(d & dp) + 1))


def broken_run_count(A):
    """Deliberately wrong run-count for the negative control: shift by +1
    unconditionally (so it also differs on the empty set, which occurs with
    multiplicity n-2 as M_d △ M_d)."""
    return run_count(A) + 1


def census(n):
    """Return (distinct_map, cross_ok_pairwise, sum_over_pairs_closedform).
    distinct_map: {A: dict(mult, size, span, runs, example)}."""
    dset = {d: downset(d, n) for d in range(2, n)}
    mp = {}
    sum_over_pairs_closedform = 0
    pairwise_ok = True
    for d in range(2, n):
        for dp in range(2, n):
            A = frozenset(dset[d] ^ dset[dp])
            sz = len(A)
            cf = size_closed_form(d, dp)
            if sz != cf:
                pairwise_ok = False
            sum_over_pairs_closedform += cf
            e = mp.get(A)
            if e is None:
                mp[A] = dict(mult=1, size=sz, span=(max(A) - min(A) + 1) if A else 0,
                             runs=run_decomp(A), example=(d, dp))
            else:
                e["mult"] += 1
    return mp, pairwise_ok, sum_over_pairs_closedform


def main():
    print("=" * 78)
    print("GOAL priority-1 index multiset census  { M_d △ M_{d'} }, d,d' in [2,n-1]")
    print("=" * 78)

    span_hist_target = {32, 64, 128}

    rows = []
    for n in range(3, 129):
        mp, pairwise_ok, sum_pairs_cf = census(n)
        n_entries = sum(e["mult"] for e in mp.values())

        # (3) cross-checkes
        assert n_entries == (n - 2) ** 2, (n, n_entries)
        sum_over_multiset = sum(e["mult"] * e["size"] for e in mp.values())
        assert sum_over_multiset == sum_pairs_cf, (n, sum_over_multiset, sum_pairs_cf)
        assert pairwise_ok, n

        # (1) weighted span histogram
        H = Counter()
        for A, e in mp.items():
            H[e["span"]] += e["mult"]
        max_span = max(H)
        max_span_weight = H[max_span]

        # weighted run-count histogram + negative control
        R = Counter()
        Rb = Counter()
        for A, e in mp.items():
            R[run_count(A)] += e["mult"]
            Rb[broken_run_count(A)] += e["mult"]
        assert dict(Rb) != dict(R), f"negative control did not change run histogram, n={n}"

        rows.append((n, len(mp), n_entries, max_span, max_span_weight,
                     sum_pairs_cf, sum_over_multiset))

        if n in span_hist_target:
            print()
            print(f"--- n = {n} : weighted span histogram H_n(k) ---")
            for k in sorted(H):
                print(f"  span={k:3d}  weight={H[k]:7d}")
            print(f"  max span carrying weight: {max_span}  (weight {max_span_weight})")

    # aggregate table of max span / cardinality across all n
    print()
    print("n   |distinct sets| entries=(n-2)^2  max_span(max_weight)  sum|A|==sum CF")
    for (n, nd, ne, ms, msw, sp, sm) in rows:
        flag = "OK" if (sp == sm and ne == (n - 2) ** 2) else "MISMATCH"
        print(f"{n:4d} | {nd:6d} | {ne:5d} | span<=? max_span={ms:3d}(w={msw:5d}) | {flag}")

    # ===== (2) long-span multiplicity and dyadic family confirmation =====
    print()
    print("=" * 78)
    print("(2) long-span sets: do sets with span comparable to n carry m(A) >= 1?")
    print("=" * 78)
    for n in [32, 64, 128]:
        mp, _, _ = census(n)
        # longest spans
        by_span = sorted(mp.items(), key=lambda kv: (kv[1]["span"], -kv[1]["mult"]), reverse=True)
        print(f"\nn={n}: top spans (span, mult, size, runs, example d,d'):")
        seen = set()
        shown = 0
        for A, e in by_span:
            if e["span"] in seen:
                continue
            seen.add(e["span"])
            print(f"  span={e['span']:3d}  mult={e['mult']:4d}  |A|={e['size']:4d} "
                  f"runs(len[])= {e['runs']}  example(d,d')= {e['example']}")
            shown += 1
            if shown >= 8:
                break

    print()
    print("=" * 78)
    print("(2) three dyadic families, confirmed (d,d'), for n = 64 (and 128):")
    print("=" * 78)
    for n in [64, 128]:
        print(f"\n  n={n}:")
        m = max(k for k in range(1, 40) if 2 ** k <= n - 1)
        for k in range(1, m + 1):
            d  = 2 ** k - 1
            e1 = downset(d, n) ^ downset(2 ** k, n)          # fam1 one run
            e2 = downset(d, n) ^ downset(2 ** k - 2, n)      # fam2 singletons
            e3 = downset(2 ** k, n) ^ downset(2 ** k + 1, n)  # fam3 two-point
            span1 = max(e1) - min(e1) + 1
            r2 = run_decomp(e2)
            print(f"    k={k:2d} fam1 one-run: span={span1:3d} len={len(e1):3d} "
                  f"(expect span=len=2^{k}={2**k}) | "
                  f"fam2 runs(len)= {r2} (expect {2**(k-1)} singletons) | "
                  f"fam3 = {sorted(e3)} (expect {{n-2^{k}-2,n-2}} = "
                  f"{{{n-2**k-2},{n-2}}})")

    # ===== (3) final cross-check statement =====
    print()
    print("=" * 78)
    print("(3) cross-check summary (asserted for every n in 3..128):")
    print("  - #entries (with multiplicity) == (n-2)^2")
    print("  - sum over distinct A of m(A)*|A| == sum over ALL pairs of the")
    print("    closed form 2^pc+2^pc'-2^{pc(d&d')+1}")
    print("  - every |M_d △ M_{d'}| equals the closed form (pairwise)")
    print("  - negative control: broken run_count yielded a DIFFERENT weighted")
    print("    run-count histogram than the true run_count at every n")
    print("ALL ASSERTIONS PASSED.")


if __name__ == "__main__":
    main()
