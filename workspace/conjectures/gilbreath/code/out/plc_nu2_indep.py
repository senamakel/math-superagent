"""Fully independent recomputation of nu2(N) (2s in maximal {0,2} right-diag
suffix) for Thue-Morse switch, plus a prime-family sanity check.
Method: build the row-triangle one row at a time (memory O(w)), extract the
right diagonal A_k[n-k], then count 2s in the maximal {0,2} suffix using a
hand-rolled scan (not cycle_and_nu2)."""
from lib.gilbreath import primes_up_to

def popcount(j): return bin(j).count("1")

def diagonal_from_seq(seq, n):
    # seq[0]=q1..seq[n]=q_{n+1}; rows built to depth n; right diag A_k[n-k]
    row = list(seq[:1])          # A_0
    # we need depth n; build rows iteratively
    prev = list(seq[:n+1])       # A_0 = q_1..q_{n+1}
    diag_row0 = prev[n]          # A_0[n] i.e. first index of right diag
    cur = None
    diag = [prev[n]]
    for k in range(1, n+1):
        cur = [abs(prev[i]-prev[i+1]) for i in range(len(prev)-1)]
        diag.append(cur[n-k])
        prev = cur
    return diag

def nu2_scan(diag):
    """hand-rolled: maximal {0,2} suffix of diag[:-1], count 2s."""
    body = diag[:-1]
    i = len(body)
    while i > 0 and body[i-1] in (0,2):
        i -= 1
    return body[i:].count(2), i

# ---- Thue-Morse to n=512 ----
N = 512
h = [popcount(j)&1 for j in range(N+2)]
q = [2,3]
for j in range(N+2):
    q.append(q[-1]+(2 if h[j] else 4))
diag = diagonal_from_seq(q, N)
n2, tau = nu2_scan(diag)
print("Thue-Morse n=512: nu2=%d tau=%d  powers-of-two-count=10" % (n2, tau))
print("  => %s" % ("witness-10 REPRODUCED" if n2==10 else "witness-10 NOT reproduced"))

# small-n table of nu2 vs power-of-two count
print("\nn -> nu2 (this scan) ; #powers_of_two<=n :")
for k in range(0,10):
    m=1<<k
    if m<=N:
        d = diagonal_from_seq(q, m)
        n2m,_ = nu2_scan(d)
        print("  n=%-5d nu2=%d  #powers_of_two=%d" % (m, n2m, k+1))

# ---- Prime family sanity: nu2/n and nu2/w should be ~0.5-ish at some n ----
print("\nPrime-family sanity (sieve small, n in {100,200,500}):")
P = primes_up_to(30000)
def prime_h(j):
    return ((P[j+2]-P[j+1])//2) & 1
for n in (100,200,500):
    hh=[prime_h(j) for j in range(N+2)]
    qq=[2,3]
    for j in range(N+2):
        qq.append(qq[-1]+(2 if hh[j] else 4))
    dd=diagonal_from_seq(qq, n)
    nn2,_=nu2_scan(dd)
    ww=sum(hh[:n])
    print("  n=%-5d nu2=%d nu2/n=%.3f nu2/w=%.3f w=%d" % (n,nn2,nn2/n,(nn2/ww if ww else float('nan')),ww))
