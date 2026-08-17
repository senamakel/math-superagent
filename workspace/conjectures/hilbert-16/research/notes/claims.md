```claim
id: h16-gasull-lazaro-torregrosa-abelian-zero-bounds-2010
status: sourced
statement: Gasull, Lázaro & Torregrosa (arXiv:1012.5201, 2010), "Upper bounds
  for the number of zeroes for some Abelian integrals": for the planar vector
  field x'=−yG(x,y), y'=xG(x,y) whose critical set {G=0} is K straight lines
  (not through the origin, parallel to one/two orthogonal directions),
  perturbed by a general polynomial of degree n, they give an explicit upper
  bound on the number of limit cycles bifurcating from the period annulus of
  the origin, in terms of K and n. Method: explicit computation of the
  Abelian integral controlling the bifurcation, and a new result bounding the
  zeros of the family of real functions arising. For K ≤ 4 the bounds recover
  or improve earlier results. This is the open-access sibling of the
  Mañosas–Villadelprat JDE 251 (2011) Chebyshev zero-bound criterion, sharing
  the Wronskian/Chebyshev machinery for the run's sharp-Abelian-integral
  instrument route.
hypotheses: unperturbed systems of the form x'=−yG, y'=xG with G polynomial,
  {G=0} = K straight lines in two orthogonal directions; polynomial
  perturbations of degree n; first-order (Abelian/Melnikov) bifurcation.
evidence-class: sourced (arXiv abstract page full text held,
  research/sources/gasull-lazaro-torregrosa-abelian-zero-bounds-2010.full.md;
  PDF at research/summaries/gasull-lazaro-torregrosa-abelian-zero-bounds-2010.md).
falsifier: a specific (K,n) instance where the stated zero bound fails — the
  paper's bounds are explicit, so a counterexample system within the class
  would refute; none is known.
holds-here: yes as a named instrument for GOAL's "sharp zero-count for Abelian
  integrals in one named Hamiltonian family" route — an explicit,
  algebraically-checkable zero bound for a concrete family of Hamiltonian
  systems, statable in Lean (bounds depend only on K and n).
```

```claim
id: h16-torregrosa-cubic-12-small-cycles-2024
status: sourced
statement: Torregrosa (2024), "Cubic planar vector fields with high local
  cyclicity", São Paulo J. Math. Sci. 18 (Sotomayor memorial issue):
  Theorem 1.1 — for α one of the two real simple roots of
  315α^14+4144α^12+4425α^10−9630α^8+1485α^6+5580α^4−1713α^2−510=0,
  there exist cubic perturbations of the exhibited one-parameter cubic system
  (1) such that TWELVE small-amplitude limit cycles bifurcate from the origin;
  Theorem 1.2 — for two values of β, cubic perturbations of system (2) produce
  twelve small-amplitude cycles from the equilibrium (x0,y0) =
  ((32β²−75)/(6(8β²+25)), 35β/(3(8β²+25))). This is the current best local
  lower bound M(3) ≥ 12 for the cyclicity of a cubic focus (previously
  M(3) ≥ 11, Żołądek). All Lyapunov-coefficient computations are exact
  polynomial arithmetic (CAS); the exceptional parameter values are located by
  Sturm sequences.
hypotheses: planar cubic vector fields; small-amplitude (local) limit cycles
  around a single monodromic equilibrium via degenerate Hopf bifurcation;
  perturbations of degree ≤ 3.
evidence-class: sourced (open-access full text held,
  research/sources/torregrosa-cubic-high-local-cyclicity-2024.full.md,
  DOI 10.1007/s40863-024-00486-9).
falsifier: an error in the Sturm-certified root localization or in the
  Lyapunov-coefficient computations — the paper states all computations are
  exact polynomial arithmetic with no numerics, so a clean-room re-derivation
  of the Lyapunov constants for system (1)/(2) would verify or refute;
  otherwise the claim stands.
holds-here: yes — this is the current best local (small-amplitude) lower
  bound for cubic systems, crossing GOAL's "twelfth small-amplitude cycle at a
  cubic focus" target; the explicit α polynomial and systems (1),(2) are
  reproducible and Lean-statably checkable.
```

```claim
id: h16-huzak-canard-hyperbolic-saddles-2022
status: sourced
statement: Huzak (2022), "Cyclicity of canard cycles with hyperbolic saddles
  located away from the critical curve", J. Differential Equations 320:479-509:
  for smooth (ε,µ)-families of planar slow-fast systems ẋ=f(x,y,ε,µ),
  ẏ=εg(x,y,ε,µ) with canard cycles Γ containing a hyperbolic saddle S away
  from the slow curve, exact finite cyclicity bounds: Thm 2.1 — if the slow
  dynamics is regular on the corner interval and S is attracting (resp.
  repelling) then Cycl(X,Γ) ≤ 1 and the limit cycle, if it exists, is
  hyperbolic; Thm 2.2 — S non-neutral (r≠1) gives bounds; Thm 2.3 — hyperbolic
  saddle at one corner point: cyclicity ≤ 3 when a connection breaks (S not
  neutral), and ≤ 2 with extra slow singularities; Thms 2.4-2.6 — corner
  singularities at both ends with product of hyperbolicity ratios ≠ 1 give
  upper bounds 2-3. Methods: family blow-up, slow divergence integral, singular
  perturbation theory, degenerate graphics. Also: such canard cycles occur in
  predator-prey models (Holling types II, IV) with small predator death rate.
hypotheses: smooth planar slow-fast systems, ε ≥ 0 singular perturbation
  parameter, one hyperbolic saddle away from the critical curve, Hopf/jump/
  non-generic turning point breaking mechanisms; canard cycle with corner
  points.
evidence-class: sourced (author-version full text held,
  research/sources/huzak-canard-cycles-hyperbolic-saddles-2022.full.md,
  bitstream 1942/36990/1/Hyperbolicsaddle.pdf, DOI 10.1016/j.jde.2022.02.050).
falsifier: an explicit smooth slow-fast system in the stated class whose
  canard cycle produces more limit cycles than the stated cyclicity bounds —
  no such counterexample is known; the theorems' hypotheses (neutrality,
  hyperbolicity-ratio products) are stated precisely so the bounds' scope is
  checkable.
holds-here: yes as a named instrument for GOAL's slow-fast/canard route —
  gives exact finite cyclicity bounds for a class of canard cycles; extends
  the library's slow-fast holdings (De Maesschalck-Roussarie birth of canards,
  Huzak DF2a, alien limit cycles) with hyperbolic-saddle-away-from-critical
  curves.
```

```claim
id: lu-h14-3-bundle-scripts-now-held
status: sourced
statement: The two Lu (2026) reproducibility-bundle scripts previously missing
  are now held as full texts:
  research/sources/lu-h14-3-verify-center-bautin.py.full.md and
  research/sources/lu-h14-3-verify-center-global-domains.py.full.md
  (from arxiv.org/src/2607.13785v2/anc/h14_3_reproducibility/certificates/).
  verify_h14_center_bautin.py reproduces the focal calculations for blueprint
  equations (B9)-(B10): builds the homogeneous focal values L1=(AC+CD+2DF−EF)/8,
  L2 (universal numerator), substitutes the H14 ω-parametrization
  (A=B/w, C=a(2B−1)/w², D=(a²(B−1)+m−ad)/w³, E=1/w, F=(a+d)/w², w²=1−a²),
  proves L2 vanishes on both exact center components (a=0,d=0 and m=−B,d=−a),
  solves ℓ1=0 to second order along the radial scaling, and checks
  L2|ℓ1=0 = (a(B+m)/48)ε² + O(ε³), giving U(0)=1/48.
  verify_h14_center_global_domains.py checks both global H14 center components
  exactly: (reversible) first integral H=(1/2)z^(−2B)x²+V(z) with
  V_z=z^(−2B−1)((z−1)−m(z−1)²) has zero Lie derivative, the extra critical
  point (0,1/m), and the source-minus-saddle barrier identity; (quadratic)
  inverse integrating factor (1+y)·k/(a²−1) with invariant conic k, gate point
  (−a/B,−1/B), and axis-factor (a−1)(a+1)(By+1)² on x=ay.
hypotheses: the H14_3 Bautin recurrence and both global center components, per
  Lu 2026's Theorem 1 framework.
evidence-class: sourced (full texts held; the pristine arXiv .py bytes' SHA-256
  are recorded in research/sources/lu-h14-3-spec-bautin.full.md rows
  6c22eb5f…/10a3ff15… and 37b5a823…/e7df44d9… — the held copies are
  markdown-wrapped conversions, so the recorded hashes certify the arXiv
  originals, and the held copies' bodies must be re-executed, not byte-hashed,
  to verify).
falsifier: re-executing the held script bodies (compare against the recorded
  canonical-stdout SHA-256, or re-derive clean-room) fails to reproduce the
  stated checks — L1/L2 focal identities, vanishing on both center components,
  U(0)=1/48, inverse-integrating-factor and barrier identities.
holds-here: yes — closes the documented gap that the two bundle scripts were
  "still not held"; the computational core of Lu 2026's H14_3 closure is now
  fully reproducible from held artifacts (see thread lu-h14-3-verification).
```

