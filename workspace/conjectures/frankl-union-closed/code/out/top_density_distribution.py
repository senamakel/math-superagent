"""Distribution of the top (max) element density among UC families on [n],
n=2..5, using the validated canonical cascade. 

Motivation: a minimal counterexample must have NO abundant element, i.e. every
element density < 1/2. At n<=5 every UC family HAS an abundant element, so we
measure how 'marginal' the families are: the count of families whose top density
is exactly 1/2 vs. strictly above. Families at exactly 1/2 are the closest
thing to a counterexample that exists on small n, and their count sequence as a
function of n is a candidate exploitable structure.

We also record (for each n) how many families have top density == 1/2, and how
many have a unique element at density exactly 1/2 (a genuinely 'half-abundant'
element). 
"""
from fractions import Fraction


def is_uc(F):
    F = list(F)
    for a in F:
        for b in F:
            if (a | b) not in F:
                return False
    return True


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
                next_level.add(fam)
    return next_level


def abundance(F, n):
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def analyze_level(fams, n):
    """Return (total, half_top, surplus_top, exact_half_present) counts."""
    total = 0
    half_top = 0            # top density == 1/2
    surplus_top = 0         # top density > 1/2 (the strict case)
    half_fams = []          # example families with top density == 1/2
    for F in fams:
        counts = abundance(F, n)
        m = len(F)
        present = [c for c in counts if c > 0]
        top = max(present)
        den = Fraction(top, m)
        total += 1
        if den == Fraction(1, 2):
            half_top += 1
            if len(half_fams) < 3:
                half_fams.append(sorted(F))
        elif den > Fraction(1, 2):
            surplus_top += 1
    return total, half_top, surplus_top, half_fams


def main():
    # build levels n=1..5
    levels = {}
    level = {frozenset({0}), frozenset({1}), frozenset({0, 1})}
    levels[1] = {f for f in level if f != frozenset({0})}
    for k in range(1, 5):
        level = extend_level(level, k)
        levels[k + 1] = {f for f in level if f != frozenset({0})}
    print("n | UC families | top==1/2 | top>1/2 | top<1/2(none expected)")
    print("--+-------------+---------+---------+----------------------")
    seq_half = []
    seq_total = []
    for n in range(1, 6):
        t, h, s, ex = analyze_level(levels[n], n)
        seq_half.append(h)
        seq_total.append(t)
        print(f"{n} | {t:9} | {h:7} | {s:7} | families with top<1/2: "
              f"{t - h - s}")
        if n == 4 and ex:
            print("   example top==1/2 fam:", ex)
        if n == 5:
            print("   example top==1/2 fam:", ex)
    print("\nSequence: UC families whose TOP density == 1/2 (n=1..5):", seq_half)
    print("Sequence: total UC families (n=1..5):", seq_total)


if __name__ == "__main__":
    main()
