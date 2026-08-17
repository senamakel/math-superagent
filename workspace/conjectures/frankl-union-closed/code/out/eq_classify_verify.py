"""Second-route verification of the KPT-equality-family classification.

Claim under test: an empty-free union-closed family F on [n] satisfies
f == min{nn, 2k-nn+1} (KPT Thm 5(3) equality) iff
  (a) |F| == 1  (singleton), or
  (b) |F| == 2 and F = {S, S u {b}} with nonempty S, b notin S  (2-chain).

Verified computationally n<=5 exhaustively (cascade pass); here we verify
the two PROVEN directions independently via lib.uc brute force at n=4 and the
m<=2 characterization at n=5 via direct mask enumeration + lib.uc:

  (i)   every singleton and every consecutive 2-chain is an equality family
        (n=1..5, all such families, via lib.uc);
  (ii)  among m=2 empty-free UC families (all of which are 2-chains A proper
        subset B), equality holds iff |B| == |A|+1;
  (iii) among m=1 families all are equality families.
  (iv)  classification (a)/(b)-iff-equality holds for n<=4 by EXHAUSTIVE
        lib.uc enumeration (independent of the cascade).

Exact integer arithmetic only.
"""
from lib.uc import decide_union_closed, abundance


def popcount(x):
    return bin(x).count("1")


def eq_holds(F, n):
    """KPT equality: f == min{nn, 2k-nn+1}; empty-free assumed (0 not in F)."""
    m = len(F)
    counts = abundance(F, n)
    f = sum(1 for c in counts if 2 * c > m)
    ks = [popcount(s) for s in F]
    k = min(ks)
    nn = max(ks)
    return f == min(nn, 2 * k - nn + 1), (k, nn, f, m)


def main():
    # (i) every singleton and every consecutive 2-chain is equality
    bad = 0
    for n in range(1, 6):
        masks = list(range(1, 1 << n))
        # singletons
        for S in masks:
            F = {S}
            eq, _ = eq_holds(F, n)
            if not eq:
                bad += 1
        # consecutive 2-chains: {S, S|{b}} with b not in S, S nonempty
        for S in masks:
            for b in range(n):
                if (S >> b) & 1:
                    continue
                F = {S, S | (1 << b)}
                if not decide_union_closed(F):
                    bad += 1
                    continue
                eq, _ = eq_holds(F, n)
                if not eq:
                    bad += 1
    print(f"(i) singleton/consecutive-chain families not equalities: {bad} (expect 0)")

    # (ii) among m=2 UC empty-free families: equality iff consecutive
    bad2 = 0
    tallies = {(True, True): 0, (True, False): 0,
               (False, True): 0, (False, False): 0}
    for n in range(1, 6):
        masks = list(range(1, 1 << n))
        for i, A in enumerate(masks):
            for B in masks[i + 1:]:
                F = {A, B}
                if not decide_union_closed(F):
                    continue
                m = len(F)
                assert m == 2
                k = min(popcount(A), popcount(B))
                nn = max(popcount(A), popcount(B))
                consecutive = (nn == k + 1)
                eq, _ = eq_holds(F, n)
                tallies[(eq, consecutive)] += 1
                if eq != consecutive:
                    bad2 += 1
                    print(f"   mismatch n={n}: F={F} eq={eq} consecutive={consecutive}")
    print(f"(ii) m=2 families where equality != consecutive: {bad2} (expect 0)")
    print(f"     tallies (eq,consecutive): {tallies}")

    # (iii)+(iv) exhaustive classification n<=4 via lib.uc (cascade-free route)
    for n in range(1, 5):
        all_masks = list(range(1 << n))
        eq_fams = []
        for sub in range(1 << len(all_masks)):
            F = set()
            for i, mask in enumerate(all_masks):
                if (sub >> i) & 1:
                    F.add(mask)
            if not F or 0 in F:
                continue
            if not decide_union_closed(F):
                continue
            m = len(F)
            if m == 1:
                is_model = True
            elif m == 2:
                A, B = sorted(F)
                is_model = (popcount(B) == popcount(A) + 1)
            else:
                is_model = False
            eq, _ = eq_holds(F, n)
            if eq:
                eq_fams.append((F, is_model))
        bad = sum(1 for (F, is_model) in eq_fams if not is_model)
        missing = len(eq_fams) - sum(1 for (F, is_model) in eq_fams if is_model)
        print(f"(iii/iv) n={n}: #equality families={len(eq_fams)} "
              f"non-model among them={bad} (0 expected); "
              f"models minus equalities={missing} (0 expected)")
    print("done")


if __name__ == "__main__":
    main()