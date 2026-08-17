"""Verify the EQ(n) derivation:

EQ(n) = # empty-free UC families F with f == min{nn, 2k-nn+1}  (KPT Thm 5(3) equality),
where k = min set size, nn = max set size, f = # strict-abundant elements (2c > |F|).

Claim (structural decomposition, n<=5 exhaustive):
  (i)   every EQ family is EITHER a single-set family (len(F)==1) OR a two-chain
        {A, A u {x}} with A nonempty, x notin A (len(F)==2, A subset top, |top|=|A|+1);
  (ii)  conversely every singleton and every two-chain satisfies the equality;
  (iii) hence EQ(n) = (2^n - 1) + n(2^{n-1} - 1) = (n+2)2^{n-1} - n - 1 = A053221.

We verify (i),(ii) exhaustively n=1..5 via the validated cascade, and verify
(iii) as exact equality. Each EQ family is printed with len(F) so we can
confirm no len>=3 family is EQ.
"""
import importlib.util
from collections import defaultdict

spec = importlib.util.spec_from_file_location(
    "profile_count_cascade", "code/out/profile_count_cascade.py")
pc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pc)


def popcount(x):
    return bin(x).count("1")


def main():
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels = {1: level}
    for k in range(1, 5):
        level = pc.extend_level(level, k)
        levels[k + 1] = level

    expected = {1: 2, 2: 12, 3: 120, 4: 4958, 5: 2771102}
    for n in range(1, 6):
        nonempty = {f for f in levels[n] if f != frozenset({0})}
        assert len(nonempty) == expected[n], (n, len(nonempty), expected[n])

    print("verify EQ decomposition n=1..5 (cascade, exact)")
    print("oracle: profile_count_cascade (validated vs A121921 all levels)")
    print("range : n=1..5, ALL empty-free nonempty UC families, no floats")

    for n in range(1, 6):
        nonempty = {f for f in levels[n] if f != frozenset({0})}
        eq = []          # (masks,len,k,nn,f,is_single,is_twochain)
        by_len = defaultdict(int)
        for F in nonempty:
            if 0 in F:
                continue
            m = len(F)
            counts = [0] * n
            for s in F:
                for i in range(n):
                    if (s >> i) & 1:
                        counts[i] += 1
            f = sum(1 for c in counts if 2 * c > m)
            ks = [popcount(s) for s in F]
            k = min(ks)
            nn = max(ks)
            if f != min(nn, 2 * k - nn + 1):
                continue
            is_single = (m == 1)
            # two-chain: m==2 and A subset B and |B|==|A|+1
            is_tc = False
            if m == 2:
                a, b = tuple(F)
                sa, sb = popcount(a), popcount(b)
                if (a | b) == b and sb == sa + 1:
                    is_tc = True
            by_len[m] += 1
            eq.append((sorted(F), m, k, nn, f, is_single, is_tc))
        singles = sum(1 for e in eq if e[1] == 1)
        tcs = sum(1 for e in eq if e[5] or e[6])
        non_single = len(eq) - singles
        only_single_or_tc = all((not e[5]) or (e[1] == 1) for e in eq)
        # check: every single is_single, every two-chain is_tc, nothing else
        rest_ok = all((e[1] == 1 and e[5]) or (e[1] == 2 and e[6] and not e[5])
                      for e in eq)
        twochains = sum(1 for e in eq if e[6])
        # formula
        formula = (2 ** n - 1) + n * (2 ** (n - 1) - 1)
        check = (2 ** n - 1) + n * (2 ** (n - 1) - 1)
        print(f"n={n}: EQ={len(eq)}  singles={singles}  twochains={twochains} "
              f"len>=3_EQ_fams={len(eq)-singles-twochains}")
        print(f"      formula (2^n-1)+n(2^(n-1)-1)={formula}  "
              f"match={formula == len(eq)}")
        print(f"      every EQ family is single-or-twochain: "
              f"{all((e[1]==1) or (e[1]==2 and e[6]) for e in eq)}")
        print(f"      by |F| (len->count): {dict(sorted(by_len.items()))}")


if __name__ == "__main__":
    main()
