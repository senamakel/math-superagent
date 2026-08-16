# Scholar pass: the approaches-folder pass, and what it settles

Follows `scholar_pass_new_material.md` (Pivato bridge, fold-rank, RW caveat)
and `scholar_pass_computation_contradictions.md` (R-finite contradiction,
convention collision, single-boundary refutation). This pass covers the
research agent's reformulation/grounding pass — the `research/approaches/*`
files — and the two board lessons (chisel's Lucas-mixing orthogonality, the
adversarial hunch), against GOAL: does the fold `Φ` do work the switch-density
form cannot see?

## What the new material is

Eight approach files and a consolidated `precedent_grounding_report.md`.
Verdicts are already written inside each file; this note is the digest that
indexes them and says what each settles for the run.

## One adopted route (live), nine dead/ungrounded

**LIVE — `lucas-mixing-finite-transfer` (adopted).** Reformulates SUPPLY as the
finite deterministic instance of Pivato–Yassawi 2006 Thm 7.1 (Φ=1+σ randomizes µ
iff µ is Lucas mixing). It does NOT prove SUPPLY: (a) the empirical measure of the
prime gap-parity string being Lucas mixing is unproved (a pure correlation-decay
statement along submask unfoldings), and (b) the finite-prefix transfer
(density-one-time law convergence ⇒ wt(Φ_n h) ≥ c·n for the fixed string) is
absent. Both halves are named as open.

**Refuted, each with a `killed-by`:**
- `kummer-2adic-lift` — the 2-adic valuation of a difference is NOT a function
  of the operands' valuations (cancellation depends on the 2-adic *residue* of
  the ratio), so the advertised "valuation propagation from initial gap
  valuations" is unrealisable; the lift re-derives ν₂=wt(Φ_n h) with no new
  tractable invariant.
- `mahler-2kernel-automaticity` — step (a), "density-1 sparse window ANF ⇒
  finite 2-kernel", is not a theorem and does not follow; and the non-automaticity
  of the prime *indicator* does NOT transfer to the *by-index gap-parity string*
  h (no source proves THIS string non-automatic). The mechanism asserts its own
  conclusion to sidestep the e_{2^m} witness.
- `walsh-subset-sum-fold-structure` — the Walsh identity is correct but a
  Φ-alone bound cannot hold: door-4 balanced anti-dyadic strings are in the
  candidate's own admissible class yet have wt(Φ_m h)∈{1,2}; kernel vectors kill
  it. Near-injectivity bounds the kernel, not the image weight.
- `hypergraph-cut-cheeger` — false kernel premise (d=0 singleton edge; operative
  ker = span(even-alt, odd-alt), not span(all-ones)); plus all hypergraph Cheeger
  inequalities are k-uniform while the fold's hypergraph has edge sizes 1..n, and
  the Cheeger constant is ~1/n.
- `diagonal-2regular-automaton` — Rampersad–Wiebe's transform is a scalar
  run-length product of a fixed recurrence, not SUPPLY's vector-in-d submask-XOR
  fold (claims `rw-not-the-submask-xor-fold`); and the prime-driven coefficient
  string is non-automatic, so ν₂(n) is not a finite-state function of n.

**Grounded identity but payoff ungrounded:**
- `anf-mobius-reed-muller` — the dictionary is real and correct: T(n,d) = a_d,
  the ANF/Möbius coefficient of the reversed window. Verified here by hand on
  n=4 (d=1,2,3 all match), consistent with `supply-fold-submask-zeta-involution`.
  But no source bounds sliding-window ANF-*support* (the RM weight spectrum is
  itself open), so the identity is a change of language, not of ground.
- `pascal-cascade-block-recursion` — block recursion is grounded for the full
  Pascal matrix rows but ungrounded for the anti-diagonal slice Φ_n that SUPPLY
  uses; the diagonal sequences are the 2-regular binomial sequences, so the
  dyadic hope is already housed in the (refuted) 2-regular route.

## Board lessons (asserted, not established)

- **chisel (precision correction).** Lucas mixing does NOT constrain the
  single-site marginal: for µ=Bernoulli(ρ), ⟨χ∘Φ^{h·⟨⟨χ⟩⟩},µ⟩=(1−2ρ)^{|K|·…}→0
  for every ρ∈(0,1) as wt(h)→∞. So "the prime string is Lucas mixing" is
  ORTHOGONAL to mod-4 switch density (a pattern-correlation statement, not a
  mean statement) and does not inherit the ABGS switch-side dead end. Earlier
  pricing of Lucas mixing as "weaker or harder than" switch density should read
  "orthogonal to the mean." The decay exponent is asserted; the qualitative
  conclusion (|1−2ρ|<1 for ρ∈(0,1)) is checked arithmetic.
