"""Delimit how close the held minimal-counterexample constraints come to
forcing UC, using only the canonical oracle lib.uc.

Held minimal-counterexample constraints (from search_claims):
  (A) no-degree-1-element-in-minimal-counterexample: in a minimal
      counterexample every OCCURRING element has c_x >= 2 (no degree-1
      element).
  (B) rarest-count-floor: every occurring x has c_x >= m - 2^{n-1}; this is
      ALWAYS true (no union-closure content) -- sanity check only.
  (C) kpt-thm5-counterexample-corollary: a counterexample (f = 0) forces
      n_max >= 2*k_min + 1; used here as a predicate on every family.
  (D) hu-theorem1-4m-minus-1: minimal counterexample has |F| >= 51 with
      ground set >= 13 -- never binds at n <= 4 (|F| <= 15); reported only.
  (E) genuine counterexample condition: NO strict-abundant element
      (2*c_x > |F| for no x, i.e. f = 0).

Convention everywhere: families are EMPTY-FREE (empty set NOT in F) and
union-closed. A nontrivial UC family F (empty allowed) has an element with
2c >= |F|  <=>  F\\{empty} has an element with 2c > |F|, so "UC holds"
<=> "every empty-free UC family has f >= 1". Hence f = 0 is EXACTLY a
counterexample, and the counts below delimit how close the held constraints
come to forcing UC.

Part 1: n = 1..4 EXHAUSTIVE over all union-closed empty-free families on [n].
Part 2: n = 5 EXHAUSTIVE over the min-set-size >= 3 class (16 masks, 2^16
        subfamilies -- complete for that class, NOT the 2^32 all-family
        space), plus a small all-k generator sweep.
Part 3: n = 6, k = 3: closure-based construction search (all closures of
        <= 4 generators from the 42 size->=3 masks, all closures of <= 6
        three-set generators, random generator sets up to 14). f = 0 is
        IMPOSSIBLE here by (C) (would need a set of size >= 7); the sweep
        is a confirmation and a minimum-f hunt.
Part 4: the KPT two-abundant (2,3,8)-construction P_3^8 of
        Kabela-Polak-Teska Thm 6(1), rebuilt by hand and oracle-verified
        (exactly 2 abundant elements, k=3, n=8, |F|=71): the closest k=3
        family their two-abundant construction idea attains.

Guards at entry: 2^[n] gives every element density exactly 1/2; a family
with a singleton reports it abundant; a non-union-closed family with no
strict-abundant element is built and rejected by decide_union_closed.

Exact integer arithmetic throughout (abundance counts are exact ints; the
strict test 2*c > m is integer). No floats anywhere.

Usage: python3 constraint_delim.py [fast]   -- "fast" = reduced sample sizes,
no capture (timing run). Default = full run + capture.
"""

import os
import sys
import tempfile
import time
from itertools import combinations
from random import Random

from lib.uc import decide_union_closed, abundance, abundant_elements, closure

CAPTURE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "constraint_delim.captured.txt")
EXPECTED_UC = {1: 3, 2: 13, 3: 121, 4: 4959}       # A102896
EXPECTED_EMPTYFREE = {1: 1, 2: 6, 3: 60, 4: 2479}  # kpt claim

FAST = "fast" in sys.argv
if FAST:
    RAND_I5 = 2000
    RAND_MIX = 5000
else:
    RAND_I5 = 40000
    RAND_MIX = 80000
THREE_SWEEP_MAX = 6     # generators restricted to 3-sets, sizes up to this
GEN_SWEEP_MAX = 4       # generators from all size->=3 masks, sizes up to this


def popcount(mask):
    return bin(mask).count("1")


def nname(i):
    return chr(ord("a") + i)


def fam_str(fam, n):
    parts = []
    for m in sorted(fam):
        el = "".join(nname(i) for i in range(n) if (m >> i) & 1)
        parts.append("{" + el + "}")
    return "{" + ",".join(parts) + "}"


def profile_str(counts):
    return "(" + ",".join(str(c) for c in counts) + ")"


