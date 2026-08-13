# Keith Conrad — Wieferich primes

**Source:** https://kconrad.math.uconn.edu/blurbs/ugradnumthy/wieferich-primes.pdf (undergraduate number theory notes).

## What it records (background for the Dupuy–Weirich / sparse-bit direction)

- A base-2 Wieferich prime is p with 2^(p−1) ≡ 1 (mod p^2). The only known ones are p = 1093 (Meissner 1913) and 3511 (Beegner 1922); searched to p < 1.25×10^15.
- Base 3: known Wieferich primes to base 3 are 11 and 1006003 (searched to 2^32).
- Wieferich primes are central to digit-uniformity results for a^n in base b: Dupuy–Weirich's theorem on the asymptotic equidistribution of binary digits of 3^n is conditional on an effective "no large Wieferich prime" / non-Wieferich framework.
- The heuristic: base-a Wieferich primes are rare but conjecturally infinite.

## Claims
```claim
id: CONRAD-W
statement: The only known base-2 Wieferich primes are 1093 and 3511; the only known base-3 ones are 11 and 1006003; the searches cover p < 1.25·10^15 (base 2) and p < 2^32 (base 3).
hypotheses: none.
holds-here: context only — the Wieferich obstruction explains why digit-uniformity results for powers are hard to make unconditional.
status: asserted-by-source (canonical survey notes)
bearing: if the run's middle-digit argument needs equidistribution of digits of 2^n in base 3, it will collide with the same Wieferich/non-recurrence obstruction Dupuy–Weirich face for 3^n in base 2.
anchor: research/sources/conrad-wieferich-primes.md
```