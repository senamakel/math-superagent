# Proof skeleton: Project Euler 1006

```skeleton
goal: Compute Ψ(10^18) mod M, where M=101001001 and Ψ(k)=Σ_{w∈F_k} N(w)^2; F_k is the set of distinct contiguous length-k factors of S_n (S_0=0, S_1=01, S_n=S_{n-1}S_{n-2}), and N(w) is the binary word w interpreted as a decimal numeral.
implies: G1 identifies F_k with the length-k factors of the infinite Fibonacci fixed point and supplies its cardinality k+1. G2 parametrises those factors by the k+1 mechanical/rotation intercepts. G3 rewrites each decimal value as an affine geometrically weighted floor expression. G4 then provides a correct fixed-dimensional Euclidean/Ostrowski recursion for the joint intercept-and-position second moment in O(log k); substituting k=10^18 and reducing modulo M gives the requested answer. The implications are by successive substitution: G1→G2 identifies the summation domain, G2→G3 changes each summand, and G4 evaluates exactly the resulting finite sum.
status: live
rests-on: governing-sturmian, fibonacci-sturmian-complexity, governing-factor-complexity, g1-factor-chain-nested, mechanical-word-digit-rule, g2-mech-shell-exact-binary, monoid-composition-formulas-verified, universal-euclidean-geometric-floor-sum
```

```gap
id: G1-finite-subword-limit-identification
lemma: For every k≥1, the union over n of the length-k factor sets of S_n is exactly the length-k factor set of the infinite Fibonacci fixed point, and this set has cardinality k+1.
status: discharged
discharged-by: g1-factor-chain-nested, fibonacci-sturmian-complexity, governing-sturmian, governing-factor-complexity
next: Already discharged in the claim library; the remaining Lean `sorry` is a formalisation-status issue, not a new mathematical gap for this skeleton.
```

```gap
id: G2-mechanical-factor-parametrisation
lemma: For every k≥1, the k+1 factors in G1 are exactly the binary words d_0(x_m)…d_{k-1}(x_m), where d_j(x)=⌊x+(j+1)α⌋−⌊x+jα⌋, α=1/φ², and x_m is one representative from each arc cut by {frac(−mα):0≤m≤k}; equivalently a sufficiently large Fibonacci rational convergent gives the same length-k factor set.
status: discharged
discharged-by: governing-sturmian, mechanical-word-digit-rule, g2-mech-shell-exact-binary
next: Already discharged; the finite evaluator is regression evidence only.
```

```gap
id: G3-telescoped-decimal-second-moment
lemma: For every mechanical representative x, with v(x)=Σ_{j=0}^{k−1}d_j(x)10^{k−1−j}, one has v(x)=⌊x+kα⌋−10^{k−1}⌊x⌋+9Σ_{j=1}^{k−1}10^{k−1−j}⌊x+jα⌋; consequently Ψ(k)=Σ_{m=0}^k v(x_m)^2.
status: discharged
discharged-by: g3-telescoped-second-moment
next: Already discharged by the elementary telescoping identity and checked implementation.
```

```gap
id: G4-joint-intercept-evaluation
lemma: For the rational Fibonacci convergent a=p/q used for length k (q>k+2), there is an explicitly defined state of dimension independent of k and an exact Euclidean/Ostrowski composition, using O(log k) quotient/block compositions and arithmetic modulo M, whose output is J(a,k)=Σ_{m=0}^{k}v_a(m)^2, including the coupled m,j boundary and carry terms; this output equals Ψ(k) and is stable when a is replaced by any sufficiently deep convergent.
status: open
next: Define the state and its composition in `code/lean/G4Statement.lean` (the current fixed-dimensional theorem is intentionally `sorry`), then have a theorem prover check the composition identity and have tool_builder test the resulting evaluator against the exact mechanical oracle for k=1,2,3,…,150, followed by anchors k=10^4 and k=10^6. A smallest-case failure refutes the proposed state; passing tests is only evidence until the composition proof is completed.
```
