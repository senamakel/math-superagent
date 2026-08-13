<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/741FD190AF22FFAC67645BCB29324531/S000843950005267Xa.pdf/div-class-title-unitary-perfect-numbers-div.pdf | converted from PDF -->

# Subbarao–Warren (1966) — full text (Cambridge PDF conversion)

The complete primary text of *Unitary perfect numbers*, Canad. Math. Bull. 9
(1966) 147–153 (DOI 10.4153/CMB-1966-018-4); the other two files under this
name are the journal extract page and a different conversion of the same paper.
OCR is degraded; every statement below is read from the converted text.

## What the paper establishes

**Setup.** `N = 2^m · n`, `n` odd, `n = n1·n2·n3` with: `n1` primes ≡ 1 (mod 4);
`n2` primes ≡ 3 (mod 4) to *even* exponent; `n3` primes ≡ 3 (mod 4) to *odd*
exponent. Counts `a, b, c`. `K(a,b,c)` the class of odd parts with those counts;
`B(a,b,c) = max σ*(x)/x` over the class.

**Theorem 1.** No odd unitary perfect number exists.

**Lemma 1** (N = 2^m·n unitary perfect):
- (3.1) `p_r | 2^m + 1` if all exponents are 1;
- (3.2) `a + b + 2c ≤ m + 1`, equality when `c = 0`;
- (3.3) `B(a,b,c) ≥ 2/(2^m+1)` for some admissible `(a,b,c)`.
- **Remark (3.6), the 2-adic budget:** `a + b + Σ C_i = m + 1`, where the sum
  runs over the `n3`-primes and each such `p` contributes `i` with
  `2^i || (1+p)`. Since for `p ≡ 3 (mod 4)` with odd exponent `v2(p^e+1) =
  v2(p+1)` (LTE), and every other component contributes `v2 = 1`, this is
  exactly the run's proved identity `Σ v2(p_i^{e_i}+1) = a_exponent + 1`
  (`research/notes/parity-and-2-adic-budget.md`, claim
  `unitary-perfect-2-adic-budget`). **The identity has 1966 provenance; the
  run's version is an independent complete proof with a witness check, not a
  new result.**

**Lemma 2** (3 | N): `m` even; every `p^α ∥ n` has `p^α ≡ 1 (mod 6)`; some
`p | n` is `≡ 5 (mod 6)` to even exponent; `n` has an even number of distinct
primes. The paper states verbatim: the authors found no UPN not divisible by 3
and could not prove none exist — **this is the primary statement of the open
"is 3 | n forced?" question** (all five known are divisible by 3).

**Theorem 2** (small cases): `r = 1 ⇒ N = 6`; `m = 1 ⇒ {6, 90}`;
`m = 2 ⇒ 60`; `r = 2 ⇒ {60, 90}`; `m = 3, 4, 5, 7` impossible; `r = 3 or 5`
impossible; `m = 6 ⇒ 87360`; `r = 4 ⇒ 87360`. So `ω(odd) ∈ {1,2,4}` are fully
classified and `ω(odd) = 3, 5` excluded already in 1966; the first unclassified
`ω(odd)` was 6 until Wall 1988 (`ω(odd) ≥ 9` for a sixth). Note `m = 8, 9, 10`
are **not** excluded here — that is Subbarao 1970 (see
`research/notes/subbarao-1970-a-ge-11.md`).

**Theorem 3.** Fixed `m` ⇒ finitely many UPNs with `2^m | N`; **Theorem 4**:
finitely many UPNs with a fixed number of distinct primes (claim
`sw1966-finiteness-fixed-omega`).

## Bearing on this run

- (3.6) must be cited as the source of the budget identity; the parity note
  gains a provenance line.
- Lemma 2 is the earliest primary anchor for "3 | n forced?" — still open in
  both directions.
- Theorems 3–4 are the historical grounding of "rarity ≠ finiteness": the
  open question is whether `ω` can grow without bound.

```claim
id: sw1966-budget-identity-36
statement: Subbarao-Warren 1966 Lemma 1 remark (3.6): for a UPN N = 2^m * n
  with n = n1*n2*n3 (n1 primes 1 mod 4; n2 primes 3 mod 4 even exponent; n3
  primes 3 mod 4 odd exponent), a + b + sum_i C_i = m + 1 where each n3-prime p
  contributes i = v2(1+p). This is the 2-adic budget identity
  sum_i v2(p_i^{e_i}+1) = a + 1 in the run's notation, with 1966 provenance.
hypotheses: N unitary perfect, 2^m || N
holds-here: yes; the run's unitary-perfect-2-adic-budget is an independent
  complete proof, checked against all five witnesses
status: catalogued
bearing: names the 1966 origin of the run's central budget constraint; the
  run's derivation remains valid but must be reported as a re-derivation
anchor: research/sources/subbarao-warren-1966-cambridge-pdf.full.md
answers: budget-origin-provenance
```