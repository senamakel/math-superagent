```approach
idea: Coding-theory / Delsarte linear-programming bound on OR-closed codes. View a union-closed family F as a binary code: a subset of {0,1}^n of size m closed under coordinatewise OR (union = OR over bits). Abundance of element x is the fraction of codewords with bit x = 1 — a marginal/weight profile. The named object is the Hamming association scheme and Delsarte's LP bound, which packages every valid inequality a nonnegative distance-distribution (pseudocodeword) must satisfy (Krawtchouk/MacWilliams PSD moment matrices). A counterexample to UC is exactly a code with every coordinate marginal < 1/2; the question is whether the Delsarte-reachable moment region, cut by the OR-closure constraint, has any point with all marginals < 1/2.

mechanism: Delsarte's theorem makes the distance distribution of any code of size m a feasible point of an explicit LP whose moments are the (normalised) pair counts at each Hamming distance, constrained by Krawtchouk PSD inequalities. The weight-profile marginals are linear in the moment variables, so "all marginals < 1/2" is a linear slice of the feasible pseudocode polytope. Union-closure is not linear but is a finite algebraic (triple) condition on the OR-closed code. The higher Krawtchouk moments carry the pair/co-occurrence information that the first-moment entropy line provably cannot see (cap (3−√5)/2 ≈ 0.382), so this is a genuine second/higher-moment coding-theoretic strengthening if the OR-closure constraint can be made finite-and-positive.

status: adopted

killed-by: (not refuted — adopted; recorded as live)


## Decision (inventor, converging pass)

Research grounded this line as genuinely novel and worth exactly one probe. The
literature confirms: (a) Delsarte LP for constrained/monotone codes is real and
active (Rameshwar–Kashyap arXiv:2301.05098, IEEE-TIT dual programs 2024,
Coregliano–Jeronimo–Jones ITCS 2022), and (b) NO source applies it to the
OR-closed abundance (marginal ≥ 1/2) question — Yu's own OR-channel bound is
first-moment only, capped at ≈0.38234. The first-moment entropy/coupling route
is exhausted (capped ≈0.382 < 1/2), so a second/higher-moment coding-theoretic
bound is the only structural escalation left that is not already closed.

## Sharpened first-step (a tool_builder starts today)

The hinge is a MEASURED gap, not a vague worry. Compute, for n ≤ 5 (n ≤ 6 if
cheap), using the canonical oracle, three nested regions and the question of
whether each has a point with ALL coordinate marginals < 1/2:

- R_true = convex hull of the moment/marginal vectors of actual OR-closed codes
  (families F on [n], ∅ ∈ F for rooted form, closure under union).
- R_cont = Delsarte/pseudocode region over the *containment-constrained* codes
  C ⊆ A (the Rameshwar–Kashyap setting): distance distribution B_k constrained
  to come from a code contained in a given monotone A.
- R_del = unconstrained Delsarte-feasible quasicode region (MacWilliams/Krawtchouk
  PSD moment inequalities only).

Expected outcomes, stated before running:
- R_true has empty all-<1/2 slice (it must, if UC holds on [n] for these n) —
  the guard that the oracle measures the right thing.
- The interesting comparison is R_cont and R_del: if R_del's slice is NONEMPTY
  while R_cont's (or R_true's) is empty, the Delsarte relaxation over-relaxes
  exactly by dropping OR-closure's positive description, and the gap is
  precisely the missing finite-positive-moment encoding — the theorem a real
  higher-moment proof would have to construct.
- If even R_true is nonempty through n=5, the oracle is wrong (UC is verified
  to n≈11 by Bosnjak–Markovic), so that branch is a bug in my checker, not a
  result.

The deliverable that ends the probe: for the largest n the exact hull
computation reaches, report whether each of the three slices is empty or
nonempty, computed exactly (never floating point for the verdict). Empty-hull
slice = computational evidence for UC from a non-entropy route (new support);
nonempty-Delsarte-slice with empty-hull = a barrier theorem for the Delsarte
relaxation and the exact locus of the missing OR-closure description. Do NOT
scale past n=6 — the hull is 2^n-dimensional and the answer at n≤6 is what
decides whether a real moment proof is worth pursuing at all.

precedent: The machinery is real, active, and directly applicable to constrained/monotone codes, and no source applies it to the union-closed *abundance* question — so the application is genuinely novel, with the hinge named honestly.

- V. Arvind Rameshwar, Navin Kashyap, "Estimating the Sizes of Binary Error-Correcting Constrained Codes" (arXiv:2301.05098, 2023): explicitly **extends Delsarte's LP to constrained code families C ⊆ A**, giving Del(n,d;A) that upper-bounds |C| for codes with C ⊆ A and min distance ≥ d; reduces to the classical Del(n,d) when A = {0,1}^n; shows monotone (order/OR-closed) constraints are among the constrained systems handled. This is exactly the "Delsarte over an OR-closed/monotone subfamily" machinery the candidate calls for.
- "New Solutions to Delsarte's Dual Linear Programs" (IEEE Trans. Inf. Theory, 2024, arXiv version by Loyfer–Linial 2211.12977 / Sberlo–Shpilka): universal Delsarte dual bounds with explicit application to monotone (upward-closed, OR-closed) codes and fractional/average-weight constraints — the marginal-profile type of constraint this candidate needs.
- Coregliano–Jeronimo–Jones, "A Complete Linear Programming Hierarchy for Linear Codes" (ITCS 2022, doi:10.4230/lipics.itcs.2022.51): the higher-order (ℓ-point) Krawtchouk/moment hierarchy (KrawtchoukLP(n,d,ℓ)) that packages the pair and higher co-occurrence information, corroborating that Delsarte moments beyond level 1 encode pair structure.
- Yu, "Dimension-Free Bounds for the Union-Closed Sets Conjecture" (Entropy 25(5):767, 2023, doi:10.3390/e25050767): frames UCSC itself as an OR-channel/pseudocode problem, but its bound is first-moment (marginal) only, capped at ≈0.38234 — confirming the gap (higher moments unused) that this line would attack.
- No source in or out of this library applies Delsarte/association-scheme moments to the OR-closed *abundance (marginal ≥ 1/2)* question. The closest is the entropy/coupling line (AHS, Sawin, Yu, Cambie, Liu — all first-moment), which is why this is novel.

The hinge — THE OPEN QUESTION A CHECK MUST FIRST BUILD OR REFUTE — is exactly what the inventor flagged, and the literature confirms it is genuinely open, not silently wrong: whether OR-closure of a code is expressible as finitely many POSITIVE (moment-inequality / PSD) constraints within the Delsarte polytope. The Rameshwar–Kashyap and dual-program papers handle monotone constraints but as *code-containment* restrictions (C ⊆ A, and distance-constrained size bounds), not as a finite positive-moment description of the (already optimistic) pseudocode polytope. If OR-closure cannot be written as positive moment inequalities, the "finite algebraic rows" step fails and the polytope over-relaxes hopelessly. Concretely: a union-closed code's moment region is the image of an exponential set of codewords, and its convex hull may be very large; whether the "all marginals < 1/2" slice of that hull is empty is a concrete, checkable small-n question (n ≤ 5/6), and that empty-slice claim is the honest target — it is exactly what the first-step below measures.

first-step: With the canonical oracle, for n ≤ 5 enumerate the OR-closed codes (union-closed families), compute the distance distribution B_k and the Krawtchouk moment matrix, and verify Delsarte's PSD/MacWilliams inequalities hold identically (guards on 2^[n]: B_k MacWilliams-feasible, marginals exactly 1/2). Then compute the actual convex hull of the moment/marginal representations and decide — by exact LP over the hull, and separately over the Delsarte-feasible region — whether the "all marginals < 1/2" slice is empty. THREE controls apply: 2^[n] gives marginals exactly 1/2; a non-union-closed family shows the OR-closure row failing; finiteness enters via m ≤ 2^n. The decisive deliverable, stated before the run: either (a) an exact LP shows the hull's all-<1/2 slice is empty through n=5 (computational evidence for the conjecture from a second-moment route, and a checkable target for a real moment proof at higher n), or (b) a nonempty slice is exhibited — in which case Delsarte's *relaxation* (unconstrained quasicode polytope) provably cannot prove UC, which is itself a barrier theorem, and the exact reason (the over-relaxation) is the finding. The hinge is measured by comparing (true hull empty?) vs (Delsarte-feasible region empty?): if the hull slice is empty but the Delsarte slice is not, the gap is precisely the missing finite positive description of OR-closure, and THAT is what a real theorem would have to construct.

Note: genuine novelty does not yet mean genuine progress. The literature grounds the machinery (Delsarte-for-constrained-codes is real and active) and confirms the first-moment gap (Yu/entropy cap at ≈0.382), so the line is worth exactly one computational probe — the small-n empty-slice question — which is cheap, exact, and either produces the strongest available computational evidence for UC from a non-entropy route or refutes the Delsarte relaxation as a route. Do not scale it past small n (the hull is 2^n-dimensional) without that probe returning (a).
```
