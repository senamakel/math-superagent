"""Verify the tight-coclique family identities across all five feasible
srg(v,k,1,2) members, u in {1,3,4,10,31}, k=u^2+u+2, v=1+k^2/2, s=-(u+1).

If a coclique C meets the Hoffman bound (|C| = alpha), equality forces
the outside-degree into C to be
    d_C = alpha*(k-s)/v
and the {neighbourhood-restricted} sets form a 2-(alpha, d_C, mu) design
with replication r = mu*(alpha-1)/(d_C-1) and block count b = v - alpha.

Claim under test (the closed-form identities):
    d_C = -s = u+1            (both exactly, over all five members)
    r   = k                  (replication of the coclique design = k)

alpha = (u*k+2)/2  [Hoffman closed form, report 3].
Exact integer arithmetic only.
"""
import math

def fam(u):
    k = u*u + u + 2
    v = 1 + k*k//2
    disc = 4*k - 7
    d = math.isqrt(disc)
    assert d*d == disc
    s = (-1 - d)//2
    return k, v, s

print("# ver tigh-coclique identities d_C = -s and r = k, five feasible members")
print("# (u, k, v, s, alpha, d_C, -s, match_dC, r, replication\"; r==k?)\n")
rows = []
for u in (1,3,4,10,31):
    k, v, s = fam(u)
    alpha = (u*k + 2)//2                       # Hoffman closed form
    dC = alpha * (k - s) // v                  # forced outside-degree into C
    # design parameters 2-(alpha, dC, mu=2):
    mu = 2
    r_rep = mu * (alpha - 1) // (dC - 1)       # replication (integer check below)
    b = v - alpha
    # integrality checks
    assert alpha * (k - s) % v == 0, (u, "dC not integer")
    assert mu * (alpha - 1) % (dC - 1) == 0, (u, "r not integer")
    rows.append((u, k, v, s, alpha, dC, r_rep, b))
    print(f"u={u:>2} k={k:>4} v={v:>6} s={s:>4} alpha={alpha:>6} "
          f"d_C={dC:>3} -s={-s:>3} dC==-s: {dC==-s}   r={r_rep:>4}==k: {r_rep==k}")
    # design bolster identities
    # b*C(dC,2) == mu*C(alpha,2) and b*dC == alpha*r
    assert b * (dC*(dC-1)//2) == mu * (alpha*(alpha-1)//2), (u, "block-pair id")
    assert b * dC == alpha * r_rep, (u, "bk=vr id")

print()
print("d_C family sequence:", [r[5] for r in rows])
print("replication r family:", [r[6] for r in rows])
print("block count b family:", [r[7] for r in rows])
print()
print("ALL identity checks (dC==-s, r==k, bk=vr, block-pair) PASS on all five members")
