"""Split-(k-)gon spectrum of the VERIFIED lib/es_construct ES construction.

Two conventions (reported side by side to avoid conflating them):

(A) PAPER convention (Baek-Balko SoCG 2025, Section 2.1):
      a split k-gon = an a-cap and a u-cup that share the RIGHTMOST point
      with a + u = k + 2.  Its union has k or k+1 points (k if the chains
      also share the leftmost point).  ESsplit(k) = 2^{k-2}+1 (their Thm 3).
      So at 32 points (n=7): a paper split 6-gon (a+u=8) is FORCED
      (17 <= 32); a paper split 7-gon (a+u=9) is NOT forced (33 > 32).
      es_construct at a=u=k is the paper's tightness witness: it should
      contain a paper split (n-1)-gon but NO paper split n-gon.

(B) TASK convention (the concrete cup+cap object requested):
      an a-element cup and a u-element cap with the SAME rightmost-by-x
      vertex q, all other elements strictly left of q; "split size" =
      |cup u cap| (union size).  We tabulate existence per (a,u) for
      union size <= 7 and report the maximum union size, specifically
      whether a split of union 7 ("split 7-gon (union 7)") exists.

All cup/cap tests are exact (Fraction slope comparisons on the x-sorted
chain), via lib.cupcap.is_cup / is_cap.  Chains are generated directly by
DFS (never the whole subset space) and validated against an exhaustive
probe (`split_probe.py`) — see `split_chain_enum.py`.

Also re-verified: the even/odd block bipartition halves of es_construct(7)
(even T0/T2/T4 = 16 pts, odd T1/T3/T5 = 16 pts) must each be 6-avoiding
(no convex 6-gon), plus longest cup and longest cap of the full 32-point set.
"""
import time
from collections import defaultdict
from fractions import Fraction

from lib.es_construct import es_set, es_set_blocks
from lib.cupcap import is_cup, is_cap
from lib.es_geom import in_general_position, has_convex_k_subset, \
    largest_convex_subset, longest_cup, longest_cap
from lib.chainenum import chains_by_rightmost


def rank_of_rightmost(pts, xorder=None):
    N = len(pts)
    xorder = xorder or sorted(range(N), key=lambda i: Fraction(pts[i][0]))
    return {i: r for r, i in enumerate(xorder)}


def has_chain_sizes_by_rank(chains_by_rm):
    """has[size] = set of rightmost ranks having a chain of that size."""
    has = defaultdict(set)
    for rm, lst in chains_by_rm.items():
        for fs in lst:
            has[len(fs)].add(rm)
    return has


def compute_spectrum(n, max_s=7):
    pts = es_set(n)
    N = len(pts)
    gp = in_general_position(pts)
    xorder = sorted(range(N), key=lambda i: Fraction(pts[i][0]))
    xrank = rank_of_rightmost(pts, xorder)

    cups_by_rm, caps_by_rm = chains_by_rightmost(pts, max_s)
    cups_size_has = has_chain_sizes_by_rank(cups_by_rm)
    caps_size_has = has_chain_sizes_by_rank(caps_by_rm)

    # ---- (A) paper convention: max a+u over (a-cap, u-cup) sharing rightmost
    # max cap size per rank, max cup size per rank
    cmax_rank = defaultdict(int)
    for rm, lst in caps_by_rm.items():
        cmax_rank[rm] = max((len(fs) for fs in lst), default=0)
    umax_rank = defaultdict(int)
    for rm, lst in cups_by_rm.items():
        umax_rank[rm] = max((len(fs) for fs in lst), default=0)
    paper_max_au = 0
    paper_witness = None
    for rm in set(cmax_rank) | set(umax_rank):
        au = cmax_rank[rm] + umax_rank[rm]
        if au > paper_max_au:
            paper_max_au = au
            paper_witness = (cmax_rank[rm], umax_rank[rm], rm)
    paper_max_k = paper_max_au - 2  # k = a+u-2

    # does a paper split-k exist (a-cap+u-cup with a+u=k+2 sharing a rightmost)?
    paper_split_exists = {}
    for k in range(4, max_s + 1):
        need_au = k + 2
        found = False
        for rm in set(cmax_rank) & set(umax_rank):
            if cmax_rank[rm] + umax_rank[rm] >= need_au:
                # specific sizes: does a cap of size a and cup of size u with
                # a+u=need_au share rm?
                for a in range(2, need_au - 1):
                    u = need_au - a
                    if cmax_rank[rm] >= a and umax_rank[rm] >= u and \
                       rm in caps_size_has.get(a, set()) and \
                       rm in cups_size_has.get(u, set()):
                        found = True
                        break
                if found:
                    break
        paper_split_exists[k] = found

    # ---- (B) task convention
    # table for union <= 7
    table = {}   # (a,u) -> 'union<=7 exists' (bool)
    # cells with a+u <= 8: YES iff some rank has both an a-cup and a u-cap
    for a in range(2, max_s + 1):
        for u in range(2, max_s + 1):
            if a + u <= 8:
                inter = cups_size_has.get(a, set()) & caps_size_has.get(u, set())
                table[(a, u)] = (len(inter) > 0)

    # max union + union==7 from full pairwise (pairs with a+u >= 8)
    max_union = 0
    max_witness = None
    union7 = False
    union7_witness = None
    # also fill table cells with a+u >= 9 from real pairs (union<=7)
    t0 = time.time()
    for rm, cuplst in cups_by_rm.items():
        capst = caps_by_rm.get(rm)
        if not capst:
            continue
        for C in cuplst:
            a = len(C)
            for D in capst:
                u = len(D)
                if a + u < 8:
                    continue
                inter = len(C & D)
                union = a + u - inter
                if union > max_union:
                    max_union = union
                    max_witness = (a, u, rm, inter)
                if union == 7 and not union7:
                    union7 = True
                    union7_witness = (a, u, rm, inter)
                if union <= 7:
                    table[(a, u)] = True
    pairing_time = time.time() - t0

    return {
        "n": n, "N": N, "gp": gp,
        "longest_cup": longest_cup(pts), "longest_cap": longest_cap(pts),
        "paper_max_k": paper_max_k, "paper_witness": paper_witness,
        "paper_split_exists": paper_split_exists,
        "table": table, "max_union": max_union, "max_witness": max_witness,
        "union7": union7, "union7_witness": union7_witness,
        "pairing_time": pairing_time,
    }


