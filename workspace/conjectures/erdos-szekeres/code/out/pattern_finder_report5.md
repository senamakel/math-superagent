# Pattern-finder round 5: explicit bijection for the triangular realized-pattern-class count

## Deliverable

Upgraded the report4 *count* conjecture (`#realized (n-1)-convex block patterns =
C(n-1,2)`) to an **explicit, verified bijection with unordered block pairs** and a
closed-form profile, by attacking the exact lists rather than hand-waving the bijection.

## The formula

For es_construct(n), B = n-1 blocks. A realized pattern is exactly one of the C(B,2)
profiles indexed by unordered {L,R}, 0 ≤ L < R ≤ B-1:

```
c_L = L+1 ; c_R = B-R ; c_i = 1 for L<i<R ; c_i = 0 otherwise ;  sum = B = n-1
```

## Verification

`code/out/pattern_bijection_check.py` (EXIT 0), exact oracle, exhaustive n=4..7:

- n=4..7: realized set == formula set, **zero missing, zero spurious** (n=7 = all 906,192
  subsets). n=8: all 21 formula patterns realized by sampling (supportive only).

## Sequence tools

- `analyze_sequence([3,6,10,15,21])`: degree-2 polynomial, constant 2nd diffs = 1 — C(B,2).
- `oeis_lookup([3,6,10,15,21])`: A000217 triangular numbers (also A161680 = C(n,2) with a
  different shift). Exact catalogued match.

## Status

**Conjecture, exact n=4..7 (=C(n-1,2)), sampled n=8.** It is a genuine upgrade: the count
conjecture's "likely bijection" is now stated exactly and checked. First falsifier: a realized
pattern outside the formula set at any n (none through n=7 exhaustive).