```claim
id: h16-villanueva-tucker-darboux-bautin-enclosure-2026
status: sourced
statement: Villanueva & Tucker (arXiv:2602.22558v2, 2026), "Darboux-type
  center conditions for families of planar polynomial vector fields":
  Theorem 1 gives an enclosure of the Bautin ideal 𝔅(ℱ_h(n)) = ⟨L1,L2,…⟩ of
  the homogeneous degree-n family ẋ=−y+F_n(x,y), ẏ=x+G_n(x,y) by the ideal
  generated by the coefficients of the first non-trivial homogeneous term of
  the Lyapunov function:
    for even n:  𝔅 ⊆ ⟨v_{n+1,0}, …, v_{0,n+1}⟩   and V_{n+1}=0 gives center conditions;
    for odd n:   𝔅 ⊆ ⟨L_{(n−1)/2}, v_{n+1,0}, …, v_{0,n+1}⟩  and
                 L_{(n−1)/2}=0 together with V_{n+1}=0 gives center conditions.
  Proposition 2: those center conditions correspond to Darboux centers —
  V_{n+1}=0 forces xF_n+yG_n=0 so the radial form ẋ=−y(1−F̃_n),
  ẏ=x(1−F̃_n) has integrating factor R=(x²+y²)^{λ1}/(1−F̃_n) and explicit
  first integral H. The proof is an induction (base m=2: L_{n−1} and all of
  V_{2n} are linear in v_{n+1}; general m>2 likewise), so all Lyapunov
  constants are linear functions of the coefficients of V_{n+1} — an explicit
  algebraic structure of the Lyapunov constants, valid for any degree n ≥ 2.
hypotheses: homogeneous planar polynomial systems of degree n ≥ 2
  (ℱ_h(n)), plus a non-homogeneous extension (Theorem 2, §5);
  Lyapunov-function/displacement-map setup; Darboux integrability.
evidence-class: sourced (full text held,
  research/sources/villanueva-tucker-darboux-center-bautin-ideal-2026.full.md,
  arXiv:2602.22558v2; abstract page at
  research/sources/villanueva-tucker-generic-bautin-cyclicity.arxiv.full.md).
falsifier: an explicit homogeneous polynomial system of some degree n where a
  Lyapunov constant is NOT a linear function of the coefficients of V_{n+1},
  or a center condition not captured by V_{n+1}=0/L_{(n−1)/2}=0 contradicting
  Theorem 1's enclosure; the paper itself notes "there are center conditions
  not captured by V_{n+1}=0", so the enclosure direction (⊆) is the precise
  claim to test.
holds-here: yes — this is a new instrument for GOAL's Bautin-ideal step: an
  explicit finite enclosure of the Bautin ideal for the full homogeneous
  degree-n family, exactly the algebraic structure (Lyapunov constants linear
  in a finite coefficient set) the run's verify_lu_core / lean Bautin
  recurrence targets. Unrefereed preprint (arXiv v2 2026-07-02); conditional.
```

```claim
id: h16-hilbert-1900-canonical-statement
status: sourced
statement: Hilbert's 16th problem, original 1900 wording (Newson translation,
  Bull. AMS 8 (1902) 437-479): for a first-order differential equation
  dy/dx = Y/X where X, Y are rational integral functions of degree n, determine
  the maximum number and relative position of Poincaré's "cycles limites"
  (boundary cycles). The problem is framed as answerable by the same method of
  "continuous variation of coefficients" as the algebraic part, and the two
  parts (real algebraic curves; limit cycles of the differential equation) share
  a number. This is the canonical statement that fixes H(n) as a uniform bound
  over the family (the uniformity is the whole content).
hypotheses: polynomial vector fields (X, Y rational integral of degree n).
evidence-class: sourced (Hilbert 1900, Newson 1902 translation, full text held
  in research/sources/hilbert-1900-mathematical-problems-newson.full.md,
  Project Gutenberg #71655).
falsifier: an authentic earlier/differing canonical wording — none expected; the
  Newson translation is the standard English reference.
holds-here: yes — anchors the uniform-bound reading of H16.2 used throughout.
```

```claim
id: h16-bautin-1952-m2equals3-primary
status: sourced
statement: Bautin (1952), "On the number of limit cycles appearing with
  variation of the coefficients from an equilibrium state of the type of a
  focus or a center", Mat. Sb. (N.S.) 30(72):1 (1952), 181-196: the maximum
  number of small-amplitude limit cycles bifurcating from a focus/center of a
  quadratic system under all coefficient variations is 3 (M(2)=3). The paper
  gives the exact definition of cyclicity of order k (§1), reduces to the
  canonical focus form (II), expands the radial equation in polar coordinates
  (III), and constructs a quadratic system with 3 limit cycles.
hypotheses: quadratic systems, small-amplitude cycles around a single
  focus/center (local problem, not global H(2)).
evidence-class: sourced (PRIMARY full text now held in
  research/sources/bautin-1952-full.pdf.full.md from mathnet's full-text PDF;
  previously recorded as "not openly downloadable").
falsifier: a quadratic system with 4 small-amplitude cycles from a single focus
  — would contradict M(2)=3. No such system is known; M(2)=3 is standard.
holds-here: yes — this is the literature boundary GOAL.md asks to reproduce
  (M(2)=3) before trusting anything computed past it, now at the primary source.
```

```claim
id: h16-llibre-schlomiuk-2004-qw3-every-h2-4-example
status: sourced
statement: Llibre & Schlomiuk (2004), "The Geometry of Quadratic Differential
  Systems with a Weak Focus of Third Order", Canad. J. Math. 56(2):310-343:
  (i) every known quadratic system with ≥4 limit cycles (H(2)≥4 examples of
  Shi/Chen-Wang) is obtained by perturbing a member of the QW3 family (weak
  focus of third order); (ii) QW3 admits a topological classification into 18
  phase portraits via integer-valued affine invariants (divisors, zero-cycles on
  the line at infinity); (iii) there is a neighborhood of the QW3 family (among
  quadratic systems with the same coefficient topology) with graphics but no
  polycycles and no limit cycles, in which any quadratic system has at most
  four limit cycles.
hypotheses: quadratic systems with a weak focus of third order.
evidence-class: sourced (full text held in
  research/sources/llibre-schlomiuk-weak-focus-third-order-cjm-2004.full.md,
  Cambridge open PDF).
falsifier: a quadratic system with ≥4 limit cycles NOT obtained by perturbing a
  QW3 member; or a fifth cycle in the stated neighborhood.
holds-here: yes — both establishes the QW3 centrality for H(2)≥4 and gives the
  only known upper bound (≤4) in a full neighborhood.
```

```claim
id: h16-ilyashenko-2016-digest-revised-proof
status: sourced
statement: Ilyashenko (2016), "Finiteness theorems for limit cycles: a digest
  of the revised proof", Izvestiya Math. 80(1):50-112 (first of two papers):
  a digest of the revised proof of the finiteness theorem for limit cycles of a
  planar polynomial vector field, plus sketches of the analytic-field analogue
  and the asymptotics of the monodromy transformation for polycycles. Uses
  "superexact asymptotic series" — the revised notion addressing the
  non-hyperbolic/oscillatory-asymptotics step.
hypotheses: individual fields; the revised proof targets the gap Yeung 2024
  locates in the 1991 monograph.
evidence-class: sourced (full text held in
  research/sources/ilyashenko-2016-digest-revised-proof.full.md).
falsifier: if Yeung's 2024-25 gap claim is correct and this digest does not
  repair the non-hyperbolic step, the Ilyashenko-side proof remains incomplete;
  conversely if it does, the gap claim is answered. Needs the scholar.
holds-here: yes as an Ilyashenko-side rejoinder; the exact relation to the Yeung
  counterexample is for the scholar to adjudicate.
```

```claim
id: drr-zhu-rousseau-2004-15-pp-graphics-16-total
status: sourced
statement: Rousseau & Zhu (2004), "PP-graphics with a nilpotent elliptic
  singularity in quadratic systems and Hilbert's 16th problem", JDE 196:169-208:
  (i) Theorem 1.1 restates the DRR reduction (uniform bound for quadratic iff
  all limit periodic sets surrounding the origin have finite cyclicity);
  (ii) Theorem 2.2: all 16 pp-graphics have finite cyclicity; (iii) Theorem 3.1:
  a pp-graphic through a triple nilpotent elliptic point with a hyperbolic
  saddle of ratio σ≠1 has cyclicity ≤2; Corollary 3.2: (I²₂₃),(I²₂₄),(I²₂₅)
  cyclicity ≤2. Altogether proves finite cyclicity of 15 DRR graphics (pp-type,
  not surrounding a center).
hypotheses: quadratic systems; pp-graphics through a multiplicity-3 nilpotent
  singularity of elliptic type NOT surrounding a center.
evidence-class: sourced (full text held in
  research/sources/rousseau-zhu-pp-graphics-nilpotent-elliptic-jde-2004.full.md
  from Rousseau's site). Independently restates Zhu 2005 (all 16 pp-graphics
  finite).
falsifier: a pp-graphic of this class with cyclicity >2 for σ≠1.
holds-here: yes — this fixes the boundary inside the DRR program between the
  closed pp-graphics (not surrounding a center) and the OPEN graphics that DO
  surround a center; the latter is where the remaining rows (I⁶b₁, H³₁₃, DI₂b
  full) sit.
```

```claim
id: h16-lower-bound-catalogue-2012
status: sourced
statement: Caubergh (2012) Liénard survey, p.2, gives the 2012 lower-bound
  catalogue: H(2)≥4, H(3)≥13, H(4)≥22, H(5)≥28, H(6)≥35, H(7)≥50,
  H(n)≥kn²ln n (Christopher-Lloyd), and the Li-Chan-Chung refinement
  H(n) ≥ 4(n+1)²(1.442695 ln(n+1) − 1/6) + n − 2/3. Confirms the n²log n
  asymmetry (no quadratic upper bound on H(n)).
hypotheses: polynomial vector fields of degree n.
evidence-class: sourced (full text held in
  research/sources/caubergh-lienard-h16-2012-uab.full.md).
falsifier: an upper bound on H(n) below the n²log n growth — none known; the
  held Buzzi-Novaes 2024 repeats the same n²log n lower bound.
holds-here: yes — corroborates the Established entries on lower bounds.
```

```claim
id: h16-moussu-bourbaki-1987-finitude
status: sourced
statement: Moussu, "Le problème de la finitude du nombre de cycles limites"
  [d'après R. Bamón et Yu. S. Ilyashenko], Séminaire Bourbaki 38e année 655,
  Astérisque 145-146 (1987) 89-101: sets the finiteness problem in Poincaré's
  framework — a cycle C is a periodic trajectory; it is a limit cycle iff the
  germ of its return map f is not the identity; when V is analytic f is
  analytic and a limit cycle is isolated in the set of periodic orbits.
  Theorem 0.1 (Bamón 1985): a quadratic vector field on R² has finitely many
  limit cycles. Theorem 0.2 (Ilyashenko 1984): the Dulac finiteness conjecture
  holds outside a proper algebraic subset of the space of vector fields (a
  corollary of Ilyashenko's fundamental results). Includes the reduction of the
  Dulac problem to polycycles (limits of cycles must accumulate on a polycycle),
  analytic extension of the return map in the log coordinate, N(2) ≥ 4 [37].
hypotheses: individual fields; analytic vector fields; the finiteness problem
  (not uniform in parameters).
evidence-class: sourced (full text held in
  research/sources/moussu-bourbaki-finitude-cycles-limites.full.md, Numdam).
falsifier: a retyped Dulac-1923 full text or a modern line-by-line account
  showing a different point of failure in Dulac's argument; the 1987 exposé is
  Bamón/Ilyashenko's 1980s state of the art and predates the 1991/1992 final
  proofs.
holds-here: yes — this is the canonical statement of Poincaré's limit-cycle
  definition (return-map germ ≠ identity, isolation in the set of periodic
  orbits) that the Lean statement h16_2 and the certified limit-cycle oracle
  must implement, and the earliest held treatment of the Dulac-conjecture
  reduction to polycycles.
```

