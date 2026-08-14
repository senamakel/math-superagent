# OEIS A014778 (main entry) — fixed points of f(n,1)=n

**Source:** https://oeis.org/search?q=A014778&fmt=text (OEIS catalogue entry). Full text: `research/sources/oeis-A014778-main.full.md`. The b-file (84 terms) is `research/sources/oeis-A014778-full.md`.

## What it establishes

- A014778: numbers k equal to the number of 1's in the decimal digits of all numbers ≤ k — i.e. the PE156 solution set for d=1, including 0.
- **Finiteness (Joseph L. Pe's proof sketch, Nov 2002):** the count of 1's used in positive integers ≤ k is ≥ A(k) = (1/10)·(number of digits in positive integers 1..k) = (1/10)·Σ_{i=1..k}(1+⌊log₁₀ i⌋). By comparing the area below a logarithm with the integral, A(k)/k → ∞, so beyond some k the count always exceeds k and no further fixed points exist. This is the "f grows superlinearly ⇒ finitely many solutions" fact, stated for d=1 in the catalogue and generalized by Khovanova–Marton Prop 9.1.
- Structure (David Wasserman, Jun 2007): six runs of ten consecutive numbers, ten pairs, four isolated numbers; 84 terms total, last = 1111111110.
- Completeness history: no more terms ≤ 10^9 (Propper, Dec 2004); final term sent by Lambrecht Kok Jan 2005 ("H. van Haeringen and I showed this list of 84 terms is complete, Dec 15 2004"); independently shown complete by Ryan Propper and Vaughan Pratt, Jan 2005.
- Cross-references: A094798 (the defining f(n,1)); A101639+A101640+A101641+A130427–A130431 (other digits' fixed-point sequences); A130432 (counts); A165617 (generalization to arbitrary base) — and cites Khovanova–Marton AMM 132(8) 2025 p. 783 Table 2, and the arXiv version.

## Implications for PE156

- Confirms (catalogue status `asserted`) the term count 84 for d=1 and the maximum 1,111,111,110 < 10^10 — consistent with the bound n ≤ d·10^10.
- Gives the run a complete term-count target for d=1: the solver must find exactly 84 values ending at 1,111,111,110.

## Does not settle

- The per-digit sums s(1)..s(9): those are A216398 (excluded; not in this entry). Not a proof of the bound (the arXiv Prop 9.1 is), merely a catalogue finiteness sketch for d=1.