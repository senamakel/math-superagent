#!/usr/bin/env python3
"""combine_constraints.py — combine the held minimal-counterexample constraints
into ONE structural claim about a counterexample, and attack it by hunting the
counterexample on small n.

Held constraints — ESTABLISHED in this run, cited, NOT re-derived (see the
claim store via search_claims):
  (A) kpt-thm5-counterexample-corollary   (proved): counterexample (empty-free,
      no strict-abundant element) => n_max >= 2*k_min + 1.
  (B) karpas-large-families               (proved): counterexample =>
      m = |F| < 2^{n_ground-1}, n_ground = |union F|.
  (C) verified-m-small                    (proved): counterexample =>
      m >= 4*n_ground - 1, n_ground >= 13, in particular m >= 51.
  (D) no-degree-1-element-in-minimal-counterexample (verified-computational
      n<=4): a counterexample has no element of degree exactly 1.
  (E) rarest-count-floor                  (proved for ALL families):
      count_x >= m - 2^{n_ground-1} for every present element x.

KEY OBSERVATION TO VERIFY (the sharpest content): (E) is vacuous exactly on
the counterexample regime. Under (B) any counterexample has
m < 2^{n_ground-1}, so the floor m - 2^{n_ground-1} is NEGATIVE, and the bound
count_x >= (negative number) says nothing. The envelope lower bound does all
its work only where counterexamples cannot live. Confirmed numerically below
over ALL 2^16 subfamilies of [4] and every UC family on n=1..4.

NEGATIVE-CONTROL HUNT (the real attack): over ALL families on [4] (2^16
subfamilies, feasible), find a NON-union-closed family satisfying the
arithmetic counterexample constraints
   (A) n_max >= 2*k_min + 1   (empty-free convention, k_min of the members)
   (D) no degree-1 element    (every present element occurs in >= 2 sets)
   (B) m < 2^{n_ground-1}
yet with NO abundant element (no 2*c >= m). If one exists: the constraints
minus union-closure do NOT force abundance — union-closure is the hypothesis
doing the work, and the claim "these constraints force abundance" is FALSE.

Joint consistency: show (A)&(D) are jointly satisfiable by UNION-CLOSED
families on [4] that are NOT counterexamples (UC holds there — the known
verified floor, consistent with Bosnjak-Markovic n<=11).

Pure-count question: smallest n_ground admitting ANY family (closure-free)
with n_ground present elements, m < 2^{n_ground-1}, and no abundant element.

Guards: UC-family counts on [n], n=1..4, equal A102896 (3,13,121,4959);
empty-free UC counts equal 1,6,60,2479. Exact integer arithmetic only — no
floats anywhere. Oracle: lib.uc.decide_union_closed, lib.uc.abundance,
lib.uc.abundant_elements. Abundance convention: 2*c >= m (>= half).

Capture policy: writes to code/out/combine_constraints.captured.txt via a
temp file moved into place only on exit 0. First three lines state what ran,
which oracle function, and the exact range.
"""

import os
import sys
import tempfile

from lib.uc import decide_union_closed, abundance, abundant_elements

CAPTURE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "combine_constraints.captured.txt")

# A102896: number of union-closed families on [n] (excluding the empty
# collection, including {empty}); equality with these counts is the guard.
A102896 = {1: 3, 2: 13, 3: 121, 4: 4959}
# empty-free (0 not in F) UC counts from claim kpt-thm5-corrob-n4.
EMPTY_FREE_UC = {1: 1, 2: 6, 3: 60, 4: 2479}


def popcount(x):
    return bin(x).count("1")


def elem_name(i):
    return chr(ord("a") + i)


def fam_str(fam, n):
    parts = []
    for msk in sorted(fam):
        es = "".join(elem_name(i) for i in range(n) if (msk >> i) & 1)
        parts.append("{" + es + "}")
    return "F = {" + ", ".join(parts) + "}"


def stats(fam, n):
    """Exact stats of a family (set of bitmask ints) over [n], all integers."""
    lst = sorted(fam)
    union = 0
    for s in lst:
        union |= s
    n_ground = popcount(union)
    sizes = [popcount(s) for s in lst]
    k_min = min(sizes) if sizes else 0
    n_max = max(sizes) if sizes else 0
    counts = abundance(fam, n)
    return {
        "m": len(fam),
        "union": union,
        "n_ground": n_ground,
        "k_min": k_min,
        "n_max": n_max,
        "counts": counts,
        "has_degree1": any(c == 1 for c in counts),
        "abundant": abundant_elements(fam, n),
        "empty_present": 0 in fam,
    }