```claim
id: h16-grau-manosas-villadelprat-chebyshev-2010
status: sourced
statement: Grau, Mañosas, Villadelprat, "A Chebyshev criterion for Abelian
  integrals", Trans. AMS (2010) — an extended Chebyshev-system criterion for
  bounding the number of zeros of Abelian integrals from the number of critical
  points and the geometry of the Hamiltonian level curves; the standard modern
  instrument for sharp zero-counts in specific Hamiltonian families.
hypotheses: Abelian integrals over ovals of a polynomial Hamiltonian; the
  criterion verifies that the generating functions form an extended complete
  Chebyshev system (ECT-system).
evidence-class: cited by the held Jibin Li 2003 survey's citation graph (174
  citations), abstract verified via search; full text NOT yet held.
falsifier: full text showing the criterion's hypotheses fail for a family this
  run would apply it to.
holds-here: yes as a named instrument for GOAL's "sharp zero-count for Abelian
  integrals in one named Hamiltonian family" route; to be downloaded next.
```

```claim
id: h16-alvarez-coll-demaesschalck-prohens-canard-lower-bounds-2020
status: sourced
statement: Álvarez, Coll, De Maesschalck, Prohens, "Asymptotic lower bounds on
  Hilbert numbers using canard cycles", J. Differential Equations 268(7)
  (2020) 3370-3391 — the most recent construction-style lower bound on H(n)
  built from canard cycles in slow-fast systems.
hypotheses: polynomial Liénard-type slow-fast families; asymptotic (as the
  slow-fast parameter → 0) counting of canard cycles.
evidence-class: cited in the held Llibre "From Abel to Hilbert" 2024 survey
  bibliography; full text NOT yet held.
falsifier: full text showing the construction does not produce the stated
  count.
holds-here: yes as a named instrument for the slow-fast test and for the
  lower-bound route; to be downloaded next.
```

```claim
id: h16-grau-manosas-villadelprat-chebyshev-2010
status: sourced
statement: Grau, Mañosas, Villadelprat, "A Chebyshev criterion for Abelian
  integrals", Trans. AMS 363 (2011) 109-129 (arXiv:0805.1140, held full):
  an extended Chebyshev criterion for Abelian integrals. Theorem A: for
  H(x,y)=Φ(x)+Ψ(y) with even-multiplicity Φ, Ψ at 0, involutions σ₁, σ₂ with
  Φ(x)=Φ(σ₁(x)), Ψ(y)=Ψ(σ₂(y)), define the balance ℬ_σ(κ)(x)=κ(x)−κ(σ(x)) and
  the chain g_{i+1}=g′_i/Ψ′. Then (I₀,…,I_{n−1}), I_i(h)=∫_{γ_h} f_i(x)g(y)dx,
  is an ECT-system on (0,h₀) if (ℬ_{σ₁}(f_i/Φ′)) is a CT-system on (0,x_r) and
  (ℬ_{σ₂}(g_i)) is a CT-system on (0,y_r) with ℬ_{σ₂}(g₀)(y)=o(y^{2m(n−2)}).
  Theorem B handles H=A(x)+B(x)y^{2m}, g(y)=y^{2s−1}: ECT if s>m(n−2) and
  (ℓ_i) with ℓ_i=ℬ_σ(f_i/(A′B^{(2s−1)/2m})) is a CT-system. The CT-system
  hypotheses are verified by computing Wronskians (Lemma 2.3), so the whole
  criterion is algebraic in many cases.
hypotheses: H separable (Theorem A) or A(x)+B(x)y^{2m} (Theorem B); ovals γ_h
  surrounding the origin; the CT-system balances.
evidence-class: sourced (full text held in
  research/sources/grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full.md,
  arXiv:0805.1140).
falsifier: a family satisfying the stated balances whose Abelian integrals
  nonetheless have more than n+k−1 zeros — would refute the criterion; none
  known; the paper reproves known results and proves new ones via it.
holds-here: yes — this is the wieldable instrument for GOAL step "sharp or
  improved zero-count for Abelian integrals in a named family": certify the
  balances algebraically (resultants + Sturm) and read off the ECT-system
  zero-count. Directly relevant to the run's Abelian-integral route and to
  Lean-statably checkable statements (Wronskian nonvanishing certificates).
```

```claim
id: h16-canard-asymptotic-lower-bound-2020
status: sourced
statement: Álvarez, Coll, De Maesschalck, Prohens, "Asymptotic lower bounds on
  Hilbert numbers using canard cycles", J. Differential Equations 268(7)
  (2020) 3370-3391: defines H̲(N) = (N² log N)/(2 log 2)·(1+o(1)) as N→∞, and
  proves there is a sequence N_k→∞ with H(N_k) ≥ H̲(N_k) for all k — an
  asymptotic lower bound on the Hilbert number H(N) matching the
  Christopher-Lloyd / Han-Li n²log n asymptotic. The construction uses
  singularly perturbed Liénard systems ẋ=y−F(x), ẏ=εG(x), canard cycles and
  nests, and singular Hopf bifurcation.
hypotheses: polynomial systems of degree N; the sequence N_k is subexponential
  in general; the bound is asymptotic, not for every N.
evidence-class: sourced (MaRDI review text of the article confirmed the exact
  statement; full text paywalled at ScienceDirect, DOI 10.1016/j.jde.2019.09.057;
  no open version located this cycle).
falsifier: an upper bound on H(N) below N² log N — none known; the held
  Buzzi-Novaes and Caubergh confirm the same n² log n growth.
holds-here: yes — this is the modern slow-fast/canard construction confirming
  the n² log n lower bound; the paper's own references include
  Huzak-De Maesschalck "Slow divergence integrals in generalized Liénard
  equations near centers" (EJQTDE 2014) and De Maesschalck-Dumortier
  "Bifurcations of multiple relaxation oscillations in polynomial Liénard
  equations" (Proc. AMS 2011) — two canard-instrument papers now frontier leads.
```

# Claims established by the reference library — Hilbert 16th, limit cycles

Each fenced `claim` block below is read into `derived/CLAIMS.md`. Status labels:
`sourced` = asserted-by-source (held full text or verified abstract); nothing
here is proved in this run. Evidence class, the exact source, and a falsifier
are given for each.

```claim
id: h16-dulac-finiteness-theorem
status: sourced
statement: A planar polynomial vector field has only finitely many limit
  cycles; the same holds for an analytic vector field on the 2-sphere. Proved
  independently by Ilyashenko (1991) and Écalle (1992), after Ilyashenko found
  ~1981 the gap in Dulac's 1923 proof.
hypotheses: individual field fixed (no uniformity in coefficients).
evidence-class: sourced (Ilyashenko, "Centennial History of Hilbert's 16th
  Problem", Bull. AMS 39 (2002) 301-354, held in full in
  research/sources/ilyashenko-centennial-history-h16.full.md)
falsifier: a published, refereed disproof — see below, the 2024 preprints
  claim exactly this for Ilyashenko's *approach*.
holds-here: yes as the classical received statement; see the separate claim on
  the 2024 gap claims, which put the *proof*, not the theorem, under question.
```

```claim
id: h16-gap-claims-2024
status: sourced
statement: The gap claim in Ilyashenko's approach to Dulac's finite-limits
  theorem is now made in PEER-REVIEWED form: Yeung, "Dulac's Theorem
  Revisited", Qual. Theory Dyn. Syst. 24 (2025) Art. 57,
  doi:10.1007/s12346-025-01220-2 (held full text), asserts the approach of
  Ilyashenko (1991 monograph) has a gap — the argument that its asymptotics
  are not themselves oscillatory is insufficient — gives an explicit
  counterexample, and draws confines to which Ilyashenko's result may be
  restricted to keep validity. Preprint precursors: Yeung arXiv:2402.12506
  (held full HTML), Palma-Márquez–Yeung arXiv:2410.07532 (maximum-modulus
  dichotomy, partial repair); Yeung arXiv:2409.13630 proves a specific
  hyperbolic-polycycle case in Ilyashenko's style. The classical *theorem*
  (finitely many limit cycles) is not claimed false; the *published proof's
  completeness* is under active contention, and hyperbolic polycycles remain
  the fully-understood corner stone.
hypotheses: These are the current (2024-2025) claims in the field. The 2025
  paper is peer-reviewed; the 2024 arXiv precursors are not. No Ilyashenko-side
  rebuttal located yet.
evidence-class: sourced (held full text of Qual. Theory 2025 in
  research/sources/yeung-dulac-theorem-revisited.full.md and of
  arXiv:2402.12506 HTML).
falsifier: a published refutation of the counterexample, or an independent
  verified completion of Ilyashenko's step; either side's community acceptance.
holds-here: this is live contention to report. It puts "finite limit cycles
  for a fixed field" at "settled modulo a contended proof" — directly relevant
  to GOAL.md's question of whether a complete proof of H(2)<∞ (or even of the
  individual finiteness statements it rests on) stands.
```

```claim
id: h16-bamon-quadratic-finiteness
status: sourced
statement: Bamón (1986), "Quadratic vector fields in the plane have a finite
  number of limit cycles", Publ. Math. IHÉS 64, 111-142,
  doi:10.1007/BF02699193 (held): each individual quadratic planar field has
  finitely many limit cycles. This is finiteness for a fixed quadratic field,
  NOT the uniform H(2) bound. Bamón used Ilyashenko's 1984/85 result on
  non-accumulation of limit cycles around hyperbolic singular cycles.
hypotheses: n=2, individual field.
evidence-class: sourced (bibliographic record + title/abstract held; relies on
  the Chile survey's account).
falsifier: a single quadratic field with infinitely many limit cycles.
holds-here: yes as individual-finiteness for n=2; it does NOT settle H(2).
```

