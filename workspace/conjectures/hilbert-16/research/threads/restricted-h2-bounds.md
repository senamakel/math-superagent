# Thread: restricted H(2) bounds — Ilyashenko–Llibre (held) and Fishkin (constants gap)

```thread
question: What are the exact numerical constants in Fishkin 2010 Theorems 1 and 2 (Trans. Moscow Math. Soc. 71, DOI 10.1090/s0077-1554-2010-00181-1)? The held claim fishkin-perturbed-center-quadratic-bound states the theorem structure (confirmed by the OpenAlex abstract) and explicitly records the constants as unverified. Earlier run reports quoted 10⁷² / 10⁷⁷ / δ^{−33} without any held source containing them — those figures are UNVERIFIED and must not be repeated as fact.
status: open
rests-on: fishkin-perturbed-center-quadratic-bound, ilyashenko-llibre-restricted-h16-quadratic-bound
blocked-by: Fishkin full text not held (AMS free-archive PDF returned 429 rate-limit on three attempts this cycle; CiteSeerX doi 10.1.1.309.2425 unreachable; MathSciNet paywalled; Semantic Scholar has no abstract)
next: retry the AMS free-archive PDF (vol 71 is >5 years old, so retrieval is legitimate) when the server allows; verify or strike the quoted exponents; upgrade the claim's holds-here to yes with a primary-text anchor. Also: clean-room re-derivation of Ilyashenko–Llibre Lemma 10's seven-jet Bautin decomposition (Mathematica-computed in the paper) is the check that keeps that claim from resting on an unverified computation.
```

## What is established (verified against held sources)

**Ilyashenko–Llibre 2010, Theorem 5** (full text held,
`research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md`
lines 113–122): for any δ, σ, κ ∈ (0, 0.1), the number of δ-tame limit cycles
of a normalized quadratic field that is σ-distant from centers and κ-distant
from singular quadratic fields is at most

    H(2,δ,σ,κ) = |log σ| · exp(exp(10²⁵ · δ^{−31} · κ^{−2})).

The appendix (lines 633–698) carries the explicit **Bautin-ideal seven-jet
decomposition** of the displacement at a centre (Lemma 10, lines 275–288):
a₁≡1, a₂≡0, a₃=α₀g₂, a₄=α₁g₂, a₅=β₀g₃+β₁g₂, a₆=β₂g₃+β₃g₂,
a₇=γ₀g₄+γ₁g₃+γ₂g₂, with α₀=−2π, β₀=−2π/3, γ₀=−5π/4. Caveat: Lemma 10 was
computed with Mathematica; clean-room re-derivation pending.

**Fishkin 2010** (abstract-level only): the OpenAlex abstract confirms the
theorem structure (Theorem 1: δ-good limit cycles of a quadratic field with a
perturbed center-like singular point, κ = distance to fields with a line of
singular points; Theorem 2: uniform bound dropping the center-distance
assumption, complementing Ilyashenko–Llibre). The constants are NOT in any
held source.

## Why this thread matters

These are the only two known uniform restricted bounds on H(2) of their kind
(the authors' own framing: "the only known estimate of this kind"). They
bound δ-tame/δ-good cycles away from the DRR-graphics regime (σ,κ → 0, δ → 0),
so they do not touch H(2) < ∞ — but they are the quantitative shadow of the
finite-cyclicity obstruction, and the seven-jet Bautin decomposition is direct
primary evidence for the run's Bautin-ideal Lean work
(`code/lean/Lib/Bautin.lean`).
