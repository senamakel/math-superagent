# boundary-mobius-coboundary

**Status: refuted**  (killed-by: `boundary-mobius-identity-false`, this file)

## The approach

Write `h = ∂r` over F2, `h[j] = r[j+1] ⊕ r[j]`, with `r` the mod-4 residue string
(`r[j] = q_j mod 4`, valid since all primes ≥ 3 are odd and residue-switch is
exactly `h`). Then the approach conjectures a shuffle identity

    T(n,d) = b_d ⊕ b_{d-1},

where `b_e = XOR_{o⊆e} r[n-1-e+o]` are the submask-XOR ("Möbius") coefficients
of the reversed `r`-window. If true it would give

    wt(Φ_n h) = #{ d in [2,n-1] : b_d ≠ b_{d-1} } = variation of the Möbius profile,

making the fold weight a one-point function of the residue string (Shiu-accessible,
not the open adjacent-pair switch density).

## Why it dies — the load-bearing identity is FALSE

The step `h = ∂r` itself is correct (residue-switch ⟺ `h`), but the shuffle
"differentiation commutes with the submask-zeta transform" is not. The zeta/Möbius
transform runs over the **subset lattice** of `d`, while the shift/difference `1+σ`
runs over the **linear chain** of the window; they do not conjugate.

Explicit counterexample (exact F2 arithmetic, hand-checked and consistent with the
script `code/gfold/boundary_mobius_identity.py` — which has **no capture file** and
is out-of-bounds for `d=n-1`, i.e. it never ran cleanly, so the identity was never
verified here).

n=4, d=2, submasks of 2 = {2,0}. Let `r = (0,0,0,0,1)`, so `h = (0,0,0,1)`:

    T(4,2) = h[4-1-2+2] ⊕ h[4-1-2+0] = h[3] ⊕ h[1] = 1 ⊕ 0 = 1
    b_2     = r[3] ⊕ r[1]            = 0 ⊕ 0     = 0
    b_1     = r[3] ⊕ r[2]            = 0 ⊕ 0     = 0
    b_2 ⊕ b_1 = 0  ≠  1 = T(4,2)

The identity holds only under a boundary condition on the extra bit `r[n-1]`
(here `r[4]=r[3]`), the very bit `h` does not determine — so the approach's
promise that the boundary "kills" the defect is backwards: the defect is *at*
the boundary and is not removable.

## Why "variation of the Möbius profile" cannot be the weight

Even setting the false shuffle aside, the weight-reduction "fold weight = number
of sign changes in the Möbius profile" is the same Möbius/ANF/Reed-Muller reading
already refuted as inert relabeling under `anf-mobius-reed-muller` and
`newton-series-degree-dichotomy` (the ANF basis and the numeric shift basis do not
interact; the fold cell is the F2-zeta transform, an involution on the cube, while
`1+σ` acts on the chain). The weight of a zeta-transformed sliding window is not a
variation count of its potential.

## The arithmetic-input question is settled independently

Even if the shuffle were true, the proposed input — one-point mod-4 balance /
bounded discrepancy of the residue string — is strictly weaker than positive
switch density, and the run already knows that *no* one-point input can force the
g=0 (adjacent-index) stratum. That is exactly the parity barrier named in
`mod2m-lift-onepoint` and `rubinstein-sarnak-prime-race-ergodic` (refuted): a
one-point residue distribution does not determine adjacent-pair switch frequency,
and ABGS §9 state switch density is unknown and "cannot be treated using
L-functions". So the one-point input, even granted, is the known dead end.

## Precedent (literature, focused search)

- The false shuffle is **not** a known identity in the F2 Möbius / Walsh-Hadamard
  / Reed-Muller / binomial-sum literature, because it is not true. What the
  literature does state: Boolean partial/directional derivatives lower algebraic
  degree and compose commutatively (Davio "Boolean differential calculus", IEEE
  T-C 1973, doi 10.1109/T-C.1973.223729), but these act on the *cube subset*
  structure, not the numeric chain shift; the ANF/zeta transform is self-inverse
  on the cube (Bakoev, "Fast bitwise implementation of the ANF transform",
  Serdica J. Comput. 11 (2017) 45–57). No source conjugates the chain shift to a
  pointwise bit multiplier through the zeta transform — because the two structures
  are incompatible.
- No prior work on Gilbreath/SUPPLY writes the residue string as a potential of
  the gap-parity string and identifies image weight with the variation of the
  Möbius transform of residue windows. The Gilbreath literature attacks the
  leading diagonal directly: Odlyzko 1993 (Math. Comp., doi 10.1090/s0025-5718-
  1993-1182247-7) verified to 10^13; Plouffe 2025 (arXiv:2510.06688) to 10^14;
  Chase 2023 random analogue (Math. Ann., doi 10.1007/s00208-023-02579-w);
  Chase–Hunter–Tao 2026 (arXiv:2607.08712) Cramér random model + deterministic
  inverse theorem whose obstructions are **long zero blocks / shallow {0,λ}
  blocks** — exactly the long all-zero runs that Shiu 2000 injects and that the
  one-point input cannot control (closed doors 2 and the `h`-family). Agama 2021
  (RG) frames Gilbreath as a boundary "circuit trace" but does not touch residue
  Möbius inversion.

## Verdict

**Refuted.** The single load-bearing step is a false identity, falsified by a
4-term boundary counterexample; and even granting it, the arithmetic input it
would need is the known one-point dead end. Confirmed as the fourth independent
route into the same family as `anf-mobius-reed-muller` and
`newton-series-degree-dichotomy`, all dead on the basis mismatch between the
ANF/zeta (subset-lattice) basis and the chain shift `1+σ`.

Searched: the named shuffle ("submask-zeta conjugates shift"), the ANF/RM/zeta
commutation, and Gilbreath-by-Möbius-of-residue-windows, across the F2 Möbius /
Reed-Muller / Walsh literature and the Gilbreath attack literature. Not a search
for an exhaustive bibliography; two focused angles as requested.
