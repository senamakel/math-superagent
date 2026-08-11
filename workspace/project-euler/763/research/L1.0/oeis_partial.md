# Direct OEIS search — partial (offset-1) 11-term amoeba sequence

Source: https://oeis.org/search?q=1,3,9,30,99,336,1134,3855,13086,44499&fmt=text (converted plain text)

## What it establishes

The direct OEIS search for the offset-1 11-term partial sequence
1,3,9,30,99,336,1134,3855,13086,44499 returns exactly **"No results."**
Second authoritative negative against any catalogued entry for D(N).

## Bearing on D(N)

Independently confirms the full-sequence negative (oeis_direct): even the
shorter, offset variant of the head of D(N) is not in OEIS. Removes the
possibility that the full run of terms was failing to match only because
of an offset mismatch. No catalogued recurrence or formula exists.

```claim
id: dN-offset-also-not-in-oeis
statement: The offset-1 partial sequence 1,3,9,30,...,44499 also returns "No results" from OEIS, confirming D(N) is absent regardless of offset.
hypotheses: partial terms as BFS-verified
holds-here: yes
status: asserted (OEIS search result)
bearing: strengthens the negative; the lookup route is closed both ways
anchor: research/L1.0/oeis_partial.md
```
