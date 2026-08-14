import os

# PROVEN structural fact:  f_d(k*10^m + x) = f_d(x) + k*m*10^(m-1)
#   for 0<=k<=d-1, 0<=x<10^m   (leading digit k never equals d when k<=d-1).
# For m=10: f_d(k*10^10+x)-f_d(x)=k*10^10, so fixed-point sets are exactly
# translation-invariant: block k = {k*10^10+x : x block-0 solution}, k=0..d-1.
# Consequence (independent route to each s(d)):
#   s(d) = d*S0 + (d-1)d/2 * 10^10 * N0
# where S0 = sum of block-0 solutions, N0 = number of block-0 solutions.
print("Independent block-decomposition route to s(d):")
print(f"{'d':>2} {'N0':>4} {'S0':>14} {'s(d)_decomp':>16} {'s(d)_solver':>16} {'match':>5}")
tot_decomp = 0
reported = {1:22786974071,2:73737982962,3:372647999625,4:741999999540,
            5:100000000000,6:2434703999430,7:1876917059570,
            8:15312327487352,9:360000000000}
for d in range(1,10):
    sols=[int(x) for x in open(f"/workspace/code/out/solutions-d{d}.txt").read().split()]
    b0=[x for x in sols if x < 10**10]
    S0=sum(b0); N0=len(b0)
    decomp = d*S0 + (d-1)*d//2 * 10**10 * N0
    tot_decomp += decomp
    match = (decomp == reported[d])
    print(f"{d:>2} {N0:>4} {S0:>14} {decomp:>16} {reported[d]:>16} {match!s:>5}")
print(f"\nTOTAL via decomposition = {tot_decomp}")
print(f"TOTAL via solver        = 21295121502550")
print("match:", tot_decomp == 21295121502550)
