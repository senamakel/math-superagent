# Finding A reconciliation — survives the corrected comparison (pattern_finder)

## Background

CONTEXT.md's Contradictions section flagged `research/patterns/
open_degree_complement_and_sequences.md` §A (Finding A: the published
open-degree list <= 100 equals the settled `m·p^k`-family complement with
anomalies n=96 and n=98) as **unsound until re-derived**, on the suspicion that
the open-degree script's comparison was inverted (`pub != cov` instead of
`pub == cov`).

## Reconciliation (this pass)

I re-ran both on-disk harnesses in this session and independently read the
primary source; all agree that Finding A SURVIVES the corrected comparison and
the anomaly set is genuinely exactly {96, 98}.

1. `scenario/verify_open_degrees_check.py` — corrected comparison
   (genuine mismatch iff `pub_open(n) == covered(n)`), negative controls
   16/20/28 all on the consistent side, old-buggy comparison falsely flags all
   89.
   → GENUINE mismatches: **[96, 98]** (exactly two).

2. `scenario/full_coverage_reconcile.py` — FULL m<=7 coverage (including 6·p^k
   with the 53 degree-6 bad primes, and 7·p^k with the 127-bound).
   → Only inconsistent degrees: **[96, 98]** (exactly two).
     - 98 = 2·7² : covered by 2·p^k (Graf-von-Bothmer 2007, no exclusions) but
       LISTED open → settled-but-listed-open.
     - 96 = 6·16 = 3·32 : both need p=2, which is BAD for degree 6 and for
       degree 3 → genuinely open, yet absent from the published list →
       open-but-unlisted.

3. **Independent source confirmation (new this pass):** read directly from
   castryck2012_degree12_html.full.md, the degree-6 bad-prime Table 1
   begins with **2, 5, 7, 11, 13, 19, ...** — i.e. `p=2` is the first entry.
   This is the fact `full_coverage_reconcile.py` had hardcoded in its 53-prime
   exclusion set; I verified the source actually lists 2. So 96 = 6·2⁴ genuinely
   has its base prime banned, and is open for exactly the same structural reason
   as 20, 24, 28, ... (base prime is a bad prime for the multiplier).

## Verdict

Finding A's conclusion is correct and re-derived under the correct comparison:
the published open-degree list is a pure `m·p^k`-complement object, and the two
boundary anomalies are 98 (settled-but-listed-open, a likely 2012-list
oversight) and 96 (open-but-unlisted, a likely omission). The two are of
opposite kinds. This resolves the CONTEXT.md unsoundness note in the direction
of *survives*.

## Status

- All integer comparisons here are exact integer/set arithmetic (sympy factorint
  only for prime-power detection; no floats).
- The underlying settled-family facts are sourced: Graf-von-Bothmer 2007 (2·p^k,
  p^k), Draisma–de Jong (3·p^k), bad-prime lists (Castryck 2012), d=12 (Castryck
  2012, eq 6.5 for the open list).
- Conjectural part, unchanged: whether the 2012 list's inclusion of 98 and
  omission of 96 are literally errors (they cannot be settled by arithmetic).
