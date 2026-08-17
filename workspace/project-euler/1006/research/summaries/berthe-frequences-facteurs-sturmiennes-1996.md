# Berthé — Fréquences des facteurs des suites sturmiennes (1996)

Source: Valérie Berthé, "Fréquences des facteurs des suites sturmiennes",
Theoretical Computer Science 165(2) (1996), 295–309, DOI
10.1016/0304-3975(95)00224-3 (French). Full text:
`research/sources/berthe-frequences-facteurs-sturmiennes-1996.full.md`
(author copy from https://www.irif.fr/~berthe/Articles/st.pdf).

## Statements it establishes

- **Setup**: the Fibonacci sequence is the fixed point of the substitution
  σ(a)=ab, σ(b)=a — the PE1006 word S with letters relabelled (a↔0, b↔1).
  Reminder: Sturmian sequences have complexity p(n) = n + 1 for all n
  (and a sequence with p(n) ≤ n for some n is ultimately periodic).
- **Proposition 1**: every Sturmian sequence is a_α = (a_α(n)) with a_α(n) =
  ⌊(n+1)α + ρ⌋ − ⌊nα + ρ⌋ or its mirror — the mechanical-word digit formula
  (claim `mechanical-word-digit-rule`).
- **Dekking's theorem, generalized** (main theorem): the frequencies of the
  factors of the same length of a Sturmian sequence take at most 3 values.
  The possible frequency *values* and the *counts* of factors achieving each
  value are explicit functions of the continued-fraction expansion of the
  angle α. Method: the Rauzy word-graph (special factors).
- **Proposition 3** (Farey structure): for consecutive Farey points p₁/q₁ <
  p₂/q₂ with the slope α between them, the set of length-m factors stabilises
  exactly at m = q₁+q₂−2 — the exact threshold at which the factor structure
  of the rational approximant p/q matches the irrational limit. This is the
  quantitative version of "denominator F(n) > k is enough" that directive 2's
  slope choice (F(n−2)/F(n), denominator F(n) ≫ k) relies on.

## Relation to PE1006

- **Primary source for the ≤ 3-frequency theorem** that Alessandri–Berthé
  state as Theorem 8 and the run's claim `governing-factor-complexity` uses.
  Dekking's case of the Fibonacci word: three possible frequencies per length,
  explicit values via the golden-ratio continued fraction.
- The **Farey-stabilisation Proposition 3** is directly load-bearing for the
  solver's choice of rational slope approximant: it says that with slope
  F(n−2)/F(n) (whose Farey neighbours are the consecutive Fibonacci
  convergents) the length-k factor set of the approximant coincides with the
  Fibonacci word's factor set exactly when k ≥ F(n)−2 — the run's k = 1..150
  vs-brute gate is the empirical shadow of this theorem. (The run uses
  F(n) ≫ k; Proposition 3 explains why a smaller margin cannot be safe.)
- The graph-of-words method is the same bookkeeping behind directive 1's
  autocorrelation counts: the "at most three" class structure of the pairs at
  each lag.

This is the deepest primary source now held on the *counting/frequency*
side of the factor structure. French; the statements above are the operative
ones for the run.