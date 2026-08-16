# Ducci / 2-adic collapse: gap MAGNITUDE, the resource the linearisation discards

```approach
idea: >
  Every route so far lives entirely in F2: result 1 (linearisation) turns nu2(n)
  into wt(Phi_n h), a function of the gap-PARITY string h alone, and the whole
  run has priced inputs on h. That is not forced. nu2(n) counts actual 2s in the
  maximal {0,2} suffix of the integer absolute-difference triangle, and the
  LENGTH of that suffix — hence an upper bound on where the 2s can live — is
  controlled by the MAGNITUDES of the prime gaps, which the parity reduction
  throws away. The classical theory that governs "when does the absolute-
  difference (Ducci) system reach its eventual {0,c} state" is the Ducci
  sequence classification (Ciamberlini-Marengoni 1937; Ehrlich 1990), and the
  recent Chase-Hunter-Tao inverse theorem for the Cramer model (arXiv:2607.08712,
  already on disk) names exactly the obstructions: long zero blocks and shallow
  {0,lambda} blocks. Small gaps collapse the triangle fast (Ducci), a long
  suffix contains ~half 2s (the settled surjectivity/rank fact), and gap sizes
  ~ log n are a provable/measurable input strictly weaker than mod-4 switch
  density. This is a change of representation back to the INTEGER triangle, the
  one object result 1 is a theorem about.
mechanism: >
  Two named engines, used together. (1) DUCCI/GILBREATH COLLAPSE: the non-cyclic
  absolute-difference map x_i -> |x_i - x_{i+1}| converges to a 2-periodic state
  whose entries are 0 or a fixed value c, with c and the convergence depth
  determined by the 2-adic structure and SIZE of the initial data (Ehrlich 1990
  for the cyclic game; the Gilbreath triangle is the non-cyclic slice, and
  Chase-Hunter-Tao 2026 gives the deterministic inverse theorem in the Cramer
  model). Concretely: if every initial gap is <= B then after O(log B) rows every
  entry is small, so the {0,2} suffix begins early; the primes' gaps average
  log n, so the collapse depth is O(log log n), leaving a suffix of length
  n - O(log log n). (2) HALF THE SUFFIX ARE 2s: within the {0,2} suffix the
  count of 2s equals wt(Phi_n h) (result 1), and wt(Phi_n h) ~ (n-2)/2 is the
  settled fair-model fact (rank Phi_n = n-2, surjectivity, exact Binomial) for
  any h that is not in the two-dimensional kernel collapse. The combined claim:
  suffix length >= c n (a MAGNITUDE statement about gap sizes) and the kernel
  coordinates of the prime h are o(n) (measurable, already computed) together
  give nu2(n) >= c' n. The arithmetic input is now "gaps are small / have bounded
  moments", a statement about gap SIZE, not about the mod-4 switch frequency —
  the reduction that was a dead end (positive switch density, ABGS 2011 §9).
status: refuted
killed-by: >
  Refuted on evidence, not on absence. Two grounds, each sufficient. (1) THE
  ROUTE RE-IMPORTS THE CLOSED kummer-2adic-valuation-lift OBSTRUCTION UNDER A
  DUCCI NAME. The library already refuted the "gap magnitude / 2-adic
  valuation is an independent coordinate the parity reduction discards" idea:
  the 2-adic valuation of a difference is NOT a function of the valuations of
  the two operands (ultrametric cancellation is residue-dependent), so the
  advertised explicit propagation from initial gap magnitudes "re-derives the
  same count with no new tractable invariant" (research/approaches/
  kummer-2adic-lift.md, killed-by). Candidate 1 proposes exactly that
  magnitude-as-independent-resource move under the Ducci umbrella; the refuted
  obstruction applies unchanged. (2) MAGNITUDE IS NOT AN INDEPENDENT CONTROL OF
  nu2 GIVEN THE HELD LINEARISATION. The operative identity (claim
  linearisation-fold-weight, problem.md fact 1, machine-consistent with the
  oracle and the excess identity) pins nu2(n) = wt(Phi_n h) as a PURE function
  of the gap-parity string h. If that holds, then whatever the gap magnitudes
  do to the count of 2s in the {0,2} suffix is already encoded in h; a magnitude
  input is at best a proxy for a parity statement, so it is not a strictly
  weaker arithmetic demand. (3) THE OBJECT MISMATCH. The named engines are real
  but target a different object. Ducci collapse (Ciamberlini-Marengoni 1937;
  Ehrlich 1990 "The Ducci game", Fibonacci Quart.; Breuer 2019, Proc. AMS/
  Bull. Aust. Math. Soc.; Lewis-TeFFT 2024, arXiv:2401.17502/2403.05319) is the
  CYCLIC map and collapses to the zero/{0,c} state of the WHOLE tuple; the
  Chase-Hunter-Tao/Cramer inverse theorem (arXiv:2607.08712) is about the LEFT
  diagonal reaching {0,1} (Gilbreath), not about the count of 2s in the RIGHT-
  diagonal {0,2} suffix. No source transfers either to "suffix length >= c n
  for the primes". Odlyzko 1993 (on disk) is the canonical treatment of the
  actual triangle and gives no such suffix bound.
precedent: >
  Ducci collapse (real, precisely stated, wrong object): Ehrlich, "The Ducci
  game", Fibonacci Quarterly 28 (1990) 1-7; Breuer, "Periods of Ducci
  sequences and odd solutions to a Pellian equation", Bull. Aust. Math. Soc.
  100 (2019) (DOI 10.1017/s0004972719000212); Lewis-Tefft, arXiv:2401.17502
  and arXiv:2403.05319; Ciamberlini-Marengoni 1937 (periodicity, cited in
  te Riele 1983 / Dular 2020). Chase-Hunter-Tao, "Gilbreath's conjecture: a
  Cramer random model and a deterministic analysis", arXiv:2607.08712 (2026),
  Theorem 1.2 (Cramer model: Gilbreath a.s.) + inverse theorem (obstructions:
  long zero blocks, long shallow {0,lambda} blocks) — already on disk.
  In-workspace (established): kummer-2adic-valuation-lift-refuted (the same
  magnitude route, closed); linearisation-fold-weight (nu2 = wt(Phi_n h) as a
  pure parity function); excess-is-negative-character-sum; fair-model-exact-
  binomial (surjectivity/rank n-2, ~half 2s for non-kernel h);
  odlyzko-0-2-reduction (whole-triangle {0,2} reduction, not a right-diagonal
  suffix bound).
falsifies: >
  The route is closed by the two grounds above; a reopening would need (a) a
  proof that the linearisation is wrong, i.e. that gap magnitudes carry nu2
  information not in the parity string — which would contradict result 1 as
  held; or (b) a source transferring Ducci/CHT collapse to a right-diagonal
  {0,2} suffix length bound for the primes — none exists in the library or the
  collapse literature located here.
```

## Grounding note (research pass, this dossier)

Ducci/Gilbreath collapse theory is real and well-sourced; the Chase-Hunter-Tao
inverse theorem is on disk and is the correct modern reference for the Cramer
model. But none of it prices a right-diagonal suffix-length bound, and the
"magnitude is a discarded resource" premise collides directly with the held
linearisation `nu2 = wt(Phi_n h)`, which makes nu2 a function of parity alone.
This is substantively the kummer-2adic-valuation-lift route re-named; the
library already closed that with a precise non-Archimedean obstruction
(residue-dependence of cancellation). Verdict: refuted.
