# PE1006 reference-library digest

## Sources that bear directly

- [[cambridge-lothaire-sturmian-chapter.primary.full]] — Lothaire, *Sturmian Words*, DOI https://doi.org/10.1017/CBO9781107326019.003. The chapter summary states that Sturmian words are exactly binary infinite words with n+1 factors of length n, and that the class is equivalently balanced aperiodic words and irrational mechanical/rotation codings. The Fibonacci morphism fixed point is Sturmian. Thus the problem's F_k has exactly k+1 elements and floor-difference/rotation coding is justified. It does not establish the weighted decimal second-moment aggregation for k=10^18.

- [[perrin-sturmian-words-lecture2-mechanical.full]] — Perrin's lecture gives the exact lower mechanical word s_{alpha,rho}(n)=floor(alpha(n+1)+rho)-floor(alpha n+rho), proves digits are binary for 0<=alpha<=1, identifies rotations, and states that all intercepts of one irrational slope have the same factor set. It also identifies the Fibonacci word as characteristic of slope 1/tau^2. Applied here, it supplies the exact arithmetic representation of factors. It does not supply a fast sum over all intercept cells with decimal weights.

- [[berstel-vuillon-coding-rotations.full]] — Berstel–Vuillon prove that codings of irrational rotations can be recoded by Sturmian words of the same angle; their Proposition 6.1 gives the interval-state transition j = i + |K| modulo m+1 for the finite interval partition automaton. This supports finite-state rotation coding and possible aggregation, but the paper treats finite interval codings/automata and does not prove the PE1006 weighted second-moment collapse.

- [[sivasankar-rama-fibonacci-factors-2022.full]] — The 1D portions enumerate and locate Fibonacci factors using substitution into finite blocks. Theorem 4 gives location sets of length-l factors from length-m and length-(m+1) block factors, with explicit affine maps of occurrence positions and boundary cases. This can support bounded factor generation/location checks and block-boundary analysis. It does not give a distinct-factor weighted sum for decimal values at astronomical k; duplicate factors and boundary corrections remain important.

- [[oi-wiki-universal-euclidean-floor-sum.full]] — The universal Euclidean algorithm represents an affine floor-line operation sequence in a monoid, recursively reduces parameters by Euclidean quotients, and uses binary exponentiation. The source states O(log max{a,c}+log(b/c)) complexity when monoid multiplication is O(1). It also explicitly gives a contribution monoid maintaining sum floor, weighted x-floor, and sum floor^2 (and explains higher mixed moments). Applied here, it can evaluate one affine floor path or a fixed-dimensional set of moments exactly, but it does not establish aggregation over the k+1 PE1006 intercepts. The source is an algorithmic reference, not a complete solution.

- [[peltomaki-sturmian-repetitions.full]] — Peltomäki gives continued-fraction/three-distance and repetition results for Sturmian factors. These are not needed for Psi's decimal second moment; no direct usable theorem for this objective was found.

## Contradictions / corrections

The library's earlier claim that a pair-correlation collapse C(j,j')=A(j'-j) holds generally is contradicted by executed evidence in `code/out/solution_checks.md`: it already fails at k=3, j=j'=1, and the resulting Psi is wrong. The claim is therefore valid only in restricted Fibonacci-length regimes, not for arbitrary k. Likewise, the 1D block-summary closure proposal is refuted by `code/out/current_attempt_report.md`: blocks 01 and 10 have equal scalar summaries but appending 0 produces different value statistics.

The current durable status remains: brute and bounded mechanical/window routes verify the anchors, but no proved O(log k) joint-intercept aggregation and no honest value for Psi(10^18) are available. The source library does not contain a published Project Euler answer and none was searched.

## Sources that do not help directly

The automatic-sequence decision-procedure sources do not apply: the Fibonacci word is not a k-automatic sequence in the required decimal/base-10 sense, and decision procedures do not compute the weighted sum. Repetition, least-period, Christoffel-conjugacy, three-distance, and factor-catalogue sources provide context or auxiliary structure but no missing aggregation theorem. The 2D Fibonacci-array parts of Sivasankar–Rama are irrelevant to this 1D objective.