def even_odd_halves_7():
    """Even/odd block bipartition halves of es_construct(7)."""
    pts, blocks = es_set_blocks(7)
    even = [p for i in (0, 2, 4) for p in blocks[i]]
    odd = [p for i in (1, 3, 5) for p in blocks[i]]
    res = {}
    for name, half in (("even", even), ("odd", odd)):
        res[name] = {
            "size": len(half),
            "gp": in_general_position(half),
            "has_convex6": has_convex_k_subset(half, 6)[0],
            "largest_convex": largest_convex_subset(half)[0],
        }
    return res, pts


def main():
    print("=== Split-(k-)gon spectrum on VERIFIED lib/es_construct (exact) ===")
    results = {}
    for n in (5, 6, 7):
        r = compute_spectrum(n)
        results[n] = r
        print(f"\n----- n={n}  N={r['N']}  general_position={r['gp']} "
              f"longest_cup={r['longest_cup']} longest_cap={r['longest_cap']} "
              f"(pairing time {r['pairing_time']:.2f}s) -----")
        # paper convention
        pe = r["paper_split_exists"]
        print(f"  [PAPER] max paper-split-k (a+u=k+2): k={r['paper_max_k']} "
              f"(witness a-cap,u-cup,rank={r['paper_witness']})")
        print(f"  [PAPER] paper split-k exists? " +
              ", ".join(f"k={k}:{pe.get(k,'-')}" for k in sorted(pe)))
        # task convention
        print(f"  [TASK ] max union size = {r['max_union']} "
              f"(witness a-cup,u-cap,rank,overlap={r['max_witness']})")
        print(f"  [TASK ] split with union==7 ('split 7-gon (union 7)'): "
              f"{r['union7']} " + (f"(witness={r['union7_witness']})" if r["union7"] else ""))
        # table (union <= 7), rows = a (cup size), cols = u (cap size)
        print("  [TASK ] (a,u) table: 'X' = union<=7 split exists, '.' = none  (a=cup,b=cap)")
        print("           u=    " + "".join(f"{u:4d}" for u in range(2, 8)))
        for a in range(2, 8):
            row = []
            for u in range(2, 8):
                row.append("   X" if r["table"].get((a, u)) else "   .")
            print(f"           a={a}: " + "".join(row))

    # even/odd halves at n=7
    halves, full7 = even_odd_halves_7()
    print(f"\n===== es_construct(7) even/odd block halves (must be 6-avoiding) =====")
    print(f"  full-7 longend cup={longest_cup(full7)} cap={longest_cap(full7)} gp={in_general_position(full7)}")
    for name, h in halves.items():
        print(f"  {name} blocks: size={h['size']} gp={h['gp']} "
              f"has_convex_6={h['has_convex6']} (must be False) "
              f"largest_convex={h['largest_convex']} (must be <=5)")

    print("\nEXIT: 0")


if __name__ == "__main__":
    main()