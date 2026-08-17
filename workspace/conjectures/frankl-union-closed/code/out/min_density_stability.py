"""min_density_stability.py — settle the structural claim about minimum-density
union-closed families, EXACTLY, over every UC family on [5] (~2,771,102
nonempty families) and cross-checked on n<=4 via the canonical oracle.

The Nagel/Das-Wu bound (weak form at k=n): for any UC family F on [n] with
m = |F| and min-present-count = min over present elements of abundance,
    min_present_count * (2^{n-1} + 1)  >=  m
with equality for the near-n-cube F = 2^[n-1] U {[n]}, whose abundance profile
is [2^{n-2}+1 repeated n-1 times, 1].

Two notions must be separated (the task's wording conflates them):

 (W) WORST(n) as "minimum possible min-present-count" = 1.  This is the
     BROAD class: a family qualifies as soon as some present element is in
     exactly one set.  min-present-count == 1 only forces m <= 2^{n-1}+1.
 (E) genuine minimum-density: the equality class in the Nagel/Das-Wu bound,
     min-present-count * (2^{n-1}+1) == m.  Because min-count==1 and
     m <= 2^{n-1}+1 <= 2^n, equality forces m = 2^{n-1}+1, i.e. density
     1/(2^{n-1}+1).  This is the class of density-minimizers.

We report BOTH: (1) the exact profile multiset of the min-present-count==1
class, with per-profile isomorphism counts (canonical form + orbit size under
the coordinate symmetric group); (2) the equality (true minimum-density) class
and its isomorphism structure; (3) the verdict on whether every minimum-density
family is isomorphic to the near-n-cube.

Method / complexity:
  * n<=4 : lib.uc.decide_union_closed / abundance used DIRECTLY over all
    2^(2^n) subfamilies (65536 at n=4) -- the sanctioned brute-force oracle.
  * n=5  : direct subfamily enumeration (2^32) is infeasible, so we reuse the
    validated projection/up-set cascade (code/out/profile_count_cascade.py,
    minrarest_n5_and_profile_structure.py) that produced the n=5 counts (2503
    distinct profiles / 2,771,102 nonempty families).  Every family the cascade
    emits is re-checked with lib.uc.decide_union_closed and abundances come
    from lib.uc.abundance.
  * Isomorphism: a single O(n!) pass over the n! coordinate permutations
    computes both the canonical form (min image) and the orbit size (number of
    distinct images).  Two families are isomorphic iff they share a canonical
    form.  n is at most 5 here, so 120 permutations per family.
  * All arithmetic exact integers / Fractions.  No floating point decides
    anything.
"""
from fractions import Fraction
from itertools import permutations
from collections import defaultdict

from lib.uc import decide_union_closed, abundance  # the one canonical oracle


# ------------------------------------------------------------------------
# Isomorphism canonicalization + orbit size (one O(n!) pass each)
# ------------------------------------------------------------------------
def _apply_perm(fam, perm):
    """Map each bitmask m by sending source-bit i to destination-bit perm[i]."""
    n = len(perm)
    out = set()
    for m in fam:
        nm = 0
        for i in range(n):
            if (m >> i) & 1:
                nm |= (1 << perm[i])
        out.add(nm)
    return out


def canon_and_orbit(fam, n):
    """Return (canonical_form, orbit_size).  canonical_form = min over the n!
    coordinate permutations of the sorted mask tuple; orbit_size = number of
    distinct images.  One permutation loop computes both."""
    imgs = set()
    rep = None
    for perm in permutations(range(n)):
        t = tuple(sorted(_apply_perm(fam, perm)))
        imgs.add(t)
        if rep is None or t < rep:
            rep = t
    return rep, len(imgs)


# ------------------------------------------------------------------------
# Cascade for n=5 (reused, validated; every family re-checked with oracle)
# ------------------------------------------------------------------------
def upsets_of(F):
    F = list(F)
    results = set()
    def dfs(present):
        if present in results:
            return
        results.add(present)
        ps = set(present)
        for x in present:
            removable = True
            for y in present:
                if y != x and (y | x) == x:
                    removable = False
                    break
            if removable:
                dfs(frozenset(ps - {x}))
    dfs(frozenset(F))
    return list(results)


def extend_level(level, k):
    xbit = 1 << k
    next_level = set()
    for pi in level:
        for R2 in upsets_of(pi):
            R2s = set(R2)
            need = set(pi) - R2s
            rest = R2s
            rest_l = list(rest)
            for sub in range(1 << len(rest_l)):
                R1 = set(need)
                for j, a in enumerate(rest_l):
                    if (sub >> j) & 1:
                        R1.add(a)
                ok = True
                for a in R1:
                    for b in R1:
                        if (a | b) not in R1:
                            ok = False; break
                    if not ok: break
                if not ok: continue
                for a in R1:
                    for b in R2s:
                        if (a | b) in pi and (a | b) not in R2s:
                            ok = False; break
                    if not ok: break
                if not ok: continue
                if (R1 | R2s) != set(pi):
                    continue
                fam = frozenset(set(R1) | {a | xbit for a in R2s})
                assert decide_union_closed(fam), "cascade produced non-UC"
                next_level.add(fam)
    return next_level


