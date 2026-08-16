# K*(n) measured table — n = 4..20

Files the measured correlation-order budget table as a claim, so the weakened
rung `R-kstar-measured-n20` (research/weakened/supply-order-k.md) has a named
establishing claim. The table is imported from the dedicated collapse run
(`workspace/conjectures/gilbreath-collapse`, `2628fcfb`), not re-derived with
this workspace's canonical oracle.

```claim
id: kstar-n20-measured-table
statement: For n = 4..20, K*(n) := min{K ≥ 1 : S² is constant on every C_K-fiber of F₂ⁿ} takes the values n=4→2, 5→2, 6→3, 7→4, 8→4, 9→5, 10→5, 11→6, 12→6, 13→7, 14→7, 15→8, 16→8, 17→9, 18→9, 19→10, 20→10. Equivalently K*(n) = ⌈n/2⌉ for every n in 4..20 EXCEPT n=5, where K*(5)=2 ≠ ⌈5/2⌉=3, and K*(n)=1 for the degenerate n=2,3. In particular the budget reaches ⌈n/2⌉=10 at n=20, far past the K=1 that the eight first-pass routes were confined to.
hypotheses: canonical floored fold, d∈[2,n−1]; S(n)=(n−2)−2ν₂(n) the signed fold excess (claim excess-is-negative-character-sum), so S² and ν₂ have identical fibers; C_K(h) the empirical (K+1)-gram count vector of h.
holds-here: yes — pure combinatorics of Φ_n over F₂ⁿ, no primes, no arithmetic.
status: measured (imported) — NOT proved. Table from research/witness-hunt-n20-imported.txt; the n=4..12 range is independently re-checked by research/witness-crosscheck-imported.txt, which flags the SAME n=5 mismatch (claim ⌈5/2⌉=3, found 2) rather than smoothing it. The n=5 exception is unexplained; the closed form K*(n)=⌈n/2⌉ is a hypothesis on this evidence, not a theorem.
bearing: pins GOAL.md priority 3's budget to n=20 with a known exception; the exception is the natural first test of any structural (non-2^n-enumerating) argument that extends the table, which is exactly the next rung R-kstar-beat-exhaustion. It is the quantitative backing for "the eight collapses were a property of the eight routes, not a law about Φ".
anchor: research/witness-hunt-n20-imported.txt (primary table); research/witness-crosscheck-imported.txt (independent n=4..12 crosscheck); research/REOPENED.md (the ⌈n/2⌉ reading and the n=5 flag).
```
