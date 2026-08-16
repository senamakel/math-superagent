#!/usr/bin/env python3
"""INDEPENDENT verification of the SUPPLY fold nu2(n) by LITERAL definition.

This deliberately does NOT import s_sos / s_direct or any f2/zeta machinery from
lib. It implements the fold from scratch by the literal definition in
problem.md:

    T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o]
    nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 }
    S(n)   = sum_{d=2}^{n-1} (-1)^{T(n,d)} = (n-2) - 2*nu2(n)

The submask set is computed by iterating o in 0..d and testing (o & d) == o.
This is a different code path from the SOS transform (lib.supply_fold.s_sos)
and serves as a ground-truth oracle cross-check.

Items verified (each printed beside its expected value):
  (1) e_{n-2} mechanism: h = e_{n-2} (single 1 at index n-2) gives
      nu2(n) == #{odd d in [2,n-1]} = ceil((n-2)/2) for every n in 3..40.
  (2) n=8 witness: h=e_6 -> nu2=3, S=0, S^2=0; h=e_5 -> nu2=4, S=-2, S^2=4.
  (3) Min-weight threshold: n in {10,14,16}, exhaustive over all 2^n strings,
      grouped by Hamming weight w: report mean nu2/n and
      frac(nu2/n>=0.40), find first w with (mean>=0.40 AND frac>=0.5).
      Expected first w = 3 (n=10), 4 (n=14), 3 (n=16).
  (4) Negative control: all-ones h of length n -> nu2(n)=0 for every n in 6..40.

Exact integer arithmetic throughout (no floats except the reported ratios).
"""

import itertools


# ---------------------------------------------------------------------------
# Literal oracle (no lib imports). h is a tuple/list of 0/1 of length n.
# ---------------------------------------------------------------------------
def fold_literal(h):
    """Return (nu2, S) by the literal definition for length n = len(h)."""
    n = len(h)
    count = 0
    s = 0
    for d in range(2, n):            # d in [2, n-1]
        acc = 0
        # iterate all o in [0,d]; o is a bitwise submask of d iff (o & d)==o
        for o in range(0, d + 1):
            if (o & d) == o:
                acc ^= h[n - 1 - d + o]
        if acc:
            count += 1
            s -= 1
        else:
            s += 1
    return count, s


def e_j(h):
    """h = e_{n-2}: single 1 at index n-2 of a length-n string."""
    n = len(h)
    out = [0] * n
    out[n - 2] = 1
    return out


def odd_count(n):
    """#{odd d in [2,n-1]} = floor((n-2)/2).

    NOTE: the task prompt's stated closed form ceil((n-2)/2) is WRONG for odd n.
    The true count of odd integers strictly less than n (i.e. in [2,n-1]) is
    floor((n-2)/2): e.g. n=5 -> odd d in [2,4] = {3}, count 1 = floor(3/2), but
    ceil(3/2)=2. The literal oracle reproduces the true odd-count exactly, so
    the oracle (not the formula) is the ground truth here.
    """
    return (n - 2) // 2


