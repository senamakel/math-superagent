# Ford–Konyagin–Luca (2010), *On prime chains* (arXiv:0904.0473)

Full text: [[ford-konyagin-luca-prime-chains-2010.full]] (readable OCR).

**Setup.** For positive integers `a, b` write `a ≺ b` if `b ≡ 1 (mod a)`. A *prime chain* is `p_1 ≺ p_2 ≺ ⋯ ≺ p_k` (each `p_{j+1} ≡ 1 mod p_j`), e.g. `3 ≺ 7 ≺ 29 ≺ 59`. `N(x; p)` counts chains starting at `p` with `p_k ≤ x`; `H(p)` is the length of the longest prime chain ending at `p`.

**Results.**
- **Theorem 1:** `N(x; p) = O_ε(x^{1+ε})` effective for `p ≥ 2, x ≥ 20`.
- **Theorem 2:** `f(p) ≥ 0.378 log p` for almost all primes; hence `N(x) ≫ x`.
- **Theorem 4:** `H(p) ≤ (log p)^{0.9503}` for almost all `p` (first nontrivial upper bound on chain length).
- Conjectures: `H(p)` has normal order `e log_2 p` (Conj. 2); explicit `e log_2 p − (3/2) log_3 p + E(p)` (Conj. 3).
- The paper settles an Erdős–Granville–Pomerance–Spiro 1990 conjecture via the branching-random-walk model.

**Why clustered near this run but peripheral.** The 3-Higgs / Pratt structure (each factor of `p−1` is itself 3-Higgs) is a prime-chain condition, and Ford-Konyagin-Luca give tools for *counting chains by length* and *placing shifts in residue classes*. Maciejewski's branch uses the *semigroup* `𝒮₃^{(≤3)}` (Higgs-cubefree shifts `(r−1)/(4p)`) and Ford's *thinness* (the 2014 paper, `heven-thinness`), not directly the chain-length results here. So this source is context: it bounds how long a Pratt-type chain can be, but does not by itself close the divisor-level `Φ_{4p}(2)` gap. It does not appear in `claim` form in the ledger because none of its theorems is currently load-bearing for a specific branch step.

```claim
id: fkl-prime-chain-length
statement: For almost all primes p, the length H(p) of the longest prime chain
  ending at p satisfies H(p) <= (log p)^0.9503, and most chains starting at a
  fixed prime are O(x^(1+epsilon)) in count.
hypotheses: p prime; chain is p_{j+1} ≡ 1 (mod p_j); "almost all" quantifier
holds-here: partially - the 3-Higgs primes form a downward-closed set of
  Pratt-type chains, so these apply to the counting/length of P_3, but H_even
  needs the semigroup shift (r-1)/(4p) which this source does not control
status: asserted
bearing: context only; bounds chain length of the 3-Higgs lattice but does not
  contribute a new step to the divisor-level Phi_{4p}(2) branch
contradicts: (none)
```
