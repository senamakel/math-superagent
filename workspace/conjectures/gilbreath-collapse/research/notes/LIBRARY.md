# Reference library for COLLAPSE — librarian catalogue

Built against GOAL.md priorities: the symmetric-difference multiset (priority 1),
the run/endpoint structure (items 5–7), and the Walsh/Krawtchouk second-moment
framework of S².

## Genuine full texts held locally (indexed, searchable via `search_documents`)

| Source | Full-text file | URL | What it establishes for this problem |
| --- | --- | --- | --- |
| Mathonet–Rigo–Stipulanti–Zénaïdi, *On digital sequences associated with Pascal's triangle* (2022) | `sources/mathonet-rigo-stipulanti-zenaidi-digital-sequences-pascal.full.md` | https://arxiv.org/pdf/2201.06636 | Row `t_{p,n} = Σ C(n,i) mod p · p^i`; Lucas theorem as p-automatic structure; p-synchronized subsequences; evil/odious numbers. 2-regularity vocabulary for items 4–7. |
| Cilleruelo et al.? no — Wu, *Sums of products of binomial coefficients mod 2 and 2-regular sequences* (2023) | `sources/run-length-transform-binmod2-wu.full.md` | https://arxiv.org/pdf/2309.04012 | Run length transforms of recurrence sequences are **2-regular**; Walnut proofs. The run-structure vocabulary of item 5 (`ν₂(d+1)`, run lengths `2^g`). |
| Wu, *Sums of products of binomial coefficients mod 2* (INTEGERS 22, 2022) | `sources/run-length-transform-binomial-mod2-integers.full.md` | https://math.colgate.edu/~integers/w81/w81.pdf | **Theorem 1**: `C(n,k) ≡ 0 (mod 2) iff k ∧ ¬n ≠ 0` (the submask criterion defining `M_d`); run-length-transform recurrences; Sierpinski interpretation. Canonical for item 5. |
| Rowland, *The number of nonzero binomial coefficients mod p* (2011) | `sources/rowland-number-nonzero-binomial-modp.full.md` | https://arxiv.org/pdf/1001.1783 | Fine/Glaisher: `a₂(n) = 2^{pc(n)}`; Kummer/Lucas machinery; subword counts `|n|_w`. Down-set size counts behind items 2–3. |
| Callan, *Sierpinski's triangle and the Prouhet–Thue–Morse word* (2006) | `sources/sierpinski-thue-morse-callan.full.md` | https://arxiv.org/pdf/math/0610932 | Down-set incidence matrix `S[i][j]=C(i,j) mod 2 = 1 iff j⊆i`; Moebius-inversion inverse `S⁻¹`; carry-free binary-addition condition governing run structure. **The algebraic setting of `M_d` and `M_d△M_{d'}`.** |
| Amarilli–Monet–Suciu, *The Non-Cancelling Intersections Conjecture* (2024) | `sources/non-cancelling-intersections-amarilli.full.md` | https://arxiv.org/pdf/2401.16210 | Principal down-sets of the Boolean lattice; Moebius inversion on the meet-semilattice; non-cancelling (Moebius-nonzero) sets. Vocabulary for **which sets occur** in the S² index multiset (priority 1). |
| O'Donnell, *Analysis of Boolean Functions* (full book) | `sources/odonnell-analysis-of-boolean-functions-full.pdf.full.md` | http://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf | Walsh/Fourier spectral framework; influence, correlation, second-moment machinery — the analytic setting of `S(n,h)²`. |
| Rains–Sloane, *Self-Dual Codes* (Handbook of Coding Theory) | `sources/rains-sloane-self-dual-codes.full.md` | https://arxiv.org/pdf/math/0208001 | MacWilliams identities and Krawtchouk polynomials — the weight-enumerator/distribution machinery that governs how a sum over `(d,d')` characters behaves. |
| Shevelev, *On Stephan's conjectures concerning Pascal triangle modulo 2* (2012 v4) | `sources/stephan-conjectures-pascal-mod2-shevelev-fulltext.full.md` | https://arxiv.org/pdf/1011.6083v4 | Fermat-factorization of `d(n)`, generating functions for the binomial-mod-2 tower. |
| Meštrović, *Lucas' theorem: its generalizations, extensions and applications* (2014) | `sources/lucas-survey-fulltext.full.md` | https://arxiv.org/html/1409.3820v1 | Full six-section survey; `C(n,m) mod 2 = 1 iff m⊆n` — definitional basis of `Φ_n`. |

## Abstract stubs / duplicates — have real full texts elsewhere

- `analysis-of-boolean-functions-odonnell.full.md` (7.6 KB) — abstract page only; the real book is the CMU PDF listed above.
- `lucas-theorem-survey-mestrovic.full.md`, `stephan-conjectures-pascal-mod2-shevelev.full.md` — abstract pages; real texts are the HTML/PDF versions listed above.
- `stephan-conjectures-pascal-mod2-shevelev-fulltext2` — early v1 of Shevelev; superseded by the v4 full text.

## BAD CAPTURE — do not cite

- `symmetric-patterns-ca-pascal-barbe.full.md` is **NOT** Barbé's *Symmetric patterns in the cellular automaton that generates Pascal's triangle modulo 2*. The URL `arxiv.org/pdf/math/0508058` resolves to Levin–Olshanetsky–Zotov, *Painlevé VI, Rigid Tops and Reflection Equation* (quantum algebra), a completely unrelated paper. Do not attribute anything to Barbé from this file. If Barbé's CA paper is wanted, it is Discrete Appl. Math. 105 (2000) 1–38, DOI 10.1016/s0166-218x(00)00211-0 — not obtained (no open-access PDF found). The run-structure gap it would fill is instead covered by the two Wu run-length papers above.

## Notes

- All genuine full texts above are indexed via `index_document` and reachable through `search_documents`.
- Sources named `...full.md` in `sources/` are complete texts; each has a short digest in `summaries/`.
