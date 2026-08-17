# de Frutos Marín 2012 — Perspectivas aritméticas para la Conjetura de Casas-Alvero (PhD thesis)

**Source:** Rosa María de Frutos Marín, PhD thesis, U. Valladolid, Dec 2012 (advisor
Antonio Campillo López). Full text:
`research/sources/defrutosmarin2013_thesis.full.md`
(originally https://uvadoc.uva.es/bitstream/10324/3602/1/TESIS367-130927.pdf).

This thesis is the arithmetic/scheme-theoretic lineage that the run's bad-prime work
and the Ghosh/Schaub–Spivakovsky program both sit on. It is written in Spanish.

## What it establishes (load-bearing, and checkable)

**The discriminant/superdiscriminant formulation (§5.6).** For degree n and a set of
indices I, the thesis defines discriminants Δ(n,I) (generator of 〈N_1(s_1), R(s_1)⟩ ∩ ℤ)
and resultants δ(n,I) = Res(R(s_1), N_1(s_1)). Observation 5.6.9: Δ(n,I) ≠ 0 ⟺ δ(n,I) ≠ 0
are two independent characterisations of the non-existence of {i,j,k}-counterexamples
to CA of degree n. Lemma 5.6.10 / Thm 5.6.11: for every prime p,
`δ(n,I) ≢ 0 mod p ⟺ Δ(n,I) ≢ 0 mod p AND µ ≢ 0 mod p`, where µ = gcd of the
leading coefficients of R(s_1), N_1(s_1).

**The superdiscriminant D_n (§5.6, terminating Teorema 5.6.13).** With
D_n = ∏_{i=1}^{n−2} Δ(n,I_i):

- **(a)** For n ≥ 3 and any prime p ≥ n: if p ∤ D_n, then p is *efficacious* for n,
  and **CA holds for all degrees n·p^r (r ≥ 0)** — the bad-prime-to-families lift.
- **(b)** For p ∤ D̃_n (the product over the discriminants not yet shown nonzero over ℂ):
  **CA holds in degree n itself.**

The proof of (a) uses the "expansion principle" (§4.3): showing S_{n,J}(F_p) = ∅ for a
prime p, then lifting to n p^r.

## Original claim blocks (from the librarian digest; restored)

```claim
id: defrutos-discriminant-formulation
statement: (de Frutos Marin 2013 thesis, Teo 5.6.6) CA in degree n over C is equivalent
  to the non-vanishing of the superdiscriminant D_n = product_{i=1}^{n-2} Delta(n,I_i),
  where I_i = {i,i+1,...,n-2} and Delta(n,I) is a generator of the elimination ideal
  J(n,I) ∩ Z (intersect with Z of the ideal of the synthetic scheme S_{n,I} in the affine
  chart U_{n,I}). Delta(n,I) != 0 iff U_{n,I}(C) != empty iff no I-counterexample exists.
  One-exponent case: Delta(n,{i}) = 1 - C(n,i) exactly the run's binomial bad-prime
  criterion p | C(n,i)-1. Two-exponent: Delta(n,{i,j}) = (a-1)^i (e-1)^{n-j} Delta^d,
  a=C(n,i), e=C(j,i), d=gcd(n-j,j-i) (Teo 5.6.8).
hypotheses: char-0 field, monic degree n, I ⊆ {1,...,n-2}
holds-here: true (the arithmetic/scheme axis of this run's agenda)
status: asserted-by-source (held full text, not recomputed)
bearing: The binomial bad-prime criterion is not a heuristic: it is the exact
  one-exponent discriminant. Gives a concrete integer to verify for each n in place of the
  abstract minor-criterion J_T. Open comparison: relation of Delta(n,I) to Schaub-
  Spivakovsky J_T (both kill the counterexample ideal).
anchor: research/sources/defrutosmarin2013_thesis.full.md (Def 5.6.1, Teo 5.6.2/5.6.6/
  5.6.8, Def 5.6.5)
falsifies: a source showing Delta(n,I) can vanish while no I-counterexample exists, or a
  recomputation contradicting the D_5 factorisation.
```

```claim
id: defrutos-n5-badprimes-superdiscriminant
statement: The prime divisors of the degree-5 superdiscriminant
  D_5 = Delta(5,{3})·Delta(5,{2,3})·Delta(5,{1,2,3}) are exactly
  {2,3,7,11,131,193,599,3541,8009}, the published degree-5 bad-prime list. Explicitly
  Delta(5,{3})=3^2; Delta(5,{2,3})=2^2·3^2·11·3541; delta(5,{1,2,3})=
  2^24·3^6·7^3·131·193·599^2·8009 (delta and Delta share prime divisors by Teo 5.6.11,
  mu=1). {2,3,7,131,193,599,8009} from delta(5,{1,2,3}); {11,3541} from Delta(5,{2,3}).
hypotheses: degree n=5, char 0
holds-here: true (read-in from thesis; a THIRD independent route to the bad list the run
  verified by rank-mod-p minor criterion and by semantic enumeration)
status: asserted-by-source; corroborated by the run's two other independent computational
  routes agreeing on the same list
bearing: Three independent derivations of the degree-5 bad-prime list now agree:
  (1) Schaub-Spivakovsky minor criterion rank-over-F_p (run-verified), (2) semantic
  is_ca_hasse enumeration (run-verified), (3) this closed-form superdiscriminant
  factorisation. The integers delta(5,{1,2,3}) and Delta(5,{2,3}) are checkable by a
  future symbolic recomputation.
anchor: research/sources/defrutosmarin2013_thesis.full.md (Sec 5.6 worked example)
falsifies: a recomputation that factors D_5 to a different prime-divisor set.
```

```claim
id: defrutos-good-prime-lifts
statement: (Teo 5.6.13) For n>=3 and prime p>=n: (a) if p does not divide D_n then p is
  efficacious for n and CA holds for all degrees n·p^r, r>=0; (b) if p does not divide the
  dynamic superdiscriminant D~_n (product over discriminants not yet shown non-zero over
  C) then CA holds in degree n itself. Also (Teo 4.2.1, resolution by condensation)
  Y_{h p^r}(F_p) != empty iff Y_h(F_p) != empty: an efficacious prime for degree h works
  for degree h p^r.
hypotheses: prime p >= n, char-0 conclusion
holds-here: true (sharper primary route to the run's badprime-upper-bound and n·p^r
  lifting results than sources currently cited)
status: asserted-by-source (held full text)
bearing: Principled "good prime for base degree ⟹ infinitely many degrees" statement for
  the run's p^k / n·p^r settled classes, alongside Graf-von-Bothmer 2007 and Draisma-
  de Jong 2011. 5.6.13(b) is a direct route to CA in degree n from a single prime not
  dividing D~_n.
anchor: research/sources/defrutosmarin2013_thesis.full.md (Teo 4.2.1, 5.6.13)
falsifies: a degree n·p^r with an efficacious prime p ∤ D_n that nevertheless has a
  char-0 counterexample.
```

## Scholar verification (this pass)

The one-exponent discriminant is **exactly** the run's binomial bad-prime criterion:

```claim
id: defrutos-one-exponent-discriminant-equals-binomial-criterion
statement: Delta(n,{i}) = 1 - C(n,i) (Def 5.6.5), so p | Delta(n,{i})  <=>  p | C(n,i)-1.
  Hence de Frutos Marin's one-exponent discriminant is literally the run's binomial bad-prime
  criterion (bad-prime-criterion, Schaub-Spivakovsky Cor 8 arXiv:2307.05997): p bad for degree
  n if p | C(n,i)-1. For n=5, i=3: Delta(5,{3}) = 1 - C(5,3) = 1 - 10 = -9 = -3^2, so
  |Delta(5,{3})| = 3^2, matching the thesis.
hypotheses: degree n, single exponent i in 1..n-1, char 0 / reduction mod p
holds-here: true
status: checked (hand arithmetic: C(5,3)=10, 1-10=-9=-3^2; structural identity is definitional)
bearing: confirms the binomial bad-prime criterion is not ad hoc but is the exact
  one-exponent discriminant of the arithmetic formulation. Corroborates binomial-criterion-calibration.
anchor: research/sources/defrutosmarin2013_thesis.full.md (Def 5.6.5, lines ~10394)
follows-from: defrutos-discriminant-formulation, bad-prime-criterion
```

The superdiscriminant D_5 prime-divisor arithmetic is **consistent with the run's
independently verified degree-5 bad list** (not re-executed here; a coding role should
recompute the large resultants — see request below):

```claim
id: defrutos-superdiscriminant-consistent-deg5
statement: The union of prime divisors of the degree-5 superdiscriminant factors
  Delta(5,{3})=3^2, Delta(5,{2,3})=2^2·3^2·11·3541, delta(5,{1,2,3})=2^24·3^6·7^3·131·193·599^2·8009
  is {3} union {2,3,11,3541} union {2,3,7,131,193,599,8009} = {2,3,7,11,131,193,599,3541,8009},
  which equals EXACTLY the run's independently verified degree-5 bad-prime list
  (badprimes-n5-minor-criterion-verified, rank-mod-p route, code/out/badprimes_n5.captured.txt).
hypotheses: degree 5, char 0
holds-here: true
status: asserted-by-source for the individual factorisations (not recomputed here);
  the set-union identity is checked by set arithmetic against the run's own verified list.
bearing: a third, closed-form route to the degree-5 bad-prime list, agreeing with the two
  routes the run has already verified (rank-mod-p minor criterion; semantic is_ca_hasse).
  The dangerous residue is therefore not in the small-prime set; the only un-checked residue
  is whether delta(5,{1,2,3}) and Delta(5,{2,3}) factor as stated.
anchor: research/sources/defrutosmarin2013_thesis.full.md (Sec 5.6 worked example, lines ~10731-10748)
contradicts: (nothing - agrees with all three run routes)
```

The good-prime lift is the thesis's version of the same result the run holds from
Graf-von-Bothmer 2007 and Castryck 2012:

```claim
id: defrutos-good-prime-lift-corroborates-gvb
statement: Teo 5.6.13(a): if p >= n and p does not divide D_n then p is efficacious for n
  and CA holds for all degrees n·p^r, r>=0. This is the discriminantal form of the
  Graf-von-Bothmer / Castryck lift (gvb-lift, gvb-lift-and-bad-primes): a prime with no
  degree-n counterexample lifts to every n·p^r. Teo 5.6.13(b): if p does not divide the
  dynamic superdiscriminant D~_n then CA holds in degree n itself — a single-prime route to
  CA in degree n, which the run has not yet exploited.
hypotheses: n>=3, prime p>=n, char-0 conclusion
holds-here: true
status: asserted-by-source (held full text)
bearing: corroborates and re-derives the run's n·p^r lifting from a primary (thesis) source;
  (b) offers an alternate single-prime criterion for CA in a fixed degree n.
anchor: research/sources/defrutosmarin2013_thesis.full.md (Teo 5.6.13, lines ~10990+)
follows-from: defrutos-discriminant-formulation
```

## Reconciliation: binomial criterion not exhaustive vs D_5 exhaustive — no contradiction

There is a clean reconciliation between two held claims that a quick reader might take
to conflict:

- `binomial-criterion-calibration`: the *single-exponent* binomial criterion
  p | C(n,i)−1 is sufficient but never exhaustive (n=5 certifies only {2,3} of the 9).
- `defrutos-n5-badprimes-superdiscriminant` / `defrutos-superdiscriminant-consistent-deg5`:
  the *full* superdiscriminant D_5 = ∏ Δ(5,I) over all exponent sets I is **exhaustive** —
  its prime divisors are all 9 bad primes.

No contradiction arises because the binomial criterion is exactly the **one-exponent**
discriminant Δ(n,{i}) (claim `defrutos-one-exponent-discriminant-equals-binomial-criterion`),
whereas D_n is the product over *all* exponent sets I_i = {i,…,n−2}, including the
two- and three-exponent discriminants that supply the missing primes (11, 3541 from
Δ(5,{2,3}); 7,131,193,599,8009 from δ(5,{1,2,3})). The exhaustive judgement lives in the
higher-exponent discriminants, which are exactly what the single-exponent criterion omits.
This is corroborated by the run's own verified list: the three-exponent discriminant's
primes plus the two-exponent discriminant's primes fill in precisely the gap.


- The `arithmetic-jet-lift` / bad-prime framework rests on exactly these notions
  (efficacious/inefficacious primes, the lift to n p^r). The thesis provides an
  independent *discriminant* route to the same bad lists, and Theorem 5.6.13(b) is a
  direct route to CA in degree n itself from a single prime not dividing D̃_n.
- The one-exponent case is checked and coincides with the binomial criterion.
- The worked n=5 superdiscriminant is consistent with the run's own degree-5 bad-prime
  result, but the two large factorisations remain to be recomputed by a coding role.

## What a coding role should verify (outstanding, filed as a request)

A symbolic recomputation (sympy `resultant`, exact integers) of:
- δ(5,{1,2,3}) = Res(R(s_1), N_1(s_1)) where
  R(s_1)=64·(1−5s_1²)(5s_1²−3)(2450s_1⁴−1445s_1²+193),
  N_1(s_1)=−s_1(s_1−1)²(9s_1²−2s_1−3);
  claimed = 2²⁴·3⁶·7³·131·193·599²·8009, µ=gcd(lc R, lc N_1)=1.
- Δ(5,{2,3}) via Teo 5.6.8: (a−1)^i(e−1)^{n−j}Δ^d with a=C(5,2)=10, e=C(3,2)=3,
  d=gcd(5−3,3−2)=1; claimed 2²·3²·11·3541.
These turn `defrutos-superdiscriminant-consistent-deg5` and `defrutos-n5-badprimes-superdiscriminant`
from asserted to checked.

## Caveat

This is a thesis; the discriminant statements are asserted-by-source unless a coding role
recomputes them (the n=5 numbers are the natural calibration). The one-exponent case is
now checked by hand and coincides with the run's verified binomial criterion.
