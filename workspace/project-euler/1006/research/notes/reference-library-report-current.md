# Reference-library report against PE1006

Memory storage was unavailable in this run (remember_memory timed out/health failure), so this durable workspace note records the verified source digest pending a later retry.

## Directly load-bearing sources

### Project Euler statement
[[project-euler-1006-statement.full]] — https://www.projecteuler.net/minimal=1006
Defines `S_0=0`, `S_1=01`, `S_n=S_{n-1}S_{n-2}`; Fibonacci subwords are contiguous factors of some `S_n`; `Psi(k)` sums squares of the decimal interpretations of the `k+1` distinct length-`k` factors. It gives `Psi(3)=20302`, `Psi(10)=10699667 mod 101001001`, and asks for `Psi(10^18) mod 101001001`. This establishes the oracle and target, not an algorithm.

### Perrin mechanical/Sturmian lecture
[[perrin-sturmian-words-lecture2-mechanical.full]] — http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture2/slides2.pdf
Defines the lower mechanical word `s_(alpha,rho)(n)=floor((n+1)alpha+rho)-floor(n alpha+rho)`, identifies it with irrational rotation coding, and states that all intercepts of a fixed irrational slope have the same factor set. It states the Morse–Hedlund equivalence between Sturmian words and irrational mechanical words. Applied here, the Fibonacci fixed point is the characteristic word of slope `alpha=1/phi^2=(3-sqrt(5))/2`; factors can be indexed by rotation intervals. The source does not derive Psi or the decimal moment reduction.

### Lothaire / Perrin–Restivo / Morse–Hedlund complexity
[[lothaire-sturmian-words-C2.full]], [[perrin-restivo-sturmian-words.full]], and the original https://www.jstor.org/stable/2371261 support the standard theorem: an irrational Sturmian word has exactly `p(k)=k+1` distinct contiguous factors of length `k`. The readable Perrin material is the operational source; Lothaire's downloaded PostScript is not readable at theorem-page level, so specific claims attributed only to it remain unchecked here. This theorem exactly justifies the problem's `k+1` summands.

### Berstel–Vuillon rotation coding
[[berstel-vuillon-coding-rotations.full]] — https://arxiv.org/abs/math/0106217
Establishes coding irrational rotations as Sturmian/mechanical words under its interval hypotheses. It supports the rotation model, but not the exact arc-midpoint indexing or Psi evaluation.

### Sivasankar–Rama factor-location theorem
[[sivasankar-rama-fibonacci-factors-2022.full]] — https://arxiv.org/html/2207.04304
States a one-dimensional Fibonacci position theorem: for `F(n)<=k<F(n+1)`, the `k+1` factors are prefixes of rotations of a finite Fibonacci word at an explicit front block plus tail block of positions. Their convention is the complemented/rabbit word, so indices require translation and small-case checking. This supports a finite contiguous-window oracle/reformulation, not a polylogarithmic Psi evaluator and not the decimal square-moment collapse.

### AtCoder floor_sum
[[atcoder-floor-sum-editorial]], [[atcoder-math-hpp-v151]] — https://atcoder.jp/contests/practice2/editorial/579 and https://atcoder.github.io/ac-library/production/document_en/math.html
The ordinary floor sum `sum_{i=0}^{n-1} floor((ai+b)/m)` reduces by a reciprocal Euclidean identity and runs in `O(log max(a,m))`; ACL also supplies exact modular inverse/power primitives. This is only the unweighted base primitive and does not cover geometric weights or PE1006's factor aggregation.

