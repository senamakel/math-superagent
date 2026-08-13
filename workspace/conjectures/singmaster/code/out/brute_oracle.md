# Naive oracle run — Singmaster's conjecture

Command: `timeout 120 python3 code/brute.py`

Convention: `N(a)` counts **both** mirrored occurrences `(n,k)` and `(n,n-k)`
and includes the trivial pair `C(a,1)=C(a,a-1)`. Matches
`code/out/witnesses.json`. A bound under this convention is twice a bound under
the "one of each mirror" convention.

## Results (all matched the statement / witness set)

| a | N(a) | nontrivial (n,k) with k<=n/2 |
|---|------|------------------------------|
| 3003 | 8 | (78,2), (15,5), (14,6) |
| 120  | 6 | (16,2), (10,3) |
| 210  | 6 | (21,2), (10,4) |
| 1540 | 6 | (56,2), (22,3) |
| 7140 | 6 | (120,2), (36,3) |
| 11628| 6 | (153,2), (19,5) |
| 24310| 6 | (221,2), (17,8) |

The record identity `3003 = C(3003,1) = C(78,2) = C(15,5) = C(14,6)` confirmed,
each with its mirror.

```claim
status: checked
The naive oracle reproduces N(3003)=8 and the six numbers of multiplicity 6,
under the both-mirrors-plus-trivial convention, matching code/out/witnesses.json.
```
