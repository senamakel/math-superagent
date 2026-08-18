# Collatz reference library root

Updated 2026-08-18. The canonical statement is the positive-integer map `C(n)=3n+1` for odd n and `n/2` for even n; equivalently use accelerated `T(n)=(3n+1)/2` on odd n and `n/2` on even n. The conjecture remains open: a proof must exclude both unbounded orbits and nontrivial cycles.

## Minimal counterexample / obstruction structure
A hypothetical counterexample is either an unbounded orbit or a nontrivial cycle. For a nontrivial cycle, parity/odd-step counts impose a near relation between powers of 2 and 3; cycle arguments therefore use congruences, continued fractions, and logarithmic Diophantine approximation. Hercher's m-cycle framework defines m as the number of local minima and proves no m-cycle for m≤91; conditional on convergence verification through `3·2^69`, every nontrivial cycle has more than `1.375·10^11` odd members. These are sourced claims, not a proof of the conjecture.

## Current computation
Barina et al. (Journal of Supercomputing, 2025, DOI `10.1007/s11227-025-07337-0`) report verification that every start `n≤2^71` reaches the trivial cycle. Their method combines CPU baseline checking, 3^k and 2^k sieves, congruence-class parallelism, GPU acceleration, and distributed computation. This is verified numerically by that project, not a universal proof.

## Three settled restricted classes / reductions
1. **Every arithmetic progression is sufficient** for the accelerated map: every positive orbit merges with an orbit starting in any fixed nonconstant progression `A+Bℕ` (Monks 2006, Theorem 1.1). Thus proving convergence on one progression would imply convergence everywhere.
2. The same sufficiency holds separately for the divergent-orbit and nontrivial-cycle sub-conjectures (Monks 2006, Corollaries 1.2–1.3).
3. **No nontrivial m-cycle with m≤91** (Hercher 2023, Theorem 23), using cycle inequalities and continued fractions. This is a restricted cycle class, not all cycles.
4. **Almost-all result:** Tao proves that for every unbounded `f`, the orbit minimum is `<f(N)` for logarithmic-density-one many N. This does not exclude a density-zero exceptional orbit, divergence, or a nontrivial cycle.

## Failed/limited approaches
- Random-walk and density arguments control typical orbits, not every orbit.
- Natural/arctic matrix-interpretation termination proofs fail for the full rewrite-system encoding (Yolcu–Aaronson–Heule 2023); automated tools prove weakenings only.
- Generalized Collatz-like systems can be computationally undecidable, so unrestricted generalization is not a direct route to this specific map.

## Sources
Primary and canonical sources are held under `research/sources/`; short digests are under `research/summaries/`. Key files: `barina-2025-verification-2p71-doi.full.md`, `lagarias-3x1-overview.full.md`, `tao-almost-all-orbits.full.md`, `monks-2006-sufficiency-arithmetic-progressions.full.md` (if present), `hercher-2023-no-collatz-m-cycles-jis-published.full.md`, `encyclopedia-of-mathematics-syracuse-problem.html.full.md`, and `wikipedia-collatz-conjecture-encyclopedic.full.md`. URLs are recorded in each summary/source header.
