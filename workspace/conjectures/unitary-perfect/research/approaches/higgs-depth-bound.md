# Pratt-tree depth bound for the 3-Higgs poset

```approach
idea: Attack H_even from within the 3-Higgs definition rather than from the
  divisor side. The 3-Higgs condition is a recursively-defined well-founded
  tree: p is 3-Higgs iff every q | p−1 is 3-Higgs AND v_q(p−1) ≤ 3. For
  m = 2p ∈ H_even, every primitive divisor r of 2^{2p}+1 has r ≡ 1 (mod 4p)
  so r−1 = 4p·k with k Higgs-cubefree. Prove — using only the structural
  combinatorics of the Pratt tree under the cubefree constraint — that the
  3-Higgs tree has bounded depth (an absolute constant D), making the
  3-Higgs semigroup finite, or at minimum prove that r cannot be 3-Higgs
  for large p because the depth required to reach r's size contradicts the
  exponent cap v_q ≤ 3.

mechanism: The Pratt tree of a prime p is the rooted tree whose nodes are
  primes, with q a child of p if q | p−1, terminating at 2. For the 3-Higgs
  set P_3, every edge q → p has the "cubefree" label: v_q(p−1) ≤ 3. This
  means that for a node p at depth d, p is at most the cube of the product
  of its children, each of which is itself a 3-Higgs prime bounded by the
  same rule. This gives a recursive size bound:

      p ≤ (Π_{q child of p} q)^3 · (other cubefree factors)

  Since the 3-Higgs primes omit 17 (the smallest non-Higgs prime), the tree
  is constrained at the base. Ford (2014) proved that downward-closed prime
  sets omitting an odd prime are power-saving thin — but that does not bound
  depth. The new ingredient is the exponent cap v_q ≤ 3, which means each
  edge transmits at most a cubic factor. For p to be very large, the tree
  must either be deep (many edges) or wide (many children per node). The
  FKL (2010) bound says that for almost all primes the chain length
  H(p) ≤ (log p)^{0.9503}, but the cubefree cap may force H(p) ≪ log log p
  or even H(p) ≤ D absolutely for 3-Higgs primes.

  The argument: Start from the bottom (p=2, the unique even Higgs prime).
  At depth 1, the children of 2 are primes p with p−1 = 2^e, v_2(p−1) ≤ 3
  ⇒ p ∈ {3, 5}. (p = 2^1+1 = 3, 2^2+1 = 5, 2^3+1 = 9 not prime).
  At depth 2, primes whose p−1 factors are from {2,3,5} with each exponent
  ≤ 3, giving a finite set. The crucial question is whether this process
  terminates finitely (all 3-Higgs primes have bounded depth) or whether
  there exist arbitrarily deep 3-Higgs chains.

  If bounded depth D can be proved, then the set P_3 is finite (each level
  has finitely many elements determined by the finite set of possible
  factorizations of p−1 from the level above), so H_even is finite.
  If not, one may still prove that for sufficiently large p, the depth
  required for a primitive divisor r | Φ_{4p}(2) exceeds what the
  3-Higgs condition allows given the growth rate of r ~ 2^p.

status: refuted
killed-by: The 3-Higgs primes form an infinite set (OEIS A057447, b-file to
  n≥1000; Ford's power-saving thinness is consistent with infinitude and
  the set demonstrably continues). The paper's own m=2426 example features
  the fully 3-Higgs divisor P=25893760589 with nontrivial Pratt descent
  depth, directly refuting bounded depth ≤ D for any small D. Since depth
  is unbounded, the "depth growth rate" fallback is just a re-derivation of
  thinness constraints the paper already makes via Ford's theorem — thinness
  does not close the gap (the paper's §5.3 says "density arguments by
  themselves cannot close Conjecture 6").
```