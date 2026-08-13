# Singmaster 1975 — Repeated binomial coefficients and Fibonacci numbers

Source: D. Singmaster, Fibonacci Quarterly 13(4) (1975) 295–298; primary scanned
PDF read. [[singmaster-fibonacci-1975]]

## What the paper establishes

**The infinite family (equation (1))**: `C(n+1,k+1) = C(n,k+2)` has **infinitely
many** solutions. From the equation, `(n+1)(k+2) = (n−k)(n−k−1)`; with
`m=n+1, j=k+2`:
`m = [−1+3j+√(5j²−2j+1)]/2`, requiring `5j²−2j+1=s²v²`, i.e.
**`(5j−1)² − 5v² = −4`** (u=5j−1) — a Pell-like equation, completely solvable by
standard theory. All solutions come from `u+v√5 = (L_{2i−1} + F_{2i−1}√5)(9+4√5)^t`
etc.; the class `(9+4√5)` drives the infinitely many solutions. Result (eq (6)):

    n = F_{2j+2}·F_{2j+3} − 1
    k = F_{2j}·F_{2j+3} − 1         (j=1,2,…)

satisfying `C(n+1,k+1)=C(n,k+2)`, so infinitely many binomial coefficients occur at
**least 6 times**.

- First members (n,k): (14,4), (103,38), (713,271), (4894,1868), …
- **j=1**: `n=14,k=4`: `C(15,5)=C(14,6)=3003`.
- **j=2**: `C(104,39)=C(103,40) = 61218182743304701891431482520`; Singmaster
  verified computationally (mod-p and division methods) that this number does **not**
  occur as any other binomial coefficient — so it has exactly the multiplicity from
  the family (6 twice-family + mirrors + trivial).
- There is **no** extension to a triple pattern (consecutive n in (1) impossible).

## The computer search (§4, primary)

Two searches:
1. ALGOL up to `2^23`: built 4717 binomial coefficients `C(n,k)`, `k≥2, n≥2k`, by
   addition, binary-search the preceding rows. Found all seven nontrivial
   repetitions: 120, 210, 1540, 7140, 11628, 24310, **3003**.
2. FORTRAN up to **`2^48`** (60-bit limit): triangular/tetrahedral subroutine +
   binary search. Refound 210, 11628, 24310, 3003 — **no new results**. So
   up to `2^48`, the only `N=8` value is 3003 and the six `N=6` values are as above.

## Conjecture (beyond the 1971 one)

"No binomial coefficient is repeated more than 10 times. (Perhaps the right number
is 8 or 12?)" — Singmaster's own guess; the run's `B=8` witness is consistent with
the lower end of this range.

## Bearing for this run

Primary source for the `infinite-family-6` / `fibonacci-n6-family` claims, with the
full Pell solution and the explicit `2^48` verification frame. This is the exact
basis for "N(a)≥6 infinitely often," and it confirms 3003 (j=1) as the `N=8` record
and that the j=2 value is `N=6` exactly. Cross-checked by witnesses.json / OEIS
A003015.

```claim
id: singmaster-1975-pell-family
statement: Singmaster 1975 (FQ 13(4), primary): C(n+1,k+1)=C(n,k+2) solved
  completely via Pell u^2-5v^2=-4 (u=5(k+2)-1); infinitely many solutions
  n=F_{2j+2}F_{2j+3}-1, k=F_{2j}F_{2j+3}-1 (j>=1), giving infinitely many a with
  N(a)>=6. j=1: 3003=C(15,5)=C(14,6); j=2: 61218182743304701891431482520
  =C(104,39)=C(103,40), verified to occur nowhere else. Computer search up to 2^48
  finds only 3003 with N=8 and exactly 120,210,1540,7140,11628,24310 with N=6.
  Conjecture: no binomial coefficient repeated more than 10 times (maybe 8 or 12).
hypotheses: j>=1; F_0=0,F_1=1 Fibonacci.
holds-here: yes — the basis for N>=6 infinitely often.
status: sourced (primary PDF read; values match witnesses.json/OEIS)
bearing: fixes B>=6; 3003 is the record N=8; j=2 value has N=6 exactly.
anchor: research/summaries/singmaster-fibonacci-1975.md
```