def cA(st):
    """(A) n_max >= 2*k_min + 1  (empty-free convention)."""
    return st["n_max"] >= 2 * st["k_min"] + 1


def cB(st):
    """(B) m < 2^{n_ground-1} (Karpas counterexample regime); n_ground >= 1."""
    return st["n_ground"] >= 1 and st["m"] < (1 << (st["n_ground"] - 1))


def cD(st):
    """(D) no degree-1 element: every present element occurs in >= 2 sets."""
    return not st["has_degree1"]


def no_abundant(st):
    return len(st["abundant"]) == 0


def e_floor(st):
    """(E) floor value m - 2^{n_ground-1} (exact int); None if n_ground < 1."""
    if st["n_ground"] < 1:
        return None
    return st["m"] - (1 << (st["n_ground"] - 1))


def check_E(st):
    """(E) holds: count_x >= e_floor for every present element (trivial when
    the floor is negative). Union-closure-independent by claim rarest-count-floor."""
    fl = e_floor(st)
    if fl is None:
        return True, 0
    bad = 0
    for i, c in enumerate(st["counts"]):
        if c == 0:
            continue  # element not present; (E) is about present elements
        if c < fl:
            bad += 1
    return bad == 0, bad


def run_part0():
    """Oracle guard on fixed families (mirrors uc_oracle_check)."""
    ok = True
    print("PART 0: oracle guard (fixed families, exact integers)")
    # powerset 2^[3]: UC, every element at density exactly 1/2
    ps = set(range(1 << 3))
    g1 = decide_union_closed(ps) and all(2 * c == len(ps) for c in abundance(ps, 3))
    print(f"  guard powerset 2^[3]: uc={decide_union_closed(ps)}, "
          f"all-densities-1/2={all(2*c == len(ps) for c in abundance(ps, 3))} - "
          f"{'PASS' if g1 else 'FAIL'}")
    ok &= g1
    # {empty, {a}}: UC, {a} abundant (count 1 >= m/2 = 1)
    fs = {0, 1}
    g2 = decide_union_closed(fs) and 0 in abundant_elements(fs, 2)
    print(f"  guard {{empty,{{a}}}} uc={decide_union_closed(fs)}, "
          f"a abundant={0 in abundant_elements(fs, 2)} - {'PASS' if g2 else 'FAIL'}")
    ok &= g2
    # negative control {{a},{b},{c}}: NOT UC, no abundant element
    nc = {1, 2, 4}
    g3 = (not decide_union_closed(nc)) and len(abundant_elements(nc, 3)) == 0
    print(f"  guard antichain {{a}},{{b}},{{c}}: uc={decide_union_closed(nc)}, "
          f"abundant={abundant_elements(nc, 3)} - {'PASS' if g3 else 'FAIL'}")
    ok &= g3
    print(f"  => PART 0 {'PASS' if ok else 'FAIL'}\n")
    return ok


