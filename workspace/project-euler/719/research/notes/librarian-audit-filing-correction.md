# Librarian audit — canonical-tier filing corrected

One real defect found and fixed, plus one missing claim supplied.

## 1. A104113 record page was misfiled

The full OEIS A104113 record page — the canonical statement of the S-number
definition, the page that *links Project Euler 719 itself* and carries
Branicky's exact `expr` digit-partition recursion used by `code/solution.py` —
was filed as

    research/summaries/oeis_a110113_full.md

That is wrong on two counts: the sequence ID is A104113 (A110113 is a
different/nonexistent id), and a "full" text belongs in `research/sources/`,
not `research/summaries/`. Worse, the summary stub `oeis_a104113.md` still said
"Filed by an OEIS lookup, not read", so the run's own summary of its canonical
source claimed not to have read it. A search for "A104113 full" would have
missed the one page that establishes the definition.

**Fix.** Correctly named full text now at
`research/sources/oeis_a104113.full.md` (source https://oeis.org/A104113/internal),
indexed. The old `oeis_a110113_full.md` path is now a short pointer note so the
stale link resolves instead of dangling. Summary upgraded at
`research/summaries/oeis_a104113.md`. Also fixed the stale `[[oeis_a110113_full]]`
link in `oeis_a104113_b.md` → `research/sources/oeis_a104113.full.md`.

## 2. Missing claim a104113-bfile-cover

`research/threads/split_and_sum_search.md` and
`research/backward/pe719-root-enumeration.md` both reference
`a104113-bfile-cover` as something the thread rests on, but no claim block on
disk established it — the derived `THREADS.md` "Resting on nothing recorded"
warning flagged exactly this. **Fix:** the claim is now recorded in
`research/summaries/oeis_a104113_b.md`: the A104113 b-file's first 408 terms
are exactly the S-numbers ≤ 10^12 (term 408 = 10^12), so T(10^12) = sum of
those 408 terms. `search_claims` returns it.

## 3. No other provenance problems

Audited every full-text source in `research/sources/` and all 33 summaries for
their `source:` lines. All 17 source files carry a real, verifiable URL that
matches their filename. The library is otherwise complete and the final answer
T(10^12)=128088830547982 stands double-verified (solution.py recursion vs
A038206 b-file sum of squares, `code/out/final.log`).

## Lesson

When a memory names a file (`oeis_a110113_full`) that the summary stub for the
*correct* id still says it has not read, that is a misfile, and it propagates:
a future librarian `recall_memory`-ing "A104113" would have been told the run
holds it, opened the stub, and found "not read". Filing the full text under the
right id in `research/sources/` with the source URL on line 1 is what ends the
propagation.