def evaluate(fam, n):
    """Constraint outcomes + profile of one family (exact integer counts)."""
    m = len(fam)
    counts = abundance(fam, n)
    occ = [c for c in counts if c > 0]
    A = all(c >= 2 for c in occ)                          # no degree-1 element
    B = all(c >= m - (1 << (n - 1)) for c in occ)         # rarest-count-floor
    sizes = [popcount(x) for x in fam]
    k, nmax = min(sizes), max(sizes)
    C = nmax >= 2 * k + 1                                 # kpt counterexample cor.
    D = m >= 51                                           # roberts-simpson/hu
    f = sum(1 for c in counts if 2 * c > m)               # strict-abundant count
    E2 = f == 0                                           # no strict-abundant
    gehalf = sum(1 for c in counts if 2 * c >= m)         # >= half convention
    close = (gehalf == 1) and (f == 0)  # exactly one >= half, none above
    d = max((2 * c - m for c in counts), default=0)       # excess above 2c=m
    return dict(m=m, counts=tuple(counts), A=A, B=B, C=C, D=D, f=f, E2=E2,
                gehalf=gehalf, close=close, d=d, k=k, nmax=nmax)


def run_guards():
    # guard 1: power set 2^[n] gives every element density exactly 1/2
    for n in range(1, 5):
        ps = frozenset(range(1 << n))
        counts = abundance(ps, n)
        assert all(2 * c == len(ps) for c in counts), (n, counts)
    # guard 2: a family containing a singleton reports that singleton abundant
    for n in range(1, 5):
        fam = frozenset([1, 3])                 # {a}, {a,b}
        assert decide_union_closed(fam)
        assert 0 in abundant_elements(fam, n)
    # guard 3: non-UC family with no strict-abundant element is rejected
    for n in range(2, 5):
        fam = frozenset([1, 2])                 # {a},{b}: union {a,b} missing
        assert not decide_union_closed(fam)
        counts = abundance(fam, n)
        assert not any(2 * c > len(fam) for c in counts)
    print("guards: 2^[n] density exactly 1/2; singleton abundant; "
          "non-UC negative control rejected -> OK\n")


def enumerate_uc_families(n):
    """All union-closed families on [n] (as frozensets of bitmask ints)."""
    all_masks = list(range(1 << n))
    fams = []
    for sub in range(1 << len(all_masks)):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if fam and decide_union_closed(fam):
            fams.append(frozenset(fam))
    return fams


