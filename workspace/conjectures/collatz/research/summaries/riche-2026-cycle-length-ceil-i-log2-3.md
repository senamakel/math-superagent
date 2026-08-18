# Riche 2026 — cycle lengths and the smallest element

<!-- src: Sebastien Riche, "3X+1 cycles having length k=⌈i log_2(3)⌉", Cambridge Open Engage, Version 1, 26 Feb 2026, DOI 10.33774/coe-2026-6tt9p. Full landing text: research/summaries/riche-2026-cycle-length-ceil-i-log2-3.md -->

## What the source claims

This is an explicitly **unpeer-reviewed working paper**. For an accelerated Collatz cycle with i odd elements, total length k, and smallest member a_0, it states:

- the elementary bound i < 3a_0 implies k = ceil(i log₂3);
- the paper claims the stronger i < 304a_0 implies k = ceil(i log₂3);
- for m-cycles in the Simons–de Weger sense, it claims m < 1.8296017 a_0 implies the same equality.

This is directly relevant to the run's minimum-element/Diophantine collision arm: it would constrain the cycle's parity ratio whenever the smallest member is large relative to the number of odd members. However, only the abstract/landing page is held here, not a proof text, and the venue labels it an early alternative output.

## Claim

```claim
id: riche-cycle-length-ceil
statement: In an accelerated Collatz cycle with i odd elements and smallest member a_0, the working paper claims i < 304 a_0 implies total length k = ceil(i log₂3), and in an m-cycle claims m < 1.8296017 a_0 implies the same (Riche 2026, DOI 10.33774/coe-2026-6tt9p).
hypotheses: accelerated Collatz cycle; exact definitions of i, a_0, m as in the paper
holds-here: not established — only a working-paper abstract is held
status: asserted-by-source / open for verification
bearing: possible new structural input for G-min-element-lower; must be attacked before use
anchor: research/summaries/riche-2026-cycle-length-ceil-i-log2-3.md
```
