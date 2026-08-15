#!/usr/bin/env python3
"""
Independent exact-integer verification of the sharpened descent lemma
(Granville Lemma 5.4 combinatorial core) in HALVED units.

The clean halved form: pattern e in {0,1}^L, nu1 = #{painful entries e=1},
trajectory  d_0 = w (a natural),  d_k = |d_{k-1} - e_k|  for k = 1..L.

Two claims + one closure, verified EXHAUSTIVELY over every e in {0,1}^L,
L = 1..18, and every w in [0, L+6]:

  (1) w <= nu1 + 1        =>  d_L in {0,1}
  (2) w >  nu1 + 1        =>  d_L = w - nu1      (exact value)
  (3) {0,1} is absorbing : once d_k in {0,1}, d_{k'} in {0,1} for all k' >= k.

Structural fact being checked (why the lemma holds, exact-integer):
while d >= 2, each step is  d' = d (e=0) or d-1 (e=1), so the value equals
w minus the running count of ones WITHOUT ever bouncing; the claims are exactly
the statements that the trajectory either has enough ones to fall into {0,1}
(claim 1, since nu1 >= w-1) or has too few to ever leave the exact-count regime
(claim 2, since w - nu1 >= 2).  Absorbing is |{0,1}-{0,1}| subset {0,1}.

Cost: O(sum_L 2^L * (L+7) * L) time, O(L) space.  All exact integers.

Also reproduced as an INDEPENDENT cross-check: the original even-unit form
(x_k = |x_{k-1} - c_k|, c in {0,2}^L, x_0 = v even) over the exact domain of
code/out/lemma54_descent_check.captured.txt (L=1..16, even v in [0, 2L+8]),
mapping back delta = 2d, c = 2e, v = 2w.  That domain's totals (2,621,432
pairs) and three claims must be reproduced with zero violations.
"""


def halved_traj(w, e):
    """Exact trajectory d_0..d_L for pattern e (tuple of 0/1) and start w."""
    d = w
    out = [d]
    for bit in e:
        d = abs(d - bit)
        out.append(d)
    return out


def even_traj(v, c):
    """Exact even trajectory x_0..x_L for c in {0,2}^L and even v."""
    x = v
    out = [x]
    for bit in c:
        x = abs(x - bit)
        out.append(x)
    return out


def check_halved(LMAX=18, wcap_offset=6):
    """Exhaustive halved check over L=1..LMAX, e in {0,1}^L, w in [0, L+wcap_offset]."""
    viol1 = viol2 = viol3 = 0
    total_pairs = 0
    enter_low = 0
    for L in range(1, LMAX + 1):
        pairs_L = 0
        for mask in range(1 << L):
            e = tuple((mask >> (L - 1 - i)) & 1 for i in range(L))  # MSB-first, no matter
            nu1 = sum(e)
            for w in range(0, L + wcap_offset + 1):
                traj = halved_traj(w, e)
                dL = traj[-1]
                pairs_L += 1
                total_pairs += 1
                # claim (1)
                if w <= nu1 + 1 and dL not in (0, 1):
                    viol1 += 1
                # claim (2)
                if w > nu1 + 1 and dL != w - nu1:
                    viol2 += 1
                # absorbing: from first index in {0,1}, all later stay
                entered = None
                for k in range(L + 1):
                    if traj[k] in (0, 1):
                        entered = k
                        break
                if entered is not None:
                    enter_low += 1
                    for k in range(entered, L + 1):
                        if traj[k] not in (0, 1):
                            viol3 += 1
                            break
        print(f"  {L:3d}  patterns {1<<L:8d}  pairs {pairs_L:10d}  "
              f"viol1 {viol1:5d}  viol2 {viol2:5d}  viol3 {viol3:5d}")
    return total_pairs, viol1, viol2, viol3, enter_low


def sharpness(LMAX=18):
    """All-1s pattern (maximises nu1 = L): tightness at the boundary."""
    ok = True
    line = []
    for L in range(1, LMAX + 1):
        e = (1,) * L
        nu1 = L
        # w = nu1+1 = L+1  ->  d_L in {0,1}; sharpest expectation d_L = 1
        d1 = halved_traj(L + 1, e)[-1]
        # w = nu1+2 = L+2  ->  d_L = w - nu1 = 2 (exact)
        d2 = halved_traj(L + 2, e)[-1]
        good = (d1 == 1) and (d2 == 2)
        ok = ok and good
        line.append(f"L={L}: w={L+1}->d_L={d1} (want 1); w={L+2}->d_L={d2} (want 2)")
    return ok, line


