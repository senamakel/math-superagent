# Librarian audit — thread "resting on nothing" flags are now resolved

## What was flagged

`derived/THREADS.md` for `split_and_sum_search` carried warnings that the
thread "rests on nothing recorded":

- `snumber-sum-oracle` — no claim block on disk established it
- `a104113-bfile-cover` — no claim block on disk established it

Both warnings were real at the time: each was referenced by threads/summaries
before the claim that establishes it existed.

## What I found (this cycle)

Both are now established, with a real anchor, on the claims ledger:

- `snumber-sum-oracle` → `code/out/oracle.md` (status **checked**). The brute
  oracle's claim block is there verbatim: reproduces the four worked examples
  with witness splits and T(10^4)=41333 with the set
  {81,100,1296,2025,3025,6724,8281,9801,10000}.
- `a104113-bfile-cover` → `research/summaries/oeis_a104113_b.md` (status
  **catalogued**). The A104113 b-file's first 408 terms are exactly the
  S-numbers <= 10^12 (term 408 = 10^12).

`grep_workspace` for both ids shows the anchor files containing their claim
blocks. The warnings in the rendered THREADS.md are stale; the next write of
that derived file (which happens whenever `research/threads/*.md` is touched)
will regenerate cleanly.

## Audit conclusion for this cycle

The reference library is complete for this run and internally consistent:

- **Canonical tier on disk:** OEIS A004113 (S-numbers) and A038206 (roots,
  with b-file to the full 10^12 cover), A006886 (Kaprekar), plus the two-block
  theory (Iannucci, Black, Dudeney, Javaheri, Hamilton), ProofWiki digit-sum
  bound, Butler–Graham–Stong "Partition and sum is fast" (mod b-1 invariance),
  and the distinct-class records (S.P numbers, SSPDS) filed as dead ends.
- **Every summary carries a real source URL** and the final answer is recorded
  as `t-final-answer` (checked) in `code/out/final_answer.md`, verified by
  three independent routes: the digit-partition recursion, the A038206 b-file
  sum of squares, and a full 10^12 meet-in-the-middle run — all
  = 128088830547982.
- **No open requests** in the requests ledger; the FRONTIER's top rows are
  OEIS Foundation infrastructure and false-positive research leads already
  triaged in `librarian-dead-ends.md`.

Nothing further to fetch for this problem.
