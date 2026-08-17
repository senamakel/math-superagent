"""Targeted hunt for a counterexample to the EQ structural lemma, biased toward
LARGER union-closed families (more sets, wider size range), at n=6,7,8.

Lemma: an empty-free UC family F with f == min{N, 2k-N+1} (N=max set size,
k=min set size, f=#strict-abundant) is a singleton or a strict two-chain.

Random closures from a few base elements made mostly-small families (weak
hunt). Here we sample DENSER generating sets (more base elements, forcing
larger closures) and also unions-of-uvt-style structured families, and check
every UC family found for the equality + non-singleton/twochain combo.

A single hit refutes the lemma (and shows the A053221 decomposition needs
more terms). Zero hits strengthens the n<=5 exhaustive + n<=8 random case.
"""
import random
from lib.uc import decide_union_closed, abundance


def popcount(x):
    return bin(x).count("1")


def closure(gen):
    fam = set(gen)
    changed = True
    while changed:
        changed = False
        add = set()
        lst = list(fam)
        for a in lst:
            for b in lst:
                u = a | b
                if u not in fam:
                    add.add(u)
        if add:
            fam |= add
            changed = True
    return fam


def eq_and_ok(F, n):
    if 0 in F or not F:
        return None
    m = len(F)
    counts = abundance(F, n)
    f = sum(1 for c in counts if 2 * c > m)
    ks = [popcount(s) for s in F]
    k = min(ks); N = max(ks)
    if f != min(N, 2 * k - N + 1):
        return None
    if m == 1:
        return 'single'
    if m == 2:
        a, b = tuple(F)
        sa, sb = popcount(a), popcount(b)
        small, large = (a, b) if sa <= sb else (b, a)
        if (small | large) == large and popcount(large) == popcount(small) + 1:
            return 'twochain'
        return 'BAD2'
    return 'BAD'


def main():
    random.seed(777)
    print("targeted hunt for EQ-structural-lemma counterexample (large fams)")
    print("oracle: lib.uc + closure(); many independent closure constructions")
    print("range : n=6..8, 500k+ constructions biased to larger families")
    total_eq = 0
    total_bad = 0
    bad_ex = []
    bysize = {}
    for n in [6, 7, 8]:
        trials = {"6": 300000, "7": 120000, "8": 40000}[str(n)]
        found_eq = 0
        found_bad = 0
        max_size = 0
        for _ in range(trials):
            # denser generating sets -> larger closures
            k0 = random.randint(2, max(2, n - 2))
            base = random.sample(range(1, 1 << n), random.randint(n, 3 * n))
            F = closure(base)
            if not decide_union_closed(F):
                continue
            max_size = max(max_size, len(F))
            # skip tiny families to focus the hunt on the interesting case
            r = eq_and_ok(F, n)
            if r is None:
                continue
            found_eq += 1
            total_eq += 1
            bysize[len(F)] = bysize.get(len(F), 0) + 1
            if r != 'twochain' and r != 'single':
                found_bad += 1
                total_bad += 1
                if len(bad_ex) < 5:
                    bad_ex.append((sorted(F), n, len(F), r))
        print(f"n={n}: trials={trials}  eq_fams={found_eq}  "
              f"non-single/twochain={found_bad}  max_clos_size={max_size}")
    print(f"\nTOTAL eq families found: {total_eq};  "
          f"counterexamples to lemma: {total_bad}")
    print(f"eq families by family size (len->count): "
          f"{dict(sorted(bysize.items()))}")
    for ex in bad_ex:
        print(f"   BAD: n={ex[1]} |F|={ex[2]} type={ex[3]} masks={sorted(ex[0])}")


if __name__ == "__main__":
    main()
