# PE1006 — formal statement verdict

File: `code/lean/Lib/Statement.lean`
Checked with `lean_check` on this run. Verdict:

```
file: code/lean/Lib/Statement.lean
compiled: true        <- the statement ELABORATES
outcome: failed       <- only because 5 `sorry` remain (the deliverable)
sorry warnings: 5
target theorem: pe1006 : ∃ A : ℕ, A < M ∧ PsiResidue 1000000000000000000 = A
```

All five declarations resolved with the right types; the only remaining axioms
are `propext`, `Classical.choice`, `Quot.sound` plus `sorryAx` (the 5 sorries).
No cited axioms.

## What the file defines

- `fibWord : ℕ → List Char` — the S_n recurrence (S_0=0, S_1=01, S_n=S_{n-1}S_{n-2}).
- `digitVal : Char → ℕ` — '0'→0, else 1.
- `valueOf : List Char → ℕ` — foldl `acc*10 + digit`, so *leading zeros are
  ignored automatically* (10·acc+0 = 10·acc), matching int('001')==1 in the oracle.
- `slidingFactors w k` — all length-k contiguous substrings of w (a Finset).
- `Psi k` — sum of squares of the *distinct* length-k factor values, sampled from
  `fibWord (k+2)` (length F_{k+2} > k, so it contains every factor of the limit).
- `PsiResidue k` — `Psi k % 101001001`.
- `M = 101001001`.

## Theorem statements (all `:= by sorry`)

- `modulus_prime : Nat.Prime M`
- `ten_invertible : Nat.Coprime 10 M`
- `oracle_examples : Psi 3 = 20302 ∧ Psi 10 % M = 10699667`
- `fib_word_factor_count (k) : (slidingFactors (fibWord (k+2)) k).card = k + 1`
- `pe1006 : ∃ A : ℕ, A < M ∧ PsiResidue 1000000000000000000 = A`

## Where the statement could differ from the problem as written

1. **"Ignore leading zeros"** is realised by defining `valueOf` as the *integer
   the word denotes* (left fold), so `"001"`, `"01"`, `"1"` are the *same* value
   1, and the Finset over factor-*words* then a second `image valueOf` collapses
   words that are equal-as-words *or* merely equal-as-values. Because the
   Fibonacci words contain no two distinct factors that differ only in leading
   zeros (a factor's value determines it), this coincides with the statement,
   but the collapse is implicit in `valueOf`, not an explicit "interpret as
   decimal". A stricter reading could keep the factors distinct and sum
   `(valueOf w)^2` over the word-set; the two agree here.
2. **Sampling index.** `Psi k` uses `fibWord (k+2)`, whose length F_{k+2} > k;
   the statement says "some S_n", and any S_n of length > k gives the same
   length-k factor set on the infinite word. `k+2` is a sufficient bound, so
   `Psi` is well-defined, but this reliance on length > k (that the whole
   factor set is already present) is exactly what `fib_word_factor_count` and
   an implicit "factors of the limit = factors of each long S_n" would need to
   state. That identification is a lemma the run has *not* formalised yet.
3. **10^18 is hard-coded as a ℕ literal** `1000000000000000000`; a reader
   expecting `10^18 = 10 ^ 18` is fine, but should know `PsiResidue` takes a ℕ
   argument, so the literal is the value, not the expression.
4. The answer is stated *existentially* (`∃ A < M, PsiResidue (10^18) = A`),
   not as the concrete residue — the run does not yet know the numeric value to
   put in a closed form. This is a finding, not a defect of the formalisation.
5. `modulus_prime` and `ten_invertible` are hypotheses of the *method* (the
   floor-sum route uses x = 10⁻¹ mod M), not of the problem. `ten_invertible`
   follows from gcd(10, M) = 1; primeness is asserted-only and not needed for
   the reduction.

## Why it compiles clean

`slidingFactors` as a Finset needs `DecidableEq`, which has a global instance
for `List Char`. The big-operator `.sum` resolves via
`Mathlib.Algebra.BigOperators.Intervals` and `Mathlib.Data.Finset.Basic`.

## Oracle (independently reproduced in-container, code/brute.py)

- Psi(3) = 20302 with length-3 factors 001,010,100,101.
- Psi(10) % 101001001 = 10699667.
- distinct length-k factor count = k+1 for all k in 1..30.
