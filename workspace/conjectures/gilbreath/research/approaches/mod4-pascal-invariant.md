```approach
idea: The mod-4 Pascal linearization as an invariant machine — reframe the conjecture as a statement about the Sierpinski-gasket dot product of the prime gap sequence
mechanism: >
  Odlyzko's mod-4 linearization (d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4) wherever
  d_k(n) is even) is already established (sourced, Odlyzko 1993 §2 eq.201, CHT
  Lemma 3.10). This is an exact algebraic fact, not a heuristic: after dividing
  even entries by 2, the absolute-difference operator reduces to addition mod 2.
  Iterating, d_k(1)/2 (mod 2) = Σ_{j=0}^{k-1} binom(k-1, j) · (d_1(2+j)/2)
  (mod 2). That is: the parity of the halved second entry at row k is exactly
  the dot product of the (k-1)-st row of Pascal's triangle mod 2 (the Sierpinski
  gasket) with the halved initial gap sequence d_1(2), d_1(3), ... 

  The conjecture A_k(1) ∈ {0,2} is equivalent to: for every k ≥ 1, this dot
  product is 0 or 1 (not 2, 3, ...), with the halved value being 0 or 1 mod 2
  giving 0 or 2 after doubling. But the mod-2 reduction only captures parity of
  the halved value — the actual value needs tracking mod higher powers of 2
  to distinguish e.g. 0 from 4/2=2 (both 0 mod 2).

  The full invariant: work mod 2^t for t ≥ 1. The Pascal iteration lifts to
  mod 2^t via Kummer/Lucas for higher powers, giving d_k(1) = Σ binom(k-1, j)
  · d_1(2+j) with the sum understood as an alternating sum (with signs from the
  absolute-value operator's branch choice). The sign pattern is determined by
  the ordering of d_{k-1}(j) and d_{k-1}(j+1) — which is itself a function of
  the Pascal structure.

  This approach bypasses the consumption/regeneration framework entirely: it
  does not track blocks at all. It asks whether a specific linear combination
  (with Sierpinski-pattern coefficients) of the prime gaps is always 0 or 2.
  The question becomes number-theoretic: what property of the prime gaps makes
  their Sierpinski dot products bounded by 2?

status: proposed
first-step: >
  Write a program that computes d_k(1)/2 for k=1..1000 using both the iterative
  row method (gold standard) and the Sierpinski-dot-product formula mod 2^t for
  increasing t. Verify they agree. Then study the sequence a_k = d_k(1)/2: it is
  known to be 0 or 1, but what is its Sierpinski autocorrelation? Plot
  a_{2^m + r} for fixed r as m varies — the self-similarity of the Sierpinski
  coefficients should induce structure in the a_k sequence that can be
  characterised as an additive cellular automaton, potentially yielding a
  closed-form invariant.
```