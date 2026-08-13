# The modular sieve grows exactly like `2^(k-1)`, so it can never close

Extended by the operator from the run's own `sieve_Ak.py`, which had reached
`k = 12`. Computed by **lifting** rather than by re-scanning each level: a
surviving class `r mod 2·3^(k-2)` has exactly three preimages
`r + j·2·3^(k-2)` (`j = 0,1,2`) modulo `2·3^(k-1)`, and only those are tested.

## The count

```
k    |A_k|        2^(k-1)
 1          1           1
 2          2           2
 ...
12       2048        2048
16      32768       32768
20     524288      524288
22    2097152     2097152
```

Exact agreement at every `k = 1..22`. The three witnesses `n = 0, 2, 8` remain
in `A_k` at every level, so nothing here forbids them.

## What it means

`A_k` is indexed by residues mod `2·3^(k-1)`, so the **density** is

```
|A_k| / (2·3^(k-1)) = 2^(k-1) / (2·3^(k-1)) = (1/2)·(2/3)^(k-1)  ->  0
```

The density tends to zero and **the count doubles**. Those are not in tension;
they are the whole point, and confusing them is the trap `GOAL.md` names.
Closing a sieve requires `|A_k| = 0` at some finite `k`, and `|A_k|` is
growing without bound.

**Therefore no purely modular obstruction modulo any power of 3 can prove this
conjecture.** Whatever kills the `n > 8` cases is not visible at any finite
3-adic precision. That is a genuine negative result about the method, of the
same kind as the p-adic dead end recorded in the magic-square workspace, and
it is the honest answer to "show that `2^n mod 3^k` forces a digit 2": it does
not, at any `k`.

## The structure to prove

The data says the lifting is **exactly 2-to-1**: each class surviving at level
`k` has three candidate lifts and exactly two of them survive at level `k+1`.
Proving that is the theorem, and it would give `|A_k| = 2^(k-1)`
unconditionally rather than for `k <= 22`.

The likely mechanism, which needs checking rather than assuming: adding
`j·2·3^(k-2)` to the exponent multiplies `2^r` by `(2^{2·3^(k-2)})^j`, and
`2^{2·3^(k-2)} ≡ 1 + c·3^(k-1) (mod 3^k)` for some `c` not divisible by 3 —
lifting the exponent. So the three lifts differ by `c·3^(k-1)` steps in the
top ternary digit, which takes the values `{d, d+c, d+2c}` mod 3. Exactly one
of those three is `2`, so exactly two survive. If that argument holds, it is a
complete proof of `|A_k| = 2^(k-1)`, and with it a proof that the sieve can
never close.

Check `c` and the exact congruence before recording this as proved — the
argument above is a sketch, not a verification.

```claim
id: ternary-sieve-count-doubles
statement: Let A_k be the set of residues r mod 2*3^(k-1) for which the low k
  ternary digits of 2^r mod 3^k all lie in {0,1}. Then |A_k| = 2^(k-1) for
  every k = 1..22, verified exactly by lifting. The density
  |A_k|/(2*3^(k-1)) = (1/2)(2/3)^(k-1) tends to 0 while the count doubles at
  each level. Consequently the modular sieve never empties, and no obstruction
  modulo a power of 3 can prove the Erdos ternary conjecture at any finite
  3-adic precision. The witnesses n = 0, 2, 8 survive in A_k at every level
  tested.
hypotheses: k = 1..22 only; exact integer arithmetic; A_k defined by the low k
  ternary digits of 2^r mod 3^k
holds-here: yes, computed in this workspace
status: checked
bearing: closes the purely modular route as a proof strategy and redirects the
  run to what the sieve cannot see. The 2-to-1 lifting is the statement worth
  proving unconditionally; a proof of it turns this from a bound at k <= 22
  into a theorem. Not an impossibility lemma about n, so the witness set does
  not falsify it, but the witnesses were checked to survive at every level
anchor: code/out/sieve_cannot_close.md; code/out/sieve_Ak.captured.txt
source: operator-computation
```
