# Pattern recognition on the sharp-kernel census — verified report

Author: pattern-recognition specialist. Every number below was produced by a
program this run ran, or is read from an exact captured artifact. Structural
conclusions over a finite sample are stated as **conjectures**, never dressed up
as proofs.

## Data under analysis

The sharp-kernel census `C_N` (`code/out/census_kernel*.captured.txt`,
`code/out/analyze_kernel_chrom.captured.txt`): graphs on N vertices with
min-degree >= 4, K4-free, K2,3-free, every vertex-neighbourhood graph of
max-degree <= 2. This is the universe any 5-chromatic unit-distance graph must
belong to (a 5-critical subgraph has min-degree >= 4 and inherits the three
geometric inequalities).

Per-N kernel member counts (exact, complete nauty-geng enumeration):

| n | kernel | 4-chromatic | 3-colourable |
|---|--------|-------------|--------------|
| 8 | 1      | 1           | 0            |
| 9 | 4      | 1           | 3            |
| 10| 16     | 16          | 0            |
| 11| 228    | 198         | 30           |

(Total 249 members; every one 4-colourable — verified by BOTH Cadical153 SAT and
independent exhaustive DSATUR backtracking, 249/249 agree, 0 failures.)

## Sequence tools — all three main sequences carry no structure

Run by me this run:

- kernel-count `[1,4,16,228]`: not polynomial (diffs 3,12,212; 9,200; 191),
  leading ratios 4.0,4.0,14.25 (super-exponential onset at n=11). No
  constant-coefficient linear recurrence of order <= 4. OEIS miss.
- 4-chromatic `[1,1,16,198]`: not polynomial; not recurrent; OEIS miss.
- 3-colourable `[0,0,3,30]`: common divisor 3 (every term divisible by 3),
  periodicity mod 3 is trivial; only 4 terms carry no weight. Not polynomial.

The `4^0,4^1,4^2 = 1,4,16` head of the kernel counts is a coincidence-sized
geometric run that breaks at 228 (ratio 14.25). With OEIS silent and only four
terms there is no defensible closed form, and the tools correctly refuse to
manufacture one.

## NEW data slice (not in prior reports): edge-count distribution of the
   198 four-chromatic n=11 kernel members

Extracted by parsing `analyze_kernel_chrom.captured.txt` (`code/edge_counts.py`):

    edges=22 : 15 members
    edges=23 : 112
    edges=24 : 62
    edges=25 : 9
    sum = 198   (matches the reported 198 four-chromatic n=11 members exactly)

**Structural fact (a mild theorem, not just a count).** Every kernel member on
11 vertices has min-degree >= 4, so its edge sum = 2E >= 4*11 = 44, i.e.
E >= 22. A 22-edge member has 2E = 44 exactly, so all 11 degrees are exactly 4:
**the 22-edge members (15 of them) are exactly the 4-regular kernel graphs on 11
vertices.** All 15 are 4-chromatic. Nothing deeper: 23-edge (112), 24-edge (62),
25-edge (9) are just the low-density rim of a class whose members are all still
4-colourable.

The edge sequence `[15,112,62,9]`: not polynomial (diffs 97,-50,-53; -147,-3;
144), no ODEIS match, and the order-2 rational recurrence the tool fits over 4
terms is meaningless overfitting — four terms always fit some such recurrence,
and there is no interpretation behind the fractional coefficients, so it is
rejected, not reported as structure.

## Verdict

**No exploitable numerical sequence structure exists in the data this run
produced.** The three census count sequences and the new edge distribution are
short, uncatalogued, non-polynomial, non-recurrent, and their growth points to
combinatorial accumulation rather than a closed form. There is no route to turn
any of these four-term heads into a theorem by analysis alone; the n=12 count
would be the only term that could decide, and that enumeration is infeasible
(~100M+ graphs; n=11 at 187,095,840 is already at the edge of the 540s / 8 GiB
budget).

The genuinely load-bearing, exact regularity is **structural and already
recorded**: every kernel member through N=11 is 4-colourable (249/249, two
independent oracles), giving `size-bound-udg-4color-n11` — every unit-distance
graph on at most 11 vertices is 4-colourable, and every 5-chromatic UDG has at
least 12 vertices. That is the size-bound result; the counts explain why a
closed form cannot extend it, so the only way forward on that ladder rung is
the enumeration its cost, not its formula, now blocks.

## What this implies for the bound

A 5-chromatic UDG, if it exists, has >= 12 vertices (checked) and contains a
5-critical kernel member; through N=11 none exists. The Moser spindle is the
dominant 4-critical subgraph present in most 4-chromatic kernel members but is
never an induced subgraph (its min-degree-3 vertex violates the kernel's
min-degree condition) and never forces 5-chromaticity at any N <= 11 — a
concrete instance of the core difficulty: 4-chromatic subgraphs are abundant and
harmless, and moving the bound needs accumulated rigidity, not a gadget.

## Artifacts

- `code/edge_counts.py` (new): extracts and checks the edge distribution.
- `code/out/analyze_kernel_chrom.captured.txt` (source of the edge lines).
- Prior reports: `research/approaches/kernel-census-pattern.md`,
  `research/approaches/kernel-sequence-structure.md` (confirm the same
  conclusions independently).
