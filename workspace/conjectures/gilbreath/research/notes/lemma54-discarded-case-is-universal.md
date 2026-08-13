# Granville's Lemma 5.4 discards a case that occurs in 100% of rows

## What was tested

`code/lemma54_iff_check.py`, run by the operator on the host (CPython, exact integers, no
sympy). Primes below 2e6, diagonals `delta_k(q_n) = A_k[n-k]` through columns n = 20..2499,
2480 columns tested. Capture: `code/out/lemma54_iff_check.captured.txt`.

**In-container reproduction (this run, 2026):** the script was re-run in-container
(timeout 540, EXIT_CODE=0) and the independent route
`code/verify_granville_nu2_independent.py` (lib.gilbreath generator, entry-level zero
statistics) reproduces the four numbers below identically and adds the finer grain: of
3,095,143 gray-block entries across the 2480 columns, 1,546,291 (50.0%, avg 623.5 per
block) are 0 — the discarded `delta=0` case is not merely present per row, it is the
dominant entrywise regime of the block. Captures: `code/out/lemma54_iff_check.captured.txt`,
`code/out/verify_granville_nu2_independent.captured.txt`.

The 0-2 cycle of `delta(q_{n-1})` is its maximal `{0,2}` suffix before the terminal entry;
`tau_n` is where that cycle starts, `nu_2` counts the 2s in it, and `v_n = delta_{tau_n}(q_n)`
is the yellow value his Table 13 calls unknown.

## Result

    tested n: 2480   all successful: True (2480)
    iff  v <= 2*nu2+2  <=>  success : violations = 0
    suff g* <= 2*nu2+2  =>  success : violations = 0
    rows where the discarded delta=0 case actually occurs: 2480 (100.0%)

## The finding

In the proof of Lemma 5.4 (p. 16 of arXiv:2607.04166) the descent argument runs
`delta_k(q_n) in {delta_{k-1}(q_n) - 2, delta_{k-1}(q_n)}` **"unless `delta_{k-1}(q_n) = 0`.
We can ignore that exception: when it happens, success is guaranteed."**

That exception is not an exception. A zero appears inside the gray block on **every one of
the 2480 columns tested — 100%**. The generic case is the one the proof sets aside, and the
clean two-cases-only descent it relies on never actually occurs. His parenthetical "success
is guaranteed" is asserted, not argued, and it is carrying the whole lemma.

This does not refute the lemma. The conclusion holds everywhere tested. It means the
published proof does not establish it, and the repair — showing that a zero inside the block
really does guarantee success, in general rather than by inspection — is the actual work.

## What this test could NOT do, stated plainly

Every real prime column succeeds, because Gilbreath holds this far. So `success` is
constantly true over the sample, and the biconditional `v_n <= 2*nu_2 + 2 <=> success`
was confirmed only in the direction where both sides are true. **The test cannot exercise
the failure direction at all**, and reporting "iff violations = 0" as support for the
biconditional would be the same vacuity that `check_edge_zero_run.py` was caught in.

To test the iff, the sufficiency threshold has to be approached from the failing side, on
sequences that do fail — Granville's own "closest failing sister" construction (his section
5.1) or synthetic Poisson-gap sequences (his section 4). That is the experiment worth
building.

```claim
id: lemma54-discarded-case-universal
statement: In the proof of Lemma 5.4 of arXiv:2607.04166 the descent step delta_k(q_n) in {delta_{k-1}(q_n)-2, delta_{k-1}(q_n)} is claimed to hold "unless delta_{k-1}(q_n)=0", an exception the author discards. On primes below 2e6, a zero occurs inside the relevant block on 2480 of 2480 columns tested (100%). The discarded case is the generic case, so the published proof does not establish the lemma, although the lemma's conclusion and its hypothesis g*_n <= 2*nu_2(q_{n-1})+2 hold on all 2480 columns.
hypotheses: primes below 2e6; columns n=20..2499; delta_k(q_n) = A_k[n-k]; 0-2 cycle = maximal {0,2} suffix before the terminal entry; exact integer arithmetic
holds-here: yes
status: checked
bearing: Lemma 5.4 must be re-proved here before anything cites it, with the delta=0 case handled as the main case rather than an exception. The lemma's statement is not in doubt; its proof is.
anchor: code/out/lemma54_iff_check.captured.txt, research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md
source: operator-computation
```

Verify independently before adopting: reproduce the four numbers above in-container
(2480, 0, 0, 2480) and confirm the zero-detection window matches his `[tau_n, n-1)`.
