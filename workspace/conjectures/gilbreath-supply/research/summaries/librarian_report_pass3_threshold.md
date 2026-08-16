# Librarian cycle — third pass, threshold-weight phase

**Author:** librarian. **Cycle:** search-freeze operative; run in third-pass
computational phase (directive 44/45).

## What this cycle added

1. **OEIS mischeck on the run-computed sequence** (the one genuinely new
   library action). The exact-mean linear-supply threshold weight
   `w*(n) = 3, 3, 3, 4, 3, 5, 7, 11, 16, 24, 35, 52, 77, 112, 164, 239`
   (n = 8..32768) is **not in the OEIS** — no closed form will be looked up.
   Recorded at `research/notes/oeis_threshold_weight_not_catalogued.md`,
   consistent with the fitted exponent `w* ~ n^0.5568` and with
   `model_compare.py`'s inability to separate a pure power from
   `n^{1/2}(log n)^β`. A miss is a result; nobody searches for it again.

## What I verified (no new acquisition)

- Library is complete for the current phase: 80 full sources (each URL-tagged at
  line 1) + 120+ summaries cover Krawtchouk/MacWilliams machinery, Lucas/Reed-
  Muller weight spectra, Rule-90/Pascal-mod-2, prime-residue biases, automatic
  sequences, Pivato-Yassawi randomization, comparative-prime-number-theory.
- The threshold-work mathematics is fully sourced: the sphere-mean Krawtchouk
  formula (`sphere-mean-krawtchouk-exact`) is proved-by-derivation and
  machine-verified; the exponent fit has a proper committed capture
  (`threshold_exponent_fit_pass3.txt`: sequence/oracle/range header, E =
  0.55678 ± 0.00225 over n≥256).
- The one open request `walsh-spectral-subset-b904` is *shape*-answered on disk
  (Yoshida Lemma 2: `wt(Φ_n h) ≥ 2^{popcount(d_min)}`); its theorem gap is a
  computational/theoretical gap, not a literature gap.
- Cognee recall is down (404) but storage works; on-disk ledgers render into
  context, so the library remains findable via `search_documents` and the
  notes/threads/ledgers.

## Why nothing further

Directive 7's gate: a new source must be preceded by naming a FRONTIER
candidate read and why none answers. I read the frontier: the ~799 cited-once
rows are mostly off-topic noise (supply-chain-management leaks) or already
covered; none answers the *computational* threshold question, which is in-house
computation, not literature. The pattern-finder has further run on the
discriminating exponent test (`librarian_directive45_discriminate.py`:
w/sqrt(n), w/(sqrt·log), n^log_4(3)) — coder's delivery, not a library gap.

**NOTHING FURTHER** until a stated gap in `research/REQUESTS.md` gives a query
worth spending a fetch on. The library is mature for this task; further
gathering would be waste.