```claim
id: drr-df1a-df2a-cyclicity-sourced
status: sourced
statement: Dumortier–Rousseau 2009 (Comm. Pure Appl. Anal. 8:1133–1157,
  "Study of the cyclicity of some degenerate graphics inside quadratic
  systems", full text now held from dms.umontreal.ca/~rousseac/
  Dumortier_Rousseau.pdf) treats the DRR degenerate graphics DF1a and DF2a and
  gives the exact 5-parameter normal forms for the 13 degenerate graphics with
  a line of singular points (3 normal forms suffice: finite-plane line
  {ẋ=y+bxy−y²+µ1+µ2x+µ3x², ẏ=xy+µ4} for DF1a,DF1b,DF2a,DF2b,DH1,DH2; infinity
  line {ẋ=cx−y+1+(1+µ2)x²+µ1xy+µ0y², ẏ=xy−µ3x²} for DI1a,DI1b,DI2a,DI2b,DH3,DH4;
  and DH5 with a 7-parameter unfolding because no analytic 5-normal form
  exists — its slow motion is ẋ=µ0+µ1x+µ2x² on the line and
  ẋ=µ3+µ4v+µ5v²+µ6v³ on the equator). Thm 3.1: DF1a (b0∈(0,2)) has at most 3
  limit cycles (≤1 if E1≥0); DF2a (b0=0) at most 5 (≤1 if bE1≥0, ≤1 on the
  circle {D=E1=0}). The single remaining open point is P*=(D,E0,E1,E2)=
  (0,0,0,1), where the family CANNOT be desingularized — a genuine obstruction
  (E0=D=0, E1=0 gives several expected limit cycles and no blow-up exists).
hypotheses: n=2; degenerate graphics with a line of singular points; x0 in a
  compact subset of (0,∞).
evidence-class: sourced-held (full text of Dumortier–Rousseau 2009).
falsifier: a counterexample with more limit cycles than the stated bounds, or
  a proof that P* has infinite cyclicity.
holds-here: yes — this is the primary source for the DF1a/DF2a rows, upgrading
  them from 'reported' (Shan thesis) to sourced-held.
```

```claim
id: drr-rousseau-2008-pp-center-cyclicity2-sourced
status: sourced
statement: Roussarie–Rousseau 2008 (Bull. Belg. Math. Soc. Simon Stevin,
  "Finite cyclicity of nilpotent graphics of pp-type surrounding a center",
  full text held from dms.umontreal.ca/~rousseac/Roussarie_Rousseau.pdf)
  proves finite cyclicity of 4 DRR graphics through a triple nilpotent point
  of elliptic type surrounding a center: (H1_7), (F1_7a), (H3_11), (I1_6a),
  all of pp-type (join two parabolic sectors of the nilpotent point). Exact
  cyclicity = 2 for (H1_7) and (H3_11); (F1_7a) and (I1_6a) occur in
  continuous families with exact cyclicity 2 except for a discrete subset.
  The method is stated to apply to most other graphics through a triple
  nilpotent point surrounding a center.
hypotheses: n=2; DRR graphics through a triple nilpotent elliptic point
  surrounding a center.
evidence-class: sourced-held (full text of Roussarie–Rousseau 2008).
falsifier: a counterexample with >2 stable limit cycles near one of these
  graphics, or a proof that a discrete-subset member has cyclicity >2.
holds-here: yes — upgrades the drr-... pp-type cyclicity-2 rows from 'reported'
  (Shan thesis) to sourced-held.
```

```claim
id: drr-zhu-2005-pp-graphics-16
status: sourced
statement: Zhu 2005 (Proc. proceedings "From the pp-graphics to the finiteness
  part of Hilbert's 16th problem for quadratic systems", full text held from
  YorkSpace bitstream 3526f30d) states Theorem 1.2: all 16 pp-graphics of
  quadratic systems have finite cyclicity (including the hemicycle H1_16 and
  related structures); Theorem 1.1: a pp-graphic with a triple nilpotent
  elliptic point (Epp) with two parabolic and two hyperbolic sectors has
  cyclicity bounded by n if the nth derivative of the regular transition map
  is non-vanishing. This is the primary survey of the pp-graphics route
  (frontier's top-cited row, 9 citations from this library's sources).
hypotheses: n=2; pp-graphics (parabolic-parabolic) in quadratic systems.
evidence-class: sourced-held (full text of Zhu 2005).
falsifier: a pp-graphic in the list of 16 with unbounded cyclicity, or a
  counterexample to the transition-map-derivative bound hypothesis.
holds-here: yes — primary source for the "16 pp-graphics finite" statement.
```

```claim
id: drr-zhu-rousseau-2002-nilpotent-machinery
status: sourced
statement: Zhu–Rousseau 2002 (J. Differential Equations 178:325–436,
  "Finite cyclicity of graphics with a nilpotent singularity of saddle or
  elliptic type", full text held from YorkSpace bitstream fc2121d3) proves
  finite cyclicity of several generic graphics through a nilpotent point of
  saddle or elliptic type of codimension 3 in C∞ families; in some cases the
  result depends only on the nilpotent point having multiplicity 3, not the
  exact codimension. Method: blow-up of the family, two types of Dulac maps,
  a method proving some regular transition maps have nonzero higher
  derivative, and a generalized derivation–division (Roussarie) technique. This
  is the primary machinery behind the nilpotent-graphics closures (inside the
  88-by-2015 tally).
hypotheses: planar C∞ families; graphics through nilpotent saddle/elliptic
  point of codimension 3 (some cases multiplicity-3 only).
evidence-class: sourced-held (full text of Zhu–Rousseau 2002).
falsifier: a codimension-3 nilpotent graphic with unbounded cyclicity,
  contradicting the derivation–division bound.
holds-here: yes — primary machinery source for the nilpotent rows.
```

```claim
id: drr-saddle-node-normalforms-dir2002
status: sourced
statement: Dumortier–Ilyashenko–Rousseau 2002 (Ergodic Theory Dynam. Systems
  22:783–818, "Normal forms near a saddle-node and applications to finite
  cyclicity of graphics", full text held from dms.umontreal.ca/~rousseac/
  DIR.pdf) gives normal forms near a saddle-node and applies them to finite
  cyclicity of graphics; this is the saddle-node normal-form machinery used
  throughout the DRR program's semi-hyperbolic and nilpotent closures.
hypotheses: planar analytic vector fields; saddle-node singular points in
  graphics.
evidence-class: sourced-held (full text of DIR 2002).
falsifier: a saddle-node graphic whose transition maps contradict the normal
  form / cyclicity bounds derived.
holds-here: yes — the saddle-node normal-form anchor for the DRR program.
```

```claim
id: drr-dmrt-2015-fake-saddle-cyclicity2
status: sourced
statement: De Maesschalck–Rebollo-Perdomo–Torregrosa 2015 (J. Differential
  Equations 258(2):588–620, "Cyclicity of a fake saddle inside the quadratic
  vector fields", open-access UAB DDD postprint now held in
  research/sources/demaesschalck-rebollo-torregrosa-fake-saddle-2015-postprint.full.md
  from https://ddd.uab.cat/pub/artpub/2015/gsduab_3787/
  joudifequ_a2015v258n2p588preprint.pdf) studies the cyclicity of small-amplitude
  limit cycles near an unfolded fake saddle (a degenerate singular point, also
  "impassable grain", whose normal form is a degenerate flow box with parallel
  fibers and one node on the singular fiber) and shows the cyclicity is ≥ 2 when
  the normal form is quadratic. This is the companion primary source to Marín
  2026's uniform fake-saddle transition-map expansion and anchors the thread
  `fake-saddle-transition-maps` for the DRR degenerate D-families at infinity.
hypotheses: planar vector fields near a fake saddle of quadratic normal form.
evidence-class: sourced-held (open-access postprint full text).
falsifier: a quadratic fake-saddle unfolding with cyclicity < 2, or a
  counterexample to the ≥2 lower bound.
holds-here: yes — resolves the fake-saddle thread's blocked-by (DMRT 2015
  previously only a "Redirecting" stub, now full primary text).
```


```claim
id: h16-drr-121-graphics
status: sourced
statement: H(2) < ∞ is equivalent (via the compactness/DRR program of
  Dumortier, Roussarie and Rousseau 1994, J. Diff. Eq. 110, 86-133) to proving
  finite cyclicity of 121 graphics in S²×K, where K is the compactified
  parameter space of quadratic anti-saddle-type systems and S² the Poincaré
  sphere. Proving the (I¹₁₂), (I¹₁₃) graphics (Rousseau–Shan–Zhu 2015) brought
  the count of graphics with proved finite cyclicity to 88 of 121. Verified
  post-2015 closures include: degenerate graphics DF2a (Huzak 2018,
  CPA 17(3):1305-1316, family blow-up + slow divergence integral; DF1a was
  Dumortier–Rousseau 2009, CPA 8), and the center-surrounding triple-nilpotent
  graphics (I¹₁₄), (I¹₆b), (H³₁₃), (DI²b) with (H³₁₄) left open (Roussarie–
  Rousseau 2015, Moscow Math. J.). Free full-text account:
  Huzak 2018 "Cyclicity of degenerate graphic DF2a" starts from
  Dumortier–Rousseau 2009 "Study of the cyclicity of some degenerate graphics
  inside quadratic systems", CPA 8 (2009) 1133-1157.
hypotheses: n=2; graphics surround a nondegenerate singular point of
  anti-saddle type; parameter family compact.
evidence-class: sourced (Rousseau–Shan–Zhu arXiv:1502.00689 held full HTML;
  Huzak 2018 held full bibliographic + abstract; Roussarie–Rousseau 2015
  held abstract/text).
falsifier: a graphic of the 121 proved to have INFINITE cyclicity, or a
  complete proof of finite cyclicity for all 121 (none published); or a named
  open graphic like (H³₁₄) being closed or shown open in a later paper.
holds-here: yes. NOTE 121-vs-125 discrepancy (Shan 2013 thesis counts 125) —
  to be settled from the DRR 1994 paper itself.
```


