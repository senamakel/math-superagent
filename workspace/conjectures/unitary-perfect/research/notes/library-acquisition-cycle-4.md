# Library acquisition cycle 4 — Fibonacci primary tier + Cunningham Appendix C (+1 side)

## What was added this cycle

| Path | What it is | Verdict |
| --- | --- | --- |
| `research/sources/wall-1983-unitary-harmonic-numbers.full.md` | Wall, *Unitary Harmonic Numbers*, Fib. Quart. 21(1):18–25 (1983) | **PRIMARY** — classifies unitary harmonic numbers (23 with ω<4, 43 below 10^6); budget/divisibility technique |
| `research/sources/hagis-1987-biunitary-amicable-multiperfect.full.md` | Hagis, *Bi-Unitary Amicable and Multiperfect Numbers*, Fib. Quart. 25(2):144–151 (1987) | **PRIMARY + provenance-critical** — source of `n > 10^102` for unitary MULTIPERFECT numbers |
| `research/sources/cunningham-appendix-c-2n-plus-1.full.md` | Cunningham Appendix C: composite cofactors of `b^n±1`, incl. the `2^n+1` / `2^{4k+2}+1` Aurifeuillean L/M side | **PRIMARY lookup** — first held source for the `+1` side; closes the "Appendix C not held" gap |
| `research/sources/cunningham-pmain901-2n-plus-minus.full.md` | Cunningham main tables, Table 2− (`2^n−1`, odd) newer version | **PRIMARY lookup** — marginal; upgrades held `2^n−1` data, no `+1` content |

All summaries written with fenced claim blocks; sources indexed.

## Key findings

1. **10^102 provenance resolved.** The held Hagis 1987 text contains
   "if n is a unitary multiperfect number, then n > 10^102" (citing Hagis 1984
   Thm 3). So the orphan "10^102" in GOAL/ROOT is a **unitary MULTIPERFECT
   (k≥3 triperfect) lower bound**, NOT a Wall search bound. Wall 1975's actual
   UPN bound is N < W ≈ 1.46e23. New claim `hagis1987-10e102-is-ump-triperfect-bound`
   recorded; CLAIMS.md / CONTEXT updated.

2. **Cunningham `+1` side now in the library.** The branch needs `2^{2p}+1`
   data; previously only `2^n−1` (Table 2−) was held. Appendix C gives the
   `+1`/`L`/`M` composite cofactors, but at 2001-vintage exponents (hundreds to
   thousands) and as unfactored composites only — it is structural-check data,
   not branch closure (open candidates are exponents to ~35000).

3. **Dead end recorded:** Subbarao–Cook–Newberry–Weber 1972 (Delta) PDF is a
   scanned no-text-layer image; download fails. Low value, not needed for the
   branch. Added to REQUESTS.md as OBSTRUCTED.

## Library shape after this cycle

Encyclopedic, canonical-head-tier (Subbarao–Warren 1966, Wall 1975, Graham
1989, Wall 1987/1988), the H_even/branch tier (Maciejewski 2026), the quartic
reciprocity tier (Williams 1976 primary), and now the Fibonacci secondary tier
(Wall 1983, Hagis 1987) plus the Cunningham `+1` cofactor lookup are all held.
Still unobtainable and recorded: Frei 1978, Goto 2007 (pay/captcha-walled).
