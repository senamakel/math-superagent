# Librarian reachability & coverage verification pass

Author: librarian. This is a *second* coverage pass; it does not re-do the first
(`librarian_coverage_pass.md`). It verifies the prior pass's claims about
indexing/reachability, fixes what it finds, and corrects one stale evidentiary
label in CONTEXT.md.

## What I verified, and the one fix

**The library is complete and almost entirely search-reachable.** I confirmed,
by spot-checks that the derived ledgers and CONTEXT.md actually quote primary
sources correctly, not on the coverage note's word alone:

- **The parity barrier.** ABGS 2011 §1: the consecutive-prime residue-pair
  frequency problem is "wide open, and cannot be treated using L-functions,
  unlike the case of Dirichlet's theorem." Verified verbatim in
  `sources/ash_beltis_gross_sinnott_prime_residues.full.md` (lines 188–192).
  This is the exact barrier `problem.md` §7 attributes.
- **Lau 2024.** Even *a single non-constant residue class pattern of length m
  occurring infinitely often among consecutive primes* is "beyond the reach of
  existing methods." Verified in `sources/lau_residue_patterns.full.md`
  (line 125). The switch (non-equal) side of mod-4 is genuinely untouched.
- **Shiu 2000 / door-3 refutation.** The freely-available Ethan Yang expository
  `sources/shiu_strings_expository.full.md` states the full quantitative theorem
  (Thms 1.1, 4.1): arbitrarily long strings of consecutive primes ≡ a (mod q)
  with quantitative length and density bounds. For q=4, a=1 and a=3 are both in
  A±, so arbitrarily long all-zero runs exist in the gap-parity string h.
- **Odlyzko 1993.** Archived; documents the {0,2} stop-block structure of the
  iterated-absolute-difference object and Gilbreath's conjecture / verification.

**The fix.** Three sources were on disk but *not* reachable through
`search_documents` — the exact failure the first coverage pass warned about.
`index_document` was called on all three and confirmed:
- `sources/hofer_pascal_matrices_mod2.full.md` (indexed, 4769 words)
- `sources/shiu_strings_expository.full.md` (indexed, 2991 words)
- `sources/lau_residue_patterns.full.md` (indexed, 11028 words)

A distinctive-text re-search after indexing still ranks the 808 KB coding-theory
textbook and the 151 KB Lucas-HTML mirror above everything — a *search-ranking
artifact of document size*, not a gap. A reader wanting a specific small source
should go to `research/sources/<name>.full.md` directly by name rather than
trust `search_documents` ranking for the small sources.

**One stale label corrected (durable memory).** CONTEXT.md's "Sources on
disk" section says the Shiu input is "unsourced here" because the Wiley
paywalled original was never downloaded. That is now *false*: the locally-held
Ethan Yang expository states and proves the theorem. So the "no long constant
runs / primes not eventually periodic" input (problem.md fact 5, closed
door 3's refutation) is **proved-status**, not merely conditional-on-abstract.
Recorded in Cognee.

## Current library inventory

- **44 full texts** in `research/sources/`, each recording its source URL in
  the first line (`<!-- source: … -->`). All indexed.
- **~55 digests** in `research/summaries/`, each carrying claim blocks that
  feed `research/CLAIMS.md`.
- Every **adopted live line's engine is backed by a primary local source**
  (Krawtchouk/MacWilliams/Delsarte tier; Lucas-mixing/ergodic tier; Pascal-mod-2
  fold-matrix tier; prime-residue barrier tier).
- The one *open* library-level gap is unchanged: `walsh-spectral-subset-b904` —
  no source anywhere states a Walsh/subset-sum lower bound on `wt(Φ_n x)` for
  inputs not "complicated" in the five refuted senses. That is a gap in
  *theorems*, not in the library; no source on it exists to download.

## Bottom line

Phase 1 (library building) is complete and can stop. ROOT.md meets its phase-1
completion test (structure of a minimal counterexample, verification bounds, and
three settled restricted classes with hypotheses all stated). Further gathering
happens only against a stated gap in `research/REQUESTS.md`.
