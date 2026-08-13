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

named mathematics: max-flow/min-cut theorem (Ford-Fulkerson, Edmonds-Karp),
Menger's theorem, Hall's marriage theorem, Dilworth's theorem on chain
decompositions, network flow with gains, conservation laws.

status: refuted
killed-by: >
  Refuted on the two points that decide whether the approach can ever say
  anything. (1) The min-cut certificate is a restatement of the recharge
  identity, not a new bound on it. The recharge identity
  b_k = b_1 + Σ(j_i+1) − (k−1) is already PROVED (claim
  step-law-and-recharge-identity, evidence checked, zero failures to depth
  800). The cut of a forward chain S→row1→…→rowk has capacity exactly
  min over prefixes of (b_1 + Σ_{events ≤ prefix}(j_i+1) − consumption) —
  the min-cut VALUE is b_k. Every cut with capacity < k−1 exists iff b_k
  would be < 0, which is the conjecture's negation itself. So "no finite cut
  of capacity < total consumption" ⟺ "b_k ≥ 1 ∀k" is literally the
  conjecture restated in flow language; the max-flow/min-cut theorem
  (Ford–Fulkerson 1957) supplies no new inequality because the network is
  a single chain — there is no branch structure for a cut to exploit.

  (2) The "key lemma to prove" — that pumps inject at least some minimum mass
  on average — is exactly the open regeneration-rate question, and the run's
  own evidence says a mean-rate bound is the WRONG target: the recharge
  surplus is heavy-tailed (bigjump-cap-characterization-1000: 12 genuine
  giant jumps carry 86.1% of the surplus S_1000; the giants are NOT
  erosion-recovery events, arriving 1–13 rows after the previous event), and
  the measured event rate λ̂ = 0.585 is family-independent but not bounded
  below for all k (conditional-rate-experiment-family-independent, measured
  not proved). A network-flow statement whose required lemma is "jumps are
  large enough, often enough" has simply renamed the open quantity.

  (3) The general-class hope is dead on the same evidence that kills every
  general-class approach: Eppstein 2011 (anti-gilbreath-construction) builds
  2-then-odds sequences with gaps ≤ f(n) whose right edge escapes and
  re-enters 1 infinitely often — i.e. the flow through any such "pump
  network" runs dry infinitely often in that class. The primes can only
  differ by non-concentration, which no flow theorem supplies.

  What is genuinely useful in the file is the identification of the
  recharge identity as a conservation law — but that is already proved and
  already the run's central accounting. The flow vocabulary adds no new
  theorem.
precedent: >
  - https://doi.org/10.4153/cjm-1957-024-0 (Ford–Fulkerson 1957: the
    max-flow/min-cut theorem — the named mathematics, correct but inert here
    because the network is a single chain)
  - https://doi.org/10.1090/s0025-5718-1993-1182247-7 (Odlyzko 1993 — the
    literature on the actual triangle; no flow treatment exists)
  - https://arxiv.org/abs/2607.08712 (CHT 2026 — the only structural
    obstructions to decay; no network formulation)
  - claims: step-law-and-recharge-identity, bigjump-cap-characterization-1000,
    conditional-rate-experiment-family-independent, anti-gilbreath-construction
holding-claims: step-law-and-recharge-identity,
  bigjump-cap-characterization-1000, conditional-rate-experiment-family-independent
falsifies: >
  That the min-cut certificate is a NEW inequality beyond the proved recharge
  identity, or that a flow theorem supplies a lower bound on the (2,4)-event
  jump mass for the primes or for the 2-then-odds class. The first is false
  because the network is a single chain (min-cut value = b_k exactly); the
  second is exactly the open question, and Eppstein's construction shows the
  class-level version is false.
buy: >
  A clean vocabulary for the proved recharge identity (initial endowment +
  pump injections − consumption = block length), but no new mathematics: the
  conservation law is already proved, the certificate it would produce is a
  restatement, and the missing lemma (jump mass lower bound) is the
  conjecture. Refuted as a route to regeneration.

first-step (superseded): >
  Building the exact flow network from blocks_depth1000.json would reproduce
  b_k at every row by construction — a tautology, not a check. The residual
  capacity question (max consumption before a cut appears) is b_k itself
  restated.
```

```claim
id: zero-sum-flow-mincut-restatement-refuted
statement: The max-flow/min-cut reformulation of the recharge identity
  b_k = b_1 + Σ(j_i+1) − (k−1) is a restatement, not a new bound: on the
  forward chain S→row1→…→rowk, the min-cut value equals b_k exactly, so
  "no cut of capacity < total consumption" ⟺ "b_k ≥ 1 for all k" is the
  conjecture itself; the required lemma (pump jump mass bounded below) is
  the open regeneration-rate question, and the class-level version is false
  by Eppstein 2011.
hypotheses: the proved recharge identity; the run's heavy-tail measurement
  of the surplus (12 genuine giant jumps carry 86.1% of S_1000).
holds-here: yes
status: refuted (structural: single-chain network has no branch structure for
  a cut to exploit; the missing lemma is the conjecture)
bearing: closes the network-flow line; the recharge identity remains the
  exact accounting, but no flow theorem adds to it. A lower bound on jump
  mass is the only thing that would matter, and none is known.
anchor: research/approaches/zero-sum-flow-conservation-mincut.md
```