def run_parts(n_max=4):
    """Guards + per-family stats + vacuity + hunt + consistency, n=1..n_max."""
    uc_all = {}          # n -> list of fams (frozenset)
    uc_empty_free = {}   # n -> list of fams without 0
    for n in range(1, n_max + 1):
        uc_all[n] = []
        uc_empty_free[n] = []
        n_sub = 1 << (1 << n)
        for sub in range(n_sub):
            fam = set()
            for i in range(1 << n):
                if (sub >> i) & 1:
                    fam.add(i)
            if fam and decide_union_closed(fam):
                uc_all[n].append(frozenset(fam))
                if 0 not in fam:
                    uc_empty_free[n].append(frozenset(fam))
    # --- guards ---
    ok = True
    print("PART 1: guards and per-UC-family constraint checks (n=1..4)")
    for n in range(1, n_max + 1):
        g = len(uc_all[n]) == A102896[n]
        g2 = len(uc_empty_free[n]) == EMPTY_FREE_UC[n]
        print(f"  n={n}: UC families={len(uc_all[n])} (guard A102896={A102896[n]} "
              f"{'PASS' if g else 'FAIL'}), empty-free UC={len(uc_empty_free[n])} "
              f"(guard {EMPTY_FREE_UC[n]} {'PASS' if g2 else 'FAIL'})")
        ok &= g and g2

    # Statistics over UC families.
    print("\n  UC-family stats (n=1..4):")
    no_cex = True
    for n in range(1, n_max + 1):
        cnt_uc = len(uc_all[n])
        # excluding the trivial {empty} family (no ground elements)
        cex = [f for f in uc_all[n] if f != frozenset({0})
               and len(abundant_elements(f, n)) == 0]
        d1_ok = True   # degree-1 element  =>  abundant element
        d1_cnt = 0
        for f in uc_all[n]:
            st = stats(f, n)
            if st["has_degree1"]:
                d1_cnt += 1
                if no_abundant(st):
                    d1_ok = False
        a_viol = 0
        a_sat = 0
        for f in uc_empty_free[n]:
            st = stats(f, n)
            if cA(st):
                a_sat += 1
            else:
                a_viol += 1
        no_cex &= (len(cex) == 0)
        print(f"    n={n}: UC counterexamples (n_ground>=1, empty abundant list)="
              f"{len(cex)}; families with a degree-1 element={d1_cnt}, of which "
              f"all have an abundant element: {d1_ok} (claim D backwards: "
              f"degree-1 => NOT counterexample); empty-free UC satisfying "
              f"(A) n_max>=2k_min+1: {a_sat}, violating: {a_viol}")
        ok &= (len(cex) == 0) and d1_ok

    # part 2: vacuity of (E) over ALL families on [4] (and UC on n<=4)
    print("\nPART 2: vacuity of the rarest-count-floor (E) on the counterexample regime")
    print("  (E): count_x >= m - 2^{n_ground-1} for every present element x "
          "(proved for ALL families, union-closure-free).")
    print("  Under (B) Karpas forces m < 2^{n_ground-1} on a counterexample, so")
    print("  m - 2^{n_ground-1} < 0 and (E) is vacuous: the envelope lower bound")
    print("  does all its work only where counterexamples cannot live.")
    total_fams = 0
    with_B = 0
    with_B_floor_nonneg = 0
    e_viol_all = 0
    e_viol_uc = 0
    uc_cnt4 = 0
    for n in range(1, n_max + 1):
        n_sub = 1 << (1 << n)
        for sub in range(n_sub):
            fam = set()
            for i in range(1 << n):
                if (sub >> i) & 1:
                    fam.add(i)
            if not fam:
                continue
            total_fams += 1
            st = stats(fam, n)
            fl = e_floor(st)
            if fl is not None:
                holds, bad = check_E(st)
                if not holds:
                    e_viol_all += 1
                if cB(st):
                    with_B += 1
                    if fl >= 0:
                        with_B_floor_nonneg += 1
            if n == 4:
                if decide_union_closed(fam):
                    uc_cnt4 += 1
                    fl = e_floor(st)
                    if fl is not None:
                        holds, _ = check_E(st)
                        if not holds:
                            e_viol_uc += 1
    print(f"  families total over n=1..4: {total_fams}")
    print(f"  families in Karpas regime (B) m < 2^(n_ground-1): {with_B}")
    print(f"  of those with (E) floor >= 0: {with_B_floor_nonneg} "
          f"(must be 0: (B) => floor < 0) - {'PASS' if with_B_floor_nonneg == 0 else 'FAIL'}")
    ok &= (with_B_floor_nonneg == 0)
    print(f"  (E) violated over ALL families: {e_viol_all} "
          f"(must be 0, proved for all families) - {'PASS' if e_viol_all == 0 else 'FAIL'}")
    ok &= (e_viol_all == 0)
    print(f"  (E) violated over UC families on [4] ({uc_cnt4} of them): {e_viol_uc} "
          f"- {'PASS' if e_viol_uc == 0 else 'FAIL'}")
    ok &= (e_viol_uc == 0)

    # part 3: the negative-control hunt over ALL subfamilies of [4]
    print("\nPART 3: THE NEGATIVE-CONTROL HUNT — does union-closure do the work?")
    print("  Hunt: NON-union-closed family on [4], empty-free, satisfying (A) "
          "n_max >= 2k_min+1, (D) no degree-1, (B) m < 2^(n_ground-1), with NO "
          "abundant element (2*c >= m fails for every element).")
    n = n_max
    n_sub = 1 << (1 << n)
    witness_first = None
    witness_cnt = 0
    distrib = {}       # (n_ground, m) -> count
    hunt_total_empty_free = 0
    for sub in range(n_sub):
        fam = set()
        for i in range(1 << n):
            if (sub >> i) & 1:
                fam.add(i)
        if not fam or 0 in fam:
            continue
        hunt_total_empty_free += 1
        st = stats(fam, n)
        if not (cA(st) and cD(st) and cB(st) and no_abundant(st)):
            continue
        if decide_union_closed(fam):
            continue  # the hunt is for NON-union-closed families
        witness_cnt += 1
        key = (st["n_ground"], st["m"])
        distrib[key] = distrib.get(key, 0) + 1
        if witness_first is None:
            witness_first = (sub, fam)
    print(f"  nonempty empty-free subfamilies of [4] scanned: {hunt_total_empty_free}")
    print(f"  WITNESSES FOUND: {witness_cnt} non-union-closed families on [4] "
          f"satisfying (A)&(D)&(B) with no abundant element")
    print(f"  distribution by (n_ground, m): "
          f"{dict(sorted(distrib.items()))}")
    if witness_first is not None:
        sub, fam = witness_first
        st = stats(fam, n)
        print(f"  first witness (enumeration order sub={sub}):")
        print(f"    {fam_str(fam, n)}")
        print(f"    masks={sorted(fam)}, m={st['m']}, n_ground={st['n_ground']}, "
              f"k_min={st['k_min']}, n_max={st['n_max']}, counts={st['counts']}, "
              f"abundant={st['abundant']}")
        print(f"    (A) n_max>=2k_min+1: {cA(st)}, (D) no-degree-1: {cD(st)}, "
              f"(B) m<2^(n_ground-1): {cB(st)}, no-abundant: {no_abundant(st)}, "
              f"union-closed: {decide_union_closed(fam)}")

    # Explicit canonical witness, oracle-verified.
    canon = {1, 3, 4, 8, 14}  # {{a},{ab},{c},{d},{bcd}}
    stc = stats(canon, 4)
    print(f"\n  canonical witness (explicitly verified): {fam_str(canon, 4)}")
    print(f"    masks={sorted(canon)}, m={stc['m']}, n_ground={stc['n_ground']}, "
          f"k_min={stc['k_min']}, n_max={stc['n_max']}, counts={stc['counts']}, "
          f"abundant={stc['abundant']}")
    print(f"    (A) {cA(stc)}, (D) {cD(stc)}, (B) {cB(stc)}, no-abundant "
          f"{no_abundant(stc)}, oracle decide_union_closed={decide_union_closed(canon)}")
    ok &= witness_cnt >= 1
    ok &= (not decide_union_closed(canon)) and cA(stc) and cD(stc) and cB(stc) \
        and no_abundant(stc)
    if witness_cnt >= 1:
        print(f"  VERDICT: a witness exists on [4] — the held arithmetic "
              f"constraints (A),(B),(D) MINUS union-closure do NOT force "
              f"abundance. Union-closure is the hypothesis doing the work; the "
              f"claim 'these constraints force abundance' is FALSE.")
    else:
        print(f"  VERDICT: no witness on [4] — proceed to pure-count question.")

    # part 3b: pure-count minimum n_ground (closure-free).
    print("\nPART 3b: pure-count question — smallest n_ground with a family of")
    print("  size m < 2^(n_ground-1) and no abundant element (no closure, no "
          "(A)/(D) constraints).")
    min_n = None
    min_wit = None
    for nn in range(1, n_max + 1):
        n_sub = 1 << (1 << nn)
        found = None
        full = (1 << nn) - 1
        for sub in range(n_sub):
            fam = set()
            for i in range(1 << nn):
                if (sub >> i) & 1:
                    fam.add(i)
            if not fam:
                continue
            st = stats(fam, nn)
            if st["union"] != full:
                continue  # n_ground must equal nn (every element present)
            if cB(st) and no_abundant(st):
                found = (sub, fam)
                break
        if found is not None:
            min_n = nn
            min_wit = found
            break
    if min_n is not None:
        _, fam = min_wit
        st = stats(fam, min_n)
        print(f"  smallest n_ground = {min_n}, witness "
              f"{fam_str(fam, min_n)}: masks={sorted(fam)}, m={st['m']} < "
              f"2^{min_n-1}={1 << (min_n - 1)}, counts={st['counts']}, "
              f"no-abundant={no_abundant(st)}")
        ok &= (min_n == 3)  # = 3 settles the pure-count minimum; verified below
    else:
        print(f"  no such family found on n=1..{n_max}")

    # part 4: joint consistency of (A)&(D) inside UNION-CLOSED non-counterexamples
    print("\nPART 4: joint consistency — union-closed families on [4] satisfying")
    print("  (A) n_max>=2k_min+1 AND (D) no-degree-1, that are NOT counterexamples.")
    n = n_max
    ok_fams = [f for f in uc_empty_free[n] if cA(stats(f, n)) and cD(stats(f, n))]
    print(f"  such empty-free UC families on [4]: {len(ok_fams)} "
          f"(of {len(uc_empty_free[n])} empty-free UC families)")
    if ok_fams:
        f0 = ok_fams[0]
        st = stats(f0, n)
        print(f"  example: {fam_str(f0, n)}")
        print(f"    masks={sorted(f0)}, m={st['m']}, n_ground={st['n_ground']}, "
              f"k_min={st['k_min']}, n_max={st['n_max']}, counts={st['counts']}, "
              f"abundant={st['abundant']}")
        print(f"    (A) {cA(st)}, (D) {cD(st)}, union-closed="
              f"{decide_union_closed(f0)}, abundant nonempty -> NOT a "
              f"counterexample (UC holds at n<=4, consistent with "
              f"Bosnjak-Markovic n<=11).")
    ok &= len(ok_fams) >= 1
    print("  (C) Roberts-Simpson m >= 4*n_ground - 1 is vacuous here: it needs "
          "n_ground >= 13, unreachable on [4] (recorded, not a failure).")

    # part 5: the combined claim.
    print("\nPART 5: THE COMBINED STRUCTURAL CLAIM (status recap)")
    print("  A counterexample F (empty-free convention) must satisfy, with")
    print("  k=k_min, N=n_max, n=n_ground, m=|F|:")
    print("    (A) N >= 2k + 1           [KPT corollary, claimed proved]")
    print("    (B) m < 2^{n-1}           [Karpas, claimed proved]")
    print("    (C) m >= 4n - 1, n >= 13  [Roberts-Simpson/Hu, claimed proved]")
    print("    (D) every element in >= 2 sets [verified-computational n<=4]")
    print("    (E) count_x >= m - 2^{n-1} for all x  [proved for ALL families,")
    print("         but VACUOUS under (B): m - 2^{n-1} < 0 — the envelope does")
    print("         all its work where counterexamples cannot live]")
    print("  NEGATIVE CONTROL: (A)&(B)&(D) minus union-closure do NOT force")
    print("  abundance (witness on [4]); union-closure is indispensable.")
    print("  On n<=4 no UC family is a counterexample: UC holds there (known")
    print("  verified floor, consistent with Bosnjak-Markovic n<=11).")
    print("  LARGER RUN: the non-UC hunt at n_ground=5 = 2^32 subfamilies = the")
    print("  enumeration ceiling; the [4] verdict (a witness EXISTS) already")
    print("  settles the claim, so pushing to n=5 only adds witness statistics.")
    print("  The genuinely new next step is the UC-side extrapolation of (D) to")
    print("  n=5 (2,771,103 UC families, reachable by the existing cascade),")
    print("  extending the no-degree-1 verified floor beyond n=4.")
    return ok


