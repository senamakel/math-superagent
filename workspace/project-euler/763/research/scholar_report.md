# Scholar report — verification pass over the research library

This pass read the full research library against the PE763 goal (D(10000),
3D amoeba = 2N+1-cube reachable-position count) and verified the primary
sources against their full texts. The L1.0 OEIS batch and the run-level
notes were already well-formed; what this pass added was *verification* and
*stale-index repair*.

## What was already correct (no re-summarising needed)

- **L1.0 OEIS batch** (A001006, A005207, A086246, A168049, A007902, oeis_direct,
  oeis_partial) were all complete with claim blocks. They establish the
  negatives: 3D D(N) is NOT in OEIS (two authoritative "No results" queries),
  and is not any Motzkin/Fibonacci-family closed form.
- **A007902 = 2D amoeba** identification, cross-checked against the run's own
  double-BFS-verified 2D values.

## What this pass verified (full text ⇄ digest)

1. **CGMO/Dijkstra** (`research/L2.0/cgmo_opening_dijkstra.md` vs
   `research/L0.0/cgmo_opening_dijkstra.full.md`): Lemma 1 (Kontsevich weight
   invariant 2^{-(i+j)}, L(1)∪L(2)∪L(3) unavoidable), Lemma 2 (Khodulev
   L(1)∪L(2) unavoidable), Lemma 3 (stacking⇔non-stacking), Theorem 1
   (X unavoidable iff after M(X) some cell ≥3 pebbles). All match verbatim.
2. **Zhen–Knessl** (`research/L2.0/pebbling_knessl_pdf.md` vs
   `research/L0.0/pebbling_knessl_pdf.full.md`): G(k,m) recurrence eqs 2.1–2.3,
   Thm 2.1 contour formula, Cor 2.1 (G(k)), Thm 2.2/Cor 2.2 asymptotics
   (z_*≈0.430729593137930, growth 1/z_*≈2.321642), corrected constants
   (c1≈2.02740, c1K*≈0.28777). All match.
3. **Eriksson "Pebblings"** (`research/L2.0/pebbling_ejc_survey.md` vs
   `research/L0.0/pebbling_ejc_survey.full.md`): the pivotal structural source.
   Theorem 9 (n≥3 four-way bijection: reachable positions ⇄ voidance sets ⇄
   folded polyominoids ⇄ labelled vector pairs), Prop 24 (no node fired twice
   in n≥3), Prop 20 (positions⇄shot counts⇄voidance sets), Prop 1
   (origin+3 neighbours unavoidable in Z^n, n≥3), Theorem 10 (2D crossings),
   Fig. 3 table.
   **Fig. 3 verified by hand:** column n=2 equals Catalan C_{k+1}
   (1,2,5,14,42,132,429) and row k=2 equals n(3n−1)/2 (1,5,12,22,35,51) — both
   check exactly (see `code/check_eriksson_fig3.py`). This confirms internal
   consistency of the OCR'd table.

## Contradiction / flag findings

- **Stale indexes (fixed):** `research/INDEX.md` and `research/L2.0/INDEX.md`
  still labelled the three primary-source digests (cgmo, amz, ejc_survey,
  knessl_pdf) and oeis_a007902 as "STILL A PLACEHOLDER / not yet summarized".
  This was wrong — the digests were complete and faithful. Fixed all rows;
  indexes now agree with disk (calls to `search_workspace` confirmed).
- **No contradiction with MEMORY.md.** The A007902=2D match and the BFS
  D(0..14) values are untouched and confirmed. Nothing in the primary sources
  contradicts the run's numbers.
- The two structural claims (`n3-folded-polyominoid-voidance`,
  `d2-positions-are-polyominoid-voidance`) were marked `holds-here: unchecked`
  in the claims ledger because a trailing explanation after "yes" broke the
  parser; cleaned to `holds-here: yes` and re-derived. Their hypotheses are
  exactly PE763's rules (≤1 pebble/cell, n children per split), so `yes` is
  correct — the 3D D(N) IS an Eriksson n=3 folded-polyominoid count.

## Bearing on the goal

- The correct counting object for 3D D(N) is now named and sourced (folded
  3-labelled polyominoids), and the 2D machinery (G(k,m) recurrence) is the
  transfer model to lift. But **no source hands over the numeric D(10000)**:
  not in OEIS, and neither CGMO/Zhen-Knessl (2D-only) nor Eriksson (names the
  object, gives only a small-N Fig.3 table) provide a 3D recurrence. The
  numeric answer must be derived in the run.
- New thread opened: `research/threads/lift_gkm_to_3d.md` — derive the 3D
  G(k,m)-style recurrence from the level-histogram / voidance-set structure
  (data/level_N.txt).

## Still lacking

A 3D structural recurrence / DP that reaches N=10000 and reproduces D(14)
and the worked examples (D(20)=9204559704, last 9 of D(100)=780166455).
