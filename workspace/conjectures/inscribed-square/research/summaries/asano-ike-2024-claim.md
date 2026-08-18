# Asano–Ike 2024 — precise claims

**Source:** Tomohiro Asano, Yuichi Ike, "The rectifiable rectangular peg problem," arXiv:2412.21057v3 (5 Jan 2026). Full text: [[research/sources/asano-ike-2024-rectifiable-rectangular-peg.full.md]]

---

```claim
id: asano-ike-2024-thm1-1
statement: Let c : S¹ → R² be a Jordan curve. Assume there exists a sequence of smooth
  Jordan curves (cₙ : S¹ → R²)ₙ such that
  (1) (cₙ)ₙ → c in the C⁰ sense, and
  (2) setting fₙ to be the primitive of (cₙ ∘ e)∗λ, the sequence (fₙ)ₙ converges to a
      continuous function f on R uniformly on every compact subset,
      where e : R → R/2πZ ≃ S¹ is the quotient map and λ = ξ dx is the Liouville 1-form
      on T*R (so (c ∘ e)∗λ = y(t) dx(t) under the identification R² ≅ T*R, (x, y) = (x, ξ)).
  Then c inscribes a θ-rectangle for every θ ∈ (0, π).
hypotheses:
  - c is a Jordan curve (continuous injective S¹ → R², image C).
  - c admits the existence of smooth approximants cₙ with C⁰ convergence and the
    primitive convergence condition (2).  This pair of conditions is called "admitting
    a continuous Legendrian lift."
  - No further regularity (not even rectifiability) is assumed on c beyond what the
    Legendrian-lift condition implies.
status: proved-by-source
evidence: Asano–Ike 2024 arXiv:2412.21057, Theorem 1.1 (p.2), §5.1 proof pp.20-26
holds-here: yes
bearing: The sharpest known positive result for the square-peg problem.  It subsumes
  Stromquist's locally-monotone theorem, Tao's two-graph result, and Greene–Lobb's
  smooth-rectangle result.  The frontier it leaves: whether every Jordan curve admits
  a continuous Legendrian lift.
falsifies: A rectifiable Jordan curve (which Cor 5.9 says does satisfy the hypothesis)
  with no inscribed θ-rectangle for some θ; or a retraction/correction of the preprint
  showing the proof has a gap.
answers: asano-ike-2022-lift-convergence-role
```

```claim
id: asano-ike-2024-continuous-legendrian-lift-defn
statement: A Jordan curve c : S¹ → R² admits a continuous Legendrian lift iff there
  exists a sequence of smooth Jordan curves (cₙ)ₙ such that (i) cₙ → c in C⁰, and
  (ii) the primitives fₙ (each a function R → R with dfₙ = (cₙ ∘ e)∗λ on R, where
  e : R → S¹ is the universal cover) converge uniformly on compact sets to a continuous
  function f : R → R.
  Equivalently, the Legendrian lift L̃_c = {(c(t), f(t))} ⊂ J¹(R) ≅ T*R × R_t of c
  exists as a continuous Legendrian curve, approximated by the smooth Legendrian lifts
  of cₙ.
  The key consequence (entering the proof via Proposition 2.3 and Proposition 5.1) is
  that the sheaf quantization F_C of C×C, obtained as the limit of sheaf quantizations
  F_{Cₙ} of the smooth approximants, satisfies
    T_a SS•(F_C) ∩ SS•(F_C) = ∅   for all a ∈ R \ πZ,
  which is exactly the hypothesis of Theorem 4.1.
hypotheses:
  - c is a Jordan curve (injective continuous S¹ ↪ R²).
  - cₙ are smooth Jordan curves satisfying (i) and (ii).
  - λ = ξ dx is the Liouville 1-form on T*R; (cₙ ∘ e)∗λ = yₙ(t) dxₙ(t) under the
    identification R² ≅ T*R with coordinates (x, y) = (x, ξ).
status: proved-by-source
evidence: Asano–Ike 2024, §1.1 (p.2), combined with Proposition 2.3 (p.6), Proposition 5.1
  (p.20), proof of Theorem 1.1 (pp.25-26)
holds-here: yes
bearing: This is the *hypothesis gap* of the problem.  The run's frontier is exactly
  whether every Jordan curve (or a strictly larger class than rectifiable curves) admits
  such a lift.  The paper proves that all rectifiable curves (Cor 5.9) and all locally
  monotone curves (Cor 5.12) do; non-rectifiable (infinite-length) curves without the
  lift are the only possible counterexamples.
falsifies: A non-rectifiable Jordan curve that provably admits a continuous Legendrian
  lift (would narrow the open class), or a rectifiable curve that fails the condition
  (would contradict Cor 5.9).
answers: asano-ike-2024-legendrian-lift-gap
```

