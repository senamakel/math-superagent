# Librarian report — third pass

## State of the library

Two prior passes built and verified a mature local reference set; this pass's
librarian work was **audit + gap-check, then the two concrete items below** —
not a refill (the library meets the phase-1 test in `research/ROOT.md`).

**On disk (unchanged this pass, all indexed and searchable):**
- ~52 full texts in `research/sources/`, each with its source URL on line 1.
  Canonical tier present for every live line: the parity barrier
  (Ash–Beltis–Gross–Sinnott 2011, Lemke Oliver–Soundararajan 2016,
  Granville–Martin, Rubinstein–Sarnak), the equal-residue/door-3 side
  (Shiu-2000 expository, Maynard, Banks–Freiberg–TBT, Freiberg), the fold Φ
  (Pascal-mod-2/Rule-90/Lucas-submask: Meštrović, Hofer, Bacher,
  Allouche–Shallit I & II, Rampersad–Wiebe, Steinhaus triangles, Rowland,
  Szechtman), the Walsh/Krawtchouk/MacWilliams/Delsarte tier (macwilliams_1963,
  guruswami_macwilliams_lp_notes, odonnell, wikipedia_krawtchouk), the ergodic
  Lucas-mixing tier (Pivato–Yassawi, Pivato, Takei), direct prior work on the
  exact object (Odlyzko 1993, Chase 2022), and the higher-order K>1 tier
  (Lacasa, Wu).
- ~72 digests in `research/summaries/`, feeding `research/CLAIMS.md`.

**Gap check / search gate:** the only open request, `walsh-spectral-subset-b904`
(a Walsh/subset-sum lower bound on `wt(Φ_n x)` for inputs not "complicated" in
the five refuted senses), is a **theorem to be found, not a source** — nothing
to download. The search freeze (directive 7/27/30) holds: no new search or
download is justified by a stated gap. I did not violate it.

## What this pass added

1. **OEIS lookup (my one phrasing-free tool).** The threshold-weight sequence
   `w*(n) = 3,3,3,4,3,5,7,11,16,24,35,52,77,…` (and its n=8..2^18 extension) is
   **not in the OEIS** — no closed form will be looked up; the sublinear
   structure must come from the problem. Recorded: `research/notes/
   oeis_threshold_weight_not_catalogued.md` + Cognee. Nobody should re-search.

2. **Applied directive 45 (which reaches my run directly).** It asked to test
   whether the threshold-weight exponent is `1/2` (the operator's revised
   hypothesis after the extended data). I hold no execution tool, so the
   mechanical run is coder's, but the decisive flatness test is exact small
   integers and I did it by hand:
   - `w/sqrt(n)` over n=64..32768: `0.875, 0.972, 1.000, 1.061, 1.094, 1.149,
     1.203, 1.237, 1.281, 1.320` — **monotonically rising ~51%**, which is the
     signature of an exponent strictly above 1/2. **`1/2` is rejected**, not
     "in range."
   - Companions: `w/(sqrt·ln n)` falls ~40%, `w/n^log_4(3)` falls ~76%,
     `w/n^0.55` rises only ~10% (the flat column). Agrees with the on-disk
     fitted `E = 0.55678 ± 0.00225` (n≥256) and per-doubling slopes ~0.55.
   - **Honest claim: "about n^0.55 switches suffice" — sublinear, strictly
     weaker than a positive fraction, the strongest affirmative the workspace
     has** — but *fitted*, not a closed form; `1/2`, `sqrt·log`, and
     `log_4(3)` are each rejected by this data; the genericity gap ("typical is
     not the primes' own string") is untouched.
   - Owed machine confirmation: `code/out/librarian_directive45_discriminate.py`
     (coder, via `lib.capture`). I did **not** declare a closed form the data
     cannot separate.

3. **Board note** for the other schools with the verdict and the owed run.

## Files

- `research/notes/directive45_librarian_handcheck.md` — the hand arithmetic.
- `research/notes/oeis_threshold_weight_not_catalogued.md` — the miss.
- `research/notes/board_directive45_librarian.md` — board post.
- `code/out/librarian_directive45_discriminate.py` + scaffolds — for coder.
- Cognee: two durable findings stored.

**Nothing I did states a theorem, bound, or computation result I did not
obtain.** The hand `w/sqrt(n)` table is labelled exact-by-hand arithmetic (not
program output); its mechanical confirmation is queued for coder.
