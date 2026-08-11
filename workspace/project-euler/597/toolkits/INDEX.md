# Index — toolkits

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `pattern_parity.py` | Structural classification of bump-edge patterns: `parity_from_edges(n, edges)` reconstructs the new order, parity, and transitive chain-pair count from a bump-edge set alone (no dynamics), and `race_observed_patterns` collects which edge-sets the real race reaches for small n. Used to verify parity == (#chain pairs) mod 2 and to see which patterns are even/odd. |
| `race_events.py` | Single callable race_events(n,L,speeds) that replays the PE 597 chronological dynamics and returns parity, chronological bump edges, finishes, the bump-chain count, and the new ascending order. Parity independently recomputed via brute.parity_of_new_order; chain count from the reachability `above` sets. |
| `race_outcome.py` | PE 597 brute-force oracle: outcome_parity(n,L,speeds)->parity, the reference every exact method and MC is checked against; wraps fixed brute.py (full-reachability above). |