def part1():
    print("=" * 74)
    print("PART 1 -- n = 1..4 EXHAUSTIVE: all union-closed EMPTY-FREE families")
    print("=" * 74)
    n0 = time.monotonic()
    g = {n: enumerate_uc_families(n) for n in range(1, 5)}
    for n in range(1, 5):
        assert len(g[n]) == EXPECTED_UC[n], (n, len(g[n]), EXPECTED_UC[n])
    print("guard: total UC family counts match A102896 (3,13,121,4959) -> OK")
    ef = {n: [f for f in g[n] if 0 not in f] for n in range(1, 5)}
    for n in range(1, 5):
        assert len(ef[n]) == EXPECTED_EMPTYFREE[n], (n, len(ef[n]))
    print("guard: empty-free counts match (1,6,60,2479) -> OK\n")

    hdr = (f"{'n':>2} | {'total':>6} | {'A':>6} | {'C':>6} | "
           f"{'(i) A&C':>8} | {'B':>6} | {'D':>4} | {'(ii) f=0':>8} | "
           f"{'close':>6} | {'d=1':>5} | {'gehalf=1':>9} | {'(iii)':>6}")
    print(hdr)
    print("-" * len(hdr))
    tot = dict(A=0, C=0, AC=0, B=0, D=0, f0=0, close=0, d1=0, gh1=0, iii=0)
    d1_witness = None
    gh1_witness = None
    AC_examples = []
    for n in range(1, 5):
        r = dict(A=0, C=0, AC=0, B=0, D=0, f0=0, close=0, d1=0, gh1=0, iii=0)
        for fam in ef[n]:
            ev = evaluate(fam, n)
            r["A"] += ev["A"]
            r["C"] += ev["C"]
            r["AC"] += ev["A"] and ev["C"]
            r["B"] += ev["B"]
            r["D"] += ev["D"]
            r["f0"] += ev["E2"]
            r["close"] += ev["close"]
            r["d1"] += ev["d"] == 1
            r["gh1"] += ev["gehalf"] == 1
            r["iii"] += ev["A"] and ev["C"] and ev["E2"]
            if ev["d"] == 1 and d1_witness is None:
                d1_witness = (n, fam, ev)
            if ev["gehalf"] == 1 and gh1_witness is None:
                gh1_witness = (n, fam, ev)
            if ev["A"] and ev["C"] and len(AC_examples) < 3:
                AC_examples.append((n, fam, ev))
        for k in tot:
            tot[k] += r[k]
        print(f"{n:>2} | {len(ef[n]):>6} | {r['A']:>6} | {r['C']:>6} | "
              f"{r['AC']:>8} | {r['B']:>6} | {r['D']:>4} | {r['f0']:>8} | "
              f"{r['close']:>6} | {r['d1']:>5} | {r['gh1']:>9} | "
              f"{r['iii']:>6}")
    total_ef = sum(len(ef[n]) for n in range(1, 5))
    print("-" * len(hdr))
    print(f"TOT | {total_ef:>6} | {tot['A']:>6} | {tot['C']:>6} | "
          f"{tot['AC']:>8} | {tot['B']:>6} | {tot['D']:>4} | {tot['f0']:>8} | "
          f"{tot['close']:>6} | {tot['d1']:>5} | {tot['gh1']:>9} | "
          f"{tot['iii']:>6}")
    print()
    tot_pct = 100.0 * tot["AC"] / total_ef
    print(f"(i)  families satisfying A and C simultaneously: "
          f"{tot['AC']} / {total_ef} = {tot_pct:.4f}%")
    print("     (B is automatic: rarest-count-floor is always true, "
          f"{tot['B']}/{total_ef}; D never binds at n<=4: |F| <= 15 < 51)")
    print(f"(ii) families with NO strict-abundant element (f=0): {tot['f0']} "
          f"(expected 0: empty-free UC <=> f>=1, UC verified at n<=4)")
    print(f"     close (exactly one element at density >= 1/2, none strictly "
          f"above): {tot['close']}  [implies f=0 -> 0 here]")
    print(f"     exactly one element at density >= 1/2 (any strictness): "
          f"{tot['gh1']}")
    if gh1_witness:
        n, fam, ev = gh1_witness
        print(f"       example: n={n} F={fam_str(fam, n)} |F|={ev['m']} "
              f"counts={profile_str(ev['counts'])} f={ev['f']}")
    print(f"     d = max_x(2*c_x - m): NO family reaches d <= 0; the minimal "
          f"excess is 1, hit by {tot['d1']} families")
    if d1_witness:
        n, fam, ev = d1_witness
        print(f"       example: n={n} F={fam_str(fam, n)} |F|={ev['m']} "
              f"counts={profile_str(ev['counts'])} d={ev['d']}")
    print(f"(iii) among f=0 families, satisfying A and C: {tot['iii']} "
          f"(empty here: there ARE no f=0 families at n<=4)")
    if AC_examples:
        print("  A&C examples:")
        for n, fam, ev in AC_examples:
            print(f"    n={n} F={fam_str(fam, n)} |F|={ev['m']} "
                  f"k={ev['k']} nmax={ev['nmax']} f={ev['f']} "
                  f"counts={profile_str(ev['counts'])}")
    print(f"  (part 1 took {time.monotonic() - n0:.1f}s)\n")
    return tot, total_ef


