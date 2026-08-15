import sys
sys.path.insert(0, "/workspace")
from lib.gilbreath import primes_up_to

# e(n) = switch-majority walk on consecutive-prime mod-4 residues
# u_k = +1 if p_k = 1 mod 4, -1 if p_k = 3 mod 4 (for k>=2 relevant)
# e(n) = -sum_{k=3}^{n} u_k u_{k+1}   (step +1 on switch, -1 on stay)
# Choose a sieve giving ~200 primes each p_k and p_{k+1}.
LIM = 2000
P = primes_up_to(LIM)
# map residue
res = [p % 4 for p in P]
u = [0]*len(P)
for i,p in enumerate(P):
    if p==2: u[i]=0
    elif p%4==1: u[i]=1
    elif p%4==3: u[i]=-1
    else: u[i]=0
# index of p=2 is i0
i0 = P.index(2)
# e(n) defined over k=2.. (p_2=3 onward)
# build e over primes from p_2=3
start = i0+1  # p_2
vals_u = u[start:]  # u for p_2, p_3, ...
# e over n where n counts pairs (p_k,p_{k+1}) hmm; use the k-indexing: e(n)=-sum_{k=3}^{n} u_k u_{k+1}
# Here val index j corresponds to p_{j+2}? Let's index from p_2=3.
# u_k = vals_u[k-2]
e_terms = []
cursum = 0
# sum over k=3.., i.e. j-th term uses vals_u[(k-2)] and vals_u[(k-1)]
# iterate k from 3 upward
for k in range(3, len(vals_u)+1):
    uk = vals_u[k-2]
    uk1 = vals_u[k-1]
    cursum -= uk*uk1
    e_terms.append(cursum)
# e(n) for n=2 => 0; n=k => cursum
first_e = [0]  # n=2 placeholder not needed
print("e(n) first 60 (n=3..62):")
print(e_terms[:60])

# also nu2 q: number of 2s in maximal {0,2} suffix. Skip; just e.
