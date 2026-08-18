# Ueoka 2025 v5 — full text verdict: the claimed proof does not establish the conjecture

**Source:** Yoshiki Ueoka (with AI support Gemini/ChatGPT), "The Proof of the Inscribed Square Problem using Topological Degree," Zenodo record 17847990, v5, dated 7 Dec 2025. **Full PDF text now on disk** at `research/sources/ueoka-2025-v5-toeplitz-proof.pdf.full.md` (converted from the 62.5 kB PDF; record landing page at `research/sources/ueoka-2025-zenodo-degree-proof.full.md`).

**This is the only full-proof claim for the Toeplitz conjecture in existence, and it is now held in the library with its actual argument, not just its abstract. Verdict: the argument as written does not prove the claim.** The gap is not in the AI-assistance or the self-publishing; it is a mathematical gap in the two steps the library already identified as the unsolved core.

## The argument, in brief (v5)

1. **§1.** T⁴ = ordered quadruples 0 ≤ t₁ < t₂ < t₃ < t₄ ≤ 1; F : T⁴ → R⁴ with components (ℓ₁₂−ℓ₂₃, ℓ₂₃−ℓ₃₄, ℓ₁₃−ℓ₂₄, ℓ₁₃²−2ℓ₁₂²), ℓᵢⱼ = ‖γ(tᵢ)−γ(tⱼ)‖. A zero of F is a square (equal sides, equal diagonals, diagonal² = 2·side²).
2. **§2.** Approximate γ₀ by C¹ curves γₙ, uniform convergence ‖γₙ−γ₀‖∞ → 0, hence Fₙ → F₀ uniformly (Lemma 2.1, correct: |ℓ⁽ⁿ⁾−ℓ⁽⁰⁾| ≤ 2‖γₙ−γ₀‖∞).
3. **§3.** Lemma 3.1: Fₙ ≠ 0 on ∂T⁴ — **this lemma is FALSE as stated.** At the all-coincident boundary point t₁ = t₂ = t₃ = t₄ = t, we have p₁ = p₂ = p₃ = p₄ = γ(t), so every ℓᵢⱼ = 0 and F(t,t,t,t) = (0,0,0,0) **identically, for every curve γ**. The paper's proof of Lemma 3.1 says "if Fₙ(t) = 0, all side lengths must be equal and non-zero, leading to a contradiction since at least one side length must be zero" — but F = 0 is satisfied by *all side lengths equal and zero* as well as all-equal-and-nonzero; the word "non-zero" is smuggled in with no justification. The all-coincident point is exactly the degenerate square-shrunk-to-a-point configuration that Shnirelman/Stromquist/Matschke/CDM all handle with care (Stromquist's Q simplex, the mod-2 degree on a vertex-neighborhood cover, the size ≥ µ parameter bound). The paper never addresses it.
4. **Lemma 3.2 (the fatal step):** claims a uniform positive margin ε > 0 on ∂T⁴ for all Fₙ. Proof: "F₀ continuous, non-zero on compact boundary ∂T⁴, attains minimum m₀ > 0; by uniform convergence...". **The claimed m₀ > 0 is false**: F₀ vanishes at the all-coincident boundary point (Lemma 3.1's failure), so min over ∂T⁴ of ‖F₀‖ = 0. The positivity of the margin is *the* claim that needs proving — it is the claim that the boundary winding number is well-defined and nonvanishing for the wild curve γ₀, which is precisely the step Stromquist's local monotonicity and Asano–Ike's Legendrian-lift hypothesis exist to guarantee. The paper asserts it from continuity alone, which is false: F₀ does vanish on the boundary (at the diagonal point), and the whole degenerate locus needs control.
5. **§4. Lemma 4.1 (second fatal step):** claims δ > 0 with dist(Z(Fₙ), ∂T⁴) ≥ δ for all n. Proof: "if zero points approached the boundary, uniform convergence would imply F₀(t∗) = 0, contradicting the boundary non-zero property." **This is a non sequitur**: uniform convergence Fₙ → F₀ says nothing about the *locations* of zeroes; a sequence of interior zeroes can converge to a boundary point t∗ without F₀ vanishing at t∗ (F₀ need not vanish anywhere near the boundary for the Fₙ zeroes to drift there). Moreover the "boundary non-zero property" it cites is Lemma 3.1, which is false. The claimed "stay away from the boundary" is exactly the anti-shrinkout conclusion — a square with side → 0 has parameters approaching the diagonal t₁=t₂=t₃=t₄, and the whole literature (Tao shrinkout; GL 2024 sharpness) says this can happen. The paper proves it by assertion.
6. **§5. Theorem 5.1** then concludes deg(F₀) = deg(Fₙ) ≠ 0. The C¹ case is cited as "known" ([1] "Pugh 2009 preprint," [2] Shnirelman 1944) but **no nonzero-degree statement for F on T⁴ is established for the C¹ case either** — the standard arguments (Stromquist, Matschke, CDM) work on the *Möbius band* or the closed simplex Q with the degenerate point *removed/controlled*, not on the open simplex T⁴ with this F; the degree of F on T⁴ as defined is not shown to be nonzero (indeed F vanishes at the diagonal point, so the degree is not even defined there without excision), and Lemma 3.3's "Degree Stability" inherits both gaps.

**The reference list is unreliable.** [3] "Stromquist, W. (1989). Inscribed squares and continuous curves. Amer. Math. Monthly 96(6): 521–523" is **wrong**: that is the citation for a *different* paper — Stromquist's actual square-peg paper is "Inscribed squares and square-like quadrilaterals in closed curves," Mathematika 36(2) 1989, 187–197 (in this library via its Cambridge abstract + Rius thesis exposition + Matschke/Barber). [1] "Pugh 2009, The Inscribed Square Problem, a preprint" is not in any standard bibliography this library holds. This alone would disqualify the preprint from being a reliable reference source, independent of the mathematical gaps.

## Verdict, stated exactly

- **The v5 proof does not establish the Toeplitz conjecture.** Lemma 3.1 is *false as stated* — F vanishes identically at the all-coincident boundary point (t,t,t,t), since all ℓᵢⱼ = 0 there. Lemma 3.2's uniform positive boundary margin then cannot hold (min over ∂T⁴ of ‖F₀‖ = 0), and its positivity is the exact claim that local monotonicity / Legendrian-lift hypotheses exist to guarantee. Lemma 4.1 infers boundary-separation of zeroes from uniform convergence, which is invalid and is precisely the shrinkout phenomenon. The degree argument on the open simplex T⁴ is not the standard Möbius-band argument and its nonzero-degree premise for the C¹ case is not established (F vanishes at the diagonal point, so the degree needs excision there).
- **It is not a counterexample to the conjecture either** — it contains no construction of a curve without an inscribed square.
- **The claim is closed as "unvalidated and, on the evidence of the full text, incorrect in the steps that matter."** This is now a *documented* verdict from the primary text, not a guess: the library can name the exact sentences where the argument fails and why.
- **It confirms the run's structural thesis from the primary-text side:** the obstruction is exactly the boundary-margin and anti-shrinkout steps; the general conjecture remains open.

## Claim blocks

```claim
id: ueoka2025-v5-proof-fails-at-boundary-margin
statement: Ueoka's v5 (Dec 2025) claims a C⁰ proof via uniform approximation + Brouwer degree on T⁴, but Lemma 3.1 is false as stated (F vanishes identically at the all-coincident boundary point (t,t,t,t) since all ℓᵢⱼ = 0 there), so Lemma 3.2's uniform positive boundary margin cannot hold — its positivity is the exact claim that local monotonicity / Legendrian-lift hypotheses exist to guarantee — and Lemma 4.1 (zeroes stay away from the boundary) infers boundary-separation from uniform convergence, which is invalid and is exactly the shrinkout phenomenon. The degree argument on the open simplex T⁴ is not the standard Möbius-band argument and its nonzero-degree premise for the C¹ case is not established. The reference list mis-cites Stromquist 1989 (gives the wrong journal/paper). Verdict: the argument as written does not establish the conjecture.
hypotheses: none — a mathematical assessment of a claimed proof.
holds-here: yes — closes the only full-proof claim in existence as incorrect-in-the-steps-that-matter, from the primary text now on disk.
evidence: full PDF text verified (Zenodo 17847990 v5); the all-coincident boundary computation F(t,t,t,t) = 0 checked directly; the named lemmas read verbatim.
status: derived verdict (checked against the primary text and the known literature)
falsifies: a corrected version of Ueoka's proof that proves Lemma 3.2's positivity from the actual hypotheses without extra regularity; or a published expert endorsement showing the argument is valid.
```

```claim
id: ueoka2025-mis-cites-stromquist
statement: Ueoka's reference [3] attributes the square-peg result to "Stromquist, Inscribed squares and continuous curves, Amer. Math. Monthly 96(6):521–523 (1989)" — the correct citation is Stromquist, "Inscribed squares and square-like quadrilaterals in closed curves," Mathematika 36(2):187–197 (1989); the Monthly citation is a different paper and the reference list is unreliable.
hypotheses: none.
holds-here: yes — a documented citation error in the only full-proof claim; strengthens the verdict.
evidence: library's own Stromquist record (Cambridge abstract, DOI 10.1112/S0025579300013061) vs the v5 PDF's reference [3].
status: verified discrepancy (primary texts compared)
falsifies: evidence that Stromquist published the square-peg theorem in the Monthly 96(6) 1989.
```
