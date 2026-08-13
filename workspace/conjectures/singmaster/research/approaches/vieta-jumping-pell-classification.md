```approach
idea: Vieta jumping / infinite descent on the Markov-type surface defined by
  C(x,k1) = C(y,k2) in the three integer variables (x, y, a). For the specific
  infinite family C(n+1,k+1) = C(n,k+2) (the Pell/Singmaster/Lind family),
  rewrite as a quadratic Diophantine equation in n and k after fixing the
  relation between the column indices. Generalize: for arbitrary (n,k) pairs
  with C(n,k) = a, the ratios between different representations satisfy
  recursive relations that can be studied via Vieta jumping — the technique
  that solved Markov's equation x²+y²+z²=3xyz and was used in IMO problems.
  The idea: if a has "too many" representations, Vieta jumping constructs an
  infinite descending chain, contradicting well-ordering unless the
  representations satisfy a specific recursion — which then forces them to
  be part of the known infinite family. This would prove that any a with
  N(a) ≥ 7 must belong to the known Pell family, reducing the problem to
  proving that the Pell family has bounded multiplicity.

mechanism: [PARTIALLY GROUNDED as a classification, REFUTED as a mechanism.]
  What the idea correctly points at is the REAL classification result, which
  the library already holds:
  (i) The infinite family C(n+1,k+1)=C(n,k+2) is COMPLETELY classified and
      is a Pell phenomenon: Lind 1968 (FQ 6, 86-93, PRIMARY, claim
      lind-1968-fibonacci-family-primary) solved it entirely via the units of
      Q(sqrt 5) / Pell u^2 - 5v^2 = -4, giving exactly
      n = F_{2i+2}F_{2i+3}-1, k = F_{2i}F_{2i+3}-1 (i>=1), with C(x,2)=C(y,2)
      the only fixed-pair diagonal case; Singmaster 1975 rediscovered it.
      The complete list of all known nontrivial solutions of C(n,k)=C(m,l)
      (GRKTU 2020, claim grktu-known-solutions-list) is: the Fibonacci family
      plus twelve sporadic values (3003, 120, 1540, 7140, 210, 11628, 24310,
      ...), each on a FIXED pair of small columns.
  (ii) Jenkins (arXiv:1411.4111, claim jenkins-ab-finite): the shifted family
      C(x,y) = C(x-a,y+b) has finitely many natural solutions for EVERY shift
      (a,b) except a=b=1 — the golden-ratio quadratic giving the Pell family.
      So "the only genus-0 diagonal of the shift family is (1,1)" is exactly
      Jenkins' theorem; for a != b the curves have genus >= 2 (limiting ratio
      c, root of c^{a+b}-(c+1)^a=0, is non-quadratic — Jenkins' Lemma).
      The run's genus grid and BST 1999 Thm 2.2 (claim
      bst-genus-classification-matches-grid) corroborate: for FIXED distinct
      pairs the genus-0 and genus-1 loci are exhausted by (2,2) diagonal,
      (2,3) and (2,4); everything else is genus >= 2.
  What is NOT supported:
  (i) "N(a) large forces membership in a genus-0 curve" is FALSE on the
      witnesses: every known high-multiplicity value sits on FIXED curves of
      genus >= 1, not on a genus-0 diagonal. 3003 = C(15,5)=C(14,6) is the
      (1,1)-shift pair (genus-0 quadratic), but its third representation
      C(78,2) lives on the fixed curve C(x,2)=C(y,78)?? no — on the fixed-a
      fiber C(x,2)=3003 — and the six N=6 values (120, 210, 1540, 7140,
      11628, 24310) each come from ONE nontrivial pair on a FIXED curve of
      genus 1 ((2,3): 120,1540,7140; (2,4): 210; (2,5): 11628; ...). So the
      mechanism's engine (an a with >= 7 reps must be Pell-family) would have
      to show 3003 is the LAST non-Pell collision — exactly the content of
      de Weger's Conjecture A (claim deweger-genus3-curve), which is OPEN, not
      a consequence of Vieta jumping.
  (ii) Vieta jumping is a descent on a QUADRATIC equation (one variable is
      the root of a degree-2 polynomial in the others: Markov x^2+y^2+z^2=3xyz,
      IMO 1988 Problem 6, Pell x^2 - Dy^2 = m). The binomial equations
      C(x,k1)=C(y,k2) are degree-k1/k2 >= 3 algebraic curves; the "conjugate
      solution" phenomenon that makes Vieta jumping work (sum of the two roots
      is an integer polynomial in the other variables) has NO analogue at
      degree >= 3. The literature on Vieta jumping (Lemmermeyer arXiv:2601.15229
      survey "Vieta jumping and small norms"; the Markov/cluster-algebra work
      Lampe J. Algebra 2016, Banaian-Sen Ramanujan J 2023, Gyoda-Maruyama
      arXiv:2312.07329) is uniformly about quadratic equations / Pell-type
      conics and Markov-type cubics. No source applies Vieta jumping to
      binomial equalities, and none could: the method is quadratic by
      construction.
  (iii) The reformulation "bound the column indices rather than the value"
      (classify all solutions of C(x,k)=C(y,l) with k,l not fixed) is the
      Jenkins/C(x,y)=C(x-1,y+1) frame, which is settled as far as infinite
      families go (Lind-Singmaster complete classification + Jenkins a!=b
      finiteness). It does not bound N(a): a value can be hit by many
      FIXED small pairs before any shift-family structure appears (3003 is
      hit by the (1,1)-shift pair AND the fixed (2,·)-column; the six N=6
      values are single-pair).

status: refuted
killed-by: (i) the completed Pell classification of the infinite family
  (lind-1968-fibonacci-family-primary, singmaster-1975-pell-family,
  grktu-known-solutions-list) and Jenkins' a!=b finiteness
  (jenkins-ab-finite) already exhaust the genus-0 diagonal content — the
  only infinite family is the (1,1)/Pell one; (ii) the claim that large N(a)
  forces genus-0 membership is contradicted by the witnesses (3003 has a
  genus-1/g2 fixed-curve component via C(78,2); the six N=6 values are each
  a single nontrivial pair on a fixed genus>=1 curve) and is exactly de
  Weger's OPEN Conjecture A, not a consequence of descent; (iii) Vieta
  jumping is a quadratic-recurrence technique with no degree>=3 analogue;
  the search found no application of it to binomial equalities.
precedent:
  https://arxiv.org/abs/1411.4111 (Jenkins, repeated binomial coefficients —
    the shift-family finiteness, held: jenkins-ab-finite)
  https://www.fq.math.ca/6-3.html (Lind 1968, Fibonacci Quart. 6(3), 86-93 —
    the Pell/unit-of-Q(sqrt5) complete solution, held primary:
    lind-1968-fibonacci-family-primary)
  https://www.fq.math.ca/13-4.html (Singmaster 1975, Fibonacci Quart. 13(4),
    295-298 — rediscovery, Pell u^2-5v^2=-4:
    singmaster-1975-pell-family)
  https://doi.org/10.1016/j.jnt.2019.07.002 (GRKTU 2020, JNT 208 — complete
    known-solutions list: grktu-known-solutions-list)
  https://doi.org/10.48550/arxiv.2601.15229 (Lemmermeyer 2026 — Vieta jumping
    survey; scope: conics/quadratic number fields, Pell-type)
  https://doi.org/10.1016/j.jalgebra.2016.04.033 (Lampe 2016 — Markov
    equation via cluster mutations; quadratic)
  claims: jenkins-ab-finite, lind-1968-fibonacci-family-primary,
    singmaster-1975-pell-family, grktu-known-solutions-list,
    deweger-genus3-curve, bst-genus-classification-matches-grid,
    infinite-family-6
first-step: none — the working kernel (Pell-family classification, shift-family
  genus-0 locus = {(1,1)}) is already grounded library content; the Vieta-
  jumping mechanism has no degree>=3 analogue and the genus-0-forcing claim is
  contradicted by known N=6/N=8 witnesses. Do not re-propose Vieta jumping for
  this problem; the honest reformulation is de Weger's Conjecture A (no
  nontrivial collisions beyond the known list + infinite family), which is
  open and is attacked by the effective-methods wall, not by descent.
```

