# Pattern-finder report — round 27: Paley(9) pattern verified exactly on BvLS (first check of Keramatipour Lemma 3.4.1)

## What I did

1. Verified no artifact on disk postdates report26 except the derived-ledger
   re-renders AND `code/out/paley9_pattern_check.py` (01:08), which had been
   written but **never executed** — its only reference in commands.log is a
   `find` listing, and it has no `.captured.txt`. Its docstring says it was
   built to "refute or confirm Keramatipour Lemma 3.4.1: the Paley(9) pattern
   is present in the Berlekamp-van Lint-Seidel graph srg(243,22,1,2)".

2. Running the original script reproduces the reason it was never captured: it
   crashes on `RuntimeError: v=0: matching has 11 edges, need 7` — the check
   hardcodes the k=14 local structure (7K2), but BvLS has k=22, so its
   neighbourhood matching has 11 edges. The crash was captured to
   `code/out/paley9_pattern_check.captured.txt`.

3. Wrote the corrected check `code/out/paley9_pattern_check_fixed.py`: the
   matching size is read from the graph (k/2), and for every vertex v and every
   pair of matching edges, the 9 vertices
   `{v, v1,v2,v3,v4, (v1,v3), (v1,v4), (v2,v3), (v2,v4)}` (with (a,b) the
   unique non-v common neighbour of the non-adjacent a,b, well-defined by mu=2)
   are induced and tested by `lib.srg.is_srg` against (9,4,1,2) — exact integer
   arithmetic throughout, no floats.

## The result (checked, exact)

- rook(3) = srg(9,4,1,2): 9 configurations (9 vertices × C(2,2)=1 pair),
  **ALL are Paley(9)**.
- BvLS = srg(243,22,1,2): 13365 configurations (243 × C(11,2)=55),
  **ALL are Paley(9)**.

So **Keramatipour Lemma 3.4.1 is CONFIRMED by exact exhaustive computation on
the actual BvLS adjacency matrix** — previously asserted-by-source, claim
`keramatipour-no-paley9-pattern-99` had `Holds here: unchecked`. The
verification covers the lemma's BvLS-side. Theorem 3.4.2 (a putative 99-graph
cannot follow the Paley(9) pattern) remains asserted-by-source: my check
validates the lemma its proof claims, not the forcing argument itself, whose
99-side is uncheckable without a 99 graph (conditional).

## Sequence tools on the extracted counts

- Per-vertex config count over the five feasible members (k=4,14,22,112,994):
  `[1, 21, 55, 1540, 123256]` = `C(k/2,2) = k(k-2)/8` (verified: closed form
  equals C(k/2,2) at all five k; BvLS total 243×55 = 13365 matches the measured
  count exactly). Not a low-degree polynomial in the index, no
  constant-coefficient recurrence of order ≤ 4, **OEIS: no match** (recorded in
  `research/notes/oeis-miss-paley-pattern-config-counts.md`). This is the same
  anticipated structure as every other family count (a=2u+1 | 63-governed
  quartic), so it does not separate 99 from the controls — the value at 99
  (2079) is a conditional count, not evidence.
- A `[1,2,4,7,11,16]` term list I drafted by hand to probe `analyze_sequence`
  has no provenance on disk and is NOT reported as a finding.

## What would falsify

The next term for the config-count sequence would be at k=6426 (u=64,
a=129 ∤ 63) — NOT a feasible member, so no 6th family term exists. The BvLS
verification is a complete enumeration (13365/13365), not a sampled claim: a
falsifier would be one BvLS configuration failing `is_srg` — none exists.
Theorem 3.4.2's 99-side is conditional (needs a 99 graph to test).

## Verdict

One genuinely new checked result this round (Lemma 3.4.1 upgraded from
asserted to checked), plus the OEIS miss for its count sequence. Everything else
on disk is unchanged since round 26; no other untooled sequence exists. The
structural content of the finding for the 99 problem: the Paley(9) pattern is a
real local structure shared by all existing (1,2)-members with k ≥ 6
(well-defined and verified at k=22); a 99-argument forbidding it (Theorem
3.4.2's route) must fail on the qualification — it cannot be an eigenvalue or
counting argument, which survive on both controls; the thesis's own forcing
proof is the thing to verify next if the run picks this route up.

## Files
- `code/out/paley9_pattern_check_fixed.py` (corrected checker)
- `code/out/paley9_pattern_check_fixed.captured.txt` (output: ALL pass)
- `code/out/paley9_pattern_check.captured.txt` (crash traceback of the original)
- `research/notes/oeis-miss-paley-pattern-config-counts.md` (OEIS miss)
- This report (`pattern_finder_report27.md`).