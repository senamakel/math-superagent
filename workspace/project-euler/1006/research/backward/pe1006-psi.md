# Proof skeleton: PE1006 — Ψ(10^18) mod M

Canonical decomposition of the goal. G1–G3 discharged against the claims ledger; G4 is the run's only open gap.

```skeleton
goal: Compute Ψ(10^18) mod M for Project Euler 1006, where Ψ(k) = Σ_{x∈F_k} val(x)^2, F_k is the set of distinct length-k contiguous subwords occurring in some S_n (S_0 = 0, S_1 = 01, S_n = S_{n-1}S_{n-2}), val(x) = Σ_{j=0}^{k-1} x_j 10^{k-1-j}, and M = 101001001. Anchors: F_3 = {001,010,100,101}, so Ψ(3) = 20302; Ψ(10) ≡ 10699667 (mod M).
implies: An exact substitution chain — each link is an equality of finite quantities and rests on nothing outside `rests-on`. (1) G1 fixes the domain and cardinality: ⋃_n Fac_k(S_n) = Fac_k(f), the length-k factor set of the infinite Fibonacci word f (limit of the S_n), of size exactly k+1, so Ψ(k) = Σ_{u∈Fac_k(f)} val(u)^2. (2) G2 parametrises that domain: the k+1 factors are exactly the mechanical words of slope a — a Fibonacci convergent p/q of α = 1/φ² with q > k+2, which shares the length-k factor set with α — at intercepts x_m = -m·a, m = 0..k; substituting into (1), Ψ(k) = Σ_{m=0}^{k} v(x_m)^2, where v(x_m) is the decimal value of the m-th mechanical word. (3) G3 rewrites each summand by summation by parts over the digit differences d_j(x) = ⌊x+(j+1)a⌋ − ⌊x+ja⌋: v(x) = ⌊x+ka⌋ − 10^{k-1}⌊x⌋ + 9·Σ_{j=1}^{k-1} 10^{k-1-j}⌊x+ja⌋, so v(x)^2 expanded is a fixed linear combination of products ⌊x+ia⌋⌊x+ja⌋ with weights powers of 10 — Ψ(k) is a geometrically weighted joint second-moment floor sum over the (intercept m, position j) grid, and monoid-composition-formulas-verified evaluates any single intercept's contribution along a Euclidean path. (4) G4 supplies the k-independent aggregation: a fixed-dimensional state with associative composition evaluating the whole joint sum Σ_{m=0}^{k} v(x_m)^2 mod M exactly in O(log k) steps, with the output provably independent of the admissible convergent a — without that stability clause, instantiating the chain at k = 10^18 is not well-defined. Instantiating G4 at k = 10^18 yields the goal; the anchors Ψ(3) = 20302 and Ψ(10) ≡ 10699667 (mod M) check the chain end-to-end at small k.
rests-on: g1-factor-chain-nested, fibonacci-sturmian-complexity, governing-sturmian, governing-factor-complexity, mechanical-word-digit-rule, g2-mech-shell-exact-binary, monoid-composition-formulas-verified, farey-slope-stabilisation
status: live
```

```gap
id: pe1006-psi/G1-finite-subword-limit-identification
lemma: For every k ≥ 1, ⋃_n Fac_k(S_n) = Fac_k(f), where f is the infinite Fibonacci word (fixed point of the morphism 0→01, 1→0, the prefix-limit of the S_n), and |Fac_k(f)| = k+1.
status: discharged
discharged-by: g1-factor-chain-nested (formalised: the factor sets Fac_k(S_n) form a monotone nested chain, so the union stabilises), plus fibonacci-sturmian-complexity / governing-sturmian / governing-factor-complexity (Sturmian complexity p(k) = k+1); kernel-checked as the Lean theorem PE1006G1.fib_subword_count : ∀ k ≥ 1, (FibSubwords k).ncard = k+1
```

