# zero-sum-flow-conservation-mincut

```approach
idea: Reformulate the Gilbreath block-length dynamics as a max-flow/min-cut
problem on a directed acyclic graph, where b_k ≥ 1 ∀k is equivalent to the
non-existence of a finite cut separating the initial {0,2}-endowment from the
erosion sink.

mechanism: The recharge identity
    b_k = b_1 + Σ_{i<k} (j_i + 1) − (k−1)
is an EXACT conservation law. Rephrase it as a flow conservation:
    (block length at time k) = (initial block) + (total injected mass) − (total
    consumed mass).

Define a directed acyclic network:
- Source S connected to the initial block with capacity b_1.
- Each (2,4)-event i at row k_i is a "pump node" P_i with inflow = capacity
  from the upstream network, and outflow = j_i + 1 units injected into the
  block. The pump node's capacity is the maximum possible j_i given the gap
  distribution at that boundary position.
- Each transition row without an event is a "pipe" that passes flow forward
  but consumes exactly 1 unit (the erosion). Represent these as edges with
  cost 1.
- Sink T is the state b_k = 0 (conjecture failure).

The conjecture b_k ≥ 1 ∀k is equivalent to: there is NO finite cut (S,T) in
this network whose capacity is less than the total consumption demanded up to
that row. By the max-flow/min-cut theorem (Ford-Fulkerson), this is equivalent
to: the max flow from the source (initial block + all possible future pump
injections) to row k exceeds the consumption k−1.

Now the STRUCTURE: each pump node P_i draws its injection capacity from the
local halved-gap structure at the boundary at row k_i. A pump at row k_i can
inject at most M(k_i) units, where M depends on the gap values in the influence
window. The network is acyclic (time flows forward) and the min-cut theorem
applies classically.

The key lemma to prove: the cut capacity grows at least linearly in k because
the prime gaps (while irregular) supply enough even entries near the boundary
that each pump injects at least some minimum mass on average. This is a
statement about the ABUNDANCE of even integers (prime gaps) near the boundary
— not about the XOR pattern, not about blocks, not about erosion per se. It
converts the open "regeneration rate" question into a "supply rate" question:
does the prime-gap sequence supply enough {0,2}-inducing entries at the
boundary to keep the flow from ever running dry?

The min-cut certificate has a concrete form: find a set of rows R and a set of
pump nodes P such that the total consumption across R exceeds the total
injection from P plus b_1. If no such (R,P) exists, the conjecture holds. The
dual max-flow is a routing of block-mass through the events, and a max-flow
that exceeds all consumption demands forever IS a proof.

Why this is genuinely different: every approach on disk is either (a) an
algebraic invariant of the row entries, (b) a potential/Lyapunov function on
the block-intruder state, or (c) a spectral/transform analysis of the XOR
interior. This approach is none of them — it is a combinatorial network-flow
problem, where the object of study is the capacity of cuts rather than the
state of any individual row. The recharge identity is already proved; the
flow formulation just re-interprets it as a network whose cut structure is
analysed with graph-theoretic tools (max-flow/min-cut, Menger's theorem,
Dilworth, Hall's marriage theorem for the bipartite matching between pump
injections and consumption demands).

Named mathematics: max-flow/min-cut theorem (Ford-Fulkerson, Edmonds-Karp),
Menger's theorem, Hall's marriage theorem, Dilworth's theorem on chain
decompositions, network flow with gains, conservation laws.

status: proposed

first-step: Build the exact flow network from the depth-1000 prime data
(code/out/blocks_depth1000.json). For each live row k = 1..161:
- Node for each row.
- Edges from row k to row k+1: capacity = b_k (block can carry mass forward),
  cost = 1 (consumption).
- Pump nodes at each (2,4)-event row: capacity = j_i + 1 (the measured jump).
- Source edge to row 1: capacity b_1 = 2.
- Sink: a dummy node T with infinite capacity edges from every row k where
  b_k = 0 (none in the data, so T is unreachable — consistent with GC holding
  to depth 1000).

Then compute the min-cut of this network at each row k and verify it equals
b_k + (k−1) (the recharge identity). More importantly, compute the MAXIMUM
consumption that the network can sustain before a cut appears: this is the
residual capacity. Then formulate the general cut condition algebraically:
a cut is defined by a subset of rows R and a subset of excluded pump nodes P.
Prove a lemma: if no cut with capacity < k−1 exists for any k, the conjecture
holds. Then attempt to prove that the cut condition is infeasible for ANY
2-then-odds sequence using only parity + gap bounds, which would dispose of
Gilbreath for the general class.

Speculative: the cut condition may reduce to a known result about the
hardness of packing prime gaps into small intervals — i.e., a statement
about the irregularity of the primes being insufficient to starve the
network. If this step identifies a specific arithmetic property the primes
must have (e.g., "gaps cannot be clustered without also producing a
compensating nearby even entry"), that IS a partial result.
```