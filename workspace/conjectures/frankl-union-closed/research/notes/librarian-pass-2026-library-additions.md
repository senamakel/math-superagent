# Librarian pass 2026 — library additions, paywall decisions, record stability

**Role:** librarian. **Pass:** this session.
**Memory store status:** Cognee was DOWN all pass (6/6 failures: "the memory server cannot index right now"); durable findings are written here, as the download tool instructed, to be stored in Cognee once the memory recovers. This note is the durable record.

## What was fixed

1. **Bošnjak–Marković n≤11 full text (the one genuine defect).** The library held only a 1,287-byte abstract stub for the load-bearing n≤11 verification source (`bosnjak-markovic-eleven-element-case-2008.full.md`). The full author PDF is now on disk:
   - `research/sources/bosnjak-markovic-eleven-element-case-2008.full.pdf.full.md` (46,903 B, converted from https://people.dmi.uns.ac.rs/~markovicp/papers/2008-Frankl11.pdf)
   - Structural digest: `research/sources/bosnjak-markovic-eleven-element-case-2008.full.pdf.md`
   - Summary (replacing the stub's role): `research/summaries/bosnjak-markovic-eleven-element-case-2008.md`
   - Indexed. It proves Theorem 3.1 (`|⋃F| ≤ 11` ⟹ UC) via Lemma 2.1 (weight-function iff criterion), Lemma 2.3 (S-hypercube counting), Propositions 2.1–2.3 / Theorem 2.1 (3-set local configurations), and Lemmas 3.1–3.11 (all 3/4/5-set configurations at n=11). This is the largest human-proof ground-set verification.

2. **Colbert Order 2026 version of record.** The library held the arXiv version; now the open-access journal full text is also held:
   - `research/sources/colbert-order-2026-openaccess.full.md` (40,163 B, from https://link.springer.com/content/pdf/10.1007/s11083-025-09717-w.pdf, CC BY)
   - Summary + claim block: `research/summaries/colbert-order-2026-openaccess.md` (claim `colbert-order-2026-version-of-record`)
   - Indexed. This gives the peer-reviewed version of the dimension-≤2 and DCC-topological-space settled classes (claims `colbert-dim-at-most-2`, `colbert-topological-dcc` previously anchored to the arXiv version).

## What could not be obtained, and why

1. **Hachimori–Kashiwabara, "Several Minimality Concepts Related to Frankl's Conjecture"** (Graphs Combin. 40(6):130, 2024, doi:10.1007/s00373-024-02834-0). Springer paywall; no arXiv twin or free full text found (searched author pages, MaRDI, dblp, ACM). Its content (family-order, minimality relaxations, 2-transversal result) is NOT in the claim store — only referenced by 3 held sources. **Gap:** needs a free copy or a claims extraction from the two held follow-ups (arXiv:2504.13454, 2511.19833) which state the surrounding results. Recorded as a request.
2. **Wakhare, JAT 2025** (doi:10.1016/j.jat.2025.106143). Elsevier paywall; the DOI landing page returned a 110-byte redirect. The arXiv full text is already held and indexed (`research/sources/wakhare-iterated-entropy-derivatives-2025.html.full.md`); a bibliographic stub records the published-reference split.
3. **Abe, "Strong semimodular lattices and Frankl's conjecture"** (Algebra Universalis 44 (2000) 379–382) and **Norton–Sarvate** (J. Austral. Math. Soc. 55 (1993) 411–413). Both Springer/Cambridge paywalled; statements already represented via the Bruhn–Schaudt survey full text and West's open-problems page (both held). Same accepted class as Reinhold 2000 and Abe–Nakano 1998.

## Record stability re-checked (request `exact-current-published-c8b8`)

Fresh 2025–2026 searches this pass confirm the published/preprint split is unchanged:
- **Published record:** Yu, "Dimension-Free Bounds for the Union-Closed Sets Conjecture", *Entropy* 25(5):767 (2023), c ≈ 0.38234.
- **Peer-reviewed barrier:** (3−√5)/2, Alweiss–Huang–Sellke, EJC 31(3):P3.35 (2024), doi:10.37236/12232.
- **Preprints still:** Cambie (arXiv:2212.12500, c ≈ 0.3823455, v2 2025-02-16) and Liu (arXiv:2306.08824, c ≈ 0.38271 conditional, CISS 2024 conference only).
- **No 2025–2026 source exceeds ≈ 0.38271 unconditionally.** New items surfaced (Colbert Order 2026 — now held; Wakhare JAT 2025 — arXiv held) are already covered.
- Existing claim `librarian-record-still-stable-2026` (note `research/notes/librarian-record-still-stable-2026.md`) already answers the request; this pass adds the two full-text completions.

## Falsify-me

- The record ranking is stale if Cambie 2212.12500 or Liu 2306.08824 gains a journal record, or a survey/new paper states an unconditionally better published constant.
- The Bošnjak–Marković full text is wrong only if the 46,903-B author PDF is not the EJC R88 text (verified: title, authors, abstract, lemma numbering match the EJC record).
- The Colbert journal full text is wrong only if the open-access PDF is not the Order 43(5) 2026 record (verified: DOI matches 10.1007/s11083-025-09717-w).