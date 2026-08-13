# Literature check: integral Brauer–Manin, Freys 4-isogenies, Richardson/PVS

Date: this round. Author: research specialist.

Three brand-new candidates (`status: proposed`, never checked) were taken to the
literature. All three are **refuted**: each rests on a real technique but the specific
identification with the MSS fails on exact structure. None is a search reformulation
anyone should re-propose. Refutation is on evidence (structure), not on absence: the
techniques themselves are genuine and published, but the mapping to MSS is wrong or
unestablished.

## 1. integral-brauer-manin-nine-square → refuted

- The integral Brauer–Manin obstruction is real: Colliot-Thélène–Xu, "Brauer–Manin
  obstruction for integral points of homogeneous spaces and representation by integral
  quadratic forms", Compos. Math. 145 (2009) 309–363; Harpaz–Skorobogatov on Brauer
  groups of affine varieties; Browning–Matthiesen, "Norm forms for arbitrary number
  fields as products of linear polynomials", Ann. Sci. ENS 50 (2017) (BM the only
  obstruction for normic hypersurfaces on smooth projective models); Schindler–Skorobogatov
  (J. LMS 89 (2014)); Harpaz on the unramified Brauer group of norm-one tori.
- **But** the nine-square affine scheme V/Z (7 line-sum + 8 norm equations, singular,
  non-proper) lies outside every class where the integral BM group is computable. The
  magic variety X⊂P⁸ is a surface with 256 singular points; adjoining square-conditions
  keeps it singular. No source computes Br(V)/Br(Q) or an integral BM obstruction for
  the MSS variety.
- The separating premise (integral point over Z[√3,√133] but not Z) is itself the whole
  content and is unproved; the candidate offers no route to exhibit a Brauer class.
- It also cannot by itself beat the run's hinge: the rational MSS exist over extension
  fields, and the integral BM obstruction only distinguishes Z from O_K if one can
  compute it (it cannot, for this V).

## 2. freys-curve-four-q-isogenies → refuted

- E_n: y² = x³ − n²x has exactly three rational 2-torsion points; its isogeny class has
  four members connected by **2-isogenies** (LMFDB congruent-number-curve knowl),
  so there is no distinguished 4-isogeny tied to a point of 2E(Q).
- "P ∈ 2E(Q)" = "P is a double", which is the condition {X, X±c} are squares;
  it is **not** a 4-isogeny kernel. 4-isogenies are curve-level composites of 2-isogenies,
  independent of which doubled point is chosen.
- Bremner/Robertson: MSS ⇔ **three** points of 2E(Q) on the ONE curve
  E: y² = x(x² − c²) with x-coordinates in arithmetic progression (Bremner, On squares
  of squares, Acta Arith. 88 (1999) 289–297; Robertson 1996). Three points on one
  curve — the four differences do not become four independent isogeny choices, so the
  X₀(4)⁴ moduli curve does not match the problem.

## 3. richardson-orbits-weyl-group → refuted

- (SL3×SL3, M3) with the two-sided action **is** a PVS (relative invariant det; the
  open dense orbit = invertible matrices). Sato–Shintani; Sato–Kimura classification
  (Nagoya Math. J. 65 (1977) 1–155). So that premise is correct.
- **But** the MSS conditions are not expressed by PVS relative invariants, and the magic
  subspace is a centraliser of a **semisimple** element J₃ (eigenvalues 3,0,0),
  hence a reductive centraliser — not a Richardson/nilpotent orbit. Richardson orbits
  parametrise nilpotent conjugacy classes; the magic subspace is a linear subspace.
- The period-map → ball quotient → André–Oort → Bring curve → Q(√5) chain is
  ungrounded and would overprove (cannot separate Q from Q(√3,√133), over which MSS
  exist). André–Oort for curves in Hilbert modular varieties is real (Yafaev; effective
  version Binyamini–Masser) but unrelated to the MSS.