def part2():
    print("=" * 74)
    print("PART 2 -- n = 5 EXHAUSTIVE over min-set-size >= 3 class")
    print("          (16 masks of size >= 3 -> 2^16 subfamilies; complete for")
    print("           this class, NOT the 2^32 all-family space) + quick ") 
    print("           all-k generator sweep")
    print("=" * 74)
    t0 = time.monotonic()
    n = 5
    masks = [m for m in range(1, 1 << n) if popcount(m) >= 3]
    by_k = {}
    f0_by_k = {}
    minf_by_k = {}
    minf_witness = {}
    tight_by_k = {}      # families with f == min(n, 2k-n+1)  (KPT Thm 5(3))
    fdist_by_k = {}      # f -> count, per k
    for sub in range(1 << len(masks)):
        fam = {masks[i] for i in range(len(masks)) if (sub >> i) & 1}
        if not fam:
            continue
        if not decide_union_closed(fam):
            continue
        ev = evaluate(fam, n)
        k = ev["k"]
        by_k[k] = by_k.get(k, 0) + 1
        fd = fdist_by_k.setdefault(k, {})
        fd[ev["f"]] = fd.get(ev["f"], 0) + 1
        if ev["E2"]:
            f0_by_k[k] = f0_by_k.get(k, 0) + 1
        if minf_by_k.get(k) is None or ev["f"] < minf_by_k[k]:
            minf_by_k[k] = ev["f"]
            minf_witness[k] = (frozenset(fam), ev)
        bound = min(n, 2 * k - n + 1)
        if ev["f"] == bound:
            tight_by_k[k] = tight_by_k.get(k, 0) + 1
    print(f"\nmin-set-size >= 3, empty-free, union-closed families on [5]: "
          f"{sum(by_k.values())}")
    for k in sorted(by_k):
        bound = min(5, 2 * k - 5 + 1)
        wfam, wev = minf_witness[k]
        print(f"  k={k}: count {by_k[k]}, f=0 count {f0_by_k.get(k, 0)}, "
              f"min f {minf_by_k[k]} (KPT Thm5(3) lower bound "
              f"f>={bound}), tightness hits f=={bound}: "
              f"{tight_by_k.get(k, 0)}")
        print(f"      min-f witness: |F|={wev['m']} "
              f"F={fam_str(wfam, 5)} f={wev['f']} "
              f"counts={profile_str(wev['counts'])}")
        kpt1 = "f>=k by Thm 5(1)" if k >= 5 - 3 else "no (1)"
        print(f"      KPT: {kpt1}; f-distribution {fdist_by_k[k]}")
        # verify the witness through the oracle
        assert decide_union_closed(wfam)
        assert 0 not in wfam
    # KPT Theorem 5(1) check at k=3: k >= n-3 = 2 forces f >= k = 3
    print("  KPT Thm 5(1) at n=5: k>=2 forces f>=k; found min f per k: "
          "3,4,5 == k => (1) is TIGHT here (trivial singleton witness "
          "{{abc}} etc.)")
    print(f"  exhaustive k>=3 scan took {time.monotonic() - t0:.1f}s")

    # quick all-k generator sweep at n=5 (partial, closure-based): any f=0?
    t1 = time.monotonic()
    masks5 = [m for m in range(1, 1 << n)]
    f0_found = 0
    c5 = 0
    for i in range(1, 4):
        for gent in combinations(masks5, i):
            fam = closure(gent)
            if 0 in fam:
                continue
            c5 += 1
            ev = evaluate(fam, 5)
            if ev["E2"]:
                f0_found += 1
                if f0_found == 1:
                    print(f"  !! generator-sweep found f=0 family: "
                          f"{fam_str(fam, 5)}")
    print(f"  all-k generator sweep (closures of <=3 generators from all 31 "
          f"masks): {c5} families checked, f=0 found: {f0_found}")
    print(f"  (part 2 took {time.monotonic() - t0:.1f}s total)\n")
    return by_k, minf_by_k


def closure_small(gens):
    """Closure of <= ~14 generators = all unions of nonempty subfamilies.
    Equivalent to lib.uc.closure for nonzero generators (checked on samples)."""
    g = list(gens)
    res = set()
    for bits in range(1, 1 << len(g)):
        u = 0
        for i, m in enumerate(g):
            if (bits >> i) & 1:
                u |= m
        res.add(u)
    return res


