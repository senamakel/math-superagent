# Fig3 internal-consistency check

Manual verification note for the Eriksson Fig.3 folded-polyominoid table
(OCR'd in `research/L0.0/pebbling_ejc_survey.full.md`).

Two structural checks were performed by hand arithmetic (no shell tool was
available in this run, so `check_eriksson_fig3.py` is a recorded verification
script rather than a executed run):

1. **Column n=2 = Catalan C_{k+1} = 1/(k+2)·C(2k+2,k+1):** k=0..6 gives
   1,2,5,14,42,132,429 — all match the table's n=2 column exactly.
2. **Row k=2 = n(3n−1)/2:** n=1..6 gives 1,5,12,22,35,51 — all match.

This confirms the OCR'd table is the one the cited formulas describe
(internal consistency). It does NOT re-derive the true folded-polyominoid
counts (those are Eriksson's sourced results).

See `research/scholar_report.md` and `research/ROOT.md`.
