# Scholar digest — what the reference library now establishes

## Completed in this session

**Replaced 18 template digests with proper scholar notes** under `research/summaries/`,
each under ~1000 tokens, with fenced claim blocks and `[[name.full]]` wikilinks:
bremner-1999, bremner-II-2001, boyer-multimagie, boyer-notes-supplement-2005,
boyer-square-of-squares-search-v2, brown-mathpages-magic, brown-mathpages-orthomagic,
buell-hourglass, cain-gaussian, michaud-rodgers, morgenstern-extended-searches,
morgenstern-properties-2007, morgenstern-smallest-entry, oeis_a088111, oeis_a088959,
open-problem-garden, robertson-1996 (flagged as duplicate of Bremner 1999),
sallows-the-lost-theorem, wikipedia, zimmermann-loria-2015.

**Numbers program-verified** (`code/out/scholar_verify.py`): Sallows LS1 (7 of 8 sums
21609, failing diagonal 38307, all distinct squares); Bremner's square (all 8 sums
541875, centre 425², non-squares {360721,222121}); centre Pythagorean pairs (385,180)
realising v=138600 and (408,119) realising u+v=97104. Every number in the notes was a
program output.

**18 claim blocks** entered into `research/CLAIMS.md` with status and hypotheses.

## Uplift for the run's goal

- **K3 Brauer–Manin:** Bremner II gives `NS(S,Q)` rank 12 vs complex Picard 20 (the
  8-gap), every rational curve even degree, no rational curves of degrees 4 or 8 on the
  Category III K3 — the concrete object the `brauer-manin-k3-surface` approach file needs.
- **Extension-field MSS exist** (degree 4 over Q(√3,√133), degree 27 over Q(u), 8-square
  over Q(√3)) ⇒ no blanket structural impossibility; any proof must separate Q.
- **Real computational boundary:** Morgenstern's 8-digit-smallest-entry proof; the three
  primitive equal-d AP census (5 instances, none beyond d=3.31×10¹⁵ up to 6.4×10²²);
  the fixed-start AP generator/termination machinery for the four-AP condition.
- **Sieve constraints proved** (Morgenstern 2015, Zimmermann–Loria): entries ≡1 mod 24,
  sum ≡3 mod 72, no 3 mod 8 factors, step ratio excludes 4k+3 primes ±1 — must be survived
  by both witnesses.
- **Correction:** Buell's `25×10²⁴` is the *hourglass* bound, under coprimality;
  Zimmermann–Loria find 10-digit hourglass solutions when relaxed. Not a general MSS bound.

## Reconciliation (contradiction resolved)

`code/out/check_near_misses_latest.txt` and `near_misses.json` both report
`ALL CHECKS PASSED` / `all_checks_passed: true`. CONTEXT.md's "Contradictions" section
claims the flag is `false` — that is stale; the witness values are consistent and
program-verified. Flagged in memory as `Reconciliation: code/out/near_misses.json`.

## Sources that do not help (with reasons)

- **Robertson 1996** — duplicate of Bremner 1999 (same PDF).
- **Wikipedia / Open Problem Garden / Boyer multipage index** — tertiary restatements,
  no theorem or bound; pointers only.
- **Brown orthomagic** — different intermediate object, no reduction to the full problem.
- **Cain (arXiv)** — only the abstract page downloaded (no body); the quartic/Gaussian
  reformulation is asserted, not usable without the full text.
- **Michaud-Rodgers talk** — sketch-level; centre bound mis-attributed; no proofs.

## Still missing / open

- Buell full text (not on disk, only citations) — if the hourglass bound's exact
  hypothesis set is needed, re-fetch.
- Cain's paper body (if the quartic-over-abelian-extension reformulation is wanted).
- End-to-end reduction "rational point on K3 ⇔ distinct int MSS" is still not a
  checked claim (open request `exact-reduction-magic-507c`).