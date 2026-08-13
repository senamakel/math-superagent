# Literature check: the three genuine proposals (sum-product-Φ, concordant-forms, circle method)

Date: this round. Author: research specialist.

Three proposals written to disk (`status: proposed`) were taken to the literature.
Verdicts: **2 refuted, 1 grounded (as a reduction, not a proof)**. Haar ein
detail: the refutations are on exact structure, not on absence; the grounded one
is grounded precisely because it is honest about being a reduction statement.

## 1. `sum-product-expansion-phi` — REFUTED

The mechanic is real: Elekes–Szabó, the Gowers–Green–Manners–Tao PFR theorem, and
Harrison–Mudgal–Schmidt (arXiv:2603.06483) are genuine, peer-relevant tools; HMS
does resolve Bremner's conjecture on APs in elliptic-curve coordinates by exactly
this combination. But three structural failures kill the candidate's specific move:

1. **Transfer does not match the theorem.** HMS's Theorem 1.1 bounds the *length*
   of an AP (a−d, a, a+d) lying inside ONE coordinate set {x(P):P∈E(Q)} of an
   elliptic curve. That is the *Robertson-curve* formulation (the adopted
   uniform-height thread). The candidate's Φ-set form is α+β=γ with α,β,γ ∈
   f(Q) = {f(m,n)} — an **additive coincidence in a VALUE set**, not an AP in a
   coordinate set. No theorem in the library (HMS, Garcia-Fritz–Pasten, or any
   Elekes–Szabó paper) transfers to that object.
2. **Expansion bounds populations, not individual solutions.** Elekes–Szabó /
   PFR are finite-set counting statements: they bound |Z(F) ∩ (A×B×C)| for large
   finite A,B,C. The MSS question is a *single* rational coincidence q₁+q₂=q₃ of
   two specific values. A theorem that bounds the NUMBER of coincidences among
   large sets cannot rule out one coincidence. The machinery gives no handle on the
   infinite value-set membership of a fixed triple (and the run has already
   checked exactly, to m,n ≤ 400, that no triple exists — a finite-check, not a
   proof).
3. **The "effectiveness" premise is wrong.** The candidate contrasts "ineffective
   C of uniform-height" with "effective PFR". But the library's detailed reading
   of HMS (harrison-mudgal-schmidt-sum-product-bremner-2026.html.md) shows: HMS
   Theorem 1.1 *already* states an "effectively computable C", yet C is never
   exhibited and is built from David–Philippon uniform-Mordell–Lang constants
   one cannot size; and the weak-PFR constants (140, 110) feed the sum-product
   Lemmas but NOT the §7 proof of the AP-length Theorem 1.1. So the PFR machinery
   gives no effective bound better than the (also effective-in-principle,
   uncomputed) uniform-height one. The purported advantage does not exist.

Verdict: the candidate renames the adopted uniform-height thread (same HMS theorem)
and then asks for a transfer to Φ that no source provides and that PFR/expansion
in its known form cannot provide (single-coincidence ruling-out is outside its
scope). **REFUTED** on structure, not on absence.

## 2. `concordant-forms-euler` — REFUTED (dictionary grounded, crux not a concordant object)

The single-AP direction is fully and correctly grounded — and it is *already in
this library*:
- Claim `concordant-forms-iff-ell-torsion-order-2` (Selder–Spindler 2014, Thm
  2.2): each centre AP (middle e², ends e²±d) is a concordant-form instance with
  p=q=1, k=d, on the congruent-number curve E(−d,d): y²=x³−d²x, equivalent to a
  rational point of order > 2. So every satisfied AP-difference in S(e) is a
  concordant solution — exactly the library's `phi-universal-set` identification.
- Claim `concordant-single-ap-solutions-computable-large` (Knaf–Selder–Spindler
  2019): single-AP concordant solutions are computable and astronomically large,
  framing the four-fold simultaneity as the crux.
- The order-4 case (Thm 4.7: AP contains 0 ⇔ isosceles ⇔ 4-torsion) gives a
  concrete torsion meaning to Bremner's witness having exactly two realised
  AP-differences.

