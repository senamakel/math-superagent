# The number of nonzero binomial coefficients mod p — Eric Rowland (2011)

Source: https://arxiv.org/pdf/1001.1783 (arXiv:1001.1783)
Full text: [[rowland-number-nonzero-binomial-modp.full]]

## What it establishes

- **Kummer's theorem.** The p-adic valuation of `C(n,m)` is the number of borrows in
  subtracting `m` from `n` in base `p`.
- **Lucas' theorem.** `C(n,m) ≡ ∏ C(n_i, m_i) (mod p)` — restated.
- **Fine/Glaisher.** The number `a_p(n)` of nonzero entries on row `n` of Pascal mod p
  is `a_p(n) = ∏_i (n_i + 1)`; for p=2, `a₂(n) = 2^{pc(n)}` where `pc` is popcount.
- **Theorem 1 (prime powers).** Generalizes Fine to `mod p^α` via a sum over integer
  partitions; `a_{p^α}(n)/a_p(n)` is a polynomial of degree `α−1` in subword counts
  `|n|_w`.

```claim
id: fine-glaisher-2pc
statement: The number a_2(n) of odd entries on row n of Pascal's triangle mod 2 is
  2^{pc(n)}; equivalently the down-set {o : o submask of n} has size 2^{pc(n)}.
hypotheses: n nonnegative integer; p=2
holds-here: yes
status: proved (Fine 1947 / Glaisher)
bearing: fixes the size of the fold rows: |M_d| = 2^{pc(d)}; enters the closed-form
  size of the symmetric differences (imported result 3) via M_d∩M_d' = M_{d∧d'}
anchor: research/sources/rowland-number-nonzero-binomial-modp.full.md
```

## Bearing / what it does NOT settle

Supplies the `2^{pc(d)}` sizes that populate the closed form for `|M_d △ M_{d'}|`
(item 3). Does not describe *which* sets occur, and the prime-power p>2 machinery is
out of scope here (no primes needed; p=2 only).
