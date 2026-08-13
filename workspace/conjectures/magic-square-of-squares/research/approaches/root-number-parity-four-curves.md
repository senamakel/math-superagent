# Approach: Root numbers and parity of the four linked congruent-number curves

```approach
idea: Each of the four three-term APs of squares through the centre — with
common differences d = u, v, u+v, u−v — is equivalent to the congruent-number
curve E_d: y² = x³ − d²x having a rational point in 2E_d(Q), i.e., the
doubling of some Q-point. The four curves E_u, E_v, E_{u+v}, E_{u−v} are not
independent: they share the same centre e² (hence the same twist family) and
their d-values satisfy additive relations. Their root numbers w(E_d) — the
sign of the functional equation of the L-function L(E_d, s) — are determined
by the residue class of d modulo some modulus (as E_d has CM by Z[i], its root
number is computable via the associated Hecke character). The existence of a
point in 2E_d(Q) forces the Mordell–Weil rank rk E_d(Q) ≥ 1. By the parity
conjecture (BSD conjecture: ord_{s=1} L(E_d, s) ≡ rk E_d(Q) mod 2), the root
number constrains the parity of the rank. Since rk ≥ 1, if w(E_d) = +1 the
rank is at least 2. The four curves' root numbers satisfy a multiplicative
relation forced by u + v = (u+v) and u − v = (u−v): the product of root
numbers of the four curves is constrained by a Hilbert-symbol-type formula
over Q(i), the CM field. If this constraint forces the four root numbers to a
configuration that cannot support four curves each of rank ≥ 1, then a full
MSS is impossible — no appeal to K3 geometry, Brauer groups, or Chabauty
integration.

mechanism: The congruent-number curve E_d: y² = x³ − d²x is the twist of
E_1: y² = x³ − x by the quadratic character χ_d. Its L-function is L(E_d, s)
= L(ψ_d, s) where ψ_d is a Hecke character of Q(i) of weight 1 attached to
the element d ∈ Q(i). The global root number w(E_d) is a product of local
root numbers: w(E_d) = ∏_v w_v(E_d) where the local signs are known
explicitly: w_∞(E_d) = −1 always, w_2(E_d) depends on d mod 16 or mod 2^k
(known tables; Rizzo, 1999, or Dokchitser–Dokchitser), and for odd primes p|d,
w_p(E_d) is the Legendre symbol of something. The product over all places
gives w(E_d) = ±1.

Now, the four d values are u = e²·q_u, v = e²·q_v, u+v = e²·q_{u+v},
u−v = e²·q_{u−v} where q = 4mn(m²−n²)/(m²+n²)² ∈ Φ. The four curves are
quadratic twists of each other: E_{d1} ⊗ χ_{d2/d1} ≅ E_{d2}. The root numbers
satisfy w(E_{ab}) = w(E_a) w(E_b) × (something) when a and b are coprime, but
the additive relations u+v and u−v tie the curves in a different way.

The key structural fact: in Q(i), the element d = 2mn(m²−n²) (up to squares)
corresponds to the square of the Gaussian integer (m+ni) times its conjugate
difference: d = Im((m+ni)⁴)/4. So d, up to squares, is essentially the
quartic residue of m+ni. The four differences u, v, u+v, u−v correspond to
four Gaussian integers z₁, z₂, z₃, z₄ with z₃ ∼ z₁+z₂ and z₄ ∼ z₁−z₂ in
some sense. The root number w(E_d) for d = Im(z⁴) is related to the quartic
residue symbol (z/π)_4 in Q(i) for primes π dividing the conductor.

The computation: using the Dokchitser–Dokchitser formulae for root numbers of
CM elliptic curves, express w(E_u)w(E_v)w(E_{u+v})w(E_{u−v}) as a product of
local symbols. Since local solubility is established everywhere, each local
factor is independently consistent — but the global product may force a
parity contradiction: specifically, if w(E_u) = w(E_v) = w(E_{u+v}) =
w(E_{u−v}) = +1, then all four curves have even rank; but rk ≥ 1 from the
existence of a point in 2E(Q), so each must have rank ≥ 2. This is not a
contradiction by itself (curves can have rank 2). However, if the root number
product relation forces at least one curve to have w = −1 (odd rank) while
that same curve also must have rk ≥ 1 (because of the 2E(Q) condition), there
is no contradiction either — rank 1 with w = −1 is consistent.

The real leverage comes from the fact that for E_d to have a point in 2E(Q),
the 2-Selmer rank must be at least 2 (since 2-descent on E_d shows
dim_{F₂} Sel₂(E_d) = dim_{F₂} E_d(Q)[2] + rk E_d(Q) + dim_{F₂} Ш[2], and a
point in 2E(Q) forces the image of the 2-descent map to contain an element of
a specific shape). If the root numbers plus the 2-Selmer structure force a
contradiction in the parity of the dimension of Sel₂ across the four curves,
non-existence follows unconditionally (no BSD required for 2-descent
conclusions).

This approach is computationally concrete: the local root numbers of E_d for
d in specific residue classes are known, and the additive relations
d₁, d₂, d₁+d₂, d₁−d₂ impose congruence conditions on the d-values mod powers
of 2 and odd primes. A finite computation checks all residue class
configurations mod, say, 2⁶·3²·5², and verifies that none can satisfy the
four simultaneous 2E(Q) conditions.

status: refuted
speculation-vs-established: ESTABLISHED — E_d: y²=x³−d²x is the CM curve j=1728,
  its L-function is a Hecke L-function over Q(i), and its global root number is
  a product of local root numbers computable by the Dokchitser–Dokchitser
  algorithm; the "point in 2E_d(Q) forces rk ≥ 1" step is classical 2-descent.
  SPECULATION — (a) that d = 2mn(m²−n²) is Im((m+ni)⁴)/4 up to squares and
  that this gives a clean quartic-residue description of the local root
  numbers; (b) that the additive relations u+v, u−v induce a usable
  multiplicative relation among the four root numbers strong enough to force a
  parity/Selmer contradiction; (c) that a finite residue-class computation
  mod 2⁶·3²·5² can close the case. All three are exactly what the first-step
  must check, and any of them failing would close the approach.
first-step: Derive the exact formula for the global root number w(E_d) where
  d = 2k²mn(m²−n²) with primitive m>n. Use the Dokchitser–Dokchitser
  algorithm or the Rizzo tables for twists of y² = x³ − x. Then, for a grid
  of residue classes of (u, v) modulo 2⁶·3²·5², compute the four root
  numbers and check whether the pattern (all four curves having 2-Selmer rank
  ≥ 2) can occur. If no residue class survives, the proof is complete
  (unconditional, via 2-descent). If some classes survive, they give explicit
  congruence constraints on any counterexample — a strong partial result.
## Verdict (literature check): refuted

**What the reformulation actually is.** The four curves E_d: y² = x³ − d²x are
the congruent-number curves, i.e. the quadratic twists of E_1: y² = x³ − x
(j = 1728, CM by Z[i]) by the character attached to d. The candidate's first
claim is established and classical: the analytic rank/order of vanishing
R(n) = ord_{s=1} L(E_n, s) has parity determined by n mod 8. Precisely
(Birch–Stephens, "Calculation of Tate–Shafarevich groups", Topology 1966;
repeated in e.g. "A necessary condition for p and 2p to be congruent for a
prime p ≡ 1 (mod 8)", J. Number Theory, 2023):

    R(n) ≡ 1 (mod 2)  iff  n ≡ 5, 6, 7 (mod 8),
    R(n) ≡ 0 (mod 2)  iff  n ≡ 1, 2, 3 (mod 8).

So for each of the four differences d = u, v, u+v, u−v the root number (≡
parity of R(d)) is fixed by d mod 8. The global root number of a CM curve is
indeed a product of local root numbers, computable by the Dokchitser brothers'
algorithm (J. Reine Angew. Math., 2010) and Rizzo's tables — that part of the
candidate is real.

**Why it does not close the problem.** The parity formula is a *necessary
condition*, not an obstruction, and it is compatible with everything the run
already knows:

1. A point in 2E_d(Q) forces rk E_d(Q) ≥ 1, but an even root number (rank ≥ 1
   with even parity → rank ≥ 2, or rank 0) and an odd root number (rank odd ≥ 1)
   are both perfectly consistent with rk ≥ 1. There is no configuration of the
   four parities that rules out four curves each of rank ≥ 1. The candidate's
   hoped-for "multiplicative relation among the four root numbers forced by
   u+v, u−v that is incompatible with four rank-≥1 curves" is exactly the step
   the file itself flags as speculation (b), and no published result supplies it.
2. The parity of R(n) is inherently a **Q-level, mod-2** phenomenon. The run's
   established hinge (`extension-field-mss-exist`) is that genuine MSS exist over
   Q(√3,√133) and Q(√3). Any argument that relies only on Q-ranks, Q-root numbers
   and Q-2-Selmer parity cannot distinguish Q from these extensions, so it cannot
   be the whole obstruction. A parity contradiction is therefore dead on the same
   grounds as every other Q-level local/descent argument.
3. The 2-Selmer/descent level of exactly this four-curve family was already
   refuted as `simultaneous-congruent-numbers-2selmer` (subsumed by Bremner II's
   K3 NS and singular-fibre data). Root-number parity is the analytic shadow of
   that same descent; it carries the same rank information at mod 2 without the
   geometric structure Bremner already extracted. It adds no new leverage.

**killed-by**: the known root-number parity law (Birch–Stephens: R(n) mod 2
determined by n mod 8) is a necessary condition compatible with the witness and
forces no incompatibility among four rank-≥1 curves; the decisive
additive-relation→root-number relation is unestablished speculation; and the
Q-level mod-2 framework cannot separate Q from the extension fields over which
MSS provably exist (the run's own `extension-field-mss-exist` hinge).

## Precedent for the verdict

- Birch & Stephens, "Calculation of Tate–Shafarevich groups", Topology 5 (1966)
  295–316 — the R(n) mod 2 by n mod 8 parity law for E_n: y²=x³−n²x.
- "A necessary condition for p and 2p to be congruent for a prime p ≡ 1 (mod 8)",
  J. Number Theory (2023), https://www.sciencedirect.com/science/article/pii/S002240492300018X
  — restates the parity law and its use as a necessary (not sufficient) condition.
- T. & V. Dokchitser, "Root numbers and parity of ranks of elliptic curves",
  J. Reine Angew. Math. (2010), arXiv:0906.1815 — local root numbers computable.
- `simultaneous-congruent-numbers-2selmer` (this library, refuted) — the same
  four-curve descent at the 2-Selmer level, subsumed by Bremner II's K3.
- `extension-field-mss-exist` (this library) — MSS exist over Q(√3,√133); a
  Q-parity-only argument cannot be the obstruction.

## First step (none — refuted, do not pursue)

The first-step's finite residue-class check mod 2⁶·3²·5² was never a route to a
contradiction: the parity configuration of the four curves is determined by four
independent mod-8 classes and admits four compatible rank-≥1 assignments.

precedent:
  - The congruent-number curve E_d: y² = x³ − d²x is the CM curve with
    j=1728; its L-function and root numbers are classical
  - O. Rizzo, "Average root numbers for a non-constant family of elliptic
    curves" (1999); Dokchitser–Dokchitser, "Root numbers of elliptic curves"
    (2010) — computation of local root numbers
  - The Dokchitser brothers' root number formula for CM curves: the global
    root number is a product of local symbols; for Q(i)-CM curves, the root
    number at an odd prime p is (−1)^{(some exponent function of d)}
  - The parity conjecture for elliptic curves over Q (weak BSD): ord_{s=1}
    ≡ rk mod 2; unconditionally known for CM curves? Not in general, but the
    2-Selmer parity can be studied without BSD
  - This approach is the analytic number theory layer that sits between the
    local-to-global Hasse-principle (already checked) and the geometric
    Chabauty/K3 methods. It is not subsumed by either.
  - The refuted simultaneous-congruent-numbers-2selmer approach tried to use
    2-Selmer relations but was subsumed by Bremner II's K3 NS because it
    didn't exploit the root number / L-function level. This approach works
    at the analytic level (root numbers) rather than the geometric level
    (NS of the elliptic surface), so it is genuinely different.
```