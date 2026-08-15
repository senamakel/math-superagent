#!/usr/bin/env python3
"""Directive 43: comprehensive exact-integer exhaustive check of the
descent/absorption lemma (Granville Lemma 5.4 combinatorial core) under the
CORRECTED case-split proof.

OBJECT
  c = (c_1..c_L) in {0,2}^L (the 0-2 cycle / maximal {0,2} suffix),
  nu2 = #{s : c_s = 2}, v even in [0, 2L+8].
  Orbit: x_0 = v, x_s = |x_{s-1} - c_s|, s = 1..L.

CLAIMS (each over ALL pairs, exact integers, no floats):
  (a) biconditional BOTH directions:  x_L in {0,2} <=> v <= 2*nu2 + 2
  (b) tight value in the failure regime: v > 2*nu2+2 ==> x_L == v - 2*nu2, x_L >= 4
  (0) structural: every x_s even; {0,2} closed under the step
  (c) the corrected case-split partition (the proof, not the old algebra):
        branch 1 = "some x_t <= 2"  <=> v <= 2*nu2+2   (absorption)
        branch 2 = "all x_s >= 4"   <=> v >  2*nu2+2   (descent)
        in branch 2 every step is exact: c_s=2 -> x_s=x_{s-1}-2, c_s=0 -> x_s=x_{s-1}
  (d) tightness at the budget boundary per pattern:
        v = 2*nu2+2 -> x_L in {0,2} (expect exactly 2)
        v = 2*nu2+4 -> x_L == 4

VERIFICATION, NOT A PROOF: the proof is the case-split argument —
  if some x_t <= 2 then x_t in {0,2} (even, nonneg) and {0,2} is absorbing,
  so x_L in {0,2};  v <= 2*nu2+2 (branch 2's contradiction).
  else every x_s >= 4: each c_s=2 subtracts exactly 2, c_s=0 passes through,
  so x_L = v - 2*nu2; x_L >= 4 means v - 2*nu2 >= 4 i.e. v > 2*nu2+2.
  Contrapositively v > 2*nu2+2 forces the all->=4 branch and the exact value;
  v <= 2*nu2+2 forces some x_t <= 2 (else x_L = v-2*nu2 <= 2 contradicts
  x_L >= 4) and absorption. Nothing discarded; the delta=0 "exception" that
  Granville's published proof drops is branch 1's bounce, the main case here.

COMPLEXITY: time = sum_L 2^L*(L+5)*L = 197,132,292 elementary |a-b| steps,
space O(L) (one trajectory streamed).  The finite domain is the lemma's own
(L=1..18, all 524,286 patterns, all 11,534,328 (pattern,v) pairs) — this IS
the object under test, declared as the verification oracle.
"""
import sys

LMAX = 18


def tight_check(v, cs):
    """Return x_L for the reported budget-boundary values (exact)."""
    x = v
    for c in cs:
        x = abs(x - c)
    return x


def independent_cross_check():
    """Second, structurally different route on a deterministic subsample:
    re-derive each trajectory in HALVED units (d_s = |d_{s-1} - e_s|,
    e = c/2 in {0,1}, d_0 = v/2) and verify x_s == 2*d_s for every s,
    plus claims (a),(b).  Different code path (list-based, halved)."""
    Ls = list(range(1, 7)) + [10, 18]
    cnt = 0
    for L in Ls:
        for pat in range(1 << L):
            es = [1 if (pat >> s) & 1 else 0 for s in range(L)]
            cs = [2 * e for e in es]
            nu1 = sum(es)
            for v in range(0, 2 * L + 9, 2):
                w = v // 2
                d = w
                x = v
                ok = (x == 2 * d)
                for s in range(L):
                    d = abs(d - es[s])
                    x = abs(x - cs[s])
                    ok &= (x == 2 * d)
                c1 = (d in (0, 1)) == (w <= nu1 + 1)
                c2 = (w > nu1 + 1) and (d == w - nu1)
                ok &= c1 and (c2 or w <= nu1 + 1)
                assert ok, (L, pat, v, x, d)
                cnt += 1
    return cnt


