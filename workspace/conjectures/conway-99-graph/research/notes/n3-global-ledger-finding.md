# n3 seed global incidence ledger — finding

## Question (thread n3-forced, goal G-n3-positive, solution.md §7)

Does the n3 seed (a 2-edge-joined disjoint triangle pair, the configuration
whose existence Makhnev 1988 Thm 2 leaves open) pin forced lines/incidences
that OVER-SUBSCRIBE the fixed global budget of the partial Steiner triple
system of a putative srg(99,14,1,2)?  Budget: 99 points, 231 lines (99·7/3),
693 point-line incidences (99·7), 7 lines per point.

## Method (the k=14-specific structural step)

Grow the seed to a lambda-witness fixpoint (every adjacent pair with 0 interior
common neighbours gains a fresh witness adjacent to both, the ONLY growth rule
— sound), enumerate all interior completions under the SOUND upper-bound
criterion (adjacent ≤1 CN, non-adjacent ≤2, locally-7K2, degree ≤14; only
excesses are contradictions), reaching a stable fixpoint with 19 fully-decided
survivors (0 free interior bits).  Then the forced line/incidence ledger is
EXACT:

- lambda=1 ⇒ every graph edge lies in exactly one line (triangle).
- At the fixpoint every inside edge has exactly one common neighbour, which by
  7K2 is its matching partner in N(v).
- Hence |I(v)| is even for every v and equals 2·(patch 3-cliques through v), so
  every line through a patch vertex is either FULLY inside (counted as a
  3-clique) or has BOTH other points outside.  No line has exactly one patch
  partner.

## Numbers (all 19 radius-6 survivors consistent)

- patch sizes {8,9,10,11,12}; all fully decided; max lines through any vertex = 3.
- forced lines L_in = #patch 3-cliques: **min 4, max 8**.
- forced incidences = 3·L_in: **min 12, max 24**.
- residual lines 231−L_in: **223 .. 227**; residual incidences 693−3L_in: **669 .. 681**.
- every patch vertex has even |I(v)|, ≤3 patch lines (≤7 budget), nonneg deficit.
- independent parity check: |I(v)| = 2·tris_through(v) for ALL 210 patch
  vertices across the 19 survivors (code/out/verify_global_ledger_parity.txt).
- residual identity: per-vertex deficits sum to 7·|patch|−3·L_in, and +7·(99−|patch|)
  outside = 693−3L_in exactly, always saturated by construction.

## Verdict (honest)

**NO forcing floor over-subscribes.**  The residual is arithmetically absorbable
by the ~87-91 outside points; every patch vertex's line deficit is small and
nonnegative.  So a counting floor at this seed CANNOT overflow: if an
obstruction to srg(99,14,1,2) exists, it is GENUINELY cross-patch / global
(structural), not a local forced-line/incidence over-subscription of this
closure.  This confirms the local runs' suggestion (the obstruction, if real,
is global/structural), and it isolates the gap further.

## Files

- `code/lib/n3patch.py` — single home of the n3 seed, sound growth/closure,
  upper-bound oracle, patch_cliques/forced_ledger (third-copy dedup).
- `code/out/n3_global_ledger.py` → `code/out/n3_global_ledger.captured.txt`.
- `code/out/verify_global_ledger_parity.py` → `code/out/verify_global_ledger_parity.txt`.
