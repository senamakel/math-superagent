# Lucas mixing ⟺ fold randomization: finite transfer to SUPPLY

```approach
idea: Reformulate SUPPLY as the finite deterministic instance of Pivato–Yassawi's
      theorem "Φ = 1+σ (Rule 90) asymptotically randomizes a measure µ iff µ is
      Lucas mixing" (arXiv:math/0306136, Thm 7.1). This is a change of
      representation from the switch-density character sum to an ergodic /
      measure-theoretic one: the fold is attacked through its sharp
      randomization characterization, not through prime-pair residue frequency.
mechanism: Lucas' theorem makes the fold Φ read h along binary submask sets,
      which is exactly the correlation structure Pivato–Yassawi prove is the
      sharp condition for the fold to drive every character toward Haar. SUPPLY
      asks about a single fixed deterministic string h (prime gap parities) and
      a single finite depth n, so the bridge needs (a) an arithmetic statement
      that the empirical measure of h is Lucas mixing (correlation decay of
      every character along its binary-submask unfoldings) and (b) a
      quantitative finite-prefix transfer from density-one-time law convergence
      to a density-one-n lower bound wt(Φ_n h) ≥ c·n. Part (a) is a pure
      correlation-decay statement along binary-submask unfoldings — ORTHOGONAL
      to the mod-4 switch-density mean (Bernoulli(ρ) is Lucas mixing for every
      ρ, see precision note) — and reads h only where Lucas makes Φ read it;
      part (b) is pure finite linear algebra.
status: grounded (theorem real & precisely stated, Pivato–Yassawi Thm 7.1; hypotheses hold here — SUPPLY's fold is the finite 1+σ over Z/2 and Lucas is its engine. The open content is the finite transfer step (a)+(b): lucas-mixing of the prime gap-parity string and the quantitative density-one transfer are NOT in any source and remain open. Step (a) is orthogonal to the mod-4 switch-density mean — Bernoulli(ρ) is Lucas mixing for every ρ — so it does not inherit the ABGS dead end, but it is an unestablished correlation-decay statement on the primes, not a theorem.)
precedent:
  - "Pivato & Yassawi, Asymptotic randomization of sofic shifts by linear
     cellular automata (2006), arXiv:math/0306136, Theorem 7.1: for Φ=1+σ and
     A=(Z/p)^s, (Φ asymptotically randomizes µ along a density-one Cesàro set) ⟺
     (µ is Lucas mixing)."  https://arxiv.org/pdf/math/0306136
  - "Pivato, Linear CA, asymptotic randomization, and entropy, arXiv:math/0210241:
     positive entropy of µ is neither necessary nor sufficient for
     randomization by Φ=1+σ."  https://arxiv.org/abs/math/0210241
  - "Takei, Limiting measures for addition modulo a prime CA, IJNC 7 (2017):
     rigidity of Λ-invariant measures; uniform is the only invariant measure in
     the strong-mixing class — the ergodic sibling of the 'no structural
     invariant' obstruction."  https://doi.org/10.15803/ijnc.7.2_124
  - claims: lucas-mixing-iff-fold-randomization (sourced), entropy-neither-
    necessary-nor-sufficient-for-randomization (sourced), lucas-mixing-is-
    weakest-for-1-plus-sigma (sourced) — all in
    research/notes/pivato_lucas_mixing_equivalence.md
killed-by:
open-step: the finite transfer (a)+(b). No source supplies it. (a) asks whether
      the prime gap-parity string's empirical measure is Lucas mixing — a
      correlation-decay statement along binary-submask unfoldings. By the
      precision note below, this is ORTHOGONAL to the mod-4 switch-density mean
      question (Bernoulli(ρ) is Lucas mixing for every ρ), so (a) does NOT
      inherit the ABGS switch-side dead end. (b) is a finite quantitative
      transfer not in the CA-mixing literature, whose hypotheses (stability /
      cylinder approximation, quantitative Cesàro) must be stated precisely
      before it can be attacked. Neither is closed; the approach is adopted as a
      named reformulation with a real sharp theorem and a freed arithmetic step,
      but it does NOT yet prove SUPPLY.
first-step: Build the finite shadow of Lucas mixing, averaged form first. (1) The
      Walsh identity wt(Φ_n h) = (n−2)/2 − (1/2)Σ_{d=2}^{n−1} (−1)^{T(n,d)} is the
      exact bridge: M(N) = (1/N)Σ_{n≤N} ν₂(n)/n → 1/2 iff the Cesàro character sum
      (1/N)Σ_{n≤N} (1/n)Σ_d (−1)^{T(n,d)} → 0. (2) Lucas mixing is the ergodic
      statement that these character correlations ⟨χ∘Φ^{h⟨⟨χ⟩⟩}, µ⟩ → 0; its finite
      shadow is a variance/autocorrelation bound on (−1)^{T(n,d)} over the (n,d)
      submask windows of the fixed prime string h. (3) tool_builder, with the
      existing oracle (n ≤ 8000): compute (i) the submask-window autocorrelation of
      the prime h, (ii) the running Cesàro character sum above, (iii) the same for
      all-ones (→0) and Thue-Morse (decay) as negative controls. The transfer lemma
      to prove is: submask-window correlation decay ⇒ the Cesàro character sum → 0 ⇒
      ν₂(n) ≥ c·n on a density-1 set — GOAL priority 1 in Lucas-mixing coordinates.
      Step (a) is the arithmetic heart: price whether the primes' submask-window
      correlations decay (a pure correlation statement, orthogonal to switch density —
      see the precision note below).
```

