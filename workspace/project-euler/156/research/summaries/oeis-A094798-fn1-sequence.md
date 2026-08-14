# OEIS A094798 — f(n,1), the number of 1's in writing 1..n

**Source:** https://oeis.org/search?q=A094798&fmt=text (OEIS catalogue entry, witnessed). Full text: `research/sources/oeis-A094798-fn1-sequence.full.md`.

## What it establishes

- A094798: a(n) = number of times 1 is used in writing out all numbers 1 through n. This is exactly the run's f(n,1) with the 0..n vs 1..n origin difference (0 contributes no 1s, so equal for all n).
- Values (cross-check targets): a(1..12) = 1,1,1,1,1,1,1,1,1,2,4,5 — matches the statement's f(n,1) table shifted by the origin (statement lists f(0,1)=0 and f(1..12)).
- a(9), a(99), a(999), ... = 1, 20, 300, 4000, ... (A053541), i.e. f(10^k − 1, 1) = k·10^(k−1) — the same identity repeated in every source.
- a(n) = Σ partial sums of A268643 (number of 1-bits-... actually A268643 = number of 1's in the decimal representation of n, per Robert Israel's comment: A094798 = partial sums of A268643).
- **Generating function (Robert Israel, corrected Visonà):** g(x) = x/((1−x)(1−x^10)) + ((1−x^10)/(1−x))^2 · g(x^10). This is a self-similar/formula route to f(n,1) usable as an independent third implementation.
- Fixed points of A094798 are A014778 (David Wasserman).

## Implications for PE156

- Independent catalogue confirmation of the d=1 counting function and its values, useful as oracle cross-checks (a(12)=5 etc.) and as a second implementation route (the generating-function recurrence).
- Establishes nothing about d=2..9 or the sums; the answer values are not in this entry (they live in A216398, which is excluded).

## Does not settle

- Nothing about solution counts, bounds, or sums for d ≥ 2; those are the paper's Table 2 and the (excluded) A216398.