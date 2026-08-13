#!/usr/bin/env python3
"""Exhaustive machine check of the sharpened descent lemma (Granville Lemma 5.4 core).

Combinatorial core:
  pattern c_1..c_L with each c_s in {0,2}; even start value v >= 0.
  x_0 = v;  x_s = |x_{s-1} - c_s| for s = 1..L.   nu2 = #{s : c_s = 2}.

(1) EXACT biconditional:  x_L in {0,2}  <=>  v <= 2*nu2 + 2.
(2) Runway:               v >  2*nu2 + 2  ==>  x_L == v - 2*nu2  (exactly).
(3) Closure:              x_s in {0,2}  ==>  x_t in {0,2} for all t > s.
(4) Sharpness:            all-2s pattern (maximises nu2 = L):
                             v = 2*nu2+2 -> x_L = 2 ;  v = 2*nu2+4 -> x_L = 4.

Exhaustive over ALL patterns in {0,2}^L for L = 1..16 and ALL even v in
[0, 2L+8].  Expected violation counts: 0.

Why the lemma is true (descent argument, the independent route):
  x_s is always even and nonnegative. While x >= 2, a c=2 step maps
  x -> x-2 exactly (|x-2| = x-2 for x >= 2; no bounce), a c=0 step maps
  x -> x.  So the value descends by exactly 2 per 2-step until it reaches
  {0,2}, after which {0,2} is absorbing (both 0 and 2 stay in {0,2} under
  |x-c| for c in {0,2}).  (v-2)/2 2-steps are needed to reach <= 2, hence:
    v <= 2*nu2+2  <=>  enough 2-steps exist  <=>  x_L in {0,2}.       [1]
  If v > 2*nu2+2 then v - 2k >= 4 along the whole trajectory, so every
  2-step descends and x_L = v - 2*nu2 >= 4, never touching {0,2}.     [2]
  Absorption of {0,2} gives [3]; the all-2s pattern gives [4].
  Third confirmation on real data: code/lemma54_iff_check.py found 0
  violations of the iff over 2480 real-prime columns.
"""

def simulate(v, cs):
    """Exact integer trajectory x_0..x_L of the descent; x even, x >= 0 always."""
    x = v
    traj = [x]
    for c in cs:
        x = abs(x - c)
        traj.append(x)
    return traj


def main():
    Lmax = 16
    total_patterns = 0
    total_pairs = 0
    entered_pairs = 0          # pairs whose trajectory ever enters {0,2}
    viol1 = viol2 = viol3 = viol_sanity = 0
    sharp_ok = True
    sharp_examples = []

    print("sharpened descent lemma (Granville Lemma 5.4 combinatorial core) - exhaustive machine check")
    print("=" * 78)
    print(f"domain: L = 1..{Lmax}, ALL {2**Lmax} patterns of {{0,2}}^L per L")
    print("        even v in [0, 2L+8] for each L  (L+5 even values per pattern)")
    print()
    print(f"{'L':>3} {'patterns':>10} {'(pattern,v) pairs':>18} {'viol1':>6} {'viol2':>6} {'viol3':>6} {'sanity':>6}")
    print("-" * 78)

    for L in range(1, Lmax + 1):
        npat = 1 << L
        total_patterns += npat
        vmax = 2 * L + 8
        vs = range(0, vmax + 1, 2)          # all even v in [0, 2L+8]
        Lpairs = 0
        for pat in range(npat):
            cs = [2 if (pat >> s) & 1 else 0 for s in range(L)]
            nu2 = bin(pat).count("1")
            for v in vs:
                Lpairs += 1
                total_pairs += 1
                traj = simulate(v, cs)
                xL = traj[-1]

                # internal sanity: trajectory must stay even and nonnegative
                for x in traj:
                    if x < 0 or (x & 1):
                        viol_sanity += 1

                # claim (1): exact biconditional
                if (xL in (0, 2)) != (v <= 2 * nu2 + 2):
                    viol1 += 1
                # claim (2): runway, never stalls above 2
                if v > 2 * nu2 + 2 and xL != v - 2 * nu2:
                    viol2 += 1
                # claim (3): closure - once {0,2} is entered it is never left
                entered = False
                for x in traj:
                    if x in (0, 2):
                        entered = True
                    elif entered:
                        viol3 += 1
                        break
                if entered:
                    entered_pairs += 1

        # sharpness for this L (all-2s pattern, nu2 = L)
        all2 = [2] * L
        g_lo = simulate(2 * L + 2, all2)[-1]   # v = 2*nu2+2 -> expect 2
        g_hi = simulate(2 * L + 4, all2)[-1]   # v = 2*nu2+4 -> expect 4
        if g_lo != 2 or g_hi != 4:
            sharp_ok = False
        if L == Lmax:
            sharp_examples.append((L, 2 * L + 2, g_lo, 2 * L + 4, g_hi))

        print(f"{L:>3} {npat:>10} {Lpairs:>18} {viol1:>6} {viol2:>6} {viol3:>6} {viol_sanity:>6}")

    print("-" * 78)
    print(f"total patterns: {total_patterns}   total (pattern, v) pairs: {total_pairs}")
    print(f"pairs whose trajectory enters {{0,2}} at some point: {entered_pairs} "
          f"(closure is vacuous on the remaining {total_pairs - entered_pairs})")
    print()
    print(f"(1) x_L in {{0,2}} <=> v <= 2*nu2+2  : violations = {viol1}  (expect 0)")
    print(f"(2) v > 2*nu2+2 => x_L = v - 2*nu2   : violations = {viol2}  (expect 0)")
    print(f"(3) closure {{0,2}} absorbing          : violations = {viol3}  (expect 0)")
    print(f"(0) trajectory even + nonnegative     : violations = {viol_sanity}  (internal sanity)")
    print()
    print("(4) sharpness on the all-2s pattern (maximises nu2 = L):")
    for L, v2, g2, v4, g4 in sharp_examples:
        print(f"    L={L}: v = 2*nu2+2 = {v2} -> x_L = {g2} (expected 2) | "
              f"v = 2*nu2+4 = {v4} -> x_L = {g4} (expected 4)")
    print(f"    sharpness holds for every L = 1..{Lmax}: {sharp_ok}")
    print()
    ok = (viol1 == 0 and viol2 == 0 and viol3 == 0 and viol_sanity == 0 and sharp_ok)
    print(f"RESULT: {'ALL CHECKS PASSED' if ok else 'VIOLATIONS FOUND'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
