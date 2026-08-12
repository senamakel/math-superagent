# Index — code/pattern_finder

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `census_c16_profile.py` | Computes the C16 cycle-profile of the Apollonian K4-triangle-expansion family (n=4..22): per level, total / avoidsC4 / avoidsC4C8 / avoidsC4C16 / avoidsC4C8C16, by exact bounded-DSF cycle-existence on the saved canon graph6 classes. Verify: avoidsC4 reproduces census 1,1,2,5,15,50,202 exactly. Finding: avoidsC4C16 = 1,1,2,0,0,0,0,0 (n=10..24) — every C4-free member at n>=16 contains a C16. (Re-verified over the on-disk canon files on a fresh run; earlier "1,1,2,2,..." was a typo.) |
| `falsifiers_check.py` | States the concrete falsifier of the NO4 growth law (NO4(18) departing from ~834M) and confirms the avoidsC4 sequence is a closed direction (no OEIS, no recurrence, rational fit refuted by integrality). |
| `level24_c16.py` | Runs the same C16-profile over level_24_classes.txt (58713 classes). Verify: avoidsC4=807, avoidsC4C8=1 (Markström). Finding: avoidsC4C16=0 at n=24 too — the unique C4,C8-free member still has a C16, so avoidsC4C8C16=0 for all n<=24. |
| `no4_growth_check.py` | _(undescribed)_ |
