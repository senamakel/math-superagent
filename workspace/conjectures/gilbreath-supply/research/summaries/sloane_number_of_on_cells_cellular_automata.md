# Sloane, "On the Number of ON Cells in Cellular Automata" — metadata page

**This file is the arXiv abstract/metadata page for arXiv:1503.01168.** The full
text is digested in the companion `research/summaries/sloane_number_of_on_cells_body.md`
(complete text at `research/sources/sloane_number_of_on_cells_body.full.md`).
Do not re-read this metadata page; read the `_body` digest when the question is
content.

## One-line bearing (from the body digest)

For odd-rule CAs from a single ON cell, the number of ON cells after n
generations is computed by the **run length transform**. For Rule 90 the count
is `a_n = 2^wt(n)` (Gould's sequence, OEIS A001316) — the sparse-amplification
extreme the run already knows (`h = e_{2^m}` gives `wt(Φ_n h) = n − O(1)`). The
run-length transform is the same structure the fold's submask-XOR reading lives
on. It does **not** give a per-input lower bound for a general seed h (request
`walsh-spectral-subset-b904` stays open); it fixes the vocabulary and the
canonical counting reference.

Full text: [[sloane_number_of_on_cells_body.full]] via
`research/sources/sloane_number_of_on_cells_body.full.md`.
