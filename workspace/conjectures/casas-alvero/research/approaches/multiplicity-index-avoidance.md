# multiplicity-index-avoidance

```approach
idea: Attack through the multiplicity structure, not the coefficients. Let f have distinct
roots beta_1..beta_r with multiplicities m_1..m_r, sum m_j = n, and let M = max m_j. The
hypothesis is *mainly a statement about M*. Because f^(i)(r) = i! * (i-th Taylor coeff of f
at r), a root of multiplicity m witnesses index i automatically iff i < m, and NEVER
witnesses i = m; indices i > m require a genuine vanishing of a higher Taylor coefficient
(a root-difference coincidence). Hence all indices i >= M are "hard": for each such i there
must be a shared root beta with m(beta) <= i, i != m(beta), and H_i(prod_{k!=beta}(x-beta_k))
= 0 as a genuine coincidence. There are n - M hard indices; for a counterexample M <= n-1 so
at least one. The claim to test: the hard-index conditions are n-M independent algebraic
conditions on ~r root positions, and for every multiplicity partition with r >= 5 distinct
roots (Laterveer-Ounaiës) and the "index-avoidance" structure, they overdetermine and force
M = n (pure power) -- unless a whole block of middle Hasse derivatives vanishes, which is
exactly what happens in characteristic p.

mechanism: The mechanism is a count, and it is where char 0 and char p bifurcate. Let m_j
be the multiplicities. Define the "free index set" F = {i < M}: these are witnessed
automatically by the max-multiplicity root. Every i in [M, n-1] is hard. A hard index i is
witnessed by some root beta_j with m_j <= i and i != m_j through the genuine root-difference
condition H_i(f)(beta_j) = e_{n-i}(beta_j - beta_*) = 0 (the owned identity, char-free). Each
such genuine coincidence is one independent algebraic equation in the root configuration.
Vertically summing over the hard block the number of independent coincidences must be
absorbed by the number of free parameters (r-1 root positions after translation, plus the
choice of which beta_j witnesses each i). If for every partition with r >= 5 that count
exceeds the free dimension, CA follows for char 0. The named theorem behind "hard index needs
a genuine coincidence" is just the Hasse-Taylor expansion; the named theorem behind the
collapse is Newton's identities turning the coincidences into power-sum constraints. In char
p the repeated binomial vanishing H_i = 0 for the Lucas block (p | [k choose i] for p <= ...)
declares many middle indices FREE automatically, shrinking the hard block and killing the
overdetermination -- this is the named, located char-p break (same Lucas vacuity as
root-difference-coloring's), and the witness x^{p+1}-x^p has M = p, n-M = 1 hard index which
is genuinely satisfiable in char 0's analogue, showing where the forcing dies.

precedent: laterveer-ounaies-2012, (arXiv:1204.0450:, CA-polynomial, has, ≥5, distinct, roots,
N≥6;, CA, holds, if, ≤4, distinct, roots;, root, of, multiplicity, ≥N−2, forces, pure, power,
so, a, counterexample, has, M, ≤, N−3);, polstra-2012, (every, root, a, vertex, of, C_f, ◯,
pure, power, convex-hull);, five-roots-rung, (code/roots5/multipattern.py:, the, run's, own,
already-executed, version, of, this, line:, the, multiplicity+centroid, mechanism, rules, out,
all, 19, five-distinct-root, partitions, for, n=5..10, at, i=m_1, and, i=n−2);,
root-difference-identity, (H_i(f)(β_j), =, e_{n−i}(β_j−β_*), the, owned, char-free, identity,
the, hard-index, coincidences, reduce, to).

status: refuted

killed-by: The dimension count this line rests on is neither a theorem nor uniformly
binding. (1) The "r−1 free root parameters" undercounts the true freedom: the hypothesis
lives in the (n−1)-dimensional coefficient space (a_1..a_{n−1}), minus the n−1 resultant
constraints R_i=0, at most one dimension removed each — so the configuration space of
shared-root patterns has dimension n−1, not r−1, and there is no shortage of parameters for
the n−M hard coincidences to live in. A pure count on root positions cannot overdetermine
roots that also live in a coefficient space of dimension n−1. (2) The count is shape-dependent
in the wrong direction: whether n−M > r−1 holds at all depends on the partition (e.g. n=9,
(2,2,2,2,1): n−M=7 > 4 bites; but n=20, (11,1,1,1,1,1,1,1,1): n−M=9 vs r−1=8 marginal, and
a max-multiplicity root of size M witnesses ALL hard indices i in [M,n−1] by the same
β_j, so the n−M conditions are far from independent — one root can satisfy many). (3) It is
the run's own executed negative control: code/roots5/multipattern.py confirms the
multiplicity+centroid mechanism rules out all 19 five-root partitions for n=5..10, yet
nobody concludes CA from that count, because the hard-block condition (i ≥ M, a genuine
root-difference coincidence, exactly the "uncovered i in [m_1, n−2]" the script names as the
open content) is precisely what the count cannot force without a real root-position theorem
this line does not supply. Refuted as an overdetermination argument; the one honest product —
the census of multiplicity-compatible partitions — is already delivered by the run itself.
This is the bernstein-sato refutation from the other side: multiplicity structure alone does
not force CA because the hypothesis constrains shared roots, not multiplicities.

status: refuted

first-step: (tool_builder, exact sympy, oracle-guarded) (1) PROVE and verify the corrected
index rule -- f^(i)(r) = 0 with f(r) = 0 holds automatically iff i < mult(r), impossible iff
i = mult(r), genuine coincidence iff i > mult(r) -- on the guard set ((x-1)^n passes with
M=n, generic f fails, char-p witness x^{p+1}-x^p over F_p has M=p and satisfies each hard
index). (2) Enumerate all integer partitions m of n with r >= 5 parts, compute M and the
hard block [M, n-1], and count, for each partition, the minimal number of independent
root-difference coincidences required to cover the hard block, against the r-1 free root
parameters. Report which partitions survive the count (expect: only r with a part = n).
(3) For each survivor compute a symbolic witness if one exists via the oracle, recording the
char-0/p difference in the count. State exactly what a bigger run would settle: whether ANY
partition with M<n survives the dimension count in char 0.
```

