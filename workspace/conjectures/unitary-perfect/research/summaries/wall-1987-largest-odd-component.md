# Wall (1987), *On the largest odd component of a unitary perfect number*

Full text: [[wall-1987-largest-odd-component.full]] (Fibonacci Quarterly 25, no. 4 (1987) 312–316, genuine OCR).

**Setup.** UPN `N = 2^a m`, `m` odd; `K` = largest odd prime-power unitary component. The problem is equivalent to writing 2 as `Π (denominator+1)/denominator` with denominators distinct prime powers.

**Result.** Except for the five known UPNs, the largest odd component `K > 2^15` (smallest admissible candidate is 32771). Proof mechanics:

- For each odd prime `p < 2^15`, the *entry point* of `p` (smallest `A` with `2^A ≡ −1 mod p`) is computed; `p | 1 + 2^a` iff `a` is an odd multiple of its entry point.
- Only two primes `< 3·10^9` have `p^2 | 1 + 2^A` (Wiebferich-like phenomenon): **1093 and 3511**; for these, `1 + 2^A` has a component `> 2^15`.
- So for `p < 2^15`, either `p ∤ 1 + 2^a`, or `p || 1 + 2^a`, or the component `> 2^15`.
- Algebraic factors show `1 + 2^a` has all components `< 2^15` only for `a ≤ 11` and the `a` values in Table 1 (`2^18, 2^21, 2^22, 2^25, 2^26, 2^30, 2^33, 2^34, 2^42, 2^46, 2^78`, each with an explicit factorization giving a large component). Wall credits Subbarao's bound `a ≥ 10` for new UPNs.

**Consequence for this run.** This is the input Wall 1988 uses to force the "least unknown odd component ≥ 32771" floor in the seven/eight-component exclusions, so it underpins `ω(odd) ≥ 9` (Wall 1988) and hence `a ≥ 8`. The identification of exactly two `p` with `p^2 | 2^A + 1` (1093, 3511) below `3·10^9` is a bounded computational claim (catalogue-grade) not reproduced here.

```claim
id: wall1987-largest-odd-component
statement: Except for the five known UPNs, a unitary perfect number has an odd
  component larger than 2^15 (smallest candidate 32771); and among primes
  p < 3*10^9 only 1093 and 3511 satisfy p^2 | 1 + 2^A for their entry point A.
hypotheses: N = 2^a m unitary perfect not among the five known; entry-point
  computation over odd primes p < 2^15; Subbarao's a >= 10 for new UPNs
holds-here: yes - applies to any sixth UPN, the object the run targets
status: asserted
bearing: supplies the 32771 component floor used by Wall 1988 to derive
  omega(odd) >= 9, and hence the a >= 8 lower bound on a sixth UPN
anchor: research/summaries/wall-1988-nine-odd-components.md
contradicts: (none)
answers: whether-6th-UPN-large-odd-component
```
