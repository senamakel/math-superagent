# Ford, "Cycle type of random permutations: A toolkit" (Discrete Analysis 2022:9)

Kevin Ford. *Discrete Analysis* 2022:9, 36 pp, DOI 10.19086/da.38090; arXiv:2104.12019v3 (24 Apr 2021, rev 7 Sep 2022). Full text: L0 `ford_cycle_type_toolkit.full.full.md` (ar5iv HTML, 122 KB), URL https://ar5iv.labs.arxiv.org/html/2104.12019.

## What it establishes

Standard reference for the cycle type of a uniform random permutation σ ∈ S_n. Organizing principle: C_k = # cycles of length k behaves like independent Poisson(1/k), subject to the size constraint Σ k·C_k = n.

- **Exact factorial moments** (the precise exact form of the heuristic for bounded cycle counts):
  E[ ∏_k (C_k)_{r_k} ] = ∏_k k^{−r_k} whenever Σ_k k·r_k ≤ n, with (x)_r the falling factorial. This is the calculus that lets sums over S_n of functions of cycle counts telescope into simple products of powers.
- Sieve/Poisson approximations with explicit error terms for the count of cycles with lengths in an arbitrary set I (Poisson/CLT regime when Σ_{k∈I} 1/k grows), plus bounds on number of cycles, largest/smallest cycle, and fixed-set sizes.
- Number of fixed points: distribution converging to Poisson(1), with explicit error rates — the a₁ = #fixed-points input to both gap-affine inversion mechanisms already in the library.

## Why it matters for this run

memory.md reduces Q(n) to closed forms for A_n, B_n in f_n(k) = A_n + (k−1)B_n. The only unconditional exact handles on sums over cycle types are (i) conjugacy-class sizes n!/∏(k^{c_k} c_k!) and (ii) the factorial-moment identities above. Ford collects and re-proves (ii), plus the fixed-point-count facts used by [[pinsky_schickentanz_ewens_html]], in one place. Both candidate routes to A_n, B_n — the per-cycle-type gap-affine inversion probability of [[conjugacy_class_statistics_body]] and the fixed-point-count conditioning of [[pinsky_schickentanz_ewens_html]] — are cycle-type sums, and this is the canonical toolkit for evaluating them and for replacing them with Poisson asymptotics at n = 10⁶. Its §1 bibliography is also the map of the order-of-a-permutation literature (Erdős–Turán, Goh–Schmutz…), which governs the n!/ord(π) weights in brute2's period formula.

## Caveats

Tooling/reference only: no statement about powers π^k, cyclic subgroups {π^i}, inversion probabilities, or rank statistics. Its main theorems are asymptotic with rates; exactness at n = 10⁶ still requires the run's own summation.