## Why it is distinct

This is the *ergodic* route: it reformulates SUPPLY through a theorem whose
hypotheses the fold satisfies by construction, and shifts the number theory
onto a correlation-decay statement along submask sets (which is what Lucas makes
Φ read) rather than adjacent-pair switch frequency.

## Precision gained by reading the definition (post-research, 2026-02)

Lucas mixing does **not** constrain the single-site marginal. For the i.i.d.
measure µ = Bernoulli(ρ), the expectation over the finite character χ (nontrivial
on K, |[χ]| = S) is

⟨χ∘Φ^{h·⟨⟨χ⟩⟩}, µ⟩ = (1−2ρ)^{|K|·p^{wt_p(h)}}  →  0

along the density-one set {h : wt_p(h) → ∞}, for **every** ρ ∈ (0,1). Hence
Bernoulli(ρ) is Lucas mixing for every mean ρ. The condition is therefore
**orthogonal to switch density**, not stronger than it: it tests pattern
correlations, the mod-4 switch-density reduction tests the mean, and neither
implies the other. (Deduction, standard; Thm 7.1 then gives the consistent
conclusion that Φ asymptotically randomizes Bernoulli(ρ) for every ρ ∈ (0,1),
matching the direct computation Φ^j Bernoulli(ρ) = Bernoulli(2ρ(1−ρ)) → Haar.)

Consequence for step (a): "the prime string's limiting empirical measure is
Lucas mixing" is a pure correlation-decay statement along submask windows. It
does **not** reopen the ABGS switch-density dead end and does not require the
parity barrier's mean question to be resolved — that is precisely what makes
candidate 1 a genuine escape from the dead-end reduction rather than a relabel
of it. The earlier phrase "strictly weaker-sounding" should read "orthogonal to
the mean." The hard, still-absent content remains the finite-prefix transfer (b),
and the averaged form is where it is most likely to close (GOAL priority 1).

## Literature verdict (research specialist, 2026-02)

- **The theorem is real and precisely stated as above**; its hypotheses hold
  here because SUPPLY's fold is exactly the finite version of 1+σ over Z/2 and
  Lucas' theorem is the engine of both.
- **Applied to the primes?** No. Searches returned the CA-mixing literature
  (Pivato–Yassawi, Pivato, Takei, Maass–Martínez–Pivato, subgroup-shift
  generalisation) and the prime-residue literature (Lemke Oliver–Soundararajan,
  ABGS, Shiu, Maynard), but no paper connects the two. Lucas mixing of the prime
  string is not established anywhere.
- **The open content is the finite transfer**, which is not in any source. Being
  honest: the step (a) is a new correlation statement on the primes and is not
  established anywhere; it is, however, orthogonal to the switch-density mean
  (see precision note), so the ABGS switch-side gap does not automatically
  subsume it. The approach buys a *named, sharp target* for the weakest-input
  question, not a proof.
