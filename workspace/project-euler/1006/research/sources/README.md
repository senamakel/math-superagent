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
| `morse-hedlund-1940-sturmian.md` | https://www.jstor.org/stable/2371487 (Morse & Hedlund, "Symbolic dynamics II: Sturmian trajectories", 1940) | The original 1940 paper. Only the paywalled cover was obtainable (307 bytes, unusable); cited for provenance only. |

## Notes on availability

- de Luca 1981 "A combinatorial property of the Fibonacci words" (the n+1-distinct-factors
  result), Cassaigne–Kaboré 2022, and several Elsevier PDFs were blocked by 403; their
  content is re-covered by the Lothaire chapter and the Perrin–Restivo note.
- Berstel–Séébold survey at univ-mlv.fr failed to download (connection refused); replaced
  by the Lothaire chapter (same authors' canonical text).

## Summary notes

Every source above has a digest/summary under `research/summaries/` (same basename). Read
the summary first; open the `.full.md` only when the summary does not answer the question.
