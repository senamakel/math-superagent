#!/usr/bin/env python3
"""Independent cross-check of combine_constraints.py headline numbers.

Second route, different loop structure (per-union subset enumeration rather
than the global subfamily integer), same canonical oracle lib.uc. Re-checks:
  (1) the 74 non-union-closed witnesses on [4] to constraints (A)&(D)&(B)
      with no abundant element, and the (n_ground,m) distribution;
  (2) the canonical witness F={{a},{ab},{c},{d},{bcd}} is one of them;
  (3) pure-count minimum n_ground=3 with m<2^{n_ground-1}, no abundant element;
  (4) vacuity: 0 families in the Karpas regime (B) have (E)-floor >= 0 on n<=4.
Exact integers only. Prints CROSSCHECK PASS/FAIL at the end.
"""
import sys
from itertools import combinations

from lib.uc import decide_union_closed, abundance, abundant_elements


def popcount(x):
    return bin(x).count("1")


def stats(F, n):
    union = 0
    for s in F:
        union |= s
    n_ground = popcount(union)
    k_min = min(popcount(s) for s in F)
    n_max = max(popcount(s) for s in F)
    counts = abundance(F, n)
    has_d1 = any(c == 1 for c in counts)
    return dict(m=len(F), n_ground=n_ground, k_min=k_min, n_max=n_max,
                union=union, counts=counts, has_d1=has_d1,
                abundant=[i for i, c in enumerate(counts) if 2 * c >= len(F)])


def cA(st):
    return st["n_max"] >= 2 * st["k_min"] + 1


def cB(st):
    return st["n_ground"] >= 1 and st["m"] < (1 << (st["n_ground"] - 1))


def cD(st):
    return not st["has_d1"]


def main():
    # (1)+(2): enumerate all nonempty empty-free subfamilies of [4] via
    # combinations of the 16 masks (different structure from the bit-iterator).
    masks4 = list(range(16))
    witnesses = []
    dist = {}
    canon = frozenset({1, 3, 4, 8, 14})
    canon_found = False
    for r in range(1, 17):
        for comb in combinations(masks4, r):
            F = frozenset(comb)
            if 0 in F:
                continue
            st = stats(F, 4)
            if not (cA(st) and cD(st) and cB(st)):
                continue
            if len(st["abundant"]) != 0:
                continue
            if decide_union_closed(F):
                continue
            witnesses.append(F)
            key = (st["n_ground"], st["m"])
            dist[key] = dist.get(key, 0) + 1
            if F == canon:
                canon_found = True
    got = len(witnesses)
    ok1 = got == 74 and dist == {(4, 5): 13, (4, 7): 61}
    ok2 = canon_found
    print(f"(1) witnesses on [4]: {got} (expected 74) "
          f"{'PASS' if ok1 else 'FAIL'}; dist={dict(sorted(dist.items()))}")
    stc = stats(canon, 4)
    print(f"(2) canonical witness {sorted(canon)} in set, not UC, "
          f"counts={stc['counts']}, abundant={stc['abundant']} "
          f"{'PASS' if ok2 else 'FAIL'}")

    # (3) pure-count minimum on n=1..4: n_ground=3, {{a},{b},{c}}.
    ok3 = False
    for n in range(1, 5):
        masks = list(range(1 << n))
        full = (1 << n) - 1
        found = None
        for r in range(1, len(masks) + 1):
            for comb in combinations(masks, r):
                F = frozenset(comb)
                st = stats(F, n)
                if st["union"] != full:
                    continue
                if cB(st) and len(st["abundant"]) == 0:
                    found = F
                    break
            if found is not None:
                break
        if found is not None:
            # Minimum n_ground is the claim, not the specific witness: the
            # first witness found depends on enumeration order. At n=3 both
            # {{a},{b},{c}} (masks 1,2,4) and {0,{a},{b,c}} (masks 0,1,6)
            # qualify (both m=3 < 4, counts (1,1,1), no abundant).
            st = stats(found, n)
            print(f"(3) smallest n_ground = {n}, first witness {sorted(found)} "
                  f"(n_ground={st['n_ground']}, m={st['m']}, "
                  f"counts={st['counts']}, abundant={st['abundant']}) "
                  f"{'PASS' if n == 3 else 'FAIL'}")
            ok3 = (n == 3)
            break
    if not ok3:
        print("(3) FAIL: no n_ground found or wrong minimum")
        ok3 = False

    # (4) vacuity of (E): over ALL nonempty subfamilies n=1..4 (bit-iterator
    # this time), count those in (B) with floor >= 0.
    with_B = 0
    with_B_floor_nonneg = 0
    for n in range(1, 5):
        K = 1 << n
        for sub in range(1, 1 << K):
            F = frozenset(i for i in range(K) if (sub >> i) & 1)
            if not F:
                continue
            st = stats(F, n)
            if not cB(st):
                continue
            with_B += 1
            if st["m"] - (1 << (st["n_ground"] - 1)) >= 0:
                with_B_floor_nonneg += 1
    ok4 = with_B_floor_nonneg == 0
    print(f"(4) families in (B) regime: {with_B}; with (E)-floor >= 0: "
          f"{with_B_floor_nonneg} {'PASS' if ok4 else 'FAIL'}")

    all_ok = ok1 and ok2 and ok3 and ok4
    print(f"\nCROSSCHECK {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())