def main():
    report = []

    def P(line=""):
        report.append(line)

    P("sequence = independent literal fold oracle (no lib f2/SOS code)")
    P("oracle   = T(n,d)=XOR_{o submask of d} h[n-1-d+o]; nu2=#{d in [2,n-1]:T=1}")
    P("range    = n in 3..40 (item 1,4); n in {10,14,16} exhaustive (item 3); n=8 (item 2)")

    # ---------------- ITEM 1: e_{n-2} mechanism ---------------------------
    P("\n================== ITEM 1: e_{n-2} mechanism ==================")
    P("For h = e_{n-2} (single 1 at index n-2), expect nu2(n) = #{odd d in [2,n-1]}.")
    P("True odd count = floor((n-2)/2); the task prompt's stated ceil((n-2)/2) is ")
    P("wrong for odd n (n=5 -> odd d in [2,4] = {3}, count 1, not ceil(3/2)=2);")
    P("the literal oracle reproduces the true odd-count exactly.")
    P(f"{'n':>4} {'nu2':>5} {'odd_count':>10} {'match':>6}")
    item1_ok = True
    for n in range(3, 41):
        h = e_j([0] * n)
        nu2, _ = fold_literal(h)
        exp = odd_count(n)
        ok = (nu2 == exp)
        item1_ok = item1_ok and ok
        P(f"{n:>4} {nu2:>5} {exp:>10} {str(ok):>6}")
    P(f"ITEM 1 {'PASS' if item1_ok else 'FAIL'} (all n in 3..40 agree: {item1_ok})")

    # ---------------- ITEM 2: n=8 witness ---------------------------------
    P("\n================== ITEM 2: n=8 witness ==================")
    P("S(n) = (n-2) - 2*nu2(n); expected h=e_6:(nu2=3,S=0,S^2=0)  h=e_5:(nu2=4,S=-2,S^2=4)")
    for idx, name in ((6, "e_6"), (5, "e_5")):
        h = [0] * 8
        h[idx] = 1
        nu2, S = fold_literal(h)
        exp_nu2, exp_S = (3, 0) if name == "e_6" else (4, -2)
        ok = (nu2 == exp_nu2 and S == exp_S and S * S == exp_S * exp_S)
        P(f"h={name}: nu2={nu2} (exp {exp_nu2})  S={S} (exp {exp_S})  "
          f"S^2={S*S} (exp {exp_S*exp_S})  {'OK' if ok else 'MISMATCH'}")
    # pull explicit e_6/e_5 numbers into variables for the summary
    h6 = [0] * 8
    h6[6] = 1
    h5 = [0] * 8
    h5[5] = 1
    nu2_6, S_6 = fold_literal(h6)
    nu2_5, S_5 = fold_literal(h5)
    item2_ok = (nu2_6 == 3 and S_6 == 0 and nu2_5 == 4 and S_5 == -2)
    P(f"ITEM 2 {'PASS' if item2_ok else 'FAIL'}")

    # ---------------- ITEM 3: min-weight threshold -------------------------
    P("\n================== ITEM 3: min-weight threshold ==================")
    P("For each weight w: mean nu2/n and frac(nu2/n>=0.40) over all 2^n strings.")
    P("First w with (mean>=0.40 AND frac>=0.5). Expected: n=10->3, n=14->4, n=16->3.")
    expected_first = {10: 3, 14: 4, 16: 3}
    item3_ok = True
    for n in (10, 14, 16):
        P(f"\n--- n={n} (2^{n} strings exhaustive) ---")
        # group counts by weight
        n_depths = n - 2
        total_by_w = [0] * (n + 1)
        ge40_by_w = [0] * (n + 1)
        sum_nu2_by_w = [0] * (n + 1)
        for bits in itertools.product((0, 1), repeat=n):
            w = sum(bits)
            nu2, _ = fold_literal(list(bits))
            total_by_w[w] += 1
            sum_nu2_by_w[w] += nu2
            if nu2 >= 0.40 * n:
                ge40_by_w[w] += 1
        P(f"{'w':>3} {'count':>7} {'mean nu2/n':>11} {'frac>=0.40':>10}  typical")
        first_w = None
        for w in range(0, n + 1):
            if total_by_w[w] == 0:
                continue
            mean = sum_nu2_by_w[w] / (total_by_w[w] * n)
            frac = ge40_by_w[w] / total_by_w[w]
            typical = (mean >= 0.40 and frac >= 0.50)
            tag = ""
            if typical and first_w is None:
                first_w = w
                tag = "  <== FIRST TYPICAL"
            P(f"{w:>3} {total_by_w[w]:>7} {mean:>11.4f} {frac:>10.4f}{tag}")
        exp = expected_first[n]
        ok = (first_w == exp)
        item3_ok = item3_ok and ok
        P(f"  first typical w = {first_w}  (expected {exp})  {'OK' if ok else 'MISMATCH'}")
    P(f"ITEM 3 {'PASS' if item3_ok else 'FAIL'}")

    # ---------------- ITEM 4: all-ones negative control --------------------
    P("\n================== ITEM 4: all-ones negative control ==================")
    P("h = all-ones of length n, expect nu2(n)=0 for every n in 6..40.")
    P(f"{'n':>4} {'nu2':>5}")
    item4_ok = True
    for n in range(6, 41):
        nu2, S = fold_literal([1] * n)
        ok = (nu2 == 0)
        item4_ok = item4_ok and ok
        P(f"{n:>4} {nu2:>5}")
    P(f"ITEM 4 {'PASS' if item4_ok else 'FAIL'} (all-ones nu2=0 for all n in 6..40)")

    # ---------------- summary ---------------------------------------------
    P("\n================== SUMMARY ==================")
    P(f"ITEM 1 (e_n-2 odd-count): {'PASS' if item1_ok else 'FAIL'}")
    P(f"ITEM 2 (n=8 witness):     {'PASS' if item2_ok else 'FAIL'}")
    P(f"ITEM 3 (min-weight thr):  {'PASS' if item3_ok else 'FAIL'}")
    P(f"ITEM 4 (all-ones ctrl):   {'PASS' if item4_ok else 'FAIL'}")
    all_ok = item1_ok and item2_ok and item3_ok and item4_ok
    P(f"OVERALL: {'PASS' if all_ok else 'FAIL'}")

    print("\n".join(report))


if __name__ == "__main__":
    main()
