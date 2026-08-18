# Refutation note: minimal-counterexample closure is unsupported

```approach
id: structural-closure-analogue
idea: A least Goldbach counterexample should force the exceptional set to have
positive lower density, perhaps by closure under translation by a modulus,
multiplication by primes, or a Bohr-set mechanism. This would close gap
G-structural-closure of the backward decomposition.
status: refuted
closed-reason: Minimality alone gives no closure operation; translation and prime
multiplication do not preserve the exact additive primality predicate, and the
singular-series main term is only a local major-arc feature that does not
control minor-arc cancellation. The conditional skeleton survives (E=O(X^(2/3))
plus E>>X would force E=0) but the positive-density inference is unsupported.
claim-attacked: A least binary-Goldbach counterexample should force the full
exceptional set E(X) to have positive lower density, perhaps by closure under
translation by a modulus, multiplication by primes, or a Bohr-set mechanism.

hand-check: Minimality alone gives only that every smaller even integer has a
representation. It gives no implication for larger integers. The proposed
maps are especially implausible: Goldbach representations depend on the exact
additive shift n, while primality is not preserved by either translation or
multiplication of n.

small-oracle: `code/refute/closure_oracle.py` is the naive exact oracle. It
checks all even n <= 200 and directly tests the proposed maps if an exception
exists. It reports no Goldbach exception in this range, so the implication is
vacuous there. This is a required oracle check, not evidence for closure.
`code/refute/closure_analogues.py` tests analogous predicates and exhibits the
same logical failure mode: a least failure of a simple arithmetic predicate
does not imply translation closure or a density conclusion. These are analogy
counterexamples, not Goldbach counterexamples.

finite-model-attack: `code/refute/goldbach_closure.p` was submitted to
`find_counterexample`. Result: `undecided`, no countermodel and no proof at the
sizes reached. The encoding is only a sanity fragment (not a faithful
first-order formalisation of standard arithmetic/primality), so this result
cannot establish Goldbach or the closure claim.

why-the-structural-step-fails: The cited circle-method structure is local: the
major-arc main term contains a positive singular series, but a failure means
minor arcs cancel that term at one integer. No known theorem turns one such
cancellation into cancellation for a positive-density family. The singular
series is not periodic in a way that preserves the sign or size of the full
representation count. Similarly, sieve parity permits prime/semiprime
ambiguity, rather than a closure law on the exceptional set.

search-frame: hand tests n=0,1,2 and degenerate small predicates; exact oracle
for even n <= 200; finite-model search at its reached sizes. This lies far
inside the published Goldbach verification through 4*10^18, so it finds no
new Goldbach frontier. The analogue failures are smallest-scale logical
obstructions to the proposed inference, not witnesses to E.

what-would-be-needed: A genuine closure theorem must be stated with a concrete
map T and prove n in E => T(n) in E for a positive-density family, while
preserving the exact Goldbach predicate. No such theorem is in the current
library. The density-vs-sparsity skeleton is therefore logically conditional,
not a route presently supported by known structure.
```

## Refuter's verdict

`full-goldbach-via-exceptional-set` is not refuted as a conditional logical
skeleton: an upper bound `E(X)=O(X^(2/3))` is incompatible with a proven lower
bound `E(X) >> X`. What is refuted is the likely inference that minimality or
singular-series considerations supply that lower bound. The smallest
analogous closure assertions fail immediately because additive primality has
no monotone or semigroup closure.

The finite-model search is `undecided`, not `proved`: its weak language does
not faithfully encode standard natural numbers. The exact small computation
also finds no Goldbach counterexample, as expected, and cannot test a closure
implication on an empty exceptional set.
