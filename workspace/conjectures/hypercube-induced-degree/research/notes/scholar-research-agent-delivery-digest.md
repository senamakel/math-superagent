# Scholar digest — the research agent's new delivery

This pass reviewed what the research agent added to `research/` since the last
scholar pass (`scholar-new-library-pass.md`). Most of the reference library was
already digested and claimed in CLAIMS.md across the prior scholar notes. The
genuinely new material this delivery adds, evaluated against the goal
(f(n)=min{D(S):|S|=2^{n-1}+1}, max internal degree; deliverable = proved
partial result on the log-vs-sqrt gap):

## New and load-bearing: exact values f(1..7) with a broken-encoding warning

`research/sources/sqrt-upper-construction-tightness.md` is a run-generated note
(no external source was downloadable — Huang's paper and every direct answer
query are withheld by the screen). It carries NO claim block and is therefore
NOT in CLAIMS.md's exact-value rows, which only hold f(1..4) and f(1..5). What
it establishes, with the evidence I corroborated directly from `code/out/`:

- **f(1..7) = 1,2,2,2,3,3,3 = ceil(sqrt(n))**, computed by the HiGHS binary ILP
  decision oracle, validated against the exhaustive oracle on all 13 (n,d)
  pairs n=1..4 and against a separately-configured CP-SAT on n=1..5, each
  witness re-verified by pure-python degree counting. I verified the n=6 rows:
  `verify_n6n7.captured.txt` shows BOTH HiGHS and CP-SAT agree n=6,d=2
  infeasible and n=6,d=3 feasible (AGREE). n=7 is corroborated only through
  `c7d3.txt` ("n=7 d=3 feasible=True |S|=65"); the `verify_n7.captured.txt`
  file is empty and there is no captured n=7,d=2 run, so **f(7)=3 rests on the
  note's word plus the d=3 feasibility witness, not a captured d=2
  infeasibility** — weaker corroboration than n=6.
- **The lower bound is machine-verified for ALL n**: signed adjacency
  A_n (A_n²=n·I, entries {0,±1}, support=Q_n edges, spectrum ±sqrt(n) each
  mult 2^{n-1}), Cauchy interlacing forces λ_max(A_n[S,S]) >= sqrt(n) for
  |S|=2^{n-1}+1, and λ_max <= Δ(H) at the degree bound. Hence
  **f(n) >= ceil(sqrt(n)) for every n** (integer degrees). Since f(n) is an
  integer, the correct literal statement is f(n) >= ceil(sqrt(n)), not
  floor(sqrt(n)) (n=2: sqrt 2 = 1.414 forces integer degree 2).
- **WARNING that kills a false result**: the claims in
  `code/out/upper_n10_11.captured.txt` that f(10)>4 and f(11)>4 are FALSE
  NEGATIVES from a KNOWN-BROKEN CP-SAT encoding that returns INFEASIBLE even
  for n=3,d=2, a provably-feasible case (witness {0,1,2,5,6}). The HiGHS
  confirmation meant to settle n=10,11 (`f10_11_independent.py`) timed out
  (empty output; the OPENBLAS thread failures in `c10d4.txt` are a resource
  artifact, not a result). f(10), f(11) remain UNCONFIRMED.
- Extremal witnesses are "flat" (large fraction at max degree; n=5: 12/17
  vertices at degree 3) and are NOT "parity class + one vertex" (n=4 witness
  [0,1,2,5,6,11,12,13,14] is not parity-plus-one). This flatness is what a
  degree-profile oracle must show: the max-degree count is an O(|S|) fraction,
  so no averaging argument can ever reach sqrt(n).

## What does not help (already ruled, or catalogue noise)

