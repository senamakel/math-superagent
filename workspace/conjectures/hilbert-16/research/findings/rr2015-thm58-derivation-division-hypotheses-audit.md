# RR 2015 Theorem 5.8 — audit of the "conditional center-ideal/derivation-division zero bound"

**Question.** Does a held source actually support the run's conditional
center-ideal / derivation-division zero bound — displacement maps of the form
V = Σᵢ Aᵢ(λ) Mᵢ(1+gᵢ), Mᵢ generalized monomials, gᵢ uniform o(1) remainders,
bound "at most l−1 zeros per leaf, uniformly over a compact parameter box"?
And which hypotheses are missing?

**Answer.** Partially. The bound is exactly **Roussarie–Rousseau 2015, Theorem 5.8**
(arXiv:1506.07104, Appendix II "Counting the number of roots"; held full text at
`research/sources/primary-roussarie-rousseau-2015-center-graphics.full.md` lines
1007–1190, duplicate `rousseau-shan-zhu-center-graphics-2015.full.md`), whose
hypotheses the run's goal files state *almost* correctly. Three ingredients the
run's goal text carries are **not** hypotheses of the theorem and are the
missing pieces: uniformity over a compact box, the identically-zero exclusion,
and (for the H^3_13 non-boundary strata) the Ω-free monomial restriction.
The phrase "center ideal" is not a hypothesis of Theorem 5.8 at all — it is
what the *applications* prove about the coefficients Aᵢ.

---

## 1. What the source actually states (verified from held full text)

**Theorem 5.8** (primary copy lines 1099–1131). Let
V(r,ρ,λ) = Σ_{i=1}^l Aᵢ(λ) Mᵢ (1 + gᵢ(r,ρ,λ)) on 𝒜×ℬ ∩ {r>0, ρ>0}, where:

1. **Mᵢ = r^{aᵢ} ρ^{bᵢ} ω^{cᵢ}** are *general monomials without Ω-factor*
   (Definition 5.4; ω = (ωⱼ) compensators, aᵢ, bᵢ, cᵢ smooth in λ);
2. **gᵢ are C^k-functions on monomials with k ≥ l**, of order **o(1)** — and
   Notation 5.2 defines o(1) as **h(0,0,λ₀) = 0**: a *pointwise value condition
   at the base parameter value*, not a uniform limit over a box;
3. **Aᵢ(λ) are continuous** (nothing more — not analytic, not smooth);
4. **pairwise non-resonance**: aⱼ⁰ − aᵢ⁰ − bⱼ⁰ + bᵢ⁰ ≠ 0 for i ≠ j (eq. 5.5),
   equivalently the reduced exponents pᵢ⁰ = aᵢ⁰ − bᵢ⁰ are pairwise distinct
   (Remark 5.9(3)).

Then, on a **sufficiently small neighborhood 𝒜×ℬ of (0,0,λ₀)**:
**(i)** V has at most l−1 isolated zeros counted with multiplicity on each
curve l_ν = {rρ = ν} ⊂ 𝒜 (the orbits of 𝒳 = r∂ᵣ − ρ∂_ρ, which are connected —
this is what Rolle needs); **(ii) or V is identically zero.**

Proof (lines 1131–1174): divide by M₁(1+g₁), apply L_𝒳 (Lemma 5.7), repeat
l−1 times; ends with V_{l−1} = (∏(aᵢ−bᵢ−aₘ+bₘ))·A_l·M_l·M_{l−1}⁻¹·(1+g_l^l)
nowhere zero when A_l ≠ 0, then Rolle backwards. Lemma 5.3 is the workhorse:
L_𝒳 of a C^k-function on monomials is C^{k−1} on monomials and still o(1) —
this is exactly the "behaves well under derivation" that the run's summaries
attribute to the method.

## 2. What is NOT in the theorem — the missing hypotheses

