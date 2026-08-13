# Lind 1968 — The quadratic field Q(√5) and a certain Diophantine equation (PRIMARY)

Source: D.A. Lind, "The quadratic field Q(√5) and a certain Diophantine
equation", Fibonacci Quarterly 6(3) (1968) 86–93. Full text read:
`research/sources/lind-1968-quadratic-field.full.md`.
URL: http://www.mathstat.dal.ca/FQ/Scanned/6-3/lind.pdf

## What the paper establishes

A self-contained algebraic-number-theory derivation of the infinite binomial
collision family. Structure:

- **Theorems 1–6**: determine the ring of integers of `Q(√5)` (elements
  `(a+b√5)/2`, `a≡b mod 2`, Thm 2), the **norm** `N(u) = (a²−5b²)/4` (Thm 3:
  unit ⟺ N(u)=±1), and the full unit group (Thm 4: `±α^n, ±α^{−n}` where
  `α=(1+√5)/2`). Theorems 5–6 characterize Fibonacci/Lucas numbers: `α^n =
  (L_n+F_n√5)/2`, and `(a+b√5)/2` is a unit iff `a=L_n, b=F_n`.
- **Theorem 7**: the complete solutions of the Pell-type equation
  `x²−5y²=±4`:
  - `x²−5y² = 4` ⟺ `x=L_{2n}, y=F_{2n}`
  - `x²−5y² = −4` ⟺ `x=L_{2n+1}, y=F_{2n+1}` (n ∈ Z).
  (Already proved by Long–Jordan via Pell theory; Lind gives the unit-group proof.)
- **Section 5 — the binomial equation** `C(n,2) = C(k+1, k−1)` (his eq. (5),
  i.e. `(n choose 2) = (k+1 choose k−1)`; in the notation of the run's family,
  this is the singleton-column/triangular collision). By cancelling common
  factors it becomes `n(k+1) = (n−k)(n−k−1)`, a quadratic in k whose
  discriminant is `5n²+2n+1 = t²`, i.e.
  `(5n+1)² − 5t² = −4` (his eq. (7)) — exactly the Pell equation solved in
  Theorem 7 with `n = (L_{4s+1}−1)/5`, `t = F_{4s+1}`. Using Binet forms,
  `(L_{4s+1}−1)/5 = F_{2s}F_{2s+3}` and the corresponding k gives
  `k = F_{2s−2}F_{2s+1}`. So:

  **all solutions** of the binomial equation are
  `n = F_{2s}F_{2s+3}, k = F_{2s−2}F_{2s+1}, s = 1,2,3,…`
  (Lind's notation; note the shift: with s=1 this gives n=3, k=1 — the small
  solution `C(3,2)=C(2,1)=3`; with s=2, n=15, k=5 — the 3003 pair `C(15,5)=C(14,6)`
  with k+1=6, k−1=4 in his equation).

This is the **original 1968 discovery** of the infinite family that Singmaster
(1975, FQ 13(4)) rediscovered and that the run's ledger records as
`fibonacci-n6-family` / `singmaster-1975-pell-family` / `infinite-family-6`.
Stroeker–de Weger 1999 and Yamada 2020 both attribute the family to "[Lind] and
… Singmaster" — so the primary attribution is now held for both authors.

## Bearing for this run

- **Primary source for the infinite N(a)≥6 family** (it gives the collision
  `C(n,2)=C(k+1,k−1)`; the modern indexing `C(F_{2i+2}F_{2i+3}−1, F_{2i}F_{2i+3}-1) =
  C(F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3}+1)` is the same family with n/k shifted — the
  run's `family_seq` verified values 3003, 61218182743304701891431482520, …
  match). This makes `infinite-family-6` primary-sourced twice (Lind 1968 +
  Singmaster 1975, both held).
- Confirms the **Pell/unit-group mechanism** (`u²−5v²=−4`; fundamental unit
  `9+4√5` in the 1975 presentation = `α⁶` in Lind's indexing) that the run's
  `family_sequences.py` uses to derive the closed recurrences
  `n_i = 7n_{i-1}−n_{i-2}+6`, `k_i = 7k_{i-1}−k_{i-2}+9`.
- No new bound, no uniformity statement, no contradiction to the run's ledger:
  the family is exactly the known infinite B≥6 source. Recorded so the original
  primary is on disk instead of being attested only through Singmaster 1975.

## Claim

```claim
id: lind-1968-fibonacci-family-primary
statement: Lind 1968 (FQ 6(3), 86-93, PRIMARY): via the units of Q(sqrt(5))
  (Thm 4: units are ±alpha^n, alpha=(1+sqrt(5))/2; Thm 6: (a+bsqrt(5))/2 is a
  unit iff a=L_n,b=F_n) and the complete solution x^2-5y^2 = -4
  (x=L_{2n+1}, y=F_{2n+1}, n in Z), the binomial equation (n choose 2) =
  (k+1 choose k-1) has exactly the solutions n=F_{2s}F_{2s+3},
  k=F_{2s-2}F_{2s+1} (s>=1). This is the ORIGINAL discovery of the infinite
  Fibonacci collision family rediscovered by Singmaster 1975 (run's
  fibonacci-n6-family / infinite-family-6).
hypotheses: n,k positive integers; F_0=0,F_1=1, L_n Lucas; s>=1.
holds-here: yes — the run's infinite N(a)>=6 family is primary-sourced to this
  paper (plus Singmaster 1975); the Pell mechanism matches family_sequences.py.
status: asserted-by-source (primary full text read; the run's witnesses.json and
  family_sequences.py independently reproduce the first members)
bearing: completes the primary-sourcing of the infinite B>=6 family (the reason
  any uniform bound must be >= 6); no uniformity or effectiveness content added.
anchor: research/sources/lind-1968-quadratic-field.full.md
answers: none (the family was already in the ledger via Singmaster 1975; this
  adds the original primary and the explicit Pell derivation)
```