# Directive 3: stop searching, convert, record the refutation

## What was done

The refutation of `check_regenerate_lemma.py` is now recorded in `code/out/check_regenerate_lemma.notes.md` with a fenced claim and exact k-values for both failure modes (IFF FAIL and REGEN FAIL). The oracle PASSED; the lemma FAILED.

TASKS.md was rewritten: the library-search tasks are gone, the two sharp facts from `regeneration_analysis.captured.txt` are stated precisely — (a) block length never approaches 0, minima are [13,24,96,97,175,2762,5939,31525,31533,31534,733574,1094263], smallest after the first few rows is 13 at k=3; (b) regeneration is real but not monotone (97→96, 871→872, 21→24 all occur). The honest open question — "is there a k with block length 0?" — is stated sharply. Next steps are concrete: characterise the rows at minima, state a new precise claim (the local iff approach is dead), attack it, and formalise in Lean.

CONTEXT.md was updated: the refutation under Ruled Out, the two facts under Numbers, the run state reworded to "library sufficient, search halted," and the Gaps section sharpened. The regeneration thread now reflects the refutation and the two facts. Both findings were filed in durable memory.

## What was not changed

The block lemma and all proved claims remain untouched — the refutation was of a candidate that had not been recorded as a claim, not of anything established. No programs were written or run.
## 3 — from steer

You ran check_regenerate_lemma.py and it REFUTED your candidate lemma, and you have recorded nothing. There is no claim in research/CLAIMS.md containing 'regener' or 'refut'. A refutation you do not write down is a refutation you will rediscover.

code/out/check_regenerate_lemma.captured.txt shows dozens of failures of two distinct kinds:
[IFF FAIL] at k=3,5,6,7,8,15,17,19,20,21,23,24,25,26,27,28,29,... every one with q in {0,2}=True but rhs=False. So your proposed iff is false in the direction you need: the left side holds and your right side does not. That is not a near miss, it is the wrong characterisation.
[REGEN FAIL] at k=3 (13->13), k=8 (21->24), k=11 (97->96), k=13 (97->96), k=15 (173->175), k=17 (175->175), k=19 (175->290), k=23 (739->873), k=26 (871->872).

Write both up NOW as status: refuted, with the exact k values, in a note beside the capture. Do not weaken the statement and re-assert it. Note the oracle itself PASSED (first 40 rows block lengths and second entries match witnesses.json), so the failures are the lemma's, not the instrument's.

Then look at what your own data actually says, because it is more interesting than the lemma you tried. From code/out/regeneration_analysis.captured.txt the record of minimum block lengths is [13,24,96,97,175,2762,5939,31525,31533,31534,733574,1094263] and the dwell at each minimum is 1 to 4 rows. Two facts to state precisely and separately: (a) the block length never approaches 0 over the range computed - the smallest ever seen is 13, at k=3, and minima grow rapidly after; (b) regeneration is real but NOT monotone - 97->96 and 871->872 and 21->24 all occur, so consumption and regeneration alternate.

The honest open question is now sharp: is there a k with block length 0. Everything you have says no and nothing you have proves it. State it that way.

exa_search 25->37 and frontier 309->345 while checked stayed at 3. Stop searching and convert.

The directive is carried out. Here is what changed and why:

- **`code/out/check_regenerate_lemma.notes.md`** — created with a fenced claim recording the refutation, exact k-values for both IFF FAIL and REGEN FAIL modes, and the conclusion that the local iff approach is dead.

- **`TASKS.md`** — rewritten from top to bottom. Library-search tasks are removed. The two sharp facts from the data are stated precisely: (a) minima `[13,24,96,97,175,...]`, smallest 13 at k=3; (b) regeneration alternates (97→96, 871→872, 21→24). The honest open question — "is there a k with block length 0?" — is stated sharply. Next steps are concrete characterisation, not searching.

- **`CONTEXT.md`** — the refutation under Ruled Out, the two facts under Numbers, the run state reworded to "library sufficient, search halted," the Gaps section sharpened with the open question first.

- **`research/threads/regeneration.md`** — metadata updated to reflect the refutation; body rewritten around the two facts and the open question.

- **Durable memory** — both the refutation and the two data facts filed so future roles do not rediscover either.

Nothing was weakened or re-asserted. No programs were written or run. The library search is halted: FRONTIER.md stays at 309→345 with checked at 3, and the directive to stop searching and convert is now the run's stated position in every file that carries it.
