# Entropy / hard-core gas with a degree ceiling

```approach
idea: View the problem as a degree-constrained hard-core gas on Q_n: the quantity
of interest is the largest induced subgraph of Q_n with maximum degree ≤ d, and
f(n) is the least d for which that equals 2^{n-1}+1. Bound it with Shearer's
entropy lemma and the hard-core (independence) ratio of the cube — probability
and statistical mechanics instead of linear algebra.

mechanism: A set S with D(S) ≤ d is a "d-independent" set. The d = 0 case is the
independence number α(Q_n) = 2^{n-1}, achieved exactly by the two parity classes —
a phase transition at density exactly 1/2, with the single extra vertex a
critical excess. The cube is the n-fold Cartesian power K_2^□n, and Kahn's
entropy method / Shearer's lemma (the standard machine for independence ratios of
products) reproduces α = 2^{n-1} — this covers the d = 0 line of `f-exact-1..5`
and the worked even-weight example, satisfying Scholze's rule.

The new step is to lift the entropy bound from "independent" (d = 0) to
"degree ceiling d": a random S with D(S) ≤ d has an entropy upper bound as a
function of d, obtained by summing the per-vertex local constraints, and
inverting it gives a lower bound on D(S) for |S| = 2^{n-1}+1. The growth of f(n)
becomes the question of how the entropy profile of the hard-core model on Q_n
behaves at the critical excess — a phase-transition question, not a max-min
obstruction. Caveat stated honestly: entropy is a total/average-type quantity,
so this may be subject to the same averaging obstruction as influence arguments;
the point of the proposal is to test whether the *degree ceiling* (a max-type
constraint) escapes it.

covers: reproduces α(Q_n) = 2^{n-1} (parity classes) and the worked example;
a genuinely different world (probability/entropy) from the closed spectral route.

status: refuted (as a route to sqrt(n)); grounded (as the d=0/independence-number line only)
killed-by: The entropy/hard-core method is a real and deep technique for the
  NUMBER of independent sets and independence-number-type quantities, but it
  is a total/average-type method: Shearer's lemma and Kahn's entropy argument
  (the standard machines) bound averages/counts, and by the problem.md/
  probabilistic obstruction any method that bounds an average cannot reach
  sqrt(n) for the MAX internal degree D(S). The proposed lift from "independent
  (d=0)" to "degree ceiling d" as a large-deviation bound whose inversion at
  |S|=2^{n-1}+1 reaches sqrt(n) has no published support found, and there is an
  independent numerical red-flag: at n=5 the extremal set has 12 of 17 vertices
  at the max degree 3 (flat), so the average internal degree (3*12+2*3+1*2)/17
  = 44/17 = 2.59 is far below the max 3 — an entropy/average upper bound on |S|
  as a function of ceiling d would be dominated by this spread and caps at
  logarithmic growth, never forcing the flat max to sqrt(n). What the method
  DOES cover, and grounds: the d=0 line (independence number alpha(Q_n)=2^{n-1}
  via the two parity classes) and the independent-set counting of the cube
  (Kahn's entropy bound and Galvin's threshold), satisfying Scholze's rule for
  that sub-claim only.
precedent:
  - Jeff Kahn, "An entropy approach to the hard-core model on bipartite
    graphs" 2001 (CPC 10:219-237); and Proc AMS "Entropy, independent sets and
    antichains" (DOI 10.1090/s0002-9939-01-06058-0): n-regular bipartite
    i(G) <= (2^n+1)^{N/(2n)} via Shearer's lemma/entropy. Real technique.
  - Sah et al., "The number of independent sets in an irregular graph":
    https://www.sciencedirect.com/science/article/pii/S0095895619300085 —
    Kahn's conjecture (2019), entropy/combinatorial, general graphs.
  - Galvin, "A threshold phenomenon for random independent sets in the
    discrete hypercube": https://doi.org/10.1017/s0963548310000155 — sharp
    threshold at lambda=1 in the hard-core model on Q_n, with occupation minim
    (min |I∩E|,|I∩O|) transitions; the hypercube hard-core phase structure is
    exactly the parity/excess theme of this problem. Supports the d=0 frame.
  - Jenssen, Perkins, Potukuchi, "Independent sets of a given size and
    structure in the hypercube": https://doi.org/10.1017/s0963548321000559 —
    asymptotics of i_{floor(beta N)}(Q_d) via polymer/cluster/local CLT;
    the +1-excess / beta≈1/2 regime in the cube.
  - MDPI Entropy 23:270 (2021), generalized Kahn method for irregular bipartite
    graphs.
  No source applies entropy/large-deviation degree-ceiling to force a MAX
  internal degree at |S|=2^{n-1}+1; the entire published hard-core-on-cube
  literature bounds counts and typical (average) structure, not D(S).
refuted-at: n=5 exact witness (flat degree profile 12/17 at max 3 vs average
  2.59) is the concrete manifestation of the averaging obstruction.

first-step: Derive Shearer's/Kahn's entropy bound for K_2^□n and confirm it gives
α = 2^{n-1} exactly (d = 0). Then define the degree-ceiling partition function and
compute, for small n, the entropy upper bound on |S| as a function of the ceiling
d, comparing the inversion point (least d with bound ≥ 2^{n-1}+1) to
f(1..5) = (1,2,2,2,3).
```
