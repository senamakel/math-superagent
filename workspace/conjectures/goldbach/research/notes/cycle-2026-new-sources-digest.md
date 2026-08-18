# Cycle digest: new restricted-class, small-gaps, Liouville, and average-order sources

What the newly-landed sources establish, judged against this run's goals and current beliefs. Per-source notes live in `research/summaries/`; this note records the cross-cutting verdicts and the defects found.

## Sources that help (filed as claim blocks in their summaries)

- **Grimmelt–Teräväinen 2022/2026** (almost twin primes; two Chen primes): power-saving exceptional sets for sums of two Chen primes (m≡4 mod 6). Directly underpins the run's thesis `chen-prime-exceptional-set` and the computation task `chen-prime-goldbach-computation`. The 2026 paper's δ is effective in principle; neither paper computes it.
- **Salmensuu 2022**: Goldbach with both summands in prescribed residue classes mod r, almost-all in three layers, r up to N^(1/2). Restricted-class rung material.
- **Cumberbatch 2024**: power-saving exceptional set within digit-restricted sets (|A(X)|^(1−δ) counting in the thin set). New restricted-class angle.
- **Mangerel 2024 (two papers)**: Liouville convolution bound |Σλ(n)λ(N−n)|<N−1 unconditionally; GRH-conditional sign-pattern version. Analogues, not transfers to primes; benchmark only.
- **Goldston–Suriajaya 2023**: unconditional Fujii average Goldbach formula (previously RH-conditional). Sharpest average-order identity; tool for minor-arc analysis, not every-n.
- **Hongze Li 2000**: E(x)=O(x^0.914), full text on disk; confirms ledger chronology.
- **Bhowmik–Grimmelt 2026 survey**: explicit major-arc formula + sparse-HL-implies-no-exceptional-zero; canonical survey for exceptional-set record. **File misnamed as Pintz.**
- **Akeno 2025/2026, Tsuda 2025**: small gaps between Goldbach primes (0.76542 record vs 0.8201) and level of distribution 1/6 for Goldbach primes. Almost-all structural results for the small-gaps thread.
- **Meng 2007**: predecessor (3,8) in the restricted-class chain; superseded.

## Sources that do NOT help (and why)

- **`brudern-kaczorowski-perelli-…TAMS-2019.full.md` is the wrong document** (Saha, withdrawn arXiv:1802.10562) — **but the true BKP paper IS in the library** at `bkp-explicit-formulae-averages-goldbach-representations-arxiv-1712.00737.full.md` (arXiv:1712.00737; TAMS 372 (2019) 6981–6999), digested with claim `bkp-cesaro-riesz-explicit-formula` (explicit formula for Cesàro–Riesz means of Goldbach representation counts). The misnamed file must not be cited; the correct file is the BKP source.
- **Akeno small-gaps / Tsuda / Meng / Matomäki 2008**: abstract pages only; the on-disk text is the Springer/arXiv abstract, not the full paper. Claims filed are abstract-level, marked asserted.
- **Mangerel–Shusterman** is GRH-conditional and about λ-signs, not primes — no implication for binary Goldbach (filed as asserted analogue).

## Defects found this pass

1. **`brudern-kaczorowski-perelli-…TAMS-2019.full.md` is the wrong document** (Saha, withdrawn arXiv:1802.10562). **However, the true BKP paper is on disk** at `bkp-explicit-formulae-averages-goldbach-representations-arxiv-1712.00737.full.md` (arXiv:1712.00737; TAMS 372 (2019) 6981–6999), now digested with claim `bkp-cesaro-riesz-explicit-formula`. The library-status note's "arXiv:1802.10562" attribution was wrong and is corrected; the misnamed file should be deleted or renamed.
2. **`peneva-exceptional-set-goldbach-short-intervals-monatshefte-2008.full.md` is misnamed**: the article is by **Kaisa Matomäki**, not Peneva (Peneva's same-titled paper is Monatsh. Math. 132 (2001) 49–65). The library-status note's "(7) Peneva 2008" is wrong on authorship.
3. **`pintz-exceptional-set-goldbach-problem-survey-explicit-major-arcs-arxiv-2607.27282.full.md` is misnamed**: authors are Bhowmik & Grimmelt, not Pintz.
4. **Weakened-ladder δ=1/3 vs claims-ledger δ=0.28**: `research/weakened/goldbach-binary.md` rung R-density-delta said "best unconditional δ=1/3 (Pintz 2004, announced; Kumchev–Tolev §1 eq. (1.6))", but the claims ledger and ROOT correctly record best published δ=0.121 (Lu 2010), best claimed δ=0.28 (Pintz 2018 preprint X^0.72), and Zhao 0.7 preprint. The ladder's "announced δ=1/3" is a 2004 announcement superseded by Pintz's own 2018 X^0.72; **the ladder was stale and contradicted the ledger — corrected this pass** (now the ledger's `exceptional-set-chronology` is the current record).

## Verdict against current beliefs

None of the new sources resolves or refutes binary Goldbach; none contradicts the standing thesis (GT exceptional set empty in verified ranges). The new restricted-class results (Salmensuu, Cumberbatch, GT 2026) strengthen the restricted-class rung and the Chen-prime computation task. The explicit-major-arcs formula (Bhowmik–Grimmelt), the Fujii average formula (Goldston–Suriajaya), and the BKP Cesàro–Riesz formula are tools for the exceptional-set and average-order lines. The misnamed `brudern-kaczorowski-perelli-…TAMS-2019.full.md` file should be deleted or renamed so nobody cites it; its true content is the `bkp-…-1712.00737.full.md` file.