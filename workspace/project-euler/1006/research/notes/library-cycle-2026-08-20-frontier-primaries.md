# Librarian cycle — 2026-08-20: frontier primaries + double-floor-product gap assessment

## What this cycle did

1. **Audited the library against the frontier's top rows.** The previous cycle
   (glen-justin-frontier) had resolved most anonymous OpenAlex rows to held
   sources. This cycle verified the remaining top rows against disk and
   identified three genuinely-absent primaries:
   - **Berthé–Holton–Zamboni, "Initial powers of Sturmian sequences"** (Acta
     Arith. 122, 2006) — top frontier row (cited by 5+ held sources). Now
     downloaded in full from the author's IRIF page (`berthe-holton-zamboni-initial-powers-sturmian.full.md`).
   - **Iliopoulos–Moore–Smyth, squares-in-Fibonacci-strings** (CATS'96 full
     text / TCS 172, 1997) — frontier row; full scanned PDF now held
     (`iliopoulos-moore-smyth-squares-fibonacci-string-cats96-pdf.full.md`).
   - **Huang–Wen, squares and cubes in the Fibonacci sequence** (arXiv:1603.04211)
     — new open primary on Fibonacci repetition structure, downloaded in full
     (`huang-wen-squares-cubes-fibonacci-sequence-ar5iv.full.md`).

2. **Attempted but could not obtain** (recorded, covered in-library):
   - Droubay–Justin–Pirillo, "Episturmian words and some constructions of de
     Luca and Rauzy" (TCS 255, 2001, cited 293×, cited by 16 of our sources):
     ScienceDirect 403-blocked; no open full text found. Its content (episturmian
     words, Rauzy rules, de Luca constructions, palindromic closure) is carried
     by the held Glen–Justin survey (which is the same authors' canonical survey
     of that theory) and by Berstel 2007 §7. Recorded as an honest gap, not a
     lead to burn budget on.
   - The Murdoch landing page was captured twice (278-byte shell then the real
     PDF); the shell file is superseded.

3. **Assessed the double-floor-product request and did not file it.** I tried to
   request a citable source for Σ floor(ai/c)·floor((ai+b)/c) geometric-weight
   double-floor sums. The request tool refused: the library's existing
   universal-Euclidean claims already cover single-floor geometric second
   moments, and the mechanical digits are {0,1}, so a product of two digits
   reduces via g(u)g(u+h) = (g(u)+g(u+h)−|g(u)−g(u+h)|)/2 to single-floor sums
   plus a |difference| term — and the |difference| of two {0,1} floors is again
   a {0,1} floor. So the double-floor-product tier is **not** the missing
   primitive. The genuine open gap remains **G4: a fixed-dimensional O(log k)
   aggregation over the k+1 intercepts** — a construction problem, not a source
   gap. This is recorded in the reductions ledger (pe1006-g4-diagonal-coupling)
   and CONTEXT.md's "Missing" section; no new request was needed.

4. **Two further frontier rows closed (Ramírez–Rubiano cluster).**
   - Ramírez & Rubiano, "On the k-Fibonacci words" (Acta Univ. Sapientiae
     5(2) 2013 212–226) — full text obtained via DocsLib after the journal
     landing page gave only the index; k=1 gives PE1006's S_n, |f_{k,n}|=F_{k,n+1}.
   - Ramírez, Rubiano & De Castro, "Fibonacci word fractal and snowflake"
     (TCS 528 2014, arXiv:1212.1368) — full text via ar5iv; fractal/polyomino
     applications, contextual.

5. **Durable memory still down.** All downloads this cycle reported "the memory
   server cannot index right now"; recall_memory passage search works but the
   graph half returns 409 Conflict, and remember_memory refuses with a health
   timeout. Verified findings are recorded on disk in the summaries/claims above
   and in `research/notes/durable-findings-pe1006.md`; they should be submitted
   to Cognee when it recovers, per the existing convention (CONTEXT.md "Where
   things disagree").

## Where the library stands

- Sturmian complexity, factor structure, position theorems, singular/standard
  words, three-gap/floor-sum, universal-Euclidean moments, lexicographic order,
  and now the prefix-power and square/cube repetition structure are all
  source-backed on disk.
- The live gap G4 remains construction work, not citation: no published theorem
  states the joint second-moment collapse of Ψ over k+1 intercepts.
- Frontier top rows are now worked to the limit of open access; the remaining
  paywalled primaries (Droubay–Justin–Pirillo 2001, Chuan 1997, Berstel–de Luca
  1997, Morse–Hedlund 1940, Ostrowski 1922, van Ravenstein 1988) are all
  covered by held surveys/equivalents, with the honest gaps recorded in
  `research/summaries/requests-closed-recap.md` and the frontier notes.