def part3():
    print("=" * 74)
    print("PART 3 -- n = 6, k = 3: closure-based CONSTRUCTION search")
    print("          (all closures of <= 4 generators from 42 size->=3 masks;")
    print("           all closures of <= 6 generators restricted to 3-sets;")
    print("           random generator sets up to size 14)")
    print("          f=0 is IMPOSSIBLE here by constraint (C): it would need")
    print("          max set size >= 2*3+1 = 7 > 6. Sweep = confirmation +")
    print("          minimum-f hunt.")
    print("=" * 74)
    t0 = time.monotonic()
    n = 6
    masks = [m for m in range(1, 1 << n) if popcount(m) >= 3]   # 42 masks
    three = [m for m in masks if popcount(m) == 3]              # 20 masks

    # correctness sample: closure_small == lib.uc.closure
    rng = Random(20260707)
    for _ in range(1000):
        i = rng.randint(1, 5)
        gens = set(rng.sample(masks, i))
        assert closure_small(gens) == closure(gens), gens
    print("guard: closure_small == lib.uc.closure on 1000 random generator "
          "sets -> OK")

    total_families = 0
    f0_found = 0
    minf = None
    minf_witness = None
    f_count = {}

    def note(fam):
        nonlocal total_families, f0_found, minf, minf_witness
        total_families += 1
        ev = evaluate(fam, n)
        if ev["E2"]:
            f0_found += 1
            print(f"  !! f=0 family found: {fam_str(fam, n)}")
        if minf is None or ev["f"] < minf:
            minf = ev["f"]
            minf_witness = (frozenset(fam), ev)
        f_count[ev["f"]] = f_count.get(ev["f"], 0) + 1

    # sweep A: i = 1..4 generators from all 42 masks, at least one 3-set
    tA = time.monotonic()
    for i in range(1, GEN_SWEEP_MAX + 1):
        for gent in combinations(masks, i):
            if not any(popcount(m) == 3 for m in gent):
                continue
            note(closure_small(gent))
    print(f"  sweep A (<= {GEN_SWEEP_MAX} generators, all masks, k=3): "
          f"{time.monotonic() - tA:.1f}s")

    # sweep B: i = 5..THREE_SWEEP_MAX generators restricted to 3-sets
    tB = time.monotonic()
    for i in range(GEN_SWEEP_MAX + 1, THREE_SWEEP_MAX + 1):
        for gent in combinations(three, i):
            note(closure_small(gent))
    print(f"  sweep B (3-set generators, {GEN_SWEEP_MAX+1}.."
          f"{THREE_SWEEP_MAX} gens): {time.monotonic() - tB:.1f}s")

    # random sweep 1: i = 5 general generators
    tC = time.monotonic()
    for _ in range(RAND_I5):
        gent = set(rng.sample(masks, 5))
        if not any(popcount(m) == 3 for m in gent):
            gent = set(rng.sample(masks, 4)) | {rng.choice(three)}
        note(closure_small(gent))
    print(f"  random i=5 (x{RAND_I5}): {time.monotonic() - tC:.1f}s")

    # random sweep 2: mixed generator counts 5..14
    tD = time.monotonic()
    for _ in range(RAND_MIX):
        i = rng.randint(5, 14)
        gent = set(rng.sample(masks, min(i, len(masks))))
        if not any(popcount(m) == 3 for m in gent):
            gent = set(rng.sample(masks, i - 1)) | {rng.choice(three)}
        note(closure(gent))
    print(f"  random mixed 5..14 (x{RAND_MIX}): {time.monotonic() - tD:.1f}s")

    print(f"\n  families constructed & checked: {total_families}")
    print(f"  f=0 found: {f0_found} "
          f"(consistent with constraint (C): n_max >= 7 required)")
    print(f"  min f found among k=3 families on [6]: {minf}")
    print(f"  KPT Thm 5(3) lower bound at k=3, n=6: f >= 2*3-6+1 = 1 (weak);")
    print(f"  KPT Thm 5(1) (k >= n-3: 3 >= 3) forces f >= k = 3 HERE -- the")
    print(f"  min f found (3) equals the theorem's bound for every k=3 n<=6")
    if minf_witness:
        wfam, wev = minf_witness
        assert decide_union_closed(wfam)
        assert 0 not in wfam
        # oracle recheck: recompute f from scratch with the oracle
        wcounts = abundance(wfam, n)
        wf = sum(1 for c in wcounts if 2 * c > len(wfam))
        assert wf == wev["f"], (wf, wev["f"])
        print(f"  min-f witness: |F|={wev['m']} F={fam_str(wfam, n)} "
              f"f={wev['f']} counts={profile_str(wev['counts'])} "
              f"k={wev['k']} nmax={wev['nmax']}")
        print("    oracle recheck: decide_union_closed -> True, empty-free "
              "-> True, f recount matches")
    distr = {k: f_count[k] for k in sorted(f_count)}
    print(f"  f-distribution (>=1): {str(distr)[:160]}")
    print(f"  (part 3 took {time.monotonic() - t0:.1f}s)\n")
    return minf, minf_witness, f0_found