def main():
    # capture header: what ran, which oracle fn, exact range (required form)
    print("combine_constraints.py — combine the held minimal-counterexample"
          " constraints into ONE structural claim and attack it by hunting the"
          " counterexample on small n (GOAL.md phase 4).")
    print("Oracle: lib.uc.decide_union_closed / lib.uc.abundance /"
          " lib.uc.abundant_elements; exact integer counts, no floats.")
    print("Range: n=1..4 exhaustive — ALL 2^(2^n) subfamilies of [n] per n"
          " (65,536 at n=4); UC guard A102896 = 3,13,121,4959.")
    print()
    ok = run_part0()
    ok &= run_parts(4)
    print()
    if ok:
        print("ALL PARTS PASS (exact integer arithmetic; oracle lib.uc)")
        return 0
    print("SOME PARTS FAILED")
    return 1


def _run_and_capture():
    tmp_fd, tmp_path = tempfile.mkstemp(
        prefix="combine_constraints.", suffix=".captured.txt.tmp",
        dir=os.path.dirname(CAPTURE_PATH))
    os.close(tmp_fd)
    ok = True
    try:
        with open(tmp_path, "w") as fh:
            sys.stdout = fh
            rc = main()
            sys.stdout.flush()
            sys.stdout = sys.__stdout__
        with open(tmp_path) as fh:
            content = fh.read()
        if rc == 0 and content.strip():
            os.replace(tmp_path, CAPTURE_PATH)
            print(f"captured -> {CAPTURE_PATH}")
        else:
            ok = False
            print("capture NOT completed (non-zero exit or empty output); "
                  f"temp left at {tmp_path}")
    except Exception:
        import traceback
        traceback.print_exc()
        ok = False
    finally:
        if not ok and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(_run_and_capture())