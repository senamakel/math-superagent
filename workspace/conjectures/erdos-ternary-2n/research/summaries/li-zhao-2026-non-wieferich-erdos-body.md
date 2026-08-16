# Li & Zhao, "Non-Wieferich property of prime ideals and a conjecture of Erdős" — full body

Source: arXiv:2601.12753 (19 Jan 2026), PDF. Full text: `research/sources/li-zhao-2026-non-wieferich-erdos-body.full.md`. This note replaces the earlier abstract-only digest with what the body actually establishes.

## What it establishes

**The Dupuy–Weirich theorem, quoted precisely (this paper's Theorem 3, Section 1.1).**

Given the q-ary expansion `p^n = a_0 + a_1 q + ··· + a_N q^N`, write `(p^n)_{q,i} := a_i`
(the i-th digit). Define the proportion of `b`'s among the first `m` digits of `pn`:

```
f_{p,n,m}(b) := #{ i ∈ [0, m−1] : (p^n)_{q,i} = b } / m
```

Let `L_m := { p^n + q^m Z : n ∈ Z } ⊂ (Z/q^m Z)^×`, `l_m := #L_m`, and the average
proportion over `n`:

```
f_{p,m}(b) := average over the orbit ... = (1/l_m) Σ_{n=1}^{l_m} f_{p,n,m}(b)
```

**Theorem (Dupuy and Weirich [3, Theorem 3]).** Let `p` and `q` be distinct primes
and `b ∈ {0,…,q−1}`. Then `lim_{m→∞} f_{p,m}(b) = 1/q`.

**This is unconditional** — stated for all distinct primes `p, q` and all digits `b`,
with no Wieferich condition in the statement. (This paper generalises it to number
fields and separately generalises Dupuy–Weirich's Theorem 6 on Wieferich primes, but
the rational result stands on its own.)

## What it does NOT do — the precise scope

`f_{p,m}(b)` is an **average over n** of the proportion of `b`'s in the first `m`
digits of `p^n`. It is:

- an asymptotic statement (`m → ∞`),
- an average over the whole orbit of `n`,
- a statement about the *proportion* of a fixed digit, not about the **absence** of
  a digit in a *specific* power.

So it says the ternary digits of `2^n` are asymptotically equidistributed **in
average over n**. It is compatible with the probabilistic heuristic behind Erdős's
conjecture and proves nothing about any particular `n`. In particular it does **not**
rule out a counterexample `n > 8`, and it does not pin down any integer at all. This
is the same gap the heuristic has: equidistribution is about densities, and the
conjecture is about a thin sequence hitting an excluded set.

## Relation to the library's other sources

- The paper also cites **Dimitrov–Howe [2, Theorem 1.2]** (line 48): if `n ∉ {0,2,8}`,
  then the ternary expansion of `2^n` either contains a digit `2` or has at least
  twenty-six `1`s. This matches `research/sources/dimitrov-howe-2021-*`.
- Confirms the interpretation used across the library: the Dupuy–Weirich
  equidistribution is the strongest average digit-distribution statement in this
  line, and it is strictly weaker than (and does not imply) Erdős's conjecture.

```claim
id: DW-THEOREM-UNCONDITIONAL
statement: (Dupuy-Weirich 2016, Theorem 3; quoted in Li-Zhao 2026 Sec 1.1)
  Let p, q be distinct primes and b in {0,...,q-1}. With f_{p,m}(b) the
  average over n of the proportion of digits equal to b in the first m digits
  of p^n, lim_{m->infty} f_{p,m}(b) = 1/q. Unconditional: no Wieferich
  condition in the hypothesis for the rational case.
hypotheses: p, q distinct primes; b a valid digit; the average f_{p,m}(b).
holds-here: yes -- p=2, q=3, b=2 (or any b) gives ternary digits of 2^n
  asymptotically equidistributed in average over n.
status: asserted-by-source (quoted verbatim from Li-Zhao 2026 body, which
  attributes it to Dupuy-Weirich JNT 2016 Thm 3). The primary Dupuy-Weirich
  paper itself is still paywalled, but the statement is now held verbatim.
bearing: equidistribution of ternary digits of 2^n in the average. This is
  compatible with but strictly weaker than Erdos's conjecture; it does not
  rule out any particular counterexample n > 8 and says nothing about which
  integers lie in S. Background, not a proof route.
anchor: research/summaries/li-zhao-2026-non-wieferich-erdos-body.md
answers: primary-full-text-e26b  (Dupuy-Weirich statement now held verbatim
  via this primary number-field generalization that quotes it exactly)
```

## Status

Sourced, exact statement held. The equidistribution theorem is verified as
unconditional (for the rational case) from this primary source. It remains
background, not a proof route, for the reasons above.
