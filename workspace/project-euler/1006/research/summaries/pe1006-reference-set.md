# PE1006 reference-set digest

The local source set was read against the problem. Full texts are linked below.

## Directly applicable theory

- [[lothaire-sturmian-words-primary-2026.full]] and [[perrin-sturmian-words-lecture2-mechanical.full]] establish the relevant language framework: the limit of S0=0, S1=01, Sn=Sn-1Sn-2 is the characteristic Fibonacci Sturmian/mechanical word with slope alpha=1/phi^2=(3-sqrt(5))/2. Lower mechanical digits are floor((n+1)alpha+rho)-floor(n alpha+rho); factor cylinders are rotation intervals; same irrational slope gives the same factor language; Sturmian complexity is exactly k+1. These sources directly justify the object set, but not Psi(k).
- [[berstel-vuillon-coding-rotations.full]] supports irrational-rotation coding as a source of Sturmian words under its stated hypotheses. It does not establish the particular PE1006 intercept representatives or the second moment.
- [[chuan-fibonacci-words-fq1992.full]] proves that finite labelled Fibonacci words are cyclic shifts of a standard word (Theorems 6–7), giving useful checks at special Fibonacci lengths. It does not solve general k.
- [[sivasankar-rama-fibonacci-factors-2022.full]] studies factor enumeration/location, but the digest does not expose a clean one-dimensional theorem sufficient for the exact general-k window formula; do not overclaim it.
- [[cassaigne-extremal-properties-fibonacci-word-2008.full]] proves the Fibonacci first-occurrence quotient rho'*=phi+1, so a prefix of asymptotic length about 2.618k contains all length-k factors. This supports the small brute oracle only.

## Geometry-only sources

[[alessandri-berthe-three-distance-theorems.full]] and [[van-ravenstein-three-gap-theorem-1988-hal.full]] establish at-most-three orbit gaps with continued-fraction recurrences and the link from rotation interval lengths to Sturmian factor frequencies. They explain the intercept geometry but do not provide the exact Psi aggregation. Rauzy frequency bounds, Obryant's parity theorem, and generic Fibonacci recurrence/repetition sources likewise do not give Psi.

## Arithmetic sources

[[oi-wiki-universal-euclidean-floor-sum.full]], [[universal-euclidean-geometric-weight-fhq.full]], and [[loj138-universal-euclidean-floor-moments.full]] establish the universal Euclidean monoid recursion: affine floor paths and fixed-size geometric-weight floor/floor^2 moments are evaluated by Euclidean quotient/flip steps in logarithmic coefficient complexity, independent of n. [[atcoder-internal-math-hpp.full]] and [[atcoder-math-hpp-v151.full]] independently anchor the ordinary O(log) floor_sum base case. These apply to the inner arithmetic after, and only after, proving the missing aggregation over all k+1 intercepts.

## Non-helpful sources and caveats

Berstel's Fibonacci survey file contains only an abstract, not a citable theorem. Chuan's 2003 conjugacy moments concern special cyclic classes. Automatic/Cobham sources concern automatic decision procedures, not this non-automatic Fibonacci language. Babichev-Shpakova concerns lattice rectangles. A prior recalled pair-correlation identity is valid only at k=F_n-1, not arbitrary k; using it generally is a contradiction. The slope must be 1/phi^2, not 1/phi, because the latter is a complemented convention in some sources.

Memory indexing failed during this run, so this note is the durable local record awaiting later Cognee indexing.