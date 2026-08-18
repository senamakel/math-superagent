# Bonardo–Frid–Shallit: The number of valid factorizations of Fibonacci prefixes (arXiv:1806.09534)

<!-- source: https://ar5iv.labs.arxiv.org/html/1806.09534 | downloaded 2026-08-19 -->

Full text: `research/sources/bonardo-frid-shallit-valid-factorizations-fibonacci-prefixes-ar5iv.full.md`
(also: https://arxiv.org/abs/1806.09534; published in Theoret. Comput. Sci.)

## What it establishes

Pierre Bonardo, Anna E. Frid, Jeffrey Shallit study **V(n)**, the number of factorizations of the
length-n prefix of the Fibonacci word into a (not necessarily strictly) decreasing sequence of
standard Fibonacci words. They establish recurrence relations and an explicit formula: V(n) is the
shuffle of the ceilings of two linear functions of n. The paper works in the Fibonacci (Zeckendorf)
numeration system: canonical representations n = Σ F_{m_k} with m_k − m_{k−1} ≥ 2 form the regular
language ε + 1(0+01)*, and if consecutive Fibonacci numbers are allowed at most once each, the count
is OEIS A000119.

## Why it matters here

- This is the **frontier's top-ranked missing primary source** (16 citations from the library's own
  sources): it is the standard reference for the standard-word prefix-decomposition of Fibonacci
  prefixes, which the run's positional/contiguous-window approach (`fibonacci-position-theorem-contiguous-windows`)
  and Ostrowski-prefix-decomposition axis rest on.
- It gives the canonical Zeckendorf-representation machinery for Fibonacci positions (the automatic-
  digit-DP axis, refuted for this problem by Cobham–Bès–Frougny, but the decomposition itself is
  standard).
- It does **not** give the decimal second-moment formula Ψ(k); it fixes the factor/prefix structure,
  not the weighted sum.

## Claims anchored here

Corroborates the Zeckendorf/prefix-decomposition picture (`ostrowski-prefix-decomposition-characteristic`,
`fibonacci-position-theorem-contiguous-windows`). No new claim block needed.
