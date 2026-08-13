# Odlyzko's block lemma, re-derived exactly

**Status: proved (elementary), with the constant made explicit — this run's
re-derivation, verified against the real prime rows and by exhaustive
adversarial brute force. This CORRECTS the loose `≈ n/2` figure.**

## Setup and notation

`A_k` is the k-th iterated absolute-difference row of the primes:

```
A_0(n) = p_n,        A_{k+1}(n) = | A_k(n) - A_k(n+1) | .
```

We write `A_k = (1, b_1, b_2, ...)` where `b_j = A_k(j)` for `j ≥ 1`. Every row
`k ≥ 1` has the shape `(odd, even, even, ...)`. A **leading `{0,2}` block of
length `n`** means `b_1, ..., b_n ∈ {0,2}` (the second entry through the n+1-st
entry of the row).

## The lemma, stated exactly

> **Block lemma.** If `A_k` has a leading `{0,2}` block of length `n`, then
> 1. `A_{k+d}(1) ∈ {0,2}` for every `d = 0, 1, ..., n−1`; and
> 2. `A_{k+d}(0) = 1` for every `d = 0, 1, ..., n`.
>
> So **exactly `n + 1` rows `A_k, ..., A_{k+n}` are guaranteed to begin with
> `1`**. The first row that *can* fail to begin with 1 is `A_{k+n+1}`; the
> first row whose second entry *can* leave `{0,2}` is `A_{k+n}`. Both bounds are
> sharp.

### Proof

**Structure.** Inside a block all entries are in `{0,2}`, so `|x−y| = 2` iff
`x ≠ y` and `= 0` iff `x = y`. Hence a difference applied to a `{0,2}` block
produces 0 at runs of equal entries and 2 at boundaries between unequal runs — 
still a `{0,2}` string. Applying the operator repeatedly, the whole **subtriangle**
built from the block's entries stays in `{0,2}`.

**Diagonal bound (A).** `A_{k+d}(1)` is a function only of
`A_k(1), A_k(2), ..., A_k(1+d)` — the length-`(1+d)` diagonal descending from
position 1. (This is immediate: the operator's value at a position depends only
on the same diagonal of the row above, inductively one row at a time.) For
`d ≤ n−1` that diagonal has `1+d ≤ n` entries, all inside the `{0,2}` block, so
each is in `{0,2}`; the whole diagonal-subtriangle is in `{0,2}`, hence
`A_{k+d}(1) ∈ {0,2}`. For `d = n` the diagonal uses `n+1` entries, including
`A_k(n+1)`, which is *outside* the block — so `d = n` is the first offset where
position 1 is no longer forced.

**Leading-entry bound (B).** Since `A_{k+d}(0) = |A_{k+d-1}(0) − A_{k+d-1}(1)|`
and `A_{k+d-1}(0) = 1` for `d−1 ≤ n` (induction), we have
`A_{k+d}(0) = |1 − A_{k+d-1}(1)|`, which equals `1` iff `A_{k+d-1}(1) ∈ {0,2}`.
By (A) that holds for `(d−1) ≤ n−1`, i.e. `d ≤ n`. So rows `k..k+n` begin
with 1. Row `k+n+1`'s leading entry depends on `A_{k+n}(1) ∈ {0,2}`, which by
(A) with `d = n` is **not** forced — the first row that can fail. ∎

> The constant is **`1`**, not `n/2`. A block of length `n` protects `n+1`
> rows. This agrees with Odlyzko's own statement in *Iterated absolute values
> of differences of consecutive primes* (Math. Comp. 61 (1993), §2, p. 374):
> *"if d_K(1) = 1 while d_K(n) ∈ {0,2} for all 1 ≤ n ≤ N, then we can conclude
> that d_k(1) = 1 for K ≤ k ≤ N+K−1"* — i.e. `N = n+1` rows of protection, a
> **linear** guarantee. The `≈ n/2` figure that has been passing around this
> run's notes is a misremembering; the primary source gives the factor `1`.

## Interpretation and the regeneration gap

The block of length `n` protects `n+1` rows — **geometric consumption is only
in the wrongful `n/2` reading**. Protection is actually consumed *one row per
row* (each descending row uses one more block entry to supply its position 1).
But the entry `A_k(n+1)` just past the block is a boundary value that the
operator immediately starts reducing toward `{0,2}` from below, which is the
only engine that can keep the regime alive past row `k+n`. Nothing in the
block lemma forces that reduction; it is exactly the regeneration-rate question
the conjecture turns on, and it remains open.

## The stronger structural question

After one difference the `{0,2}` block's interior becomes 0 exactly on runs of
equal entries and 2 at the boundaries between unequal runs. The whole
subtriangle built from the block is in `{0,2}`, and its **apex** (the value
`A_{k+n-1}(1)`) is determined *exactly* by the block's bit pattern:

$$A_{k+n-1}(1) = 2 \cdot \bigoplus_{j=0}^{n-1} \binom{n-1}{j}_{\!2} \cdot (b_{j+1}/2)$$

where the sum is a binary XOR over the binomial coefficients reduced mod 2
(the Sierpinski / Pascal-modulo-2 structure), verified by exhaustive brute
force over all `2^n` patterns for `n = 1..13`.

