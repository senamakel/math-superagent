# Cassaigne — On extremal properties of the Fibonacci word (RAIRO-ITA 42 (2008) 701–715)

<!-- source: https://www.numdam.org/item/ITA_2008__42_4_701_0/ | full text read 2026-08-19 -->

Full text: `research/sources/cassaigne-extremal-properties-fibonacci-word.full.md`
(Also `research/sources/cassaigne-extremal-properties-fibonacci-word-2008.full.md` = the Numdam *landing page* only; the actual paper is the `.full.md` without the `-2008`.)

## What it establishes

**Convention.** f = Fibonacci word (fixed point of a↦ab, b↦a), slope 2−Φ = [0; 2, 1, 1, …] ≈ 0.382 in this paper's convention. (PE1006's S has slope 1/φ² = (3−√5)/2 ≈ 0.382 — the complement; the extremal constants below are convention-independent.)

**§2 Repetitions.** Index (critical exponent) ind(u) = sup{e(w): w ∈ L(u)}.
- Theorem 2.1 (Carpi–de Luca, Damanik–Lenz): for Sturmian slope α = [0; a₁,a₂,…], ind(u) = supₙ (2 + a_{n+1} + (q_{n−1}−2)/qₙ). Hence ind(f) = Φ+2 ≈ 3.618, and this is the *minimum* index among Sturmian words (Theorem 2.2 classifies the six slopes attaining it).
- Theorem 2.3: asymptotic index ind*(f) = Φ+2 also minimal among Sturmian words.
- Theorem 2.8: I(f) = Φ+1 (minimal initial critical exponent in a subshift, maximal among non-periodic words).

**§3 Recurrence.** R(n) = inf{N: every length-N block contains every length-n factor}; recurrence quotient ρ*(u) = limsup R(n)/n.
- Theorem 3.1: for Sturmian slope α = [0; a₁,a₂,…], ρ*(u) = 2 + limsup [aₙ; a_{n−1},…,a₁]. So ρ*(f) = Φ+2 ≈ 3.618, the minimum possible for a Sturmian word (Morse–Hedlund 1940); a non-Sturmian word has ρ* ≥ 3+√2 once quotients are not eventually 1.
- Theorem 3.3: for Sturmian u, ρ*(u) = ind*(u).
- Prop 3.2: for any word, ind*(u) ≥ 1 + 1/(ρ*(u)−1).

**§3.2 First occurrence.** R′(n) = inf{N: Lₙ(u₀…u_{N−1}) = Lₙ(u)} (shortest prefix containing all length-n factors); ρ′*(u) = limsup R′(n)/n. **R′(n) − n + 1 is the maximal position where a length-n factor occurs for the first time.**
- **ρ′*(f) = Φ + 1 ≈ 2.618** (stated in the running text and in the §5 summary table).
- Theorem 3.4: the *optimal* (minimum) value of ρ′* across all non-eventually-periodic words is (29−2√10)/9 ≈ 2.519, attained by a *different* Sturmian word u (fixed point of a↦abaababa, b↦aba, slope (5−√10)/5). The Fibonacci word is NOT the minimizer — that is the theorem's point. **Do not cite Theorem 3.4 for ρ′*(f); the Φ+1 value is the pre-theorem contrast.**

**§4 Palindromes (context).** δ(f) = Φ (palindromic prefix gap); ψ(f) = Φ (first palindrome occurrence rate); π(f) = 1, π̄(f) = 3 (palindrome densities).

## Why it matters for PE1006

- **The prefix-completeness bound:** ρ′*(f) = Φ+1 ≈ 2.618 means a prefix of length ≈ 2.618·k contains every length-k factor. This justifies brute.py's "≥ 3k is safe" heuristic (3 > 2.618) and bounds directive 9's contiguous-window range {Fₙ−k−1 … Fₙ−1} which must cover all first occurrences to be a complete factor set.
- The recurrence quotient ρ*(f) = Φ+2 is a *different* quantity (block-completeness, not prefix-completeness) and must not be conflated with ρ′*.
- ind(f) = Φ+2 bounds the repetition structure of the word's factors (relevant to any periodicity/extension argument, not to the Ψ sum directly).

## What it does NOT establish

- No statement about Ψ(k) or the sum of squares of factor values; the paper is about extremal repetition/recurrence/palindrome constants.
- The first-occurrence result is a *limsup* bound, not an exact R′(n) formula; for exact small-k values (e.g. k=15 needs 35, k=30 needs 63) the run's own brute-force is the authority.

## Claims anchored here

`fibonacci-first-occurrence-window-bound` (value ρ′*(f) = Φ+1 **confirmed**; the claim's citation "Theorem 3.4" was **misattributed** — corrected in `research/notes/cassaigne-first-occurrence-window.md` to §3.2 running text + §5 summary table).
