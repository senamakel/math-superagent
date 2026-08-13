# ROOT — structure of this problem, from the library

Derived from the sources in `research/sources/`; every claim below has an `id` that appears in `research/CLAIMS.md` and an anchor file.

## The object

For each k ≥ 1 let

- `S_k = { r mod 3^k : the k low ternary digits of r lie in {0,1} }`, `|S_k| = 2^k`;
- `A_k = { n mod 2·3^(k-1) : 2^n mod 3^k ∈ S_k }`, the sieve set of exponents whose low k ternary digits of 2^n avoid 2;
- `A_∞ = { n : (2^n)_3 avoids digit 2 entirely }`.

`A_{k+1} ⊆ A_k` under the natural lift. The Erdős conjecture is `A_∞ = {0,2,8}`.

## The naive-count obstruction (stated before any approach)

`|A_k|` lives in the exponent ring Z/(2·3^(k-1))Z, which has ~2·3^(k-1) elements. If the 2^k residue classes of `S_k` were hit "uniformly" by the power map, `|A_k| ≈ 2·3^(k-1)·(2/3)^k = 2·2^k/3`, which **grows** like 2^k/3, not to zero. This is not a folklore heuristic: it is exactly the content of Narkiewicz's uniform bound (LAG-1, LAG-2): `|A_k| ≤ 2^(k-1)` for every k, matching the 2^k growth. **Any approach must beat this estimate or explain why it is wrong.** The only way it could be wrong is a structural correlation: the surviving classes of `A_k` must *share* a nontrivial arithmetic condition beyond "low digits avoid 2" — something broad like the class structure of n mod (2·3^(k-1)) being constrained by more than the count.

## What the sources establish

1. **Order/splitting structure (SAYE-2, proved):** 2 has order `u_k = 2·3^(k-1)` mod 3^k, and the k→k+1 digit rule is
   `d_{k+1}(2^(i·u_k + j)) ≡ d_{k+1}(2^j) + i·d_1(2^j) (mod 3)`, `0≤j<u_k`, `i∈{0,1,2}`.
   So a class j in A_k with representative power `2^j ≡ ε (mod 3)` (ε=1 or 2) splits into either
   - three children i with `d_{k+1}(2^j) + i·ε ≢ 2`, if d_{k+1}(2^j) + i·ε mod 3 avoids 2 for all three i (happens iff ε·i covers only values ≠2: that means d_{k+1}(2^j) ∈ {0,2} or {1} configuration — exact rule below), or
   - two children, or one child — but never zero (digit 2 in the new position is produced for exactly one i since ε is a unit).
   **A class in A_k never dies outright.** It survives to A_{k+1} in 1–3 children. So |A_k| is non-decreasing in the 2-adic growth sense unless the 1-child/2-child cases dominate.
2. **Narkiewicz's bound (LAG-1, LAG-2):** `N_1(X) ≤ 1.62 X^{α_0}` with α_0 = log_3 2; uniform 3-adic version `≤ 2 X^{α_0}`. Since α_0 < 1, `#{n ≤ X} = |A_k|` over a period of length 2·3^(k-1), with X = 2·3^(k-1), gives `|A_k| ≤ 1.62·(2·3^(k-1))^{α_0} ≈ 1.62·2^{α_0}·3^{α_0(k-1)} = 1.62·2^{α_0}·2^{k-1} ≈ 2^k·0.9…`, matching `2^k` up to a constant. **The growth is real and matches the naive estimate up to constant.**
3. **Sparse side settled (DH-1, proved):** beyond {0,2,8}, any solution must have ≥ 26 ones. So the sieve cannot die among few-ones solutions.
4. **Verification bound:** Gupta 1978 n<4374; Vardi n ≤ 2·3^20 ≈ 7×10^9; **Saye 2022 n ≤ 2·3^45 ≈ 5.9×10^21** (SAYE-1, verified-numerically).
5. **Dynamical/exceptional structure (LAG-3, LAG-4):** 3-adic and real exceptional sets have Hausdorff dimension log_3 2 at the first level and shrink for higher levels; the middle digits are untouched by both methods. Erdős conjecture ⟺ 1 ∉ E(ℝ+) ⟺ 1 ∉ E(ℤ_3).

