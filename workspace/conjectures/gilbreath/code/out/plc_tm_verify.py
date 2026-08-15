"""Independent verification of nu2 for Thue-Morse 2-then-odds.
Two routes: (A) incremental_diagonals + cycle_and_nu2;
(B) direct full row-triangle rows_generator, count {0,2} suffix of right diag.
"""
from lib.gilbreath import rows_generator
from lib.rightdiag import incremental_diagonals, cycle_and_nu2
def popcount(j): return bin(j).count("1")

def build_q(h, n_terms):
    q=[2,3]
    for j in range(n_terms):
        q.append(q[-1]+(2 if h[j] else 4))
    return q

def nu2_direct(q, n):
    # right diagonal of triangle from q[:n+1]: A_k[n-k]
    rows=list(rows_generator(q[:n+1], n))
    diag=[rows[k][n-k] for k in range(n+1)]
    _,nu2=cycle_and_nu2(diag)
    return diag,nu2

N=64
h=[popcount(j)&1 for j in range(N+2)]
q=build_q(h, N+2)
y=incremental_diagonals(q)
for n in (8,16,32,64):
    # route A
    dd=list(y)  # already consumed through? rebuild each time cleaner
for n in (8,16,32,64):
    # rebuild incremental fresh
    y=incremental_diagonals(q)
    dd=None
    for _ in range(n+1):
        dd=next(y)
    _,nuA=cycle_and_nu2(dd)
    diag,nuB=nu2_direct(q,n)
    # check diag == dd
    match = (diag==dd)
    print("n=%4d nu2A=%d nu2B=%d diag_match=%s" % (n, nuA, nuB, match))
    # also print the {0,2} suffix window
    body=dd[:-1]; i=len(body)
    while i>2 and body[i-1] in (0,2): i-=1
    print("      suffix window diag[%d:-1]=%s" % (i, dd[i:-1]))
