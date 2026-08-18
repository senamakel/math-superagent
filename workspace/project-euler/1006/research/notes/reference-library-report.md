# Reference-library report

The library was read against PE1006. The source-backed findings are below; inaccessible journal pages (ScienceDirect HTTP 403 and a DOI landing page without extractable text) were not treated as evidence.

## Sources that bear directly

### Lothaire, *Algebraic Combinatorics on Words*, chapter 2
URL: https://doi.org/10.1017/CBO9781107326019

Defines factor complexity P(x,n)=|F_n(x)| and Sturmian words as infinite binary aperiodic words with P(x,n)=n+1. Applied to the Fibonacci limit of the problem, this proves that the distinct length-k factors are exactly k+1. It supplies the cardinality of the sum defining Psi, not its numerical evaluation.

### Perrin, *Sturmian Words, Lecture 2: Mechanical Words, Rotations*
URL: http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture2/slides2.pdf

Defines the lower mechanical word s_{alpha,rho}(n)=floor((n+1)alpha+rho)-floor(n alpha+rho), and identifies it with coding of rotation by alpha. Factors correspond to intercept intervals and the factor set is independent of rho. The problem's word uses the characteristic/Fibonacci slope alpha=1/phi^2 (not the complementary rabbit-word convention's 1/phi). This licenses indexing factors by rotation/intercept representatives and telescoping decimal values into weighted floor expressions. The source does not give Psi itself.

### OI Wiki, universal Euclidean algorithm
URL: https://oi.wiki/math/number-theory/euclidean/

Models the floor sequence floor((a i+b)/c) as an R/U lattice path and evaluates a monoid product by affine reductions and a reciprocal Euclidean flip. The recursion decreases parameters by Euclidean steps and has O(log max(a,c)+log(b/c)) depth, independent of n. It directly supports the structural complexity claim for the solver, but its displayed core monoid is unweighted; the geometric-weight extension is supplied by the next source.

### fhq_treap, geometric-weight universal Euclidean algorithm
URL: https://www.cnblogs.com/dixiao/p/15719155.html

Extends the R/U monoid to sums with geometric weights and carries constant-size state including first and second floor moments. Its merge and flip recurrences are exact integer identities and take O(log max(p,q)) monoid operations. This is the operational primitive needed after Psi is expressed as a quadratic form in geometrically weighted floor values. Hypotheses: integer nonnegative parameters, positive modulus arithmetic, and closure under moments through degree two; these hold for the proposed reduction because the decimal value is linear in floor values and its square is quadratic. It does not itself prove the Fibonacci mechanical reduction.

### LOJ138 universal-Euclidean floor moments
URL: https://loj.ac/p/138 (source captured locally)

States the moment-array generalisation: states sum x^p floor^q and are combined by binomial expansion under monoid concatenation. It corroborates that first/second moments remain finite-state under the Euclidean recursion. It is algorithmic corroboration, not a PE1006-specific derivation.

### AtCoder Library math.hpp v1.5.1
URL: https://cdn.jsdelivr.net/gh/atcoder/ac-library@v1.5.1/atcoder/math.hpp

Provides the standard exact integer floor_sum(n,m,a,b)=sum_{i=0}^{n-1} floor((a i+b)/m), with O(log m) Euclidean complexity, plus modular inverse. It is a base-case reference and implementation check; it does not establish geometric weights or Fibonacci factors.

### Babichev & Babichev, *Counting All Lattice Rectangles...*
URL: https://arxiv.org/html/2604.22456v2

Lemmas 4–5 and Corollary 6 establish closure of a constant-size family of polynomially weighted floor moments under affine normalization and reciprocal Euclidean steps, with O(log n) evaluation. This independently supports the finite-state/O(log) principle. Its moments are polynomial-index weighted rather than geometric, so it corroborates the method but does not replace the fhq geometric-weight source.

## Sources useful only as corroboration/catalogue

Berstel's Sturmian surveys corroborate the Sturmian/Fibonacci classification and complexity. Wikipedia's Fibonacci-word page explicitly lists the four length-3 factors and complexity n+1, useful as a check but encyclopedic rather than primary. OEIS A003849/A213975 catalogue Fibonacci words/subwords; they do not prove the O(log) evaluator and are not needed for the derivation. Three-distance, least-period, standard-factor, singular-word, automatic-sequence, and Ostrowski references concern related structure but do not directly evaluate Psi; they are background only. The automatic-sequence decision papers do not apply because the Fibonacci word is not a finite-base automatic sequence for this task.

## Contradictions and limits

Recall contains an important convention warning confirmed by Perrin: using slope 1/phi instead of 1/phi^2 models the complemented rabbit word and can give the wrong factor set. The sources do not contradict the working Sturmian/mechanical/universal-Euclidean route, but none of them alone proves the complete Psi reduction or the final residue; those remain computation-specific claims requiring executable verification.