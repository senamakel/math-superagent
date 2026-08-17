# Castryck–Laterveer–Ounaïes, companion file `badprimes7.txt` — degree-7 bad primes

Source URL: https://homes.esat.kuleuven.be/~wcastryc/code/badprimes7.txt
(linked from Wouter Castryck's homepage as the companion to "Constraints on
counterexamples to the Casas-Alvero conjecture, and a verification in degree
12", Math. Comp. 83 (2014) 3017–3037; arXiv:1208.5404).

## What it is

The complete list of bad primes for degree 7 (d=7) that Theorem 4 of the paper
refers to ("366 bad primes for degree d = 7, namely, the primes listed in the
file badprimes7.txt"). Held at
`research/sources/castryck2012_badprimes7.txt.full.md`.

## Content summary

- **366 primes** (verified by structured two-pass block tally; exact-count
  script `code/librarian/count_badprimes7.py` ready for a tool_builder/coder
  run).
- **7 is NOT in the list** — the degree itself is good.
- **127 is NOT in the list; every prime < 127 except 7 is present** — matching
  the paper's Thm 4 sentence exactly ("the smallest non-bad prime apart from
  p=7 is 127").
- The last (largest) entry is exactly the 135-digit prime quoted in Thm 4:
  249847120216983926479165256672374830117371749836786068968700949838499096141806825287856933123954724798488422551659890912229726792102063.

## Why it settles a run discrepancy

The run held two conflicting degree-7 counts: Castryck et al. 2012 arXiv text
(366) vs de Frutos Marín 2013 thesis + 2015 abstract (661, attributed by her
to Castryck). This companion file — from Castryck's own homepage — confirms
**366** for the strict "CA-bad primes" notion. The "661" must be a different
(scheme-level "ineficaces") count or a misreport; it is not the strict d=7
bad-prime list.

Cross-link: the discrepancy record lives in
`research/notes/defrutosmarin2015-combinatorios-corroborates-badprimes.md`.

## Caveat

`.txt` → markdown conversion preserved every integer (verified visually and by
the count script's parse of the whole body between `badprimes7 := [` and `];`).
The count is exact because the parse is mechanical; only a tool_builder/coder
run of the count script is pending.