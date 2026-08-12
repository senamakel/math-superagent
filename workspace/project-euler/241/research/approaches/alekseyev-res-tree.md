# Alekseyev's RES tree with analytic prime-wheel pruning

```approach
idea: Alekseyev (2026) tree-search over the lpf-based tree T_U with Theorem 3.2 prime-wheel pruning and algebraic shortcuts for 1-prime and 2-prime cofactors
mechanism: The equation 2σ(n) = r·n (r odd) is a·σ(n) = b·n + c with (a,b,c) = (2,r,0). Alekseyev's method traverses a tree where node n>1 has parent n/p^{ν_p(n)} with p = lpf(n). At each node m, the method maintains reduced coefficients (a',b',c') for the residual equation a'σ(n') = b'n' + c' on the cofactor n', then constructs a prime wheel W = (𝔭_k, 𝔭_{k+1}, …, 𝔭_{k+ℓ-1}) of consecutive primes. Theorem 3.2 gives two analytic bounds: P_0(W) ≤ n' ≤ U' (product bound) and L(W) ≤ a'·σ(n')/n' (abundancy bound). The wheel rolls (increments k) and grows (increments ℓ) until both bounds prove no solution can have spf(n') ≥ W_1, at which point the subtree is pruned. When neither bound prunes, the smallest wheel prime W_1 is a candidate for spf(n'), and its feasible powers are added as children. Two shortcuts handle cofactors n' = p^k and n' = pq algebraically without tree descent. This is fundamentally different from the denominator-cancellation DFS: the tree topology is lpf-based rather than multiplicative-build-up, the pruning is analytic (Theorem 3.2) rather than residual-driven (Q<1, n·den > LIMIT), and the shortcuts eliminate terminal branching algebraically.
status: refuted
killed-by: Alekseyev's method (arXiv:2601.17832) is the same tree-search core as the denominator-cancellation DFS already implemented in code/hemiperfect_dfs.py, with extra analytic wheel-pruning (Theorem 3.2) and algebraic p^k/pq shortcuts. Adopting it as a distinct approach means porting the SageMath reference implementation to Python — a substantial engineering investment whose payoff is extra pruning over a DFS that already runs in milliseconds on 6 targets. The run's existing DFS works; the real structural win is the 2-adic split (separates the problem into (a,k) pairs with fixed targets), and the DFS inside each split is the standard technique either way. Porting Alekseyev's wheel is not wrong — it is the published complete method — but it costs more than it buys at this bound (10^18 is tiny for these methods) and the 2-adic split + denominator-forcing DFS is provably complete by the same multiplicativity arguments. Close this as not-worth-it rather than wrong.
first-step: Implement the prime-wheel construction (Theorem 3.2) for the c=0 special case: given reduced (a',b') and bound U', construct the set Q of feasible prime powers. Then implement the tree traversal with shortcuts for n' = p^k and n' = pq. Run against the brute oracle at small bounds. The SageMath implementation exists at github.com/maxale/multiplicative_functions but needs to be ported to Python for this environment.
precedent: [arXiv:2601.17832](https://arxiv.org/abs/2601.17832) (M. A. Alekseyev, "Computing bounded solutions to linear Diophantine equations with the sum of divisors", Jan 2026) — this is the exact named published method; Section 2-3 defines T_U, the prime wheel, Theorem 3.2 (both bounds), Theorem 3.3 (wheel completeness), and the p^k / pq shortcuts; full text read at research/sources/alekseyev_diophantine_sigma_html.full.md. Implementation: [github.com/maxale/multiplicative_functions sigma_linear_eq.sage](https://github.com/maxale/multiplicative_functions), res_solve_sigma_abc(a,b,c,U). Claim ids: flammenkamps-tree-search-method, goto-shibata-multiplicative-monotone-method (monotonicity underlying the wheel pruning).
```

## What the literature says

