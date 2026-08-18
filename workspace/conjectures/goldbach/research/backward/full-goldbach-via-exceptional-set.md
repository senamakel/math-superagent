```skeleton
goal: If every sufficiently large even integer is a sum of two primes and all even integers up to 4·10^18 are verified, then every even integer n > 2 is a sum of two primes.
implies: Combine G-exceptional-density with G-verification-bound and G-structural-closure: a least counterexample would force E(X) ≥ cX for all sufficiently large X, contradicting the exceptional-set estimate E(X) ≪ X^{1−δ}; the finite verification handles the remaining range.
status: live
rests-on: montgomery-vaughan-1975, verification-4e18
```

```gap
id: G-structural-closure
lemma: If a least even counterexample exists, then the exceptional set of binary Goldbach numbers has positive lower asymptotic density: there is c > 0 such that E(X) ≥ cX for all sufficiently large X.
status: open
next: Prove or refute the claimed density-generating closure from least-counterexample minimality; specifically identify an operation preserving failure that produces linearly many distinct even exceptions, and check the claim against the known obstruction that primality of summands is not preserved under translation or multiplication.
```
