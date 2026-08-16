# On Stephan's conjectures concerning the Pascal triangle modulo 2 — Shevelev (v4 full text)

Source: https://arxiv.org/pdf/1011.6083v4; full text at
`research/sources/stephan-conjectures-pascal-mod2-shevelev-fulltext.full.md` →
[[stephan-conjectures-pascal-mod2-shevelev-fulltext.full]]

## What it establishes

Same paper as `stephan-conjectures-pascal-mod2-shevelev.md` (which see for the full
note and bearing), in its v4 full-text form. Confirms the Fermat factorization: the
binary integer for row `n` of Pascal's triangle mod 2 is `d(n) = ∏_i F(k_i)` over the
1-bit positions `k_i` of `n`, `F(k) = 2^{2^k}+1`; `∏_k (1 + F(k) x^{2^k}) = Σ d(n) x^n`;
the number of factors is the digit sum. Proves Stephan's conjectures 1–4 and gives an
"orthogonality of nonnegative integers" proof route plus direct mod-2 row
manipulation.

## Bearing and caution

Used only for the algebraic/factorization structure of the down-sets (matches item 5's
run structure). **Suppress the Fermat-prime / divisor interpretation** — no primes in
this problem. It does not describe `{M_d △ M_{d'}}` with multiplicities (the crux gap).

## Claim blocks

```claim
id: shevelev-fermat-factor-v4
statement: The row-n binary value d(n) of Pascal's triangle mod 2 equals the product
  over the 1-bit positions k_i of n of F(k_i), F(k)=2^{2^k}+1, with generating function
  prod_k (1 + F(k) x^{2^k}) = sum_n d(n) x^n; the Fermat-factor count is the digit sum.
hypotheses: n >= 0 binary; used as an algebraic factorization identity only
holds-here: yes (as factorization identity; the prime/divisor reading is out of scope)
status: proved
bearing: closed-form digital structure of the down-set rows; supports item 5's runs.
anchor: research/sources/stephan-conjectures-pascal-mod2-shevelev-fulltext.full.md
```

## Not settled

No statement on the symmetric-difference multiset or the collapse.
