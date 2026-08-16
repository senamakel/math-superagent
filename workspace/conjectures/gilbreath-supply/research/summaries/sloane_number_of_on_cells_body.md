# Sloane, "On the Number of ON Cells in Cellular Automata" (arXiv:1503.01168)

**Source:** https://arxiv.org/abs/1503.01168 (full text at `research/sources/sloane_number_of_on_cells_body.full.md`; the URL above)

**What it establishes.** For a cellular automaton started from a single ON cell, how many cells are ON after n generations. For odd-rule CAs the answer is computed via a new **run length transform** combined with "scissor cuts".

**Rule 90 (the case directly relevant to SUPPLY).** For Rule 18 / Rule 90 (Rule 182 is very similar), the number of ON cells in generation n is

```
a_n = 2^wt(n)   (Gould's sequence, OEIS A001316)
```

where `wt(n)` is the number of 1s in the binary expansion of n. This is the run length transform of the powers of 2. (Full text line ~362.)

**Run length transform (the paper's main tool).** Given a sequence `[a_n]`, its run length transform is built by reading runs of consecutive 1s in the binary expansion of n: `a_n = ∏_{i in L(n)} a_{2^i − 1}` where L(n) is the set of lengths of runs of 1s in n's binary expansion. This is exactly the structure the fold's submask-XOR reading lives on (the 2-cell / odd-rule CA structure), and it is the same transform SUPPLY's `ν₂ = wt(Φ_n h)` layer-respecting structure exhibits — this is a primary source that the fold's fractal/2-automatic counting is a catalogued, named phenomenon.

**Bearing on SUPPLY.** Confirms and diarises the single-seed case: Rule 90 from a single ON cell gives `2^wt(n)` ON cells at generation n. This is the *sparse-amplification* extreme (one input 1 → many output cells) that the run already knows (`h=e_{2^m}` gives `wt(Φ_n h)=n−O(1)` at n=2^m+1). It does **not** give a per-input lower bound on `wt(Φ_n h)` for a general seed h (that is the open request `walsh-spectral-subset-b904`), but it fixes the vocabulary (run length transform, Gould's sequence, rule-90 ON-cell counting) and the canonical counting reference. The run-length transform connects directly to the run/character-product structure of the fold cell.

**Status: sourced primary reference.** Not a solution to SUPPLY; a canonical adjacent reference for the literal object `wt(Φ_n h)` in the single-seed case.
