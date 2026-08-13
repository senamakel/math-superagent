# Refuted: candidate regeneration lemma

**Status: refuted** by `check_regenerate_lemma.py` against the actual prime Gilbreath rows (sieve to 2e7, 1.27e6 primes, depth 1000).

## What was tested

A candidate `iff` characterising when regeneration occurs — the claim was that some property `rhs` of the row (involving the intruder `c`, the block length `b`, and the second entry `e`) is equivalent to the second entry staying in `{0,2}`. The oracle PASSED (first 40 rows block lengths and second entries match `witnesses.json`), so the failures are the lemma's.

## Two distinct failure modes

### [IFF FAIL] — the `iff` is false in the direction needed

At rows k=3,5,6,7,8,15,17,19,20,21,23,24,25,26,27,28,29,... and many more:
`q_in{0,2}=True` (the left side holds — the second entry *is* in `{0,2}`) but `rhs=False` (the right side does not hold). So the proposed right-hand-side is not necessary for the second entry to be in `{0,2}` — the `iff` fails in the direction the lemma needs.

### [REGEN FAIL] — the lemma's regeneration prediction mismatches reality

At rows where the lemma's right-hand-side would predict regeneration but the block length does not actually increase (or decreases):
- k=3: b stays 13→13 (lemma predicted regen)
- k=8: b goes 21→24 (lemma predicted erosion)
- k=11: b goes 97→96 (lemma predicted regen)
- k=13: b goes 97→96
- k=15: b goes 173→175
- k=17: b goes 175→175
- k=19: b goes 175→290
- k=23: b goes 739→873
- k=26: b goes 871→872
- and many more through k=161

## What survives

The oracle is sound. The data the lemma was tested against is correct. The lemma itself is wrong — both directions of its `iff` fail systematically across the computed rows. It is not a near miss; it is the wrong characterisation.

## Next

Do not weaken and re-assert. The honest open question remains: is there a k with block length 0? Everything computed says no; nothing proves it.

```claim
id: candidate-regeneration-iff-refuted
statement: A candidate iff characterising block-length regeneration (q_in{0,2} ⇔ rhs, where rhs involves the intruder c, block length b, and second entry e) was tested against the actual prime Gilbreath rows to depth 1000 and refuted. The → direction fails at k=3,5,6,7,8,15,17,19,20,21,23,24,25,26,27,28,29,... (q_in{0,2}=True but rhs=False). The ← direction fails at k=3,8,11,13,15,17,19,23,26,... (lemma predicts regen but block does not grow, or predicts erosion but block grows).
hypotheses: none that survive — the lemma itself is what was tested
holds-here: no — refuted
status: refuted (test run captured at code/out/check_regenerate_lemma.captured.txt; oracle PASSED, lemma FAILED)
bearing: the iff approach to characterising regeneration by a single-row property of the intruder and block length does not work. Regeneration is not a local property of the current row alone.
anchor: code/out/check_regenerate_lemma.notes.md
```