## Structure of a minimal counterexample, as far as the library pins it down

Suppose n > 8 is a counterexample. Then:

1. n ∈ A_k for all k (by definition); in particular n mod 2·3^(k-1) survives every sieve level.
2. `2^n` has ≥ 26 ternary digits equal to 1 (DH-1, proved) and no 2s.
3. The first ternary digit of 2^n (its most significant) is 1 (since 2^n is between 3^m and 2·3^m for m = ⌊n·α_0⌋; and can't be 0 by definition of most significant; the digit 2 is forbidden, so it must be 1). Its least significant digit is the parity: 2^n is even for n≥1, so the last digit is 1 (since 0 mod 3 is impossible for a power of 2). Both ends are pinned.
4. n mod 2·3^(k-1) must lie in the survival set at every level, and the splitting rule SAYE-2 says the survival is *universal*: conceptually the class of n is a path in a 3-ary tree of depth k that never takes the "digit-2" child. The number of such paths at depth k is |A_k|.

The minimal-counterexample question is therefore: which paths in this tree survive forever? A single infinite path = a counterexample; three known paths = 0,2,8.

## The counting obstruction restated as a survival problem

Each node at depth k has 3 children, one of which is forbidden (produces digit 2 in position k+1). Counting alone gives expected |A_{k+1}| = 2·|A_k| → growth 2^k. Real survival |A_{k+1}|/|A_k| must be < 2 systematically. Since each node has exactly 3 children and exactly one is forbidden, the ratio |A_{k+1}|/|A_k| = (2·3^(k-1) surviving classes at depth k+1)/(3^(k-1)·3 classes total at depth k) aggregated... in the natural "each class splits into #(non-forbidden) children" accounting, #(non-forbidden) ∈ {1,2,3} and the average must be < 2 for |A_k| to decay. Narkiewicz says the average cannot be *much* less than 2 (it stays ≈ 2 - O(k/3^k) or so); beating Narkiewicz means showing the specific classes 0,2,8 are the only ones with *infinite* survival paths, not that the total count decays.

## Settled restricted classes (each with its hypothesis)

1. **n ≤ 2·3^45:** verified-numerically (Saye, SAYE-1). Hypothesis: none.
2. **Solutions with ≤ 25 ones:** only {0,2,8} (Dimitrov–Howe, DH-1, proved). Hypothesis: number of 1s ≤ 25.
3. **Solutions in the low-ones family general:** none beyond DH-1; the ≥26-ones case is open and is exactly the hard residual.
4. **3-adic λ-side:** for generic nonzero λ, #{n≤X} ≤ 2 X^{α_0} (LAG-2, proved) — a counting bound, not an existence statement.

## What would end the run (from GOAL.md, with the library's confirmation)

- A complete determination of A_k for some explicit k, with the classes of n=0,2,8 identified and the surviving classes listed. The best literature bound is |A_k| ≤ 2^(k-1); computing |A_k| exactly for k up to ~the largest feasible (Saye reached k≈46 by structure) is a fact about that k.
- A proof that |A_k| decays/stabilises with an explicit mechanism — must beat the Narkiewicz 2^k growth and name the mechanism.
- Reproduction of Narkiewicz's bound with explicit constant; or a located error.
- A proof restricted to a stated subclass of n (congruence class, range, family) with the hypothesis named.
- A precise statement of why the modular sieve cannot close.

## Open items worth requesting (feed REQUESTS.md)

- Narkiewicz's 1980 note full text (only JSTOR entry and secondary statements obtained so far; the JSTOR link https://www.jstor.org/stable/43667894 was not fetched).
- Gupta's 1978 original (Univ. Beograd series) — likely paywalled.
- Dupuy–Weirich (J. Number Theory 158 (2016) 268–280) full text — the Wieferich obstruction for digit-equidistribution; not yet in the library.
- Abram–Lagarias (J. Fractal Geom. 2014) for the 3-adic Cantor intersections.