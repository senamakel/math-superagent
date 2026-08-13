# A. Bazsó, I. Mező, Á. Pintér, Sz. Tengely, "Singmaster-type results for Stirling numbers and some related diophantine equations" (arXiv:2311.06080, 2023)

Source: https://arxiv.org/abs/2311.06080 ; full HTML at
https://arxiv.org/html/2311.06080v1
Full text: `research/sources/singmaster-type-stirling-2023.full.md`

## What it is

2023 (Debrecen school: Bazsó–Mező–Pintér–Tengely) transfer of Singmaster's
question to the Stirling numbers of both kinds. M_i(a) = number of times the
integer a appears among the Stirling numbers of the i-th kind (i=1,2).

## Results

- **Thm 1 & 2**: for all a ≥ 2,
  `M_2(a) ≤ 2 + 2 log a / W(½ log a)` and likewise `M_1(a)`, where W is the
  Lambert W function. Hence `M_i(a) = O(log a / (log log a − log log log a))`.
  Method: the exact template of Singmaster's 1971 argument — monotonicity of
  the Stirling triangle rows, choose the least b with the central column
  exceeding a, bound b via a growth estimate (here the associated Stirlings),
  then `M ≤ 2b` (one solution per row index per column index, two directions).
- Numerical tables up to a = 100000. Second-kind: the only doubles are
  {15, 4095, 66066}, where e.g. {14 \brace 11} = {364 \brace 363} = 66066.
  First-kind: only {6, 120} occur twice (1 occurs infinitely often).
- **Conjecture 1**: the unique solution of C(n,4)+10C(n,5)+15C(n,6) = C(m,2)
  (n≥6) is (n,m) = (14,364). Checked up to n = 4.6×10^7 by MAPLE.
- **Theorem 3**: under the ABC-conjecture, n! = P_k(x) (k-gonal number) has
  only finitely many solutions for fixed k≠4; with a Legendre-symbol sieve over
  19 primes > 10^5 the complete solution list for 3 ≤ k ≤ 50, n ≤ 10^5 is
  (k,n,x) = (3,3,3),(3,5,15),(6,3,2),(6,5,8),(9,4,3),(24,4,2),(41,5,3). For
  k=4, n! = x² has unique solution (1,1) (Bertrand).
- Also confirms the Singmaster record: N(3003)=8; N(a)=6 for infinitely many a
  (cites [12],[15],[16]); best known global bound is Kane 2007.

## Relevance

- A 2023 primary confirmation that the current record and the main structural
  facts (N(3003)=8, infinite N=6 family, Kane record bound) are stable.
- The transfer shows the "monotone triangle → bound the central column → M≤2b"
  template is robust; for the binomial triangle it yields exactly Singmaster's
  N(a) ≤ 2+2 log_2 a.
- The related Diophantine equation C(n,4)+10C(n,5)+15C(n,6)=C(m,2) is a
  single-column vs k=2 intersection — the same small-k boundary family; the
  authors note "the solution to the above conjecture is out of reach of current
  methods," a candid statement of the effective-results wall.

## Claims

```claim
id: stirling-2023-bound-and-record
statement: Bazso-Mező-Pinter-Tengely 2023 (arXiv:2311.06080, Debrecen):
  the number M_i(a) of times an integer a occurs among Stirling numbers of
  kind i satisfies M_i(a) <= 2 + 2 log a / W((1/2) log a) for a >= 2 (Lambert
  W), hence O(log a/(log log a - log log log a)); up to a=100000 the only
  repeated second-kind values are {15, 4095, 66066} and first-kind {6, 120}.
  The paper re-confirms N(3003)=8 and the infinite N(a)=6 family, and cites
  Kane 2007 as the record global binomial bound.
hypotheses: a >= 2; Stirling triangles of both kinds; standard Lambert W.
holds-here: yes (this is the Stirling analogue of Singmaster; the binomial
  record statements agree with the run's witness ledger).
status: asserted (quoted from the arXiv full text)
bearing: independent 2023 primary corroboration of the run's three pillars
  (3003 record, infinite 6-family, Kane-best-bound); shows the Singmaster
  counting template has a robust analog family.
anchor: research/sources/singmaster-type-stirling-2023.full.md
```