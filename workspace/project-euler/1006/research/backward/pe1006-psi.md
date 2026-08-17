# Proof skeleton: Ψ(10^18) mod 101001001

Decomposition of the goal of PE1006 into four lemmas that compose into the answer.

```skeleton
detail: Skeleton at research/backward/pe1006-psi.md. G1 fixes the index set (k+1 length-k factors of infinite Fibonacci word, Sturmian slope 1/phi^2, count via library, infinite-limit stabilisation open). G2 turns each factor into a mechanical-word decimal value v(x_m) with corrected slope F(n-2)/F(n) (mech_reproduces_factors open). G3 telescopes v into a geometrically weighted floor sum (pure algebra, cheapest, checks Psi(3)=20302 and Psi(10)=10699667). G4 evaluates the second moment in O(log k) via the universal Euclidean monoid (build code/lib/ueuclid.py, acceptance tests 1-5, then k=10^18 with two approximants). Status: sketched. First to close: G3.
goal: compute Ψ(10^18) mod 101001001, where Ψ(k) is the sum of the squares of the k+1 distinct length-k Fibonacci subwords read as decimal numbers
implies: The four lemmas compose left-to-right. G1 fixes the index set: the k+1 distinct length-k Fibonacci subwords are exactly the length-k factors of the infinite Fibonacci word F, and F is Sturmian of slope 1/φ² — so Ψ(k) is a sum over m = 0..k. G2 turns each factor into a value: the m-th factor is a mechanical word of the corrected slope, encoding the digit digit_j(x_m) = floor(x_m+(j+1)a) - floor(x_m+ja), so each factor is a decimal number v(x_m) = Σ_j digit_j(x_m)·10^(k-1-j). G3 telescopes v: substitution of the digit rule turns v(x) into a geometrically weighted floor sum, so Ψ(k) = Σ_{m=0}^k v(x_m)^2 is the second moment of that floor sum over m. G4 evaluates that second moment in O(log k) by the universal Euclidean monoid carrying (count, Σx^j, Σx^j·floor, Σx^j·floor²) mod M — this is the step that reaches k = 10^18. Each lemma supplies the index set / term the next consumes; the chain has no gaps in quantifiers: the m-range is fixed by G1, the term by G2, the telescoped form by G3, and the evaluation by G4.
killed-by: (none — nothing broken)
rests-on: fibonacci-sturmian-complexity, governing-sturmian, governing-factor-complexity, g1-factor-chain-nested, g1-oracle-length3, g2-mech-shell-exact-binary, mechanical-word-digit-rule, universal-euclidean-geometric-floor-sum, req-close-universal-euclidean, governing-universal-euclidean
status: sketched
title: Compute Psi(10^18) mod 101001001 as a chain of four lemmas
```

## Gaps

```gap
id: G1-sturmian-factor-structure
lemma: The k+1 distinct Fibonacci subwords of length k are exactly the length-k
      factors of the infinite Fibonacci word F (limit of S_n), and that count k+1
      holds for every k ≥ 1 (F is Sturmian with complexity k+1). The open part is the
      stabilisation into the infinite limit word: the finite chain FactorSet(S_n,k)
      is nested and stabilises, giving FibSubwords k = the length-k factor set of F.
status: open
discharged-by: (partially) fibonacci-sturmian-complexity, governing-sturmian,
      governing-factor-complexity, g1-factor-chain-nested, g1-oracle-length3 supply
      the count k+1, Sturmian-ness, and the finite nested chain; the Lean
      fib_subword_count is still a sorry, and the infinite-limit stabilisation lemma
      (factor_limit_stabilises) is not yet closed as a verdict.
next: finite oracle check k = 1..60 that the length-k factor set of S_n stabilises
      for n ≥ 3k+1 and equals FibSubwords k; then close factor_limit_stabilises to
      promote the count to a conditional verdict in Lean.
```

```gap
id: G2-mechanical-word-representation
lemma: With the corrected slope a = F(n-2)/F(n) (|S_n| = F(n+2) indexing), the k+1
      factors of F of length k, read as decimal numbers, are exactly the values
      v(x_m) where x_m is the midpoint of the m-th arc of the partition of the unit
      circle by {frac(-m·a) : m = 0..k} and digit_j(x) = floor(x+(j+1)a) - floor(x+ja).
      The literal slope F(n-1)/F(n) is refuted (steer-d2-literal-slope holds no).
status: open
discharged-by: (partially) g2-mech-shell-exact-binary (the construction shell is
      formalised), mechanical-word-digit-rule, governing-sturmian give the mechanical
      digit rule; the deep identity mech_reproduces_factors (that the mechanical
      values v(x_m) equal the decimal values of the k+1 distinct factors) is open.
next: reproduce directive-2's checks in-container (k = 3,5,8,10,13,17,21,26,34,40,55)
      asserting exact set equality of {v(x_m)} with the factor-set decimal values;
      close mech_reproduces_factors.
```

```gap
id: G3-telescoped-second-moment
lemma: With v(x) = Σ_{j=0}^{k-1} digit_j(x)·10^(k-1-j) and the digit rule
      digit_j(x) = floor(x+(j+1)a) - floor(x+ja), the telescoping identity
      v(x) = floor(x+ka) - 10^(k-1)·floor(x) + 9·Σ_{j=1}^{k-1} 10^(k-1-j)·floor(x+ja)
      holds, so Ψ(k) = Σ_{m=0}^k v(x_m)^2 is the second moment of this geometrically
      weighted floor sum over m.
status: open
discharged-by: (none)
next: pure algebra — in Python, check Σ_m v(x_m)^2 with the telescoped v reproduces
      Ψ(3) = 20302 and Ψ(10) ≡ 10699667 mod 101001001 exactly, against the direct
      digit sum. This is the cheapest gap and the first that touches the goal's own
      oracle; the telescoped form is exactly what G4 must evaluate at full size.
```

```gap
id: G4-universal-euclidean-floor-sum
lemma: The second-moment floor sum Σ_{m=0}^k v(x_m)^2 mod M is evaluable in O(log k)
      by the universal Euclidean algorithm: the monoid of operations carrying the
      tuple (count, Σx^j, Σx^j·floor, Σx^j·floor²) mod M with x = 10^(-1) mod M,
      split by the Euclidean recursion (AtCoder floor_sum / Chtholly's algorithm).
      The dU shifts carry floor values across segment boundaries — the one place the
      primitive goes wrong.
status: open
discharged-by: (partially) universal-euclidean-geometric-floor-sum,
      req-close-universal-euclidean, governing-universal-euclidean are the library's
      word for the primitive's correctness; the build-and-run (code/lib/ueuclid.py
      does not exist) is what is open.
next: build code/lib/ueuclid.py and run directive-4 acceptance tests 1–5: (1) S0 vs
      direct loop on random (p,q,r,n,z); (2) S1 vs plain floor_sum at z=1 and vs
      direct loop at z≠1; (3) S2 vs direct loop; (4) the telescoped v through the
      primitive vs code/mech/mech_psi.py at k=1..150 and vs Ψ(10) ≡ 10699667; (5)
      match valid general-k values at k=1000, 10000 exactly; only then run k=10^18
      with a Fibonacci approximant F(n) > 10^18, confirmed stable across two
      approximants.
```
