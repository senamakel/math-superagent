# Scratch: does the run-telescope structure lift to symmetric differences?

Hand-check (no floats, no code) before trusting the hypothesis.

↓d = {o ∈ [0,d] : o bitwise-submask of d}.

**Claim under test:** every maximal run of ↓d △ ↓d' has power-of-2 length.

**Witness:** d = 2 (binary 10), d' = 7 (binary 111).
- ↓2 = {0, 2}
- ↓7 = {0,1,2,3,4,5,6,7}
- ↓2 △ ↓7 = {1,3,4,5,6,7}
- Sorted: 1, 3,4,5,6,7 → maximal runs {1} (length 1) and [3,7] (length **5**).

5 is not a power of 2. **The claim is FALSE.**

**Corrected claim (true, by chain cancellation):** for ANY interval [u,v] of
consecutive integers, the XOR telescope holds:

  ⊕_{o=u}^{v} h[j+o] = [r_{j+u} ≠ r_{j+v+1}]   (two-valued boundary r, h = [r_{k+1}≠r_k])

The power-of-2 run length was special only to the SINGLE-down-set decomposition
(where runs end at aligned block boundaries); it does NOT lift to the symmetric
difference, whose runs have arbitrary lengths. The telescoping identity itself
is interval-generic and survives.

**Consequence for the cross-moment:** with χ the nontrivial char mod 4 and
s_j = χ(q_j), (−1)^{h[j]} = s_j s_{j+1}, so

  ε_d ε_{d'} = (−1)^{⊕_{o∈↓d△↓d'} h[...]} = ∏_{R∈runs(↓d△↓d')} s_{pos+u_R} s_{pos+v_R+1}

a product of two-point character values at separations = (run length)+1, which
may be ARBITRARY integers, not just powers of 2.
