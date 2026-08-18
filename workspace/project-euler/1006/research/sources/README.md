# Local reference set

Primary sources held as full text in `research/sources/` (each carries its URL
in the first line; summaries live in `research/summaries/`).

## Canonical tier — Sturmian words / Fibonacci word / factor complexity

- `lothaire-sturmian-words-C2.full.md` — Lothaire, *Sturmian Words*, DOI https://doi.org/10.1017/CBO9781107326019.003
- `perrin-restivo-note-sturmian-words.full.md` — Perrin–Restivo, *A note on Sturmian words*, DOI https://doi.org/10.1016/j.tcs.2011.12.047
- `perrin-sturmian-words-lecture2-mechanical.full.md` — Perrin, *Sturmian words Lecture 2: mechanical words, rotations* (http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture2/slides2.pdf)
- `berstel-recent-results-sturmian-words-dlt95.full.md` — Berstel, *Recent results in Sturmian words* (http://www-igm.univ-mlv.fr/~berstel/Articles/1996SturmianDLTMagdeburg.pdf)
- `berstel-sturmian-episturmian-survey-2007.full.md` — Berstel et al., *Sturmian and Episturmian Words* (https://ligm.univ-eiffel.fr/~berstel/Articles/2007SturmianThessalonique.pdf)
- `berstel-karhumaki-combinatorics-words-tutorial.full.md` — Berstel–Karhumäki tutorial (HAL)
- `morse-hedlund-symbolic-dynamics-1938-ams-abstract.full.md` — Morse–Hedlund 1938 abstract (AMS); the 1940 "Symbolic Dynamics II" itself is paywalled (MathSciNet MR0000745)
- `coven-hedlund-sequences-minimal-block-growth-1973.full.md` — Coven–Hedlund 1973 (minimal block growth)
- `cassaigne-complexite-facteurs-speciaux-1997.full.md` — **Cassaigne, *Complexité et facteurs spéciaux*, Bull. Belg. Math. Soc. 4 (1997) 67–88** (full text from the EMIS mirror; Project Euclid gives only an abstract). Special/bispecial-factor machinery: Prop 3.1 s(n)=p(n+1)−p(n), Prop 3.2 bs(n)−bf(n)=s(n+1)−s(n); the Fibonacci right-special tree is filiform.
- `fici-mantaci-restivo-romana-rosone-sciortino-bwt-combinatorics-words-dagstuhl.full.md` — **Fici et al., *BWT and Combinatorics on Words*, OASIcs 131 (Manzini festschrift, 2025), DOI 10.4230/OASIcs.Manzini.1, CC-BY** — modern survey of the BWT–Sturmian connection; standard Sturmian = minimal BWT runs; Fibonacci = standard Sturmian with directive sequence all-1s; Christoffel = Lyndon conjugate of a standard word.
- `glen-justin-episturmian-words-survey-2009-ar5iv.full.md` — **Glen–Justin, *Episturmian words: a survey*, RAIRO-ITA 43 (2009) 403–442 (arXiv:0801.1655, full text via ar5iv)** — canonical modern survey of the Sturmian/episturmian theory axis; §7 "Balance & lexicographic order" gives Pirillo's Sturmian inequalities `as ≤ min(s) ≤ max(s) ≤ bs` (char. standard Sturmian, Veerman mid-80s), the Glen–Justin–Pirillo finite-word lexicographic characterizations (Thm 7.5; Cor 7.7), and the infinite-Lyndon/standard correspondence (Thm 7.9) — the lexicographic-order structure that PE1006's val(x) = decimal value on equal-length binary factors sums over. Replaces the abstract-page-only first download (`glen-justin-episturmian-words-survey-2009.full.md`).
- `glen-justin-widmer-zamboni-palindromic-richness-ar5iv.full.md` — **Glen–Justin–Widmer–Zamboni, *Palindromic richness*, EJC 29 (2008) 510–531 (arXiv:0801.1656, full text via ar5iv)** — the primary companion to the held Glen–Justin survey: rich words (maximal palindromic complexity |w|+1), Thm 2.14 (rich iff complete returns to palindromes are palindromes), Thm 5.2 (recurrent balanced rich = balanced episturmian). The Fibonacci word is Sturmian hence rich; third corroborating characterisation axis for the factor set, no bearing on the decimal second moment Ψ(k).
- `wikipedia-fibonacci-word.full.md`, `wikipedia-sturmian-word.full.md`, `mathworld-sturmian-sequence.full.md`, `mathworld-morse-hedlund-theorem.full.md` — encyclopedic tier

## Primary factor-structure sources

- `sivasankar-rama-fibonacci-factors-2022.full.md` — *Locating factors of the infinite Fibonacci word*, https://arxiv.org/abs/2207.04304
- `fibonacci-word-2d-factor-complexity-ar5iv.full.md` — Sivasankar–Rama 2D factor complexity, https://arxiv.org/abs/2204.13977
- `chuan-fibonacci-words-fq1992.full.md` — Chuan, *Fibonacci Words*, Fibonacci Quart. 30 (1992) (https://www.fq.math.ca/Scanned/30-1/chuan.pdf)
- `chuan-moments-conjugacy-classes-fq2003.full.md` — Chuan, *Characterizations of α-Words, Moments, and Determinants*, Fibonacci Quart. 41 (2003) (https://fq.math.ca/Scanned/41-3/chuan.pdf)
- `fici-factorizations-fibonacci-infinite-word-ar5iv.full.md` — Fici, *Factorizations of the Fibonacci infinite word*, https://ar5iv.labs.arxiv.org/html/1508.06754
- `currie-saari-least-periods-factors.full.md` — Currie–Saari, *Least periods of factors of infinite words* (numdam ITA 2009)
- `richomme-saari-zamboni-standard-factors-sturmian.full.md` — RAIRO-ITA 2010, *Standard factors of Sturmian words* (DOI 10.1051/ita/2010011)
- `rytters-subword-graphs-docslib.html.full.md` — Rytter, *The structure of subword graphs and suffix trees of Fibonacci words*
- `lanciault-reutenauer-symmetry-property-christoffel-eptcs.full.md` — **Lanciault–Reutenauer, *A Symmetry Property of Christoffel Words*, EPTCS 403 (2024) 123–127 (arXiv:2406.16408, CC BY 4.0)** — recent primary on the Christoffel-class axis: strong factor-symmetry of δ_w(i,j) (distinct factors by Parikh image) characterises Christoffel words among primitive Sturmian words (Thm 3.2); explicit Parikh-complementing factor bijection (Thm 4.1); support = paths of w and its upper reversal (Thm 4.2). Complements held Borel–Reutenauer 2006; Parikh-image symmetry, not the decimal moment Ψ — background for the conjugacy axis, no engine for G4.
- `bugeaud-reutenauer-conjugates-christoffel-ar5iv.full.md` — *On the conjugates of Christoffel words*, https://ar5iv.labs.arxiv.org/html/2202.05486
- `wen-wen-singular-words-fibonacci-word-1994.full.md` — Wen–Wen, *Some properties of the singular words of the Fibonacci word*
- `bonardo-frid-shallit-valid-factorizations-fibonacci-prefixes-ar5iv.full.md` — *The number of valid factorizations of Fibonacci prefixes*
- `cassaigne-extremal-properties-fibonacci-word.full.md` — Cassaigne, *On extremal properties of the Fibonacci word* (numdam RAIRO-ITA 2008)
- `hegedus-nagy-representations-circular-words-arxiv.full.md` — Hegedüs–Nagy, *Representations of Circular Words*, https://arxiv.org/abs/1405.5607

## Rotation / three-gap / discrepancy tier (Ostrowski route)

- `weiss-three-gap-rauzy-veeche.full.md` — Weiß, *Deducing Three Gap Theorem From Rauzy-Veech Induction*, https://arxiv.org/pdf/1807.11273
- `van-ravenstein-three-gap-theorem-1988-hal.full.md` — Mayero's detailed formalisation of van Ravenstein's 1988 proof (HAL); the 1988 original itself is scanned-only/no text layer in open copies
- `alessandri-berthe-three-distance-theorems.full.md` — Alessandri–Berthé, *Three distance theorems and combinatorics on words*
- `berthe-reutenauer-three-distance-2024.full.md`, `berthe-reutenauer-three-distance-intelligencer-2024.full.md` — Berthé–Reutenauer, *On the Three-Distance Theorem*
- `brown-shiue-sums-fractional-parts-multiples-irrational.full.md` — **Brown–Shiue 1995**, explicit CF closed form for C_α(n)=Σ({kα}−1/2) (https://www.sfu.ca/~vjungic/tbrown/tom-27.pdf)
- `pinner-sums-fractional-parts-nα+γ-1997.full.md` — **Pinner 1997**, non-homogeneous C_m(α,γ) closed form (https://www.math.ksu.edu/~pinner/Pubs/frac.ps)
- `ralston-substitutions-1-2-discrepancy-rotations-paper.full.md` — **Ralston**, *Substitutions and 1/2-discrepancy of {nθ+x}* (https://ar5iv.labs.arxiv.org/html/1105.5810)
- `ostrowski-numeration-addition-finite-automata.pdf.full.md` — Hieronymi–Terry, *Ostrowski numeration systems, addition and automata*
- `schaeffer-ostrowski-local-period-sturmian-2012.full.md` — Schaeffer, *Ostrowski numeration and local periods of Sturmian words*
- `formal-intercepts-sturmian-2018.full.md`, `sturmian-formal-intercepts-hal-01827511.full.md` — *Formal intercepts of Sturmian words* (Ostrowski expansions)

## Automaticity / Cobham tier (negative results — what does NOT work)

- `durand-rigo-on-cobham-theorem-ems-2021.full.md` — Durand–Rigo survey, Cobham theorem (EMS)
- `frougny-mult-dep-linear-numeration-2002-irif.full.md` — Frougny, multiplicative dependence of linear numeration
- `mousavi-schaeffer-shallit-fibonacci-automatic-ar5iv.full.md` — Du–Mousavi–Schaeffer–Shallit, *Decision algorithms for Fibonacci-automatic words*
- `hieronymi-decidability-sturmian-words-ar5iv.full.md` — Hieronymi, decidability for Sturmian words

## Floor-sum / universal-Euclidean tier (committed primitive)

- `oi-wiki-universal-euclidean-floor-sum.full.md` — OI-wiki 万能欧几里得 (https://oi.wiki/math/number-theory/euclidean/)
- `universal-euclidean-geometric-weight-fhq.full.md` — fhq cnblogs geometric-weight universal Euclidean
- `loj138-universal-euclidean-floor-moments.full.md` — LOJ138 universal Euclidean floor moments
- `atcoder-math-hpp-v151.full.md` — AtCoder Library atcoder/math.hpp (floor_sum)
- `chtholly-universal-euclidean-oiwiki.full.md` — Chtholly's algorithm (OI-wiki)
- `beck-robins-computing-continuous-discretely.full.md` — Beck–Robins, *Computing the Continuous Discretely* (lattice-point sums)
- `binner-reciprocity-floor-square-functions.full.md`, `bin̄ner-reciprocity-fulltext.full.md` — Binner, reciprocity for sums of squares of floor functions
- `babichev-shpakova-weighted-floor-moments-2026.full.md` — weighted floor moments / lattice rectangles

## OEIS / catalogue tier

- `oeis-A003849-fibonacci-word.full.md`, `oeis-a003849-fibonacci-word.full.md`, `oeis-A003849-first-1652-subwords.full.md` — A003849 (Fibonacci word)
- `oeis-A213975-fibonacci-subwords-lexicographic.full.md` — A213975 (factors of the Fibonacci word, lexicographic)

## Failed/blocked downloads this cycle (recorded in `research/notes/fractional-part-sums-closed-form-acquisitions.md`)

- Chuan 1997 α-words; Chuan–Ho 2010 location/decompositions; Berstel–de Luca 1997 Lyndon/trees; van Ravenstein 1988 original (scanned, no text layer); Ostrowski 1922 (paywalled). All have adequate modern/primary substitutes already held, except the Chuan factor-location papers whose content overlaps `sivasankar-rama-fibonacci-factors-2022.full.md`.

The source tree is catalogued by Cognee (the workspace's durable recall layer);
per the workspace convention, `research/` carries no manual INDEX.md.
