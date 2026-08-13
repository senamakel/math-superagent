# OEIS A036262 — iterated prime differences (Gilbreath array)

**Full text:** `research/sources/oeis-A036262-iterated-prime-differences.full.md` [[oeis-A036262-iterated-prime-differences.full]]
**Source:** https://oeis.org/A036262 (catalogue).

## What it establishes

The catalogue of the Gilbreath array (row 0 = primes, rows = absolute differences). Terms read by antidiagonals; the leading column is all 1s by the conjecture.

- **M.F. Hasler's comment (2012) — the key mechanism of this run, catalogued here.** (1) Every term except the first of a row is even. (2) The first term >1 in any row must equal 2, else the conjecture is violated: if the 2nd term >2 then ≥4, and the first term of the next row is ≥3. (3) If a positive number of zeros precedes a first term >2 (hence ≥4), this "jump" remains constant and *propagates* to the beginning of the row in subsequent rows — the `second-entry-4-kills`/propagation mechanism the run's ROOT.md and reduction use. (4) Equivalence: GC ⟺ A036277(n) > A213014(n) + 2 for all n, where A213014 counts zeros before the first term >1 in row n and A036277 is... (the first term >1).
- **Clark Kimberling's comment (2022):** defines the Gilbreath transform G(S) = (g(n,1)) (first column of the array); GC is G(primes) = all 1s. "It appears that there are many S such that G(S) is eventually periodic" — cf. A358691. (Kimberling's g(k,n) indexing differs slightly from Hasler's; the caveat that "row 0 vs row 1" differs across sources is also recorded.)
- Odlyzko bound restated (π(10^13) ≈ 3×10^11).
- **Links/refs:** Guy A10, Montgomery, Pickover, Ribenboim, Sierpiński; Killgrove–Ralston 1959, Odlyzko 1993, Proth 1878, and now **Muney 2026** (Sect 14.1). T.D. Noe b-file through n=5049.

## Hypotheses / bearing

Catalogue source (status catalogued). The Hasler comment is the cleanest OEIS statement of the "second entry must stay in {0,2} or the jump propagates and kills the leading 1" — exactly this run's `second-entry-4-kills` and `gilbreath-reduces-to-second-in-02`. It gives the A036277/A213014 reformulation, a catalogue-backed checkable identity. Kimberling's eventual-periodicity observation is heuristic.

## Claims

```claim
id: oeis-hasler-propagation
statement: Every row's non-first terms are even; the first term >1 in a row must be 2 (else ≥4 and the next row's first term is ≥3); a ≥4 value preceded by zeros propagates unchanged toward the row start in later rows; and GC ⟺ A036277(n) > A213014(n)+2 for all n.
hypotheses: primes triangle; the absolute-difference iteration.
holds-here: yes — the propagation mechanism is the run's second-entry-4-kills statement.
status: catalogued (OEIS comment by M.F. Hasler); matches the run's proved reduction.
bearing: catalogue-backed phrasing of the {0,2}-second-entry necessity; a checkable identity.
anchor: research/sources/oeis-A036262-iterated-prime-differences.full.md
```
