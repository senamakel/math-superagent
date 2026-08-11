# 1D ballistic aggregation final state — Majumdar, Mallick & Sabhapandit (Phys. Rev. E 79, 021109, 2009)

<!-- source: https://journals.aps.org/pre/abstract/10.1103/PhysRevE.79.021109 | peer-reviewed version; DOI 10.1103/PhysRevE.79.021109 -->

The peer-reviewed (PRE) version of the 1D sticky-gas result. It is identical in substance to the arXiv preprint; the APS `.full.md` sibling here contains only the journal abstract page (paywall, article text not retrievable), so every substantive claim below comes from the arXiv full text [[torpids_ballistic_aggregation_arxiv.full]] (arXiv:0811.0908), not from this page. I flag that distinction so nobody mistakes the paywalled abstract for the derivation.

## What the paper establishes (pure, no-boundary model)
Model: N unit-mass particles on a line, ballistic at constant speeds v_i, forming sticky clusters on collision (mass & momentum conserved, energy dissipated); initial v_i iid from any continuous φ(v). No boundary. In the long-time limit the system reaches the **fan state**: clusters whose velocities strictly increase left→right, so no further collisions.

- **Final partition = convex minorant** of the random walk with steps (1, v_i) (cumulative mass & momentum). Each straight minorant segment is one cluster; its slope = cluster velocity = mean of the v's in that contiguous index block.
- **Universal (φ-independent) cluster statistics:**
  - P(k clusters) = S1(N,k)/N! = P(a uniform random permutation of N has k cycles); mean # clusters H_N ~ ln N.
  - Unordered cluster-size distribution = random-permutation cycle-length distribution: Pr(#clusters of size j = c_j) = δ(Σ j c_j = N)·Π_j 1/(j^{c_j} c_j!).
  - Largest cluster ~ Golomb–Dickman 0.6243299885·N; smallest ~ e^{−γ} ln N; typical cluster N/ln N; per-cluster factor 1/n from **Raney's lemma** (of the n cyclic rotations of an n-step block, exactly one keeps the walk above its chord).
- **Leader** (rightmost/highest-velocity cluster; φ with finite σ²): leader size ⟨n⟩ ~ b√N with b = e^{C/2}√π = 2.63533…, universal scaling W(x)=b/π^{1/2} x^{−3/2}(1−x)^{−1/2}; leader velocity distribution is non-universal (depends on φ). Cauchy φ (σ² infinite): conditional leader size ~ N/ln N, exactly solvable.

## What it implies for PE 597
- Identifies the **pure bumper race (no finish line)** — boats merging into the convoy of the next rowing boat ahead — with these convex-minorant clusters; bump leaders = right-to-left record minima of the speeds (see [[torpids_record_runs_platoons_haghighi_talab]]). The pure-case bump partition is therefore *cycles of a uniform random permutation*, a concretely computable object whose parity is a signed sum over the block/cycle structure (a derivation the paper does not itself carry out).
- **Does NOT solve the target p(13,1800).** The entire theory is for the boundary-free problem. The finish line at L removes boats from the convoy by finishing (inverse-exponential finish times, [[inverse_exponential_finish_times_wikipedia.full]]), which the convex-minorant mapping does not model — it is precisely the missing boundary that MEMORY.md's refuted treap/rate-ratio recursions failed to absorb. So this is background structure for the no-finish limit, not a closed recursion for the finite-finish probability.
- **No contradiction with MEMORY.md.** It corroborates the library's reading (parity depends on magnitudes of speeds, not w-order alone; the finish line is the obstruction), and independently explains why the earlier exponential-clock/treap route failed.

DOI: https://doi.org/10.1103/PhysRevE.79.021109