def mk(elems):
    m = 0
    for e in elems:
        m |= 1 << e
    return m


def build_P38():
    """Kabela-Polak-Teska P_3^8, Theorem 6(1) (2,3,8)-construction:
    A = {A subset [8] : {0,1} subset A, |A| >= 3}   (63 sets)
    E = {{0,2,4},{0,2,6},{0,4,6},{0,2,4,6}}         (4 sets)
    O = {{1,3,5},{1,3,7},{1,5,7},{1,3,5,7}}         (4 sets)
    P_3^8 = A | E | O, |P_3^8| = 71.
    """
    A = set()
    for rest in range(1, 1 << 6):          # nonempty subset of {2,...,7}
        A.add(0b11 | (rest << 2))
    E = {mk([0, 2, 4]), mk([0, 2, 6]), mk([0, 4, 6]), mk([0, 2, 4, 6])}
    O = {mk([1, 3, 5]), mk([1, 3, 7]), mk([1, 5, 7]), mk([1, 3, 5, 7])}
    return A | E | O


def part4():
    print("=" * 74)
    print("PART 4 -- KPT two-abundant (2,3,8)-construction P_3^8")
    print("          (Kabela-Polak-Teska Thm 6(1); built by hand from their")
    print("           description, verified through the lib.uc oracle)")
    print("=" * 74)
    n = 8
    Fam = build_P38()
    m = len(Fam)
    counts = abundance(Fam, n)
    f = sum(1 for c in counts if 2 * c > m)
    gehalf = sum(1 for c in counts if 2 * c >= m)
    sizes = [popcount(x) for x in Fam]
    k, nmax = min(sizes), max(sizes)
    ge1 = all(c >= 1 for c in counts)          # every element present
    ok_uc = decide_union_closed(Fam)
    ok_ef = 0 not in Fam
    assert ok_uc and ok_ef
    assert m == 71, m
    assert k == 3 and nmax == 8, (k, nmax)
    assert f == 2, f
    assert gehalf == 2, gehalf
    assert ge1
    assert counts[0] == counts[1] == 67, counts
    assert all(c == 35 for c in counts[2:8]), counts
    print("constructed P_3^8 (n=8, 71 sets):")
    # print a compact description (63 A-sets compressed, E and O in full)
    print("  A = {A subset [8] : {0,1} subset A, |A| >= 3}   (63 sets)")
    print("  E = {{0,2,4},{0,2,6},{0,4,6},{0,2,4,6}}")
    print("  O = {{1,3,5},{1,3,7},{1,5,7},{1,3,5,7}}")
    print("  P_3^8 = A | E | O")
    sample = sorted(Fam)[:5]
    print("  sample members: " + " ; ".join("{" + "".join(
        nname(i) for i in range(8) if (m >> i) & 1) + "}" for m in sample))
    print(f"oracle verification (lib.uc):")
    print(f"  |F|           = {m}   (paper: 63+4+4 = 71)")
    print(f"  decide_union_closed(F) = {ok_uc}   (paper: union-closed)")
    print(f"  empty-free    = {ok_ef}")
    print(f"  min set size  = {k}, max set size = {nmax}   (paper: (2,3,8))")
    print(f"  every element present = {ge1}")
    print(f"  counts: elements 0,1 in {counts[0]} sets; elements 2..7 in "
          f"{counts[2]} sets (paper: 67 and 35)")
    print(f"  f = # strict-abundant = {f}   (paper: exactly 2 abundant, "
          f"0 and 1)")
    print(f"  # elements with 2c >= |F| = {gehalf}")
    assert 2 * counts[0] > m and 2 * counts[2] < m
    print(f"  check: 2*67 = 134 > 71 and 2*35 = 70 < 71 -> "
          f"0,1 abundant, 2..7 strictly below half")
    print("  => a k=3 union-closed EMPTY-FREE family with exactly 2 "
          "strict-abundant")
    print("     elements needs ground set n = 8 (= 2k+2); the construction "
          "idea")
    print("     cannot produce a k=3 family with f=0 at n <= 6 (nor any "
          "n, by (C))")
    print("  (part 4 checks only)\n")


