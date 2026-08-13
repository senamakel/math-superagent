# Tian's Conjecture on the Prime Factorization of the Binomial Coefficient C(n+1,2) — abstract-level record

Source: Zhenbing Zeng, Ákos Pintér, Xinchu Fu, Jianjun Paul Tian, "Tian's
Conjecture on the Prime Factorization of the Binomial Coefficient (n+1 choose
2)", Mathematics (MDPI) 14(1), 127 (2025-12-29), pp. 1-11.
Bibliographic record + abstract held (RePEc/IDEAS mirror of the MDPI record):
`research/sources/tian-conjecture-cn1-2-factorization-2025.full.md`.
**Full text NOT held** — MDPI returns HTTP 403 to this container; the RePEc
page carries only the abstract and metadata, no theorems, tables, or proofs.

Previously flagged (research/summaries/claimed-resolutions-2025-2026-caution.md)
as "403-blocked; adjacent to Singmaster". Now the abstract itself is in the
library, so the conjecture's statement is precise; the paper's contents remain
outside.

## What is established by the abstract (asserted-by-abstract, NOT checked here)

**Tian's conjecture:** for fixed distinct primes `p₁,...,p_m`, the Diophantine
equation

    C(n+1,2) = n(n+1)/2 = p₁^{α₁} · p₂^{α₂} ··· p_m^{α_m}

in positive integers `n, α₁, ..., α_m` has **at most m solutions**.

The paper is described as: (a) developing a computational method to verify
special cases (the search summary adds: estimating linear forms in elliptic
logarithms); (b) giving an alternative proof of a first sub-conjecture via the
classical **Zsigmondy theorem**; (c) giving a **sharp absolute upper bound for
the number of solutions for m = 2 and 3** (e.g. at most 4 for the two-prime
case, at most 6 for the three-prime case with p₁=2, in certain formulations —
per the MDPI search abstract, not verified against the paper's own text).

## Bearing for this run — what it does and does NOT give

**Relevance:** this is fixed-column structure for the **k = 2 column** (the
triangular numbers, `C(n+1,2)`), the column that carries several Singmaster
witnesses: `3003 = C(78,2)`, `120 = C(16,2)`, `1540 = C(56,2)`,
`7140 = C(120,2)`, `11628 = C(153,2)`, `24310 = C(221,2)` — every one of the
six `N(a)=6` values below `2^48` has a k=2 representation. Tian's conjecture
says: for a fixed prime set of size m, a triangular number built from exactly
those primes has at most m triangular representations. This corroborates the
run's standing theme ("small columns carry the multiplicity; a uniform bound
must control them uniformly") with a *structural* conjecture about the k=2
column's multiplicity — but note it is a bound on representations **as
triangular numbers**, i.e. solutions of `C(n+1,2)=a` as n varies, NOT a bound
on `N(a)` (representations across all columns).

**What it is NOT:** Tian's conjecture is not a proof of Singmaster's
conjecture, not a bound on `N(a)`, and not verified by this run. Its "at most
m" bounds the *number of n* making `C(n+1,2)` equal to a fixed prime-combination
shape, which is a different (fixed-column, fixed-prime-support) question. It
does not touch the k=2 column's cross-values (`C(n,2)` meeting `C(m,k)`, k≠2),
which is where 3003's multiplicity actually comes from. And even the m=2,3
sharp bounds are asserted in the abstract, not reproduced here.

## Status

`asserted-by-abstract` only. The paper's claims are adjacent corroboration for
the k=2-column theme, not a held theorem and not a Singmaster result. If a
later run needs the paper's actual theorems (the Zsigmondy proof, the
elliptic-logrithm computations, the exact m=2/3 bounds), it must obtain the
MDPI full text through a route that is not blocked.

```claim
id: tian-2025-k2-column-abstract-record
statement: Tian's conjecture (Zeng-Pinter-Fu-Tian, Mathematics 14(1):127,
  2025): for fixed distinct primes p1..pm, the equation C(n+1,2)=p1^{a1}..pm^{am}
  has at most m positive-integer solutions (n,a1,..,am). The paper verifies
  special cases computationally and gives a Zsigmondy-theorem proof of a first
  sub-conjecture, with sharp absolute bounds for m=2,3.
hypotheses: fixed finite distinct prime set; triangular numbers (k=2 column).
holds-here: ADJACENT-ONLY — fixes the k=2 column's triangular-representation
  multiplicity for fixed prime support; does not bound N(a) (cross-column
  representations untouched, e.g. 3003's multiplicity involves k=2,5,6).
status: asserted-by-abstract (full text 403-blocked; abstract held via RePEc)
bearing: corroborates the small-columns-carry-multiplicity theme at a
  structural-conjecture level for the k=2 column; NOT a Singmaster result.
anchor: research/sources/tian-conjecture-cn1-2-factorization-2025.full.md
```