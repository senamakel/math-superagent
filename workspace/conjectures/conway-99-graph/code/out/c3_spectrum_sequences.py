"""Triangle-graph C3 predicted spectra across the srg(v,k,1,2) family.

Phillips eq 4.3: C3(Gamma) has spectrum
  d^1,  (k/2 + r - 3)^m_r,  (k/2 + s - 3)^m_s,  (-3)^(nT - v)
where d = 3(k/2 - 1), r,s the graph eigenvalues (r=u, s=-(u+1)),
m_r, m_s their multiplicities, nT = vk/6.

This computes the family-wide sequences of the C3 eigenvalues and their
multiplicities (the "-3 count" nT-v = v(k-6)/6 and the eigenvalues
rt = (u-1)(u+4)/2, st = (u-3)(u+2)/2) that prior pattern-finder rounds
never tabulated. Exact integer arithmetic only.
"""
import math

def fam(u):
    k = u*u + u + 2
    v = 1 + k*k//2
    return k, v

def mult_r(u, k, v):
    # multiplicity of eigenvalue r in the graph (f(r) from older report)
    a = 2*u + 1
    r = u
    # m_r = (v-1)/2 - ((v-1)*? ... compute directly via standard SRG mult formula
    # multiplicity of eigenvalue r: f = [ (v-1) + (2k + (v-1)(lam-mu))/d ]/2 with d = r-s
    # For lam=1, mu=2: 2k + (v-1)(-1) = 2k - (v-1)
    d = r - (-(u+1))   # r - s = 2u+1 = a
    m_r = (v - 1 + (2*k - (v-1)) // d) // 2
    return m_r

results = []
for u in (1,3,4,10,31):
    k, v = fam(u)
    nT = v*k//6
    r = u; s = -(u+1)
    d_g = 3*(k//2 - 1)          # C3 degree (eigenvalue, mult 1)
    rt = k//2 + r - 3
    st = k//2 + s - 3
    mr = mult_r(u,k,v)
    ms = (v - 1 - mr) // 1      # total - 1 - mr ; check
    ms = (v - 1 - mr)           # remaining multiplicities? Actually m_s = (v-1)-m_r
    nminus3 = nT - v            # mult of -3 in C3
    results.append((u,k,v,nT,d_g,rt,mr,st,ms,nminus3))
    print(f"u={u:>2} k={k:>3} v={v:>6} nT={nT:>8} d={d_g:>3}  "
          f"rt={rt:>3}^{mr:>6}  st={st:>3}^{ms:>6}  -3^{nminus3:>8}")

print()
print("rt (C3 eigenvalue from r) family:", [x[5] for x in results])
print("st (C3 eigenvalue from s) family:", [x[7] for x in results])
print("-3 multiplicity nT-v family:      ", [x[9] for x in results])
