```approach
idea: D-finite (holonomic) closure of the unsigned-difference "fold" operator on ordinary generating functions — ask whether the row map h ↦ |∂h| preserves a manageable function class, and derive the functional equation that determines the left column.
mechanism: |
  A row a_0, a_1, a_2, ... has ordinary generating function F(x) = Σ a_n x^n.
  The SIGNED forward difference is linear and classical: it is multiplication
  of the generating function by (1−x)/x with a shift — the Riordan-array fact
  the run already holds. The Gilbreath operator replaces the signed difference
  by its ABSOLUTE VALUE, i.e.

        |a−b| = max(a,b) − min(a,b),

  which is the "tropical fold" of the two parent values. In generating
  function terms this is NOT a coefficientwise linear map; it is a
  piecewise-linear (max-plus/min-plus) fold F ↦ G where each coefficient of G
  is a max/min of neighbouring coefficients of F.

  The proposal is the standard generating-function program, aimed at the
  UNKNOWN direction the run has not tried: determine whether the fold operator
  is CLOSED on a class rich enough to make the left column computable, and
  whether the resulting functional equation is exact.

  Two nested targets, in order of ambition:

    (T1) D-FINITE / HOLONOMIC CLOSURE. A sequence is D-finite if its
         generating function satisfies a linear differential (equivalently
         linear recurrence with polynomial coefficients). Question: is the
         class of D-finite power series closed under the tropical fold
         F ↦ (coefficientwise max/min fold)? If YES, then the left column
         A_k(1), as a function of k, is D-finite — it satisfies a linear
         recurrence with polynomial coefficients, and the {0,2} property is
         DECIDABLE by checking finitely many initial terms. If NO, the
         negative answer is a theorem: no finite-recurrence route to the
         conjecture exists, which explains the run's stall and is a genuine
         partial result. The earlier automaticity attempt (refuted) asked
         whether the INPUT (primes) is automatic; this is different — it asks
         whether the OPERATOR preserves a class, with the input class being
         "gaps in a finite set" or the prime instance read as an ordinary
         series.

    (T2) EXACT FUNCTIONAL EQUATION. |a−b| = a+b−2·min(a,b), and min(a,b) is
         the coefficientwise "Hadamard product with a threshold" — in the
         halved {0,1} regime min = AND (product) and |a−b| = XOR = a+b−2ab.
         Inside the block the fold is exactly G(x) = ((1+x)F(x) mod 2 lifted),
         a closed functional equation; outside the block the fold is a
         max-plus convolution. The hope is a single piecewise functional
         equation for the bivariate generating function of the whole triangle,
         whose boundary (the left column) is then read off by a
         kernel/residue-type extraction (Banderier–Flajolet style, but for
         the piecewise fold rather than a finite step set).

  The load-bearing bet is (T1): either the fold is D-finite-closed (then the
  conjecture is, in principle, decidable) or it is not (then the failure is a
  structure theorem worth exactly as much).
status: refuted
killed-by: | Load-bearing premise fails on the run's own proved facts: applying the fold to the halved {0,1} interior does NOT yield the claimed closed functional equation "G(x) = (1+x)F(x) mod 2 lifted" — inside the {0,2} block the halved fold is XOR/Rule 90 (rule90-interior-xor, proved), i.e. G(x)=((1+x)F(x)) with coefficientwise XOR, but this is a finite-prefix (block-bounded) relation, and past the block boundary the max/min fold breaks holonomicity. The known literature is uniformly negative on D-finite closure under the relevant operations: (i) D-finite/P-recursive classes are closed under algebraic operations, diagonals, Hadamard products, derivatives — but NOT under arbitrary piecewise-linear (max/min, |·|) coefficientwise operations, which is exactly the load-bearing (T1); (ii) Walks confined in a quadrant are "not always D-finite" (Banderier–Flajolet–Bousquet-Mélou–...), a canonical instance of a combinatorial o.g.f. failing holonomicity from boundary conditions; (iii) there are explicit non-holonomic sequences built from such operations (Flajolet–Gerhold–Salvy 2010 non-holonomicity methods; Garrabrant 2015: P-recursivity is not preserved under natural generating-set operations, dissolves Kontsevich's question). Even granting (T1) hypothetically, the conclusion it buys — "the {0,2} property is DECIDABLE by checking finitely many initial terms" — is a non-result for the conjecture: P-recursive classes are NOT decidable-from-finite-terms in the sense the proposal needs. The Skolem problem (does a term vanish) is unsettled beyond order 4; membership/positivity likewise (Neumann 2021, Kenison–... 2023: decidability only for restricted hypergeometric subclasses). A D-finite certificate for A_k(1)∈{0,2} would require deciding a global membership property of a P-recursive sequence, a problem with no known algorithm even under the (T1) closure. So the approach's "if yes, decidable" hook is not delivered by D-finiteness.
precedent: https://www.sciencedirect.com/science/article/pii/S0304397503002196 (Banderier–Flajolet–Bousquet-Mélou et al., walks in a quadrant not always D-finite); https://doi.org/10.37236/275 (Flajolet–Gerhold–Salvy, methods proving non-holonomicity); https://escholarship.org/uc/item/004616km (Garrabrant 2015, P-recursivity not preserved under natural operations); https://doi.org/10.46298/lmcs-17(3:16)2021 (Neumann 2021, decision problems for linear recurrences, Skolem/positivity hardness); https://dl.acm.org/doi/fullHtml/10.1145/3597066.3597121 (Kenison et al. 2023, restricted hypergeometric membership decidability); claims rule90-interior-xor (proved, the block-internal XOR), block-growth-literature-not-covered (and no source studies the fold/left-column holonomicity either), thue-morse-sublinear-supply-witness (the run measured the fold-parity count ≠ real ν₂, the exact (T2) equation is not the left column).
side: general-class / dynamical (the operator, not the primes)
named-mathematics: D-finite (holonomic) sequences and functions (Stanley,
  Gessel, Zeilberger); closure properties under Hadamard products, diagonals
  and piecewise-linear operations; the algebra of generating functions for
  difference tables; max-plus (tropical) generating functions.
speculative: MEDIUM-HIGH — D-finite classes are notoriously NOT closed under
  arbitrary piecewise-linear operations; the specific claim that the tropical
  fold preserves holonomicity is untested and may well fail. The negative
  result is still a deliverable.
falsifier: (a) a single explicit D-finite series F whose fold is not D-finite
  (proved or detected by differential-equation guessing on a deep truncation)
  refutes (T1); (b) the functional equation derived fails on oracle rows
  (witnesses.json) — every identity must reproduce problem.md's A_1..A_5.
first-step: |
  1. Derive the exact bivariate generating function for the SIGNED triangle
     (known: a(XY/(1+Y))/(1+Y)) and state precisely the fold's deviation
     term from it (the 2·min correction).
  2. Test (T1) numerically: take the halved prime-gap word (finite, from the
     oracle), and separately a family of random/combinatorial D-finite top
     rows; compute several folded rows; run a differential-equation/guess
     (sympy `guess` or linear-recurrence guessing) on the left column to
     detect a polynomial-coefficient recurrence, or its absence up to a
     stated order/depth bound.
  3. On the {0,1} interior (XOR regime), write the exact functional equation
     G(x) = (1+x)F(x) mod 2 and verify it against the oracle block; then
     attempt to extend it past the block boundary with the min-correction.
  4. Report which of (T1)/(T2) survives, with the order and depth bounds the
     negative test was run under.
```
