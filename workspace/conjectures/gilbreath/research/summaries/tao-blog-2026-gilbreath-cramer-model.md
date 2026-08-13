# Tao blog 2026-07-11 — Gilbreath's conjecture: a Cramér random model and a deterministic analysis

**Full text:** `research/sources/tao-blog-2026-gilbreath-cramer-model.full.md` [[tao-blog-2026-gilbreath-cramer-model.full]]
**Source:** https://terrytao.wordpress.com/2026/07/11/gilbreaths-conjecture-a-cramer-random-model-and-a-deterministic-analysis/

## What it is

Tao's expository announcement of the Chase–Hunter–Tao 2026 arXiv:2607.08712 paper. The mathematical content is exactly the paper — see `summaries/chase-hunter-tao-2026-full-html.md` for the statements (Cramér model Theorem 1.2, general model Theorem 1.3, continuous model c_i / 1/i floor, deterministic inverse Theorem 1.6, the two obstruction scenarios of long zero-blocks and long shallow {0,d}-blocks). The post adds the **frame**: GC as a discrete nonlinear "wave equation" in 1+1 dimensions, initial data = primes = space-time scalar field, equation of motion the absolute difference. The 2-separated avoidance iterate: the preimage under a↦|a−c| of a 2-separated set is 2-separated (the Lemma 3.11 separation lemma, stated informally).

The two obstruction scenarios are explained concretely: (1) a long run of zeroes stops the neighbouring entries from decreasing; (2) an extremely long two-valued {0,d} block persists for a time equal to its length (for even d needing joint independence heuristics; for odd d the parity identity |a−b|=a+b mod 2 rules it out probabilistically).

## Distinct added content — the comments (NOT the paper)

Three commenters add quantitative refinements, all cited here as comment-level, not peer-reviewed:

- **Michael M. Ross**: extended the exact rational constants c_i to c_4, c_5, c_6 (sign-cone simplex decomposition; github.com/michaelmross/Gilbreath); published as **OEIS A397880 and A395556** (29 Jul 2026). TAO confirmed excellent fit with Monte Carlo and that no OEIS entry existed. So the library's OEIS A397880/A395556 summaries relate to these c_i values.
- **Emmanuel Audigé**: exact 2-separated concentration for a geometric X, Λ_2(X)=1/(2−p), unique extremizer A=2ℤ; exact cutoff-parity law Λ_2(X_D)=1/(2−p)(1+(−1)^D p q^{D+1}/2); plugged into CHT Prop. 4.1 gives explicit finite-n failure bound with threshold δ* = 0.0370366917265559, e.g. δ=0.03 gives P(a(n−1,1)>1) ≤ n exp(−(0.06+o(1))n/log n) + exp(−(0.0536121728…+o(1))n).

## Hypotheses / bearing

Duplicate of the CHT paper for the theorems. The comments quantify the 2-separated concentration constant in the Cramér model — directly usable if the run ever wants a concrete probability bound in a random-model comparison, and matches the `two-separation-hypothesis` claim. Neither the paper nor the blog settles the prime case (heuristic support only); the Audigé/δ* and Ross/c_i results are unverified here.

## Claims

```claim
id: tao-cramer-blog-frame
statement: GC is the absolute-difference (nonlinear 1+1 wave-equation) dynamics on the primes; its only generic obstructions to decay are long zero-blocks and very long shallow {0,d}-blocks; the 2-separated-avoidance iterate (preimage of a 2-separated set under |x−c| is 2-separated) is the mechanism ruling the probability of such blocks.
hypotheses: as in CHT 2026 (Cramér bounds are conjectural for the primes).
holds-here: yes as model/heuristic; prime case unproved.
status: asserted (expository; identical to arXiv:2607.08712)
bearing: frames the obstruction hunt; the separation iterate is a reusable elementary tool.
anchor: research/sources/tao-blog-2026-gilbreath-cramer-model.full.md
```

```claim
id: tao-2sep-exact-geometric
statement: For a geometric X with P(X=k)=pq^k, the maximal probability over 2-separated sets is Λ_2(X)=1/(2−p), uniquely attained at the even integers 2ℤ; with cutoff at D the law is Λ_2(X_D)=1/(2−p)(1+(−1)^D p q^{D+1}/2). Plugging into CHT Prop. 4.1 gives an explicit failure bound with threshold δ*=0.0370366917265559.
hypotheses: geometric Cramér model, D=⌊δn⌋ cutoff.
holds-here: as a commenter's computation in the model; unverified here.
status: asserted (blog comment, E. Audigé, not peer-reviewed)
bearing: concrete constant if a quantitative random-model failure rate is needed.
anchor: research/sources/tao-blog-2026-gilbreath-cramer-model.full.md
```
