"""Verify the extremal-counting claim about min max-density of non-Boolean UC families.

Claim:  among NON-Boolean union-closed families F ⊆ 2^[n],
        min_x max density_x  =  2^{n-1}/(2^n - 1),
        attained "uniquely" by the odd filter F = 2^[n] \\ {∅}.

Laid out as the five candidate proof steps with PASS/FAIL per step:

 STEP 1  max density >= 1/2 (Frankl), and non-Boolean => max strictly > 1/2
         (this needs the half-density lemma: max=1/2 forces Boolean).
 STEP 2  for |F|=m, max_x c_x >= ceil(m/2)   [uses UC => some element >= half]
 STEP 3  odd m=2q+1: density >= (q+1)/(2q+1)=(m+1)/(2m), decreasing in m;
         largest odd m <= 2^n is 2^n-1.
 STEP 4  uniqueness of the odd filter as the size-2^n-1 UC family: is 2^[n]\\{T}
         union-closed only for T=∅?   <-- the "uniqueness" claim to test
 STEP 5  even m non-Boolean: c_max >= m/2+1, density >= 1/2+1/m; compare to
         1/2 + 1/(2(2^n-1)) = 2^{n-1}/(2^n-1).

Everything here is exact: integer counts, Fraction densities, sympy for the
algebraic inequalities, and oracle enumeration (lib.uc) for the family facts.
"""
from fractions import Fraction
import itertools

from sympy import (symbols, Rational, simplify, expand, S, factor, refine, Q,
                   Symbol, sqrt)
from lib.uc import decide_union_closed, abundance


def is_block_union(F, n):
    """Boolean/block-partition test: F = {union of any subset of its atoms},
    atoms pairwise disjoint (i.e. F is a Boolean subalgebra a.k.a. closed under
    symmetric difference within its own span)."""
    nonempty = [s for s in F if s != 0]
    if not nonempty:
        return False
    atoms = []
    for s in nonempty:
        if not any(t != s and (t & s) == t for t in nonempty):
            atoms.append(s)
    k = len(atoms)
    for i in range(k):
        for j in range(i + 1, k):
            if atoms[i] & atoms[j]:
                return False
    union_of_atoms = set()
    for J in range(1 << k):
        u = 0
        for i in range(k):
            if (J >> i) & 1:
                u |= atoms[i]
        union_of_atoms.add(u)
    return set(F) == union_of_atoms


