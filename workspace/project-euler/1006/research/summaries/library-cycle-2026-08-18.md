# Reference-library refresh

## Sources checked and retained
- Perrin/Restivo, *Sturmian words* lecture material, locally available at `research/sources/perrin-restivo-sturmian-lecture.md`; URL: https://hal.science/hal-00828351v1/file/noteSturmianWords.pdf. It states that Sturmian words are exactly irrational mechanical words and have exactly n+1 factors of length n; it also gives a lexicographic factor-generation algorithm.
- Praveen & Rama, *A Note On ℓ-Rauzy Graphs for the Infinite Fibonacci Word*, locally available summary/source material at `research/summaries/citations_w4306801116.md`; URL: https://doi.org/10.48550/arxiv.2210.08629. It records Fibonacci subword complexity k+1 and Rauzy graph structure/connectivity.
- OI Wiki, *类欧几里德算法 / Universal Euclidean algorithm*, full source at `research/sources/oi-wiki-universal-euclidean-floor-sum.full.md`; URL: https://oi.wiki/math/number-theory/euclidean/. Lines 181–286 give the floor_sum recurrence and O(log min(a,c,n)) complexity. Lines 350–453 give simultaneous first, index-weighted, and square floor moments (f,g,h), including the reciprocal recurrence and implementation.

## Search outcomes
Searches covered Sturmian/Fibonacci complexity, mechanical coding, Rauzy graphs, and generalized floor sums. Existing local copies prevented duplicate downloads; no published Project Euler solution was searched for or downloaded.

## Mathematical findings
The Fibonacci fixed point is Sturmian/mechanical, hence its length-k factors are exactly k+1. The universal Euclidean algorithm evaluates ordinary and first/second polynomial floor moments by Euclidean recursion in logarithmic iteration count. This supports floor-moment subroutines, but does not by itself establish the missing aggregation from all k+1 Fibonacci factors to one fixed-dimensional floor-moment query.
