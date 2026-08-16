# Index — code/weights

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `linear_supply_by_weight.py` | Characterises which binary h of length n have linear supply (nu2(n)=wt(Phi_n h)>=c*n) as a function of Hamming weight w. Part0 reproduces the e_{n-2} mechanism (nu2=count of odd d in [2,n-1]) and the n=8 witness (e_6:(S,nu2)=(0,3), e_5=(-2,4)); Part1 exhaustively enumerates all 2^n strings for n in {6,8,10,12,14,16} reporting per-(n,w) count/mean/fraction of nu2/n>=0.25/0.40/0.45; Part2 samples 300 random strings of exact weight {1,2,3,4,5,8,16,32,n//2,n} for n in {32,64,128}; Part3 states the min weight at which linear supply is typical (mean>=0.40 and frac>=0.40>=0.5); all-ones string is a negative control (kernel, nu2/n=0). Uses canonical oracle lib.supply_fold.s_sos (returns (S,nu2)) cross-checked on a random 5% sample against s_direct — all agree. Captured to code/out/linear_supply_by_weight.txt. Verified: n=8 witness reproduced exactly, mechanism confirmed n=3..40. |
