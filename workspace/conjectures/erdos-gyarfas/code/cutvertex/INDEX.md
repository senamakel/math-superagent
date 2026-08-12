# Index — code/cutvertex

Machine verification of the run's Cut-Vertex Characterization theorem clauses, plus the oracle worked-example reproduction.

| File | Purpose |
| --- | --- |
| `verify_cutvertex.py` | Verifies cut-vertex lobe clauses (a),(b),(c) of the Cut-Vertex Characterization theorem and the oracle's worked examples. Builds 2-lobe (Petersen+K4, K4+K4, prism+prism), 3-lobe (3x Petersen, 3x prism, Petersen+prism+K4), and random 2/3-lobe glued cut-vertex graphs; enumerates every simple cycle exactly (lib.cycle_oracle, cross-checked against networkx — always agree) and checks (a) every simple cycle lies in a single lobe (equiv. cycle_lengths(G) == union of lobe cycle sets), (b) pow2-free G ⇒ pow2-free lobes, (c) d_L(w)==d_G(w) for every w. Also asserts the oracle worked examples (K4 {3,4}, K3,3 {4,6}, cube {4,6,8}, Petersen {5,6,8,9}). **All 14 checks PASS**; log at code/out/cutvertex/verify_cutvertex.log. The earlier clause-(a) FAILs were a checker bug (redundant vn==2 block), not a theorem failure — with it removed, the union-equals-G-cycle-set identity holds in every case. |

See also `../connectivity/verify_connectivity.py` and `verify_connectivity_k2.py` (the k=2 split-type lobe lemma), which this script generalises to arbitrary cut vertices and k≥3 lobes.