```claim
id: asano-ike-2024-cor5-9-rectifiable-square
statement: Every rectifiable Jordan curve inscribes a θ-rectangle for every θ ∈ (0, π);
  in particular, every rectifiable Jordan curve inscribes a square (θ = π/2).
hypotheses:
  - c : S¹ → R² is a Jordan curve with finite 1-dimensional Hausdorff measure (finite
    length).  No further regularity is required.
status: proved-by-source-as-corollary
evidence: Asano–Ike 2024, Corollary 5.9, proved via Proposition 5.8 (p.26) showing
  rectifiable curves satisfy the continuous Legendrian lift hypothesis of Theorem 1.1.
  The proof uses the Riemann mapping theorem, Carathéodory theorem, and
  Riesz–Privalov theorem (smooth approximation of the conformal map from the disk),
  and the classical Green's theorem lemmas for rectifiable curves.
holds-here: yes
bearing: This is the strongest result in the library for the square problem.  Rectifiable
  = finite length, which is an enormous class containing all C¹, piecewise-C¹, Lipschitz,
  locally monotone, and two-graph curves.  It is the first positive answer for all
  rectifiable curves (the paper states: "To the best of our knowledge, this is the first
  result that gives an affirmative answer to the square peg problem for all the rectifiable
  Jordan curves").
falsifies: A rectifiable Jordan curve with no inscribed θ-rectangle for some θ.
contradicts: (none)
follows-from: asano-ike-2024-thm1-1, asano-ike-2024-continuous-legendrian-lift-defn
```

```claim
id: asano-ike-2024-cor5-12-locmon-rectangle
statement: Every locally monotone Jordan curve inscribes a θ-rectangle for every
  θ ∈ (0, π).
hypotheses:
  - c : S¹ → R² is a Jordan curve that is locally monotone (Definition 5.10: for
    every p ∈ R there exists an open connected neighbourhood U_p ⊂ R of p and a
    unit vector v(p) such that q ↦→ c(q)·v(p) is strictly monotone on U_p).
status: proved-by-source-as-corollary
evidence: Asano–Ike 2024, Corollary 5.12, proved via Proposition 5.11 (pp.26-27) showing
  locally monotone curves satisfy the continuous Legendrian lift hypothesis.
holds-here: yes
bearing: This reproves and strengthens Stromquist's 1989 theorem (which proved existence
  of a square for locally monotone curves) to all θ-rectangles.  It is NOT proved via
  Cor 5.9: Proposition 5.11 proves the locally monotone case directly by constructing
  the continuous Legendrian lift from the local strict-monotonicity data (no length
  argument anywhere in §5.3).  The nesting locally monotone ⇒ rectifiable is asserted
  by neither the paper nor any source in the library; the Feller–Golla 2022 note marks
  it UNPROVEN and likely false (point-dependent linear functionals allow unbounded
  winding).  Treat locally monotone and rectifiable as separate classes, both inside
  the Legendrian-lift class.  (Scholar pass, phase 2: corrected a prior digest's
  unstated assumption.)
falsifies: A locally monotone curve with no inscribed θ-rectangle for some θ.
follows-from: asano-ike-2024-thm1-1, asano-ike-2024-continuous-legendrian-lift-defn
```

```claim
id: asano-ike-2024-thm4-1-sheaf-criterion
statement: Let φ be a Hamiltonian homeomorphism with compact support on T*R.
  Consider the Jordan curve C = φ(C₀) where C₀ is the unit circle.  Define
  F_C := K(φ × φ) F_{C₀} ∈ T^η(T*R²).  If
    T_a SS•(F_C) ∩ SS•(F_C) = ∅   for all a ∈ R \ πZ,
  then C inscribes a θ-rectangle for every θ ∈ (0, π).
hypotheses:
  - φ is a Hamiltonian homeomorphism with compact support (equivalently, a compactly
    supported area-preserving homeomorphism; the paper cites Oh 2006, Sikorav 2007
    for the identification).
  - C₀ is the unit circle in R² ≅ T*R.
  - F_{C₀} is the sheaf quantization of C₀ × C₀ constructed in §3.
  - K(φ × φ) is the GKS kernel quantizing φ × φ.
status: proved-by-source
evidence: Asano–Ike 2024, Theorem 4.1 (p.14), proof pp.14-18
holds-here: yes — Thm 4.1 is the central sheaf-theoretic criterion; Thm 1.1 proves its
  hypothesis (the microsupport separation) from the continuous Legendrian lift condition.
bearing: Reduces the existence of an inscribed θ-rectangle to a microsupport-separation
  condition that can be checked via the sheaf quantization of the curve.  The proof of
  Thm 1.1 shows the continuous Legendrian lift hypothesis implies this condition.
falsifies: A Hamiltonian homeomorphism φ such that C = φ(C₀) satisfies the microsupport
  separation but has no θ-rectangle for some θ.
follows-from: (built on Asano–Ike 2023, AI2024, GKS2012, GV2024)
answers: asano-ike-2024-rectifiable-square
```

