# Eppstein 2011 — Gilbreath made practical (practical numbers)

**Full text:** `research/sources/eppstein-gilbreath-practical-numbers.full.md` [[eppstein-gilbreath-practical-numbers.full]]
**Source:** https://11011110.github.io/blog/2011/02/19/gilbreath-made-practical.html (D. Eppstein), companion to the anti-Gilbreath post.

## What it establishes

Introduces the **Rule-90 cellular-automaton lens** on the {0,2} interior and a **new conjecture for the practical numbers**.

- **Rule 90 identification.** In the prime triangle, the big region of 0s and 2s on the right behaves like the one-dimensional Rule-90 CA (each triangle column is an automaton configuration, time flowing left→right). Rule 90 behaves "as if random" despite being deterministic; so each successive row gets a seemingly-random {0,2} string whose 2s wears down larger values in the next row. (Eppstein gives no proof here — it is a heuristic framing, later formalised by the run's `rule90-identification-real-absorption-refuted` and CHT/Odlyzko's mod-4/Pascal structure.)
- **Practical numbers.** The practical numbers (every fraction < 1 with denominator dividing them is an Egyptian fraction with those denominators) are dense like primes and also have first element parity different from all the rest. The practical-number triangle also has 1s all down the right edge (worked example shown).
- **Conjecture + verification.** Eppstein conjectures the right edge is all 1s for practical numbers, with evidence: **computed first 212,000 rows** (up to practical number 2,314,890), all ending in 1. Heuristic: Rule-90 randomness makes counterexamples increasingly rare, so "if true this far out it seems almost certainly true in general."
- Provides Python source (bit-manipulation Rule-90), noting speedups possible.

## Hypotheses / bearing

- Note the practical numbers don't start (2,3) — they start (1,2,4,6,...) — so they are NOT of the run's canonical "(2, odd, odd, ...)" shape; Eppstein's leading column is 1,2,4 here. It is a separate Gilbreath-like family, marginally relevant as confirmation that the {0,2} regime + Rule-90 recurs in many "prime-like" sequences.
- Bearing: the Rule-90 lens corroborates the mod-2/Pascal structure (Odlyzko, CHT Lemma 3.10, run's mod4-linearization); the 212,000-row practical-verification is a data point in the run's "small-gaps/prime-like sequences are Gilbreath" general-class program.
- It is a heuristic/motivational source; the run's own depth-600 prime check and Odlyzko's rigorous verification dwarf this numerically, and it proves no theorem.

## Claims

```claim
id: eppstein-practical-rule90
statement: (heuristic/conjectural) the {0,2} interior of a Gilbreath triangle evolves as a Rule-90 cellular automaton (per-column, time left→right), which behaves as if random and wears down larger values; the practical-number triangle's right edge was verified all-1 to 212,000 rows (up to 2,314,890).
hypotheses: the {0,2} interior of a Gilbreath-like integer triangle.
holds-here: yes as heuristic; the Rule-90 structure is formalised by Odlyzko/CHT mod-2 parity; the practical-verification is empirical.
status: asserted by source (blog heuristic + a computation); not a theorem.
bearing: motivates the Rule-90/randomness view of the {0,2} regime; adds a second verified prime-like family.
anchor: research/sources/eppstein-gilbreath-practical-numbers.full.md
```