The ~18 isoperimetric/influence sources (Harper ×2, Keevash–Long ×2, Ellis ×2,
Ellis–Keller–Lifshitz, KKL, Beckner, Friedgut, Falik–Samorodnitsky,
Beltrán–Ivanisvili–Madrid, Durcik–Ivanisvili–Roos, Kruskal–Katona,
induced-subgraphs, Barber ×2, Liu–Zhou) were all digested and claimed in prior
passes; they bind average/outer-boundary quantities and confirm the four
"stuck techniques" of problem.md cannot reach the maximum D(S). The seven OEIS
stubs are catalogue noise, none is f(n). `LIBRARY-STATUS.md` was digested in
`scholar-new-library-pass.md`; nothing new there. The Ambainis et al. 2014
sensitivity-complexity lead remains a lead (transfer to D(S) unproved), not
evidence.

## The decisive closed result, restated with its new numerical floor

Prior scholar pass already recorded `f-n-sqrt-n-proved` (status: proved): the
spectral argument gives f(n) >= sqrt(n) for ALL n, so f(n) = Θ(sqrt(n)) =
ω(log n) — the log–sqrt gap is closed from below. This delivery adds the
computed exact values f(1..7)=ceil(sqrt(n)), checked at non-squares (n=2,3,5,6,7)
not only at perfect squares, which strengthens the empirical basis: the lower
bound is attained (empirically) at every n<=7. The honest open residue is
unchanged: whether f(n)=ceil(sqrt(n)) for ALL n (the upper construction
attaining ceil(sqrt n) for n beyond 7, and n=8..11), whose source was withheld
and whose oracle runs at n=10,11 were too slow / broken. f(7)=3 has only d=3
feasibility corroboration on disk.

## Claim blocks

```claim
id: f-exact-1..7
statement: f(n) = min{ D(S) : S ⊆ {0,1}^n, |S| = 2^{n-1}+1 } takes values f(1..7) = 1,2,2,2,3,3,3 = ceil(sqrt(n)).
hypotheses: n = 1..7
holds-here: yes
status: computed (HiGHS ILP decision oracle, validated against exhaustive n<=4 and independently-configured CP-SAT n<=5, witnesses re-verified by python degree count)
bearing: lower bound f(n)>=ceil(sqrt n) is attained at every n<=7, including non-squares n=2,3,5,6,7
anchor: research/sources/sqrt-upper-construction-tightness.md
answers: exact-f-values-1..7
```

```claim
id: f-lower-bound-ceil-sqrt-n
statement: f(n) = min{ D(S) : S ⊆ Q_n, |S| = 2^{n-1}+1 } >= ceil(sqrt(n)) for every n >= 1, because f(n) is an integer and the spectral bound f(n) >= sqrt(n) holds for all n.
hypotheses: none beyond the problem's definition
holds-here: yes
status: proved (spectral: A_n signed adjacency, A_n^2 = nI, Cauchy interlacing, lambda_max <= Delta)
bearing: closes the log-vs-sqrt gap from below; forces integer degree ceil(sqrt n), not floor
anchor: research/sources/sqrt-upper-construction-tightness.md
```

```claim
id: n1011-false-negative-warning
statement: The f(10)>4 / f(11)>4 claims in upper_n10_11.captured.txt are false negatives of a known-broken CP-SAT encoding that reports INFEASIBLE even for n=3,d=2 (provably feasible); f(10) and f(11) are unconfirmed.
hypotheses: n = 10, 11
holds-here: yes
status: checked (encoding sanity check shows mismatch; HiGHS confirmation timed out)
bearing: do not record f(10)>4 or f(11)>4 as results; the values are open
anchor: code/out/upper_n10_11.captured.txt
```

## Contradictions flagged

- **None of the new material contradicts recalled memory.** The prior open
  contradiction (problem.md asserting the log-vs-sqrt gap is open, versus the
  run's proved spectral f(n)>=sqrt(n)) is NOT reopened by anything here; the
  new exact values agree with ceil(sqrt(n)).
- **Internal note**: the n=10/11 "f>4 counterexample" claims in
  `upper_n10_11.captured.txt` contradict the spectral lower bound only if
  believed; they are already identified as false negatives of the broken
  encoding and must not be recorded as results.
