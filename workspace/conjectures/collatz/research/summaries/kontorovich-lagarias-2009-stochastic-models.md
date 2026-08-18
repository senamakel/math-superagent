# Kontorovich–Lagarias 2009 — stochastic models for 3x+1 and 5x+1

<!-- src: Kontorovich & Lagarias, "Stochastic Models for the 3x+1 and 5x+1 Problems", arXiv:0910.1944 (in: The Ultimate Challenge, AMS 2010, pp. 131–188) -->

Full text: `research/sources/kontorovich-lagarias-2009-stochastic-models.full.md`

## What the source establishes

A 68-page survey of probabilistic models for the long-time behavior of the
3x+1 and 5x+1 maps. This is the canonical source for the "random walk
heuristic" that problem.md warns about: the models are rigorously analyzable,
but they yield **conjectures**, not theorems about the actual map.

**The two stochastic models for a single forward orbit (§3):**
1. **Multiplicative random product (MRP) model** — each 3x+1 step multiplies
   the orbit value by 3 or 1/2; the products are treated as random.
2. **Bernoulli random walk (BRW) model** — logarithmic rescaling gives an
   additive random walk with unequal steps and **negative drift**.

These predict: all orbits converge to a bounded set; the total stopping time
σ∞(n) grows like c·log n for a specific constant c (in a
distributional/typical sense).

**Rigorous results the framework covers:**
- Symbolic dynamics for accelerated iteration (§6): Kontorovich–Sinai showed
  suitably scaled initial trajectories converge in a limit to **geometric
  Brownian motion**.
- Verification as of the writing: 3x+1 conjecture verified for all
  n ≤ 5.67×10^18 by computer experiments [31] (that is Oliveira e Silva's
  20×2^58 bound, the pre-Barina record).
- 5x+1 is conjecturally different: a density-one set of integers are
  conjectured to lie on divergent trajectories, with finitely many periodic
  orbits including {1,3,8,4,2,...}.

## What it implies for this run

This is the statistical shadow of the conjecture, not progress on it: the
models are analyzable but heuristic. The negative-drift BRW model is exactly
the "expected multiplicative drift √3/2 < 1" that problem.md identifies as
the unproved independence assumption. Any claim that "stochastic models prove
Collatz" is refuted by this source: the models predict, they do not imply.

## Claims

```claim
id: kl-stochastic-heuristic
statement: Stochastic models for the 3x+1 map — the multiplicative random product (MRP) and the negative-drift Bernoulli random walk (BRW) on log-values — predict that all orbits converge to a bounded set and total stopping time grows like c log n, but these are heuristic conjectures, not theorems about the actual map (Kontorovich–Lagarias 2009).
hypotheses: the models assume independence of successive 3x+1 steps (unproved)
holds-here: yes, as context — this is the average-case shadow, not the conjecture
status: asserted
bearing: marks the random-walk heuristic as heuristic; any result built on it does not touch the conjecture
anchor: research/summaries/kontorovich-lagarias-2009-stochastic-models.md
```

```claim
id: kl-kontorovich-sinai-gbm
statement: Suitably scaled initial trajectories of the accelerated Collatz iteration converge in a limit to geometric Brownian motion (Kontorovich–Sinai, surveyed in Kontorovich–Lagarias 2009 §6).
hypotheses: accelerated (Syracuse) iteration, initial segment of trajectories, scaling limit
holds-here: yes — a rigorous result about typical initial behavior, not about all orbits
status: asserted
bearing: the strongest rigorous statement about typical orbit shape; still density/typical, not worst-case
anchor: research/summaries/kontorovich-lagarias-2009-stochastic-models.md
```

```claim
id: kl-5x1-divergence-conjecture
statement: For the 5x+1 map it is conjectured that a density-one set of integers lie on divergent trajectories, with finitely many periodic orbits including {1,3,8,4,2,...} — conjecturally different from 3x+1.
hypotheses: the 5x+1 map on integers
holds-here: no — different map, but contrast case for why 3x+1 shrinking is special
status: asserted
bearing: the contrast with q≥5 maps shows 3x+1's drift < 0 is what makes it special
anchor: research/summaries/kontorovich-lagarias-2009-stochastic-models.md
```
