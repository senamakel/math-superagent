# Scholar synthesis — the log-vs-sqrt gap is closed by the spectral route

This note records the scholar's judgment on the state of the library and the
decisive finding. It is a reading-and-combining note, not a new computation: the
computations it relies on are already captured (see `code/out/` and the anchors
below). `scholar_verify_chain.py` (this file's sibling) was written as a fresh
independent duplicate but was NOT run in this session; the authoritative runs are
`code/out/huang_spectral.captured.txt` and `code/out/verify_interlacing_chain.captured.txt`,
which contain the identical checks.

## The decisive finding (already on disk, independently re-derived here)

The "thirty-year open gap" of `problem.md` — `c·log n <= f(n) <= sqrt(n)` — is
**closed from below**: this run has a complete proof that `f(n) >= sqrt(n)` for
every n, independently re-deriving Hao Huang's theorem (the primary source is
withheld by the evidence screen, so the argument stands on this run's own
derivation). Combined with the construction upper bound this gives
`f(n) = Theta(sqrt(n))`, subsuming the run's primary `omega(log n)` target.

The proof is three lemmas, each a genuine proof for all n (not a small-n
numerical check):

- `huang-signature-matrix-square`: recursion `A_1=[[0,1],[1,0]]`,
  `A_n=[[A_{n-1},I],[I,-A_{n-1}]]` is symmetric, {0,±1}, zero-diagonal, supported
  on the edges of Q_n, and `A_n^2 = n·I` (block-multiplication induction; exact
  verified n=1..8). Spectrum ±sqrt(n), each mult 2^{n-1}.
- `huang-interlacing-sqrt`: for any S with |S| = 2^{n-1}+1, the principal
  submatrix B = A_n[S,S] has λ_max(B) >= sqrt(n) — Cauchy's interlacing theorem
  instantiated (a proved theorem; numerically confirmed for every admissible S
  at n=1..4 and random S at n=5..10).
- `huang-degree-bounds-lambda`: λ_max(B) <= Δ(Q_n[S]) = D(S) via the quadratic
  form / Rayleigh-Ritz bound (proved).

Hence D(S) >= sqrt(n) for every admissible S, so f(n) >= sqrt(n).

Claim block:

```claim
id: f-n-sqrt-n-proved
statement: f(n) = min{ D(S) : S ⊆ {0,1}^n, |S| = 2^{n-1}+1 } satisfies
  f(n) >= sqrt(n) for every n >= 1. With the construction upper bound,
  f(n) = Theta(sqrt(n)); in particular f(n) = omega(log n).
hypotheses: none beyond the three spectral lemmas (signature-matrix-square,
  interlacing-sqrt, degree-bounds-lambda), each proved for all n.
holds-here: yes — this is the goal.
status: proved (re-derivation; primary source withheld, argument stands on this
  run's own derivation). Exact small-n values f(1..5)=1,2,2,2,3 agree.
anchor: code/out/huang_spectral_verified.md, code/out/verify_interlacing_summary.md
answers: exact-statement-huang-932b
```

## Caveat on the stated upper bound

`problem.md` states `f(n) <= sqrt(n)`. Literally this is false for several n
because f(n) is an integer: f(2)=2 > sqrt(2)=1.414, f(5)=3 > sqrt(5)=2.236.
The correct statement is `f(n) = O(sqrt(n))` (equivalently f(n) <= ceil(sqrt(n))
up to a constant), and `f(n) = Theta(sqrt(n))`. Any memory or claim quoting the
construction as exactly `sqrt(n)` should carry this rounding caveat.

## What the sources actually contribute

Every isoperimetric / influence source in the library —
`kkl-influence-1988`, `falik-samorodnitsky`, `beltran-ivanisvili-madrid`,
`durcik-ivanisvili-roos`, `harper-hamming-1999`, `keevash-long`,
`barber-erde` — bounds an **average** or **outer-boundary** quantity (total
influence, E[h_A^β], vertex boundary). None bounds the maximum internal degree
D(S). This confirms problem.md's obstruction exactly: those four standard
techniques are stuck at log n because they optimise the wrong side of the cut.

`kruskal-katona` and `induced-subgraphs-hypercubes-kk-2012` are
**maximum-producing** tools (they count degree-k / full vertices) — the correct
*kind* of tool — but at the high-degree end of the spectrum, not the
2^{n-1}+1 low-degree end; θ(n) relevant as machinery, not directly decisive.

The spectral route (`huang`) is the source that supplies a maximum directly:
λ_max(B) is a maximum over unit vectors by construction, and the sqrt comes from
a genuine quadratic relation (A_n² = n·I) — exactly the two things problem.md
predicted a successful lower bound would need.

## Verdict on the sources

- **Do not help** (for the D(S) question, except to confirm the obstruction):
  kkl, falik-samorodnitsky, beltran, durcik, harper, keevash-long, barber-erde.
- **Adjacent / correct kind but wrong end:** kruskal-katona,
  induced-subgraphs-hypercubes.
- **Decisive:** the spectral chain, independently re-derived in this run.

## Contradictions recorded

- problem.md's framing ("gap open for thirty years") vs. this run's complete
  proof that f(n) >= sqrt(n). Not a source-vs-source contradiction: the run
  resolved the question in the "close from below" direction.
- The literal `f(n) <= sqrt(n)` upper bound stated in problem.md is false for
  n = 2, 5 (integer f exceeds sqrt); the true statement is Theta(sqrt(n)).
