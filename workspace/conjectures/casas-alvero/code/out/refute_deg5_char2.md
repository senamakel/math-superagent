# Refutation: CA in degree 5 over F_2

Encoded as `code/refute/ca_deg5_char2.p`, run through `find_counterexample`.

```claim
id: deg5-char2-refuted
statement: CA in degree 5 over F_2 is false in the Hasse-derivative
  formulation: f = x^5 + x^4 = x^4(x+1) over F_2 has two distinct roots
  {0, 1} (0 with multiplicity 4, 1 with multiplicity 1), is NOT a pure
  power, yet shares a non-constant factor with every Hasse derivative
  H_1..H_4: H_1 = x^4 (shares root 0; gcd = x^4), H_2 = H_3 = 0
  (gcd(f,0) = f, vacuous), H_4 = x+1 (shares root 1; gcd = x+1).
  Hence p = 2 is a bad prime for degree 5 in the Hasse formulation.
hypotheses: char K = 2, degree n = 5, Hasse-derivative CA hypothesis
holds-here: true (this is exactly the char-p statement; CA is false in char p)
status: checked
bearing: First n=5 refutation in the refute TPTP set (degrees 3, 4, 6 were
  already exercised; degree 5 was not). Independent SEMANTIC finite-model
  route corroborates the run's n=5 bad-prime list {2,3,7,11,131,193,599,
  3541,8009} (Castryck et al. 2012 Thm 4), which was previously verified
  only by rank-over-F_p and SNF at n=4. Not a new claim about char 0: over
  Q, CA holds in degree 5 (true), and this char-p counterexample is exactly
  the break at the bad prime p=2.
anchor: code/refute/ca_deg5_char2.p (find_counterexample -> refuted),
  hand-verification below
falsifies: a finite model over F_2 satisfying the Hasse-CA hypothesis for
  degree 5 with f a pure power (none exists; p=2 is bad).
```

## Why the statement, and what it targets

The run's weakened target ladder treats `R-ca-elim-boundary` — CA over `Q` for
n = 5, 6, … — as char-0 statements to *prove*. The refuter's job is the char-p
break each such statement must exhibit. The run has already *thrown away* one
false generalisation (a char-free reading of CA is false over F_2, and the
ordinary-derivative vacuity `x^p+x^{2p}` does not survive Hasse). This note
adds the degree-5 row to that char-p sweep, at a degree the refute folder had
never attacked.

## Verification against the original statement (by hand)

`f = x^5 + x^4`, monic degree 5 over F_2. Coefficients c_5=1, c_4=1, c_3=c_2=c_1=c_0=0.
Hasse derivative H_i = sum_j C(j,i) c_j x^{j-i}:

- H_1 = 5x^4 + 4x^3 + 3·0x^2 + 2·0x + 0 = x^4 (5≡1, 4≡0 mod 2).
  gcd(x^5+x^4, x^4) = x^4, nonconstant — shares root 0.
- H_2 = 10x^3 + 6x^2 + 3·0x + 1·0 = 0 (10,6 ≡ 0 mod 2). gcd(f, 0) = f, nonconstant.
- H_3 = 10x^2 + 4x + 3·0 = 0. gcd(f, 0) = f, nonconstant.
- H_4 = 5x + 4·1 = x + 1. f(1) = 1+1 = 0, so x+1 | f; gcd(x^5+x^4, x+1) = x+1,
  shares root 1.

So f shares a non-constant factor with every Hasse derivative H_1..H_4: the
hypothesis holds. f has zeros at 0 and 1 (two distinct roots) and so is NOT a
pure power. This refutes "CA holds in degree 5 over F_2".

The TPTP model returned by `find_counterexample` (domain {0,1}: f(0)=0, f(1)=0;
h1 = identity [x^4]; h2 = h3 = 0; h4 = x+1) is exactly this f. Hand-checked and
consistent with the engine's output.

## Status

`refuted` — a genuine counterexample, checked against the original statement.
It corroborates the run's degree-5 bad-prime list (p=2 ∈ {2,3,7,11,131,193,
599,3541,8009}) by a second, independent, semantic route that had never been
run at n=5. It does not touch the char-0 statement (CA over Q, true for n=5);
it is precisely the char-p break at the bad prime.
