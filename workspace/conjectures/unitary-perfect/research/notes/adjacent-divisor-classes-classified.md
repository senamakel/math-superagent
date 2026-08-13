# Adjacent divisor classes are finite and classified — the contrast with unitary perfect

Three primary sources newly in the library settle the *neighbouring* classes
completely, each by going up one level of divisor refinement. The unitary
perfect case (Subbarao–Warren conjecture) is the exceptional member of this
family that is still open. This note records what they establish, for the
run's structural comparison, and nothing beyond that.

## Wall 1972 — bi-unitary perfect numbers

Source: `research/sources/wall-1972-bi-unitary-perfect-numbers.full.md`
(C. R. Wall, "Bi-unitary perfect numbers", Proc. Amer. Math. Soc. 33 (1972)
39–42, DOI 10.1090/S0002-9939-1972-0289403-9).

```claim
id: wall1972-biunitary-perfect-classified
statement: The bi-unitary perfect numbers are exactly 6, 60 and 90. A
  bi-unitary divisor d of n is one whose greatest common *unitary* divisor
  with n/d is 1. Theorem 1: no odd bi-unitary perfect numbers. Theorem 2:
  the only even bi-unitary perfect numbers are 6, 60, 90.
hypotheses: prime-power multiplicativity of the bi-unitary divisor sum
  sigma**(p^a) = p^a + 1 (a odd), p^a (a even), per Proposition 1 of the
  paper; N bi-unitary perfect means sigma**(N) = 2N
holds-here: yes - a complete classification of the class one refinement
  level up from unitary divisors; 90 keeps its 3^2 kernel there too
status: sourced (primary full text held, OCR clean)
bearing: finiteness for bi-unitary perfect is *proved*; the method (explicit
  sieve over a with the budget identity, exactly the workspace's 2-adic
  budget structure) is the template the open unitary case is missing the
  final step of
anchor: research/sources/wall-1972-bi-unitary-perfect-numbers.full.md
answers: what-is-known-about-adjacent-divisor-classes
```

## Cohen 1990 — k-ary and infinitary divisors

Source: `research/sources/cohen-1990-infinitary-divisors.full.md`
(G. L. Cohen, "On an integer's infinitary divisors", Math. Comp. 54 (1990)
395–411, DOI 10.1090/S0025-5718-1990-0993927-5).

```claim
id: cohen1990-infinitary-perfect-classified
statement: The infinitary perfect numbers not divisible by 8 are exactly 6,
  60 and 90 (Theorem 16). Towers of k-ary divisors: d is k-ary if its
  greatest common (k-1)-ary divisor with n/d is 1; infinitary is the
  k -> infinity limit; the infinitary divisors of p^y are p^x for the binary
  digits x carried by y (Theorem 7).
hypotheses: standard; sigma_infinity multiplicative with
  sigma_infinity(p^a) = sum of the p^x, x subset of the 1-bits of a
holds-here: yes - adjacent-class classification; the 6,60,90 non-divisible-
  by-8 statement is a theorem, not a conjecture
status: sourced (primary full text held)
bearing: two of the three refinement classes ABOVE unitary are fully
  classified finite; the boundedness exploits that going one level up moves
  the parity budget (v2(p^a+1) vs v2 of the k-ary sum) off the divisors -
  the exact mechanism the run's unitary budget identity would need to close
anchor: research/sources/cohen-1990-infinitary-divisors.full.md
answers: what-is-known-about-adjacent-divisor-classes
```

## Hagis 1984 — lower bounds for unitary multiperfect numbers

Source: `research/sources/hagis-1984-lower-bounds-ump.full.md`
(P. Hagis Jr., "Lower bounds for unitary multiperfect numbers", Fib. Quart.
22(2) (1984) 140–144).

```claim
id: hagis1984-ump-lower-bounds
statement: There are no odd unitary multiperfect numbers (Theorem 1). For a
  unitary *multiperfect* n = 2^a * prod p_i^{a_i} with sigma*(n) = k n,
  k >= 4: if k = 4 or 6 then t (number of distinct odd prime factors) > 51,
  n > 10^1010, and 2 | n; if k > 8 then t > 247, n > 10^6663. For unitary
  triperfect (k = 3): t > 45, n > 10^102, 2^166 | n, with sharpenings when
  3^2 || n or 3^3 || n (Theorem 3). NOTE: this is the incidentally-occurring
  "10^102" in the library - it is the k=3 (triperfect) lower bound, NOT the
  Wall sixth-UPN search bound, which remains an orphan claim.
hypotheses: k > 2 (multiperfect parameter); the paper's budget inequality
  (1) bounding t in terms of a and k
holds-here: yes - bounds for the multiperfect version; the k=2 case is the
  unitary perfect problem and is NOT covered by these statements
status: sourced (primary full text held)
bearing: the budget inequality method (t < a bound in terms of the target
  ratio k) is the same shape as the workspace's omega(odd) <= a+1 budget;
  the k>=4 machinery does not transfer to k=2 but the extremal-product
  technique is the model for the open omega -> a lower bound
anchor: research/sources/hagis-1984-lower-bounds-ump.full.md
answers: what-is-known-about-adjacent-divisor-classes
```

## What this means for the run

The refinement ladder (unitary → bi-unitary → k-ary → infinitary) is finite
and classified at the top three rungs, and the exceptions `{6, 60, 90}` are
exactly the squarefree-odd-part members of the unitary list (Graham 1989).
The unitary rung is the only one still open. The mechanism in Cohen 1990 /
Wall 1972 that closes the higher rungs is that the divisor sum of a prime
power loses its "+1" unit at even exponents, killing the parity budget that
the unitary case still has (the workspace's exact identity
`Σ v2(p_i^{e_i}+1) = a+1`). This is a structural contrast worth one careful
look, not a transferable proof: each rung is its own sieve, and none of the
three papers touches `σ*(n) = 2n` with repeated odd prime powers.