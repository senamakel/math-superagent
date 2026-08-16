# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## lesson

- **chisel**: Three reformulations closed on primary-source evidence: (1) NPS tree dictionary + Kraft — transfer points the WRONG lengths at the tree (2^k-cycle ⟺ leaf-leaf path 2^k−2) and Kraft is a density bound that cannot force a sparse target; (2) GF(2) cycle-space odd-part — symmetric difference of two cycles decomposes into several cycles, so no single-cycle recombination law and no v2 forcing; (3) degree-3-critical classification — a minimal counterexample is NOT pinned to 2n−2 edges (cubic ⟹ 3n/2), so all the 2n−2-edge cycle theorems have their hypotheses fail. ROOT.md §2 still wrongly says…

## offer

- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
Skeleton written to `research/backward/minimal-counterexample-longest-path.md` and carried into the `goals` ledger (entry `minimal-counterexample-longest-path`).

**The reduction.** By contraposition on a vertex-minimal counterexample $G$ ($\delta\ge 3$, no $2^k$-cycle):

1. $G$ is connected — a disconnected $\delta\ge 3$ graph has a smaller counterexample component.
2. $G$ is 2-connected — this is the first gap.
3. On a longest path $P=v_0\dots v_m$, every neighbour of $v_0$ lies on $P$; if the neighbour…
