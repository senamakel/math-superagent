# Reference library — Project Euler 1006 (Fibonacci word / subword squares)

Theme: combinatorics on words — Sturmian words and the Fibonacci word.

Governing identification: `S_n` converges to the infinite Fibonacci word, which is a
**Sturmian word** of slope `(3 - sqrt5)/2`. By the Morse–Hedlund theorem a Sturmian word
has exactly `n+1` distinct factors of length `n` — this is the problem's stated FACT that
there are exactly `k+1` distinct Fibonacci subwords of length `k`.

## Sources downloaded (full texts under `research/sources/`)

| File | Source | What it establishes |
| --- | --- | --- |
| `lothaire-sturmian-words-preview.full.md` | https://doi.org/10.1017/cbo9781107326019.003 (Lothaire, *Algebraic Combinatorics on Words*, Ch. 2 "Sturmian Words", Berstel–Séébold) | Authoritative definition of Sturmian words: exactly n+1 distinct factors of length n; Morse–Hedlund; mechanical words; characterizations. Verifies the Fibonacci word is Sturmian. |
| `sturmian-words-hal-note.full.md` | https://hal.science/hal-00828351/file/noteSturmianWords.pdf (Perrin–Restivo, "A note on Sturmian words", TCS) | **Structural theorem for the efficient method:** two length-n factors u,v of a Sturmian set are consecutive in lex order iff u=r·ab·s, v=r·ba·s or u=r·a, v=r·b. Algorithm to generate all n+1 length-n factors in lex order. |
| `morse-hedlund-theorem-sturmian-characterization.full.md` | https://hal.science/hal-01827511/document (Wojcik, "Formal intercept of Sturmian words" / hal-01827511, arXiv:1803.02073) | Primary statement of **Theorem 1 (Morse–Hedlund)**: ultimately periodic iff p(x,n)<=n for some n; a balanced word has p<=n+1; a balanced word is Sturmian iff slope irrational. Gives p=k+1 for the Fibonacci word. |
| `character-of-sturmian-words.full.md` | https://hal.science/hal-01829144v1/document (cyclic complexity of Sturmian words) | Prop 6: Sturmian iff exactly n+1 distinct length-n factors for all n. Prop 7: factor set depends only on slope. Fibonacci word fixed point of 0->01, 1->0. |
| `berstel-christoffel-words-repetitions.full.md` | https://webpages.math.luc.edu/~lauve/papers/wordsbook.pdf (Berstel, Lauve, Reutenauer, Saliola, "Combinatorics on Words: Christoffel Words and Repetitions in Words") | Christoffel words, Sturmian words, mechanical words; standard reference for surrounding theory. |
| `berthe-automatic-sturmian-sequences-course.full.md` | https://www.irif.fr/~berthe/Documents/ (Berthé, lecture notes on automatic and Sturmian sequences) | Course notes; surrounding theory of automatic / Sturmian / morphic sequences. |
| `factorizations-fibonacci-infinite-word.full.md` | https://arxiv.org/abs/1508.06754 (Fici, "Factorizations of the Fibonacci Infinite Word") | Structure of the Fibonacci word, singular words, Zeckendorf-parity encoding; factor structure. |
| `minimal-forbidden-factors-fibonacci.full.md` | https://arxiv.org/abs/2309.07070 (Rampersad–Wiebe, "Correlations of minimal forbidden factors of the Fibonacci word") | Minimal forbidden factors of the Fibonacci word; complementary view of the factor set. |
| `cassaigne-2008-extremal-properties-fibonacci-word.full.md` | Cassaigne, "On extremal properties of the Fibonacci word" (RAIRO ITA 2008) | Extremal/recurrence properties; slope 2-Phi; the Fibonacci word is a standard Sturmian word. |
| `de-luca-2013-some-extremal-properties-fibonacci-word.full.md` | de Luca, "Some extremal properties of the Fibonacci word" (IJAC 2013) | Extremal palindromic-prefix characterizations of the Fibonacci word among characteristic Sturmian words. |
| `note-on-sturmian-words-2011.full.md` | Perrin–Restivo, "A note on Sturmian words" (TCS 2012, doi:10.1016/j.tcs.2011.12.047) | Mechanical words, slope/intercept, characteristic word; Sturmian set; the lex-order consecutive-factor theorem. |
| `morse-hedlund-balanced-blocks-floor-alpha.full.md` | https://hal.science/hal-03869990v2/document (Poirier–Steiner, "Factor-balanced S-adic languages", TCS 2024) | Quotes the Morse–Hedlund balanced-blocks fact: each length-n block of a Sturmian sequence of slope alpha has floor(n alpha) or ceil(n alpha) occurrences of the alpha-frequency letter. |
| `morse-hedlund-1940-sturmian.md` | https://www.jstor.org/stable/2371487 (Morse & Hedlund, "Symbolic dynamics II: Sturmian trajectories", 1940) | The original 1940 paper. Only the paywalled cover was obtainable (307 bytes, unusable); cited for provenance only. |
| `chuan-fibonacci-words-fq.full.md` | https://www.fq.math.ca/Scanned/30-1/chuan.pdf (Chuan, "Fibonacci words", Fibonacci Quarterly 30.1, 1992, 68–76) | **Indexed enumeration of the Fibonacci-length factor set.** The F_n length-F_n "n-th Fibonacci words" are exactly the F_n cyclic shifts of the canonical coded word q_n; Theorem 11/Corollary 12 give the exact index rule for positions of the 1s in each shift. The bridge to the problem's length-(F_n−1) factor set (prefix-truncating the shifts) is a library conjecture and UNVERIFIED — see code/verify_chuan_enumeration.py. Summary at research/summaries/chuan-fibonacci-words-fq.md. |
| `de-luca-1981-property-fibonacci-words-slc-pdf.md` (full text, small) | https://www.mat.univie.ac.at/~slc/opapers/sc05deluca.pdf (de Luca, "A Property of Fibonacci words", Sém. Lotharingien Comb. 5 (1981); = the IPL 12 (1981) 193-195 paper) | **Previously blocked primary source now obtained.** Result: for n>=3 each Fibonacci word f_n has a palindrome left factor of length |f_n|-2; for n>=4, f_n is the unique product of two palindromes of lengths |f_{n-1}|-2 and |f_{n-2}|+2. The factorization that pins down the Fibonacci words. (Full text is short and lives entirely in the summaries copy.) |
| `mousavi-schaeffer-shallit-fibonacci-automatic-I.full.md` | https://cs.uwaterloo.ca/~shallit/Papers/part1.pdf (Mousavi, Schaeffer, Shallit, "Decision algorithms for Fibonacci-automatic words, I: Basic results", RAIRO ITA 50 (2016) 39-66) | Decision procedure over Fibonacci representations; ~31 proven theorems about the Fibonacci word: factor periods are Fibonacci numbers, unique right-special factor is f[0..n-1]^R, palindromes, Lyndon factors, critical exponent etc. Confirms the factor structure the run's recurrence relies on. |
| `chuan-fibonacci-words-fq.full.md` | https://www.fq.math.ca/Scanned/30-1/chuan.pdf (Chuan, "Fibonacci Words", Fibonacci Quarterly 30.1 (1992) 68-76) | Primary structure of Fibonacci words: the set of nth Fibonacci words = all cyclic shifts of a fixed word (Thm 7), F_n of them; positions of letters as arithmetic progressions mod F_n (Thm 11, Cor 12); Algorithm A constructs the nth Fibonacci word's letter positions directly. Gives the positional/cyclic-shift structure the two-point counts C_2(k,i,i') in the sum-of-squares collapse could exploit. |

## Notes on availability

- The de Luca 1981 IPL paper (previously 403-blocked) was obtained from the open-access
  Séminaire Lotharingien de Combinatoire scan (geodesic.mathdoc.fr + mat.univie.ac.at PDF).
- The RAIRO DOI (10.1051/ita/2016010) for the Fibonacci-automatic paper is 403-blocked;
  the author's own preprint PDF on Shallit's Waterloo page was obtained instead.
- Cassaigne–Kaboré 2022 and several Elsevier PDFs remain blocked by 403; content is
  covered by the Lothaire chapter and Perrin–Restivo note.

## Deprecated / do-not-use files

- `research/sources/mousavi-schaeffer-shallit-fibonacci-automatic.full.md` and
  `research/sources/mousavi-schaeffer-shallit-fibonacci-automatic.md` were created by
  mistaken arXiv-ID guesses and now carry only a correction notice. Use the
  `-I` suffixed files above.

## Summary notes

Every usable source above has a digest/summary under `research/summaries/` (same basename).
Read the summary first; open the `.full.md` only when the summary does not answer the question.
