# Scholar pass — 2026-09: digest audit and the AJM status upgrade

What this scholar pass did and concluded.

## The two new full texts this pass (both verified as partial/metadata, not new maths)

1. **Ghosh 2402.18717 "A finiteness result towards CA"** — the AJM-acceptance fact is
   the one genuine durable upgrade: the finiteness/dimension results (Thm A ≤2-dim in
   every char; Thm B/Cor C finite Z-scheme, finitely many K-points; Thm E j_C(n)≥q(n)−1)
   are now **peer-reviewed, accepted for publication in the American Journal of
   Mathematics** (2026). This does **not** upgrade the full claimed proof of CA
   (arXiv:2501.09272), which remains an unverified 0-citation preprint (v2 Mar 2026).
   CA stays open; smallest open degree stays 20. Filed as claim
   `ghosh-finiteness-ajm-accepted` (verified, primary sources), and the digest summary's
   three ghosh claim blocks' status updated to accepted-at-AJM.

2. **Schaub–Spivakovsky JCA-2025 published record** — the Project Euclid download is a
   **provenance/metadata record** fixing the official citation
   (J. Commut. Algebra 17(2):199–202, 2025, DOI 10.1216/jca.2025.17.199). Content is
   identical to the held HAL-open full text (Theorem 5: R_i ∉ √(others) for
   i ∈ {d−3,d−2,d−1}; char-p break = Rolle/real-root ordering, no char-p analogue).
   Replaced the default template in its summary with a proper note; the result is already
   claimed as `ss-note-independence` / `peerreviewed-2025-schaub-spivakovsky`. Nothing new
   to extract.

## Audit of remaining "replace this digest" templates (all resolved, none load-bearing)

Checked every summary still carrying the default template and reconciled it against
`research/notes/does-not-help-scholar-cycle.md`, which already records each as a
does-not-help or duplicate:

- **Adeniran–Yan 2019** (Goncarov–partition-lattices): enumerative parking-function flavour
  of Goncarov polynomials; no bearing on CA's derivative-sharing / scheme / char-p. Documented does-not-help.
- **Dzhaparidze–Janssen 1994 PDF**: heavier measure-theoretic Abel–Goncharoff treatment;
  the CA-relevant growth bound is already claimed (`macintyre-goncaroff-bounds`); does-not-help, kept as full-text reference.
- **Lang 1990**: Diophantine heights survey; does-not-help, no CA connection.
- **Rahman `.cambridge` / `.pdf`**: the same paper as the already-claimed
  `popoviciu-erdos-rahman-nplus2`; duplicates, no new content.
- **Abdesselam–Chipalkatti CJM2012 landing** and **siebeck-curves landing**: landing/metadata
  pages of papers already digested (`ac-hilbert-covariant-perfect-power`,
  `casas-alvero_2012_roots-and-foci`); no new content.
- **arxiv_search_\*** transcripts: coverage records, not sources; no claims.

## Durable findings stored

Cognee memory server remains down (verify — `remember_memory` refused writes all pass);
all source-backed findings are recorded in workspace notes, the canonical store, and queued
in `research/notes/durable-findings-pending-cognee-scholar-cycle.md` for re-issue once the
server recovers. Added Finding 6 (AJM acceptance) to that queue.

## What the run still lacks (unchanged)
The final step of CA — showing the 1-dimensional piece of the CA variety is empty — remains
unproved; that IS CA. The finiteness backbone is now peer-reviewed, but the characteristic-0
collapse is not supplied by any held source, which is exactly the void the run's own
scheme-dimension / u-resultant argument would have to fill.
