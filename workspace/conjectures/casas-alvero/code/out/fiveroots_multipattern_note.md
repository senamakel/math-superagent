# Five-roots multipattern rung — verdict

The first executable step of the five-distinct-roots rung of Casas-Alvero over
Q: classify multiplicity patterns by whether the pure multiplicity-plus-centroid
mechanism alone can satisfy the derivative-sharing hypothesis.

```claim
status: checked
what: No 5-distinct-root multiplicity pattern for n=5..10 is satisfiable
      through the pure multiplicity+centroid mechanism; every one is
      RULED-OUT at i = m_1 (max multiplicity) and in particular at i = n-2.
where: f monic of degree n, f = prod_{j=1..5} (x - alpha_j)^{m_j}, alpha_j
      pairwise distinct, all m_j >= 1.  i=n-2 needs a root of multiplicity
      >= n-1, impossible since 5 positive parts sum to n (max mult <= n-4).
basis: code/roots5/multipattern.py, ALL CHECKS PASSED, exit 0,
      captured code/out/fiveroots_multipattern.captured.txt.  Mechanism (1)
      (f^(i)(a)=0 iff i<m, = m! g(a) != 0 at i=m) verified exactly with sympy
      and the guaranteed covering direction cross-checked against the oracle
      lib.casas_alvero.is_ca; mechanism (2) (centroid: f^(n-1) = n!(x-c),
      c = (1/n) sum m_j alpha_j, so i = n-1 forces c = alpha_k) verified
      exactly.
consequence: No 5-root pattern is ALIVE under the multiplicity mechanism.
      Survival of any pattern rests on a NON-multiplicity (higher-order)
      coincidence — a root alpha_j with f^(i)(alpha_j) = 0 for some i >= m_1,
      in particular f^(n-2)(alpha_j) = 0 despite m_j <= n-2.  That is exactly
      the open content of CA at this rung; not settled here.
```

Headline: purely by the multiplicity-plus-centroid mechanism, **no pattern with
exactly 5 distinct roots survives** — every pattern fails at i = m_1 (the max
multiplicity), and specifically i = n-2 is never multiplicity-witnessed because
five positive parts summing to n give max multiplicity at most n-4 < n-1. Any
CA counterexample with five distinct roots, if it existed, would have to be a
*coincidence* beyond multiplicity: some alpha_j must satisfy f^(i)(alpha_j) = 0
for i >= m_1 despite m_j <= i. The rung therefore reduces to whether such
higher-order coincidences can occur — which this step does not resolve.

Mechanisms verified (not assumed):
- (1) a root a of multiplicity m in f has f^(i)(a) = 0 iff i < m; at i = m,
  f^(m)(a) = m! g(a) != 0 where g = f/(x-a)^m and g(a) != 0. For i > m the
  value C(i,m) m! g^(i-m)(a) can vanish only accidentally.
- (2) centroid: f^(n-1) = n! (x - c) with c = (1/n) sum m_j alpha_j, so the
  i = n-1 hypothesis forces f(c) = 0, i.e. c equals one of the roots.
