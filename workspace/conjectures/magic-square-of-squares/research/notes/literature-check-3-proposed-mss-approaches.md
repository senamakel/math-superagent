# Literature check: three proposed MSS approaches

Date: this round. Author: research specialist.

Three candidate lines of attack were taken to the literature and this run's own
claims. Two are **refuted** on exact structure; the third is grounded as a real
method but carries a structural obstruction to being a proof. For each I report
(a) published-for-MSS?, (b) known obstruction, (c) first-step feasibility.

## 1. Elimination ideal / Gröbner basis over Z → **refuted**

Proposal: eliminate s_1..s_9 from {entry_i(c,u,v) − s_i² = 0} over Z[c,u,v], get
J = I(V)∩Z[c,u,v] that contains 1, or defines a surface, or defines curves.

**(a) Published for MSS?** No. Every Gröbner/elimination treatment of magic
squares found (Gröbner-style Sudoku/puzzle papers; Hengeveld's MSS-over-F_p
thesis; Helms' linear parametrisation) either works over a finite field where
"square mod p" is a residue check, or merely re-derives the (c,u,v) linear
parametrisation. None applies an elimination ideal over Z to the rational MSS.
Cain arXiv:1908.03236 uses elimination/parametrisation over finite fields and
rings Z/nZ, not over Z.

**(b) Known obstruction — fatal, structural.** Over an algebraically closed (or
fraction) field, "is a perfect square" is NOT an algebraic condition: for every
(c,u,v), entry_i is an affine linear form and s_i = √entry_i always exists in
Q̄. Hence the map (c,u,v,s_i)→(c,u,v) is dominant, the elimination ideal
J = (0), and V(J) = A³. The proposed trichotomy is false — none of the three
holds. The whole difficulty of the problem is *rational/integral* square roots
(distinctness, positivity), which no ideal over a closed field can see.
Independently, J cannot contain 1: a full nine-square MSS exists over
Q(√3,√133) (Bremner 1999), so V has a Q̄-point and J is not the unit ideal.
Verification: `code/out/candidate_verdict_math.py` (dominance immediate; every
entry an affine form with Q̄ square root).

This is the same category error the run's `integral-brauer-manin-nine-square`
hit: algebraic geometry over a closure cannot express the rational-square-root
condition. The obstruction is arithmetic (rational roots in an additive
configuration), not variety structure.

**(c) First-step feasibility.** Nil — computing a literal Gröbner basis of an
ideal that equals (0) teaches nothing. Not worth the compute.

## 2. p-adic valuation / Newton polygon of the duplication map → **refuted**

Proposal: x([2]P) = (x²+c²)²/(4x(x²−c²)) on E:y²=x³−c²x restricts p-adic
valuations of doubled-point x-coordinates; the AP condition x₁+x₃=2x₂ forces an
impossible valuation relation.

**(a) Published for MSS?** No. The valuation machinery is real and explicit
(v_p(x(nP)) = v_p(φ_n)−2v_p(ψ_n); elliptic nets / division-polynomial
valuations) but only for a FIXED curve and FIXED point — it computes valuations,
it does not produce contradictions, and it is consistent with the witness. No
source applies it to the MSS doubled-point AP.

**(b) Known obstruction — fatal, established by this run's own checked
computation.** Claim `phi-padic-no-obstruction` (research/approaches/
padic-modular-obstruction-dead-end.md; seven exact programs) shows the achievable
residue sets R_p^a = {f(m,n) mod p^a} are **non-degenerately additively
closed** for every p ∈ {2,3,5,7,11,13} and p^a ≤ 2000 (and by exhaustive
residue-class enumeration). No pure p-adic/residue sieve at these primes can rule
out the additive triple q1+q2=q3. The system is locally solvable everywhere; the
obstruction (if any) is global/rational, not a finite p-adic truncation. The
Bremner witness realises two of the three AP x-coordinates in 2E(Q)
(robertson_reduction_check.txt), and its q-values 5544/7225 and 336/625 satisfy
the proved v2≥3, v3≥1 with no local contradiction (candidate_verdict_math.py,
checked). A valuation relation that forbade double-membership would kill this
witness — the run's oracle contract.

**(c) First-step feasibility.** Already executed and exhausted: the seven
`phi_padic_*` programs plus the duplication-map check. Nothing further along this
axis is worth computing unless a prime beyond 13 or a fundamentally non-local
argument is introduced.

## 3. Mordell-Weil sieve on the Robertson curve → **grounded as method, obstructed as proof**

Proposal: on a fixed E:y²=x(x²−c²), use local mod-p images to show no MW
combination of generators yields three doubled points with x-coords in AP.

**(a) Published for MSS?** No. The Mall-Weil sieve itself is thoroughly real and
published: Bruin & Stoll, "The Mordell–Weil sieve: proving non-existence of
rational points on curves", LMS J. Comput. Math. 13 (2010) 272-306; repeatedly
used as the decisive finishing tool in rational-point computations (e.g.
Quadratic Chabauty for modular curves, Compositio Math. 2023). But no source
applies it to the 3×3 MSS elliptic formulation.

**(b) Known obstruction — two structural.** (i) *Scope mismatch*: the sieve is
per-curve; it certifies points on ONE fixed curve given explicit generators of
that curve's MW group. The MSS problem is a family parameterised by c=e² with
the centre unbounded (>25×10²⁴ per Buell/Morgenstern; millions of e≤10⁷ admit
four AP-differences). Every candidate c needs its own mwrank generator
computation and its own sieve — cost scales with the BOUND, which this run's
method rules out as "wrong method" (enumeration over an unbounded family).
(ii) *Rank direction*: Garcia-Fritz–Pastén / Bremner's rank conjecture (the
run's adopted `uniform-height-bound-elliptic-ap`) says long APs of x-coords
force LARGE rank, and the MW sieve is exactly the tool that degrades as rank
grows (the cotational lattice image covers more of the product of local groups,
so the empty-intersection obstruction is exponentially harder). Bremner's witness
curve has rank 2 (this run computed, mwrank+Sage agree), and the three AP
x-coordinates (139129, 180625, 222121) are only TWO points of 2E(Q) — the third
fails (222121's quartic has no rational root, computed exactly).

**(c) First-step feasibility.** Feasible and worth doing ONCE for a fixed centre
as a checkable per-curve theorem: c=138600, exact MW basis already known (rank
2, generators (-88200,·),(315000,·)), run Bruin–Stoll's sieve for the
three-point-AP-in-2E condition. It proves non-existence for that c only; it can
never be a global proof.

## Verdicts

| Approach | (a) published for MSS? | (b) obstruction | (c) first step | status |
| --- | --- | --- | --- | --- |
| 1. Elimination ideal over Z | no | fatal: J=(0), V(J)=A³; square conditions vacuous over Q̄ | nil | **refuted** |
| 2. p-adic valuation/Newton polygon | no | fatal: residue sets additively closed at all p,a tested (phi-padic-no-obstruction) | exhausted | **refuted** |
| 3. Mordell-Weil sieve | no | per-curve scope + large-rank regime; cost scales with unbounded bound | feasible per-curve (c=138600), never global | **grounded-as-method, obstructed-as-proof** |

## Sources used

- Bremner, "On squares of squares", Acta Arith. 88 (1999) 289-297 (Robertson
  reduction: MSS ⇔ three points of 2E(Q), x-coords in AP; 2E(Q) membership
  criterion; extension-field MSS). Library: research/sources/
  bremner-on-squares-of-squares-1999.full.md.
- Bruin & Stoll, "The Mordell–Weil sieve: proving non-existence of rational
  points on curves", LMS J. Comput. Math. 13 (2010) 272-306.
  https://www.cambridge.org/core/journals/lms-journal-of-computation-and-mathematics/article/mordellweil-sieve-proving-nonexistence-of-rational-points-on-curves/29EFF630FD2859F8C79DFD48E1A33926
- Garcia-Fritz & Pastén, "A note on Bremner's conjecture and uniformity",
  arXiv:2604.04850 (2026) — long APs of x-coords force large rank. Library:
  research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md.
- Michaud-Rodgers, Warwick 2019 talk/project (magic variety is a surface with
  256 singular points; where a Gröbner elimination would be computed).
- Elliptic-nets / division-polynomial p-adic valuations (J. Number Theory /
  Can. J. Math.) — the correct valuation machinery, no contradiction content.
- This run's claims: phi-padic-no-obstruction (checked),
  phi-universal-set, phi-no-triple-m400, integral-bm-nine-square-not-applicable.

## Rejected sources / why

- Gröbner-basis Sudoku/magic-square papers: model linear/algebraic constraints,
  not "is a square"; not applicable.
- Hengeveld MSS-over-F_p thesis, M. Helms drafts: finite-field or linear
  parametrisations only; confirm the (c,u,v) parametrisation, stop short of the
  rational case.
- "p-adic L-function Newton polygon" (Pollack L±_p) papers: supersingular
  Iwasawa theory, unrelated to doubled-point valuations.