**But** this internal structure cannot *strengthen* the worst-case rank: the
largest forced position-1 value is `A_{k+n-1}(1)`, at the apex of a triangle of
side `n`; reaching position 1 of *row `k+n`* still requires the entry
`A_k(n+1)` that sits outside the block, so no reading of the `{0,2}` pattern
extends the guarantee by even one row. Read-of-the-block gives **exact apex
control** but not a *larger safe region*.

What the pattern does delimit is the worst case. Of the `2^n` block patterns,
exactly one is genuinely worst-case at the very first step: the constant block
`(0,0,...,0)` (equivalently `(2,2,...,2)`) collapses to `0` under the first
diff, so its subtriangle carries no structure to propagate the leading `1`
beyond row `k+n`. Every *other* pattern has an internal `0↔2` transition, and
the `{0,2}` self-propagation keeps the leading entry `1` for at least as long;
how much *longer* depends on the boundary value `A_k(n+1)` and on the operator
below, which the lemma does not control. That boundary dependence is precisely
the regeneration gap: the block governs its own consumption exactly (one row
per entry), and the whole open content of the conjecture is whether the
boundary keeps re-entering the `{0,2}` regime fast enough to outpace it.

## Numerical check

- **Generator oracle.** `code/lib/gilbreath.py` reproduces all five worked rows
  of `problem.md` exactly (`A_1 = 1,2,2,4,...` etc.), `match = True` for each.
- **Exhaustive guarantee, adversarial tails.** `code/block_lemma/verify_constant.py`
  and `code/block_lemma/verify_diagonal.py` run over **all** `2^n` block bit
  patterns with adversarial even completions after the block, `n = 1..11`
  (122,820 block×tail pairs), and confirm: minimum guaranteed leading-1 run
  = `n+1` exactly; the full active subtriangle of positions `1..(n−d)` in row
  `k+d` stays in `{0,2}`; and sharpness — for every `n = 1..8` there exists a
  completion where position 1 leaves `{0,2}` at offset `n`.
- **Real rows.** Rebuilding the witness rows (sieve to 400000, 33,860 primes,
  depth 600): the lemma's guarantee `rows k..k+n_k start with 1` holds with
  **zero violations**. The real rows regenerate far past the guarantee (median
  margin 492 rows past `k + n_k` with second entry still in `{0,2}`; 0 rows
  fully exhausted), confirming that in practice regeneration dominates
  consumption — but this is numerical evidence about depth 600, not a proof.

## What is proved vs. what is not

- **Proved (this note):** the exact block lemma with constant `1`, the
  `n+1`-row guarantee, its sharpness, and the exact apex (Sierpinski-XOR) value
  of the sub-triangle. These are elementary diagonal-subtriangle facts,
  verified exhaustively on small `n` and consistent with Odlyzko's sourced
  statement.
- **Not proved:** that regeneration always keeps up, i.e. Gilbreath's
  conjecture. The block lemma is precisely the *consumption* half; the
  conjecture requires the *regeneration* half (rows keep re-entering the
  `{0,2}` regime), which is untouched here.

## Files

- `code/lib/gilbreath.py` — exact row generator, reproduces the worked rows.
- `code/block_lemma/verify_constant.py` — exhaustive/adversarial constant check.
- `code/block_lemma/verify_diagonal.py` — independent subtriangle + sharpness check.
- `code/block_lemma/explore_shape.py` — apex (Sierpinski-XOR) and
  self-preservation distribution.
- `code/block_lemma/check_real.py` — real-row guarantee + regeneration margin.
- `research/sources/odlyzko-1993-iterated-absolute-differences.full.md` — the
  primary source confirming the linear constant.

## Fenced claim

```claim
id: odlyzko-block-lemma-exact
statement: If row A_k has a leading {0,2} block of length n (positions 1..n), then exactly n+1 rows A_k..A_{k+n} are guaranteed to begin with 1; the leading-entry protection constant is 1 (not n/2). Equivalently A_{k+d}(1) in {0,2} is forced exactly for d = 0..n-1, and A_{k+d}(0) = 1 exactly for d = 0..n. Row k+n+1 is the first that can fail. The d-th descendant of position 1 is a diagonal-subtriangle of the block, all in {0,2}, sharp because offset n uses index n+1 outside the block.
hypotheses: A_{k+1}(h) = |A_k(h) - A_k(h+1)|; A_k(0)=1 and A_k(1..n) in {0,2}; no assumption on entries past the block.
holds-here: yes
status: proved (elementary diagonal-subtriangle argument); verified exhaustively over all 2^n block patterns with adversarial even completions for n=1..11 (122820 pairs, zero violations); sharpness confirmed for n=1..8; real prime rows to depth 600 show zero violations and regenerate far past the guarantee. Consistent with Odlyzko 1993 §2 p.374 (linear N=n+1 constant).
bearing: fixes the exact consumption rate (1 row per row, not n/2); the open content of Gilbreath's conjecture is entirely the regeneration half, now precisely delimited: position 1 of row k+n needs A_k(n+1), outside the block, whose reduction toward {0,2} is not forced by the lemma.
anchor: research/notes/block_lemma.md
contradicts: the run's earlier loose '≈ n/2 rows' ledger (reduction.md repeats it) — the primary source and this re-derivation give n+1.
answers: exact-block-lemma-constant
```
