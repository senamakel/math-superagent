# Tao blog 2026-07-14 — Visualizing the Gilbreath expectation sequence

**Full text:** `research/sources/tao-blog-2026-visualizing-gilbreath-expectation.full.md` [[tao-blog-2026-visualizing-gilbreath-expectation.full]]
**Source:** https://terrytao.wordpress.com/2026/07/14/visualizing-the-gilbreath-expectation-sequence/

## What it establishes

Expository companion to the Chase–Hunter–Tao 2026 paper, focused on **c_n** (the "Gilbreath expectation sequence"): in the continuous Gilbreath array (top row = n+1 i.i.d. mean-1 exponentials, entries = absolute differences below), the i-th row entries all have expectation c_i (stationarity). Conjecturally the k-th row of the normalized-prime-gap array decays like c_k·log n/2, so GC is tied to how fast c_k decays.

- **Exact rational values:** c_0=1, c_1=1, c_2=7/9, c_3=227/288 (orange line). Michael Ross extended to c_4,c_5,c_6 (good Monte-Carlo fit) — github.com/michaelmross/Gilbreath.
- **Ross's empirical prediction** (Zenodo preprint, https://zenodo.org/records/21326026): c_n ≈ C·λ^{s_2(n)}/n with λ≈1.17 empirically, where s_2(n)=#ones in binary expansion of n — intended to explain c_n's non-monotonicity via the Thue–Morse-like fluctuation of s_2.
- **Sierpinski/Rule-90 link:** a single "spike" (all-zero initial data except one entry) generates a Sierpinski gasket; the number of 1s in the k-th row is 2^{s_2(k)} ("Gould's sequence"); links to Lucas'/Kummer's theorems. Observed: fragments of Sierpinski gaskets appear and decay via collisions.

## Hypotheses / bearing

The post's mathematical content is entirely about the continuous random model and the Rule-90/Sierpinski parity structure of the halved triangle — it confirms the run's `rule90-identification-real-absorption-refuted` and `cht-decay-lower-bound-logn` claims, and the Ross prediction is a *conjectural* empirical law (λ≈1.17, s_2-based), NOT proved. Relevant background for why the {0,1}-halved triangle is a Pascal-mod-2 (Rule-90) system whose spike responses are Sierpinski; does not settle regeneration of {0,2} blocks in the integer triangle. Comments add Rule-90/Cellular-Automaton references (Miyamoto 1979/1994, Lind 1984, Takei 2017) for the stationary measures of rules 90/150.

## Claims

```claim
id: gilbreath-expectation-sierpinski
statement: In the continuous (i.i.d. exponential) Gilbreath array, row-i entries have common expectation c_i (c_0=1,c_1=1,c_2=7/9,c_3=227/288); a single-spike array gives a Sierpinski gasket whose k-th row has 2^{s_2(k)} ones (Gould's sequence); Ross's empirical law is c_n≈C·λ^{s_2(n)}/n, λ≈1.17.
hypotheses: continuous model; single-spike initial data for the Sierpinski statement.
holds-here: as model/heuristic; Ross's c_n law is empirical-unproved.
status: asserted (Tao expository; c_0..c_3 exact in CHT; Ross law conjectural)
bearing: explains c_n non-monotonicity via s_2 (Thue-Morse-type) fluctuations; corroborates Rule-90/Sierpinski structure of the halved triangle.
anchor: research/sources/tao-blog-2026-visualizing-gilbreath-expectation.full.md
```
