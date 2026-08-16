# Extremal splitting: the stability reduction for ES(n) ≤ 2^{n−2}+1

```skeleton
goal: For every n ≥ 3, ES(n) ≤ 2^{n-2}+1 — i.e. every set of 2^{n-2}+1 points
      in general position in the plane contains n points in convex position.
      (The matching lower bound ES(n) ≥ 2^{n-2}+1 is settled; only the upper
      bound is the open claim.)
implies: Let f(n) be the maximum size of a set in general position with no
      convex n-gon; then ES(n) = f(n)+1, so the goal is equivalent to
      f(n) ≤ 2^{n-2} for all n ≥ 3. Induction on n.

      Base (n = 3): any three points in general position are the vertices of a
      convex triangle, so f(3) = 2 = 2^{1}.

      Step (n ≥ 4): let X be an extremal n-avoiding set, |X| = f(n). By the
      splitting lemma (G-split) there is a line ℓ meeting no point of X such
      that the two open half-planes' parts X⁺, X⁻ each contain no convex
      (n-1)-gon. Then |X| = |X⁺| + |X⁻| ≤ 2·f(n-1) ≤ 2·2^{n-3} = 2^{n-2}, by
      the induction hypothesis. Hence f(n) ≤ 2^{n-2}. Together with the settled
      lower bound f(n) ≥ 2^{n-2}, we get f(n) = 2^{n-2} and so
      ES(n) = 2^{n-2}+1.

      The cup–cap characterization (G-cupcap) is the dictionary used to attack
      G-split: it rewrites "X⁺ (resp. X⁻) contains no convex (n-1)-gon" as the
      absence, inside that half-plane, of a shared-endpoint k-cup + (n+1-k)-cap
      for any k. It is not needed for the induction's arithmetic, only for
      turning G-split into a cups-and-caps statement that an encoding or a
      prover can handle. G-split-consistent certifies the reduction is not
      refuted on arrival by the extremal template.
status: live
rests-on: f(3) = 2 (elementary: any three points in general position form a
      convex triangle); the Erdős–Szekeres 1960 lower bound
      ES(n) ≥ 2^{n-2}+1 and the base values ES(3..6) = 3, 5, 9, 17, all
      asserted in problem.md as leads to verify. The induction rests only on
      f(3) = 2; the lower bound upgrades the inequality to equality, and the
      base values fix the computational checks. None of these is yet recorded
      in the claims ledger (CLAIMS.md is empty) — the scholar must record them
      before they are treated as established.
```

```gap
id: G-cupcap
lemma: (Cup–cap characterization, Erdős–Szekeres 1935.) After a rotation
      making all x-coordinates distinct: a set X in general position contains
      n points in convex position if and only if for some k ∈ {2,…,n} it
      contains a k-cup C and an (n+2−k)-cap D whose leftmost and rightmost
      points coincide (equivalently, C ∪ D is exactly n points in convex
      position). A k-cup is k points in increasing x-order with strictly
      increasing consecutive slopes; a cap has strictly decreasing slopes.
status: open
next: Formalize the statement in Lean (convex position and cup/cap over an
      affine point set, general position, the quantifier order), then verify
      both directions against the exact oracle on all small order types —
      all order types through 8 points and random larger sets — comparing
      "contains n points in convex position" with "contains a shared-endpoint
      k-cup + (n+2−k)-cap for some k". The lemma is classical; the run should
      record it as a claim, not re-derive it from scratch.
```

```gap
id: G-split
lemma: (Extremal splitting / stability.) For every n ≥ 4, every extremal
      n-avoiding set X (|X| = f(n), no convex n-gon, general position) admits
      a line ℓ containing no point of X such that each of the two open
      half-planes' parts of X contains no convex (n−1)-gon. The stronger form
      believed true — and what the literature calls stability/uniqueness — is
      that such X is, up to order-type equivalence, the Erdős–Szekeres
      construction (the "compressed" union of n−1 clusters of sizes
      binom(n−2,i)); that form implies G-split. If G-split fails for some
      extremal set, this skeleton is broken (the conjecture itself would not
      yet be refuted).
status: open
next: SAT/CP-SAT counterexample search, only after the encoder reproduces
      ES(5) = 9 and ideally the Peters–Szekeres ES(6) = 17 negative on 16
      points. Encode over orientation variables with the signature and
      transitivity axioms: does there exist an order type on f(n) points with
      no convex n-gon and no separating line whose two sides are both
      (n−1)-avoiding? For n = 6 (N = 16) an exhaustive "no" certifies G-split
      at n = 6; for n = 7 (N = 32) the order-type space is astronomically
      large, so target the refutation search — a witness kills G-split. Use
      G-cupcap to phrase "no convex (n−1)-gon in a half-plane" as a
      cups-and-caps condition inside the encoding. State the search space,
      symmetry reduction, and isomorph rejection for every run.
```

```gap
id: G-split-consistent
lemma: (Consistency on the extremal template.) The splitting lemma is not
      refuted by the known extremal construction: for n = 5, 6, 7 the
      Erdős–Szekeres 1960 construction of 2^{n-2} points, realized in exact
      rational coordinates, admits a line separating it into two (n−1)-avoiding
      halves (2^{n-3} points each) — i.e. its recursive decomposition
      X_n = X_{n-1} ∪ X_{n-1}* witnesses G-split.
status: open
next: `es_construct` is now the verified construction (largestConvex = n−1 at
      n=4,5,6; no convex 7-gon at n=7). The even/odd block halves are each
      (n−1)-avoiding and of size 2^{n-3}, but in this realization they are NOT
      strictly line-separable (gsplit_line.py — a dead guess, not an
      obstruction). The genuine question is whether ANY line (through a point
      pair, perturbed off it) splits the set into two (n−1)-avoiding halves:
      exhaustive test at n=5,6,7, task `gsplit-exhaustive-line-test`
      (starter `code/out/gsplit_exhaustive.py`; verify its bipartition
      enumeration before trusting it). An empty result is a checked negative
      about THIS realization at these n, not about all extremal sets.
```