- **adversarial hunch (three reformulations).** ANF/Reed–Muller, dyadic cascade,
  and hypergraph each change coordinates; none opens the closed "h is
  complicated" family by itself.

## The one remaining verification gap in the adoption chain

`code/out/anf_dictionary_check.py` (checks T(n,d)==a_d for n=3..40 and the
all-ones ANF-support=1 negative control) is **written but not yet executed** —
no execution tool in the research role. My hand-check of n=4 confirms the
identity on the smallest nontrivial case, but the n=3..40 sweep and the negative
control remain un-run. tool_builder must execute it before the ANF dictionary is
leaned on.

## What this run still lacks (unchanged, now with the route count)

The single live route is `lucas-mixing-finite-transfer`; its two halves — (a)
the prime string's empirical measure is Lucas mixing, (b) a quantitative
finite-prefix transfer — are both absent. The run now has a full account of nine
approaches (one adopted, eight dead/ungrounded) and can stop re-deriving them.

```claim
id: lucas-mixing-orthogonal-to-switch-density
statement: Lucas mixing does not constrain the single-site marginal: for the i.i.d. measure Bernoulli(rho), the finite-character expectation <chi o Phi^{h<chi>}, mu> = (1-2rho)^{|K| * p^{wt_p(h)}} tends to 0 along the density-one set {h : wt_p(h) -> inf} for every rho in (0,1). Hence "the prime gap-parity measure is Lucas mixing" is a pattern-correlation statement ORTHOGONAL to mod-4 switch density (a mean statement), and pricing it as "stronger or weaker than" switch density is wrong.
hypotheses: Phi = 1+sigma over (Z/p)^s; chi a nontrivial finite character; |1-2rho| < 1 for rho in (0,1).
holds-here: yes — every rho in (0,1) gives |1-2rho|<1, so the decay holds without knowing the prime string's mean.
status: asserted on the board (chisel lesson), decay-exponent arithmetic checked; not yet a written claim in a note with a formal derivation.
bearing: frees step (a) of lucas-mixing-finite-transfer from the ABGS switch-side dead end; directs the finite-transfer search at correlations, not the mean.
anchor: teams/BOARD.md (chisel lesson); research/approaches/lucas-mixing-finite-transfer.md
```

```claim
id: kummer-2adic-valuation-lift-refuted
statement: The 2-adic valuation of A_k(i) = |A_{k-1}(i) - A_{k-1}(i+1)| is NOT a function of the two operands' valuations alone: under the ultrametric law the cancellation case v2(a)=v2(b) gives v2(a-b) its value from the 2-adic RESIDUE of a/b, not from v2(a),v2(b). So the proposed "explicit valuation propagation from initial gap valuations" of the Kummer 2-adic lift is unrealisable; the lift re-derives the same count nu2 = wt(Phi_n h) with no new tractable invariant, and cannot read prime-gap 2-adic structure through a clean fold.
hypotheses: the absolute-difference triangle recursion; standard 2-adic ultrametricity.
holds-here: yes — this is the canonical obstruction to a valuation-only recursion (Odlyzko 1993 resists precisely this).
status: refuted (approach file killed-by; literature: Odlyzko 1993, standard 2-adic analysis).
bearing: closes the Kummer/2-adic-lift route as a sixth-class dead end; the 2-adic bit of gap magnitude is not separable by a cell-valuation propagation.
anchor: research/approaches/kummer-2adic-lift.md
```

```claim
id: mahler-2kernel-contrapositive-refuted
statement: "Small nu2(n) (sparse window ANF) on a density-1 set forces the 2-kernel of the infinite gap-parity string to be finite (hence 2-automatic)" is not a theorem and does not follow: the 2-kernel span is a rigid GLOBAL condition on the single infinite string, while small nu2(n) only constrains individual local windows; the e_{2^m} amplification witness shows sparse window structure coexisting with linear fold weight. Nor is the by-index prime GAP-parity string known non-automatic (only the prime INDICATOR is, by Hartmanis-Shank/Coons/Dubbe).
hypotheses: Mahler/Christol finite-2-kernel <=> 2-automatic (real); non-automaticity of the prime indicator (real); the transfer step (a) is the unsupported one.
holds-here: yes — both refutation points hold; step (c) is additionally overclaimed for the gap string specifically.
status: refuted (approach file killed-by), the constituent pieces sourced.
bearing: kills the contrapositive route; the gap-parity string's automaticity is unproved and must not be assumed in any other argument.
anchor: research/approaches/mahler-2kernel-automaticity.md
```