def main():
    print("descent/absorption lemma (Granville Lemma 5.4 core) - exhaustive exact-integer check")
    print("CORRECTED case-split proof: branch 1 absorption (min x_s <= 2), branch 2 descent (all x_s >= 4)")
    print("=" * 96)
    print(f"domain: L = 1..{LMAX}, ALL 2^L patterns of {{0,2}}^L per L")
    print(f"        even v in [0, 2L+8] for each L  (L+5 even values per pattern)")
    print(f"        nu2 = # of 2s in the pattern;  x_0 = v, x_s = |x_{{s-1}} - c_s|")
    print()
    print(f"{'L':>3} {'patterns':>9} {'pairs':>11} {'branch1':>9} {'branch2':>9}"
          f" {'vSuff':>6} {'vNec':>6} {'vB':>5} {'vPar':>5} {'vClo':>5}"
          f" {'vB1':>5} {'vB2d':>6} {'vB2v':>6} {'vPart':>6} {'tIn2':>6} {'tOut':>6}")
    print("-" * 96)

    total_patterns = 0
    total_pairs = 0
    total_b1 = 0
    total_b2 = 0
    v_suff = v_nec = v_b = v_par = v_clo = 0
    v_b1 = v_b2d = v_b2v = v_part = 0
    t_in_viol = t_in_zero = t_out_viol = 0
    t_in_exact_2_all = True
    largest_L = 0

    for L in range(1, LMAX + 1):
        largest_L = L
        npat = 1 << L
        vmax = 2 * L + 8
        vs = range(0, vmax + 1, 2)          # all even v in [0, 2L+8]
        Lpairs = L_b1 = L_b2 = 0
        Lsuff = Lnec = Lb = Lpar = Lclo = 0
        Lb1 = Lb2d = Lb2v = Lpart = 0
        Lt_in = Lt_zero = Lt_out = 0
        Lt_in2_ok = True

        for pat in range(npat):
            cs = [2 if (pat >> s) & 1 else 0 for s in range(L)]
            nu2 = bin(pat).count("1")

            # --- tight boundary per pattern (d) -------------------------------
            tv_in = tight_check(2 * nu2 + 2, cs)     # v = 2*nu2+2
            tv_out = tight_check(2 * nu2 + 4, cs)    # v = 2*nu2+4
            if tv_in not in (0, 2):
                Lt_in += 1
            if tv_in != 2:
                Lt_zero += 1          # expect 0: terminal must be exactly 2
                Lt_in2_ok = False
            if tv_out != 4:
                Lt_out += 1

            # --- full sweep over even v --------------------------------------
            for v in vs:
                Lpairs += 1
                x = prev = v
                mn1 = 1 << 60                     # min over x_1..x_L
                le2 = (v <= 2)                    # entered {0,2} regime
                parity = not (v & 1)
                descent_ok = True                 # exact descent while in >=4 regime
                closure_ok = True
                for s, c in enumerate(cs, 1):
                    x = abs(prev - c)
                    if x & 1:
                        parity = False
                    if s == 1 or x < mn1:
                        mn1 = x
                    if le2:
                        if x not in (0, 2):
                            closure_ok = False
                    else:
                        # prev >= 4 (even): step must be exact
                        if x != (prev - 2 if c == 2 else prev):
                            descent_ok = False
                        if x <= 2:
                            le2 = True
                    prev = x
                xL = x

                # (a) both directions
                if v <= 2 * nu2 + 2:
                    if xL not in (0, 2):
                        Lsuff += 1
                else:
                    if xL in (0, 2):
                        Lnec += 1
                    # (b) tight value in failure regime
                    if xL != v - 2 * nu2:
                        Lb += 1
                    if xL < 4:
                        Lb += 1
                # (c) corrected case-split partition
                if mn1 <= 2:
                    L_b1 += 1
                    if xL not in (0, 2):
                        Lb1 += 1                  # absorption branch failed
                    if v > 2 * nu2 + 2:
                        Lpart += 1                # failure regime inside branch 1
                else:
                    L_b2 += 1
                    if not descent_ok:
                        Lb2d += 1
                    if xL != v - 2 * nu2:
                        Lb2v += 1
                    if v <= 2 * nu2 + 2:
                        Lpart += 1                # success regime inside branch 2
                # (0) structural
                if not parity:
                    Lpar += 1
                if not closure_ok:
                    Lclo += 1

        total_patterns += npat
        total_pairs += Lpairs
        total_b1 += L_b1
        total_b2 += L_b2
        v_suff += Lsuff; v_nec += Lnec; v_b += Lb; v_par += Lpar; v_clo += Lclo
        v_b1 += Lb1; v_b2d += Lb2d; v_b2v += Lb2v; v_part += Lpart
        t_in_viol += Lt_in; t_in_zero += Lt_zero; t_out_viol += Lt_out
        t_in_exact_2_all &= Lt_in2_ok

        print(f"{L:>3} {npat:>9} {Lpairs:>11} {L_b1:>9} {L_b2:>9}"
              f" {Lsuff:>6} {Lnec:>6} {Lb:>5} {Lpar:>5} {Lclo:>5}"
              f" {Lb1:>5} {Lb2d:>6} {Lb2v:>6} {Lpart:>6} {Lt_zero:>6} {Lt_out:>6}")

    print("-" * 96)
    print(f"total patterns: {total_patterns}    total (pattern, v) pairs: {total_pairs}")
    print(f"branch 1 (absorption: min x_s <= 2) pairs: {total_b1}   "
          f"branch 2 (descent: all x_s >= 4) pairs: {total_b2}")
    print(f"LARGEST L REACHED: {largest_L}")
    print()

    print("VIOLATION REPORT (each expected 0, exact integers, exhaustive):")
    print(f"  (a)  x_L in {{0,2}} <=> v <= 2*nu2+2")
    print(f"       suff direction (v<=budget but not landed):        {v_suff}")
    print(f"       nec direction (v>budget  but landed):             {v_nec}")
    print(f"  (b)  v > 2*nu2+2 => x_L == v-2*nu2 AND x_L >= 4:       {v_b}")
    print(f"  (0)  every x_s even:                                   {v_par}")
    print(f"       {{0,2}} closed under the step (once in, never out): {v_clo}")
    print(f"  (c)  branch 1: min x_s <= 2 => x_L in {{0,2}}:           {v_b1}")
    print(f"       branch 2: all x_s >= 4 => every step exact (-2 on 2, 0 on 0): {v_b2d}")
    print(f"       branch 2: x_L == v - 2*nu2:                       {v_b2v}")
    print(f"       partition (branch1 <=> v<=budget, branch2 <=> v>budget): {v_part}")
    print(f"  (d)  tight boundary per pattern:")
    print(f"       v = 2*nu2+2 -> x_L in {{0,2}} violations:          {t_in_viol}")
    print(f"       v = 2*nu2+2 -> x_L == 2 exactly (not 0):          {t_in_zero} "
          f"(all patterns give exactly 2: {t_in_exact_2_all})")
    print(f"       v = 2*nu2+4 -> x_L == 4 exactly:                  {t_out_viol}")
    print()
    print("closure table (structural claim): |0-0|=0 |0-2|=2 |2-0|=2 |2-2|=0  all in {0,2}")
    print("case-split proof instantiated per pair:")
    print("  if some x_t <= 2: x_t in {0,2} (even, nonneg), {0,2} absorbing -> x_L in {0,2}")
    print("  else all x_s >= 4: each 2 subtracts exactly 2, each 0 passes through,")
    print("        x_L = v - 2*nu2;  v <= 2*nu2+2 would force x_L <= 2 < 4, contradiction,")
    print("        so this branch is exactly v > 2*nu2+2 and x_L = v - 2*nu2 >= 4.")

    n_cc = independent_cross_check()
    print()
    print(f"independent re-derivation (halved units d_s=|d_{{s-1}}-e_s|, x_s==2*d_s,"
          f" claims (a),(b)) on L in {[1,2,3,4,5,6,10,18]}: {n_cc} (pattern,v) pairs,"
          f" 0 mismatches")

    ok = (v_suff == 0 and v_nec == 0 and v_b == 0 and v_par == 0 and v_clo == 0
          and v_b1 == 0 and v_b2d == 0 and v_b2v == 0 and v_part == 0
          and t_in_viol == 0 and t_in_zero == 0 and t_out_viol == 0)
    print()
    print(f"RESULT: {'ALL CHECKS PASSED' if ok else 'VIOLATIONS FOUND'}"
          f"  (total pairs {total_pairs}, largest L {largest_L})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
