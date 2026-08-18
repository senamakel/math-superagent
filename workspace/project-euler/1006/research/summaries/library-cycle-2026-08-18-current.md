# Reference-library cycle

Searches covered Fibonacci-factor enumeration/location, mechanical/Sturmian rotation coding, generalized Beatty occurrence positions, weighted floor moments, and universal Euclidean recursion. Existing library already contains primary/near-primary sources for all but a complete PE1006 weighted aggregation.

## Newly confirmed from readable sources

- Perrin's lecture notes define lower mechanical words `s_{α,ρ}(n)=floor(α(n+1)+ρ)-floor(αn+ρ)`, identify them with rotation coding, and state that all intercepts of one irrational slope have the same factor set. URL: http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture2/slides2.pdf; local full text `research/sources/perrin-sturmian-words-lecture2-mechanical.full.md`, lines 14-88.
- The same notes state Morse–Hedlund's equivalence: Sturmian iff balanced and aperiodic iff irrational mechanical, and give the height floor-difference formula and balance bounds, lines 88-180.
- Sivasankar–Rama's Fibonacci-factor paper is locally held; the digest points to the one-dimensional theorem: for `F(n) ≤ k < F(n+1)`, a prescribed union of prefix windows at Fibonacci-index offsets gives exactly the `k+1` distinct factors in first-occurrence order. Local full text: `research/sources/sivasankar-rama-fibonacci-factors-2022.full.md`; digest `research/summaries/sivasankar-rama-fibonacci-factors-2022.md`.
- Allouche–Dekking defines generalized Beatty sequences `p floor(n α)+q n+r` and studies Fibonacci-word occurrence positions. Local full text: `research/sources/allouche-dekking-generalized-beatty-2019.html.full.md`; digest `research/summaries/allouche-dekking-generalized-beatty-2019.html.md`.
- OI Wiki's universal Euclidean notes give exact recurrences for `f=sum floor((ai+b)/c)`, `g=sum i floor(...)`, and `h=sum floor(...)^2`; the latter two form a closed triple under Euclidean slope reciprocity and run in logarithmic recursion depth. Local full text `research/sources/oi-wiki-universal-euclidean-floor-sum.full.md`, lines 180-360. This supports floor-moment subroutines but not by itself the required aggregation over all factors.

## Search outcome

No source found that directly supplies a complete constant-dimensional algorithm for the decimal square sum in PE1006. Searching for published Project Euler solutions was intentionally avoided. The library is broad; the remaining gap is mathematical, not bibliographic.