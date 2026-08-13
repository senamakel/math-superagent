# Rowland, "Binomial coefficients, valuations, and words" (2017 survey)

<!-- source: https://ericrowland.github.io/papers/Binomial_coefficients%2C_valuations%2C_and_words.pdf | converted from PDF -->

Full text at `research/sources/rowland-binomial-valuations-words.full.md`. Eric
Rowland (Hofstra), survey of the base-p/digital machinery that governs the
arithmetic of binomial coefficients. Anchors the mechanism used by the run's
adopted `binary-lucas-submask` thread.

## What it establishes / surveys

**Theme:** p-adic statistics of `C(n,m)` (which coefficients are nonzero mod p,
which have valuation α) reflect the base-p representation of `n` — via the number
of occurrences `|n|_w` of words `w` in the base-p digits of n.

- **Kummer's theorem (1852)**: `ν_p(C(n,m))` = number of carries when adding m
  and n−m in base p.
- **Lucas (1878)** (mod p): `C(n,m) ≡ ∏ C(n_i, m_i) mod p`. For p=2 this is the
  odd ⇔ `m ⊆ n` bitwise criterion the thread uses.
- **Glaisher (1899)**: number of m with `C(n,m)` odd = `2^{|n|_1}` (`|n|_1` =
  number of 1-bits of n). Count of odd entries in row n; that this is
  exponential in the popcount is what makes the odd-only triangle sparse.
- **Fine's theorem (1947)**: `θ_{p,0}(n)` = number of m with `C(n,m) ≢ 0 mod p`
  = `∏_{d=0}^{p-1} (d+1)^{|n|_d}`.
- **Carlitz recurrence**, and the central object
  `T_p(n,x) = Σ_m x^{ν_p(C(n,m))}`.

**Theorem 4 (Rowland [13], matrix generalization of Fine):**
`T_p(n,x) = [1 0] M_p(n_0) M_p(n_1) ⋯ M_p(n_ℓ) [1 0]^T`, where
`M_p(d) = [[d+1, p-d-1],[d x, (p-d)x]]` and the `n_i` are the base-p digits of
`n`. Setting x=0 recovers Fine's theorem. Extends to k-term multinomials
(Theorem 5) with k×k matrices `M_{p,k}(d)`; the polynomial sequence is p-regular
(Allouche–Shallit).

**Theorems 2–3 (Rowland; Spiegelhofer–Wallner):** `θ_{p,α}(n)/θ_{p,0}(n)` is a
polynomial of degree α in the word counts `|n|_w` for words `|w| ≤ α+1`, with
coefficients read from power series (e.g. `θ_{2,1}(n) = 2^{|n|_1}·½|n|_{10}`;
the coefficient of `|n|_{10}` in `θ_{2,α}/2^{|n|_1}` is the `x^α` coefficient of
`log(1+x/2)`).

## Bearing on Singmaster / on the adopted binary-digit thread

This is the **counting machinery for the odd-only triangle** but it **does not
address value multiplicities** — it counts how many coefficients in a row are odd
(or have valuation α), not how often one *integer value* recurs across rows. So
it grounds the thread's mechanism (Lucas for p=2 gives `k ⊆ n`; Glaisher gives
the sparsity `2^{popcount(n)}`), but it confirms the thread's stated gap: the
question "can many pairs (n,k) with the same odd value a coexist under the submask
condition" is not treated in this survey nor in the Rowland/Spiegelhofer–Wallner
literature it summarizes. That is a genuine absence worth recording as a thread
finding (the thread's premise "unchecked against the literature" survives this
search).

Also of note for the run: Fine/Glaisher give the density of the odd-only
triangle, and Rowland's matrix theorem gives an *exact polynomial* for how many
coefficients in row n are nonzero mod p^α — a precise, computable refinement of
the sparsity intuition the thread depends on.

All statements here are quoted from a survey (secondary); the underlying primary
results (Kummer, Lucas, Fine, Carlitz, Rowland, Spiegelhofer–Wallner) are
referenced in the survey but not all held in this library.
