# Summary — The number of nonzero binomial coefficients modulo p^alpha

Source: Eric Rowland, "The number of nonzero binomial coefficients modulo
`p^alpha`", arXiv:1001.1783 (2011), *J. Combin. Number Theory* 3 (2011) 15–25.
Full text at `[[rowland_nonzero_binomial_modp.full]]`.

## What it establishes

Fine (1947) gave the count of nonzero binomial coefficients on row `n` of
Pascal's triangle modulo a prime `p`. Rowland generalises Fine's theorem to
prime powers, by Kummer's theorem, expressing

    #{ 0 ≤ k ≤ n : C(n,k) ≢ 0 (mod p^α) }

as a sum over integer partitions; for fixed `α` the expression shows explicit
dependence on the number of occurrences of each subword in the base-`p`
expansion of `n`.

**The α = 1, p = 2 case is the one this run's fold is built on.** By Lucas,
`C(n,k) ≡ 1 (mod 2)` iff `k` is a binary submask of `n`, so the count of odd
binomial coefficients on row `n` is exactly `2^{s₂(n)}` (Fine's theorem, `s₂`
= binary digit sum). This is the submask cardinality: the depth-`d` fold cell
of SUPPLY XORs over exactly the `2^{s₂(d)}` submasks of `d`
(`lucas-submask-odd`, `szechtman-lucas-submask-corollary`).

## What it implies here

- Confirms the submask count `2^{s₂(d)}` that underlies the fold's Lucas reading
  is the α=1, p=2 member of a general family (counts mod `p^α` of nonzero
  binomials, expressed in base-p subword combinatorics).
- Does **not** touch SUPPLY's actual object: taking `h` arbitrary, the fold
  weight `wt(Φ_n h)` is not a count of nonzero binomials on one row — it is an
  XOR over submask sets of `h` values. Rowland's theorem is background on the
  binomial-mod-p structure that the fold is built from, not a bound on its
  image weight.
- No further bearing on the five closed doors or the weakest-input question;
  nothing here contradicts recalled memory.

```claim
id: rowland-nonzero-binomial-prime-power
statement: Fine's theorem counts #{k ≤ n : C(n,k) ≢ 0 (mod p)} and Rowland generalises it to prime powers p^α, expressing #{k ≤ n : C(n,k) ≢ 0 (mod p^α)} as a sum over integer partitions, with fixed-α dependence on base-p subword counts of n. For α=1, p=2 the count is 2^{s₂(n)} — the number of binary submasks of n.
hypotheses: p prime, α ≥ 1, n ≥ 0; Kummer's theorem (p-adic valuation = number of carries) is the engine.
holds-here: α=1, p=2 reproduces the submask count 2^{s₂(d)} behind the fold's Lucas reading; the general p^α statement is background only and does not bound wt(Φ_n h).
status: sourced (Rowland 2011; α=1,p=2 case is classical, follows from Lucas)
bearing: Places the fold's submask cardinality in the known binomial-mod-p^α family; no weight bound on the fold follows.
anchor: research/sources/rowland_nonzero_binomial_modp.full.md
```

## Not settled / no help

This source does not advance SUPPLY: it counts nonzero binomials on a row, not
XOR weights of a folded image. Read once; nothing to reuse.
