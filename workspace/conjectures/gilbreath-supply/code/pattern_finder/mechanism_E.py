import math
from math import comb

# Test the analytical prediction: w* solves (1/n) sum_{d=2}^{n-1} P_d(w) = 0.40
# where P_d(w) = Pr[XOR of k=2^pc bits odd | weight w].
# Explore: what does P_d(w) behave like when w ~ n^E, small (w << n)?
# P_d(w) ~ 1 - exp(-2 * (w * k / n)) ... /2  in the linear regime?
# Actually P_d(w)=Pr[odd] with each of the k bits independently ~ (w/n): 
#   for a random weight-w string, each fixed bit is 1 with prob w/n (nearly independent)
#   => XOR odd prob = (1-(1-2w/n)^k)/2 ~ (1-e^{-2wk/n})/2
# mean = (1/n) sum_d (1-e^{-2 w 2^pc(d)/n})/2
# Let u = w/n. sum_d e^{-2 u 2^pc(d)}  ~ sum_p cnt(p) e^{-2 u 2^p}
# where cnt(p) ~ C(log n, p)... sparse: for small u, the exp terms with 2^p >> 1/u vanish.
# mean ~ (1/n)[ #{d: 2^{pc(d)} <= 1/u} /2 + ... ]
# If u ~ n^E/n = n^{E-1}, then 1/u ~ n^{1-E}. d with 2^{pc(d)} <= n^{1-E} => pc(d) <= (1-E) log_2 n.
# #{d<=n-1: pc(d)<=alpha log2 n} ~ n * P[Bin(log2 n,1/2) <= alpha log2 n] 
#   = n * P[Bin(m,1/2) <= alpha m], m=log2 n.
# For mean = 0.40 ~ 1/2 (1/n)*count_sat => count_sat ~ 0.8 n.
# P[Bin(m,1/2) <= alpha m] ~ 0.8-ish when alpha ~ 0.62+ (slightly above 1/2).
# alpha = 1-E ~ 0.62 => E ~ 0.38?  That's not 0.555.
# So pure sparse regime gives ~0.38-0.45, not 0.555. The measured E is higher; driven by 
# the exponential vs threshold counts, need the two-one/correlation terms. Let me just 
# numerically locate the exponent from the mean structure.

def P_approx(n, w, k):
    # continuous approx Pr[old of k bits | weight w, n]
    p=w/n
    return (1-(1-2*p)**k)/2

def mean_approx(n, w):
    tot=0.0
    for d in range(2,n):
        tot+=P_approx(n,w,1<<d.bit_count())
    return tot/n

def find_E_mean(n):
    # solve mean_approx(n, n^E)=0.4 for E
    lo,hi=0.0,1.0
    for _ in range(60):
        mid=(lo+hi)/2
        m=mean_approx(n, int(n**mid))
        if m<0.4: lo=mid
        else: hi=mid
    return (lo+hi)/2

for n in [2**10,2**12,2**14,2**16,2**18]:
    print(f"n={n}: approx-E solving mean=0.4 = {find_E_mean(n):.4f}")