def part5():
    """n = 7, k = 3 boundary: first n where constraint (C) is compatible with
    a counterexample (2k+1 = 7) AND KPT Thm 5(1) (k >= n-3) no longer forces
    f >= k.  Thm 5(2) with k = n-4 gives f >= k-1 = 2, so the minimal
    achievable f is 2; their (2,k,n)-construction inequality FAILS at n=7
    (holds at n=8: P_3^8).  Question: does a (2,3,7)-construction exist?
    f=0 is OUT OF REACH: n <= 12 is machine-verified UC (Vuckovic-Zivkovic),
    so no counterexample exists at n=7; the search is a boundary probe for
    how small f can get, not a verification.
    """
    print("=" * 74)
    print("PART 5 -- n = 7, k = 3 boundary: hunt a (2,3,7)-construction")
    print("          (f=2, k=3, n=7: minimal n allowed by KPT Thm 5(2);")
    print("           their Thm 6(2) inequality fails here, holds at n=8)")
    print("          f=0 impossible (n<=12 machine-verified UC); this is a")
    print("          boundary probe for minimal f, not a verification.")
    print("=" * 74)
    t0 = time.monotonic()
    n = 7
    masks = [m for m in range(1, 1 << n) if popcount(m) >= 3]    # 99 masks
    three = [m for m in masks if popcount(m) == 3]               # 35 masks
    rng = Random(20260708)

    found_f2 = 0
    minf = None
    minf_witness = None
    f2_witnesses = []
    fdist = {}
    total = 0

    def note(fam):
        nonlocal total, found_f2, minf, minf_witness
        total += 1
        ev = evaluate(fam, n)
        if ev["k"] != 3:
            return
        fdist[ev["f"]] = fdist.get(ev["f"], 0) + 1
        if ev["f"] == 2:
            found_f2 += 1
            if len(f2_witnesses) < 3:
                f2_witnesses.append((frozenset(fam), ev))
        if minf is None or ev["f"] < minf:
            minf = ev["f"]
            minf_witness = (frozenset(fam), ev)

    # sweep 1: closures of up to 3 generators from ALL 99 size->=3 masks
    for i in range(1, 4):
        for gent in combinations(masks, i):
            if not any(popcount(m) == 3 for m in gent):
                continue
            note(closure_small(gent))
    print(f"  sweep 1 (<=3 generators, all masks, k=3): "
          f"{time.monotonic()-t0:.1f}s, total {total}")

    # sweep 2: closures of 4 generators restricted to 3-sets
    for gent in combinations(three, 4):
        note(closure_small(gent))
    print(f"  sweep 2 (4 three-set generators): "
          f"{time.monotonic()-t0:.1f}s, total {total}")

    # sweep 3: random generator sets of size 4..10
    for _ in range(20000):
        i = rng.randint(4, 10)
        gent = set(rng.sample(masks, i))
        if not any(popcount(m) == 3 for m in gent):
            gent = set(rng.sample(masks, i - 1)) | {rng.choice(three)}
        note(closure_small(gent))
    print(f"  sweep 3 (random 4..10 gens x20000): "
          f"{time.monotonic()-t0:.1f}s, total {total}")

    print(f"\n  n=7 k=3 families constructed & checked: {total}")
    print(f"  f=0 found: 0 (required by n<=12 machine-verified UC)")
    print(f"  min f found: {minf}"
          + ("" if minf is None else
             f"  (KPT Thm 5(2) lower bound: f >= k-1 = 2)")
          )
    print(f"  f-distribution: {str({k: fdist[k] for k in sorted(fdist)})[:180]}")
    print(f"  (2,3,7)-constructions found: {found_f2}")
    for fam, ev in f2_witnesses:
        assert decide_union_closed(fam)
        assert 0 not in fam
        assert min(popcount(x) for x in fam) == 3
        assert max(popcount(x) for x in fam) == 7
        wcounts = abundance(fam, n)
        wf = sum(1 for c in wcounts if 2 * c > len(fam))
        assert wf == 2, (fam, wf)
        print(f"    witness: |F|={ev['m']} F={fam_str(fam, n)} "
              f"k=3 n=7 f=2 counts={profile_str(ev['counts'])}")
        print("      oracle recheck: union-closed, empty-free, k=3, nmax=7, "
              "f=2 all match")
    if minf_witness:
        wfam, wev = minf_witness
        if found_f2 == 0:
            print(f"  best found: f={wev['f']} |F|={wev['m']} "
                  f"F={fam_str(wfam, n)} counts={profile_str(wev['counts'])}")
            print("  => a (2,3,7)-construction NOT found in this probe; "
                  "k=3 at n=7 may force f>=3")
    print(f"  (part 5 took {time.monotonic() - t0:.1f}s)\n")
    return found_f2, minf


