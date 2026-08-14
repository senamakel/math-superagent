# Skeleton: superlogarithmic lower bound via the bipartition's threshold shadow

A decomposition of the primary target `f(n) = ω(log n)` into lemmas, each
attackable on its own, with the inference that combines them stated explicitly.
This is not a route to a new method — it is the goal broken into propositions.

The change of ground: `Q_n` is bipartite with parts `E` (even weight) and `O`
(odd weight), both of size `2^{n-1}`, and *every* edge crosses `E–O`. The
max-degree condition `D(S) ≤ d` therefore becomes a pair of cross-degree bounds,
and the `b`-side bound is equivalent to `B ⊆ O_{≤d}(A)`, a *threshold shadow*
condition. Averaging a total edge count cannot see a threshold; a threshold
quantity is a maximum by construction, which is exactly the shape the problem
statement says the lower bound must come from.

Note on scope: a concurrent skeleton (`spectral-interlacing-sqrt-lower-bound`,
a signed-adjacency-matrix + Cauchy-interlacing argument) targets the strictly
stronger `f(n) ≥ √n`. That is the argument of Huang (2019), and if its two
standard lemmas (interlacing, and `λ_max(B) ≤ Δ(H)` for a signed principal
submatrix) are verified, it discharges the *entire* goal and subsumes this file.
This skeleton is kept because it is a genuinely different, combinatorial second
viewpoint on the same quantity — valuable for independent verification, not
because it out-runs the spectral route.

```skeleton
goal: f(n) = ω(log n) — for every constant C there is N with f(n) ≥ C·log₂ n for all n ≥ N,
      where f(n) = min { D(S) : S ⊆ V(Q_n), |S| = 2^{n-1}+1 }.

implies: |
  Let E, O be the even- and odd-weight classes of Q_n; both have size 2^{n-1}
  and every edge of Q_n joins E to O. For S with |S| = 2^{n-1}+1 write
  A = S∩E, B = S∩O, a = |A|, b = |B|. Then a + b = 2^{n-1}+1, so
  b = 2^{n-1} - a + 1.

  If D(S) ≤ d then every x ∈ B has |N(x)∩A| ≤ d, i.e.
      B ⊆ O_{≤d}(A) := { x ∈ O : |N(x)∩A| ≤ d },
  hence necessarily  |O_{≤d}(A)| ≥ 2^{n-1} - a + 1.

  Contrapositive (G1): if, for some d = d₀(n), EVERY A ⊆ E satisfies
      |O_{≤d₀(n)}(A)| ≤ 2^{n-1} - |A|,
  then no S of size 2^{n-1}+1 has D(S) ≤ d₀(n), so f(n) ≥ d₀(n)+1.
  (The A-side degree bound is never used: it is enough that the necessary
  condition fails.)

  To get the universal bound on |O_{≤d}(A)|, invoke the threshold-shadow
  extremal lemma (G2): the quantity |O_{≤d}(A)| over A ⊆ E with |A| = a is
  bounded above by its value at an explicit extremal family, giving a
  computable bound U_d(a). Then (G3) establish
      U_{d₀(n)}(a) ≤ 2^{n-1} - a   for all 0 ≤ a ≤ 2^{n-1}
  with d₀(n) = ω(log n).

  Combination: G1 says the universal inequality suffices for f(n) ≥ d₀(n)+1;
  G2 supplies U_d(a) valid for every A; G3 verifies U ≤ 2^{n-1}-a at a
  superlogarithmic d₀(n). Hence f(n) ≥ d₀(n)+1 = ω(log n).

  Sanity check (hand, n=3): the decomposition is consistent with f(3) = 2.
  At d=1 the universal inequality |O_{≤1}(A)| ≤ 4 - |A| holds for
  a ∈ {0,2,3,4} and fails only at a=1: A={000} has O_{≤1}(A)=O (each odd
  vertex has ≤1 neighbour in {000}), of size 4 > 3. So the contrapositive
  correctly declines to prove f(3) ≥ 2, and indeed D(S)=1 is impossible while
  S = {000,001,011,111,100} has size 5 and D(S)=2.

status: sketched
rests-on: none — research/CLAIMS.md is empty. The even/odd bijection facts used in G1
          are trivial and are recorded as G1's own discharge target, not assumed.
```

```gap
id: G-bip-reduce
lemma: |
  For S ⊆ V(Q_n) with A = S∩E, B = S∩O: D(S) = max( max_{b∈B} |N(b)∩A|,
  max_{a∈A} |N(a)∩B| ). Consequently, for d = d₀(n), if
  |{x ∈ O : |N(x)∩A| ≤ d₀(n)}| ≤ 2^{n-1} - |A| holds for every A ⊆ E, then
  f(n) ≥ d₀(n)+1.
status: open
next: |
  theorem_prover/lean_prover: formalise the bijection and the one-line
  contrapositive (finite and elementary, no sorry left). tool_builder: brute
  force n ≤ 4 by minimising D(S) over all A,B with a+b = 2^{n-1}+1 and confirm
  it equals f_exact(n) — an independent check of the reduction.
```

```gap
id: G-threshold-shadow
lemma: |
  For each n and 0 ≤ d ≤ n, the function A ↦ |O_{≤d}(A)| = |{x ∈ O : |N(x)∩A| ≤ d}|,
  over A ⊆ E with |A| = a, is maximised by a Hamming ball in E (equivalently an
  initial segment of the simplicial or colex order). If not, exhibit any explicit
  order on E whose initial segments majorise |O_{≤d}(A)| for every A.
status: open
next: |
  sat_solver/tool_builder: for n ≤ 6 and each pair (d, a), find argmax of
  |O_{≤d}(A)| by ILP and compare against the Hamming-ball value. The first
  (n,d,a) where some A beats every ball refutes the lemma and supplies the
  seed for the true extremal family. theorem_prover: attempt a
  compression/shifting proof that |O_{≤d}(A)| is monotone under the standard
  compressions used for Harper/Kruskal–Katona.
```

```gap
id: G-threshold-analysis
lemma: |
  Let U_d(a) be the extremal upper bound from G2 (the ball value suffices if G2
  holds). There is d₀(n) = ω(log n) such that U_{d₀(n)}(a) ≤ 2^{n-1} - a for
  all 0 ≤ a ≤ 2^{n-1}.
status: open
next: |
  symbolic_math: derive a closed form for the ball value U_d(a) and solve for
  d*(n) = min { d : ∃a, U_d(a) ≥ 2^{n-1} - a + 1 }, then find its growth.
  If d*(n) = Θ(log n), this sub-lemma is refuted as stated and the obstruction
  is located exactly: the ball extremal family is too weak and the true family
  must come from G2's counterexample hunt. Record that as killed-by on this
  gap, not on the skeleton.
```

## Notes

- The primary chain is G1 → G2 → G3, in that order of dependence.
- The reduction G1 is deliberately one-sided: the proof that no valid S exists
  uses only the necessary condition `B ⊆ O_{≤d}(A)`. This is correct for a
  lower bound and keeps the inference minimal.
- The spectral route (Huang's argument) is deliberately **not** re-stated as a
  gap here: it is already decomposed in the concurrent
  `spectral-interlacing-sqrt-lower-bound` skeleton, and duplicating it would
  put two copies of the same lemma in the ledger.
- A hand computation through this decomposition gives f(3) = 2; it is a check
  of the reduction's sanity, not a program output.
