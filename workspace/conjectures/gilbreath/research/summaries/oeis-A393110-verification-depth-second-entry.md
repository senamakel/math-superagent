# OEIS A393110 — G(π(10^n)) verification depth for the Proth-Gilbreath conjecture

Source: https://oeis.org/A393110 (Michel Marcus, Feb 02 2026, keyword hard/more). Full text in the summary.

## What the catalogue records

`a(n) = G(primepi(10^n))`, where `G(k)` is the number of absolute-difference iterations from the first `k` primes until a row appears whose first term is 1 and whose remaining terms are all in `{0,2}` (the "Verification depth" — one row per `{0,2}` entry, matching this run's block profile).

Terms `n = 2..15` (offset 2):
```
5, 15, 35, 65, 95, 135, 175, 248, 329, 417, 481, 635, 693, 800
```

## Reading off the verification record (independent catalogue cross-check)

- `G(π(10^13)) = 635` — **matches Odlyzko 1993** (his reported record).
- `G(π(10^14)) = 693` — **matches Plouffe 2025 / Colonna Oct 2025** (the run quotes G=693 at π(10^14) for Plouffe).
- `G(π(10^15)) = 800` — **matches Colonna 2026** (his G(π(10^15))=800 of 23 Jan 2026).
- The table stops at n=15; Colonna's ongoing run to 1.5×10^15 (G=811 at x≈1.2125×10^15) is not yet reflected here. The catalogue does not contradict any held bound.

## Cross-references

Cf. A000720 (prime-counting), A036262 (iterated prime differences — already held), A006880. This is a catalogue lookup, not a derivation; it independently re-confirms the run's verification-bound numbers. It also lists Delahaye, *Pour la Science* 580 (Feb 2026) "Nouveaux records pour la conjecture de Proth-Gilbreath" as the popularisation of the 2025–26 records.

```claim
id: oeis-A393110-verification-depth
statement: OEIS A393110 gives G(pi(10^n)) = 5,15,35,65,95,135,175,248,329,417,481,635,693,800 for n=2..15, where G(k) is the number of absolute-difference iterations from the first k primes to the first row with leading 1 and rest in {0,2}. Reads G(pi(10^13))=635 (Odlyzko), G(pi(10^14))=693 (Plouffe/Colonna), G(pi(10^15))=800 (Colonna 2026).
hypotheses: G defined as depth-to-{0,2} row; entries from the OEIS catalogue.
holds-here: yes (independent catalogue agreement with held verification bounds; consistent with the run's block-profile data).
status: catalogued (read from OEIS; not derived here) — reproduces the run's verification-bound numbers, so reported as looked up.
bearing: independent confirmation that the run's verification-bound sequence (635, 693, 800) is the published record; a live reference for claims about the current verification depth.
anchor: research/summaries/oeis-A393110-verification-depth-second-entry.md (small catalogue record; full text is this file)
```