```claim
id: integral-bm-nine-square-not-applicable
statement: The integral Brauer–Manin obstruction is a genuine technique (CT-Xu 2009,
  Harpaz-Skorobogatov, Browning-Matthiesen 2017) but its hypotheses (smooth
  homogeneous space, normic hypersurface, or norm-one torus torsor) fail for the
  nine-square affine scheme V/Z (7 line-sums + 8 norm equations, singular,
  non-proper); no literature computes Br(V)/Br(Q) or an integral BM obstruction for
  the MSS variety, and the premise of an integral point over Z[sqrt(3),sqrt(133)]
  but not over Z is unproved.
hypotheses: (for the theorem to apply) V smooth/geometric with computable Brauer group.
holds-here: no — V is singular, non-proper, outside all computable classes.
status: refuted
bearing: closes integral-brauer-manin-nine-square; an integral-BM proof would need a
  smooth projective model of the MSS variety with computable Br, which no source
  provides.
anchor: research/approaches/integral-brauer-manin-nine-square.md
```

```claim
id: freys-4-isogeny-misidentifies-doubling
statement: For E_n: y^2 = x^3 - n^2 x, 'P in 2E(Q)' means P is a double (equivalently
  {X, X+-c} squares), not a 4-isogeny kernel; the isogeny class has four members
  connected by 2-isogenies (LMFDB), with no distinguished 4-isogeny tied to a point of
  2E(Q); and the Robertson/Bremner reduction is three points of 2E(Q) on the single
  curve E: y^2 = x(x^2 - c^2) with x-coordinates in AP, not four linked 4-isogenies.
hypotheses: none special — standard congruent-number curve structure.
holds-here: yes (this is exactly the MSS structure).
status: refuted
bearing: closes freys-curve-four-q-isogenies; the correct object is the Robertson
  reduction (three points in 2E(Q) on one curve), not a moduli curve on X0(4)^4.
anchor: research/approaches/freys-curve-four-q-isogenies.md
```

```claim
id: richardson-pvs-valid-but-mss-not-pvs-invariant
statement: (SL3 x SL3, M3) with the two-sided action is a prehomogeneous vector space
  (relative invariant det, open orbit = invertible matrices; Sato-Kimura), but the
  nine-square condition is not a PVS relative invariant, and the magic subspace
  (centraliser of semisimple J3) is a reductive centraliser, not a Richardson /
  nilpotent orbit; the period-map/Andre-Oort/Bring-curve chain is ungrounded and would
  overprove.
hypotheses: none special.
holds-here: the PVS fact yes; the application to MSS no.
status: refuted
bearing: closes richardson-orbits-weyl-group.
anchor: research/approaches/richardson-orbits-weyl-group.md
```

## Sources used

- LMFDB "Congruent number curves" knowl, https://www.lmfdb.org/knowledge/show/ec.congruent_number_curve (E_n isogeny class of 4 via 2-isogenies; torsion; 2E(Q)).
- Bremner, "On squares of squares", Acta Arith. 88 (1999) 289–297, matwbn.icm.edu.pl/ksiazki/aa/aa88/aa8837.pdf (Robertson reduction: three points in 2E(Q) with x-coords in AP).
- Colliot-Thélène–Xu, Compos. Math. 145 (2009) 309–363.
- Browning–Matthiesen, Ann. Sci. ENS 50 (2017) (normic hypersurfaces).
- Sato–Kimura, "A classification of irreducible prehomogeneous vector spaces and their relative invariants", Nagoya Math. J. 65 (1977) 1–155.
- Binyamini–Masser, "Effective André–Oort for non-compact curves in Hilbert modular varieties" (comptes-rendus 2021 / arXiv:2101.06412) — Andre-Oort is real but unrelated to MSS.

## Rejected sources / why

- arXiv:2510.08286 ("Algebraic proof of nonexistence") and vixra 2503.0131, arXiv:1506.06621-companion nonexistence "proofs": recreational/nonexpert number-theoretic contradiction arguments for the open conjecture; not peer-reviewed, attack the full conjecture directly, and would, if valid, contradict this run's extension-field-mss-exist hinge. Do not ground anything on them. (ferreira-proof-refuted already in this run.)
- The Warwick fourth-year-project (Michaud-Rodgers) is legitimately useful background (magic variety = surface, 256 singular points, lines) but does not touch any of the three candidates.
- The Rome–Yamagishi existence paper (circle method, n≥4) reconfirms 3×3 is the hard case; unrelated to the three candidates.
