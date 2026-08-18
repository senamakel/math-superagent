# Backward decomposition: full Goldbach via exceptional set to zero

The conjecture is a statement about *every* even n.  The literature reaches
only "almost every" n — the exceptional set E(X) (even n ≤ X not a sum of two
primes) satisfies E(X) ≪ X^{1−δ} with best unconditional δ = 1/3 (Pintz 2004,
announced).  To prove the full conjecture, one must raise δ to 1 — i.e. show
E(X) = 0 for all X.

This skeleton decomposes that goal into lemmas that, if proved, would force
E(X) = 0.  The inference is a **density vs. structure** collision: one lemma
bounds E(X) from above (sparse), another forces it to be either empty or
positive-density (structural), and the third cuts off the finite beginning.

---

```skeleton
goal: Every even integer n > 2 is the sum of two primes (binary Goldbach).
implies: r(n) > 0 for all even n > 2.
  The proof runs by contradiction: let n_0 be the least even counterexample.
  - Lemma C (finite verification) gives n_0 > 4·10^18.
  - Lemma A (exceptional-set density bound) says E(X) ≪ X^{2/3} for X > X_0
    (with δ = 1/3), so the set of counterexamples is very sparse.
  - Lemma B (structural closure) says that if n_0 is a counterexample then
    E(X) ≫ X for all sufficiently large X — i.e., counterexamples have
    positive lower asymptotic density.
  - Lemma A and Lemma B are incompatible unless E(X) = 0 for all X.
  - Lemma C eliminates the remaining finite range.  Hence no counterexample
    exists.
status: sketched
rests-on: speculation that the exceptional set can be shown to be closed under
  a density-generating operation; this is the core open gap.
killed-by: (none yet — the skeleton is logically valid but rests on a conjecture
  about the structure of the exceptional set that is not known.  If Lemma B is
  false the skeleton collapses.)
```

---

## Gap: exceptional-set-density-bound

```gap
id: G-exceptional-density
lemma: There exists an absolute δ > 0 such that the number E(X) of even
  integers n ≤ X not representable as a sum of two primes satisfies
  E(X) ≪ X^{1−δ} for all sufficiently large X.
  The best known unconditional δ = 1/3 is sufficient for this skeleton.
status: discharged
discharged-by: Pintz (2004, announced); δ = 1/3.  Recorded in Kumchev–Tolev
  survey §1 eq. (1.6) and the Pintz (2018) preprint, lines 40–76 of the source.
  The δ = 1/3 exponent is attributed to Pintz's announcement in June 2004;
  the next best published value is δ = 0.086 (Li 2000) and the most recent
  published is δ = 0.28 (Zhao 2025, E(X) = O(X^{7/10})).  Discharged as
  sourced from the literature; not independently verified by this run.
next: (none — this is a known result, not an attackable gap.  To improve the
  skeleton one would sharpen δ, but the skeleton works with δ = 1/3.)
```

---

## Gap: exceptional-set-structural-closure