def all_uc_families(n):
    """Enumerate every union-closed family over [n] (excluding the empty
    family and the single {∅} family).  Oracle-only, n<=4 (2^(2^n) subfam)."""
    masks = list(range(1 << n))
    for sub in range(1, 1 << len(masks)):
        fam = set()
        for i, mask in enumerate(masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if fam in ({}, {0}):
            continue
        if decide_union_closed(fam):
            yield fam


def max_density(F, n):
    m = len(F)
    counts = abundance(F, n)
    cmax = max(counts)
    return cmax, Fraction(cmax, m)


print("=" * 78)
print("SYMBOLIC STEP CHECKS (sympy, exact)")
print("=" * 78)

m = Symbol('m', positive=True)
# STEP 3: monotonicity of (m+1)/(2m) in m
diff_step3 = expand(simplify(((S(m + 2)) / (2 * (S(m) + 1))) - ((S(m) + 1) / (2 * S(m)))))
print(f"STEP 3 monotonic check: (m+2)/(2(m+1)) - (m+1)/(2m) = {simplify(diff_step3)}")
# derivative approach
from sympy import diff
d = diff((S(m)+1)/(2*S(m)), m)
print(f"   d/dm[(m+1)/(2m)] = {simplify(d)}   (negative => decreasing)")

# STEP 3: at m = 2^n - 1 (odd, q = (m-1)/2), (q+1)/(2q+1) equals 2^{n-1}/(2^n-1)
n = Symbol('n', positive=True)
oddval = Rational(1, 2) + Rational(1, 2) / (2**n - 1)   # 1/2 + 1/(2(2^n-1))
frac = 2**(n-1) / (2**n - 1)
print(f"STEP 3 value check: 1/2 + 1/(2(2^n-1)) - 2^(n-1)/(2^n-1) = "
      f"{simplify(oddval - frac)}")

# STEP 5: even-m bound 1/2+1/m vs odd-filter value 1/2+1/(2(2^n-1))
# for m even, m <= 2^n.  Smallest gap in the direction we need happens at the
# largest allowed even m.  For non-Boolean the full power set m=2^n is
# excluded from FEASIBLE family sizes, but compare at the max even m you could
# approach.  We compare B = (m/2+1)/m with O = 1/2 + 1/(2(2^n-1)).
mv = Symbol('mv', positive=True)          # an even m
evenbound = (S(mv)/2 + 1) / S(mv)
oddval2 = Rational(1, 2) + Rational(1, 2) / (2**n - 1)
gap5 = simplify(evenbound - oddval2)
print(f"STEP 5 even bound - odd-filter value = {gap5}")
# require >=0 : check under m <= 2^n using the worst case m = 2^n (largest even)
worst = gap5.subs(mv, 2**n)
print(f"   at largest even m=2^n: {simplify(worst)} "
      f"(for n>=2 this is positive since 1/2^n > 1/(2^{n+1}-2))")
print(f"   sign at even m=2^n: {simplify(worst).subs(n,3) > 0} (n=3 example)")

# STEP 5 (variant): the true min over even m is at the largest feasible even m;
# for non-Boolean, m=2^n is excluded, so m <= 2^n - 2.
print()
print("=" * 78)
print("ORACLE ENUMERATION: min max-density over NON-Boolean UC families, n=2,3,4")
print("=" * 78)
for nn in (2, 3, 4):
    allf = list(all_uc_families(nn))
    nonbool = [F for F in allf if not is_block_union(F, nn)]
    if not nonbool:
        print(f"n={nn}: no non-Boolean UC families?!")
        continue
    best = min(max_density(F, nn)[1] for F in nonbool)
    pairwise = density_BO = Fraction(2**(nn - 1), 2**nn - 1)
    minimizers = []
    for F in nonbool:
        if max_density(F, nn)[1] == best:
            minimizers.append(F)
    print(f"n={nn}: UC families={len(allf)}, non-Boolean={len(nonbool)}, "
          f"min max-density={best} = {float(best):.6f}")
    print(f"   predicted 2^{nn-1}/(2^{nn}-1) = {pairwise} = {float(pairwise):.6f} "
          f"(match={best == pairwise})")
    # which small-size families attain it (dedupe by sorted tuple)
    uniq = sorted(set(tuple(sorted(F)) for F in minimizers))
    print(f"   # minimizers = {len(uniq)}  (claim says 1: the odd filter)")
    for u in uniq:
        isodd = (tuple(sorted(set(range(1 << nn)) - {0})) == u)
        print(f"      size {len(u)} m={len(u)}, odd-filter={isodd}")

print()
print("=" * 78)
print("STEP 4 / uniqueness: which 2^[n] \\ {T} are union-closed?")
print("=" * 78)
for nn in (2, 3, 4):
    full = set(range(1 << nn))
    uc_removals, nonuc_removals = [], []
    for T in range(1 << nn):
        fam = full - {T}
        if decide_union_closed(fam):
            uc_removals.append(T)
        else:
            nonuc_removals.append(T)
    print(f"n={nn}: power set minus ONE set T.  Union-closed for T in "
          f"{{∅(odd filter), singletons}} -> count {len(uc_removals)}")
    for T in uc_removals:
        # describe T
        Ttype = '∅(odd filter)' if T == 0 else \
                ('singleton' if bin(T).count('1') == 1 else str(T))
        fam = full - {T}
        print(f"   remove T={T} ({Ttype:>14}): UC={decide_union_closed(fam)}, "
              f"non-Boolean={not is_block_union(fam, nn)}, "
              f"max-density={max_density(fam, nn)[1]}")
    # for reference how many singletons T => these per n are exactly the n
    nsing = sum(1 for T in uc_removals if T != 0)
    print(f"   => {nsing} singleton-removals + 1 odd filter = {nsing+1} UC "
          f"families of size 2^{nn}-1")

print()
print("=" * 78)
print("CONFIRM: n remove-singleton families are distinct, non-Boolean, same bound")
print("=" * 78)
for nn in (2, 3, 4):
    full = set(range(1 << nn))
    bound = Fraction(2**(nn - 1), 2**nn - 1)
    for x in range(nn):
        T = 1 << x
        fam = full - {T}
        assert decide_union_closed(fam)
        assert not is_block_union(fam, nn)
        cd, d = max_density(fam, nn)
        print(f"   n={nn} remove {{x}}: UC, non-Boolean, max-density={d} "
              f"(== bound {bound}: {d == bound})")
