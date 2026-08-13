```thread
question: Can the lifting theorem (|A_k| = 2^(k-1) for all k) be formalised in Lean 4 with Mathlib?
status: live
rests-on: ternary-lifting-theorem
blocked-by: none
next: write the three lemmas in Lean 4; report #print axioms and every sorry
```

# Lean 4 formalisation of the lifting theorem

## The target

The theorem in `code/out/lifting_theorem.md` (claim `ternary-lifting-theorem`):
the three-lemma proof that `|A_k| = 2^(k-1)` for all k. The three lemmas are:

1. **Lemma 1**: `2^(2*3^(k-2))` has order 3 mod `3^k`, hence equals `1 + c*3^(k-1)` with `3 ∤ c`.
2. **Lemma 2**: the three lifts `r + j*2*3^(k-2)` agree mod `3^(k-1)`, so they share their low `k-1` ternary digits.
3. **Lemma 3**: the `k`-th digit of the `j`-th lift is `d + v*j*c mod 3`, an affine bijection of `Z/3`, so the three top digits are `0,1,2` in some order.

Then induction: exactly one lift has top digit 2 and dies, exactly two survive → `|A_k| = 2|A_{k-1}|`, with `|A_1| = 1` → `|A_k| = 2^(k-1)`.

## What Mathlib already has

- `ZMod (3^k)` and its units group
- `orderOf` for group elements
- `pow_eq_one_iff_dvd` / order facts
- `Nat` exponent arithmetic
- Possibly `padicVal` for LTE facts (though the bijection proof doesn't need LTE)

## What needs writing

- The setup: define `A_k` as a `Finset` of residues modulo `2*3^(k-1)`
- The ternary digit extraction function (mod 3 on the appropriate digit)
- Lemma 1: `orderOf (2^(2*3^(k-2))) = 3` in `(ZMod (3^k))ˣ`
- Lemma 2: the three lifts are congruent mod `3^(k-1)`
- Lemma 3: the affine bijection on `Z/3`
- The count: `card (A_k) = 2^(k-1)` by induction

## Status

- Not yet started.
- The theorem is proved on paper; this is a machine-checked replication.
- Report `#print axioms` output and every remaining `sorry`.