```gap
id: G-structural-closure
lemma: If n_0 is the least even integer not representable as a sum of two
  primes, then the set of counterexamples has positive lower asymptotic density.
  More precisely, E(X) ≫ X for all sufficiently large X.
  Equivalently: the exceptional set is either empty or has positive lower
  asymptotic density.
status: open
next: The first move is to find a concrete operation on counterexamples that
  generates new counterexamples with positive density.  Candidate approaches:
  (a) Show that if n is a counterexample then n·p is also a counterexample for
      all sufficiently large primes p (or for a positive-density set of p).
      This would follow if, for every prime q, the condition "n − q is prime"
      implies "np − q is prime" for some large class of p — which is a
      statement about the distribution of primes in arithmetic progressions.
  (b) Show that the set of counterexamples is closed under translation by a
      multiple of a fixed modulus m (from the Chinese Remainder Theorem and
      the structure of the singular series).  If n is a counterexample, then
      n + km is a counterexample for all k in a positive-density set of
      integers, giving E(X) ≫ X.
  (c) Show that the exceptional set is a "Fourier-quasiperiodic" set in the
      sense of the circle method: the major-arc contribution to r(n) is
      determined by the singular series S(n), and if n is a counterexample
      then the minor-arc contribution must cancel the major-arc contribution,
      which forces n to lie in a Bohr set of positive density.
  (d) Use the recent result of Grimmelt–Teräväinen (2025): n ≡ 4 (mod 6) are
      sums of two Chen primes apart from a power-saving exceptional set.
      If one could show that a Chen-prime representation n = p + q with
      p, q Chen primes forces p, q to be primes (i.e., break the parity
      barrier for this specific class), then n ≡ 4 (mod 6) would be covered.
      The structural closure gap would then be: show that the minimal
      counterexample must be ≡ 0 (mod 6) or ≡ 2 (mod 6), and repeat the
      argument for those classes.
  The most concrete first step: write a computational search for the minimal
  n_0 (up to some bound) that is not a sum of two Chen primes, to see if
  the Grimmelt–Teräväinen exceptional set is actually empty in the verified
  range.  If it is, the structural closure for n ≡ 4 (mod 6) at least would
  be a finite computation, not a theoretical lemma.
```

---

## Gap: finite-verification-bound

```gap
id: G-verification-bound
lemma: Every even integer n with 4 ≤ n ≤ 4·10^18 is the sum of two primes.
status: discharged
discharged-by: Oliveira e Silva, Herzog, and Pardi (2014).  Verified on the
  project page at sweet.ua.pt/tos/goldbach.html; all even n up to 4·10^18
  checked, and double-checked up to 4·10^17.  About 781.8 CPU-years of
  computation.  The method is a segmented sieve of Eratosthenes plus
  Goldbach-partition search.
next: (none — this is a known result, not an attackable gap.  Pushing the
  bound is a separate computational task, R-push-verification in the weakened
  ladder.)
```

---

## Working notes

### 1. Why the skeleton is not yet live

G-structural-closure is the bottleneck.  The skeleton's inference is sound
(if E(X) ≪ X^{2/3} and E(X) ≫ X then E(X) = 0), but the structural lemma
that would force E(X) ≫ X from a single counterexample is not known and
may be false.  The parity problem suggests that counterexamples, if they
exist, are not obviously closed under a density-generating operation: the
sieves that give the Chen-type results are sensitive to the arithmetic
structure of n, and the exceptional set for the Chen-prime result is
already known to be power-saving (not positive-density).

### 2. Alternative skeleton: the circle-method dichotomy

A more standard decomposition (not written here) would be:

- Major-arc asymptotic: for all sufficiently large even n, the major-arc
  contribution to the representation count is ≥ c·n/(log n)^2 (unconditional,
  standard).
- Minor-arc bound: for all sufficiently large even n, the minor-arc
  contribution is o(n/(log n)^2) (the central open problem).
- Finite verification: covers n up to 4·10^18.

This is the classical Hardy–Littlewood–Vinogradov approach.  The minor-arc
gap is the same obstruction as the exceptional-set bound, stated differently.
The exceptional-set skeleton is preferred here because it has a discharged
Lemma A (δ = 1/3) and the open gap is a structural question rather than a
purely analytic one, which may be more attackable by the workspace's methods.

### 3. The weakened-ladder context

The weakened ladder (research/weakened/goldbach-binary.md) records the
verification bound as settled (R-verified-range), the exceptional-set
density result as settled (R-density-delta), and the sharpened-exponent
problem as open (R-sharpen-delta).  The present skeleton adds the structural
gap (G-structural-closure) as the missing link between the density result
and the full conjecture.

The ladder's recommended next attack is R-push-verification (computational).
The present skeleton's recommended next attack is G-structural-closure
followed by (d) — using the Grimmelt–Teräväinen Chen-prime result to
narrow the class of potential counterexamples.
```