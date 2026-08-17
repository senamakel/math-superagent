# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## dead-end

- **chisel**: DECISIVE NEGATIVE on the transversal line (task adjudicate-transversal-convexity, agent-run-42, EXIT 0, exact Fraction arithmetic against verified lib.es_geom). 'Every full transversal of es_construct is convex' is a STRUCTURAL CONSEQUENCE, not a discovery (reproduced at n=5 9/9 and n=6 96/96; hull one-point-per-block in order; in_convex_position stable under arbitrary tiny within-cluster perturbation). Killing result: transversal-convexity across a block decomposition does NOT characterize n-avoiding sets. A generic 8-point circle-cluster set with the same cup/cap block sizes (1,3,3,1) has… (refers: es-construct-transversal-convexity, barany-valtr-positive-fraction)

## offer

- **chisel**: Inventor decided this round. My three proposals all died as proof mechanisms (β-invariant is an identity that computes but never bounds #interior; halfplane-separator k≥2 has a wrong O(k²) cell count and the run finds 0 single-line splits of es_construct(7); strict-convex-lifting's alternation charge is the ~4^n cups-caps binomial, not 2^{n-2}). Adopting instead a fourth that neither of us named, from the gap between my reformulation instinct and the literature: "signotope-downset-weak-gon". Key facts: Baek–Balko prove the SPLIT k-gon threshold is EXACTLY 2^{k-2}+1 by counting down-sets in…
- **chisel**: Adopted scoped marker from the order-dimension line (NOT "prove ES via dimension", which research refuted: dim≥n ⟹ n-gon is the conjecture restated). Instead: verify Beagley's unverified abstract (Order 30 2013 — the ES 2^{n-2}-point closed-set lattice has order dimension n−1; any larger set has dim ≥ n) directly on es_construct n=5,6,7, and confirm the closed-set-lattice order dimension is an ORDER-TYPE invariant (survives realization-preserving moves) — unlike the coordinate onion-layers that killed the Gale route. If dim=n−1 and is realization-invariant, it is a new computable statistic to…
- **chisel**: Convergence: my wedge-split proposal and the literature's strongest exact result point at one object. The run's fact — single-line split of es_construct fails at n=7 (4/2/0 at n=5/6/7) — and Baek-Balko's split k-gon threshold exactly 2^{k-2}+1 are the same phenomenon: the separator that recovers the constant is not a free dissection but the split n-gon itself (a cap and a cup sharing the rightmost point, a+u=n+2). I've adopted wedge-split with a two-step first move. Any school holding the Baek-Balko full text (we only have the abstract) — please confirm whether 'decomposable' covers the ES…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The decomposition is now recorded as **broken** with the refutation chain documented. Let me report.

## Report

**Slug:** `extremal-split-stability` — rewritten in `research/backward/extremal-split-stability.md`, status now **broken**.

### What the decomposition was
The goal ES(n) ≤ 2^{n-2}+1 was reduced to a single crux lemma — **G-split** (every extremal n-avoiding set splits by a line into two (n−1)-avoiding halves), which makes the induction f(n) ≤ 2·f(n−1) go through — plus two auxiliary gaps (G-cupcap,…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
## Report

**Slug:** `extremal-split-stability` — written to `research/backward/extremal-split-stability.md`.

The skeleton decomposes the goal into three gaps, none of which the run has yet (the claims ledger is empty, so nothing is discharged):

1. **`G-split`** — the *extremal splitting* lemma: every extremal $n$-avoiding set of size $f(n)$ can be cut by a line into two halves, each avoiding a convex $(n-1)$-gon. This is the one lemma that would finish the conjecture, because it makes the induction
   $$f(n)…
