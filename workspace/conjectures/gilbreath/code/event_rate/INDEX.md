# Index — code/event_rate

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_survivor.py` | Pattern-finder survivor analysis of event_rate_stats.jsonl: per-family death counts and death-row histograms, f2 vs non-f2 conditioning, survivor-of-row-10 check, surviving-class characterization, corner-mechanism consistency checks (trunc_k / rand24 dichotomy). Pure read of the persisted sweep stats; no row arithmetic. |
| `analyze_sweep.py` | Post-analysis of event_rate_stats.jsonl: death-depth histogram, per-family survival fractions, non-degenerate survivor rates, gap-support phase boundary. Pure read of persisted sweep stats; no row arithmetic. |
| `event_rate_sweep.py` | _(undescribed)_ |
