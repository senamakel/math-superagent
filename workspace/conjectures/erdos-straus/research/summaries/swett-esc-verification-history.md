# Swett, "Current Research on ESC" (1999, rev. 10/28/99)

Source: http://math.uindy.edu/swett/esc.htm (original 404), obtained via
Wayback: https://web.archive.org/web/20060803103919/http://math.uindy.edu/swett/esc.htm
Full text: `research/sources/swett-esc-verification-history.full.md`

## What it establishes (sourced, primary)

- **Verification bound `10^14` (1999)**: ESC(n) is true for all integers
  `1 < n <= 10^14`. Method: a set of "filters" S(n) (residue classes mod n for
  which ESC is known true); a C++ program filters the first 100.8 trillion
  integers using two lemmas and filters S(n) for n = 1..1000.
  - Lemma 1: if k > 0 shares a nontrivial gcd with some m < 4000 then ESC(k)
    is true.
  - Lemma 2: if the least residue of k mod 840 is not in
    {1,121,169,289,361,529} then ESC(k) is true.
  - Lemma 4: if ESC(n) holds then ESC(m) holds for every multiple m of n
    (the prime reduction, in Swett's own words).
- After filtering, 7132 candidate cases remain (100 data files); Mathematica
  identifies 3209 primes among them; a greedy search confirms ESC for all 3209
  primes. Hence the bound 10^14.

## Consequence

Confirms the six-residue residual set from the computational side (Swett's
choice of the mod-840 filter), and provides the 1999 bound in the verification
chain Straus ≤5000 → ... → Swett 10^14 (1999) → 2×10^14 (2012) → Salez 10^17
(2014) → Mihnea–Dumitru 10^18 (2025).

```claim
id: swett-1e14
statement: ESC(n) holds for all integers 1 < n <= 10^14 (Swett 1999; sieve over a filter set S(n), n<=1000, plus two lemmas and greedy verification of 3209 residual primes).
hypotheses: none (computational verification).
holds-here: true — recorded step in the verification chain; subsumed by 10^18.
status: sourced (Swett's 1999 page via Wayback; computational).
bearing: verification-history anchor; nobody should re-verify below this bound.
anchor: research/sources/swett-esc-verification-history.full.md
```