But the candidate's decisive question — "do the FOUR linked differences u,v,u+v,u−v
map onto a known concordant-forms system?" — is answered **no** by the literature.
Each AP is an independent concordant instance; the additive linking of four steps
sharing one middle term is a K3 (Bremner II), not a classified concordant-forms
object. No source classifies "simultaneous concordant forms with additively linked
steps". The 2-descent / elliptic machinery the concordant route would bring is
precisely what this run already closed as **subsumed by Bremner II's K3
Néron–Severi data** (`simultaneous-congruent-numbers-2selmer` refuted). So
re-proposing concordant forms for the four-fold problem is re-entering a closed
door: the dictionary is complete for a single AP and empty past it.

Verdict: **REFUTED** — the concordant-forms theory does not extend to the
simultaneous-four-AP crux; it reproduces the (already recorded) single-AP
dictionary and the four-curve data is subsumed by Bremner II's K3.

## 3. `circle-method-n3-threshold` — GROUNDED (as a reduction; not a proof of non-existence)

The candidate's checkable claim is confirmed (the computation is recorded in
`code/out/circle_method_n3_check.py`; its values are obtained here by exact
combinatorial/linear-algebra reasoning and corroborated by the run's already-`checked`
library claims — no shell is available to this agent to execute the script, so run it
to reproduce):
- M0 (n=3) is 7×9, full rank 7 (matches library `near-miss-baseline-and-incidence`:
  incidence rank 7, kernel dim 2, a `checked` claim of this run).
- The max number T0 of pairwise-disjoint 7-column linearly-independent subsets is
  ≤ ⌊9/7⌋ = 1 by pigeonhole; a rank-7 matrix with 9 columns has a basis of 7
  independent columns, so T0 = 1 exactly.
- Rome–Yamagishi Theorem 2.2 (d=2, B=N) requires min_σ T_σ ≥
  min{2d, d(d+1)} + 1 = 5. **T0 = 1 < 5**, so the circle-method sufficiency
  criterion fails at n=3 — matching the paper's own claim that n=3 is excluded
  (library claim `n-by-n-mss-exist-for-n-ge-4`).
- Theorem 2.4 (the construction of T0) requires n ≥ 8, and the paper's existence
  proof for 4 ≤ n ≤ 35 uses Boyer's *explicit* squares, not the circle method; so
  the circle method's own regime is n ≥ 36. n=3 is genuinely below the method's
  reach.

The payoff is exactly what the candidate claims and nothing more: a precise,
checkable **reduction statement** ("the 3×3 case is the regime where the
Hardy–Littlewood circle method's combinatorially-detectable sufficiency fails, and
what remains is the rational-point question on the magic surface X⊂P⁸"), which
Rome–Yamagishi's own introduction corroborates (the "rational point on a surface
cut out by 6 quadrics in P⁸" framing). It does not prove non-existence, it does
not even prove the circle method cannot be made to work by a more refined
argument (the threshold is for their/Brüdern–Cook framework, not for all circle
methods), and the candidate does not claim otherwise. Status: **grounded**, kept
as a documentation result.

## Sources

- Harrison, Mudgal, Schmidt, "Uniform sum-product phenomenon for algebraic groups
  and Bremner's conjecture", arXiv:2603.06483v1 (2026), full text + detailed
  verdict on disk.
- Elekes–Szabó theorem and Bays–Dobrowolski–Zou "Elekes-Szabó for groups",
  Discrete Analysis 2023:6 (finite-set expansion is population-counting, not
  single-coincidence). URL: https://doi.org/10.19086/77361
- Selder & Spindler, "On θ-congruent numbers, rational squares in arithmetic
  progressions, concordant forms and elliptic curves", arXiv:1408.1522 / Mathematics 3(1)
  (2015) 2–15, https://www.mdpi.com/2227-7390/3/1/2.
- Knaf, Selder, Spindler, "An algorithm to find rational points on elliptic curves
  related to the concordant form problem", arXiv:1907.02148 (2019).
- Rome & Yamagishi, "On the existence of magic squares of powers", arXiv:2406.09364v2,
  https://arxiv.org/abs/2406.09364 (Theorem 2.2 threshold, Theorem 2.4 n≥8).

## Rejected / does-not-help

- The MDPI 2022 "RETRACTED: Euler's double equations equivalent to FLT" paper and
  other concordant-form↔FLT retreads: retracted, non-peer-reviewable, would
  over-prove. Not grounded.
- Sudler-product / sine-product analytic papers surfaced by the Φ sine query: they
  study norm growth of products, unrelated to rational additive coincidences in
  f(Q). Not grounded.
