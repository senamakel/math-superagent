# Scholar synthesis — what the newly-digested sources add, and the resolved state

This note records the scholar's passage through the reference library after the
research agent finished. The decisive content (the √n spectral lower bound) was
already on disk and machine-verified; the four newly-absent summaries
(Barber, Falik–Samorodnitsky, Keevash–Long, Liu–Zhou) are now written. This
note is a reading-and-combining note, not new computation: every number it cites
is in a captured output, and I read those outputs directly.

## The one decisive fact, and its verification status

The gap `c log n <= f(n) <= sqrt(n)` is **closed from below**: the run holds
`f(n) >= sqrt(n)` for every n, re-derived independently of the withheld primary
source. I re-read the captured evidence and can confirm what is and is not
verified:

- `huang-signature-matrix-square` — **exact, checked**: `A_n^2 = n·I`, zero
  diagonal, support = cube edges, for n=1..8 (sympy Integer, through 256×256),
  huang_spectral.captured.txt Part 1; spectrum ±√n each multiplicity 2^{n-1},
  exact n=2..7, numeric n=8..10, Part 2. The ∀n block-multiplication induction
  is written out and correct.
- `huang-interlacing-sqrt` — rests on the classical Cauchy interlacing theorem
  plus the exact spectrum; numerically spot-checked n=2..10 (worst-case λ_max =
  √n in every trial), and for EVERY admissible S at n=1..4.
- `huang-degree-bounds-lambda` — proved (quadratic form + Rayleigh–Ritz);
  numerically confirmed.
- `f-n-sqrt-n-proved` — derived by the chain; consistent with exact
  f(1..5) = 1,2,2,2,3 = ceil(√n). **This is a genuine proof for all n** on the
  run's own derivation, not a numerical theorem.

The `verify_interlacing_chain.captured.txt` (EXIT_CODE=0) independently confirms
Part (a) A_n²=nI etc. and the specific even-set-plus-one-odd-vertex interlacing
for n=2..8 with λ_max exactly √n.

## What the versions say about the achieved bound

`huang-f-n-sqrt-n` says `f(n) = Θ(√n)`; `f-n-sqrt-n-proved` says the same, with
the caveat that the literal `f(n) <= sqrt(n)` of problem.md is false for n=2,5
(integer f exceeds √n) — the correct statement is `f(n) = Θ(√n)`, equivalently
`ceil(√n)` attainment. This rounding caveat is the one place multiple notes
agree and must be carried.

## The four new sources

- **Barber (balanced independent sets, 2012)** — closes
  `classification-maximum-independent-20be`: the maximum independent sets of Q_n
  are exactly the parity classes. This is the structural base of the
  "parity-class-plus-one-vertex" extremal picture (that added vertex has
  internal degree n). Not a D(S) bound — it is the d=0 line — but it pins the
  extremal scaffold. **Contradiction within the library:** the source file's
  prose gives the odd-n balanced-max formula as `2^{n-1}−2^{n-2}(n−1)` while its
  own claim block and the re-derived ledger give `2^{n-1}−2^{n-2}(n−1)/2`. A
  sloppy/2, to be resolved only against the paper (withheld). Not load-bearing.
- **Falik–Samorodnitsky (2007)** — total-influence edge isoperimetric + a
  combinatorial KKL proof. It bounds Σ_i I_i, an average outer boundary; at
  problem.md's µ just over 1/2 it just misses the stated regime and, more
  importantly, bounds the wrong quantity for D(S). Part of the four "stuck"
  techniques. Confirms the obstruction; does not help the D(S) bound.
- **Keevash–Long (2018)** — Harper vertex-isoperimetric + stability. Explicitly
  bounds outer vertex boundary; applies at m=2^{n-1}+1 but says nothing about
  max internal degree. Confirms the obstruction; does not help.
- **Liu–Zhou (Cayley eigenvalues, 2022)** — the unsigned adjacency spectrum of
  Q_d is d−2i with multiplicity C(d,i). This is the *base* spectrum the run's
  signed matrix colourings; it confirms that the √n comes from the sign choice
  (A_n²=nI), not from the plain adjacency (whose top eigenvalue is d). Directly
  supports the spectral route.

The other sources (Beltrán, Durcik, Harper, KKL, Kruskal–Katona,
induced-subgraphs, Barber–Erde survey) were already summarised; they confirm the
obstruction (average/outer tools) and, for Kruskal–Katona/induced-subgraphs,
provide max-producing machinery at the wrong (full-degree) end. None change the
decisive conclusion.

## Contradiction with recalled memory

Recalled memory held Huang's theorem as "recalled, not verified" and the gap as
possibly still open. The run's own derivation + machine checks now *independently
confirm* the √n lower bound from first principles — resolving the
problem.md-"open"-vs-Huang-"closed" tension in the closed direction. This is the
most valuable resolution the library produced. No source contradicts the √n
lower bound; every isoperimetric/influence source only confirms that its own
technique cannot reach it, which is consistent.

## What the run still lacks

- The matching **upper construction** `f(n) <= ceil(√n)` — source withheld, not
  yet rebuilt; needed to certify exact equality f(n)=ceil(√n) rather than just
  the lower bound + small-n agreement.
- The pre-2019 attributions (Nisan–Szegedy / Gotsman–Linial / Rubinstein) remain
  recalled-not-sourced; they are background, not load-bearing for the proof.
- The Clifford/Dirac, Delsarte–Krawtchouk-LP, and entropy/degree-constrained
  approaches in `research/approaches/` are still *proposed/unchecked*; the LP
  and entropy routes re-derive only the average obstruction, and the Clifford
  route's exact-value conjecture `f(n)=ceil(√n)` is the one live speculative
  overshoot beyond the closed Θ(√n) result.

## Claim block

```claim
id: spectral-sqrt-lower-bound-verified
statement: f(n) = min{ D(S) : S ⊆ {0,1}^n, |S|=2^{n-1}+1 } >= sqrt(n) for every
  n >= 1, via A_n (signed adjacency, A_n^2=nI), Cauchy interlacing (λ_max of the
  (2^{n-1}+1)-principal submatrix >= sqrt(n)), and λ_max <= Δ at the induced H.
  Hence f(n) = Θ(sqrt(n)) and f(n) = omega(log n); problem.md's log–sqrt gap is
  closed from below.
hypotheses: none beyond the three spectral lemmas, each proved for all n
  (signature-matrix-square exact n<=8, interlacing + degree-bound proved + spot
  checked n<=10).
holds-here: yes — this is the goal, re-derived independently of the withheld
  primary source.
status: proved (on the run's own derivation; construction upper bound still to
  be rebuilt to certify f(n)=ceil(sqrt(n)) equality).
follows-from: huang-signature-matrix-square, huang-interlacing-sqrt,
  huang-degree-bounds-lambda
answers: exact-statement-huang-932b (supersedes the earlier f-n-sqrt-n-proved
  with the same conclusion, adding the direct captured-output re-read).
anchor: code/out/huang_spectral_verified.md, code/out/verify_interlacing_summary.md,
  code/out/huang_spectral.captured.txt, code/out/f-exact-1..5-note.md
```
