# Erdős–Gyárfás conjecture — weakened ladder

Bottom-up: the weakest rung is a single model instance (the Petersen graph,
the extremal graph for the girth obstruction at δ ≥ 3). Each step restores one
named difficulty on the way back up; the top rung is the conjecture itself.
Nothing here is settled yet — this run's claims ledger is empty — so every
rung is `open` and handed to the forward loop.

```ladder
goal: Every finite simple graph with minimum degree at least 3 contains a cycle whose length is a power of two (2^k, k ≥ 2).
difficulties: unbounded n, prescribed sparse length, minimal degree hypothesis, no structural restriction, long-cycle reach
status: open
```

```rung
id: R-petersen-8cycle
statement: The Petersen graph — the unique 3-regular graph on 10 vertices of girth 5 — contains a cycle of length 8.
off: unbounded n, prescribed sparse length, minimal degree hypothesis, no structural restriction, long-cycle reach
stance: open
merge: Restore `unbounded n` in its weakest form: pass from the single Petersen instance to the finite class of all graphs with δ ≥ 3 on n ≤ 12 vertices. This step restores `minimal degree hypothesis` and `no structural restriction` together, because they only come alive once the claim ranges over δ ≥ 3 graphs with no further hypothesis. First move: run the oracle over all graphs with δ ≥ 3 on ≤ 12 vertices and check for a 4- or 8-cycle; the Moore bound (girth ≥ 5 forces n ≥ 10) plus the Petersen case at n = 10 should make this a short enumeration.
```

```rung
id: R-delta3-n12-small-target
statement: Every finite simple graph G with δ(G) ≥ 3 on at most 12 vertices contains a cycle of length 4 or 8.
off: unbounded n, prescribed sparse length, long-cycle reach
stance: settled-by-verification — Balaji SMS (Zenodo 20782738) verifies ALL δ≥3 graphs on ≤31 vertices have a C4/C8/C16, so the n≤12 range is covered. Clifford: do not re-spend budget re-proving this; the oracle check of the n≤16/24 cases is regression only.
merge: Restore `prescribed sparse length`: raise the cap to n ≤ 16 so that 16 becomes a live target and the sparse set {4, 8, 16} has its first genuine gap — a graph could contain 4- and 8-cycles yet no 16-cycle, so the argument must now hit a prescribed length instead of "some small even cycle". First move: SAT/CP-SAT query for a δ ≥ 3 graph on ≤ 16 vertices with no 4-, 8-, or 16-cycle; UNSAT is the theorem for R-delta3-n16-three-targets, SAT is a counterexample.
```

```rung
id: R-delta3-n16-three-targets
statement: Every finite simple graph G with δ(G) ≥ 3 on at most 16 vertices contains a cycle of length 4, 8, or 16.
off: unbounded n, long-cycle reach
stance: settled-by-verification — within the Balaji n≤31 verified range (all δ≥3 graphs there have a C4/C8/C16). Keep as an oracle hand-check of the checker only.
merge: Restore `long-cycle reach`: push n to 1024. Now a guaranteed girth (≤ 5 unless n ≥ 22) sits a factor ≥ 2, and up to ~200, below the required 2^k, so the cycle must be extended across an exact-doubling gap that grows with n rather than found inside a bounded range. First move: a structural "doubling" lemma — from a cycle of length ℓ in a δ ≥ 3 graph, force a cycle of length 2ℓ (or 2ℓ ± 2) — or a refutation of R-delta3-n1024 within n ≤ 1024.
```

```rung
id: R-delta3-n1024
statement: Every finite simple graph G with δ(G) ≥ 3 on at most 1024 vertices contains a cycle of length 2^k for some 2 ≤ k ≤ 10.
off: unbounded n
stance: open — THIS is the first rung NOT settled by the Balaji 32-vertex bound, hence the first genuinely open target the run should attack. The graph may have an internal girth c with a 2^k-cycle only at lengths ≥ its Moore-required n, so the exact-doubling reach is the live difficulty.
merge: Restore `unbounded n`: drop the vertex cap entirely. This is the step from a finite verification to the full conjecture, and it is where only a uniform structure theorem works. First move: assume a minimal counterexample and derive 2-connectivity, girth ≥ 5, near-3-regularity, n ≥ 2^k for every k ≤ log₂ n, and the absence of small separators — then find the contradiction that closes it.
```

```rung
id: R-full-conjecture
statement: Every finite simple graph G with δ(G) ≥ 3 contains a cycle of length 2^k for some k ≥ 2.
off:
stance: open
merge: (The goal itself — nothing left to restore. The ladder is exhausted only when this closes, which is the one case where the conjecture is solved.)
```
