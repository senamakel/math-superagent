# Summary — Lucas' Theorem: Generalizations, Extensions, Applications (1878–2014)

Source: R. Meštrović, arXiv:1409.3820 (survey). Source URL:
https://arxiv.org/pdf/1409.3820. **Full text now available:** the earlier landing-page-only file has been superseded by the actual paper, downloaded from the HTML mirror at `[[mestrovic_lucas_theorem_survey_html.full]]` (https://arxiv.org/html/1409.3820v1). Summary of the real paper: see `[[mestrovic_lucas_theorem_survey_html]]`.


## What this establishes

The canonical statement of **Lucas' theorem** (§1): for p prime, with base-p
expansions `n = Σ n_i p^i`, `m = Σ m_i p^i`,
```
C(n,m) ≡ ∏_i C(n_i, m_i)  (mod p).
```
For p = 2, `C(n_i,m_i) mod 2 = 1` iff `m_i ≤ n_i` for each digit position, i.e. iff
`m` is a **binary submask** of `n`. Equivalent: `C(d,i)` is odd iff `i & ~d = 0`.

The survey collects: generalizations of Lucas' theorem modulo prime powers
(Granville, Anton–Stickelberger, Davis–Webb, Davis–Webb), the Lucas *property*
and *double-Lucas property* for integer sequences, and Lucas-type congruences for
Fibonomial, Lu-cnomial, Gaussian q-nomial, and generalized binomial coefficients.
Applications in number theory and combinatorics.

## What it implies here

This is the bedrock of `problem.md` fact (2): the submask characterization
`C(d,i) mod 2 = 1 ⟺ i ⊆ d (binary)`. That is what makes `Φ_n` "read" `h` only
along binary-submask XORs (`h` appears at indices `j = i + (n−k)` for `i ⊆ d =
k−1`), which is the `submask-read` difficulty: any usable arithmetic input about
the primes must be a statement about those specific submask-XOR linear forms, not
global complexity of `h`. It is also what makes the kernel rank computation
exact (the operative Φ_n has rank n−2, nullity 2 — corrected from the inherited
n−3 claim; see fold-rank-is-n-2-nullity-2-alternating).

The Lucas property for sequences (a sequence `a_n` is Lucas when
`C(n,k)`-type congruences hold) is the abstraction behind the run's own interest in
whether the fold preserves or destroys density on inputs like `h`.

## What it does not settle

The survey states Lucas' theorem and its generalizations; it says nothing about
the weight of a folded prime string. It is not a route to SUPPLY by itself, only
the machinery identifying which coordinates `Φ` reads.

```claim
id: lucas-submask-odd
statement: For nonnegative integers n,m, C(n,m) is odd iff m is a binary submask of n
  (every 1-bit of m is a 1-bit of n); equivalently m & ~n = 0. This is Lucas' theorem
  with p = 2.
hypotheses: p=2 (the run's F₂ setting).
holds-here: yes — this is problem.md fact (2), the submask characterization of Φ's cells.
status: proved (Lucas 1878; standard). Re-derivable by elementary means.
bearing: Φ_n reads h only along binary-submask XORs; this confines the admissible
  arithmetic input (submask-read difficulty).
anchor: mestrovic_lucas_theorem_survey.full, §1
```

```claim
id: lucas-generalisations-context
statement: Lucas' theorem extends to prime powers and to families of generalised binomial
  coefficients (Fibonomial, q-nomial, etc.), and underlies the (double) Lucas property of
  integer sequences.
hypotheses: none beyond the relevant coefficient families.
holds-here: unchecked (not the p=2 prime case used here; relevant only if the fold is
  generalised).
status: proved (survey of Lucas-type congruences)
bearing: context only — the run needs only the p=2 submask case.
anchor: mestrovic_lucas_theorem_survey.full, §§3–5
```
