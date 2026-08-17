"""Characterise every minimizer of max-density over NON-Boolean union-closed
families for n=2,3,4, and confirm the singleton-removal families' structure.

Claim being tested: min max-density = 2^{n-1}/(2^n-1), attained UNIQUELY by
the odd filter F = 2^[n]\\{∅}.  We found n+1 minimizers instead.  This prints
each in a human-readable form and labels it odd-filter vs singleton-removal,
and confirms each is genuinely non-Boolean.
"""
from fractions import Fraction
from lib.uc import decide_union_closed, abundance


def is_block_union(F, n):
    nonempty = [s for s in F if s != 0]
    if not nonempty:
        return False
    atoms = []
    for s in nonempty:
        if not any(t != s and (t & s) == t for t in nonempty):
            atoms.append(s)
    for i in range(len(atoms)):
        for j in range(i + 1, len(atoms)):
            if atoms[i] & atoms[j]:
                return False
    ua = set()
    for J in range(1 << len(atoms)):
        u = 0
        for i in range(len(atoms)):
            if (J >> i) & 1:
                u |= atoms[i]
        ua.add(u)
    return set(F) == ua


def humanset(mask, n):
    return "{" + ",".join(str(i) for i in range(n) if (mask >> i) & 1) + "}"


def all_uc_families(n):
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
    counts = abundance(F, n)
    return Fraction(max(counts), len(F))


print("Minimizers (families attaining min max-density over non-Boolean UC):")
for nn in (2, 3, 4):
    bound = Fraction(2**(nn - 1), 2**nn - 1)
    minimizers = [F for F in all_uc_families(nn)
                  if not is_block_union(F, nn) and max_density(F, nn) == bound]
    uniq = sorted(set(tuple(sorted(F)) for F in minimizers))
    print(f"\nn={nn}: {len(uniq)} minimizers, min max-density = {bound} = "
          f"{float(bound):.6f}")
    full = set(range(1 << nn))
    for u in uniq:
        fset = set(u)
        removed = full - fset
        r = list(removed)[0]
        # label
        if removed == {0}:
            kind = "ODD FILTER 2^[n]\\{∅}"
        elif bin(r).count('1') == 1:
            x = r.bit_length() - 1
            kind = f"power set minus singleton {{{x}}}"
        else:
            kind = "other ???"
        nb = (not is_block_union(fset, nn))
        print(f"   remove {humanset(r, nn)}  ->  {kind}   "
              f"m={len(fset)}, non-Boolean={nb}")
