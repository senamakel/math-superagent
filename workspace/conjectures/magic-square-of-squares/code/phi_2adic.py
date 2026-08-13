#!/usr/bin/env python3
"""Probe the 2-adic (mod 2^k) structure of Phi = {4mn(m^2-n^2)/(m^2+n^2)^2}.

Question: can an additive triple q1, q2, q1+q2 all lie in Phi?  Since every
q in Phi is a rational with v2(q) >= 3 (q == 0 mod 8), the obvious mod-8
obstruction vanishes.  We dig further:

  [1] the exact 2-adic valuation v2(q) distribution over Phi(M), split by
      parity class of (m,n);
  [2] the residue classes of q mod 64 as rationals (2-adically);
  [3] whether the SET of residues is closed under the additive relation
      q1+q2 -> q3  at each 2-adic precision (i.e. is there a modular
      obstruction beyond enumeration?).
"""
from fractions import Fraction
from math import gcd
from collections import Counter, defaultdict
import sys

def v2(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v

def phi_pairs(M):
    """distinct reduced (num,den) for f(m,n), m>n>=1, m<=M."""
    out = set()
    for m in range(2, M + 1):
        m2 = m * m
        for n in range(1, m):
            num = 4 * m * n * (m2 - n * n)
            den = (m2 + n * n) ** 2
            g = gcd(num, den)
            out.add((num // g, den // g))
    return out

def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 120
    pairs = phi_pairs(M)
    # rational value = num/den; as 2-adic, v2(q)=v2(num)-v2(den)
    vdist = Counter()
    byparity = defaultdict(Counter)
    # residue of q mod 2^k: the odd part of den times num (since den has the
    # only odd part after cancellation we work with q = num/den, den odd part)
    # q mod 2^k as a 2-adic value = num * inverse(den) mod 2^k, but num may
    # carry 2-powers; easiest: value minus v2 -> odd part residues.
    oddres = defaultdict(Counter)   # oddpart of den -> counter of oddpart of num mod 64
    for (num, den) in pairs:
        qv = v2(num) - v2(den)
        vdist[qv] += 1
        o_num = num >> v2(num)
        o_den = den >> v2(den)
        byparity['both_odd' if (num % 2 and den % 2) else 'even' ][qv] += 1
        # tag by parity of m,n rather than num: can't recover here; approximate
    print(f"[1] Phi({M}): |Phi| = {len(pairs)}")
    print("    v2(q) distribution:", dict(sorted(vdist.items())))
    # recompute with explicit parity tracking
    vpar = Counter()
    vpar_bo = Counter()   # both (m,n) odd
    vpar_eo = Counter()   # mixed
    for m in range(2, M+1):
        m2=m*m
        for n in range(1,m):
            num = 4*m*n*(m2-n*n); den=(m2+n*n)**2
            g=gcd(num,den); num//=g; den//=g
            qv = v2(num)-v2(den)
            if (m+n)%2==0:  # both odd (primitive -> both odd)
                vpar_bo[qv]+=1
            else:
                vpar_eo[qv]+=1
    print("    v2 distribution, both (m,n) odd:", dict(sorted(vpar_bo.items())))
    print("    v2 distribution, mixed parity   :", dict(sorted(vpar_eo.items())))

    # [3] modular additive closure: reduce each q to a residue r in Z/2^k
    # via 2-adic valuation: q = r * 2^kv with r odd.  Work mod 2^K on the
    # "odd part" after stripping v2.  For an additive triple q1+q2=q3 all in
    # Phi, compare v2(q3) with min(v2(q1),v2(q2)).
    # If v2(q1) != v2(q2), then v2(q1+q2) = min.  So to have all three with
    # v2>=3 and the sum in Phi, we'd need v2(q1+q2) = min(v2(q1),v2(q2)) >= 3
    # (always true) OR the valuations equal with odd-parts summing to the
    # odd part of q3.  So check: is there obstruction that for ANY q1,q2 with
    # equal v2=v, the odd parts never combine to an odd part present in Phi
    # at valuation v with the right odd part?  That would be a set-level
    # proof IF the odd parts in Phi at a given valuation form a sum-free
    # set mod 2^K.  Below we check, per valuation v, the set of odd parts
    # present, and test whether it is additively closed.
    K = 12
    byv = defaultdict(set)  # v -> set of odd parts mod 2^K
    for m in range(2, M+1):
        m2=m*m
        for n in range(1,m):
            num=4*m*n*(m2-n*n); den=(m2+n*n)**2
            g=gcd(num,den); num//=g; den//=g
            if num==0: continue
            qv = v2(num)-v2(den)
            # odd part of the rational = odd(num) * odd(den)^{-1} mod 2^K
            o_num = num >> v2(num)
            o_den = den >> v2(den)   # den odd (denominator of reduced frac is odd? not nec. but for v>= it is)
            r = (o_num * pow(o_den & ((1<<K)-1), -1, 1<<K)) & ((1<<K)-1)
            byv[qv].add(r)
    print(f"[2] per-valuation odd-part residue sets mod 2^{K}:")
    for v in sorted(byv):
        S = byv[v]
        # check additive closure within equal-valuation: do two odd parts in S
        # ever sum (weighted) to an odd part in S (with carry into v+1 ignored)?
        closed = True
        found = None
        for r1 in S:
            for r2 in S:
                r3 = (r1 + r2) & ((1<<K)-1)
                if r3 & 1 and r3 in S:
                    closed = False
                    found = (r1, r2, r3)
                    break
            if found: break
        print(f"    v={v}: |S|={len(S)}, additively-closed-within-valuation: {closed}"
              + (f"  (witness {found})" if found else ""))

if __name__ == "__main__":
    main()