```claim
id: h16-drr-closed-rows-2015
status: sourced
statement: As of the 2015 literature, at least 88 of the 121 DRR graphics have
  finite cyclicity proved inside the quadratic family (Rousseau–Shan–Zhu 2015
  state verbatim that proving (I₁₂¹),(I₁₃¹) "will bring the number of graphics
  of the program for which finite cyclicity is proved to 88"). Specific rows
  closed with their papers: (I₁₂¹),(I₁₃¹) — Rousseau–Shan–Zhu 2015,
  arXiv:1502.00689 (held full text: I₁₃¹ via Thm 4.3; I₉b² in the codim-3
  case via the same computation as I₁₂¹); (I₁₄¹) — Roussarie–Rousseau 2015,
  Trans. Moscow Math. Soc. Thm 1.2 (held full text). For (I₆b¹), (H₁₃³),
  (DI₂b) only the BOUNDARY limit periodic set from the blow-up is closed
  (RR 2015 Thm 1.1); the full graphics are left open ("intend to address the
  problem in the next future"), and (H₁₄³) is the one graphic through a triple
  point at infinity with no partial result (RR 2015 intro). Earlier (pre-2015,
  inside the 88): HR/nilpotent families Ji2, Ji3, Jb, fib (Zhu–Rousseau/Shan
  2013); nilpotent pp-type H₇¹, F₇a¹, H₁₁³, I₆a¹ (Roussarie–Rousseau 2008,
  cyclicity 2); DF1a, DF2a (Dumortier–Rousseau 2009; DF2a re-examined by Huzak
  2018).
hypotheses: n=2; graphics surround a nondegenerate anti-saddle point; finite
  cyclicity inside the quadratic coefficient family S²×K.
evidence-class: sourced (RSZ 2015 held full HTML; RR 2015 abstract/theorem
  text verified; pre-2015 rows confirmed via thesis/survey summaries only →
  those rows are `reported` in drr-list.md, not full-text-held).
falsifier: a held primary source giving a different closed-count, or a graphic
  here marked closed later shown still open (e.g. if DF2a was closed only in
  2018 rather than 2009, or if the RR-2015 "one open boundary set" is a
  specific named graphic that this block would then mis-label).
holds-here: yes at the level of "at least 88 by 2015" (author-stated) and the
  specifically named rows; NOT as a complete 121-row enumeration (that needs
  the DRR 1994 paper, which is not held).
```

```claim
id: h16-drr-open-rows
status: sourced
statement: The DRR program is NOT complete: at least 33 of the 121 graphics
  were still open as of RSZ 2015 (88 closed), and the open rows lie
  overwhelmingly in the nilpotent and degenerate families. Named open /
  partially-open rows: (i) (H₁₄³) — the one graphic through a triple point at
  infinity with no partial result in Roussarie–Rousseau 2015 (the primary text
  states "We have a partial result for every graphic, but one (namely (H₁₄³)),
  through a triple point at infinity");
  (ii) (I₆b¹), (H₁₃³), (DI₂b) — only their boundary limit periodic sets are
  closed (RR 2015 Thm 1.1); the full graphics are explicitly left open
  ("intend to address the problem in the next future");
  (iii) the 11 degenerate graphics other than DF1a, DF2a (Shan 2013 thesis).
  The exact full list of open graphic ids and the precise post-2015 open count
  are NOT established by any held source. The open count here is a lower bound
  on openness, not the exact number: at least 32 of 121 are not fully closed
  (after RR 2015's full closure of I₁₄¹ on top of RSZ's 88), plus 3 partially
  closed rows, and the one open sub-problem μ₁=0 in RSZ Thm 3.2.
hypotheses: n=2; finite cyclicity in the quadratic family.
evidence-class: sourced for "88 by 2015", "(H₁₄³) the one with no partial
  result", "boundary sets of I₆b¹,H₁₃³,DI₂b only" (RR 2015 primary text held);
  reported for the 11 degenerate open (Shan 2013 thesis).
falsifier: a held post-2015 primary source that closes one of the 11 degenerate
  graphics, or (I₆b¹)/(H₁₃³)/(DI₂b) fully, or (H₁₄³); or a complete proof of
  all 121 (none exists).
holds-here: yes as reported level; the exact open count remains the live gap
  for request dumortier-roussarie-rousseau-9c4f.
```

```claim
id: h16-drr-121-vs-125-discrepancy
status: reported
statement: The DRR catalog of quadratic graphics is usually stated as 121
  (DRR 1994; RSZ 2015; Ilyashenko 2002; RR 2015), but the Shan 2013 thesis
  summary counts 125 graphics "in the standard family around the origin" with
  40 challenging cases. The same program is being described with two totals.
  Whether this is a different grouping/vertex-counting convention or a
  genuinely different list is not resolved — the DRR 1994 paper itself (the
  canonical catalogue) is not held.
evidence-class: reported (secondary/thesis summaries; DRR 1994 full text not
  held).
falsifier: the DRR 1994 paper's own count, or a primary source that reconciles
  the two totals.
holds-here: recorded as an open discrepancy to resolve before any downstream
  attack trusts a single total.
```

```claim
id: h16-abelian-integral-bounds
status: sourced
statement: Tangential/infinitesimal H16: the number of isolated zeros of
  Abelian integrals (and so limit cycles born in a first-order perturbation of
  a Hamiltonian polynomial field) is uniformly bounded. Varchenko, Khovanskii
  non-constructive; Binyamini–Novikov–Yakovenko (2010, Invent. Math. 181)
  explicit double-exponential bound; Binyamini–Dor (2012) explicit bound
  linear in deg ω: N(n,m) ≤ exp⁺(n²)·m + exp⁺(n²).
hypotheses: deg H ≤ n+1, deg ω ≤ n; nonsingular ovals.
evidence-class: sourced (BNY arXiv:0808.2952, BD arXiv:1108.1846 held).
falsifier: an Abelian integral with more zeros than the bound for explicit
  small n,m.
holds-here: yes; this is the linearised problem, NOT H16.2 itself.
```

```claim
id: h16-kaloshin-uniform-bound
status: sourced
statement: Hilbert–Arnold problem for elementary polycycles: for a generic
  k-parameter family of smooth planar fields with only elementary singular
  points, cyclicity is finite with explicit bound E(k) ≤ 2^{25 k²} (Kaloshin);
  Ilyashenko–Yakovenko proved finiteness with a primitive-recursive bound.
hypotheses: elementary singularities only; generic finite-parameter family.
evidence-class: sourced (Kaloshin arXiv:math/0111053; Ilyashenko Centennial).
falsifier: a k-parameter family with elementary singularities producing more
  than the bound.
holds-here: yes; elementary is the weight-bearing hypothesis — nilpotent and
  degenerate points are outside it.
```

```claim
id: h16-lower-bounds
status: sourced
statement: H(2) ≥ 4 (Shi 1982; Chen–Wang 1979) with (3,1) configuration; H(2)=4
  is the standing conjecture but OPEN; H(3) ≥ 13 (Li–Liu–Yang 2009); H(4) ≥ 28
  (Prohens–Torregrosa 2018); M(2)=3 (Bautin 1952); M(3) ≥ 11 (Żołądek);
  H(n) grows at least as fast as (n+2)^2 log(n+2)/(2 log 2) — i.e. order
  n^2 log n — so H(n) is NOT bounded above by any quadratic polynomial in n.
  [CORRECTED 2025: the earlier "(n+2)^2/ln(n+2), order n^2/ln n" wording was
  a transcription inversion; the held full text of Buzzi-Novaes (2024), quoting
  Christopher-Lloyd 1995 and Han-Li 2012, has liminf H(n)/((n+2)^2 log(n+2))
  >= 1/(2 log 2), which is n^2 log n growth.]
hypotheses: none beyond degree.
evidence-class: sourced (abstracts/records of the named papers; M(2)=3 via
  Liang–Torregrosa held, and Kuznetsova survey).
falsifier: a certified configuration beating the stated bound for its degree.
holds-here: yes, as lower bounds. NOTE: the precise asymptotic constant and
  whether it is n² ln n or n²/ln n needs a primary source download (only
  abstract-level now).
```

```claim
id: h16-lienard-ldmp-disproved
status: sourced
note: attribution nuance (scholar, 2nd pass, per held Llibre-Zhang postprint
  pp. 2-3): DPR 2007's own contribution was n >= 7 (one extra cycle beyond the
  conjecture). The degree-6 system with 4 limit cycles is a base case in the
  survey's own proof (following De Maesschalck-Huzak 2015): I1(x)=0.4x^3
  -1.248x^5+1.17429x^7-0.3x^9 has exactly 3 positive zeros -> 4 cycles. The
  core claim (conjecture FALSE for n>=6) is unaffected; only the specific
  "degree-6 example from DPR 2007" attribution is loose.
statement: The Lins–de Melo–Pugh conjecture — classical Liénard ẋ=y−F(x),
  ẏ=−x with deg F = n has at most ⌊(n−1)/2⌋ limit cycles — is FALSE for
  n ≥ 6. A degree-6 f with 4 limit cycles exists (survey's own construction
  following De Maesschalck–Huzak 2015; DPR 2007's own paper established n ≥ 7
  with one extra cycle); later work gives ≥ n−2 cycles for n ≥ 6. n=5 was
  open as of Llibre–Zhang 2017 survey. The classic bound is achieved (not
  exceeded) by simple FSTS-canard families (De Maesschalck–Dumortier 2010).
hypotheses: classical Liénard form.
evidence-class: sourced (abstracts of DPR 2007, Dumortier–Llibre counterexamples,
  Llibre–Zhang survey). Full text of DPR 2007 NOT held (only AMS landing pages
  downloaded — see librarian report).
falsifier: a degree-n≥6 Liénard system with fewer than the claimed constructible
  count (does not exist) — this is instead a WARNING for the slow–fast test.
holds-here: yes as the received disproof.
```

```claim
id: h16-lienard-n5-open
status: sourced
statement: For the classical Liénard system the exact maximum number of limit
  cycles for degree n=5 was open as of the 2017 Llibre–Zhang survey: whether a
  degree-5 system can have more than ⌊(5−1)/2⌋=2 limit cycles was unknown.
evidence-class: sourced (Llibre–Zhang 2017 FULL postprint held in
  research/sources/llibre-zhang-lienard-survey-postprint-2017.full.md; the
  survey's open problem is verbatim "What is the maximum number of limit
  cycles for the Liénard differential systems (1) when n ≥ 5?" and Theorem 2
  leaves only n=5 undecided).
falsifier: a published determination of the degree-5 Liénard maximum after the
  survey.
holds-here: reported as open per the held source; needs a post-2017 check.
```

