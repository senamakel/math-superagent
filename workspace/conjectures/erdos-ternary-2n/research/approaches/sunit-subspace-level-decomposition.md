# S-unit / Subspace theorem level decomposition

```approach
idea: Reformulate the conjecture as *uniform-in-k* finiteness of the family of
  non-degenerate S-unit equations  2^n = sum_{a in A} 3^a,  |A| = k,  in the
  rank-2 multiplicative group U_{2,3} = {+-2^u 3^v}. For each fixed k the
  Subspace Theorem (Evertse-Schlickewei-Schmidt, Ann. of Math. 155 (2002)) proves
  finiteness of non-degenerate solutions, with an explicit bound in (k, rank);
  the whole conjecture is exactly the statement that this finiteness holds
  uniformly as k (the number of ternary 1s) varies.
mechanism: For ANY digit-2-free power 2^n = sum_{a in A} 3^a, the S-unit equation
  2^n - sum_{a in A} 3^a = 0 is *non-degenerate*: a vanishing proper sub-sum
  would force the complementary positive sum to vanish. Hence the Subspace bound
  applies at its level k. The conjecture becomes: uniformity of this finiteness
  as k varies.
status: refuted
killed-by: uniform-in-k finiteness of the non-degenerate S-unit equation is
  exactly the conjecture and has no precedent; the dual problem s_2(3^n)
  unbounded was settled by Baker-type linear-forms-in-log (Stewart 1980), not by
  a uniform Subspace bound, so the ESS per-level bound does not transfer to the
  growing support. The framing (non-degeneracy, rank-2 group U_{2,3}) is kept
  inside the adopted approach bertok-hajdu-cross-modulus-ladder; only its
  uniformity step is closed.
precedent:
  - "Non-degeneracy proved here (hand check): equation 2^n - sum_{a in A}3^a=0,
     terms {2^n,-3^{a_j}} in U_{2,3}, rank 2, is non-degenerate for every
     digit-free power incl. n=0,2,8. A proper sub-sum vanishes iff a subcollection
     of negative terms sums to 0 (impossible) or 2^n - sum_B 3^a =0 for B proper
     nonempty, forcing complement sum = 0 (impossible, all positive)."
  - "Evertse-Schlickewei-Schmidt 2002, 'Linear equations in variables which lie
     in a multiplicative group', Ann. of Math. 155: the number of non-degenerate
     solutions of a_1 x_1 + ... + a_n x_n = 1, x_i in a finitely generated
     subgroup Gamma of finite rank r, is < exp((6n)^{3n}(3(r+1))) --
     finiteness for each FIXED n, effective, triply-exponential in n."
     https://doi.org/10.48550/arxiv.0203010 (ESS), https://www.semanticscholar.org/paper/a7fac29d05b89df9eb74d82edd152154291418e7
  - "Schlickewei 1998 survey 'The subspace theorem and applications'
     (https://doi.org/10.4171/dms/1-2/19): S-unit-equation finiteness for fixed
     number of variables, number of solutions bounded by exp(n c_n(r+1))."
```

## Verdict

**Refuted as a route to the conjecture; its framing survives inside the adopted
approach.** The non-degeneracy claim is PROVED here (re-verified by hand; see
`research/candidate-precedent-handcheck.md`), and the per-level finite bound is a
real theorem (Evertse–Schlickewei–Schmidt 2002) with bounds triply-exponential in
`k`. But the bound gives an `n`-bound that grows with `k` and **no uniformity in
`k`** — and that uniformity is precisely the conjecture. The dual problem supplies
the decisive precedent: `s_2(3^n)` unbounded (the parallel "sum of distinct powers
of 2 equals a power of 3") was settled by Baker-type linear-forms-in-log (Stewart
1980), *not* by a uniform S-unit/Subspace bound. The per-variable-count S-unit
finiteness is a counting hammer that does not transfer to growing support. The
framing (non-degenerate S-unit equation in rank-2 `U_{2,3}`) is adopted as the
backbone of `bertok-hajdu-cross-modulus-ladder`; only the uniformity step is
closed here.
