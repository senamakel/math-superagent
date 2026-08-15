# OEIS A080839 — increasing sequences with all-1s Gilbreath transform

Source held in full: `research/sources/oeis-A080839-increasing-sequences-gilbreath-property.full.md` (from https://oeis.org/A080839; this summary note and the source full text were corrected this cycle — the download was initially routed under this summary name; the clean full text is now filed under sources/). Surfaced by the MathOverflow "what is known" thread (Directive 47) — commenter tdnoe: "The question of how many increasing sequences of integers have the Gilbreath property is answered in OEIS A080839. It doesn't make the primes seem that special."

## What the catalogue says (catalogue-read, not derived here)

a(n) = number of positive increasing integer sequences of length n whose Gilbreath transform (the diagonal of leading successive absolute differences) is (1,1,1,...). Terms: `1, 1, 1, 2, 6, 27, 180, 1786, 26094, 559127, 17535396, 804131875, 53833201737` (n=1..13).

- Slowest-growing length-n sequence: `1,2,4,6,...,2(n-1)`. Fastest: `1,2,4,8,...,2^(n-1)`.
- a(n+1)a(n-1)/a(n)^2 → ~1.46 (≈ growth rate of A001609; relation unproved).
- a(n) also = number of (not necessarily increasing) positive integer sequences of length n-1 with Gilbreath transform (1,...,1) (von Brömssen).
- Cross-references: A136465 (total number of increasing sequences of the same max length), A036262 (iterated prime differences), A363002..A363005.
- Cites Muney 2026 (arXiv:2606.23721), p.28 Sect 14.1 — the valid-extension-set paper already held.

## Why it matters to the run

It is a catalogue statement of the *general-class counting* side, which is the run's side: it counts how many increasing sequences (not just primes) have the all-1 Gilbreath property, at each finite length. It does NOT say the primes are rare (tdnoe's "doesn't make the primes seem special" vs Charles's "still rare; A080839 small compared to A136465"). It is evidence about the *shape* of the class, not a theorem the run is building on. Load-bearing relevance is low; it corroborates the general-class framing already in ROOT.md and adds no new proof route.

```claim
id: oeis-A080839-increasing-sequences-all-1-transform
statement: a(n) = number of positive increasing integer sequences of length n whose Gilbreath transform is (1,1,1,...); terms 1,1,1,2,6,27,180,1786,...; fastest growing is 1,2,4,...,2^(n-1).
hypotheses: count of finite increasing positive sequences with all-leading-ones diagonal.
holds-here: yes (a catalogued statement about the general Gilbreath-like class the run works on; consistent with, not load-bearing on, the run's reduction).
status: catalogued (OEIS read; an oracle reproducing the first terms by brute force is written at code/out/reproduce_A080839.py but NOT yet executed — the terms are catalogue-read, not run-reproduced).
bearing: supports the general-class framing (the property is not prime-specific); the fastest-growing sequence bound 2^(n-1) bounds any brute-force enumeration of the class.
anchor: research/sources/oeis-A080839-increasing-sequences-gilbreath-property.full.md + code/out/reproduce_A080839.py
```

The oracle bound: because the fastest-growing all-1s sequence of length n ends at 2^(n-1), every counted sequence has last element ≤ 2^(n-1), so a(n) is brute-forceable by enumerating strictly increasing (1, rest) tuples with rest ⊆ {2..2^(n-1)}.