```claim
id: h16-drr-h14-3-lu-2026-claim
status: asserted-by-source
statement: H. Lu, "Local Uniform Finite Cyclicity of the H₁₄³ Semihyperbolic
  Hemicycle", arXiv:2607.13785 (Jul 2026, 80 pp., unrefereed preprint),
  claims finite cyclicity for exactly the (H³₁₄) graphic that Roussarie–
  Rousseau 2015 left open. The claim: for the full five-parameter quotient
  unfolding (1.3) (= RR 2015 Theorem 3.1's family (3.2) with B=0 the H₁₄³
  case), there is a fixed annual collar U of Γ_{H₁₄³}, a neighborhood Λ⊂ℝ⁵ of
  0, and a finite constant B such that every λ∈Λ has ≤ B isolated limit
  cycles in U. Bound existential, not explicit. Identification is source-
  backed from both sides: RR 2015 line 63 "We have a partial result for every
  graphic, but one (namely (H³₁₄))", and Lu's §1.2 citing RR Theorem 3.1
  B=0 as precisely the H₁₄³ case.
hypotheses: n=2; graphic through triple nilpotent point at infinity
  (semihyperbolic hemicycle, noncompact source, two semihyperbolic endpoints,
  upper-equatorial degeneration); full 5-parameter quotient unfolding.
evidence-class: asserted-by-source (PREPRINT, NOT peer-reviewed; full HTML
  held in research/sources/lu-h14-3-hemicycle-html.full.md; RR 2015 full text
  held; identification verified against both texts).
falsifier: peer review finding an error in the stopped-first-hit atlas or one
  of the zero theorems; a published counterexample; or rejection of the
  preprint. Also falsifiable if the paper's "local uniform finite cyclicity in
  one collar" turns out not to match DRR's definition of finite cyclicity of
  the graphic (needs DRR 1994, not held).
holds-here: as a claim to chase, NOT established. The library's recorded open
  graphic (H³₁₄) now has a candidate closure in preprint form, and the
  candidate has ancillary reproducibility code. Priority: verify.
```

```claim
id: h16-drr-lu-2026-does-not-complete-program
status: sourced
statement: Even if Lu 2026 is correct, the DRR program is not complete. The
  closure of (H³₁₄) is one graphic. As of RR 2015 the open/partially-open
  rows also include full graphics (I₆b¹), (H₁₃³), (DI₂b) (only boundary sets
  closed) and ≥11 degenerate graphics beyond DF1a/DF2a (Shan 2013). The
  consolidated post-2015 graphic-by-graphic ledger is still NOT in the
  library.
hypotheses: n=2.
evidence-class: sourced (RR 2015 held full text; Shan 2013 thesis held).
falsifier: a complete ledger showing a different set of open graphics.
holds-here: yes.
```

```claim
id: h16-four-cycles-songling-galias-tucker
status: sourced
statement: The Songling quadratic system — ẋ = λx − y − 10x² + (5+δ)xy + y²,
  ẏ = x + x² + (−25+8ε−9δ)xy with δ≈−10⁻¹³, ε≈−10⁻⁵², λ≈−10⁻²⁰⁰ — has
  EXACTLY four limit cycles, proved rigorously by interval arithmetic
  (adaptive precision, P-map fixed points, explicit positional bounds for all
  four cycles spanning scales from 10⁻⁷⁵ to ~0.04). Verified configuration
  (Fig. 2 caption): three of the four limit cycles surround the origin, the
  fourth surrounds the equilibrium (0,1) — i.e. the (3,1) configuration
  associated with Shi's H(2)≥4 example. The four are alternately stable /
  unstable (P'<1 / P'>1, P' extremely close to 1 for the three inner cycles).
  This is a certified computational reproduction of Shi's 1980 H(2) ≥ 4 lower
  bound, and a model oracle (trapping-region/return-map with certified sign
  change) for this run's own certifier.
hypotheses: H(2) ≥ 4 with a (not necessarily (1,3)) configuration; does not
  show the 4 cycles can be arbitrary; the exponential separation of scales is
  essential to the difficulty.
evidence-class: verified-computationally (rigorous, reflexive, interval)
  — full text held in research/sources/galias-tucker-songling-four-cycles.full.md.
falsifier: a flaw in an interval-arithmetic branch; a corrected count.
holds-here: yes — H(2) ≥ 4 is confirmed by a fully certified computation,
  stronger than the historical asserted lower bound.
```

```claim
id: h16-strong-monotone-gasull-santana
status: sourced
statement: H(n) is a strictly increasing function of the degree when finite:
  H(n+1) ≥ H(n) + 1 for all n ∈ N (Gasull–Santana, PAMS 153 (2025),
  669–677, arXiv:2407.13465). Also H(n) is realizable by structurally stable
  fields with only hyperbolic limit cycles (if finite), and H(n) ≤ ℵ₀.
hypotheses: none beyond plane polynomial fields of degree n.
evidence-class: sourced (postprint held full)
  — research/sources/gasull-santana-note-h16-pams-2025.full.md; peer-reviewed
  Proc. AMS 2025.
falsifier: a published error in the sup/inf argument; a family with
  H(n+1) = H(n).
holds-here: yes.
```

```claim
id: h16-christopher-lloyd-weakened-16th
status: sourced
note: PROVENANCE CORRECTED (scholar, 2nd pass) — the held full text is by
  Chengzhi Li, Weigu Li, Jaume Llibre, Zhifen Zhang (2001), not Christopher &
  Lloyd. Christopher & Lloyd 1995 ("Polynomial systems: a lower bound for the
  Hilbert numbers", Proc. R. Soc. Lond. A 450:219-224) is a DIFFERENT,
  paywalled paper giving the H(n) ≳ n² log n growth. The two were conflated
  by the librarian; the mathematical content of this claim (the b_{m,n}
  tangential bound at one singular point) is correct and belongs to the
  2001 Li-Li-Llibre-Zhang paper.
statement: Li-Li-Llibre-Zhang (2001), "Polynomial systems: a lower bound for
  the weakened 16th Hilbert problem", Extracta Math. 16(3), 441–447: for m, n
  odd, the maximum number b_{m,n} of isolated zeros (with multiplicity) of the
  Abelian integral I(h)=∮_{H=h} ȳQ dx with H = y²/2 + x^{m+1}/(m+1), deg Q ≤
  n−1 is at least ((n+1)(n+3)/8 − 1) if n ≤ m, and ((m+1)(2n−m+3)/8 − 1) if
  n ≥ m; hence b_{m,n} ≤ N(m,n) ≤ H(max{m,n}). Growth of order n². This is
  the primary (open-access) treatment of the tangential/weakened H16 lower
  bound at a single singular point.
hypotheses: m,n odd; Hamiltonian H as given; perturbation of the centre.
evidence-class: sourced (full text held)
  — research/sources/christopher-lloyd-weakened-16th-extracta-2001.full.md.
falsifier: an error in the zero-counting / Abelian-integral multiplicity
  argument.
holds-here: yes — confirms the weakened-H16 growth rate O(n²) directly from
  the primary source.
```

```claim
id: h16-121-vs-125-rrousseau-survey
status: sourced
statement: Chris Rousseau's own survey "Hilbert's 16th problem for quadratic
  vector fields and cyclicity of graphics" (Nonlin. Anal. 30(1), 1997) describes
  the DRR program as proving finite cyclicity of the 121 graphics and
  summarizes methods (§1). Note: the survey predates the RSZ/RR closures; the
  121-vs-125 discrepancy (RSZ/RR/Ilyashenko say 121, Shan 2013 thesis says
  125) is NOT resolved by this survey — it states 121. The BIRS 2007 workshop
  report independently confirms the DRR reduction (compactify phase×param →
  limit periodic sets finite cyclicity) and that H(2)<∞ reduces to 121
  graphics.
hypotheses: n=2.
evidence-class: sourced (BIRS report full held;
  research/sources/birs-workshop-h16-2007-report.full.md; Rousseau 1997
  abstract via search).
falsifier: a source stating a different DRR graphic count.
holds-here: yes for the 121 frame; the 125 discrepancy remains open.
```

```claim
id: h16-lienard-ldmp-survey-2017
status: sourced
statement: Llibre & Zhang (2017), "Limit cycles of the classical Liénard
  differential systems: a survey on the Lins Neto, de Melo and Pugh's
  conjecture", Expo. Math. 35(3), 286–299: the LdMP conjecture (at most
  ⌊(n−1)/2⌋ cycles for deg F = n) holds for n ≤ 4 (no cycles for n=1,2; ≤1 for
  n=3,4); is FALSE for n ≥ 6 (at least n−2 cycles, constructions: DPR 2007
  n≥7, De Maesschalck–Dumortier n≥6, De Maesschalck–Huzak n−2 for n≥6); and
  for n=5 is OPEN/unresolved as of this survey. This replaces the contaminated
  held file (which was an unrelated power-grid paper) as the correct
  Liénard-survey anchor.
hypotheses: classical Liénard ẋ=y−F(x), ẏ=−x, F of degree n.
evidence-class: sourced (FULL postprint PDF held, with complete proofs of the
  known results)
  — research/sources/llibre-zhang-lienard-survey-postprint-2017.full.md;
  the earlier .uab record page is only metadata.
falsifier: a source closing the n=5 case (≥3 cycles for deg-5 Liénard).
holds-here: yes.
```

```claim
id: drr-ledger-no-consolidated-post2020
status: sourced
statement: No consolidated graphic-by-graphic ledger of the 121 DRR graphics
  with a running closed-count and the paper closing each row exists in the
  published literature, as of this run's searches (2023-2025). Christiane
  Rousseau has published no status survey of the DRR program since the 2015
  papers (Rousseau–Shan–Zhu arXiv:1502.00689; Roussarie–Rousseau Trans. Moscow
  Math. Soc. 76, 2015): her authored arXiv/OpenAlex/Math-Net/Dialnet records
  through 2025 and her Montréal publications page (held) show no consolidation.
  The DRR 1994 original (the only complete 121-id list) is paywalled at
  Academic Press/ScienceDirect with no open full text (UHasselt DSpace holds
  only the metadata record; confirmed again this cycle). The closest thing to a
  primary per-class ledger is Shan 2013 thesis Table 1.1 (held full text).
hypotheses: n=2 quadratic DRR program.
evidence-class: sourced for "no post-2020 Rousseau survey" (her publication
  lists held/searched through 2025) and "DRR 1994 paywalled" (UHasselt metadata
  only); the completeness of the negative claim is limited by search coverage.
falsifier: a held post-2020 authoritative ledger with per-graphic status and a
  closed-count (this would FILL the request, not falsify); a graphics-table in
  a paper this run has not seen.
holds-here: yes — this is the honest resolution of requests
  dumortier-roussarie-rousseau-9c4f / complete-current-ledger-cb3d: the gap
  cannot be closed from any single published source; the run's target
  inventory must be assembled by triangulating RSZ 2015 + RR 2015 + Shan 2013
  + the individual closure papers, which is exactly what research/drr-list.md
  does.
```

