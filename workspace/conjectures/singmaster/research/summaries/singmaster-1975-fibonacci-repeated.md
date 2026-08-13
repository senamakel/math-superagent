# Singmaster 1975 — Repeated binomial coefficients and Fibonacci numbers (PRIMARY, FQ 13(4))

Source: David Singmaster, "Repeated Binomial Coefficients and Fibonacci
Numbers", The Fibonacci Quarterly 13(4) (1975) 295–298. Downloaded the full
text from the Fibonacci Quarterly archive:
https://www.fq.math.ca/Scanned/13-4/singmaster.pdf
Full text: `research/sources/singmaster-1975-fibonacci-repeated.full.md`.
(This file is also in the library as `research/sources/singmaster-fibonacci-1975.full.md`
— the same paper; this fetch is the author-verified FQ scan with the complete
2^48-search description.)

## What this primary establishes (author's own words)

1. **The infinite N(a) ≥ 6 family (Theorem, §2–3).** There are infinitely many
   solutions to
       C(n+1, k+1) = C(n, k+2)
   given by
       n = F_{2j+2} F_{2j+3} − 1,   k = F_{2j} F_{2j+3} − 1   (j ≥ 1)
   (F_0 = 0, F_1 = 1). Hence infinitely many binomial coefficients occur at
   least 6 times. The proof goes through Pell's equation (the paper's Lemma on
   L_n + F_n√5 and the identity (L_n + F_n√5)(9 + 4√5) = L_{n+6} + F_{n+6}√5),
   connecting the Fibonacci family to the Pell equation u² − 5v² = −4 with
   u = 5(k+2) − 1.
2. **The complete result of the computer search up to 2^48 (§1, §4).** "A
   computer search up to 2^48 has revealed only the following seven nontrivial
   repetitions":
       120  = C(16,2) = C(10,3)
       210  = C(21,2) = C(10,4)
       1540 = C(56,2) = C(22,3)
       7140 = C(120,2) = C(36,3)
       11628= C(153,2) = C(19,5)
       24310= C(221,2) = C(17,8)
       3003 = C(78,2) = C(15,5) = C(14,6)
   (notation in the source is C(.,.) with the smaller k written second in some
   lines and first in others; the pairs above are the nontrivial
   representations). 3003 is additionally triangular and tetrahedral; the
   paper notes [2] (Avilés?/the triangular–tetrahedral classification) proved
   the only numbers both triangular and tetrahedral are 1, 10, 120, 1540, 7140.
3. **Two searches described:** an ALGOL search to 2^23 (all C(n,k), k>2, n>2k,
   check repeats in preceding rows) and a FORTRAN search to 2^48 on a CDC 6600
   (60-bit word, checking triangularity/tetrahedrality on the fly without
   storing them; 2^48 = 281474976710656 ~ 2.8×10^14).
4. **Conjecture restated (§1)**: the number of times an integer occurs as a
   binomial coefficient is bounded (Singmaster [6] = the 1971 Monthly note).

## Cross-checks with the run's own computations

- The seven values are EXACTLY the nontrivial representations in
  `code/out/witnesses.json` (six N=6 values 120…24310 plus the 3003 triple).
  The run verified N(3003)=8 and the six N=6 values independently by direct
  computation; this primary independently corroborates the witness list.
- 120, 210, 1540, 7140, 11628, 24310 all have N(a)=6; 3003 has N(a)=8
  (both-halves + trivial-pair convention). The run's `fibonacci-n6-family`
  claim (first member 3003, second 61218182743304701891431482520) matches the
  j=1,2 members here.

## Bearing for the run

- This is the PRIMARY for the infinite N(a) ≥ 6 family — the reason B ≥ 6.
- The 2^48 search bound is the current "verification bound" claim: no
  nontrivial collision beyond the seven listed below 2^48 (values), and (via
  the row structure) no N(a) ≥ 8 except 3003 in that range — matching the
  `singmaster-1975-pell-family` and `bbw-verification-bound` claims.
- It also attests Singmaster 1971's conjecture and O(log a) bound (cite via
  this held primary when the 1971 Monthly article is still paywalled).

```claim
id: singmaster-1975-search-and-family-primary
statement: Singmaster FQ 13(4) 1975 (held primary): (i) infinitely many
  solutions of C(n+1,k+1)=C(n,k+2), n=F_{2j+2}F_{2j+3}-1, k=F_{2j}F_{2j+3}-1,
  j>=1, give infinitely many binomial coefficients occurring at least 6 times
  (Pell u^2-5v^2=-4, u=5(k+2)-1); (ii) a computer search up to 2^48 found only
  the seven nontrivial repetitions 120,210,1540,7140,11628,24310,3003 (the
  last with the triple C(78,2)=C(15,5)=C(14,6)); 3003 is the only N(a)>=8 in
  that range.
hypotheses: n,k nonnegative integers; F_0=0,F_1=1; the search covers values
  up to 2^48 and rows within that range.
holds-here: yes — this is the primary source of the infinite B>=6 family and
  of the current verification bound; the run's witnesses.json reproduces the
  same seven values independently.
status: asserted-by-source (PRIMARY full text held at
  research/sources/singmaster-1975-fibonacci-repeated.full.md); the six N=6
  values and N(3003)=8 are also independently computed in code/out/witnesses.json
  (status: checked for the numeric side)
bearing: anchors B>=6 (infinite family) and the 2^48 verification bound in a
  held primary; corroborates the witness ledger.
anchor: research/summaries/singmaster-1975-fibonacci-repeated.md
```