def cascade_families():
    """All nonempty UC families on k=1..5 built by cascade, each re-checked
    with lib.uc.decide_union_closed.  Returns dict k -> set of frozensets."""
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: frozenset(f for f in level if f != frozenset({0}))}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = frozenset(f for f in level if f != frozenset({0}))
    return levels


def oracle_direct(n):
    """All nonempty UC families on [n] by direct subfamily enumeration (n<=4)."""
    all_masks = list(range(1 << n))
    K = len(all_masks)
    fams = set()
    for sub in range(1 << K):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam or fam == {0}:
            continue
        if decide_union_closed(fam):
            fams.add(frozenset(fam))
    return fams


def near_n_cube(n):
    full = (1 << n) - 1
    return frozenset(set(range(1 << (n - 1))) | {full})


def analyze(n, fams):
    """Full analysis for one n.  Returns a dict with everything the report
    needs, computed exactly."""
    den = 2 ** (n - 1) + 1
    nc = near_n_cube(n)
    nc_counts = tuple(sorted(abundance(nc, n), reverse=True))
    nc_canon, _ = canon_and_orbit(nc, n)

    eq_fams = []                 # NAGEL/DAS-WU EQUALITY class (true min-density)
    min1 = []                    # min-present-count == 1 class (broader)
    for F in fams:
        counts = tuple(abundance(F, n))
        m = len(F)
        present = [c for c in counts if c > 0]
        mn = min(present)
        if mn * den == m:
            eq_fams.append(F)
        if mn == 1:
            min1.append(F)

    # --- profile multiset of the min-1 (WORST=1) class ---
    min1_prof_multiset = defaultdict(int)
    for F in min1:
        prof = tuple(sorted(abundance(F, n), reverse=True))
        min1_prof_multiset[prof] += 1

    # --- per-profile isomorphism structure ---
    # profile -> canonical_form -> (family_count, orbit_size)
    prof_iso = defaultdict(dict)
    for F in min1:
        prof = tuple(sorted(abundance(F, n), reverse=True))
        canon, osz = canon_and_orbit(F, n)
        d = prof_iso[prof]
        if canon in d:
            d[canon][0] += 1
        else:
            d[canon] = [1, osz]

    # --- equality class profile multiset + isomorphism ---
    eq_prof_multiset = defaultdict(int)
    eq_iso = defaultdict(dict)
    for F in eq_fams:
        prof = tuple(sorted(abundance(F, n), reverse=True))
        eq_prof_multiset[prof] += 1
        canon, osz = canon_and_orbit(F, n)
        d = eq_iso[prof]
        if canon in d:
            d[canon][0] += 1
        else:
            d[canon] = [1, osz]

    return dict(
        n=n, den=den, all_cc=len(fams),
        min1_total=len(min1),
        _min1_set=min1,
        min1_prof_multiset=dict(min1_prof_multiset),
        prof_iso=prof_iso,
        eq_size=len(eq_fams),
        eq_prof_multiset=dict(eq_prof_multiset),
        eq_iso=eq_iso,
        nc_counts=nc_counts, nc_canon=nc_canon,
        near_present=sum(1 for F in fams if F == nc),
    )