```claim
id: drr-shan-2013-table11-ledger
status: sourced
statement: Shan 2013 (PhD thesis, "Theory and applications of high codimension
  bifurcations", York Univ.) Table 1.1 is the only primary per-class ledger of
  the DRR program in this library. It counts 125 graphics in the standard
  family around the origin (not 121 — the grouping/counting discrepancy is NOT
  resolved). Per-class prose statements (robust): only (DF1a),(DF2a) degenerate
  graphics have finite cyclicity, the rest 11 degenerate graphics are OPEN;
  only (I₆a) elementary non-hyperbolic graphic remains OPEN; ≥20 nilpotent
  graphics closed by Zhu–Rousseau; the thesis itself proves 4 RH-graphic
  families through a triple nilpotent point (2 saddle-type Ji2,Ua(1), 2
  elliptic-type IJb,I1b) surrounding a focus/center. The OCR'd done/open column
  totals (85 done / 36 open / 4 my-work / total 125) do NOT sum cleanly
  (classes sum to ~123) and must not be quoted as exact — cite the class labels
  and prose, not the column arithmetic.
hypotheses: n=2 quadratic DRR program; "125 graphics in the standard family
  around the origin" (Shan's counting convention).
evidence-class: sourced (full thesis text held,
  research/sources/shan-phd-thesis-2013.full.md, lines ~527-630).
falsifier: a primary ledger giving different per-class open counts; resolution
  of the 121-vs-125 discrepancy from the DRR 1994 paper itself.
holds-here: yes as a partial, per-class inventory; NOT a complete graphic-by-
  graphic 121 list (that still requires the DRR 1994 paper).
```

```claim
id: library-on-disk-more-complete-than-status
status: sourced
statement: Several sources that research/LIBRARY-STATUS.md records as "could
  not be obtained" are in fact held in full on disk, and only appear missing
  because the document-resolver tool (read_document/index_document) cannot
  reach files past a range limit that list_workspace/grep_workspace do see.
  Confirmed-on-disk-but-resolver-blind this pass: roussarie-rousseau-2008-
  nilpotent-pp-center.full.md (RR 2008, H⁷₁/F⁷a₁/H¹¹₃/I⁶a₁ closed, cyclicity 2),
  rousseau-zhu-pp-graphics-nilpotent-elliptic.full.md,
  rousseau-roussarie-center-graphics-nilpotent.full.md,
  zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full.md,
  huzak-cyclicity-degenerate-df2a.full.md, zhu-2005-pp-graphics-finiteness-
  h16.full.md. This means rows previously `reported` (RR 2008 pp-type graphics;
  Dumortier–Rousseau 2009 DF1a/DF2a; Huzak 2018 DF₂ₐ) rest on primary full
  texts actually on disk and can be upgraded to `sourced` once read. Caveat:
  the resolver's blind range this pass means some of these could not be
  *read* now, only confirmed present and (for Zhu 2005) read.
hypotheses: none — a metadata/tooling fact about this workspace.
evidence-class: verified-this-pass (list_workspace + grep_workspace on the
  files; zhu-2005 read in lines 1-200 showing the genuine pp-graphics survey).
falsifier: a later pass reporting the files' content is not the named paper
  (see the llibre-zhang contamination precedent — verify content when read).
holds-here: yes.
```

```claim
id: fake-saddle-dmrt-2015-cyclicity
status: sourced
statement: De Maesschalck–Rebollo-Perdomo–Torregrosa (2015), "Cyclicity of a
  fake saddle inside the quadratic vector fields", JDE 258(2):588–620,
  doi:10.1016/j.jde.2014.09.024: near an unfolded fake saddle (impassable
  grain, a degree-2 degeneracy with a degenerate flow-box normal form
  {ẋ=Ax²+Bxy+O(3), ẏ=x²+y²+O(3)}, A≥0, B<1, A²<4(1−B)), small-amplitude limit
  cycles appear with cyclicity ≥ 2 when the normal form is quadratic, in
  configurations (2:0) and (1:1), via Hopf, Bogdanov–Takens, slow-fast/canard,
  homoclinic/heteroclinic mechanisms. For the symmetric-restricted family
  {ẋ=ax²+bxy+µ, ẏ=x²+y²−1} the paper proves at most two limit cycles in (1:1);
  limit cycles occur only in the parameter region R11. A precise upper bound
  for the general family is NOT established ("turned out to be too difficult").
  CRITICAL caveat: the paper states the fake saddle at X0 has NO contribution
  to the DRR degree-2 programme (homogeneous fields are avoided by rescalings),
  so fake-saddle cyclicity does not by itself close a DRR graphic row.
hypotheses: quadratic (degree-2) fake saddle; perturbative mechanisms.
evidence-class: sourced (FULL postprint now held,
  research/sources/demaesschalck-rebollo-torregrosa-fake-saddle-2015-postprint.full.md,
  UAB DDD open repository, https://ddd.uab.cat/pub/artpub/2015/gsduab_3787/
  joudifequ_a2015v258n2p588preprint.pdf).
falsifier: a counterexample giving >2 small-amplitude cycles near a quadratic
  fake saddle under the symmetric family (2), or a proof the general cyclicity
  is not 2; a source showing the fake saddle closes a specific DRR graphic row
  despite the authors' "no contribution" remark.
holds-here: yes as the primary source for the fake-saddle-cyclicity fact and
  the thread's transition-map machinery.
```

```claim
id: h16-alien-limit-cycles-abelian-insufficiency
status: sourced
statement: Luca–Dumortier–Caubergh–Roussarie (2009, "Detecting alien limit
  cycles near a Hamiltonian 2-saddle cycle", DCDS 25(4):1081–1108) construct a
  cubic Hamiltonian 2-saddle cycle (saddles at (−1,0),(1,0)) whose unfolding
  produces an ALIEN limit cycle — a limit cycle NOT controlled by any zero of
  the associated Abelian integral. It appears via the second derivative of the
  transition map along the saddle connections, not via an extra zero of the
  Abelian integral. Hence the reduction "number of limit cycles born from a
  Hamiltonian perturbation ⟺ number of zeros of the Abelian integral" FAILS
  for polycycles with saddle connections (alien cycles), though it holds for
  regular (nonsingular) ovals. Thesis 1: Corollary 13 gives explicit formulas
  for the first two derivatives of the transition map along a regular orbit;
  Theorem 15/Theorem 1 apply them to the 2-saddle connection.
hypotheses: n=3 (cubic Hamiltonian); 2-saddle cycle with unbroken connections
  in a codimension-4 Hamiltonian unfolding; Abelian integral on the
  nonsingular ovals.
evidence-class: sourced (full preprint held at
  https://users.ugent.be/~stluca/Preprints/A1_2009_LUCA_Alien_Limit_Cycles.pdf,
  research/sources/luca-dumortier-caubergh-roussarie-alien-limit-cycles-2009.full.md;
  peer-reviewed DCDS 2009).
falsifier: an argument that Abelian-integral zero counts alone bound ALL
  limit cycles in Hamiltonian perturbations of degree ≥ 3 (contradicted here);
  or a source showing the alien phenomenon disappears under stronger
  genericity (the authors prove it is generic in this family).
holds-here: yes — establishes the caveat that H(n) upper bounds (n ≥ 3) via
  Abelian integrals must carry the alien-cycle correction; does not affect the
  quadratic (n=2) DRR frame.
```

```claim
id: drr-dgr-2002-elementary-closures
status: sourced
statement: Dumortier–Guzmán–Rousseau (2002, "Finite cyclicity of elementary
  graphics surrounding a focus or center in quadratic systems", Qual. Theory
  Dyn. Syst. 3:123–154) prove explicit small cyclicity bounds for seven named
  elementary DRR graphics: (H³₄) and (H³₅) have cyclicity ≤ 2 (both for
  irrational hyperbolic-saddle hyperbolicity ratios — Thm 3.1 — and rational
  ratios — Thm 3.2); (H³₆) has cyclicity ≤ 2 if r(0) ≠ 1 and ≤ 3 if r(0) = 1
  (Thm 3.3); (I²₂₇) has cyclicity ≤ 2 (Thm 4.1); (I²₁₄a) and (I²₁₅a) have
  finite cyclicity (Thm 5.1, with Lemma 5.2: (R(x))^r is not an affine map and
  has a nonvanishing higher derivative); (I²₁₅b) has cyclicity ≤ 2 (Thm 5.3).
  The generic machinery (Thms 2.1/2.2) treats a hemicycle graphic with two
  opposite hyperbolic saddles P1,P2 (hyperbolicity ratios r1·r2 ≡ 1), one
  attracting and one repelling saddle-node on the equator, both central
  connections, using C^k integrable normal forms and transition maps. This
  "nearly finishes" the elementary-graphics part of the DRR program.
hypotheses: n=2 (quadratic); DRR elementary graphics surrounding a focus or
  center (notation of DRR 1994 [3]); hyperbolic saddles at infinity in the
  hemicycle cases.
evidence-class: sourced (full text held, open PDF
  http://www.dms.umontreal.ca/~rousseac/DGR.pdf,
  research/sources/dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md).
falsifier: a counterexample with >2 limit cycles near one of (H³₄),(H³₅),
  (I²₂₇),(I²₁₅b), or >3 near (H³₆) at r(0)=1, inside quadratic systems; or a
  source showing one of these graphics is NOT elementary (mislabel).
holds-here: yes — supplies a held primary source with explicit cyclicity
  bounds for these elementary DRR rows, letting later passes verify elementary
  closures rather than report them; does NOT touch the open nilpotent/degenerate
  rows ((H³₁₄),(I⁶b¹),(H¹³₃),(DI₂b), the 11 degenerate).
```

