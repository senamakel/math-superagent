# arXiv:2607.04166 was dismissed on its abstract page; the full PDF contains a usable reduction

## What went wrong first

`research/sources/granville-2026-piercing-gilbreath-arxiv.full.md` is 6.8 KB and is the
arXiv **`/abs/` landing page**, not the paper: title, categories, submission history,
navigation links, zero occurrences of theorem/lemma/proof. On that basis the ledger
carries `granville-2026-piercing-gilbreath-not-load-bearing` as `asserted`, described as
"claim-heavy non-peer-reviewed note ... presents no result this run can use".

The actual PDF is 2,732 lines with 70 theorem/lemma/proposition/proof occurrences. It has
now been fetched with `pdftotext -layout` and stored at
`research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md`. The dismissal was
made without reading the paper and must be revisited.

## What the paper actually proves

Notation is the *right diagonal*: `delta_0(q_n) = q_n`, `delta_1(q_n) = g_n = q_n - q_{n-1}`,
`delta_k(q_n) = |delta_{k-1}(q_n) - delta_{k-1}(q_{n-1})|`. This is our triangle read along
the diagonal through `q_n`: `delta_k(q_n) = A_k[n-k]`. The "0-2 cycle" is the maximal
`{0,2}` tail of that diagonal, and `nu_2(q_n)` counts the 2s in it.

**Lemma 5.4** (p. 16). If `q_1..q_{n-1}` is valid and successful, then `q_1..q_n` also
succeeds provided

    g*_n <= 2 * nu_2(q_{n-1}) + 2,        g*_n = max(g_2, ..., g_n)  (the record gap).

The proof is a runway argument: inside the gray block each step of the new diagonal either
holds or drops by 2, so `nu_2` twos supply `2*nu_2` of descent, and `v_n <= g*_n` is the
demand. Stated as iff on `v_n`, then weakened to `g*_n` since `v_n < g*_n`.

**This is our own budget inequality in different coordinates.** Ours is
`Sum(j_i + 1) >= k - 2`: regeneration supply against erosion demand. His is
`2*nu_2 + 2 >= g*_n`: descent supply against record-gap demand. Same shape, different
bookkeeping — and his demand side is the *prime gap*, which is where the literature is.

**Theorem 5.5** (p. 16). If `g*_n < n^alpha` and `nu_2(q_{n-1}) > n^beta` with `beta > alpha`,
then for `n` large the sequence succeeds at `q_n` whenever it succeeds at `q_{n-1}`.

The demand side is **unconditional for primes**: `alpha = 0.525` by Baker-Harman-Pintz
(2001), cited correctly. So the entire remaining content is a **lower bound on `nu_2`**.
Granville does not prove one. He offers `beta = 0.99` by appeal to his own Conjecture 5.1,
and the heuristic `nu_2 ~ n/2`, and an analogy to digit-counting in normal numbers.

## Measuring nu_2 on our own primes

`code/nu2_granville_check.py`, run by the operator on the host (CPython, exact integers,
no sympy), primes below 3e6, diagonals through columns up to n = 3999. Capture at
`code/out/nu2_granville_check.captured.txt`:

**In-container reproduction (this run, 2026):** `code/nu2_granville_check.py` re-run
in-container (timeout 540, EXIT_CODE=0) reproduces every number below exactly, and the
independent route `code/verify_nu2_claim.py` (different sieve/row order) and
`code/verify_granville_nu2_independent.py` (lib.gilbreath rows_generator + prefix-max g*)
both agree identically. Captures: `code/out/nu2_granville_check.captured.txt`,
`code/out/verify_nu2_claim.captured.txt`,
`code/out/verify_granville_nu2_independent.captured.txt`. All exact integers, single
worker, well under the 8 GiB cap.

    n      nu2      n^0.525    n/2     nu2/n    g*     2*nu2+2   Lemma5.4 hyp
    50     26       7.8        25.0    0.520    14     54        holds
    100    42       11.2       50.0    0.420    18     86        holds
    200    98       16.1       100.0   0.490    22     198       holds
    400    203      23.2       200.0   0.507    34     408       holds
    800    389      33.4       400.0   0.486    34     780       holds
    1600   785      48.1       800.0   0.491    36     1572      holds
    3200   1604     69.2       1600.0  0.501    52     3210      holds
    3999   2048     77.8       1999.5  0.512    72     4098      holds

`nu_2/n` sits at 0.49-0.52 across two orders of magnitude — the `n/2` heuristic, not merely
`n^beta` for some `beta > 0.525`. At n = 3999 the theorem needs `nu_2 > 78` and the true
value is 2048, a factor of 26. Lemma 5.4's hypothesis holds at every sampled n with two
orders of margin (record gap 72 against a budget of 4098).

```claim
id: granville-nu2-density-measured
statement: For the right diagonal through q_n of the prime Gilbreath triangle, the count nu_2(q_n) of 2s in the maximal {0,2} tail satisfies nu_2/n in [0.42, 0.52] for n in {50,100,200,400,800,1600,3200,3999}, consistent with nu_2 ~ n/2 and exceeding n^0.525 by a factor of 26 at n=3999. Granville's Lemma 5.4 hypothesis g*_n <= 2*nu_2(q_{n-1}) + 2 holds at every sampled n, with record gap 72 against budget 4098 at n=3999.
hypotheses: primes below 3e6; diagonals delta_k(q_n) = A_k[n-k] for k=0..n-1; 0-2 cycle taken as the maximal {0,2} suffix of delta_2..delta_{n-2}; exact integer arithmetic
holds-here: yes
status: checked
bearing: The gap in arXiv:2607.04166 Theorem 5.5 is a lower bound nu_2 > n^beta with beta > 0.525. Empirically nu_2 ~ n/2, so the needed bound is far from tight and the target is a density statement about 2s in a diagonal rather than a statement about prime gaps, whose side is already unconditional via Baker-Harman-Pintz alpha = 0.525.
anchor: code/out/nu2_granville_check.captured.txt, research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md
source: operator-computation
```

## Rigor: do not adopt any of this, re-derive it

The paper is cs.CR, self-published through BondingAI.io, not peer reviewed, and its
standard of proof is uneven. Theorem 2.5's proof reads in full: "Take kappa_0 = 0 and the
theorem is proved! For kappa_0 = 1, the proof should be quite easy: the difficult step
is ..." — that is not a proof. Lemma 5.4's proof argues from a coloured table and discards
a case with "we can ignore that exception". Theorem 5.5's `beta` is sourced from the
author's own Conjecture 5.1, so the theorem is conditional on an unproved claim of his own.

Lemma 5.4 nevertheless looks correct and elementary, and it is the piece worth having. It
should be re-derived from scratch here, with the `delta_{k-1}(q_n) = 0` case handled
explicitly rather than waved through, before anything cites it.
