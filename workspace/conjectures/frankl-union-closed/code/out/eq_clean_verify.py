"""CLEAN verification of the EQ(n) structural decomposition (no tuple-index bugs):

Structural claim (n<=5 exhaustive, exact):
  An empty-free union-closed family F satisfies f == min{nn, 2k-nn+1}
  (KPT Thm 5(3) equality)  iff  F is a singleton {A} (A != empty)
  OR  F is a two-chain {A, A u {x}} with A != empty, x notin A.
  Equivalently: no family with >= 3 sets, and no 2-set family that isn't a
  strict two-chain, achieves the equality.

Then EQ(n) = (2^n - 1) + #two-chains, and #two-chains = sum_{k=1}^{n-1} C(n,k)(n-k)
= n(2^{n-1} - 1).  So EQ(n) = (n+2)2^{n-1} - n - 1 = A053221.
"""
import importlib.util
spec = importlib.util.spec_from_file_location(
    "profile_count_cascade", "code/out/profile_count_cascade.py")
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)


def popcount(x):
    return bin(x).count("1")


def eq_class(F, n):
    """Return 'single', 'twochain', 'other-eq', or None (not eq)."""
    if 0 in F:
        return None
    m = len(F)
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    f = sum(1 for c in counts if 2 * c > m)
    ks = [popcount(s) for s in F]
    k = min(ks); nn = max(ks)
    if f != min(nn, 2 * k - nn + 1):
        return None
    if m == 1:
        return 'single'
    if m == 2:
        a, b = tuple(F)
        sa, sb = popcount(a), popcount(b)
        # strict two-chain: smaller is a proper subset of larger, one bigger
        smaller, larger = (a, b) if sa <= sb else (b, a)
        if (smaller | larger) == larger and popcount(larger) == popcount(smaller) + 1:
            return 'twochain'
        return 'other-eq'
    return 'other-eq'


def main():
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: level}
    for k in range(1, 5):
        level = pc.extend_level(level, k)
        levels[k + 1] = level
    expected = {1: 2, 2: 12, 3: 120, 4: 4958, 5: 2771102}
    for n in range(1, 6):
        nonempty = {f for f in levels[n] if f != frozenset({0})}
        assert len(nonempty) == expected[n]

    print("clean EQ decomposition n=1..5 (cascade, exact)")
    print("oracle: profile_count_cascade (validated vs A121921)")
    print("range : n=1..5, ALL empty-free nonempty UC families, no floats")
    for n in range(1, 6):
        nonempty = {f for f in levels[n] if f != frozenset({0})}
        eq = [f for f in nonempty if eq_class(f, n) is not None]
        cats = {}
        other = []
        for f in nonempty:
            c = eq_class(f, n)
            if c is not None:
                cats[c] = cats.get(c, 0) + 1
                if c == 'other-eq':
                    other.append((sorted(f), n))
        singles = cats.get('single', 0)
        tcs = cats.get('twochain', 0)
        formula_tc = n * (2 ** (n - 1) - 1)
        formula = (2 ** n - 1) + formula_tc
        print(f"n={n}: EQ={len(eq)}  singles={singles}  twochains={tcs}  "
              f"other={cats.get('other-eq',0)}")
        print(f"      formula=(2^n-1)+n(2^(n-1)-1) = {formula}  match={formula == len(eq)}")
        print(f"      twochain count == n(2^(n-1)-1): {tcs == formula_tc}")
        if other:
            print("      OTHER EQ EXAMPLES (would refute):")
            for masks, nn in other[:5]:
                print("       ", masks)


if __name__ == "__main__":
    main()
