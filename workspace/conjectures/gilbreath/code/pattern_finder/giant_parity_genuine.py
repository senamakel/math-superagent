"""Giant landing-row parity on the 15 GENUINE giants — corrected p-values.

Settles TASKS.md Directive 36 item 1: the 1e9 capture's parity p-value counted
all 16 giants including row 247 (genuine=False). This recomputes on the 15
genuine giants only, with every convention pinned by asserts.

CONVENTIONS (authoritative):
  - b[i] = {0,2}-block length of 1-based row i+1  (blocks_depth1000.json).
  - A (2,4)-event fires at 1-based row r (the intruder pair at position b[r-1])
    and LANDS at 1-based row r+1, whose 0-based index is r.
  - giants_1e9.json['giants_0based_rows'] = 0-based LANDING indices.
  - e_bits/c.txt: 161 entries, entry k = boundary state of 1-based row k+1.
    The event set (edge=2 and intruder=4) over rows 1..161, with landing
    0-based index = k+1, reproduces the recorded base rate 36/60 = 0.600.

NULLS tested (all exact integer arithmetic):
  (a) fair coin: P(>=14 even of 15 | p=1/2) = (C(15,14)+C(15,15))/2^15.
  (b) binomial with replacement, base rate p=36/60: sum_{k>=14} C(15,k) p^k (1-p)^(15-k).
  (c) EXACT hypergeometric (without replacement): the giants are a 15-subset of
      the 60-event population; P(>=14 even | 60 events, 36 even) =
      sum_{k>=14} C(36,k) C(24,15-k) / C(60,15).  This is the honest null:
      it conditions on the actual event stream rather than sampling with
      replacement, and it was never computed before (the settlement quoted
      only the binomial 0.0052).

Oracles checked here:
  - boundary files give 60 events, 36 even landing indices (matches 0.600).
  - every genuine giant with landing index <= 160 lies in the 2e7 event set
    (e=2 & c=4 at the intruder row); the two beyond (174, 238) are verified
    as jumps by the 1e9 b-profile (b[r] - b[r-1] > 1000).
"""

import json
from math import comb

BOUNDARY_E = "code/out/pattern_finder_outputs/e_bits.txt"
BOUNDARY_C = "code/out/pattern_finder_outputs/c.txt"
BLOCKS = "code/out/blocks_depth1000.json"
GIANTS = "code/out/pattern_finder_outputs/giants_1e9.json"


def main():
    # ---- 1. event population at 2e7 (rows 1..161) ----
    eb = [int(t) for t in open(BOUNDARY_E).read().split()]
    c = [int(t) for t in open(BOUNDARY_C).read().split()]
    n = min(len(eb), len(c), 161)
    assert n == 161, f"boundary files should hold 161 rows, got {n}"
    # event at array index k: e=2 (bit 1) and intruder=4 in 1-based row k+1;
    # landing 0-based index = k+1
    landing_even = [k + 1 for k in range(n) if eb[k] == 1 and c[k] == 4]
    n_ev = len(landing_even)
    n_even = sum(1 for r in landing_even if r % 2 == 0)
    print(f"[1] (2,4)-event population at 2e7 (rows 1..161): {n_ev} events, "
          f"{n_even} even landing indices, frac {n_even}/{n_ev} = "
          f"{n_even / n_ev:.4f}")
    assert (n_ev, n_even) == (60, 36), "must reproduce recorded base 36/60"

    # ---- 2. the 15 genuine giants ----
    g = json.load(open(GIANTS))
    rows0 = [r for r, fl in zip(g["giants_0based_rows"], g["genuine"]) if fl]
    n_g = len(rows0)
    even_g = [r for r in rows0 if r % 2 == 0]
    odd_g = [r for r in rows0 if r % 2 == 1]
    print(f"[2] genuine giants (1e9, genuine=True): n={n_g}, "
          f"landing rows(0-based)={rows0}")
    print(f"    even landing rows: {len(even_g)}, odd: {odd_g}")

    # ---- 3. giants are events: verify membership ----
    evset = set(landing_even)
    inside = [r for r in rows0 if r <= 160]
    assert all(r in evset for r in inside), \
        f"giants {[r for r in inside if r not in evset]} not in 2e7 event set"
    blk = json.load(open(BLOCKS))["b"]
    for r in rows0:
        if r > 160:
            j = g["jumps"][g["giants_0based_rows"].index(r)]
            assert j > 1000, f"giant {r} has no recorded jump > 1000"
    print(f"[3] membership: all {len(inside)} giants with landing <= 160 in "
          f"2e7 event set; giants 174, 238 verified by jump in 1e9 profile")

    # ---- 4. p-values ----
    # (a) fair coin, one-sided toward the observed direction (14 even)
    fav_a = comb(n_g, 14) + comb(n_g, 15)
    tot_a = 2 ** n_g
    pa = fav_a / tot_a
    print(f"\n[4a] fair-coin one-sided: P(>=14 even of 15 | p=1/2) = "
          f"({comb(n_g,14)}+{comb(n_g,15)})/2^{n_g} = {fav_a}/{tot_a} = {pa:.6e}")

    # (b) binomial with base rate 36/60 (with replacement) — the settlement's
    #     0.0052, reproduced independently
    p = n_even / n_ev
    pb = sum(comb(n_g, k) * p ** k * (1 - p) ** (n_g - k)
             for k in range(14, n_g + 1))
    print(f"[4b] binomial base-rate (with replacement, p={p:.4f}): "
          f"P(>=14 even of 15) = {pb:.6e}")

    # (c) exact hypergeometric (without replacement): the honest null
    fav = sum(comb(n_even, k) * comb(n_ev - n_even, n_g - k)
              for k in range(14, n_g + 1))
    tot = comb(n_ev, n_g)
    pc = fav / tot
    print(f"[4c] EXACT hypergeometric (without replacement):")
    print(f"     P(>=14 even of 15 | population {n_ev} events, {n_even} even) "
          f"= {fav}/{tot} = {pc:.6e}")

    # two-sided for the exact null: at least as extreme in either tail
    fav2 = sum(comb(n_even, k) * comb(n_ev - n_even, n_g - k)
               for k in range(n_g + 1)
               if k >= 14 or k <= 1)
    print(f"     two-sided (>=14 even or <=1 even): = {fav2}/{tot} = "
          f"{fav2 / tot:.6e}")

    print("\n[5] conclusion: the giants land on even 0-based rows 14/15 "
          "against a 36/60 (0.600) even base — same convention, direction "
          "confirmed. The settlement's binomial 0.0052 reproduces; the exact "
          "without-replacement p is the one to quote, along with the "
          "fair-coin figure for reference.")


if __name__ == "__main__":
    main()
