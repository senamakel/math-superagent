# Granville & Lumley — "Primes in short intervals: heuristics and calculations"

**Full text:** `research/sources/granville-lumley-primes-short-intervals-heuristics.FULL.full.md`
**Source:** Andrew Granville, Allysa Lumley, *Experiment. Math.* (2021), doi 10.1080/10586458.2021.1927256; arXiv:2009.05000 (downloaded from arxiv.org/pdf/2009.05000).

## What it is about

This is a *heuristics* paper (explicitly conjectural, data-supported but not proved) about the range of the prime count over short intervals `[X, X+y]` within `(x, 2x]`. Its objects are

```
M(x,y) = max_{X∈(x,2x]} π(X+y) − π(X)   and   m(x,y) = min_{X∈(x,2x]} π(X+y) − π(X)
```

and it conjectures how these extremal counts grow as `y` ranges from `log x` up to order `(log x)²`.

- It believes `m(x,y) = 0` for `y ≪ (log x)²` (unknown constant), i.e. short intervals of length up to about `(log x)²` can be empty of primes, and conjectures unexpected slow growth of the maximum `M(x,y)` over the `log x → (log x)²` range.
- Proposes asymptotics `m(x,y) ~ u_−(c_− t)·log x`, `M(x,y) ~ u_+(c_+ t)·log x` for `y ~ t(log x)²`, via implicit functions `u±`.

## Bearing on this run

The run's live open content (Route B, Granville's Theorem 5.5) is the **supply-side** linear lower bound `ν₂(q_{n−1}) ≥ c·n` on the count of `{0,2}`-valued (halved, mod-4 "2") entries in a prime right diagonal — equivalently a prime-gap-mod-4 frequency statement. **This paper is the demand-side short-interval heuristic companion and does NOT supply a mod-4 gap-frequency bound.** It constrains how many primes (extremal counts `M,m`) sit in intervals, not how the prime-to-prime gaps are distributed mod 4; it is explicitly conjectural and its conclusions are about the range of `π(X+y)−π(X)`, not about ν₂.

So it is a **canonical held reference for the short-interval / Cramér-model frame** (it shares the Granville short-interval conjecture family with Banks–Ford–Tao and Chase–Hunter–Tao), but it does **not** close or even directly bound the ν₂ supply side. Use it as the documented source for the short-interval heuristic landscape; do not cite it as evidence for a mod-4 gap-frequency or ν₂ bound. The relevant two-point mod-4 frame (which does make ν₂ = n/2 the natural leading term) remains the held Lemke Oliver–Soundararajan 2016 claim `los-2016-consecutive-pair-mod4-bias`.

## Claims

```claim
id: granville-lumley-short-intervals-heuristics
statement: (Granville–Lumley 2021) Conjectures M(x,y) ~ u_+(c_+ t)·log x and m(x,y) ~ u_−(c_− t)·log x for y ~ t(log x)², with m(x,y)=0 for y ≪ (log x)² (unknown constant); M(x,y) grows surprisingly slowly as y ranges log x → (log x)². Purely heuristic, data-supported not proved.
hypotheses: primes; short intervals [X,X+y] within (x,2x]; y ≪ (log x)^{2+o(1)}; heuristic reasoning (random-model / sieve), not unconditional.
holds-here: n/a — this is a demand-side short-interval heuristic and does not bear directly on the ν₂ supply bound Route B needs. It is the canonical short-interval heuristic companion, not a ν₂ result.
status: sourced (downloaded, indexed)
bearing: documents the short-interval (Cramér/Granville) heuristic landscape that underlies the random-analogue side (Chase 2024, CHT 2026, BFT 2023); does NOT provide a mod-4 gap-frequency / ν₂ supply bound. Do not cite it for ν₂.
anchor: research/sources/granville-lumley-primes-short-intervals-heuristics.FULL.full.md
```

## Not obtained / recorded

The published *Experimental Mathematics* DOI (10.1080/10586458.2021.1927256) is paywalled; the arXiv v1 PDF (2009.05000) was obtained in full and is what is held.
