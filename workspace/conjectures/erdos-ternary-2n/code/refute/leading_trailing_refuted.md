# R-leading-trailing refuted at small L — counterexamples n=10 (L=1), n=18 (L=2)

Refuter arm. Attacked the **open rung `R-leading-trailing`** of the
erdos-ternary-powers ladder (difficulties off: middle-digits, density-gap,
independence):

> For a stated L, for every integer n > 8, the base-3 expansion of 2^n contains
> a digit 2 among its first L leading digits OR its last L trailing digits.

Because L is left free, I attacked the smallest instances, which the wording
leaves completely open. Both L=1 and L=2 are **FALSE**, refuted by hand-checked
direct arithmetic (the oracle is the exact base-3 expansion, computed by
repeated division below).

## L = 1, counterexample n = 10

2^10 = 1024. Base-3 (position 6 down to 0, each digit od/remainder):

| place | 3^6 | 3^5 | 3^4 | 3^3 | 3^2 | 3^1 | 3^0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| digit | 1 | 1 | 0 | 1 | 2 | 2 | 1 |

1024 = 1·729 + 1·243 + 0·81 + 1·27 + 2·9 + 2·3 + 1 = 1024 ✓, so 2^10 = **1101221_3**.

- first-1 leading digit (pos 6) = **1**  (not 2)
- last-1 trailing digit (pos 0) = **1**  (not 2)
- n = 10 > 8, and the two 2s are at positions 2,3 (strictly middle).

⟹ no digit 2 in the first-1 or last-1 ternary digit of 2^10 ⟹ **L=1 claim false.**

## L = 2, counterexample n = 18

2^18 = 262144. Base-3 positions 11..0 = **111022121001_3** (value check
1·177147+1·59049+1·19683+0·6561+2·2187+2·729+1·243+2·81+1·27+0·9+0·3+1 = 262144 ✓).

- first-2 leading digits (pos 11,10) = 1,1 = "11"  (no 2)
- last-2 trailing digits (pos 1,0) = 0,1 = "01"  (no 2)
- n = 18 > 8

⟹ no digit 2 in the first-2 or last-2 ternary digits of 2^18 ⟹ **L=2 claim false.**

## Checked against the original statement

The rung leaves L free ("for a stated L"); the natural reading is that some L
makes the claim true for all n>8. What these two witnesses establish is that
the claim is **false at L = 1 and at L = 2** — i.e. the smallest windows do not
work. This does not settle whether some larger L works (that is the real
content of the rung; the merge text already notes it needs a bounded-L
computation to push). The finding banked is the negative one: the rung's
trivial instances fail, so it is not a settled theorem at any L <= 2.

## Engine status (honest note)

`find_counterexample` was called on a ground-propositional encoding of the L=1
case (`code/refute/leading_trailing_l1.p`). It returned **undecided** — the
finite-model enumerator does not decide pure ground conjunctive axioms with a
disjunctive conjecture. The counterexample is therefore reported on the
strength of the direct arithmetic above, which is fully hand- and
value-verified, not on an engine verdict. This is rule-1 material (a one-line
counterexample beats a search).

## Witness-check discipline (falsification oracle)

These are refutations of the *weakened rung*, not of Erdős's conjecture. n=10
and n=18 both have digit-2s in 2^n (at positions 2,3 for n=10; at positions
5,6,8 for n=18), so neither contradicts the conjecture itself or the three
witnesses n=0,2,8. Good.

```claim
id: R-LT-L1-L2-refuted
statement: The weakened ladder rung "for a stated L, every n>8 has a ternary
  digit 2 of 2^n among its first L leading or last L trailing digits" is FALSE
  at L=1 and at L=2. Counterexamples: n=10 (2^10 = 1024 = 1101221_3, first-1
  and last-1 digits both 1) and n=18 (2^18 = 262144 = 111022121001_3, first-2
  digits "11", last-2 digits "01"). In each case all digit-2s of 2^n lie
  strictly in the middle.
hypotheses: n strictly greater than 8 (as the rung requires); windows of width
  L=1, L=2 at both ends of the expansion.
holds-here: yes — exact base-3 expansions computed digit-by-digit by repeated
  division; each value re-verified by evaluating the digits (1024, 262144).
status: checked (negative result; the rung at L<=2 is refuted). Engine gave
  undecided on the ground encoding; the counterexamples rest on the direct
  arithmetic.
bearing: settles that R-leading-trailing is not a theorem at L<=2; any serious
  settlement of the rung must use L >= 3 and a bounded-L computation over
  residue classes, as the rung's merge text already anticipated. Records the
  smallest windows as dead ends so the run does not pay for them twice.
anchor: code/refute/leading_trailing.py
```
