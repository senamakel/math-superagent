# Brummitt & Rowland, "Boundary growth in one-dimensional cellular automata" (arXiv:1204.2172)

**Source:** https://arxiv.org/abs/1204.2172 (Complex Systems 21 (2012) 85–116; full text at `research/sources/brummitt_rowland_boundary_growth_rule90_body.full.md`)

**What it establishes.** A systematic inventory of the *boundaries* (the width of the region differing from a constant background) of one-dimensional 2-color cellular automata depending on 4 cells, begun from simple initial conditions. Determines exact growth rates for reducible boundaries; morphic words characterize reducible boundaries.

**Rule 90 (relevant to SUPPLY).** From a single black cell, Rule 90's boundary length is `ℓ(t) = 2t + 1` for all `t ≥ 0` — linear boundary growth (full text line ~80). Rule 90 produces *nested structure* (line ~110), the self-similar Sierpinski/Pascal-mod-2 pattern.

**Bearing on SUPPLY.** This is the canonical citation for the boundary/support width of Rule 90 from a single seed: a single ON cell propagates to a support of width `2t+1` at step t, with `2^wt(n)` ON cells within that support (Sloane). The linear *support* width but fractal interior density is exactly the structure of the fold: the number of reading positions grows linearly while the density of the Sierpinski pattern fluctuates. It confirms that support width is linear while interior density is 2-automatic — consistent with, but not a proof of, `ν₂(n) = Θ(n)` for the primes. It is adjacent, not decisive, for the open request `walsh-spectral-subset-b904` (no per-seed input-dependent lower bound is given here).

**Status: sourced primary reference.** Rule-90 boundary growth from finite seeds; supports the vocabulary and the qualitative picture (linear support, fractal density) of the fold object. Not a bound on `wt(Φ_n h)` for the prime input.
