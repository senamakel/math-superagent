# Schaeffer & Shallit, "The local period of a Sturmian word and its Ostrowski representation" (2012)

**Source:** arXiv:1210.2343 (https://arxiv.org/pdf/1210.2343). Full text:
`[[schaeffer-ostrowski-local-period-sturmian-2012.full]]`.

## What it establishes

**Object.** The *local period* at position n of a characteristic Sturmian word
c_α (the shortest length p such that the c_α-bordered segment around n repeats
— the "repetition word" / local periodicity of Restivo–Mignosi), for the word
with digit function c_α(i) = ⌊α(i+1)⌋ − ⌊αi⌋ − ⌊α⌋, α irrational.

**Main results.**
- The local period at position n of c_α is computable directly from the
  **Ostrowski representation of n+1** (Theorem 13): with OR_α(n+1) =
  d_k···d_0 and t = number of trailing zeros of that representation, the local
  period r_α(n) is a conjugate of the standard word X_t (from the directive
  sequence), except in a listed exceptional case.
- Supporting structure: Lemma 10/12 give prefix decompositions
  c_α[0..n−1] = φ_k(c_β[0..m−1])·0^{d_0} between the word and its
  one-step-shifted directive sequence ("unbending" the Ostrowski digits —
  the same family of identities as Frid's Lemma 1); Proposition 6/7 build the
  standard words X_n from the directive sequence.

**Hypotheses.** α irrational (characteristic Sturmian word); OR_α the
Ostrowski numeration of n+1. For PE1006: α = 1/φ² has continued fraction
[0;2,1,1,...] — the Fibonacci case, where Ostrowski is Zeckendorf and the
standard words X_n are the finite Fibonacci words.

## Bearing on PE1006

**Does not help the Ψ(k) computation.** The paper targets *local periods*
(a repetition/border property of a single position), not factor-set values or
their weighted sums. Its Ostrowski-prefix machinery (Lemmas 10/12) is the same
numerational axis as the Frid note and the run's Zeckendorf digit-DP approach,
but no statement here bears on the decimal-value polynomial of a factor, the
factor set itself, or a floor-sum. Verdict: **background**; no claim needed on
disk. It does corroborate that the "Ostrowski/Zeckendorf representation of a
position" is the right way to talk about positions in the Fibonacci word — but
the committed O(log) route is the universal-Euclidean floor-sum monoid, which
does not use it.

No claim block: nothing the run leans on is established by this source.