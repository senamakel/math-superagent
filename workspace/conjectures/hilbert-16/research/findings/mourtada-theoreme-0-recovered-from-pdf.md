# Mourtada Théorème 0 conclusion recovered from arXiv PDF

## What was missing

`research/findings/mourtada-theoreme-0-truncation.md` recorded that the ar5iv
HTML conversion of Mourtada (arXiv:0912.1560) truncates **Théorème 0's
conclusion** after "il existe des entiers N et L et des voisinages … tels que".
The theorem's existence claim was clear from prose, but the exact numerical
content (the bound and the multiplicity cap) was not in the library, and the
finding's stated action was: fetch `https://arxiv.org/pdf/0912.1560` and read
Théorème 0's conclusion from the PDF.

## What was fetched

- **arXiv PDF (v1), 8 Dec 2009, 94 pp Amstex, 736579 bytes** —
  `research/sources/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.full.md`
  (219709 bytes of converted Markdown, 6399 lines, 40085 words; indexed).
- Structural digest (for the scholar to replace with a summary):
  `research/summaries/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.md`.
- Source URL recorded in the document header: `https://arxiv.org/pdf/0912.1560v1`.

## Théorème 0, complete, from the PDF (lines 50–62 of the held full text)

> **Thorme 0.** Soit X_ν un dploiement analytique de X_0 q paramtres. Alors il
> existe des entiers N et L et des voisinages Γ_k ⊂ U ⊂ U_0 et V ∈ (ℝ^q, 0)
> tels que
> (i) pour tout ν ∈ V, le nombre de cycles limites de X_ν dans U est major par N,
> (ii) la multiplicit de chacun de ces cycles limites est majore par L.

(Accents are lost in the PDF text extraction; the mathematics is complete and
unambiguous: the number of limit cycles of the perturbed field X_ν in U is
bounded by N for all ν in the parameter neighborhood V, and the multiplicity of
each such limit cycle is bounded by L.)

The truncation gap recorded in `research/findings/mourtada-theoreme-0-truncation.md`
is now **closed**: the numerical content of Théorème 0 is in the library.

## Evidence label

`asserted-by-source` — quoted from the held PDF conversion; not independently
formalised. This run does not need the actual values of N, L; what was missing
and is now held is the *statement* that they exist uniformly over the
neighborhoods U × V, which is the shape of the uniform bound Lu's QRH theorem
application assembles (thread `lu-h14-3-verification`).

## Availability record update

- Abstract page: `research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert.full.md` (6361 B).
- ar5iv full text: `research/sources/mourtada-0912.1560-algebres-quasi-regulieres-hilbert-ar5iv.full.md` (362644 B, 2506 lines) — Théorème 0 conclusion truncated there.
- **arXiv PDF v1 full text (NEW):** `research/sources/mourtada-0912.1560v1-algebres-quasi-regulieres-hilbert-pdf.full.md` — complete Théorème 0, the authoritative copy.
