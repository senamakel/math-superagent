"""Attack the EQ-decomposition structural lemma at larger n.

Structural lemma (crux of EQ(n) = (n+2)2^{n-1} - n - 1):
  An empty-free union-closed family F with f == min{N, 2k-N+1} (N = max set
  size, k = min set size, f = #strict-abundant) is a singleton or a two-chain
  {A, A u {x}}.  The N>=k+2 case (families with >2 sets) is the open direction.

Verified only n<=5 (exhaustive). Here we HUNT for a counterexample at larger
ground size n by generating many random union-closed families via closure of a
random generating set (n=6,7,8), and checking whether any has f == min{N,2k-N+1}
yet is NOT a singleton/two-chain.  Also record any EQ family found at all.

Hunt target (first falsifier): a UC family on n>=6 with f == min{N,2k-N+1}
and >2 sets (or 2 sets not a strict two-chain).  A single hit refutes the lemma
and collapses the derivation; zero hits over millions of random families is
evidence the n<=5 structure persists.
"""
import random
from lib.uc import decide_union_closed, abundance


def popcount(x):
    return bin(x).count("1")


def closure(gen, n):
    """Union-closure of a generating set of masks on [n]."""
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


def eq_check(F, n):
    """Return (is_eq, is_single_or_twochain) for empty-free UC family F."""
    if 0 in F or not F:
        return False, False
    m = len(F)
    counts = abundance(F, n)
    f = sum(1 for c in counts if 2 * c > m)
    ks = [popcount(s) for s in F]
    k = min(ks); N = max(ks)
    if f != min(N, 2 * k - N + 1):
        return False, False
    if m == 1:
        return True, True
    if m == 2:
        a, b = tuple(F)
        sa, sb = popcount(a), popcount(b)
        small, large = (a, b) if sa <= sb else (b, a)
        if (small | large) == large and popcount(large) == popcount(small) + 1:
            return True, True
        return True, False
    return True, False


def main():
    random.seed(12345)
    print("attack EQ structural lemma at n=6,7,8 via random UC closures")
    print("oracle: lib.uc (decide_union_closed, abundance) + closure()")
    print("range : random closures on [n], n=6..8; hunt counterexample")
    for n in [6, 7, 8]:
        trials = 300000 if n == 6 else (40000 if n == 7 else 5000)
        found_eq = 0
        found_bad = 0
        bad_examples = []
        eq_examples = []
        for _ in range(trials):
            base = random.sample(range(1, 1 << n), random.randint(1, 8))
            F = closure(base, n)
            if not decide_union_closed(F):
                continue
            is_eq, is_good = eq_check(F, n)
            if is_eq:
                found_eq += 1
                if len(eq_examples) < 3:
                    eq_examples.append((sorted(F), n))
                if not is_good and len(bad_examples) < 3:
                    found_bad += 1
                    bad_examples.append((sorted(F), n))
        print(f"n={n}: trials={trials}  eq_fams={found_eq}  "
              f"non-single/twochain_eq={found_bad}")
        for ex in bad_examples:
            print(f"   BAD (refutes lemma): masks={ex[0]} n={ex[1]}")
        for ex in eq_examples[:2]:
            print(f"   (eq fam example): masks={ex[0]} n={ex[1]}")


if __name__ == "__main__":
    main()