```claim
id: bautin-chart-membership-l8-l10-l12
status: checked
statement: For the Lu/RR five-coefficient chart family Q1 = Au²+Cuv+Dv²,
  Q2 = Euv+Fv² with the rotation recurrence
  R(c_k)+Q1·∂V_{k−1}/∂u+Q2·∂V_{k−1}/∂v = L_k·(u²+v²)^{k/2}, exact Gröbner over
  Q (lex, code/out/membership.captured.txt, verify_membership.py) gives:
  L8 ∉ ⟨L4,L6⟩ (16-monomial nonzero remainder — three generators genuinely
  needed); L6 ∉ ⟨L4⟩ (14-monomial remainder — first two independent); and
  L10 ∈ ⟨L4,L6,L8⟩ (remainder 0), L12 ∈ ⟨L4,L6,L8⟩ (remainder 0). The
  Bautin-trick closure step "the next focal value lies in the ideal of the
  earlier ones" HOLDS at L10 and L12 in this chart ring. Sanity guards pass:
  8·L4 = AC+CD+2DF−EF, 192·L6+P30 = 0 with P30 having 30 monomials.
  Each membership was decided three independent ways: reduction remainder == 0
  (with the correct sympy 1.11 extraction, see evidence-class), G.contains,
  and the exact identity poly == Σ q_i·b_i + rem; positive controls (generator
  in own ideal, explicit combination) all True.
  NOTE (correction history): a FIRST version of verify_membership.py read
  red[0] (the quotient list) instead of red[-1] (the remainder) of sympy 1.11's
  GroebnerBasis.reduce, which produced spurious nonzero "remainders" and
  wrongly reported L10,L12 ∉ ⟨L4,L6,L8⟩. That earlier conclusion is VOID; the
  membership.captured.txt with the 16/14-monomial nonmembership remainders and
  the two True memberships is the trustworthy run.
hypotheses: chart ring over Q with five coefficients; rotation recurrence as
  stated; lex order Gröbner; degrees 4..12 computed (degree 10+ focal values
  from the same recurrence).
search-frame: exact sympy over QQ, lex order, verify_membership.py and
  lyapunov_quadratic.py; degrees 4..12; membership of L6 in <L4>, L8 in <L4,L6>,
  L10,L12 in <L4,L6,L8>; sanity guards 8L4=AC+CD+2DF-EF and 192L6+P30=0 with
  P30 30-monomial. Published exhaustive regime: none needed (finite algebraic
  ideal-membership computation, exact over Q).
evidence-class: verified-computationally (exact sympy over QQ, lex Gröbner,
  capture in code/out/membership.captured.txt; each answer triple-checked as
  above and controls all True). Not yet kernel-checked Lean — needs cofactor
  certificates (next Lean task).
falsifier: a corrected Gröbner run showing L10 or L12 NOT in ⟨L4,L6,L8⟩, or a
  proof that a different chart/order changes the membership; a kernel-checked
  cofactor certificate for L8 ∈ ⟨L4,L6⟩ would refute the "third generator
  needed" reading.
holds-here: yes for the computed chart and order — but BEWARE: membership in a
  polynomial ideal can depend on the ring/order; the five-coefficient chart is
  the Lu H₁₄³ source-normalized reduction, not the full six-coefficient
  quadratic family. Whether the full-degree-2 Bautin ideal is generated by
  exactly L4,L6,L8 (Bautin's M(2)=3) is NOT settled by this run; these
  computations concern the chart ring and must not be quoted as M(2)=3
  evidence either way.
```

```claim
id: h16-pedregal-variational-claim-unrefereed
status: asserted-unverified
statement: Pedregal (arXiv:2103.07193, 2021, UNREFEREED preprint) claims a
  uniform upper bound on the Hilbert number depending only on degree:
  H(n) ≤ (5/2)n^4 − (23/2)n^3 + (43/2)n^2 − (37/2)n + 7 for n even, and
  H(n) ≤ (5/2)n^4 − (23/2)n^3 + (41/2)n^2 − (33/2)n + 6 for n odd;
  in particular H(2) = 4 — i.e. it claims to prove the open H16.2 and the
  standing conjecture H(2)=4. Method: variational — counts limit cycles as
  global minimizers of E0(x,y) = (1/2)∫₀¹(P y' − Q x')² dt and applies Morse
  inequalities to a perturbation Eε, bounding critical points via Bezout and
  Harnack on the divergence curve div = Px + Qy = 0 and its contact points.
  This is a CLAIMED resolution, NOT an accepted result.
hypotheses: none beyond degree n > 1 polynomial P,Q; the proof is presented as
  entirely variational, "no particular expertise in dynamical systems necessary".
evidence-class: asserted-by-source (held full ar5iv conversion,
  research/sources/pedregal-variational-h16-ar5iv.full.md; summary in
  research/summaries/pedregal-variational-h16-ar5iv.md). UNREFEREED preprint;
  no journal publication located; NOT established by this run.
falsifier: (a) any certified field of degree 2 with >4 limit cycles would
  refute H(2)=4; (b) showing the claimed bijection between isolated periodic
  orbits and counted sublevel-set components of E0 fails — the step where
  analyticity (Test 1) must enter and where the paper's argument appears to
  rely on algebraic/topological counts of the divergence curve rather than the
  analytic return map; (c) a published referee finding of a gap. The prior
  variant, Llibre–Pedregal arXiv:1411.6814, announced "...a mistake has been
  found in our way of counting limit cycles" — so the variational counting
  method has previously been found mistaken and this 2021 paper is the
  reworking, unverified.
holds-here: NO — treated as a suspect claim to test, not a result. The run's
  premise (H16.2 open, H(2)=4 conjectured not proved) is unchanged. Test 1
  (smooth test): the argument does not visibly use analyticity of the return
  map and is therefore prima facie refuted, exactly the shape of Dulac's error;
  Test 2: the quartic bound does not collide with n² log n, so the lower-bound
  test does not refute it — the suspicion rests on Test 1 and on the unrefereed
  status + prior announced mistake. Community still treats H16.2 as open (held
  Gasull 2024 survey); no peer acceptance of this preprint found.
```

## Separate: the information-geometry refutation is already recorded

```claim
id: h16-geometry-limitcycle-defn-refuted
status: refuted
statement: The "information-geometry" definition of limit cycle (count of
  singularities of |R| for a Fisher-information scalar curvature,
  arXiv 2024, H(n) = 2(n−1)(4(n−1)−2)) is NEITHER necessary NOR sufficient for
  the existence of limit cycles, so it cannot bound H(n). Refuted by
  Buzzi–Novaes (arXiv:2411.09594, held), with counterexamples; and the quadratic
  bound contradicts the n² log n lower bound.
hypotheses: n/a (definitional refutation).
evidence-class: refuted-by-source (Buzzi–Novaes 2024 held full text; also an
  authors' defense arXiv:2412.01916 exists disputing the refutation — the
  dispute is recorded, not resolved here).
falsifier: none standing — the definition is shown neither necessary nor
  sufficient.
holds-here: n/a — the approach is ruled out.
```

```claim
id: h16-ominimality-route-roussarie
status: sourced
statement: Roussarie's finite-cyclicity conjecture follows from an
  o-minimality statement for the language L_trans of parametric transition
  maps of all polynomial planar fields of a fixed degree: if the
  L_trans-structure on R is o-minimal, the uniform finiteness principle bounds
  the fibers A_mu (isolated points corresponding to limit cycles near a limit
  periodic set) uniformly, proving the finite-cyclicity conjecture and hence,
  per Roussarie's reduction (Prop. 1 of Ch. 2 of his 1998 book), H(degree)<∞.
  This o-minimality conjecture for the full L_trans is OPEN. The proved
  special case is Kaiser-Rolin-Speissegger (J. Reine Angew. Math. 636 (2009)
  1-45): for the class NRH_d of fields with ONLY non-resonant hyperbolic
  singularities, the sublanguage L_nrhyp is o-minimal, so Roussarie's
  conjecture holds for NRH_d (a "very small", non-generic class); the generic
  class H_d (all hyperbolic, including resonant) was work in progress.
hypotheses: o-minimality of the transition-map language; the class of fields
  restricted to NRH_d for the proved special case.
evidence-class: sourced by survey statement (Speissegger arXiv:1804.03585,
  Oberwolfach Snapshots; held full body in
  research/sources/speissegger-hilbert16-ominimality-body.full.md; the
  Kaiser-Rolin-Speissegger theorem it cites is refereed in Crelle).
falsifier: a field in NRH_d (only non-resonant hyperbolic singularities) with
  unbounded cyclicity in an unfolding — would contradict the proved special
  case; or a proof that L_trans is NOT o-minimal.
holds-here: yes, as the route is a genuine independent method for uniform
  finiteness. IMPORTANT for Test 1: the o-minimal transition-map theorem is a
  quasianalytic/asymptotic fact — analyticity of the return map is encoded,
  not discarded. This is the structural opposite of the Pedregal variational
  claim (h16-pedregal-variational-claim-unrefereed), which counts critical
  points of a functional via Bezout/Harnack and never touches the return map.
```

```claim
id: h16-pedregal-variational-claim-unrefereed
status: asserted-unverified
statement: Pedregal (arXiv:2103.07193, 2021, UNREFEREED preprint) claims a
  uniform upper bound on the Hilbert number depending only on degree:
  H(n) ≤ (5/2)n^4 − (23/2)n^3 + (43/2)n^2 − (37/2)n + 7 for n even, and
  H(n) ≤ (5/2)n^4 − (23/2)n^3 + (41/2)n^2 − (33/2)n + 6 for n odd;
  in particular H(2) = 4 — i.e. it claims to prove the open H16.2 and the
  standing conjecture H(2)=4. Method: variational — counts limit cycles as
  global minimizers of E0(x,y) = (1/2)∫₀¹(P y' − Q x')² dt and applies Morse
  inequalities to a perturbation Eε, bounding critical points via Bezout and
  Harnack on the divergence curve div = Px + Qy = 0 and its contact points.
  This is a CLAIMED resolution, NOT an accepted result.
hypotheses: none beyond degree n > 1 polynomial P,Q; the proof is presented as
  entirely variational, "no particular expertise in dynamical systems necessary".
evidence-class: asserted-by-source (held full ar5iv conversion,
  research/sources/pedregal-variational-h16-ar5iv.full.md; summary in
  research/summaries/pedregal-variational-h16-ar5iv.md). UNREFEREED preprint;
  no journal publication located; NOT established by this run.
falsifier: (a) any certified field of degree 2 with >4 limit cycles would
  refute H(2)=4; (b) showing the claimed bijection between isolated periodic
  orbits and counted sublevel-set components of E0 fails — the step where
  analyticity (Test 1) must enter and where the paper's argument appears to
  rely on algebraic/topological counts of the divergence curve rather than the
  analytic return map; (c) a published referee finding of a gap. The prior
  variant, Llibre–Pedregal arXiv:1411.6814, announced "...a mistake has been
  found in our way of counting limit cycles" — so the variational counting
  method has previously been found mistaken and this 2021 paper is the
  reworking, unverified.
holds-here: NO — treated as a suspect claim to test, not a result. The run's
  premise (H16.2 open, H(2)=4 conjectured not proved) is unchanged. Test 1
  (smooth test): the argument does not visibly use analyticity of the return
  map and is therefore prima facie refuted, exactly the shape of Dulac's error;
  Test 2: the quartic bound does not collide with n² log n, so the lower-bound
  test does not refute it — the suspicion rests on Test 1 and on the unrefereed
  status + prior announced mistake. Community still treats H16.2 as open (held
  Gasull 2024 survey); no peer acceptance of this preprint found.
```