```gap
id: pe1006-psi/G2-mechanical-factor-parametrisation
lemma: For every k ≥ 1, the k+1 factors of G1 are exactly the binary words d_0(x_m)…d_{k-1}(x_m), where d_j(x) = ⌊x+(j+1)a⌋ − ⌊x+ja⌋, a = p/q is a Fibonacci convergent of α = 1/φ² with q > k+2 (such a convergent shares the length-k factor set with α), and x_m = -m·a for m = 0..k.
status: discharged
discharged-by: governing-sturmian (f is the characteristic Sturmian word of slope 1/φ²) + mechanical-word-digit-rule (all mechanical words of one slope have the same factor set; the arc-midpoint intercepts enumerate it) + g2-mech-shell-exact-binary (exact binary-digit shell, kernel-checked); machine-checked mech_psi == brute for k = 1..400
```

```gap
id: pe1006-psi/G3-telescoped-decimal-second-moment
lemma: For every mechanical representative x with digits d_j(x) = ⌊x+(j+1)a⌋ − ⌊x+ja⌋ and value v(x) = Σ_{j=0}^{k-1} d_j(x)·10^{k-1-j}, one has v(x) = ⌊x+ka⌋ − 10^{k-1}⌊x⌋ + 9·Σ_{j=1}^{k-1} 10^{k-1-j}⌊x+ja⌋; hence Ψ(k) = Σ_{m=0}^{k} v(x_m)^2 is, after expanding, a fixed linear combination of products ⌊x_m+ia⌋⌊x_m+ja⌋ with coefficients powers of 10 — a geometrically weighted joint second-moment floor sum over the (intercept m, position j) grid, per-intercept evaluable along a Euclidean path.
status: discharged
discharged-by: the telescoping identity is an algebraic summation-by-parts over the digit differences (mechanical-word-digit-rule supplies the digit formula); it is verified as formulation (B) of code/mech/mech_psi.py, captured in code/out/mech_psi.captured.txt: (A)==(B) in total and per-word multiset for k=1..400, reproducing Ψ(3)=20302 and Ψ(10)≡10699667 against brute. The per-intercept Euclidean evaluation of the resulting weighted second-moment floor sum is closed by monoid-composition-formulas-verified (proved: the composition law for the geometric second-moment floor-sum monoid over a Euclidean path).
```

```gap
id: pe1006-psi/G4-joint-intercept-evaluation
lemma: There exists an explicitly defined state σ(a,k) of dimension independent of k, with an associative composition ○ computable in time independent of k, such that Σ_{m=0}^{k} v_a(m)^2 mod M (M = 101001001) is computed exactly in O(log k) composition steps; and the value so computed is the same for every admissible convergent a (any Fibonacci convergent p/q of α with q > k+2), so that instantiating the chain of this skeleton at k = 10^18 is well-defined.
status: open
next: Attack the intercept–position coupling with the cheapest refuters on disk, in this order. (1) k = 1 — the single-intercept aggregation already fails there (code/out/pinning_k123.txt); any candidate state must first pass k = 1. (2) k = 2 — the additive block summary collides on the pair 010/101 (kernel-checked in code/lean/G4BlockStateNonClosure.lean); the candidate must distinguish that pair. (3) Only a state surviving both earns the k = 1..150 sweep against the brute-force Ψ, the valid anchors Ψ(10^4) ≡ 34432237 and Ψ(10^6) ≡ 20938836 (mod M), and the two-approximant 10^18 run (candidate residue ≡ 52 mod 100). The coupling to break is recorded in the reduction target pe1006-g4-diagonal-coupling: under the diagonal coordinate h = l−m the decimal weight w_l = 10^{k−1−l} = 10^{k−1−h}·10^{−m} keeps a geometric factor 10^{−2m} on m, and the window range l∈[0,k] becomes h∈[−m,k−m], which moves with m; the pair-correlation matrix C_k(j,l)=Σ_m g(j−m)g(l−m) is Toeplitz (a function of j−l) ONLY at k = F_n−1 (claim dir1-domain-autocorrelation), so a fixed-dimensional diagonal state is not available at general k. Raw material: the LOJ138 bivariate polynomial-moment node already on disk carries (x-power, floor-power) pairs with binomial translation, so the missing piece is a coordinate absorbing the outer sum over the k+1 intercepts. Routes NOT to re-propose (all recorded in reduction target pe1006-g4-diagonal-coupling, status identity): single-intercept universal-Euclidean aggregation (refuted at k = 1,2,3), the fixed additive block summary (collides at k = 2), and Toeplitz pair-correlation closure C_k(j,l) = T(j−l) (non-Toeplitz at general k; holds only at k = F_n − 1).
```
