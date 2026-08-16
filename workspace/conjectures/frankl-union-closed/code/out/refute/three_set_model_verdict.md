# Verdict on code/out/refute/code_refute_uc_with_three_set.p.json — INVALID, do not cite

**Status: encoding bug, not a refutation. The `finding=refuted` verdict must not reach a claim.**

Directive: re-check the TPTP encoding `code/refute/uc_with_three_set.p` and its
produced model against the canonical oracle `code/lib/uc.py`.

## The produced model, decoded exactly

The JSON carries a complete finite model on a 4-object domain
`{fmb_1, fmb_2, fmb_3, fmb_4}` with a fully-specified `member` relation and the
slot definitions `s1..s6`. It is small enough to decode by hand, exhaustively
and without any guess:

| object | member(e1) | member(e2) | member(e3) | member(e4) | = set |
| --- | --- | --- | --- | --- | --- |
| fmb_1 | T | F | T | F | `{e1, e3}` |
| fmb_2 | F | F | F | T | `{e4}` |
| fmb_3 | F | F | F | F | `{}` |
| fmb_4 | T | T | T | F | `{e1, e2, e3}` |

Slot assignments in the model:
`e1=fmb_1, e2=fmb_2, e3=fmb_3, e4=fmb_4` (the elements are all distinct) but

```
s1 = fmb_1, s2 = fmb_1, s3 = fmb_1, s4 = fmb_1,
s5 = fmb_4, s6 = fmb_3
```

**Four of the six slots name the same object.** The distinct member sets are
`{ {e1,e3}, {e1,e2,e3}, {} }`, i.e. exactly **three** distinct members.

## Oracle check (exact, complete hand-derivation over the decoded model)

Bit encoding: e1=bit0, e2=bit1, e3=bit2, e4=bit3.

```
F = { 0, 5, 7 }        # {}, {e1,e3}, {e1,e2,e3}
|F| = 3
decide_union_closed:   {e1,e3} ∪ {e1,e2,e3} = {e1,e2,e3} ∈ F
                       ∅ ∪ X = X ∈ F (both)          -> True
abundance:  e1 ∈ {e1,e3}, {e1,e2,e3}      -> 2
            e2 ∈ {e1,e2,e3}               -> 1
            e3 ∈ {e1,e3}, {e1,e2,e3}      -> 2
            e4 ∈ nothing                   -> 0
abundant means 2·count ≥ |F| = 3, i.e. count ≥ 2.
            e1, e3 both have count 2 -> both abundant (2/3 ≥ 1/2)
```

Machine check (provided for a later agent to confirm): `code/out/refute/check_three_set_model.py`.

| Property | Value |
| --- | --- |
| distinct member count | 3 (not 6) |
| union-closed? | yes |
| abundant elements | e1, e3 (2 of 3 members each) |
| counterexample to R-uc-with-three-set? | **NO** |

The family is union-closed, contains the 3-set `{e1,e2,e3}`, and has an
abundant element. It refutes nothing.

## The bug, precisely

The encoding represents the family by **six slots** and phrases "abundant" as
"in ≥ 3 of the 6 slots", assuming the six slots are six DISTINCT member sets.
But the `slots_distinct_sets` axiom only asserts: *different objects are
different sets* (if a slot equals another object then they differ on some
element). It never asserts that the six **named slots** `s1..s6` are pairwise
distinct objects. The sat model exploit is to set four slots equal to one
object: then membership is counted with multiplicity over 6 slots, while the
genuine `|F|` is 3, and the "no element in ≥ 3 of the 6 slots" condition is
satisfied vacuously because at most two *distinct objects* contain any element.

Had `s1..s6` been forced pairwise-distinct (or had abundance been stated on a
cardinality-aware encoding of `|F|`), the model would not exist. The three
directive checks confirm it: (a) union-closure axiom is present and the model
satisfies it; (b) the abundance element does range over the full 4-element
ground set e1..e4; (c) the **counting/cardinality** semantics is where it
breaks — the multiplicity-6 count is not `|F|`.

## What this means

- The verdict `finding=refuted`, `status=CounterSatisfiable` is a
  **first-order encoding artifact**, not a mathematical refutation.
- It self-contradicts: had it been genuine (a UC counterexample on a 6-element
  ground set), it would disprove the machine-verified n ≤ 12 result
  (Bošnjak–Marković 2008 / Vučković–Živković). A model finder cannot do that.
- Rung **R-uc-with-three-set remains OPEN**, exactly as `research/WEAKENED.md`
  lists it. Nothing here changes that.

## Action

The misleading JSON is overwritten with a corrected verdict so it cannot be
read as a result. The encoding bug (missing pairwise-distinct `s_i`, so the
slot-count abets multiplicity) is recorded here for anyone who repairs the
TPTP file.

## Claim block

```claim
id: three-set-refutation-is-encoding-bug
answers: three-set-refutation-encoding-check
statement: The TPTP first-order 'refutation' of rung R-uc-with-three-set
  (code_refute_uc_with_three_set.p.json, finding=refuted) is a first-order
  encoding artifact, not a mathematical refutation. The counter-model collapses
  four of the six member slots onto one object (s1=s2=s3=s4=fmb_1), so the
  genuine |F| is 3, not 6, and the 'no element in >=3 of the 6 slots' clause is
  satisfied only by counting one set four times. The decoded family
  { {}, {e1,e3}, {e1,e2,e3} } is union-closed and its elements e1,e3 are each in
  2 of 3 members (>= 1/2), so it has an abundant element and refutes nothing.
hypotheses: TPTP encoding of a finite union-closed family containing a 3-set on
  a 4-element ground set.
holds-here: true
status: checked
bearing: closes the spurious 'refuted' verdict; R-uc-with-three-set stays open.
  Any future model-finder refutation of a UC rung must be re-checked by the
  canonical oracle code/lib/uc.py before it may be recorded (see REJECTED note).
anchor: code/out/refute/three_set_model_verdict.md and
  code/out/refute/check_three_set_model.py (exact decode of the model).
```