## Why this is not a re-proposal

- `berstein-sato-bfunction` was refuted because "b_f records the multiplicity multiset, an
  invariant the hypothesis does not constrain." This line is the opposite claim: the
  hypothesis DOES constrain multiplicities, through the index rule (i < m automatic, i = m
  impossible, i > m genuine). That rule is the new object, and it is provable, not a
  conjecture.
- `coincident-root-locus-intersection` was refuted because R_i does not vanish on strata
  with small multiplicity parts. This line uses the corrected per-index accounting (a root of
  multiplicity m only auto-covers i < m), which is precisely the fix that refutation demands.
- `milnor-local`, `moment-hankel`, `root-difference-coloring` all work on the root *positions*
  or the resultant ideal. This works on the *multiplicity partition* first, then uses the
  root-difference identity only for the hard block. Different primary axis.

## Char-p break (the admissibility test)

Located and named: the overdetermination argument requires that a large block of Hasse
derivatives impose genuine coincidences. In char p the middle block vanishes (Lucas: for
p <= k, [k choose i] = 0 mod p on the block), so those indices become automatically free, the
hard block shrinks to size ~1, the dimension count stops biting, and M<n counterexamples
survive. The witness x^{p+1}-x^p saturates this: M=p, one hard index, satisfied by the
mult-1 root.

## Caveat

The reformulation itself is trivial (it is the definition). The *claim* -- "for every
partition with r>=5 and M<n the hard-index count overdetermines" -- is the open content and
may be false; step (3) is where the run hunts a surviving partition. The honest partial
result this line can deliver even if the claim dies is the exact count of which multiplicity
partitions are compatible with the hypothesis, which is a new recorded fact.