### Universal Euclidean geometric/moment sources
[[oi-wiki-universal-euclidean-floor-sum.full]] — https://oi.wiki/math/number-theory/euclidean/
[[universal-euclidean-geometric-weight-fhq.full]] — https://www.cnblogs.com/dixiao/p/15719155.html
[[loj138-universal-euclidean-floor-moments.full]] — https://www.cnblogs.com/AThousandMoons/p/13129167.html
Together these describe the operation-string/monoid Euclidean recursion. OI-Wiki gives exact U/R merge and reciprocal steps with logarithmic Euclidean depth. The FHQ note extends to geometric weights and a fixed six-component monoid tracking first/second floor moments. LOJ138 gives a binomial moment-array merge. Applied here, these are candidate primitives for sums such as `sum q^i floor((ai+b)/c)^r`, `r<=2`, after the mechanical-word reduction. They establish the primitive, not the missing joint aggregation over all `k+1` intercepts. The FHQ/LOJ sources are informal notes rather than peer-reviewed proofs; the recursion must be checked against the brute oracle.

### Cobham/Frougny and Fibonacci-automatic sources
[[frougny-mult-dep-linear-numeration-2002-irif.full]] — https://www.irif.fr/~cf/publications/lucas.pdf
establishes finite-automaton conversion restrictions for multiplicatively dependent Pisot numeration systems. Since `10` and `phi` are multiplicatively independent, it rules out the proposed finite-automaton Zeckendorf-to-decimal conversion route. It does not rule out exact Euclidean arithmetic.
[[fibonacci-automatic-decision-algorithms-numdam.full]] — https://www.numdam.org/item/ITA_2016__50_1_39_0.pdf
establishes decidability and many structural Fibonacci-word facts, including unique special factors, but does not evaluate Psi. Its automatic framework is adjacent, not a solution.
[[ostrowski-numeration-addition-finite-automata.pdf.full]] — https://arxiv.org/pdf/1407.7000
establishes finite-automaton addition for quadratic Ostrowski numeration; it does not supply decimal-weighted moment aggregation. Combined with Frougny, it explains why the tempting finite transducer route is blocked.

## Useful checks, but not a solution

- O'Bryant, [[obryant-sum-heights-sturmian-factors.full]], https://doi.org/10.48550/arxiv.math/0611365: parity of the sum of heights of the `k+1` factors equals `k`; useful invariant only, no decimal second moment.
- Hamoud–Abdullah survey, [[hal-05026908-fibonacci-word-complexity-survey.full]], https://hal.science/hal-05026908v1/document: supports complexity, density `1/phi^2`, and balance. It contains a convention inconsistency: another theorem states `phi-1`; that is the complementary-letter convention and must not replace PE1006's slope.
- Binner, [[binner-reciprocity-floor-square-functions.full]], https://arxiv.org/pdf/2107.08308: Euclidean reciprocity for unweighted floor squares; no geometric weights or Fibonacci factors.
- Patricio–Hartwig, [[patricio-hartwig-euclid-corner-sums.full]], http://elib.mi.sanu.ac.rs/files/journals/flmt/177/flmn177p4613-4636.pdf: generalized Euclidean/corner and geometric-sum identities; no complete Psi reduction.
- Babichev–Shpakova, [[babichev-shpakova-weighted-floor-moments-2026.full]], https://arxiv.org/html/2607.17961v1: an exact `O(n log n)` lattice-rectangle algorithm using weighted floor moments, not polylogarithmic in the queried bound and not a Psi theorem.
- Rauzy factor-frequency source: bounds numbers of factor frequencies in low-complexity reversal-closed words; no decimal values or Psi algorithm.
- Cassaigne's Fibonacci extremal-properties source concerns recurrence/repetitions/palindromes; no Psi evaluation.

## Contradictions and limits

The library's durable investigation says the current finite `solution.py` and directive-9 evaluator are `O(k)` and lack a proved joint Fibonacci-block boundary state; no honest `Psi(10^18)` residue has been computed. This contradicts any earlier unverified claim that old finite evaluators or phase-4 residues solved PE1006. Specifically, old residues `16242174` and `77578256` are recorded invalid; `34432237` and `20938836` are only finite anchors, not a target answer. The `1/phi` versus `1/phi^2` slope discrepancy in several sources is a convention issue, not evidence for changing PE1006's slope.

No source in the library establishes the missing fixed-dimensional recurrence jointly aggregating all intercepts and decimal cross terms. Scaling the existing O(k) evaluator would only test more finite cases and cannot settle that structural gap.
