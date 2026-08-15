#!/usr/bin/env python3
"""Extract the sequences the investigation cares about into TSV for the
analyze_sequence / find_linear_recurrence tools:
  - b_k block profile (first 40 from witnesses.json)
  - nu2(n) first 100 from nu2_dense.txt
  - fluctuation dev(n) = 2*nu2(n)-n, first 200
  - inter-giant gaps at 1e9: [22,8,4,26,2,14,2,14,4,4,12,15,13,64]
"""
block = [2,7,13,13,24,23,22,21,24,58,97,96,97,96,173,175,175,175,175,290,
         289,288,739,873,872,871,872,871,870,869,868,867,866,865,2179,2178,
         2177,2176,2770,2769]
print("BLOCK_PROFILE")
print(",".join(map(str,block)))

nu2 = []
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        p=line.split()
        if len(p)==2: nu2.append(int(p[1]))
print("NU2_FIRST_100")
print(",".join(map(str,nu2[:100])))
dev = [2*nu2[n-1]-n for n in range(1,201)]
print("DEV_2NU2_MINUS_N_FIRST_200")
print(",".join(map(str,dev)))
print("GIANT_GAPS_1E9")
print("22,8,4,26,2,14,2,14,4,4,12,15,13,64")
print("W_FIRST_100")  # weights of mod4-switch window hbits[2..n-1]
P = __import__("code.lib.gilbreath", fromlist=["primes_up_to"]).primes_up_to(1_000_000)
hbits=[((P[i+1]-P[i])//2)%2 for i in range(len(P)-1)]
pref=[0]*(len(hbits)+1)
for i,bw in enumerate(hbits): pref[i+1]=pref[i]+bw
print(",".join(str(pref[n]-pref[2]) for n in range(2,102)))
