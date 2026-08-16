"""Verify the PQ<->SRG parameter map from Mohammadian-Tayfeh-Rezaie arXiv:1303.0473.

A diamond-free SRG(1+s(t+1)+s^2 t(t+1)/mu, s(t+1), s-1, mu) is the collinearity
graph of a PQ(s,t,mu). For lambda=1, s-1=1 so s=2; s(t+1)=k.

Check for the lambda=1 members of the srg(v,k,1,2) family: which (s,t,mu) do
they give, and does the formula reproduce v?
"""
import itertools

def params_from(s, t, mu):
    v = 1 + s*(t+1) + s*s*t*(t+1)/mu
    k = s*(t+1)
    lam = s-1
    return v, k, lam, mu

family = [  # (v,k,lam,mu) from integrality-five-members
    (9,4,1,2),(99,14,1,2),(243,22,1,2),(6273,112,1,2),(494019,994,1,2)
]

print("For each (v,k,1,2), find (s,t,mu) with s-1=1 (s=2), s(t+1)=k, and v matches:")
for (v,k,lam,mu) in family:
    s = lam+1  # 2
    found = []
    for t in range(1, 5000):
        if s*(t+1) != k:
            continue
        # need v = 1+s(t+1)+s^2 t(t+1)/mu  =>  mu = s^2 t(t+1)/(v-1-s(t+1))
        denom = v - 1 - s*(t+1)
        if denom <= 0:
            continue
        if (s*s*t*(t+1)) % denom != 0:
            continue
        mu = (s*s*t*(t+1))//denom
        if mu == 2:
            vv,kk,ll,mm = params_from(s,t,mu)
            found.append((s,t,mu,vv,kk,ll,mm))
    print(f"  srg({v},{k},1,2): s={s}, candidates {found}")

# Also check the BvLS neighbourhood: lambda=1 diamond-free requires lambda+1 | k
print("\nDiamond-free condition: lambda+1 | k for each member")
for (v,k,lam,mu) in family:
    print(f"  ({v},{k},{lam},{mu}): lambda+1={lam+1} | k={k} -> {k % (lam+1)==0}")