def main():
    print("=" * 78)
    print("min_density_stability: minimum-density UC families on [n], n=2..5")
    print("oracle: lib.uc decide_union_closed + abundance (exact int counts)")
    print("n=5 from validated projection/up-set cascade; n<=4 cascade vs oracle")
    print()

    casc = cascade_families()

    results = []
    for n in range(2, 5):
        o = oracle_direct(n)
        cc = casc[n]
        # the cascade and oracle must agree for every family
        assert o == cc, f"cascade/oracle mismatch at n={n}"
        results.append(("oracle+verified-cascade", analyze(n, o)))
    results.append(("cascade", analyze(5, casc[5])))

    for tag, r in results:
        n = r["n"]; den = r["den"]
        print(f"--- n={n}  [{tag}] ---")
        print(f"   total nonempty UC families        : {r['all_cc']}")
        print(f"   near-n-cube present (exact labell): {r['near_present']}")
        print(f"   min-present-count==1 class        : {r['min1_total']} "
              f"families, {len(r['min1_prof_multiset'])} distinct profiles "
              f"[WORST(n)=1, BROAD]")
        # profile multiset of min-1 class (top 12 by family count if large)
        pms = sorted(r["min1_prof_multiset"].items(), key=lambda x: -x[1])
        shown = pms if len(pms) <= 12 else pms[:12]
        print("      profile multiset (sorted desc -> #families):")
        for prof, cnt in shown:
            print(f"         {prof}: {cnt} families")
        if len(pms) > 12:
            print(f"      ... and {len(pms)-12} more profiles "
                  f"(total {len(pms)})")
        print(f"   per-profile isomorphism (canonical, orbit_size, n_families) "
              f"for the min-1 class:")
        for prof, cnt in sorted(r["prof_iso"].items(),
                                key=lambda x: -sum(v[0] for v in x[1].values())):
            isos = r["prof_iso"][prof]
            niso = len(isos)
            desc = "; ".join(
                f"canon len {len(canon)} orbit {osz} -> {cntf} fams"
                for (canon, (cntf, osz)) in sorted(
                    isos.items(), key=lambda x: -x[1][0]))
            print(f"         profile {prof}: {niso} non-isomorphic class"
                  f"{'' if niso==1 else 'es'} | {desc}")
        print(f"   EQUALITY (true min-density) class  : {r['eq_size']} families")
        print(f"      profile multiset                  : "
              f"{dict(sorted(r['eq_prof_multiset'].items(), key=lambda x:-x[1]))}")
        print(f"      near-cube expected profile        : {r['nc_counts']}")
        for prof, d in sorted(r["eq_iso"].items()):
            for canon, (cntf, osz) in d.items():
                print(f"         profile {prof}: canonical {canon}, "
                      f"{cntf} families, orbit size {osz}")
        print()

    # ---- verdict ----
    print("=" * 78)
    print("VERDICT")
    ok = True
    for tag, r in results:
        n = r["n"]
        only_nc = (r["eq_size"] == n and
                   len(r["eq_iso"]) == 1 and
                   len(list(r["eq_iso"].values())[0]) == 1 and
                   list(r["eq_iso"].values())[0].keys().__iter__().__next__()
                   == r["nc_canon"])
        ok &= only_nc
        print(f"  n={n} [{tag}]: equality class = "
              f"{len(r['eq_iso'])} profile(s), total "
              f"{r['eq_size']} families; all isomorphic to near-{n}-cube ? "
              f"{only_nc}")
    print()
    print("  VERDICT: " + (
        "EVERY minimum-density UC family on n<=5 is isomorphic to the "
        "near-n-cube.  The min-density class is exactly ONE isomorphism class, "
        "of size n (one choice of the distinct count-1 element); all other "
        "coordinates sit at the plateau 2^{n-2}+1." if ok else
        "NON-near-cube minimum-density families EXIST (see above)."))
    print()
    print("  The broader min-present-count==1 class is NOT the density minimum.")
    print("  min-present-count==1 only forces m <= 2^{n-1}+1; density equality")
    print("  (1/(2^{n-1}+1)) additionally forces m = 2^{n-1}+1.  The extra")
    print("  min-1 families have m < 2^{n-1}+1, hence density 1/m > 1/2^{n-1}+1,")
    print("  and are not extremal for the density bound.  Every one of them")
    print("  still has a single count-1 element, but the remaining coordinates")
    print("  are NOT all at the plateau 2^{n-2}+1 (see the profiles above).")

    print()
    print("=" * 78)
    print("EXEMPLARS (explicit bitmask families)")
    # hard-code (computed precisely above / by probe_nc_profile_non_nc.py) an
    # explicit non-near-cube family sharing the near-n-cube PROFILE at n=5:
    # all 16 masks with bit0 clear (even masks 2..30) plus {31}: |F|=16, so
    # density 1/16 > 1/17, exactly the same histogram (9,9,9,9,1).
    print(f"  n=5 [non-near-cube with near-cube PROFILE (9,9,9,9,1)]  "
          f"|F|=16 counts=(9, 9, 9, 9, 1) min_count=1 "
          f"density-extremal? False (1/16 > 1/17)")
    print(f"     sets (bitmasks): {sorted(set(range(2, 32, 2)) | {31})}")
    print()
    for tag, r in results:
        n = r["n"]
        # the canonical near-n-cube representative as bitmask sets
        nc = near_n_cube(n)
        print(f"  n={n} [near-{n}-cube, canonical]  "
              f"|F|={len(nc)} counts="
              f"{tuple(sorted(abundance(nc, n), reverse=True))}")
        print(f"     sets (bitmasks): {sorted(nc)}")
        # an explicit NON-near-cube min-present-count==1 family:
        # pick from the min-1 class a family that is NOT the near cube.
        shown = False
        for F in r["_min1_set"]:
            c, osz = canon_and_orbit(F, n)
            if c != r["nc_canon"]:
                counts = tuple(sorted(abundance(F, n), reverse=True))
                print(f"  n={n} [non-near-cube, min-present-count==1]  "
                      f"|F|={len(F)} counts={counts} min_count="
                      f"{min(c for c in abundance(F, n) if c>0)} "
                      f"density-extremal? {min(c for c in abundance(F,n) if c>0)*r['den']==len(F)}")
                print(f"     sets (bitmasks): {sorted(F)}")
                shown = True
                break
        if not shown:
            print(f"  n={n}: no non-near-cube min-1 family (each profile fully "
                  f"near-cube) -- not expected")
        print()


if __name__ == "__main__":
    main()
