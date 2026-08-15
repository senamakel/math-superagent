# Lewis–Tefft 2024 — "The Period of Ducci Cycles on Z_{2^l} for Tuples of Length 2^k" (arXiv:2401.17502)

**Full text:** `research/sources/lewis-tefft-2024-period-ducci-cycles-z2l-html.full.md`
**Source:** Mark L. Lewis, Shannon M. Tefft, arXiv:2401.17502v2 [math.NT], Aug 2024.

## The operator it studies (— not the absolute-difference map)

This paper studies the **summing** Ducci function
`D(x_1,...,x_n) = (x_1+x_2 mod m, x_2+x_3 mod m, ..., x_n+x_1 mod m)` over
`Z_m^n`. This is *linear* (`D = I + H`, `H` the cyclic shift), which is why a
mod-2^l analysis works cleanly for it. It is **not** the integer
absolute-difference operator `|a−b|` of Gilbreath's conjecture. So it does not
directly transfer.

## What it proves

For `n = 2^k`, `m = 2^l` (both powers of 2), every Ducci sequence over
`Z_{2^l}^{2^k}` **vanishes** to `(0,...,0)`, and the maximum number of
iterations (the length) is exactly

> **`L_m(n) = (l+1)·2^{k−1}`, with period `P_m(n) = 1`.**

The engine is the coefficient recursion `a_{r,s} = a_{r−1,s} + a_{r−1,s−1}`
(= Pascal/binomial structure; for `r < n`, `a_{r,s} = binom(r, s−1)`), plus
the mod-4 and mod-8 facts about `binom(2^j, 2^{j−1})` (≡ 2 mod 4, ≡ 6 mod 8)
and Lucas's theorem. It gives a fully explicit 2-adic valuation bound on the
vanishing time of the *linear* sum-Ducci operator.

## Why it matters to this run — and why it does NOT close the run's questions

**What it corroborates / connects:** this is the concrete `Z_{2^l}` / binomial-coefficient
machine for a Ducci-type operator that is linear over the 2-adics. It is the
natural reference for the run's mod-4-Pascal / p-adic-carry axis (the run's
own proved Rule-90 interior and mod-4 linearization, Odlyzko eq. 201 / CHT
Lemma 3.10, are the mod-2/mod-4 levels of exactly this kind of structure).
It independently confirms the Pascal/binomial skeleton (Rule-90 interior) that
the run proved.

**What it does NOT do:** because its operator is `+` (linear), not `|a−b|`
(nonlinear, carries through the min branch), it gives no bound on the
absolute-difference iteration. In particular it says nothing about the run's
`p-adic-valuation-carry-dynamics` direction for `|a−b|` (the REQUESTS row
stays open), and nothing about regeneration of the leading `{0,2}` block.
The run's discovery that mod-4 is the ceiling of the *free* linear lift of
`|a−b|` (|2−6| = 4 ≢ 0 mod 8 while 2+6 ≡ 0 mod 8) is exactly the point where
this linear `Z_{2^l}` machinery stops applying to the absolute-difference map.

```claim
id: lewis-tefft-2024-sum-ducci-z2l-vanish
statement: For the summing Ducci map D(x)=(x1+x2,...,xn+x1) over Z_{2^l}^{2^k}, every sequence vanishes to 0 with length exactly L_m(n)=(l+1)·2^{k−1} and period 1. The proof uses the binomial/Pascal coefficient recursion a_{r,s}=a_{r−1,s}+a_{r−1,s−1} and mod-4/mod-8 facts about binom(2^j,·).
hypotheses: n=2^k, m=2^l powers of 2; the operator is the sum map (linear), not |a−b|.
holds-here: no — different operator (sum, linear) than the absolute-difference map (nonlinear). Its Pascal/2-adic structure is the same skeleton as the run's proved Rule-90 interior and mod-4 linearization, but the nonlinearity of |a−b| means the mod-2^l carry analysis does not transfer.
status: proved (primary source abstracted)
bearing: gives the concrete Z_{2^l}/binomial structure for a linear Ducci operator; confirms the Pascal skeleton independent of the run; does NOT close the p-adic-valuation-carry direction for |a−b|, which remains the run's own.
anchor: research/sources/lewis-tefft-2024-period-ducci-cycles-z2l-html.full.md
answers: p-adic-valuation-carry-direction-grounding
```
