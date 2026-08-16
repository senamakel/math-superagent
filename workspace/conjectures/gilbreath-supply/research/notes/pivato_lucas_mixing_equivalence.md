# Lucas mixing ⟺ fold randomization: the weakest-input bridge

Names and proves the *candidate* weakest-input condition (Lucas mixing) behind
run's open request `walsh-spectral-subset-b904`. Does **not** close that request:
this is a measure-level ergodic equivalence, not a Walsh/subset-sum weight bound
on wt(Φ_n h) for a fixed string, and the finite-prefix transfer that would bridge
it is absent (open step below).

## The structural fact (sourced)

Pivato–Yassawi (2006), *Asymptotic randomization of sofic shifts by linear CA*,
arXiv:math/0306136, Theorem 7.1, for Φ = 1+σ (Rule 90) on (Z/p)^s:

> (Φ asymptotically randomizes µ, i.e. Φ^j µ → Haar along a density-one set of
> times j)  ⟺  (µ is Lucas mixing).

Lucas mixing means: for every nontrivial character χ, there is a density-one
H ⊂ N with ⟨χ ◦ Φ^{h·⟨⟨χ⟩⟩}, µ⟩ → 0 as H∋h→∞, where ⟨⟨χ⟩⟩ = p^⌈log_p|[χ]|⌉.
By Lucas' theorem Φ^{⟨⟨χ⟩⟩} = 1 + σ^{⟨⟨χ⟩⟩}, so the h-th fold spreads χ over the
binary-submask (Lucas) unfoldings. So the *weakest* input forcing the fold to
de-randomize toward uniform at density-one times is exactly correlation decay of h
along binary-submask sets.

## Why it bears on (does not close) the run's open question

GOAL priority 2 asks: what is the weakest statement about the primes from which
wt(Φ_n h) ≥ c·n follows? The switch-density reduction is a dead end (its
underlying pair-frequency statement is a named open problem behind the parity
barrier). This paper supplies a structurally different, named, *proved*
candidate: **Lucas mixing of h**. It reads h only along binary-submask sets (which
is exactly what Lucas makes Φ read), it is strictly weaker-sounding than positive
switch density, and the paper proves it is the *sharp* condition for the fold's
randomization in the ergodic limit.

Two support sources:
- Pivato–Yassawi, *Limit measures for affine CA* (arXiv:math/0108082): every
  nontrivial LCA is diffusive, and harmonically-mixing input converges to Haar in
  density. Supplies the harmonic-mixing→randomization half.
- Pivato, *LCA, asymptotic randomization, and entropy* (arXiv:math/0210241):
  entropy of the input is **neither necessary nor sufficient** for
  randomization — the formal refutation of the "h is complicated enough" family
  in ergodic language; the controlling quantity is the finer mixing structure.

## The open step (not in any source)

These results concern measures on infinite configurations converging in the
weak-* topology at density-one *times*, and the statistical law. SUPPLY asks about
a single fixed deterministic string h (the prime gap parities) and a single finite
fold depth n: `wt(Φ_n h) ≥ c·n`. Bridging the two needs a **finite-prefix /
transfer argument**: show (a) the empirical measure of the prime-gap-parity string
is Lucas mixing (a prime-gap correlation statement), and (b) quantitative
(stability) control so that density-one-time convergence of the law implies
density-one-n lower bounds on the actual folded weight of the fixed string. Neither
(a) nor (b) appears anywhere in this library yet. (a) is the arithmetic heart and
is the natural next research request; (b) is a finite linear-algebra/combinatorics
transfer the run's own oracle can attack.

```claim
id: lucas-mixing-iff-fold-randomization
statement: For the fold Φ = 1+σ on (Z/p)^s, Φ asymptotically randomizes µ (Φ^j µ → Haar along a Cesàro-density-one set of times) if and only if µ is Lucas mixing (correlation decay of every character along its binary-submask unfoldings Φ^{h·⟨⟨χ⟩⟩}).
hypotheses: A = (Z/p)^s, s ≥ 1; Φ = 1+σ; µ any probability measure on configuration space; randomization means weak-* convergence along density-one J.
holds-here: Yes for the object — the fold Φ in SUPPLY is precisely the finite version of 1+σ over Z/2, and Lucas' theorem is the engine of both.
status: sourced (Pivato–Yassawi 2006 Thm 7.1)
bearing: Supplies the named weakest-input candidate (Lucas mixing of h). This is NOT a weight bound and does NOT answer the walsh-spectral-subset-b904 request: it is a measure-level ergodic equivalence (weak-* convergence at density-one times) that would only feed SUPPLY through the finite-prefix transfer described above, which is absent. The request remains open. Not itself a proof of SUPPLY — needs the finite transfer.
anchor: research/sources/pivato_yassawi_sofic_randomization.full.md line 1690ff; summaries/pivato_yassawi_sofic_randomization.md
<!-- NOTE: previously this block carried `answers: walsh-spectral-subset-b904`, which per REQUESTS.md mechanism would have marked that request closed. That field is removed as an overclaim: the pivato result is an ergodic equivalence, not a Walsh/subset-sum bound on wt(Phi_n h) for a fixed string, and the required transfer is absent. The request stays genuinely open. -->

```

```claim
id: entropy-neither-necessary-nor-sufficient-for-randomization
statement: For Φ = 1+σ over Z/2, nonzero entropy of the initial measure is neither necessary nor sufficient for asymptotic randomization by Φ.
hypotheses: A = Z/2, Φ = 1+σ, measures on {0,1}^Z.
holds-here: Yes as a refutation fact — it kills the "h is complicated enough" family (GOAL rule) at the level of the fold.
status: sourced (Pivato arXiv:math/0210241 Lemmas 1–6)
bearing: Reinforces the closed-door list; directs attention to the finer Lucas/harmonic mixing structure rather than complexity.
anchor: research/sources/pivato_lca_entropy_randomization.full.md
```

```claim
id: lucas-mixing-is-weakest-for-1-plus-sigma
statement: Among conditions forcing the fold Φ = 1+σ to asymptotically randomize a measure, Lucas mixing is the weakest: the "⇒" direction of Theorem 7.1 makes it a sharp characterization, not merely sufficient.
hypotheses: Same as lucas-mixing-iff-fold-randomization.
holds-here: Yes for the fold.
status: sourced (Pivato–Yassawi 2006 Thm 7.1, "strongest possible extension")
bearing: Means the run's search for a weaker input should target Lucas mixing specifically; a strictly weaker condition would be a new theorem.
anchor: as lucas-mixing-iff-fold-randomization
```