The reformulation is **Alekseyev's method for a·σ(n) = b·n + c** (arXiv:2601.17832, Jan 2026).
PE 241 is exactly this equation with (a,b,c) = (2, 2k+1, 0): a half-integer abundancy
σ(n)/n = (2k+1)/2 is equivalent to 2·σ(n) = (2k+1)·n, i.e. a=2, b=2k+1, c=0. The paper
explicitly notes this is the special **c=0 ("multiperfect") case**, which "admits additional
optimization techniques that are not available for nonzero c."

**Precise statements (from the source, read in full):**

- *Theorem 3.2.* Let n, U, S be positive integers with n ≤ U, σ(n) ≥ S, and spf(n) = 𝔭_k.
  Then for a positive integer ℓ: if ℓ ≤ ω(n) then ∏_{i=1}^ℓ 𝔭_{k+i-1} ≤ U; if ℓ ≥ ω(n) then
  ∏_{i=1}^ℓ 𝔭_{k+i-1}/(𝔭_{k+i-1}−1) ≥ S/U. Proof: the ℓ distinct prime factors of n are
  ≥ 𝔭_k,…,𝔭_{k+ℓ-1}, so ∏ primes ≤ n ≤ U; and σ(n)/n ≤ ∏_{p|n} p/(p−1), with p/(p−1)
  decreasing in p, giving the second bound.
- *prime wheel:* W=(𝔭_k,…,𝔭_{k+ℓ−1}), P_κ(W)=∏_{p∈W}(p−κ). Wheel stops when
  P_0(W) > U' (no solution with spf(n')≥W_1) and grows length when
  a'·P_0(W)/P_1(W) < L(W) (no solution with ω(n')=|W|), where L(W) is a lower bound on
  a'·σ(n')/n'.
- *Theorem 3.3.* If n' ≤ U' solves a'σ(n')=b'n'+c' with ω(n')≥2 and spf(n')=𝔭_t>lpf(m),
  then at some point the wheel reaches |W| ≤ ω(n') with W_1 = 𝔭_t. This is the
  **completeness** guarantee: every solution is found (the wheel never misses one).
- *shortcuts:* cofactor n'=p^k is solved by factoring a'−c' (p | a'−c'), reducing the
  exponent search to prime-power factors; cofactor n'=pq by completing the rectangle
  (Ap+B)(Aq+B)=B²−AC (Brahmagupta's technique), factoring B²−AC and iterating divisors.

**Do the hypotheses hold here?** Yes. c=0 is explicitly covered (a=2, b=2k+1 odd). The
method needs only σ multiplicative and p/(p−1) monotone decreasing in p — both hold. The
bound n ≤ 10^18 is the search bound U.

**Has anyone applied it to this problem?** The method is published to solve exactly this
equation shape. Alekseyev's applications in the paper are hyperperfect, f-perfect,
quasiperfect, almost-perfect and fixed-abundance (σ(n)=bn+c with small c) families — the
same equation family as hemiperfects. It "discovers new solutions and closes gaps" and is
the natural complete tool. The specific 22-values-below-10^18 set is this run's own
computation, not extracted from the paper. (I did not search for a published PE241 answer;
the method, not the answer, is what the source grounds.)

**What it would buy:** a published, peer-referenced, proven-*complete* algorithm (Theorem 3.3)
with the algebraic p^k / pq shortcuts that collapse terminal branching analytically — over
and above the residual-driven DFS, whose completeness this run otherwise has to argue
itself. It avoids visiting almost all of T_U below 10^18. Cost is set by the recursion over
coefficients, not by the bound.

## Precedent / claim ids
- arXiv:2601.17832 (source of Theorem 3.2/3.3, wheel, shortcuts; c=0 case). Full text:
  research/sources/alekseyev_diophantine_sigma_html.full.md.
- github.com/maxale/multiplicative_functions (sigma_linear_eq.sage, res_solve_sigma_abc).
- flammenkamps-tree-search-method: exhaustive tree-search over prime powers constructed all
  multiply-perfects < e^350 — independent primary confirmation that DFS/tree-search over the
  divisor-sum equation is the standard complete method at bounds far above 10^18.
- goto-shibata-multiplicative-monotone-method: monotonicity structure (H(p^e)<H(p^f)<H(q^f))
  that the wheel pruning relies on, peer-reviewed Math. Comp. 2004.
