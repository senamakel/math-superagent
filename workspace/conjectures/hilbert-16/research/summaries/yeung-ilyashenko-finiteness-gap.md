# Yeung 2024 — a claimed gap in Ilyashenko's Dulac proof

Full text: [[yeung-ilyashenko-finiteness-gap.full]]. arXiv:2402.12506; peer-reviewed
2025 as "Dulac's Theorem Revisited", Qual. Theory Dyn. Syst. 24, Art. 57.

## What the source establishes

The **theorem** (finite limit cycles for a fixed field) is NOT claimed false. What
is contested is the completeness of **Ilyashenko's proof** for the case of
polycycles containing non-hyperbolic (semi-hyperbolic) equilibria. The gap is in
the step that proves the asymptotic classes in the logarithmic chart are
orderable / admit leading terms (the "ordering of asymptotics", needed to prove
the return map is trivial if its expansion is).

**The counterexample.** Yeung builds a polycycle (4 equilibria) with prescribed
transit maps, giving a return map whose logarithmic-chart form forces an element
of FC^{1,1}, and shows that for k₁, k₂ ∈ K_{1,1} from the example,
**k₂'k₁ − k₁'k₂ ∉ K_{1,1}** — contradicting the claim (Ilyashenko, p.198) used to
prove ordering. Also k₁k₂ ∉ K_{1,1} (not a differential algebra). The normal forms
show the leading-term argument fails because the generalized exponent does not go
to −∞.

**Hypotheses / limits of validity.** The difficulty is confined to non-hyperbolic
polycycles (semi-hyperbolic equilibria, e^{−1/z}-type transit maps, the m_α
multiplications for α≠1 that produce the deeper FC^{1,p} levels). The **hyperbolic**
case stands: Yeung's own introduction ("hyperbolic polycycles ... up to date the
only result that has not been questioned"), and Statement 2.4 shows the proof works
cleanly when every equilibrium is orbitally equivalent to {ẋ=x², ẏ=−y}.

**Status.** This is a live, recent contention (2024/25), 0 citations in the 2024
preprint, now peer-reviewed. Ilyashenko published a "digest of the revised proof"
(Izvestiya Math. 2016). The community may not yet have adjudicated.

## What it lets this run conclude

- The frame's pointwise-finiteness pillar is "settled modulo a contended proof".
- It does NOT change the DRR finite-cyclicity program (which is about uniformity,
  a different question), nor the elementary-polycycle results (Ilyashenko–
  Yakovenko / Kaloshin, hyperbolic — undisputed).
- It sharpens the smooth-test / gap-locating task: the quasi-analyticity step
  (trivial expansion ⇒ trivial map) is precisely where Dulac erred, and Yeung
  claims Ilyashenko's repair of it is itself incomplete for semi-hyperbolic
  vertices. A candidate argument for a degenerate graphic must locate where
  quasi-analyticity / almost-regularity is used.

```claim
id: h16-dulac-proof-contested
statement: The published proof (Ilyashenko's approach) of finiteness of limit
  cycles for the non-hyperbolic-polycycle case has a gap: the argument that the
  asymptotics admit proper leading terms (ordering) is insufficient, with an
  explicit counterexample (k2'k1 - k1'k2 notin K_{1,1}). The theorem is not
  claimed false; the hyperbolic case and Ecalle's route are not questioned.
hypotheses: semi-hyperbolic equilibria in the polycycle; 2024 preprint, now
  peer-reviewed (2025).
holds-here: unchecked -- live contention the run must report, not resolve.
status: asserted
bearing: the pointwise-finiteness pillar is contested at exactly the
  quasi-analyticity step; locates where an argument for a degenerate graphic
  must genuinely use analytic structure.
anchor: research/sources/yeung-ilyashenko-finiteness-gap.full.md
contradicts: h16-dulac-finiteness-individual (only the proof, not the statement)
```
