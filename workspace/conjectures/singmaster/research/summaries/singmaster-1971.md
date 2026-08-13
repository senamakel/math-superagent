# Singmaster 1971 — How often does an integer occur as a binomial coefficient?

Source: D. Singmaster, Amer. Math. Monthly 78 (1971) 385–386; primary facsimile read
(fermatslibrary, with the JSTOR page reproduced). [[singmaster-1971]]

## What the paper establishes

- **Definition**: `N(a)` = number of times `a` occurs as `C(x,y)`. `N(1)=∞`;
  `N(2)=1`, `N(3)=N(4)=N(5)=2`, `N(6)=3`, etc. For `a>1`, `N(a)<∞`.
- **Proposition**: `N(a) = O(log a)`. Proof: let `b` be first with `C(2b,b)>a`;
  `C(i+j,j)=a` forces `i<b` or `j<b` (monotonicity in each argument); for each `i`
  (or `j`) there is at most one solution; so `N(a) ≤ 2b`. From `C(2(b-1),b-1)≥2^{b-1}≤a`
  get `b ≤ 1+log₂a`; hence `N(a) ≤ 2+2log₂a = O(log a)`.
- **Conjecture**: `N(a)=O(1)`. Records that Erdős concurs and says it must be very
  hard, and later suggested (in correspondence) trying to show `N(a)=O(log log a)`
  — i.e. even the correct order might be slower than the log bounds.
- **M(k)** (first `a` with `N(a)=k`): M(1)=2, M(2)=3, M(3)=6, M(4)=10, M(6)=120.
- **"Added in proof" (primary witness frame)**: `M(8)=3003`, the ONLY solution to
  `N(a)≥8` with `a<2^23`; the six solutions to `N(a)=6` with `a<2^23` are
  120, 210, 1540, 7140, 11628, 24310.
- Note: `3003 = C(3003,1)=C(78,2)=C(15,5)=C(14,6)` (from the article's marginal
  discussion): twice in its own row, twice in row 78, twice in rows 14/15.

## Caveat / minor source issue

The Fermat's Library annotation comment states the "current best bound" (2007) as
`N(t) = O((log t)(log log log t)/(log log t)^2)` — exponent **2**. This contradicts
all authoritative sources (MRSTT, Jenkins, Wikipedia, Kane's own paper) which give
exponent **3**. This is the same transcription slip already recorded in
`research/notes/established-review.md`; **exponent 3 is correct** (Kane 2007).

## Bearing for this run

Primary source for the `O(log a)` bound, the original conjecture, and the
`a<2^23` witness frame (`N(3003)=8`, six `N=6` values). Independent confirmation of
the witnesses that `code/out/witnesses.json` reproduces. The `O(log a)` bound grows
in `a` — not a result toward the constant, but the historical baseline.

```claim
id: singmaster-1971-original
statement: Singmaster 1971 (AMM 78, primary source): N(a)=O(log a) via N(a)<=2+2 log_2 a
  (b with C(2b,b)>a forces i<j<b); conjecture N(a)=O(1); M(8)=3003 is the only
  N(a)>=8 with a<2^23, and the six N(a)=6 values <2^23 are 120,210,1540,7140,11628,24310.
hypotheses: a>1; N counts C(x,y)=a over positive x,y (both symmetric copies).
holds-here: yes — the original bound and witness frame.
status: sourced (primary facsimile read; witnesses match witnesses.json)
bearing: O(log a) is the baseline (grows with a, not a result); the witness frame
  independently confirms N(3003)=8 and the six N=6 values.
anchor: research/summaries/singmaster-1971.md
```
