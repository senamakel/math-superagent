# Superseded pointer — see threshold_weight_exponent.md

This note was drafted as a re-statement of the linear-supply threshold result.
**It is superseded by `research/notes/threshold_weight_exponent.md`**, which is
the authoritative record: it carries the full exact-mean table to n=32768, the
OLS exponent fits with error bars (0.545–0.557 over the large-n tail), the
model comparison to `n^{1/2}(log n)^{0.4}`, the honest "fitted, not a closed
form" framing, and both of the operator directive's corrections verbatim.

The canonical note now carries the claim block `threshold-weight-sublinear-exponent`
(status measured-not-proved) and pairs with the scoping claim
`threshold-typical-is-not-this-string` below (the genericity gap that keeps the
result type-4, never SUPPLY-solved).

Kept here only the distinct scoping claim that lives in this file:

```claim
id: threshold-typical-is-not-this-string
statement: Being above the linear-supply threshold (mean-typical at weight ~n^0.55) does not prove that the primes' own gap-parity string h has linear supply: the threshold is a property of the weight layer, and the primes are a single string inside it. The genericity gap — 'typical is not this string' — is unchanged from the first pass; what changed is the SIZE of the arithmetic input demanded (sublinear ~n^0.55 switch count instead of a positive fraction).
hypotheses: threshold-mean-exact-parity-formula, threshold-weight-sublinear-exponent.
holds-here: yes
status: asserted (a scoping statement, not a computed quantity)
bearing: Prevents writing the sublinear-threshold result as SUPPLY-solved or prime-specific. It files against problem.md result type 4 (arithmetic input strictly weaker than switch density), never type 1.
anchor: research/notes/threshold_weight_exponent.md
```
