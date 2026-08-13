# Gilbreath's conjecture — Wikipedia (en), retrieved this run

<!-- source: https://en.wikipedia.org/wiki/Gilbreath%27s_conjecture | full text: sources/wikipedia-gilbreaths-conjecture.full.md -->

Encyclopedic entry: fixes the statement, the names, and the current verification record.
Treats Proth's proof claim with the corrected Chase caveat, and lists the generalisation
landscape the run's general-class side lives in.

## What it establishes

- **Statement and history.** `d_n^k` recursion; `d_1^k = 1` for all k ≥ 1. Gilbreath 1958
  (napkin; presented to the community); Proth 1878 published the same observations. Chase's
  correction: though several sources say Proth released a proof later shown flawed, there is
  no evidence he published a proof at all (only the observation, called a "theorem").
  (Matches the run's `proth-myth-retracted` claim; this is a second, independent source.)
- **Verification record (now current to 1.5×10^15).**
  - Odlyzko 1993: `d_1^k = 1` for `k ≤ 3.4×10^11` via 635 rows whose 635th begins 1 then
    only 0s and 2s (implies the next `n` rows begin 1).
  - Plouffe 2025: verification for primes up to 10^14 (arXiv:2510.06688).
  - Colonna 2025: `G(π(2×10^14)) = 744` (Oct 2025); 2026: up to 1.5×10^15, `G(π(10^15)) =
    800` (Jan 2026).
  - Still open.
- **Croft's generalisation is FALSE.** Gardner 1980 published Croft's conjecture: every
  sequence beginning 2, then only odd numbers, with gaps below a low bound, should have all
  leading terms 1. **Refuted by Eppstein 2011**: for every initial 2-then-odds
  subsequence and every non-constant growth rate there is an odd continuation with gaps
  obeying the growth rate whose leading terms fail to be 1 infinitely often. (This is the
  run's `anti-gilbreath-construction` claim — now triple-sourced: Eppstein's own page, CHT
  2026, Wikipedia.)
- **Odlyzko's caution.** Only heuristic: the arguments "apply to many other sequences in
  which the first element is a 1, the others even, and the gaps not too large and
  *sufficiently random*" — with no formal definition of "sufficiently random" (Chase 2024
  supplies one).
- **Rule 90.** The parts of rows containing only 0 and 2 are governed by the linear
  cellular automaton Rule 90 — the cleanest pointer to why the {0,2} regime self-propagates
  with Pascal-type structure.
- **Chase 2024 bibliographic anchor.** "A random analogue of Gilbreath's conjecture",
  Math. Ann. 388 (2024) 2611–2625, **arXiv:2005.00530**, doi 10.1007/s00208-023-02579-w —
  gives the run the arXiv ID missing from earlier holdings.

## Bearing on this run

- The verification record must be reported as **1.5×10^15 (Colonna 2026)**, with the
  run's own depth-1000 kept strictly separate. The 10^13 figure in earlier notes is
  superseded for "current record" purposes but remains the canonical Odlyzko one.
- General-class side: the correct statement is not "bounded gaps → conjecture" (false via
  Eppstein) but the 2-separation/randomness variant; Odlyzko's "sufficiently random" is
  undefined, and Chase's model is the only rigorous version.
- Rule-90 pointer: the mod-2/Pascal structure the run's `mod4-linearization` claim rests
  on is the same structure Wikipedia names as Rule 90.

## Source status

Wikipedia, retrieved this run (rev 1348550815). Encyclopedic tier: fixes names and record;
theorem-level claims it reports (Eppstein, Odlyzko, Chase) are backed by the primary
sources already in the library. Its 2025–2026 verification entries cite primary arXiv/CNRS
pages, now also in the library.