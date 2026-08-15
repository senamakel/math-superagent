# Direct invariant potential — decomposition of Gilbreath's conjecture

This skeleton takes the problem statement's first-named route literally: "find an
invariant of the absolute-difference operator forcing `A_k(1) ∈ {0,2}` directly,
without tracking blocks." It does **not** propose which invariant — that is the
inventor's job. It states the two properties an invariant must have, and the
inference that turns those two properties into the conjecture. The other five
backward files decompose the goal through block/regeneration and through the
right-diagonal ν₂ budget; this one decomposes it through a single scalar (or
well-ordered) potential on the halved row.

```skeleton
goal: Gilbreath's conjecture — for the iterated absolute-difference triangle of the
      primes, A_k(0) = 1 for every k ≥ 1.
implies: |
  Step 0 (halving, DISCHARGED): every entry A_k(j), j ≥ 1, k ≥ 1 is even (parity
  wave), so define the halved row H_k(j) = A_k(j+1)/2 for j ≥ 0. Then
  H_{k+1}(j) = |A_k(j+1) − A_k(j+2)|/2 = |H_k(j) − H_k(j+1)|, so H is itself a
  Gilbreath triangle, on the halved prime gaps H_1(j) = gap_{j+1}/2. Moreover
  A_k(1) ∈ {0,2} ⟺ H_{k-1}(0) ∈ {0,1}; since A_{k+1}(0) = |1 − A_k(1)| is 1 iff
  A_k(1) ∈ {0,2}, the conjecture is equivalent to

      H_k(0) ∈ {0,1}  for every k ≥ 1.

  Step 1 (DI-monotone-potential): take Φ with Φ(H') ≤ Φ(H) for H' the image row
  under H ↦ (|H(j) − H(j+1)|)_j.

  Step 2 (DI-initial-minimum-clean): Φ(H_1) is the minimum of Φ over all rows, and
  every row H with Φ(H) = Φ(H_1) has H(0) ∈ {0,1}.

  Inference: suppose, toward a contradiction, that H_k(0) ∉ {0,1} for some k ≥ 1,
  and take the least such k. For every j < k we have H_j(0) ∈ {0,1}, but that is
  not even needed: monotonicity (Step 1) gives Φ(H_k) ≤ Φ(H_1) = min, hence
  Φ(H_k) = Φ(H_1), and Step 2 forces H_k(0) ∈ {0,1} — contradiction. Therefore
  H_k(0) ∈ {0,1} for all k ≥ 1, which by Step 0 is Gilbreath's conjecture.
status: sketched
rests-on: gilbreath-reduces-to-second-in-02, cht-normalized-gap-definition
```

```gap
id: DI-halving-triangle
lemma: The even part of every row halves to an exact absolute-difference triangle:
  H_k(j) = A_k(j+1)/2 is integer for all k ≥ 1, j ≥ 0, and H_{k+1}(j) =
  |H_k(j) − H_k(j+1)|, with H_1(j) = (p_{j+2} − p_{j+1})/2. The conjecture is
  equivalent to H_k(0) ∈ {0,1} for all k ≥ 1.
status: discharged
discharged-by: cht-normalized-gap-definition (the normalized-gap array a_n = H_1(n−1) − 1
  has left diagonal eventually {0,1}-valued iff GC; the halving identity itself is the
  parity-wave argument of gilbreath-reduces-to-second-in-02, research/notes/reduction.md)
next: none — restating this as open re-opens a closed fact.
```

```gap
id: DI-monotone-potential
lemma: There exists a function Φ from finite-support rows of nonnegative integers to a
  well-founded (or real, bounded-below) ordered set such that Φ(H') ≤ Φ(H), where
  H' = (|H(j) − H(j+1)|)_j is the halved-operator image of H. Strictness
  (Φ(H') < Φ(H) whenever H(0) ∉ {0,1}) is a useful strengthening for discovery but is
  not required by the inference above — weak monotonicity suffices.
status: open
next: |
  Candidate discovery, then proof. (a) tool_builder + sat_solver: parametrise a family
  of potentials over the halved row — weighted max a·max + b·(left-window sum),
  factored-max à la Chamberland, weighted run counts with the (a,a,c,c)-borderline
  handling (the run-count raw form is already REFUTED, runcount-lemma-refuted), max−min,
  and left-window ℓ1 against a target vector — and search, in parallel with
  code/lib/parallel.py, for one with Φ(H') ≤ Φ(H) on ALL halved rows with entries in
  {0..M}, length ≤ L (M,L small, e.g. M≤6, L≤10; this is a bounded universal, not a
  search of the answer space). A CP-SAT/SMT witness for a counterexample refutes a
  candidate; UNSAT over the finite class certifies it there. (b) Any survivor is then
  handed to theorem_prover/smt_solver: prove Φ(|h_j − h_{j+1}|) ≤ Φ(h) for ALL h as a
  universal statement (SMT: refute the negation). (c) Falsification oracle: every
  candidate must hold on the real halved rows in code/out/witnesses.json, especially
  rows where the leading {0,2} block is short.
```

```gap
id: DI-initial-minimum-clean
lemma: For the Φ from DI-monotone-potential: Φ(H_1) equals the global minimum of Φ, and
  every row H with Φ(H) = Φ(H_1) has H(0) ∈ {0,1}. (Equivalently the sublevel set
  {H : Φ(H) ≤ Φ(H_1)} lies inside {H : H(0) ∈ {0,1}}.)
status: open
next: |
  Two roles. tool_builder: once Φ is pinned, compute Φ(H_1) and Φ on every real halved
  row in code/out/witnesses.json (and the depth-1000 block data if present); confirm
  Φ(H_1) is the minimum attained and that every row attaining it has H(0) ∈ {0,1}. This
  is the falsification oracle, not the proof. theorem_prover/smt_solver: prove the
  combinatorial statement {H : Φ(H) ≤ Φ(H_1)} ⊆ {H(0) ∈ {0,1}} — encode its negation
  (an H with Φ(H) ≤ Φ(H_1) and H(0) ≥ 2) as a first-order/SMT query over a finite bound;
  UNSAT is a proof. Note this half of the reduction is where the initial halved prime
  gaps H_1(j) = gap_{j+1}/2 enter: the clean-sublevel condition must be verified against
  that specific initial row, not against an arbitrary row.
```
