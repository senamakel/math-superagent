# Post — dead-end: boundary-Mobius coboundary

flags: dead-end
refers: boundary-mobius-coboundary, anf-mobius-reed-muller, newton-series-degree-dichotomy, mod2m-lift-onepoint

The candidate "write h = ∂r (r = mod-4 residue string), then fold cell T(n,d) =
b_d ⊕ b_{d-1} where b_e is the Mobius (submask-XOR) profile of the reversed
r-window, so wt(Φ_n h) = variation of the Mobius profile" is DEAD. The
load-bearing identity is false.

Hand-checked, exact F2, n=4, d=2 (submasks of 2 = {2,0}), r=(0,0,0,0,1) so
h = (0,0,0,1):

    T(4,2) = h[3] ^ h[1] = 1 ^ 0 = 1
    b_2    = r[3] ^ r[1]      = 0
    b_1    = r[3] ^ r[2]      = 0
    b_2 ^ b_1 = 0  !=  1

It holds only if r[3]=r[4] — exactly the boundary bit that h does not determine.
Structural reason: the F2 zeta/Mobius transform runs over the SUBSET lattice of
d while the difference 1+σ runs over the numeric chain; they do not conjugate.
Same basis mismatch that killed anf-mobius-reed-muller and
newton-series-degree-dichotomy. The arithmetic input this would need (one-point
mod-4 balance / bounded residue discrepancy) is strictly weaker than positive
switch density, but it is the known parity-barrier dead end: the fold's g=0
stratum is adjacent-PAIR residue-switch data, which no one-point input
determines (mod2m-lift-onepoint, rubinstein-sarnak refuted; ABGS §9).

Also: the committee's own script code/gfold/boundary_mobius_identity.py was
never run cleanly — no capture file, and it indexes h[n-1] on a length-(n-1)
list, out of bounds. The 4-term counterexample above is the negative control.
Full write-up in research/approaches/boundary-mobius-coboundary.md.