**(a) Uniformity over a compact box.** Theorem 5.8 is local in λ₀: the bound
l−1 holds on small neighborhoods 𝒜^l × W_l that *depend on λ₀*. The run's goal
`h16-2-h13-3-finite-cyclicity-h13-derivation-division-uniform-zero-bound`
("applies uniformly on a sufficiently small compact parameter box … independent
of the parameter") is a **strengthening not stated in the source**. It becomes
true only by the surrounding argument: the compact box is covered by finitely
many such neighborhoods (compactness) and the expansions must be valid on the
whole cover — that is application work (done for the *boundary* set in RR
Thm 3.6), not a conclusion of Thm 5.8. The RSZ companion paper
(`rousseau-shan-zhu-2015-second-type-dulac-full.full.md`) does carry a genuine
uniformity statement, but it is about *Dulac-map remainders* — Mourtada
property (I), Definition 2.6: "lim_{y→0} y^i ∂ⱼϕ/∂yⱼ = 0 **uniformly for
λ ∈ W′**" — a different ingredient, verified per graphic, and exactly the open
analytic gap for the run's targets.

**(b) The identically-zero exclusion.** Alternative (ii) is "V ≡ 0". A zero
bound needs this case absent. The run's goal files say "identically-zero cases
excluded by the center-ideal/nonzero clause" — correct and necessary, but it is
**not part of Theorem 5.8**. The source's own application shows what it means
(second copy line 499): "either V has at most two small zeros, or V is
identically zero, **in which case we have a center**." So the exclusion is the
center condition of the graphic — a hypothesis the run must carry explicitly.

**(c) Ω-free monomials.** Hypothesis (1) excludes Ω-factors. But second-type
Dulac maps (RR Thm 2.3, lines 253–274) and the I^1_14 computation (eq. 3.34)
genuinely produce ω- and Ω-terms. For the **boundary set of H^3_13** this is
moot: eq. (3.32) has only powers and ρ — "This equation contains no resonant
monomials … We conclude that the cyclicity is at most two by Theorem 5.8"
(proof of Thm 3.6). But the run's target is the **non-boundary strata** of
H^3_13, whose expansions (per the run's own goal `H13-generalized-displacement-expansion`)
are stated as "generalized monomials (powers and compensators)" — **if any
stratum's Mᵢ include Ω-factors, Theorem 5.8 does not apply as stated**. Either
the Ω-terms must be shown to absorb into the remainder, or an extended theorem
is needed. This is a concrete, checkable missing hypothesis.

**(d) k ≥ l, and the shrinking-neighborhood convention.** Condition (2)
requires k ≥ l (the proof needs g_l^l to be at least C⁰ after l−1 derivations).
The surrounding text (after Definition 5.1) explains the convention: functions
are C^k on monomials *for every k*, with the monomial choice and neighborhood
size allowed to depend on k — this is where the analytic/quasianalytic content
lives (a C^∞-only argument is exactly Dulac's 1923 error shape). The run's
"uniformly controlled C^k" must carry k ≥ l with l the number of terms.

**(e) The dominance regions (proof-internal, flag for formalisation).** Both
held copies read ℬᵢ = {λ ∈ ℬ | **Aᵢ(λ) ≥ Aⱼ(λ)** ∀j} — *signed*, no absolute
values (primary line ~1133; second copy line 1129). But the proof's alternative
"A_l(λ) ≠ 0 or A₁ = ⋯ = A_l = 0" is valid only with the **magnitude** version
|Aᵢ| ≥ |Aⱼ|: if A_l is the signed max and A_l = 0, the other Aⱼ are only ≤ 0,
not = 0, so the final V_{l−1} could vanish and Rolle fails. Bars are preserved
elsewhere in the same conversion (e.g. |b| ≥ 2√2, line 89), so this is either a
lossy spot in the HTML→MD conversion or an imprecision in the paper itself
(the theorem is standard in use — the magnitude reading is almost certainly the
intended one, and applications order the coefficients by monomial size anyway).
**Anyone formalising from this held copy must decide this; the held text is not
self-contained at that step.**

## 3. The Lean layer's concrete gap

`code/lean/Lib/RCenterIdealZeroDivision.lean` isolates the analytic step as a
hypothesis `zero_division`:
∀ V′ satisfying (representation + center-ideal membership + uniform remainder),
∃ N, (ZeroSet K collar V′).Finite ∧ ncard ≤ N.
As written this hypothesis is **unsatisfiable**: V′ ≡ 0 satisfies all three
preconditions (0 ∈ the ideal, |0| ≤ C·|remainder_bound|) yet has ZeroSet =
K × collar, infinite when K and collar are compact infinite sets — so no finite
N exists. The theorem therefore holds vacuously and cannot be instantiated with
the real RR theorem unless the preconditions exclude the identically-zero case
(or quantify only non-identically-zero V′). The run's own goal text already
carries that clause ("identically-zero cases excluded by the center-ideal/
nonzero clause"); **the Lean file must add it to the `zero_division`
antecedent.** This mirrors Theorem 5.8's alternative (ii) exactly.

## 4. Verdict

- **Supported by the source**: the bound "≤ l−1 zeros counted with multiplicity
  per leaf rρ = ν" for V = Σ Aᵢ Mᵢ(1+gᵢ) with Mᵢ general monomials **without Ω**,
  gᵢ C^k on monomials **k ≥ l**, **gᵢ = o(1) in the pointwise sense
  h(0,0,λ₀)=0**, Aᵢ **continuous**, pairwise non-resonance — locally in λ₀.
- **Not in the source, must be carried by the run**: (a) uniformity over a
  compact box (finite-cover corollary, needs expansion-validity on the cover);
  (b) the identically-zero exclusion (= center condition in applications);
  (c) Ω-free expansions on every non-boundary H^3_13 stratum (or an extended
  theorem); (d) k ≥ l with the for-all-k convention; (e) the |Aᵢ| ≥ |Aⱼ|
  magnitude reading of the dominance regions.
- **The "center ideal" is not a hypothesis of the theorem.** It enters at the
  application layer: RR §3 (line 465) proves {ε₀, ε₁, μ̄₃} generate the center
  ideal I_C for the boundary set, and line 27 describes the method as "aᵢ belongs
  to the center ideal … hᵢ(z) = o(1) behaves well under derivation". The
  run's phrase "conditional center-ideal/derivation-division zero bound" fuses
  two layers that the source keeps separate.

**Sources.** Roussarie–Rousseau 2015, arXiv:1506.07104, Thm 5.8 + Def 5.1/5.4 +
Notation 5.2 + Lemma 5.3/5.7 (held: `primary-roussarie-rousseau-2015-center-graphics.full.md`
lines 1007–1190); application to H^3_13 boundary: Thm 3.6, eq. (3.32); center
ideal: §3 line 465; second-type Dulac maps: Thm 2.3; RSZ companion
`rousseau-shan-zhu-2015-second-type-dulac-full.full.md` Def 2.6 (Mourtada
property (I), uniform remainder) and Thm 3.1 (explicit Rolle argument).
