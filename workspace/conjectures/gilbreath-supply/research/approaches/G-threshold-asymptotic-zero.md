```approach
idea: Prove the pure F₂/hypergeometric limit (1/n) Σ_{d=2}^{n-1} K_w(2^popcount(d); n) / C(n,w) → 0 for every fixed θ = w/n ∈ (0, 1/2). This is exactly the statement that the exact mean of ν₂ over weight-w strings vanishes at any fixed positive density, and it is the mathematical core of w*/n → 0. No primes enter.
mechanism: The fold's row weights are the powers of two 2^popcount(d) (d ∈ [2,n-1]), and the Krawtchouk route expresses the exact weight-w mean of ν₂ as the normalized sum of K_w over those row weights. Fixed θ keeps w = θn proportional to n, so the question is a single Krawtchouk/hypergeometric asymptotics problem on the multiset of row weights.
status: grounded
precedent: >
  Harrow–Kolla–Schulman, Dimension-free L^p maximal inequalities on the
  hypercube, Theory of Computing 10 (2014) 55–78, DOI 10.4086/toc.2014.v010a003,
  Lemma 2.2: |κ_k^n(x)| = |K_k(x;n)/C(n,k)| ≤ e^{-c·k·x/n} for 0 ≤ k ≤ x ≤ n/2
  — the exact normalized Krawtchouk ratio K_w(2^pc(d);n)/C(n,w) decaying
  superexponentially on the large (2^pc(d) ≥ θn) cells; hypotheses hold.
  Greenblatt–Kolla–Krause, arXiv:1406.7229, Prop 3.5 (same bound, uniform).
  Greene–Wellner, Bernoulli 23 (2017) 1911–1952, DOI 10.3150/15-bej800, and
  Lahiri–Chatterjee, Proc. AMS 135 (2007), DOI 10.1090/s0002-9939-07-08676-5
  (hypergeometric log-concavity/unimodality, mode atom O(1/√Var) — the bounded
  (non-large) cell half). In-workspace: claim sphere-mean-krawtchouk-exact;
  note grounding_threshold_lemmas_krawtchouk.md.
first-step: Assemble the rigorous o(n) proof from HKS Lemma 2.2 (large cells,
  superexponential decay) + the hypergeometric mode bound (mid/small cells) +
  the popcount-group count C(⌊log₂n⌋,k); the three-group decomposition
  (small / mid-peak-n^{3/4}/√log n / large-HKS) is written in
  grounding_threshold_lemmas_krawtchouk.md. Tool_builder: evaluate the exact
  group sum Σ_k C(L,k)|K_w(2^k;n)|/C(n,w) at θ∈{1/32,1/16,1/8,1/4}, n=2^8..2^20
  and print ratio/n (must fall to 0).
```

