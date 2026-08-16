# Librarian acquisition report — signotope/CC-system foundations + SMQH repo check

What this cycle added to the local reference library, and what it settled about an open gap.

## Newly acquired (this librarian cycle)

| Source | File | URL | What it establishes |
|---|---|---|---|
| **Felsner & Weil 2001**, "Sweeps, arrangements and signotopes", Discrete Appl. Math. 109(1-2):67–94 (EuroCG 1998 proceedings; technical report B 98-06, 1999 rev.) | `sources/felsner-weil-sweeps-arrangements-signotopes-2001.full.md` (+ digest) | https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf | **The primary source for the signotope machinery.** Defines sweeps of line/pseudoline arrangements, the Sweeping Lemma; second part introduces the *triple-orientation* representation of an arrangement — a triple orientation corresponds to an arrangement exactly iff it obeys a generalized transitivity law — giving the signotope orders S_r(n) related to higher Bruhat orders B(n, r−1); maximum chains in S_{r−1}(n) map surjectively to elements of S_r(n). This is the exact correspondence the run's orientation-variable SAT encoders (Dumitru, Scheucher, SMQH, Balko–Valtr) mirror. PDF conversion is text-garbled (spaces stripped) but unambiguously this paper; its key rank-3 statement is faithfully restated in the held Bergold–Felsner–Scheucher summary. **Closes the "blocked, do not re-fetch" flag on Felsner–Weil in LIBRARY_LEDGER.md** — the primary is now held. |
| **Wikipedia — CC system** (encyclopedic tier) | `sources/wikipedia-cc-system.full.md` (+ digest) | https://en.wikipedia.org/wiki/CC_system | The standard encyclopedic statement of Knuth's counterclockwise-system axioms (cyclic symmetry, antisymmetry, nondegeneracy, interiority, transitivity) over a ternary relation `pqr`; construction from planar point sets via the 3×3 determinant; equivalence to pseudoline arrangements / sorting networks; the two-to-one correspondence between CC-systems and uniform acyclic oriented matroids of rank 3 (which correspond 1-1 to marked pseudoline-arrangement classes); the convex-hull-as-cycle definition. Fixes the combinatorial axioms behind the run's order-type abstraction. |
| **Knuth, "Axioms and Hulls"** (Springer LNCS 606, 1992) — the official page | `sources/knuth-axioms-and-hulls.full.md` | https://cs.stanford.edu/~knuth/aah.html | Points to the canonical monograph defining CC- and CCC-systems; notes chapter 15 (parsimonious algorithms) and that an electronic TeX is available (not the book text itself — a pointer/tier entry). The CC-system axioms proper are carried by the Wikipedia and CC-system entries; this holds the authoritative bibliographic anchor. |

## Gap resolution / closure record

- **Gap: explicit inner-12 configurations of SMQH** (LIBRARY-STATUS / REQUESTS standing open item).
  **Settled as *un-obtainable from the public repo* — record, not a gap.** The `orientations/`,
  `solutions/`, and `realizations/` folders in `bsubercaseaux/automatic-symmetries` are all empty
  `.gitkeep` placeholders (confirmed via the repo's git tree API: each of those three folders holds only
  a 46-byte `.gitkeep`). The paper states the six inner-12 configurations exist but gives neither
  coordinates nor orientation tables, and the repo does not carry them. So a later run should not go to
  the repo for them; the only routes are (a) re-running the SMQH encoder + Localizer, or (b) contacting
  the authors. This is filed as a *blocked/absent* record so nobody repeats the repo fetch. The claim
  `smqh-no-realizable-4fold-32-no7gon` (existence of the 6 non-realizable inner-12) remains as
  asserted-by-source.
  Also held this cycle: `sources/smqh-github-repo-search.full.md` + digest (the repo landing page,
  encoded + solver usage, folders list).

## Files on disk (all under research/)

- `research/sources/felsner-weil-sweeps-arrangements-signotopes-2001.full.md`
- `research/sources/wikipedia-cc-system.full.md`
- `research/sources/knuth-axioms-and-hulls.full.md`
- `research/sources/smqh-github-repo-search.full.md`
- plus the matching structural digests under `research/summaries/`.

All four full texts carry their source URL in the leading `<!-- source: ... -->` line. All are now
reachable by `search_documents` (library convention: ROT13 short name ↔ `search_documents`; the
full-text auto-index applies to `.full.md` siblings). Verified against the intended paper before
filing — no guessed arXiv identifiers were used; every URL came from search results or a held source.

## Scholar handoff

The structural digests auto-generated for the two PDF/HTML acquisitions this cycle —
`summaries/felsner-weil-sweeps-arrangements-signotopes-2001.md` (PDF: empty digest) and
`summaries/wikipedia-cc-system.md` (HTML: minimal digest) — should be replaced by scholar
summaries under 1000 tokens. The essential claims are already captured in this note and in
`summaries/bergold-felsner-scheucher-extension-theorem-signotopes.md` (which states the
rank-3 bijection precisely). The Felsner–Weil full text is PDF-garbled but verified correct;
quote it carefully.

## Not still not held (closure record)

- **Felsner–Weil 2001 journal version** — held via the author's revised PDF now; journal pagination
  differs but content is the same document. No gap.
- **Balko & Valtr 2017 EJC 66 journal version** — still paywalled; the open-access EuroComb ENDM 49
  (2015) full text is held and is the same content (requests `balko-valtr-attack-baa4` and
  `open-access-full-1e6e` closed by the ENDM claim blocks). No further action needed.
- **Knuth *Axioms and Hulls* book text** — only the pointer page held; the book is a Springer LNCS.
  The CC-system axioms are fully carried by the Wikipedia entry (held). A run needing the book's full
  text would have to download the author's plain-TeX zip (linked from `aah.html`); flag only if a
  precise lemma from the book is needed.
