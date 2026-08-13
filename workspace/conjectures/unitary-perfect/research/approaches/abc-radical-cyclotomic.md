# Approach: ABC radical bound on Φ_{4p}(2)

```approach
idea: Apply the ABC conjecture (or the unconditional Stewart–Tijdeman bound) to the
  equation 2^{2p} + 1 = 2^{2p}+1 — i.e., A + B = C with A = 2^{2p}, B = 1,
  C = 2^{2p}+1. The radical rad(ABC) = 2·rad(2^{2p}+1). The ABC inequality
  (either the conditional conjecture or Stewart–Tijdeman's unconditional
  exp(C·rad^{1/3}) bound) forces rad(2^{2p}+1) ≥ 2^{2p·(1−ε)}. But every prime
  divisor r of 2^{2p}+1 = Φ_{4p}(2)·5 is either 5 or a primitive divisor with
  r ≡ 1 (mod 4p). For 2p ∈ H_even, every such r is 3-Higgs, so the radical of
  2^{2p}+1 is a product of 3-Higgs primes. The thinness of P_3 (Ford,
  Π_3(x) ∼ x^{1−η}) gives a quantitative upper bound on the product of the
  first k 3-Higgs primes, and comparing this with the ABC-mandated growth of
  the radical forces a contradiction for large p. This is a divisor-level
  radical bound — it constrains the full prime support of Φ_{4p}(2), not
  just the largest divisor or the ambient density.
mechanism: Let R(p) = rad(2^{2p}+1) = 2·∏_{r|2^{2p}+1} r. By Stewart–Tijdeman
  (or ABC), log R(p) ≥ 2p·(1−ε)·log 2 for any ε > 0 and p > p_0(ε). On the
  other hand, if every r is 3-Higgs with r ≡ 1 (mod 4p), then r = 4p·k + 1
  with k ∈ S_3^{(≤3)}. Each such r ≤ something determined by the counting
  function of P_3. Summing log r over the divisor set and comparing with the
  ABC lower bound yields a contradiction for large p because the sum of logs
  over the sparse set of available 3-Higgs primes cannot keep pace with 2p log
  2. This is NOT a density argument (closed: sieve-structured-progression) — it
  bounds the actual divisor set of one integer, not the ambient primes ≡ 1 mod
  4p. And it is NOT the Stewart-size approach (closed: stewart-size-elimination)
  — it uses the radical (product of ALL distinct primes), not the largest one.
status: proposed
first-step: (1) Retrieve the exact Stewart–Tijdeman unconditional bound for
  a^n − b^n (Acta Math 211, 2013) applied to 2^{4p} − 1 =
  (2^{2p}−1)(2^{2p}+1) to separate the primitive radicals; (2) compute the
  product of the first k 3-Higgs primes for small k from OEIS A057447 and
  fit the growth function; (3) state the inequality that would close H_even
  and test whether the constants cross for the open candidates near the
  50000 frontier, where the empirical ω(Φ) data from the paper's §5.3 (82
  distinct primes, v2 distribution) provide a concrete check.
```