def main():
    t_all = time.monotonic()
    print("constraint_delim.py -- delimit how close the held minimal-"
          "counterexample constraints come to forcing UC")
    print("oracle: lib.uc.decide_union_closed + lib.uc.abundance "
          "(exact integer counts); strict test 2*c > |F|")
    print("range : n=1..4 exhaustive; n=5 class-exhaustive; n=6,7 k=3 "
          "construction probes; n=8 one explicit family")
    run_guards()
    part1()
    part2()
    part3()
    part4()
    part5()
    print("=" * 74)
    print("SUMMARY -- how close the held constraints come to forcing UC")
    print("  n<=4 (exhaustive, 2546 empty-free UC): (i) A&C holds widely;")
    print("  (ii) f=0 families: 0 -- UC itself holds there, so the")
    print("  constraints are tested on a domain where NO counterexample")
    print("  exists; the closest any family comes is one element at exactly")
    print("  density 1/2 (d=1). Boundary of the held-constraint machinery:")
    print("  n<=6 k=3: KPT Thm 5(1) (k>=n-3) forces f>=k, f=0 excluded;")
    print("  n=7  k=3: (C) compatible and Thm 5(2) gives f>=2 -- probe finds")
    print("  min f per part5 (see above); n=8 k=3: P_3^8 attains f=2 with")
    print("  ALL of A, C (and D: |F|=71 >= 51) holding -- the closest the")
    print("  two-abundant construction idea reaches; f=0 untouched.")
    print(f"  total wall time {time.monotonic() - t_all:.1f}s")
    return 0


def _run_and_capture():
    if FAST:
        return main()
    tmp_fd, tmp_path = tempfile.mkstemp(
        prefix="constraint_delim.", suffix=".captured.txt.tmp",
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
    except Exception as e:
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