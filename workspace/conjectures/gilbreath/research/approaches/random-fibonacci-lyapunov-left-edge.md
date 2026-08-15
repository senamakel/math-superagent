```approach
idea: random-fibonacci-lyapunov-left-edge
mechanism: |
  The local two-input map of the Gilbreath operator, (a,b) ↦ |a−b|, is exactly
  the "random Fibonacci" map: each step replaces a pair by the absolute
  difference, so a magnitude evolves as x_{n+1} = |x_n ± x_{n−1}| with the sign
  decided by which neighbour is larger. Viswanath (Math. Comp. 69 (2000))
  showed that the *random* ± version has a well-defined Lyapunov exponent
  ≈ 1.132…, and the whole theory of Furstenberg–Kesten, Oseledets and Kesten
  governs growth of products of random matrices.

  Along the left staircase the conjecture is a growth statement about exactly
  such a product. Each halved cell h_{k}(i) is the leftmost output of a chain
  of |a−b| operations coupling neighbours, so the pair (h_k(i), h_k(i+1))
  evolves by a 2×2 matrix chosen from {[1 −1; 0 1], [1 1; 0 −1], …} according
  to the sign of h_k(i) − h_k(i+1). The second entry A_k(1) = 2·h_k(1) is the
  first coordinate of this product; the conjecture A_k(1) ∈ {0,2} says it never
  exceeds 1 (halved), i.e. the leftmost Lyapunov exponent of the deterministic
  prime-driven product is ≤ 0 in the strong sense that the first coordinate
  stays bounded, not merely sub-exponential.

  The class-level content: Eppstein's anti-Gilbreath escape is built from a
  *degenerate* sign process (one fixed order → repeated subtraction grows the
  entry), which is exactly the regime where the random-Fibonacci product has
  positive Lyapunov exponent. A general-class theorem of the form "if the sign
  process of the gap stream is non-degenerate / has a uniform alternation
  bound, then the leftmost Lyapunov exponent is < 0, hence A_k(1) ∈ {0,2}"
  would settle the prime case as a corollary *provided* the prime gap sign
  process can be shown to meet the condition — and it is precisely the
  2-separated / non-concentration hypothesis (CHT condition (ii), Ross 2026)
  that this condition restates in dynamical language. This gives a genuinely
  new route to a named theorem: Kesten's criterion (growth of random matrix
  products) with the randomness replaced by a deterministic non-degeneracy
  hypothesis on the driving signs.
status: proposed
side: general-class / dynamical (Lyapunov-exponent route to regeneration; the prime case enters only through the sign-sequence hypothesis)
named-mathematics: random Fibonacci sequences (Viswanath 2000), Lyapunov exponents of random matrix products (Furstenberg–Kesten, Oseledets, Kesten's criterion), deterministic non-degeneracy / 2-separation
speculative: the driving process is the *deterministic* prime gap sign stream, not i.i.d.; and the map is not a single 2×2 product but an infinite coupled system (each cell is shared by two differences). The honest claim is that the leftmost coordinate of the coupled product carries a Lyapunov-type description, and a deterministic Kesten-style criterion may transfer. Whether the sign process is itself what CHT call "2-separated" is the open part.
falsifier: if the exact matrix-product model of the left staircase has positive empirical Lyapunov exponent on the prime instance while the conjecture still holds, then "exponent ≤ 0" is too crude and the reduction is not the right object; or if the sign process of the primes is provably as concentrated as Eppstein's escape, the general-class theorem's hypothesis fails for primes. First step measures the finite-n exponent for both regimes.
first-step: |
  (a) Derive the exact 2×2 matrices: from |h_i − h_{i+1}| write the update of
  (h_{k+1}(i), h_{k+1}(i+1)) in terms of (h_k(i), h_k(i+1), h_k(i+2)) and
  express it as a product of two 2×2 matrices selected by the sign of
  h_k(i) − h_k(i+1) (plus the shared-coordinate coupling). Verify by exact
  integer comparison on the oracle rows.
  (b) Compute the finite-n empirical Lyapunov exponent of the first coordinate
  for (i) the prime instance (witnesses/blocks depth 1000) and (ii) an
  Eppstein-type escape instance and a Colonna delete-5 instance; confirm the
  exponent is ≤ 0 (≈ log 1 = 0 in halved units, i.e. bounded) for primes and
  > 0 for the escape. Cost O(depth × width), one row live.
  This decides in one run whether the Lyapunov object separates the two
  regimes before any Kesten-style theorem is attempted.
```

## Why this is not already on disk

- **Not `renewal-process` / `subadditive-growth` (proposed) / `ruin-theory` (proposed):** those treat the *scalar* block length or surplus and ask for a one-parameter drift/rate. This attacks the *vector* local dynamics and the exact Lyapunov spectrum of the `|a−b|` map — a different object with a different named theorem (Kesten).
- **Not `ifs-attractor-contraction` (refuted):** that needed a pointwise metric contraction, shown impossible on (4,0,0)/(4,2,0). A Lyapunov-exponent statement is an *asymptotic* growth bound, strictly weaker than pointwise contraction, and is not refuted by that pair (a single step can grow while the product still has exponent ≤ 0).
- **Not `walsh-hadamard` / max-plus (refuted):** no finite-spectral or tropical-max claim; it is a matrix-product growth statement.

## What it would take for this to be wrong

The prime sign stream must be non-degenerate in the Kesten sense. If the primes' gap-order pattern is (contrary to belief) eventually monotone or concentrated, the hypothesis fails for primes and the route yields only a conditional theorem about a class the primes may not lie in. That is exactly what the first-step measurement and a check of CHT's 2-separation condition settle.
