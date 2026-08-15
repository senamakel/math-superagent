#!/usr/bin/env python3
"""Find the elementwise closed form of the Mersenne half-constant array
R_k[r] = c_r/2 for the tail-1 word.  Test candidates based on binary patterns.
Established: ones at r = 2^k - 2^j for j=1..k and r=0.
Test candidate: value = 2^{v} where v depends on binary form.
Also confirm sum c_r = 3^k - 3 and min c_r = 2.
"""
Rs = {
 3: [1, 3, 2, 2, 1, 2, 1],
 4: [1, 7, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
 5: [1, 15, 8, 8, 4, 8, 4, 4, 2, 8, 4, 4, 2, 4, 2, 2, 1, 8, 4, 4, 2, 4, 2, 2, 1, 4, 2, 2, 1, 2, 1],
}

for k, R in Rs.items():
    P = 2 ** k - 1
    print(f"--- k={k} P={P} ---")
    # Try candidate: value(r) = 2^{v_2( (P+1) - (r+1) )}? i.e. v of (P-r)
    # value(r) = 2^{a} where a = min exponent with r in some set
    # print per r: r (bin), value, value.bit_length()-1, v2(r+1), v2(P-r)
    for r, val in enumerate(R):
        v2_r1 = (r + 1) & -(r + 1)
        v2_Pr = (P - r) & -(P - r)
        exp = val.bit_length() - 1
        print(f"  r={r:3d} bin={bin(r)[2:]:>6s} val={val:3d} exp={exp}")
