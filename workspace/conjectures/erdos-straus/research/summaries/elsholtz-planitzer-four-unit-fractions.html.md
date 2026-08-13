# Elsholtz & Planitzer, "Sums of four and more unit fractions and approximate parametrizations"

Source: https://arxiv.org/html/2012.05984 (arXiv:2012.05984), published as
C. Elsholtz and S. Planitzer, Bull. Lond. Math. Soc. 53 (2021) 695–709.
Full text: `research/sources/elsholtz-planitzer-four-unit-fractions.html.full.md`.
(There is a second digest of this same source at
`research/summaries/elsholtz-planitzer-four-unit-fractions.md` covering the
same content; this file is the direct digest of the HTML full text. Read either,
they agree.)

## What it establishes (sourced, primary — verified against the full HTML text)

Counts of represented rationals: `f_k(m,n) = #{(a1..ak) ∈ N^k : a1≤…≤ak, m/n = Σ 1/a_i}`.

**Theorem 1**: `f_4(m,n) ≪_ε n^ε · min{ n^{3/2}/m^{3/4}, n^{8/5}/m }`.
**Corollary 1**: the best of four bounds
`n^ε min{ n^{3/2}/m^{3/4}, n^{8/5}/m, (n^{4/3}/m^{2/3}+n^{28/17}/m^{8/5}), ((n/m)^{5/3}+n^{4/3}/m^{2/3}) }`.
**Corollary 2**: the five sharpest regimes as functions of `m ≈ n^{α/30345}`.
**Theorem 2** (lift to k≥5): `f_k(m,n) ≪_ε (kn)^ε (k^{4/3} n^2/m)^{(8/5)·2^{k-5}}`.
**Remark 2 / §6**: an algorithm listing all 4-term representations of m/n (and
deciding existence) in expected time `n^ε min{...}` — the computational version
of "solve by parametrisation, not by searching n".
**Conjecture 1 (open)**: `f_k(m,n) ≪ exp(C_{m,k} log n / log log n)`.
**Lemma A**: divisor bound `d(n) ≪_ε n^ε`.

**Method — patterns, relative gcds, defining sets (§2, §3, §6).** Write
`a_i = n_i t_i`, `n_i = gcd(a_i,n)`; the tuple `(n_1,…,n_k)` is the **pattern**.
By Lemma A there are `O_ε(n^ε)` patterns. Decompose each `t_i` into pairwise
coprime **relative greatest common divisors** `x_J` (one per subset of indices).
A **defining set** is a subset of the parameters whose assignment leaves only
`O_ε(n^ε)` choices for the rest — i.e. an *approximate parametrisation*: not
a one-to-one correspondence with solutions, but a small parameter set whose
fixing pins the solution up to divisor factors. Lemma 1 lists six such defining
sets; §6 describes how a CAS enumerated candidate ones (96 equations, 8 types).

## Relation to the library and this run

- Same two authors' Proc. R. Soc. Edinb. A 150 (2020) paper (the separate
  counting source on disk) did this for 3 term-sums; this paper is the k≥4 side.
- The "define a shape, sweep only the few remaining parameters" principle is
  exactly the run's ansatz doctrine (search the shape, not the integers), and
  §6's CAS-assisted defining-set discovery is the precedent for the run's
  ansatz search over the Elsholtz–Tao two-family parametrisation.
- It does **not** construct covering identities for the six open classes. Like
  all the counting literature it bounds the number of solutions; it gives no
  new per-class family.

## A caveat about the sibling digest

The other summary
(`research/summaries/elsholtz-planitzer-four-unit-fractions.md`)
states that 3-term solutions come from "2^(k−1)−k−1 free parameters, = 0 for
k=3". **That explicit formula is NOT in this HTML full text**, which only says
the number of parameters "increases exponentially with k" (Intro). The
"only two rigid Type I/II shapes for 3-term solutions" conclusion is consistent
with the library's Elsholtz–Tao Prop 2.1/2.5 + Bloom–Elsholtz Thm 1 and can stand
on *those* sources, but the 2^(k−1)−k−1 count should be treated as asserted by
the sibling digest, not verified here.

```claim
id: elpl21-four-term-approx-parametrize
statement: f_4(m,n) ≪_ε n^ε min{ n^{3/2}/m^{3/4}, n^{8/5}/m } (Theorem 1), and fixing a "defining set" — a partial set of parameters in the relative-gcd/pattern parametrisation — pins a 4-term representation of m/n up to O_ε(n^ε) choices (Lemma 1, §6); the counting bound is proved from these defining sets.
hypotheses: m,n positive integers; ε>0; denominators a_i in increasing order.
holds-here: yes — the defining-set parametrisation is the direct methodological precedent for the run's ansatz search, and the O(n^{3/2}) count at m=4 quantifies how many 4-term representations exist (density of solutions, not a covering construction).
status: sourced (Elsholtz–Planitzer BLMS 53 (2021) 695–709; Theorem 1, Lemma 1, full text on disk).
bearing: supports the "search the shape not the integers" strategy with a proved precedent; gives the run's ansatz search a casuistic model (define a small parameter set, verify the rest are few). Does not settle the open classes.
anchor: research/sources/elsholtz-planitzer-four-unit-fractions.html.full.md
```

## Consequence for this run

Methodological only: the defining-set / approximate-parametrisation machinery is
the counting-theoretic licence for the run's assumption that fixing a
low-degree ansatz leaves few free parameters; and Theorem 1 gives a concrete
`O(n^{3/2+ε})` bound on 4-term representations of 4/n (m=4), useful if the run
ever needs the count of near-solutions. No new theorem about the six open
classes is claimed.
