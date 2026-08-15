import json
# Independently recompute e(n) ballot property and nu2, S_k regularity.
# Use blocks_depth1000 for b and s; reconstruct e-walk from prim(es).

# --- Part 1: e(n) ballot property over the primes, independent recompute ---
from lib.gilbreath import primes_up_to
LIM = 500000
P = primes_up_to(LIM)
res = [p % 4 for p in P]
# u only for p>2 (p=2 -> 0). index of p=2
i0 = P.index(2)
u = [0]*len(P)
for i,p in enumerate(P):
    u[i] = 1 if p%4==1 else (-1 if p%4==3 else 0)
uv = u[i0+1:]  # u for p_2=3 onward; uv[j] = u(p_{j+2})
# e(n) = -sum_{k=3}^{n} u_k u_{k+1}
e = []
s = 0
for k in range(3, len(uv)+1):
    uk = uv[k-2]; uk1 = uv[k-1]
    s += -uk*uk1
    e.append(s)
e_terms = [0,0]+e  # index n (n=0,1 placeholders zero; e(n) for n>=2)
# check e(2): for n=2 sum empty = 0
EMIN = min(e_terms[2:])
first_neg = next((n for n in range(2, len(e_terms)) if e_terms[n] < 0), None)
print("Part1: e(n) ballot — number of terms:", len(e_terms)-2)
print("  min e over n in [2, %d] = %d" % (len(e_terms)-1, EMIN))
print("  first n with e(n)<0:", first_neg)
print("  e first 30 (n=2..31):", e_terms[2:32])
print("  e final:", e_terms[-1])
