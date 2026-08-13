# Surplus renewal structure — claim record

Companion claim record for the full writeup
`code/out/surplus_renewal_structure.md` (same result, same run, same runs
against `code/out/blocks_depth1000.json`, depth 1000, sieve 2e7, 1,270,607
primes). The full writeup holds the derivation, the delta law, the renewal
table in `code/out/surplus_renewal_table.captured.txt`, and the independent
recomputation in `code/out/surplus_structure_independent.captured.txt`.

```claim
id: surplus-renewal-structure-1000
statement: For the prime Gilbreath rows to depth 1000 (sieve 2e7, 1270607 primes), with b_k the leading {0,2} block length and S_k = b_k - b_1 + (k-1) the recharge surplus, S_{k+1} - S_k = (b_{k+1} - b_k) + 1 at every transition (delta law); S_k is monotone nondecreasing and strictly increases exactly at the 60 (2,4)-events (17 of them jump-0 stalls); S_k >= N_k (events so far) at every k; S_1000 = 1270603 vs required k-2 = 998, margin 1269605; log(jump) vs log(b) OLS slope 0.388 over 43 positive-jump events. Conjecture-equivalent reformulation: GC holds for the primes iff S_k >= k - b_1 for all k, i.e. block length never reaches zero iff erosion never overtakes the recharged surplus.
hypotheses: rows are iterated absolute differences of primes below 2e7, block length measured from position 1, depth 1000
holds-here: yes (depth 1000, exact)
status: checked
bearing: the monotone surplus S_k is the quantity whose unboundedness of (k-1) - S_k is the conjecture; converts regeneration into "S_k - (k-1) is bounded above by b_1", and shows regeneration events (incl. stalls) are the only increments. Does not bound the event rate — that is open and is the next step (TASKS.md item 1).
anchor: code/out/surplus_renewal_structure.notes.md
```