---

## The continuous Legendrian lift: what it means precisely

Let the base manifold be M = ℝ_x (the real line, identified with the base of the cotangent bundle T*ℝ).  
Under the identification ℝ² ≅ T*ℝ with coordinates (x, ξ) = (x, y), a Jordan curve c : S¹ → ℝ²
writes as c(t) = (x(t), y(t)).  Let e : ℝ → ℝ/2πℤ ≅ S¹ be the universal cover (t mod 2π).

The **Liouville 1-form** on T*ℝ is λ = ξ dx, so for a curve γ : S¹ → T*ℝ,

(γ ∘ e)^* λ = y(t) dx(t)   on ℝ,

where dx(t) = x'(t) dt.  A **primitive** f of (γ ∘ e)^* λ is a function f : ℝ → ℝ such that
df = (γ ∘ e)^* λ; explicitly,

f(t) = ∫₀ᵗ y(s) x'(s) ds   (up to an additive constant).

A smooth curve γ has a smooth primitive f_γ, and the triple (x(t), y(t), f_γ(t)) ⊂
J¹(ℝ) = T*ℝ × ℝ_t is a Legendrian curve in the 1-jet space (the **Legendrian lift**
of γ).

**Continuous Legendrian lift (definition, Asano–Ike §1.1):**  
A Jordan curve c : S¹ → ℝ² admits a continuous Legendrian lift if there exists a sequence
of smooth Jordan curves c_n : S¹ → ℝ² such that

1. c_n → c in C⁰ (uniform convergence), and  
2. the primitives f_n of (c_n ∘ e)^* λ converge uniformly on every compact subset of ℝ
   to a continuous function f : ℝ → ℝ.

The limit f is itself the primitive of (c ∘ e)^* λ in the weak/distributional sense,
and the continuous Legendrian lift is the Legendrian curve (x(t), y(t), f(t)) in J¹(ℝ).

---

## Where the Legendrian-lift hypothesis enters the proof

The proof (p.25, proof of Theorem 1.1) proceeds as follows:

1. **Sheaf quantization of each smooth approximant** (Proposition 5.1): For each smooth
   Jordan curve C_n = c_n(S¹), there is a canonical object F_{C_n} ∈ T^η(T*ℝ²) whose
   conic microsupport SS•(F_{C_n}) equals the Legendrian lift Λ_n of C_n × C_n.

2. **Cauchy sequence** (Proposition 5.1, first part): Under C⁰ convergence of the curves
   with bounded area, (F_{C_n})_n is a Cauchy sequence for the interleaving distance d.
   Completeness (Proposition 2.2) gives a limit object F.

3. **Microsupport estimate** (Proposition 2.3): SS•(F) ⊂ ∩_k ∪_{n≥k} SS•(F_{C_n}).

4. **Primitive convergence ⇒ diagonal separation**: The uniform convergence of the
   primitives f_n → f (condition (2) of Theorem 1.1) forces the limit F to satisfy
   T_a SS•(F) ∩ SS•(F) = ∅ for all a ∈ ℝ \ πℤ.  This is the key step where the
   Legendrian-lift condition enters and the diagonal's contribution to the critical
   values is confined to multiples of π.

5. **Construction of F_C** (Proposition 5.1, second part): If C is the image of the
   unit circle under a Hamiltonian homeomorphism φ (true for any Jordan curve of
   measure zero by Oxtoby–Ulam), then F ≅ K(φ × φ) F_{C₀}, i.e., F is the sheaf
   quantization of C × C.

6. **Apply Theorem 4.1**: The microsupport separation T_a SS•(F_C) ∩ SS•(F_C) = ∅ for
   a ∈ ℝ \ πℤ is exactly the hypothesis of Theorem 4.1, which then guarantees the
   existence of a θ-rectangle for every θ ∈ (0, π).
