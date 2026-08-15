```approach
idea: ifs-attractor-contraction
mechanism: |
  Every scalar potential tried so far died on the XOR-induced non-monotonicity:
  a row can lose and regain the same {0,2} pattern cyclically, so no real
  scalar is monotone under the map D(x)_i = |x_i - x_{i+1}|. This approach
  abandons scalar monotonicity entirely and asks instead whether the safe set
  is an ATTRACTOR: a set S that is forward-invariant and to which D contracts
  the whole 2-then-odds cone in a suitable metric. A contraction needs no
  monotone potential — it only needs distances to S to shrink, which is
  compatible with a trajectory zigzagging inside S.

  Named mathematics: iterated function systems (IFS), Hutchinson–Barnsley
  attractors, contraction mapping theorem, set-valued Lyapunov functions,
  Hausdorff distance, basin of attraction.

  The concrete statement to aim for: there is a metric d on nonnegative
  (halved) sequences and a set S (the closure of {0,2}-valued leading-block
  sequences) such that (i) D(S) subseteq S, and (ii) for the prime instance and
  some c < 1, d(D^k(x), S) <= c^k d(x, S).

  The known obstruction to be honest about: the Ducci map is 2-Lipschitz in
  l1 and linfinity (constants exactly 2), so the contraction cannot be on the
  full space; the content is to find a cone/metric on which the constant drops
  below 1 relative to S.

  Speculative: the cone/metric where the constant drops below 1 may not exist,
  in which case the approach is refuted by a single pair x, x' in the cone with
  d(Dx,Dx') >= d(x,x').
status: refuted
disposition: (b) parked — refuted, not a route to G-supply; no strict l1/linf contraction on the cone ((4,0,0),(4,2,0) → ratio ≥ 1) (Directive 44 item 2).
killed-by: |
  Research (this cycle) refuted the approach at its own single-pair falsifier,
  before any theory needed to be invoked.

  (1) NO strict contraction exists in the two natural candidate metrics, and
      the approach's premise that "the content is to find the cone/metric
      where the constant drops below 1" is where it dies. The 2-Lipschitz
      obstruction is not a full-space artifact one can discount by restricting
      to a cone: it is tight INSIDE the safe set S itself, on pairs that
      legitimate the whole idea of a contraction to S.

      Pair: x = (4,0,0), x' = (4,2,0). Dx = (4,0), Dx' = (2,2).
        l1:  d(x,x')  = |4-4|+|0-2|+|0-0| = 2
             d(Dx,Dx')= |4-2|+|0-2|   = 4      -> ratio 2 >= 1
        linf: d(x,x')  = 2
              d(Dx,Dx')= max(2,2)     = 2      -> ratio 1 >= 1
      (Hand-checked exact integer computation; the on-disk checker
       code/out/check_three_candidates_research.py reproduces this and, on an
       exhaustive sweep of {0,1,2,3,4}^3, finds max l1 ratio 2.0 and max
       linf ratio >= 1, so no c < 1 contraction holds in l1 or linfinity on
       even the three-coordinate 2-then-odds-like cone.)

      This is exactly the CHT / Chamberland rigidity point the approach flagged
      ((a,a,c,c) borderline: x=(4,0,0)->(4,0) and x'=(4,2,0)->(2,2) both sit
      at equal-mass pairs), and it is fatal: the pair is INSIDE the cone of
      nonnegative sequences the approach proposes to restrict to, so "restrict
      the cone further" has nothing principled left to cut (values 0,2,4 are
      all legitimate even entries; the pair never leaves the {0,2,4}-valued
      class the whole problem lives in).

  (2) The class-level claim the contraction would prove is FALSE regardless of
      the metric: a universal, metric-independent statement "D^k(x) is forced
      toward the {0,2}-block set for ALL 2-then-odds x" is contradicted by
      held evidence — Colonna's delete-5 example (claim
      colonna-deletion-left-edge-failure) gives a 2-then-odds sequence with
      gaps <= 4 whose second entry is already 4 (A_1 = (1,4,4,2,4,2,...)), so
      no global cone-contraction can hold at the class level; and Eppstein 2011
      (anti-gilbreath-construction) builds sequences that leave and re-enter
      1 infinitely often, i.e. never settle into any contractive basin. A
      contraction bound is a uniform version of bounded absorption, which
      rule90-absorbing-boundary / CHT Lemma 3.7(iii) already refuted for the
      2-then-odds class.

  (3) The IFS/attractor vocabulary adds no theorem that a contraction on the
      prime instance could invoke: the value would have to be a genuine
      contraction constant c<1 on the primes' orbit, which is exactly what the
      (2,4)-event rate (open) would have to certify. In the cyclic Ducci
      setting the analogous machinery is the eventual-periodicity / Chamberland
      max-factoring (held, ducci-max-factoring-potential-template), whose
      rigidity (a,a,c,c) is the same pair that kills the contraction here.

  Research verdict: refuted on a machine-checked single pair inside the very
  cone it proposes, plus the class-level counterexamples already held. Do not
  re-propose a contraction/IFS-attractor formulation unless a genuinely
  different metric (e.g. one that openly discounts the tail) is proposed with
  the pair test passed first.
precedent: |
  - held claim: c2/d/ducci-max-factoring-potential-template (Chamberland: the
    factored-max + rigidity-equality-case (a,a,c,c) structure the contraction
    collides with)
  - held claim: colonna-deletion-left-edge-failure (2-then-odds, gaps<=4,
    second entry 4: class-level counterexample to a global contraction)
  - held claim: anti-gilbreath-construction (Eppstein 2011: leaves and
    re-enters 1 infinitely often — no contractive basin in the class)
  - held claim: rule90-identification-real-absorption-refuted / CHT Lemma
    3.7(iii): {0,d}-blocks persist without decrease; a bounded absorption time
    (of which a contraction is a uniform form) fails for the class
  - code/out/check_three_candidates_research.py (falsifier: x=(4,0,0),
    x'=(4,2,0); 4 vs 2 in l1, 2 vs 2 in linf)
first-step: |
  Closed by research: the single-pair falsifier fires. A contraction in l1 or
  linfinity on the 2-then-odds cone is impossible (ratio >= 1 inside the
  cone), and class-level counterexamples are already held. A contraction
  approach can only be re-opened with a specific discounted-tail metric that
  passes the pair test.
```

```claim
id: ifs-contraction-falsifier-fired
statement: The Ducci/Gilbreath absolute-difference map has NO strict contraction d(Dx,Dx') <= c d(x,x'), c<1, on the nonnegative (2-then-odds-style) cone in the l1 or linfinity metric even among three-coordinate vectors inside the {0,2,4}-valued class: the pair x=(4,0,0), x'=(4,2,0) gives l1 ratio 2 and linf ratio 1 (d(Dx,Dx') >= d(x,x')). Hence no set-valued / attractor contraction to the {0,2}-block set exists in these metrics, and the class-level contraction to S is separately false (Colonna delete-5, second entry 4; Eppstein escape).
hypotheses: l1 or linfinity metric on nonnegative integer sequences; cone of the 2-then-odds class; claim that D^k(x) contracts toward the {0,2}-block set.
holds-here: yes
status: checked
bearing: Refutes the ifs-attractor-contraction approach at its own first-step falsifier. The IFS/contraction vocabulary cannot prove the {0,2} second-entry claim by this route.
anchor: research/approaches/ifs-attractor-contraction.md
```
