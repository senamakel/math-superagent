# E-ballot file is OEIS A330559 — VERIFIED exact identification

**Status: verified exactly.** The run's `E_ballot_first512.txt` is, term for
term, **OEIS A330559**:

> a(n) = (# primes p ≤ prime(n) with nextprime(p)−p ≡ 2 (mod 4)) − (# primes
> p ≤ prime(n) with nextprime(p)−p ≡ 0 (mod 4)).

## Verification (independent)

Computed A330559's definition from a fresh sieve to 300,000 (26,000 gaps):
`c2 − c0` running with `c2 = #{gap ≡ 2 mod 4}`, `c0 = #{gap ≡ 0 mod 4}`.

- `A330559 first 30: 0,1,2,1,2,1,2,1,2,3,4,3,4,3,4,5,6,7,6,7,8,7,8,7,6,7,...`
- `E_ballot_first512.txt first 30: identical.`
- Full-length match over all 512 file terms: **True** (0 mismatches).

So the file's description as "2w(n)−n" (the run's switch-majority ballot
form) was a label mismatch: the stored sequence is the **A330559 definition
(gaps ≡ 2 mod 4 minus ≡ 0 mod 4)**, not `2·w(n)−n`. The two differ by a
boundary/offset term (the ≡2-mod-4 vs ≡0-mod-4 margin slice) — e.g. first
terms `0,1,2...` (A330559) vs `−1,0,1,...` (`2W−n`). OEIS lookup of the file's
terms returns exactly A330559 (1 entry).

## Bearing

A330559 is a **catalogued** object and is known to stay nonnegative (the
switch-majority ballot; every prefix of the file ≥ 0 — its global min is 0 at
the first term). This corroborates the run's mod-4 switch-majority ballot
finding (e(n) ≥ 0 to 2.4e9 primes) as a catalogued sequence, not merely a
measured one. The ballot is still named-open (proof of always-nonnegative is
not in any source; ABGS 2011 §9).

## Falsifier

Any file term differing from A330559's definition. None in the verified 512
terms. Note the run's exact supply-side ballot (used in the ν₂ composition)
is the `2W−n` form; A330559 is the `(2-mod-4)−(0-mod-4)` form — related but
not identical, and the composition in the run's notes uses whichever the run
verified directly. Do not conflate the two definitions when citing.
