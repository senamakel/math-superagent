#!/usr/bin/env python3
"""Extract the elementwise closed form of the Mersenne half-constant array R_k.
Values observed: R_k[r] in {1} u {2^j} u {2^{k-2}-1}.
Test candidate: R_k[r] = 2^{a(r)} except the special value 2^{k-2}-1.
Determine a(r) precisely from binary pattern of r (0 < r < P).
"""
K = 5
P = 2 ** K - 1
R = [1, 15, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 8, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1]
print("r   bin(r)      val    log2   v2(r+1)  v2(r)   exp_cand")
for r in range(P):
    val = R[r]
    if val == 15:        # the special Mersenne-1 value for k=5
        tag = "SPECIAL(2^(k-2)-1)"
    else:
        tag = "pow2 exp=%d" % (val.bit_length() - 1)
    v2r1 = (r + 1) & -(r + 1)
    print("%2d  %6s  %4d  %3s    %2d     %2d    %s" %
          (r, bin(r)[2:], val, val.bit_length()-1, v2r1, (r & -r), tag))

# candidate: exp = k-2 - (number of trailing ...)?  Let's tabulate log2 val vs r
print("\nlog2(val) as fn of r:")
print([R[r].bit_length()-1 for r in range(P)])
