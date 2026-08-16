# Attack the three-set rung via finite model finding — encoding correctness

```thread
id: three-set-refute-encoding
question: Does the bounded-fragment TPTP encoding code/refute/uc_with_three_set.p
  genuinely refute R-uc-with-three-set, or is the CounterSatisfiable verdict an
  artifact of slot collapse?
status: dead
rests-on: bosnjak-markovic-11, verified-n12-comp
blocked-by: none
next: |
  (1) Re-read code/refute/uc_with_three_set.p and confirm it asserts (a)
      union-closure for ALL pairs of member slots, (b) the abundant element
      ranges over the whole ground set {e1,e2,e3,e4}, not just {x,y,z}, and
      (c) the counting semantics of 'at least |F|/2 = 3 members'.
  (2) Decode the produced counter-model
      (code/out/refute/code_refute_uc_with_three_set.p.json) into a bitmask
      family and run it through the canonical oracle code/lib/uc.py:
      decide_union_closed and abundance/abundant_elements.
  (3) If the oracle rejects it, the encoding is wrong — fix it (assert the six
      slots pairwise distinct) or delete the artifact so it cannot be mistaken
      for a result. Keep R-uc-with-three-set open unless the oracle says
      otherwise.
```

## Why this direction

`R-uc-with-three-set` is the weakest open rung of the Frankl ladder (see
`research/WEAKENED.md`). The `code/refute/` encoding attacks it as a bounded
finite question: ground set of 4 elements, a family of exactly 6 distinct
members containing `{e1,e2,e3}`, union-closed, with no element in ≥3 members.
A model finder returned `finding=refuted`, `status=CounterSatisfiable`.

That verdict cannot be a genuine refutation: any union-closed counterexample on
a 4-element ground set would refute the conjecture at n ≤ 12, contradicting
`bosnjak-markovic-11` and `verified-n12-comp` (both in `research/CLAIMS.md`).
Operator directive: assume the encoding is missing an axiom.

## What the artifact already shows (to confirm, not take on faith)

The produced model maps the six member slots onto only three distinct domain
values — `s1 = s2 = s3 = s4` — and no axiom in `uc_with_three_set.p` asserts the
six slots are pairwise distinct. The counting axioms `no_abundant_e1..e4` and
the conjecture `goal` both require *three distinct* slots to share an element,
and `slots_distinct_sets` only requires *unequal* slots to differ, so all three
become vacuous once slots collapse. The model's "family" is therefore three sets
(`{e1,e3}`, `{e1,e2,e3}`, `∅`), not six.

## What would falsify it

If the oracle (`code/lib/uc.py`) reports the decoded family as union-closed
*and* without an abundant element, then the artifact is a genuine refutation of
the rung and must be reported as such with the family written out explicitly.
If (as expected) the oracle rejects the model, the encoding is wrong: record
that as the finding, fix the distinctness axiom, or delete the artifact.
