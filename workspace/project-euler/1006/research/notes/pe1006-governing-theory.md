# Governing theory and primary references

The limit of `S_n` is the Fibonacci word, the fixed point of the morphism `0 -> 01, 1 -> 0`. It is a characteristic Sturmian word, with slope `alpha = (3-sqrt(5))/2 = 1/phi^2` for the problem's digit convention. A Sturmian word has factor complexity `p(k)=k+1` (Morse--Hedlund minimal-complexity theorem), so the problem's factors are exactly the length-k factors of this infinite word.

Mechanical-word representation: for irrational slope alpha and intercept rho, the lower mechanical word is
`d_j(rho)=floor(rho+(j+1)alpha)-floor(rho+j alpha)`. Rotation coding partitions the circle into intervals; length-k factors correspond to the cells cut out by the finitely many boundary rotations. Thus the k+1 factors can be represented by k+1 circle intervals/intercepts. Telescoping converts their decimal values into a geometrically weighted sum of floor terms. Squaring requires only first and second floor moments.

The efficient primitive is the universal Euclidean algorithm, a monoid generalisation of AtCoder's `floor_sum`: Euclidean reciprocal/quotient steps compose a segment carrying count, geometric weight, weighted first floor moment, and weighted second floor moment. The composition law follows by shifting all floor values in the right segment by the left segment's accumulated height; Euclidean recursion gives O(log n) quotient steps rather than enumerating k factors.

Sources already local:
- `research/sources/lothaire-sturmian-words-C2.full.md`, Lothaire, *Algebraic Combinatorics on Words*, chapter on Sturmian words (complexity definition and Sturmian p(n)=n+1). URL recorded in its summary/source metadata: https://doi.org/10.1017/CBO9781107326019
- `research/sources/perrin-sturmian-words-lecture2-mechanical.full.md`, Perrin lecture notes on mechanical words and rotations. URL: http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture2/slides2.pdf
- `research/sources/oi-wiki-universal-euclidean-floor-sum.full.md`, universal Euclidean monoid and Euclidean recursion. URL: https://oi.wiki/math/number-theory/euclidean/
- `research/sources/universal-euclidean-geometric-weight-fhq.full.md`, geometric-weight universal Euclidean treatment. URL: https://www.cnblogs.com/dixiao/p/15719155.html
- `research/sources/atcoder-math-hpp-v151.full.md`, official AtCoder Library base floor_sum implementation. URL: https://cdn.jsdelivr.net/gh/atcoder/ac-library@v1.5.1/atcoder/math.hpp
- `research/sources/berstel-sturmian-episturmian-survey-2007.full.md`, Berstel et al. survey on Sturmian words. URL recorded in its source metadata.

Primary-paper search was attempted for de Luca--Mignosi and Mignosi's Sturmian-factor papers, but ScienceDirect returned 403 and the DOI landing page for de Luca's Fibonacci paper had no extractable text. The accessible local books/lecture notes and algorithm sources above are therefore the usable reference tier; the blocked papers are not cited as evidence.