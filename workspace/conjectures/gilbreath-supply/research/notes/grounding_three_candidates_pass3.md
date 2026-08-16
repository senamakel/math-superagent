# Grounding the three newly-proposed candidates (third pass, research dossier)

Task: take `ducci-valuation-magnitude`, `zeta-tensor-block-doubling`, and
`mauduit-rivat-digital-equidistribution` to the literature and report per
candidate what the reformulation is called, the precise theorem, its hypotheses
and whether they hold here, who has applied it, and what it buys. Outcome: all
three are **refuted on evidence**, each by a different ground.

## C1 `ducci-valuation-magnitude` — refuted

The engines are real and precisely stated:
- Ducci collapse: Ciamberlini-Marengoni 1937 (periodicity/collapse for power-of-2
  tuple length), Ehrlich, "The Ducci game", Fibonacci Quarterly 28 (1990);
  Breuer, "Periods of Ducci sequences and odd solutions to a Pellian equation",
  Bull. Aust. Math. Soc. 100 (2019) DOI 10.1017/s0004972719000212;
  Lewis-Tefft, arXiv:2401.17502 (vanishing time for n=2^k, m=2^l) and
  arXiv:2403.05319. The collapse to the {0,c} periodic state is classical.
- Chase-Hunter-Tao, "Gilbreath's conjecture: a Cramer random model and a
  deterministic analysis", arXiv:2607.08712 (2026), already on disk — Theorem
  1.2 (Cramer model Gilbreath a.s.) and the inverse theorem (obstructions =
  long zero blocks and long shallow {0,lambda} blocks).

Why it dies:
1. It re-imports the closed kummer-2adic-valuation-lift obstruction. The
   "gap magnitude is an independent coordinate the parity reduction discards"
   idea was already refuted: the 2-adic valuation of a difference is NOT a
   function of the operands' valuations (ultrametric cancellation is
   residue-dependent), so no explicit propagation from initial magnitudes works.
   research/approaches/kummer-2adic-lift.md, killed-by.
2. The held linearisation (claim linearisation-fold-weight, problem.md fact 1)
   pins nu2(n) = wt(Phi_n h) as a pure function of the gap-parity string. If
   that holds, gap magnitudes carry no nu2 information beyond the parity
   encoding — a magnitude input is not a strictly weaker arithmetic demand.
3. Object mismatch: Ducci collapse and the CHT inverse theorem concern the
   WHOLE tuple / the LEFT diagonal (Gilbreath {0,1}), not the count of 2s in
   the RIGHT-diagonal {0,2} suffix. No source transfers either to a suffix-
   length bound for the primes. Odlyzko 1993 (on disk) gives no such bound.

## C2 `zeta-tensor-block-doubling` — refuted

The block self-similarity Z_{m+1} = [ Z_m, 0 ; Z_m, Z_m ] is real and correctly
named: Callan, "Sierpinski's triangle and the Prouhet-Thue-Morse word",
arXiv:math/0610932 (Thm 1: S^{-1} is a (-1,0,1)-matrix with Thue-Morse sign
pattern); Bacher-Chapman, "Symmetric Pascal matrices modulo p", Eur. J.
Combin. 22 (2003) DOI 10.1016/e2003.06.001 (autosimilar matrices, LDU); Kubelka,
"Self-similarity and symmetries of Pascal's triangles mod p", 2004.

Why it dies:
1. Object mismatch — the exact category error already closed twice. The block
   structure lives on the FULL index cube, not on the anti-diagonal slice
   Phi_n SUPPLY uses. This is precisely pascal-cascade-block-recursion (refuted:
   "the Sierpinski self-similarity lives on rows/blocks/triangular regions, NOT
   on the anti-diagonal slice") and substitution-incidence-perron (refuted: the
   slice recursion T(2n,2d)=T(n,d) fails). Doubling n does not map the fold's
   slice onto two copies of itself.
2. The price re-imports switch density / local randomness: "two halves
   independent => cross = o(n)" is the short-memory input GOAL priority 2
   prices, and per-scale-refinement-collapses-to-switch-density already showed
   per-scale/local correlation inputs collapse to the g=0 switch-density scale.
3. No source applies the tensor/block decomposition to a weight lower bound for
   the slice; Callan/Bacher-Chapman/Kubelka are structural facts about the full
   matrix.

## C3 `mauduit-rivat-digital-equidistribution` — refuted (on the richest evidence)

The one-point engine is real and precisely stated: Mauduit-Rivat, "Sur un
probleme de Gelfond: la somme des chiffres des nombres premiers", Ann. Math.
171 (2010) 1591-1646, Theoremes 1-3 (on disk); Green, arXiv:0710.0823 Thm
2.1.1 (binary digit sum of primes 50/50, power saving); Drmota-Mauduit-Rivat,
"Primes with an average sum of digits", Compositio Math. 145 (2009).

Crucially, the TWO-POINT digital literature genuinely EXISTS (unlike C1/C2,
where the transfer was simply absent). It is real but about the wrong statistic:
- Toumi, arXiv:2504.02784 (2025): level of distribution of exp(2 pi i l
  s_q(n)/b) correlations.
- Spiegelhofer, "Correlations for numeration systems", PhD thesis TU Wien 2014:
  correlations of s_q(n) and s_q(n+k) in residue classes with power saving.
- Sobolewski-Spiegelhofer, arXiv:2411.07779 (2024): decomposition of the
  sum-of-digits correlation measure gamma_t.
- Aloui-Mauduit-Mkaouar, Ramanujan J. 2015 (HAL-01272915): joint distribution
  of S(n), S(n+1) in APs.
- Bésineau / Gelfond joint q-base distribution (J. Number Theory 1998).

Every one controls the digit-sum function s_q at INTEGER arguments n, n+k.
The fold needs mod-4 residue correlations at PRIME-INDEX submask positions.
That value→index transfer is exactly the gap the library holds is absent:
mr-green-set-paradigm-not-transfer ("no transfer exists between s_q(p) and the
index-domain gap-parity h") and mod2m-lift-onepoint (one-point digital
equidistribution cannot force a two-point cell). The route is priced to fail
honestly and it does.

## What the three rejections share

C1 and C2 both re-import an already-closed obstruction from the library under a
new representation (kummer-2adic for C1; pascal-cascade/substitution-incidence
object mismatch for C2). C3 dies on the value↔index transfer, the single
recurring obstruction this workspace has recorded across matomaki-radziwill,
dispersion, rubinstein-sarnak, level-set-explicit-formula, and mod2m-lift. The
one positive from the pass: the two-point digital statement is genuinely a
named, published body of work (Toumi, Spiegelhofer, Sobolewski-Spiegelhofer,
Aloui-Mauduit-Mkaouar) — worth recording so nobody re-fetches it expecting a
way past the parity barrier; it evaluates s_q at integer arguments and stops
there.

## Caveats / what I could not do

- I did not independently execute the tensor identity or the Ducci suffix
  computation. The C1 and C2 refutations rest on re-imported library-closed
  obstructions (solid: each is a specific machine/hand-verified falsifier on
  disk) plus the literature object-mismatch. If either route is ever reopened,
  its first step must be a cell-by-cell oracle check of the proposed identity.
- The C3 refutation is the most strongly evidenced (direct literature), and is
  the one the inventor explicitly priced to fail.
