# Established theory for Project Euler 1006

## Governing objects

The finite words `S_n` converge by prefix inclusion to the infinite fixed point `f` of the Fibonacci morphism `0 -> 01`, `1 -> 0`. The sets `F_k` are the length-`k` factors of `f`.

## Sturmian factor complexity

A binary infinite word is Sturmian exactly when it is aperiodic and balanced (Morse–Hedlund); equivalently it is an irrational mechanical word. Every Sturmian word has factor complexity `p(k)=k+1`, so the Fibonacci fixed point has exactly `k+1` distinct length-`k` factors. This is the theorem that reduces the factor universe from arbitrary substrings to a structured family of `k+1` factors.

## Mechanical/rotation coding

For slope `alpha` and intercept `rho`, the lower mechanical word is

` s_{alpha,rho}(n) = floor(alpha*(n+1)+rho) - floor(alpha*n+rho) `.

For irrational `alpha`, its digit is the coding of the rotation `R_alpha(z)={z+alpha}` by the partition `[0,1-alpha)` and `[1-alpha,1)`. A finite word `w` is a factor exactly when the corresponding intersection of rotated coding intervals is nonempty; this factor property is independent of the intercept. For the Fibonacci word the slope is `alpha=1/phi^2=(3-sqrt(5))/2`, where `phi=(1+sqrt(5))/2`.

For a length-`k` mechanical factor, the decimal value is computed exactly by the digit formula above, and the factor set can therefore be represented by the `k+1` rotation cells/intercepts. The remaining problem is the weighted second moment over all these cells; no source in the local library supplies a fixed-dimensional logarithmic aggregation theorem for this specific decimal square sum.

## Sources held locally

- Lothaire, *Sturmian Words*, chapter in *Algebraic Combinatorics on Words*, DOI: https://doi.org/10.1017/CBO9781107326019.003. Local file: `research/sources/lothaire-sturmian-words-C2.full.md`.
- Perrin, *Sturmian words, Lecture 2: Mechanical words, rotations*, source PDF: http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture2/slides2.pdf. Local file: `research/sources/perrin-sturmian-words-lecture2-mechanical.full.md`.
- Perrin–Restivo, *A note on Sturmian words*, DOI: https://doi.org/10.1016/j.tcs.2011.12.047. Local file: `research/sources/perrin-restivo-note-sturmian-words.full.md`.
- Sivasankar–Rama, *Locating factors of the infinite Fibonacci word*, arXiv: https://arxiv.org/abs/2207.04304. Local file: `research/sources/sivasankar-rama-fibonacci-factors-2022.full.md`.
- Berstel–Vuillon, *Coding rotations with a linear numeration system*, arXiv: https://ar5iv.labs.arxiv.org/html/math/0106217. Local file: `research/sources/berstel-vuillon-coding-rotations.full.md`.
- Official problem statement, URL: https://projecteuler.net/minimal=1006. Local file: `research/sources/project-euler-1006-official.full.md`.