def check_even_reproduce(LMAX=16, vmax_extra=8):
    """
    Independent reproduction of the ORIGINAL even-unit check
    (code/out/lemma54_descent_check.captured.txt): pattern c in {0,2}^L,
    even v in [0, 2L+8] (L+5 even values), three claims:
       (1) x_L in {0,2} <=> v <= 2*nu2+2
       (2) v > 2*nu2+2 => x_L = v - 2*nu2
       (3) {0,2} absorbing
       (0) trajectory even + nonnegative  (sanity)
    """
    viol1 = viol2 = viol3 = viol0 = 0
    total = 0
    perL = []
    for L in range(1, LMAX + 1):
        p_v1 = p_v2 = p_v3 = p_v0 = 0
        pairs = 0
        for mask in range(1 << L):
            c = tuple(2 * (((mask >> (L - 1 - i)) & 1)) for i in range(L))
            nu2 = sum(1 for b in c if b == 2)
            for v in range(0, 2 * L + vmax_extra + 1, 2):   # even v
                traj = even_traj(v, c)
                xL = traj[-1]
                pairs += 1
                # (0) even + nonneg  (all exact, sanity)
                if any(x < 0 or x % 2 for x in traj):
                    p_v0 += 1
                # (1) biconditional
                ok1 = (v <= 2 * nu2 + 2) == (xL in (0, 2))
                if not ok1:
                    p_v1 += 1
                # (2)
                if v > 2 * nu2 + 2 and xL != v - 2 * nu2:
                    p_v2 += 1
                # (3) absorbing
                entered = next((k for k in range(L + 1) if traj[k] in (0, 2)), None)
                if entered is not None and any(x not in (0, 2)
                                               for x in traj[entered + 1:]):
                    p_v3 += 1
        viol0 += p_v0
        viol1 += p_v1
        viol2 += p_v2
        viol3 += p_v3
        total += pairs
        perL.append((L, 1 << L, pairs, p_v1, p_v2, p_v3, p_v0))
        print(f"  {L:3d}  patterns {1<<L:8d}  pairs {pairs:10d}  "
              f"viol1 {p_v1:5d}  viol2 {p_v2:5d}  viol3 {p_v3:5d}  "
              f"viol0 {p_v0:5d}")
    return total, viol0, viol1, viol2, viol3, perL


def main():
    import time
    t0 = time.time()
    print("sharpened descent lemma (Granville Lemma 5.4) in HALVED units - exhaustive check")
    print("domain: L = 1..18, ALL 2^L patterns of {0,1}^L per L")
    print("        w in [0, L+6] for each L  (L+7 values per pattern)")
    print("trajectory: d_0 = w, d_k = |d_{k-1} - e_k|, e in {0,1}, nu1 = #ones")
    print("=" * 78)
    print("  L   patterns      pairs  viol1  viol2  viol3")
    print("-" * 78)
    total, v1, v2, v3, enter_low = check_halved(LMAX=18, wcap_offset=6)
    print("-" * 78)
    print(f"total patterns: {sum(1 << L for L in range(1,19))}")
    print(f"total (pattern, w) pairs: {total}")
    print(f"pairs whose trajectory enters {{0,1}} at some point: {enter_low} "
          f"(closure vacuous on the remaining {total - enter_low})")
    print(f"(1) w <= nu1+1 => d_L in {{0,1}}  : violations = {v1}  (expect 0)")
    print(f"(2) w >  nu1+1 => d_L = w - nu1   : violations = {v2}  (expect 0)")
    print(f"(3) {{0,1}} absorbing              : violations = {v3}  (expect 0)")

    print()
    print("Sharpness on the all-1s pattern (maximises nu1 = L):")
    ok_s, lines = sharpness(LMAX=18)
    for ln in lines:
        print("   " + ln)
    print(f"   sharpness holds for every L = 1..18: {ok_s}")

    print()
    print("=" * 78)
    print("CROSS-CHECK: reproduce ORIGINAL even-unit form (delta = 2d, c = 2e, v = 2w)")
    print("domain: L = 1..16, ALL 65536 patterns of {0,2}^L per L")
    print("        even v in [0, 2L+8] (L+5 even values per pattern)")
    print("  L   patterns  (pattern,v) pairs  viol1  viol2  viol3  viol0 sanity")
    print("-" * 78)
    etotal, ev0, ev1, ev2, ev3, perL = check_even_reproduce(LMAX=16, vmax_extra=8)
    print("-" * 78)
    print(f"total patterns: {sum(1 << L for L in range(1,17))}")
    print(f"total (pattern, v) pairs: {etotal}   (captured file reports 2621432)")
    print()
    print(f"(1) x_L in {{0,2}} <=> v <= 2*nu2+2  : violations = {ev1}  (expect 0)")
    print(f"(2) v > 2*nu2+2 => x_L = v - 2*nu2   : violations = {ev2}  (expect 0)")
    print(f"(3) closure {{0,2}} absorbing          : violations = {ev3}  (expect 0)")
    print(f"(0) trajectory even + nonnegative     : violations = {ev0}  (internal sanity)")
    print()
    print(f"elapsed {time.time()-t0:.2f}s")
    if (v1 == 0 and v2 == 0 and v3 == 0 and ok_s
            and ev1 == 0 and ev2 == 0 and ev3 == 0 and ev0 == 0
            and etotal == 2621432):
        print("RESULT: ALL CHECKS PASSED (halved + even cross-check reproduced)")
    else:
        print("RESULT: FAILURE - see violation counts above")


if __name__ == "__main__":
    main()