```claim
id: vieta-jumping-quadratic-only
statement: Vieta jumping cannot classify binomial equalities: the descent
  mechanism requires the equation to be quadratic in at least one variable (the
  conjugate root is an integral polynomial in the others — Markov x^2+y^2+z^2=
  3xyz, IMO 1988 P6, Pell x^2-Dy^2=m), and C(x,k1)=C(y,k2) is a curve of degree
  k1/k2 >= 3 (genus >= 2 for all fixed distinct pairs except (2,3),(2,4), per
  BST 1999 Thm 2.2 and the run's genus formula), so no Vieta-type conjugate
  exists. The claim that large N(a) forces membership in a genus-0/Pell family
  is contradicted by the witnesses: 3003=C(15,5)=C(14,6) sits on the (1,1)-
  shift quadratic, but its representation C(78,2) and the six N=6 values (each
  one nontrivial pair on a fixed genus>=1 curve: (2,3)->120,1540,7140;
  (2,4)->210; (2,5)->11628) show high multiplicity is NOT confined to genus-0
  diagonals; the honest statement is de Weger's open Conjecture A. The complete
  infinite-family classification (Lind 1968 via units of Q(sqrt5)/Pell u^2-5v^2=
  -4, exactly n=F_{2i+2}F_{2i+3}-1, k=F_{2i}F_{2i+3}-1; Jenkins a!=b finiteness)
  is already library content (lind-1968-fibonacci-family-primary,
  jenkins-ab-finite).
hypotheses: N(a) counting both mirrors and the trivial pair; k<=log2(a).
holds-here: yes
status: grounded (deduction from held primaries — Lind 1968, Jenkins 2015,
  GRKTU 2020, BST 1999 boundary result — plus the computed witness set)
bearing: permanently retires the Vieta-jumping candidate; its surviving kernel
  (Pell classification, shift-family genus-0 locus) is already established
  library content, and the open part is Conjecture A / effective per-pair walls.
anchor: research/approaches/vieta-jumping-pell-classification.md
```