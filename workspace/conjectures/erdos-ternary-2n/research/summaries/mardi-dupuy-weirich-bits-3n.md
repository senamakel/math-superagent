# Dupuy & Weirich — Bits of 3^n in binary, Wieferich primes and a conjecture of Erdős

<!-- source: https://portal.mardi4nfdi.de/wiki/Item:Q495292 ; primary: https://doi.org/10.1016/j.jnt.2015.05.022 -->

**Primary full text status.** The J. Number Theory 158 (2016) 268–280 paper is
paywalled (DOI 10.1016/j.jnt.2015.05.022) and no free arXiv full text exists.
This MaRDI entry records the paper's statements, theorems, and zbMATH review.
The theorem's precise statement is confirmed here from the primary abstract and
corroborated in full by the Li–Zhao 2026 note held in this library
(`research/sources/li-zhao-2026-non-wieferich-erdos-body.full.md`).

## What the paper establishes (per the review and the Li–Zhao restatement)

**Conjecture (Dupuy–Weirich Conjecture 1.2).** For distinct primes `p, q` and
`b ∈ {0,…,q-1}`, with `d_n(b)` = number of `b`s in the q-ary expansion of `p^n`:

```
lim_{n→∞} d_n(b) / (n · log_q p) = 1/q
```

For `p=2, q=3`, the `b=2` case is exactly: the proportion of digit-2s in the
ternary expansion of `2^n` tends to `1/3`, which for `n` large would force
`d_n(2)>0`, i.e. it would imply the Erdős conjecture (Remark 1.1(ii)).

**Theorem (Dupuy–Weirich [3, Theorem 3]; the first progress on the conjecture).**
For distinct primes `p, q` and `b ∈ {0,…,q-1}`:

```
lim_{m→∞} f_{p,m}(b) = 1/q
```

where `f_{p,m}(b)` is the *average over n of the proportion of digit b in the
first m digits of p^n*:

```
f_{p,m}(b) = lim_{N→∞} (1/N) Σ_{n=1}^{N} f_{p,n,m}(b),
f_{p,n,m}(b) = #{0 ≤ i < m : (p^n)_q,i = b} / m
```

Equivalently `f_{p,m}(b) = (1/l_m) Σ_{n=1}^{l_m} f_{p,n,m}(b)` where
`l_m = #L_m`, `L_m = {p^n + q^m Z}` (a function of the multiplicative order of
`p` mod `q^m`).

## What it does NOT establish — relevant to this run's middle-digit question

**The theorem is an average-over-n statement, not a statement about any single
`n`.** The order of limits matters:

- it first averages over `n` (all `n`, via the group `L_m`), *then*
- lets `m → ∞`.

So it constrains the *average* digit profile of `p^n` over all `n`, never the
digits of one particular `2^n`. In particular, **it cannot constrain the middle
ternary digits of any specific `2^n`** — which is exactly the gap the run's
"middle-digit coupling" targets. The equidistribution line shows the digit-2s
are plentiful *on average*, but that averages over the very exponents `n` where
the conjecture is silent.

The same holds for the Li–Zhao 2026 generalisation (`research/sources/
li-zhao-2026-non-wieferich-erdos-body.full.md`): it proves asymptotic
equidistribution of digits in β-adic expansions of α^n under number-field
hypotheses — again an average/limiting statement, not a per-`n` constraint.

```claim
id: DUPUY-WEIRICH-IS-AVERAGE-NOT-PER-N
status: established
evidence: sourced (primary abstract via MaRDI, corroborated by Li-Zhao 2026 full text in library)
hypotheses: p, q distinct primes; b a base-q digit
holds-here: yes — p=2, q=3, b=2 is Conjecture 1.2's special case
statement: Dupuy–Weirich Theorem 3 proves lim_{m→∞} f_{p,m}(b) = 1/q, where f_{p,m}(b) is the average over ALL n of the proportion of digit b in the first m q-ary digits of p^n. It is an average-over-n equidistribution statement.
consequence-for-run: The digit-uniformity line (Dupuy–Weirich, Li–Zhao) does NOT constrain the middle ternary digits of any specific 2^n, because it averages over n. It gives no per-exponent constraint and cannot by itself prove the Erdős conjecture.
answers: primary-full-text-e26b
```

## What would falsify

The belief that "Dupuy–Weirich equidistribution constrains the middle ternary
digits of a specific 2^n" is false: the theorem averages over n. A claim that a
particular `2^n` must have many digit-2s *from this theorem* is unsupported; the
theorem only says the average over all `n` tends to `1/3`. There is no per-`n`
control. This is the exact finding the open request `primary-full-text-e26b`
was looking for.
