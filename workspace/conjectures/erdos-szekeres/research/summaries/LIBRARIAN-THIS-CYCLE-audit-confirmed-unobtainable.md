# Librarian cycle — audit; two primaries re-confirmed unobtainable; no open gap remains

## Conclusion in one line

The reference library already meets the phase-1 exit test: every standing REQUEST
row is answered by a primary full text on disk, ROOT.md states the structure of a
minimal counterexample, the current verification bound, and the restricted
classes, and every-cited-is-in-the-library holds. This cycle re-verified the two
documented-but-not-held primaries against fresh author-page checks and confirmed
neither is obtainable in open access. No new on-topic primary is missing, so this
cycle acquires no new primary text.

## What this cycle did

1. **Audited the standing requests.** The three rows in `derived/REQUESTS.md`
   (`balko-valtr-attack-baa4`, `open-access-full-1e6e`, `full-text-faithful-b96b`)
   all carry `answers:` claim blocks in held summaries
   (`research/summaries/balko-valtr-A-SAT-attack-on-ES-ENDM2015.md` for the first
   two, `research/summaries/erdos-szekeres-1961-...` / `erdos-szekeres-1961
   lower-bound-construction.md` for the third). The open rendering is a
   re-derivation artifact, not a library gap — the primary content backing each
   is on disk. The claims ledger entries with `answers:` are authoritative; these
   rows must not be re-opened.

2. **Re-checked the two genuinely absent primaries by fresh author-page route.**
   Both remain confirmed unobtainable in open access:

   - **Erdős–Tuza–Valtr 1996, "Ramsey-remainder"**, EJC 17(6):519–532, DOI
     10.1006/eujc.1996.0045 — canonical primary of the ETV enumeration
     conjecture N(a,u,k) = Σ C(k−2,i−2) equivalent to ES. ScienceDirect 403.
     Checked Pavel Valtr's Charles University homepage
     (https://kam.mff.cuni.cz/~valtr/): contact-only, hosts no PDFs. SZTAKI
     repository holds metadata only. Content is faithfully restated in the held
     Baek (arXiv:2206.04260, which states and cites the equivalence as Thm 1.5,
     and proves P(n,4,n)) and in Balko–Valtr. **Documented-but-not-held; do not
     re-search.**
   - **Károlyi–Solymosi 2005/6, "Erdős–Szekeres theorem with forbidden order
     types"**, JCTA 113(3):455–465, DOI 10.1016/j.jcta.2005.04.006 — ancestor of
     the held Károlyi–Tóth 2012 restricted-class result. Checked Solymosi's UBC
     on-line publications page
     (https://personal.math.ubc.ca/~solymosi/publications/publications.html): it
     lists the paper as "to appear" but attaches **no** hosted PDF link.
     ScienceDirect 403. Its results (there is an order type T with
     F_T(n) > 2^{n−2}, hence f_T(N) = Θ(log N)) are restated in the held
     Károlyi–Tóth 2012 full text
     (`research/sources/karolyi-toth-2012-ES-forbidden-subconfigurations-springer.full.md`).
     **Documented-but-not-held; do not re-search.**

## Files on disk (this cycle)

- `research/sources/valtr-homepage.md` — Valtr's homepage (contact-only,
  confirms no hosted ETV-1996 PDF). Source URL in the file.
- `research/sources/solymosi-publications-page.full.md` — Solymosi's UBC on-line
  publications list; confirms the Károlyi–Solymosi entry is listed with no PDF
  link. 17 new citation leads added to FRONTIER.
  (`research/summaries/solymosi-publications-page.md` is the structural digest.)
- `research/summaries/LIBRARIAN-THIS-CYCLE-audit-confirmed-unobtainable.md` —
  this record.

These two files are small and confirm a *negative* (not a primary); they do not
need to be round-tripped into ROOT.md, which already documents both gaps in §7.

## Memory note (infrastructure)

`remember_memory` and `describe_file` are currently failing (the memory server's
health report did not answer in 8 s). This record is written to the workspace so
the disposition survives the outage; it should be stored to Cognee once the
memory server recovers.

## Handoff

- **ROOT.md already meets GOAL.md criterion 1.** The literature's upper bounds
  (with error terms and sources), the lower-bound construction concretely, the
  exact values ES(3..6) with methods, and ≥3 restricted classes with exact
  hypotheses are all written with evidence classes and falsifiers.
- **Everything-cited-is-in-the-library** holds: every claim's `anchor:` resolves
  to a real file; the MIS-DOWNLOAD quarantine files each have a `correct`
  sibling and are flagged DO-NOT-CITE.
- The library is complete at the fidelity this run requires. Further acquisition
  happens only against a *new* stated gap in `research/REQUESTS.md`.
