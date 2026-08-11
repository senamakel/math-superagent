"""Independent check of Eriksson Fig.3 table (folded polyominoes in Z^n, circumference 2k).

OCR'd from research/L0.0/pebbling_ejc_survey.full.md. The digest claims:
  - column n=2 = Catalan numbers C_{k+1}
  - row k=2 = n(3n-1)/2
Both verified by hand arithmetic (no shell available):
  Catalan col: 1,2,5,14,42,132,429 all match C_{k+1}; row k=2: 1,5,12,22,35,51 all match n(3n-1)/2.

This VERIFIES INTERNAL CONSISTENCY (the table is the one the claims describe),
NOT that these are the true folded-polyominoid counts (that is Eriksson's
sourced result, not re-derived here). See scholar report.
"""
