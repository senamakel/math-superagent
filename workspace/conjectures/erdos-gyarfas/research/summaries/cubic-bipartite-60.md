# 60-Vertex lower bound for cubic bipartite counterexamples (Tranquilli 2026)

**Source:** J. Tranquilli, arXiv:2608.02675v1 (2 Aug 2026), DOI 10.5281/zenodo.21695513.
Full text: [[cubic-bipartite-60.full]]. Preprint (not peer-reviewed) but a *certified*
computation (two independent searches + third streaming certificate checker + nauty
overlap through v=13 + code/artifacts archived on GitHub `floor-licker/erdos-gyarfas-cubic-bipartite`).

## What it establishes

**Theorem 1 (finite cubic-bipartite frontier):** every simple cubic bipartite graph
$G$ with $|V(G)| \le 58$ contains a simple cycle of length 4, 8, or 16.

**Corollary 2:** any simple cubic bipartite counterexample to Erdős–Gyárfás has at
least **60 vertices**. (Cubicity forces $|L|=|R|$, so the order is even; Theorem 1
excludes all orders through 58, next possible is 60.) The computation does **not**
examine side size 30 and so does **not** exclude an order-60 counterexample — the bound
is exact, not 61+.

**Forced length:** Corollary 2 also shows one of the *first three* power-of-two
lengths (4, 8, 16) is always forced in this class below 60 — no 32-cycle is needed.

## Method (structural, new for this run)

1. **Incidence translation (Prop 3):** cubic bipartite graphs biject (up to relabel)
   with connected 3-uniform, 3-regular incidence structures (symmetric $v_3$
   configurations) whose Levi graph is the original.
2. **Moore reduction (Lemma 8):** below 62 vertices a cubic bipartite graph with no
   C4 and no C8 has girth exactly 6 — contains a C6 (edge-rooted nonbacktracking tree
   through depth 4 gives level sizes 1,2,4,8,16; two exposures of 31 each = 62 vertices
   would be needed to avoid a short cycle). C6 = Berge triangle in the configuration.
3. **Two orbits only (Lemma 9):** a Berge triangle, after normalization, extends in
   exactly two rooted ways — a genuine symmetry reduction (runs two search trees, not
   an enumeration).
4. **Certified restricted-growth search (Props 10–11):** complete search on ≤29
   points (35 vertices? no — 29 points = 58 vertices via $|V|=2v$) closes both trees;
   two implementations with different C16 oracles agree on transcript hashes; a third
   streaming checker accepts both certificates with **zero completions**.

Cycle translations used as *oracles*: C4 ⟺ two blocks sharing a point-pair (Lemma 5);
C8 ⟺ a Berge quadrilateral (Lemma 6); incremental C16 ⟺ old simple 14-edge path
between two members of a new block (Lemma 7).

## Implications for this run

- **Raises the best verified lower bound inside a restricted class.** Cubic bipartite
  is a class, not the general conjecture, but it tops both Markström's cubic bound
  (≥30) and the SMS general bound (≥32) *for this class* (≥60). The comparison is a
  table in §1.1 of the paper.
- **Confirms the run's bipartite/near-miss picture.** The Method rules (Berge-cycle
  oracles, incremental C16 test) are the same kind of cycle machinery the run's oracle
  (`code/lib/cycle_oracle.py`) and Markström near-miss census use; nothing here
  contradicts them.
- **A new structural lead for the run:** the Levi-graph / incidence-configuration and
  the Moore-bound-⟹-C6 reduction are a *different* route than SMS. A minimal
  counterexample being predominantly cubic, the incidence view may transfer.

## What it does NOT settle / caveats

- Restricted to **cubic AND bipartite**; non-bipartite or non-regular min-degree-3 is
  untouched. Not the general conjecture.
- Preprint, computer-assisted, not peer-reviewed — though its certificate is
  machine-checkable-adjacent (a genuine LRAT/certified pipeline is still the SMS
  repo's future-work item; here the third checker accepts the stream).
- **Provenance nuance flagged (not a hard contradiction):** the paper reads the 2011
  Nowbandegani–Esfandiari bipartite abstract as stating **30**, while the run's CLAIMS
  ledger (`EG-bipartite-30`) and Hegde et al. attribute **32** to that 2011 work. The
  paper says "later sources sometimes attribute 32". Recorded both; the new Theorem 1
  supersedes whichever figure as the current bipartite frontier anyway.

## Sources it confirms

- Confirms Carr's "predominantly cubic" structure reference and the P10/P13-free and
  3-connected-cubic-planar partial classes as the surrounding literature (no conflict).
- Confirms the SMS n≤31 claim exists and is cited as the newest public *general*
  computation (bound ≥32) — consistent with this run's audit (`asserted-by-source`).

```claim
id: EG-cubic-bipartite-60
statement: Every simple cubic bipartite graph on at most 58 vertices contains a cycle of length 4, 8, or 16; hence any simple cubic bipartite counterexample to the Erdős–Gyárfás conjecture has at least 60 vertices. The bound is exact (an order-60 counterexample is not excluded).
hypotheses: G simple, cubic (3-regular), bipartite, |V(G)| ≤ 58; the power-of-two lengths relevant here are 4,8,16 (32 first fits at an even order ≥ 32).
holds-here: yes — cubic bipartite is a restricted class inside the run's target (⊂ min-degree-3); this is the strongest verified bound for it.
status: asserted-by-source (certified computer-assisted proof, arXiv:2608.02675v1; two independent searches + third checker; preprint not peer-reviewed)
bearing: Raises the verified lower bound for the cubic-bipartite class from ≥30 (Markström) / ≥32 (SMS general) to ≥60 — a class-level frontier the run can cite; its incidence/Moore-reduction method is a fresh structural route for the run's Phase-4 loop.
anchor: research/summaries/cubic-bipartite-60.md; research/sources/cubic-bipartite-60.full.md
answers: the open bipartite frontier row (Nowbandegani–Esfandiari 2011 was ≥30/≥32)
falsifier: an independent reproduction finding a cubic bipartite graph on ≤58 vertices with no C4, C8, or C16, or a peer review that rejects the certificate.
```
