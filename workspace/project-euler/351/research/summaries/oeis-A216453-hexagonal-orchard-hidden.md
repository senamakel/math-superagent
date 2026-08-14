# OEIS A216453 — hidden points in a hexagonal orchard

Source: https://oeis.org/A216453 — full text at
`research/sources/oeis-A216453-hexagonal-orchard-hidden.full.md`
[[oeis-A216453-hexagonal-orchard-hidden.full]]

## What this source establishes

The exact sequence for PE 351:

    a(n) = number of points hidden from the central point by a closer point
           in a hexagonal orchard of order n.
    a(1..30) = 0, 6, 12, 24, 30, 54, 60, 84, 102, 138, 144, 192, 198, 246,
               288, 336, 342, 414, 420, 492, 546, 618, 624, 720, 750, 834,
               888, 984, 990, 1122, ...

**FORMULA (the closed form this run uses):**

    a(n) = 6·(C(n+1, 2) − Σ_{i=1..n} φ(i))     [corrected by Piyush Kumar
                                                and Robert Israel, Aug 2014]
    a(n) = 6·A063985(n)                        [Jon Maiga, Jan 2019]

where C(n+1,2) = n(n+1)/2 and A063985(n) = Σ_{k≤n}(k − φ(k)) is the partial
sums of the cototient.

**Cross-checks against the statement's oracles:**
- a(5) = 30 ✓ (matches H(5) = 30)
- a(10) = 138 ✓ (matches H(10) = 138)
- a(1000) = 6·(1000·1001/2 − Φ(1000)) with Φ(1000) = 304192 gives
  6·(500500 − 304192) = 6·196308 = 1177848 ✓ (matches H(1000) = 1177848)

**OEIS lookup cross-check (this run):** the 20 computed terms
0,6,12,24,30,54,60,84,102,138,144,192,198,246,288,336,342,414,420,492 were
sent to oeis_lookup and matched A216453 exactly — the run's own sieve output
is the sequence, not a read from the catalogue.

## Why it matters here

This is the encyclopedic record tying the geometric definition to the totient
summatory function, and the source of the closed form H(n) = 6·(C(n+1,2) −
Φ(n)). The run's `code/solution.py` reproduces a(n) for every n the brute
force can reach, and the final H(10^8) is a(10^8).

## Claims

```claim
id: hexagonal-orchard-closed-form
statement: For every n ≥ 1, H(n) = 6·(C(n+1,2) − Σ_{k=1..n} φ(k)) = 6·Σ_{k=1..n}(k − φ(k)).
hypotheses: n ≥ 1; H(n) the number of points hidden from the centre in a hexagonal orchard of order n; φ Euler's totient.
holds-here: yes — reproduces H(5)=30, H(10)=138, H(1000)=1177848.
status: checked — solution.py reproduces H(5)=30, H(10)=138, H(1000)=1177848
against the brute-force oracle, and H(10^8)=11762187201804552 against the
catalogued Φ(10^8); general identity sourced from OEIS A216453 (Kumar–Israel
formula); 20 computed terms match the OEIS entry via oeis_lookup.
bearing: reduces the problem to computing Φ(10^8) = Σ_{k≤10^8} φ(k).
anchor: research/summaries/oeis-A216453-hexagonal-orchard-hidden.md
```
