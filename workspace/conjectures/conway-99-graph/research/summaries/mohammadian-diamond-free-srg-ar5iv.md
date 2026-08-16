# On a family of diamond-free strongly regular graphs — summary

**Source**: A. Mohammadian & B. Tayfeh-Rezaie, arXiv:1303.0473 (2013). Full text held:
`research/sources/mohammadian-diamond-free-srg-ar5iv.full.md`. Primary PDF/abs at
arxiv.org/abs/1303.0473.

## What it establishes (for the run's adopted PQ approach)

**The exact diamond-free ⟺ PQ reduction (Theorem-level, primary source).**
A partial quadrangle PQ(s,t,μ) exists iff a diamond-free
`srg(1 + s(t+1) + s²t(t+1)/μ,  s(t+1),  s−1,  μ)` exists. The collinearity graph
of any PQ is such a diamond-free SRG; conversely any diamond-free SRG is the
collinearity graph of the PQ whose points are the graph's vertices and whose
lines are its maximal cliques.

**This directly grounds the adopted approach `pq-2-6-2-classification`:**
for (99,14,1,2) we have k=14, λ=1, μ=2. Since λ=1 ≤ 1 (the quoted condition is
λ ≤ 1 or μ = 1), srg(99,14,1,2) IS the collinearity graph of a
partial quadrangle. Solving `s(t+1)=14`, `s−1=1`, `μ=2`, `s²t(t+1)/μ = s(t+1)(st)/2·...`:
s−1=1 ⇒ s=2; s(t+1)=14 ⇒ t+1=7 ⇒ t=6; and the SRG is
1 + 2·7 + 2²·6·7/2 = 1+14+84 = 99. So exactly **PQ(2,6,2)**. This confirms the run's
adopted reformulation from a free primary source (previously only asserted
from Cameron 1975/Bagchi abstracts).

**The diamond-free local condition as a consistency check on the oracle:**
an SRG is diamond-free iff λ+1 | k and every neighborhood is k/(λ+1)·K_{λ+1}.
For (99,14,1,2): λ+1=2 | 14 ✓, neighborhoods are 7·K₂. This matches claim `c5`
(locally 7K₂) — both control graphs are the collinearity graphs of PQs
(rook(3): PQ(1,3,2)... verify; BvLS: diamond-free, λ=1).

**A family of the same λ=1 shape (Bondarenko–Radchenko, quoted):**
`PQ(2, (n³+3n²−2)/2, n²+n)` ⇔ `srg((n²+3n−1)², n²(n+3), 1, n(n+1))` exists iff
n ∈ {1,2,4}. For n: the run already knows this subfamily — n=1 ⇔ srg(9,4,1,2)
(rook, exists), n=2 ⇔ srg(81,20,1,6) (Brouwer–Haemers, exists), n=4 ⇔ the Games
graph (441,...). **n=3 (srg(225,...)) ruled out** — this is claim
`bondarenko-radchenko-lambda1-gk`, now corroborated by a second primary source.

**The paper's own main theorem** is about a DIFFERENT family (λ=2, negative
Latin square graphs with g=k), Theorem 1: a diamond-free
srg((n²+3n−2)², n(n²+3n−1), 2, n(n+1)) satisfying condition (1) has n∈{−2,2,3,10}.
Peripheral to (99,14,1,2) but a worked example of the eigenvalue-multiplicity-
equals-valency (g=k) machinery the run's `least-eigenvalue` approach touches.

## Implications for this problem

- Confirms the partial-quadrangle reformulation Q = PQ(2,6,2) as a theorem
  with citation, not an assertion. Bearing on the adopted `pq-2-6-2` approach.
- λ=1 ⇒ diamond-free is a *necessary* condition the run already has (c5);
  this source explains it as "collinearity graph of a PQ", the geometry the
  problem statement asks the run to reason in.
- The Bondarenko–Radchenko n∈{1,2,4} subfamily corroborates the claim that λ=1
  SRGs form a sparse known family; 99 is NOT in that subfamily (it has μ=2,
  g=44≠k=14), i.e. the g=k negative-Latin-square technique of this paper does
  NOT apply to 99. That is a precise "which family 99 is not in".

## Gap / what would settle more
Cameron's defining "Partial quadrangles" (1975) remains not held (paywalled);
the PQ definition here (from Mohammadian–Tayfeh-Rezaie) matches the search
excerpts of Cameron's paper, so the core definition is now independently
sourced. If PQ(2,6,2) self-duality or a PQ-specific parameter constraint is
needed later, that is the one remaining unheld primary PQ source.

```claim
id: diamond-free-srg-iff-pq-2602-grounding
statement: An SRG is the collinearity graph of a partial quadrangle PQ(s,t,mu)
  iff it is diamond-free; explicitly PQ(s,t,mu) exists iff the diamond-free
  srg(1+s(t+1)+s^2 t(t+1)/mu, s(t+1), s-1, mu) exists (Mohammadian-Tayfeh-Rezaie,
  arXiv:1303.0473, primary). For (99,14,1,2): lambda=1 gives s-1=1 so s=2,
  s(t+1)=14 so t=6, mu=2 -> exactly PQ(2,6,2). An SRG is diamond-free iff
  lambda+1 | k and every neighborhood is k/(lambda+1)*K_{lambda+1}; for
  (99,14,1,2) this is 2|14 and neighborhoods 7*K2, matching claim c5.
hypotheses: srg(99,14,1,2) diamond-free (lambda=1); the diamond-free<->PQ
  equivalence as stated in the source.
holds-here: yes -- confirms the adopted pq-2-6-2-classification reformulation
  Q=PQ(2,6,2) as a theorem with a citation.
status: sourced (Mohammadian-Tayfeh-Rezaie arXiv:1303.0473 full text held);
  the (99,14,1,2)->PQ(2,6,2) parameter solve is verified-by-hand arithmetic.
bearing: primary-source grounding for the adopted pq-2-6-2 approach; also notes
  the g=k negative-Latin-square technique of that paper does NOT apply to 99
  (g=44 != k=14), pinning which lambda=1 family 99 is not in.
anchor: research/sources/mohammadian-diamond-free-srg-ar5iv.full.md (Section I);
  research/sources/mohammadian-diamond-free-srg.full.md (abstract);
  check: code/out/check_pq_parameter_map.py
```
