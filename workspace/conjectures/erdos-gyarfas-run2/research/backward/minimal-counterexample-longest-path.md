# Skeleton: minimal counterexample + longest path

Working backward from the Erdős–Gyárfás conjecture: what lemmas, if somebody
had them, would give it, and the inference that combines them. The route is the
standard one for sparse-prescribed-cycle problems — take a vertex-minimal
counterexample, force it to be 2-connected, then attack the 2-connected case
with a longest path, whose endpoints funnel all their neighbours onto one path
and thus produce a small family of cycle lengths.

```skeleton
goal: Every finite simple graph G with δ(G) ≥ 3 contains a cycle of length 2^k for some k ≥ 2.
implies: |
  By contraposition. Suppose G is a counterexample — δ(G) ≥ 3, no cycle of
  length 2^k — and take one with the fewest vertices.

  (1) G is connected: a disconnected δ(G) ≥ 3 graph has a component of minimum
      degree ≥ 3, which would be a smaller counterexample. [elementary]

  (2) By G-2conn, G is 2-connected. Let P = v_0 v_1 … v_m be a longest path.
      Since P is longest, every neighbour of v_0 lies on P, so
      N(v_0) = {v_{i_1}, …, v_{i_d}} with 1 ≤ i_1 < … < i_d ≤ m and
      d = deg(v_0) ≥ 3. For any a < b the closed walk
      v_0 v_{i_a} v_{i_a+1} … v_{i_b} v_0 is a cycle of length (i_b − i_a) + 2,
      so G contains cycles of every length in {i_b − i_a + 2 : a < b}.
      [elementary; formalise in Lean as the first deliverable]

  (3) G is 2-connected with δ ≥ 3, so G-heart gives a cycle of length 2^k in G,
      contradicting the choice of G.

  Induction variable: the number of vertices (minimal counterexample).
  Quantifier discipline: G-2conn supplies exactly the hypothesis
  ("G is 2-connected") that G-heart consumes; G-heart supplies the
  contradiction that closes the minimality argument. The two lemmas suffice.
status: live
rests-on: none — the claims ledger is empty this cycle; the two "elementary" facts above are stated inline and are themselves the first Lean-formalisation targets.
killed-by: ""
```

```gap
id: G-2conn
lemma: A vertex-minimal counterexample (δ ≥ 3, no cycle of length 2^k) is 2-connected.
status: open
discharged-by: ""
thread: ""
next: |
  Two independent first moves, one to try to prove it and one to try to break it.
  (a) Lean: formalise the end-block argument — if G has a cut vertex, an end-block
      B (2-connected) with articulation c has every vertex of B∖{c} of degree ≥ 3
      in B, and deg_B(c) ≤ 2 (else B is itself a smaller counterexample); since B
      is 2-connected, deg_B(c) = 2 exactly. The obstruction to be faced and stated:
      suppressing c in B gives a smaller 2-connected δ ≥ 3 graph, but every cycle
      through c shifts length by −1, and 2^k − 1 is not a power of two, so the
      naive suppression reduction does NOT close; the proof needs a sharper argument.
  (b) SAT (tool_builder/sat_solver): encode "δ ≥ 3, no cycle of length 4, 8, or 16,
      with a cut vertex" for n ≤ 16. A satisfying instance refutes G-2conn outright;
      UNSAT for n ≤ 16 is a theorem about that range and corroborates the claim.
```

```gap
id: G-heart
lemma: Every 2-connected graph with minimum degree at least 3 contains a cycle of length 2^k (k ≥ 2).
status: open
discharged-by: ""
thread: ""
next: |
  This is the conjecture restricted to the 2-connected class — the central open
  lemma, and the one to attack first. Three concrete first moves:
  (a) Lean: state it, plus the elementary longest-path position fact
      (longest path ⇒ all neighbours of each endpoint lie on the path ⇒ cycles of
      length i_b − i_a + 2 for every pair of neighbour positions). This is the
      formal scaffolding every later argument stands on.
  (b) SAT: UNSAT for "2-connected, δ ≥ 3, no 4/8/16-cycle" on n = 8..16 pushes the
      computational bound and bounds where a counterexample could still live.
  (c) SMT (Z3/cvc5): model the position constraint {i_b − i_a + 2 ≠ 2^k} together
      with maximality of P and the symmetric constraint at v_m, and find the exact
      point where pure position sets stop satisfying it. Known from hand-check:
      positions {1,2,5} give cycle lengths {3,5,6}, so the endpoint positions alone
      do NOT force a power of two; the heart lemma must use more than the endpoint —
      chord structure, the second endpoint, or the ear decomposition.
```

## Ruled-out directions (recorded so the next attempt does not pay for them twice)

- **Interval-of-ratio-2 middle lemma is false.** The natural hope — "δ ≥ 3 forces
  cycles of every even length in some interval [a, b] with b ≥ 2a, and such an
  interval contains a power of two" — fails already on the Petersen graph: its
  even cycle lengths are {6, 8} (ratio 4/3), yet it *does* contain the 8-cycle.
  So an interval result is sufficient but not necessary, and cannot serve as the
  middle lemma at δ = 3. This is the obstruction the problem statement names.
- **2-suppression does not reduce.** Suppressing a degree-2 vertex (the standard
  tool that would pass from an end-block to a smaller δ ≥ 3 graph) shifts every
  cycle through it by −1, and powers of two are not closed under ±1. This is
  exactly why δ = 3 is the sharp boundary of the problem, and it blocks the cheap
  reduction that would make G-2conn automatic.
- **Endpoint positions alone do not force.** For a longest-path endpoint with
  neighbour positions {1,2,5}, the induced cycle lengths are {3,5,6}, none a power
  of two; d = 3 (the minimum from δ = 3) is numerically compatible with the
  position constraint. The forcing in G-heart must come from global structure,
  not from a single endpoint.
