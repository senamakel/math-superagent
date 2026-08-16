# Grounding the three formerly-unchecked candidate approaches

The inventor produced no candidate list this round, so the research
grounding pass went to the three approaches the run itself flagged as
"Not yet taken to the literature": `endpoint-product-dirichlet`,
`excess-degree-spectrum-dichotomy`, `mobius-meet-factorization`.
Each was taken to the literature; verdicts below are grounded on
sources, not on absence, and each file under `research/approaches/` is
updated.

## 1. endpoint-product-dirichlet — REFUTED

**What it is called.** Using complete multiplicativity of the quadratic
character χ₄ to collapse each second-moment fold term to a single
character value at the product of run-endpoint primes, then attacking the
resulting sum with Dirichlet-series / L-function machinery (Dirichlet
L-functions, Perron inversion, Selberg–Delange, Hardy–Littlewood singular
series).

**The precise theorem it would rest on, and whether it holds.** The named
value-domain engine is
- **Dummit–Granville–Kisilevsky, *Big biases amongst products of two
  primes*, J. London Math. Soc. 93 (2016) 424–446, arXiv:1105.5022,
  Theorem 1.1**: for a quadratic character χ of conductor d, the count of
  `pq ≤ x` with `χ(p)=χ(q)=η` is `(1/4)(1 + η Lχ/log log x)` of the
  total, `Lχ = Σ_p χ(p)/p`. For χ₄, `L(1,χ₄) ≈ −0.334`.
  This is a correct, hard, citable theorem about a **value-ordered**
  prime product.

**Hypotheses and whether they hold here.** **No.** The theorem counts
products `pq ≤ x` ordered by *size*. The fold term `χ₄(P_{d,d'})` is
indexed by the **prime-index separation** `b−a = 2^g` of the run-endpoint
primes (`q_a, q_b` at index separation a power of two, claim
`no-standalone-switch-sign-in-squared-excess`). Size-ordering and
index-ordering of primes are different, and the index-domain object is
precisely the one the L-function framework cannot reach:
- **ABGS** (`abgs-p1-wide-open`): consecutive-pair residue frequencies
  are L-function-inaccessible (§9).
- **Lemke Oliver–Soundararajan** (arXiv:1709.06168): the K≥2 secondary
  bias term is a Dedekind-sum / φ-error object, not a clean L-function.

**Was it applied to this problem?** The exact product-of-two-primes
character-sum bias is applied to semiprime counting (value domain). No
source applies it to index-separated prime correlations or to a
Pascal-mod-2 fold weight.

**What it would buy, and why it does not.** The contraction
`χ(ab)=χ(a)χ(b)` is a correct bookkeeping identity, but it moves the
difficulty only from "product of two characters at two indices" to "a
character at a value-ordered prime product" — it does **not** move the
index separation into the value ordering where L-functions act. The
route's own falsifier (b) fires: every separation-`g` stratum reduces to
the same index-domain object as the adjacent-pair switch density, whose
machinery is not L-functions. Indicates priority 5 (SUPPLY ⟺ switch
density), not priority 4.

## 2. excess-degree-spectrum-dichotomy — GROUNDED (as a pricing tool)

**What it is called.** The excess functional `S(n)` is a sum of even-degree
multilinear monomials in the switch signs; the degree-1 (switch-density)
mode is exactly zero, giving a dichotomy between "even-order correlations
equivalent to switch density" (⟹ SUPPLY ⟺ switch density) and "strictly
weaker" (⟹ a weaker input).

**The precise machinery and whether it holds.** The Walsh/degree
filtration of multilinear polynomials on the hypercube, the character-basis
orthogonality, and the degree-levels-as-noise-operator-eigenspaces are
textbook (O'Donnell, *Analysis of Boolean Functions*, CUP 2014 — already
held). Low-degree spectral-mass bounds: Defant–Mastyło–Perez, *Math. Ann.*
2018 (arXiv:1806.00310). The slice/Johnson refinement: Keller–Klein,
*Israel J. Math.* 2020 (arXiv:1904.03077); Filmus, 2016
(arXiv:1505.05359). **Holds here:** yes — the evenness and orthogonality
facts are proved in-workspace as `fold-cell-degree-is-2^popcount` and
`no-standalone-switch-sign-in-squared-excess`; the degree-2/4 count uses
`downset-row-intersection-meet-formula`.

**Applied to this problem?** No source applies Walsh degree-filtration to
a sliding-window fold weight. The deterministic-pricing reading is
in-workspace.

**What it buys.** As a *pricing tool* it is grounded and exact: it reframes
the parity barrier precisely and decides the equivalence question. As a
*bound on the real prime input* it reduces to the same open index-domain
object as every other route. So: grounded as a pricing/dichotomy tool, not
a proof of a weaker input.

## 3. mobius-meet-factorization — GROUNDED (machinery); load-bearing step OPEN

**What it is called.** Rota Möbius inversion on the Boolean lattice (of
which subcube inclusion–exclusion is the special case) and the
independence polynomial of the disjointness graph, applied to factor the
second-moment monomial over the meet-semilattice of the fold's windows.

**The precise machinery and whether it holds.** Boolean-lattice Möbius
inversion: Rota, *Z. Wahrscheinlichkeitstheorie* 2 (1964) 340–368
(link.springer.com/article/10.1007/BF00531932); Baker, *Bull. AMS* 2017
(arXiv:1711.08900) states it with the meet-as-intersection structure.
Independence polynomial: Dohmen–Poenitz–Tittmann, DMTCS 2003
(arXiv:math/0305362). **Holds here:** the meet-semilattice structure
`M_d ∩ M_{d'} = M_{d∧d'}` is proved in-workspace (`downset-row-
intersection-meet-formula`).

**Applied to this problem?** No source found applies Möbius
inversion/independence-polynomial machinery to a Pascal-mod-2 fold weight,
nor factorizes the symmetric-difference monomial into per-bit factors. The
load-bearing step — "`M_d ∖ M_j` is a disjoint union of subcubes whose
character product is per-bit-multiplicative" — is neither sourced nor
refuted: it is a pure-F2 fact the first-step is designed to prove or kill.

**What it buys.** If the factorization holds, it genuinely reduces the
coupled double sum to an independence-polynomial evaluation — a structural
step, not a relabeling. Machinery grounded; the per-bit factorization is
the open checkable conjecture. Marked `grounded` with the caveat made
explicit so no later reader mistakes the grounded machinery for a grounded
conclusion.

## Where this leaves the pass

None of the three delivers a strictly-weaker arithmetic input on its own.
Two are structural/pricing tools grounded in standard machinery with their
open step named exactly (excess-degree-spectrum-dichotomy, mobius-meet-
factorization); one (endpoint-product-dirichlet) is refuted on the
value-vs-index split and its falsifier (b) fires. This is consistent with
CONCLUSION-PASS3: the arithmetic demand reduces to a sublinear switch
count, and the remaining gap is the same genericity gap — "typical is not
this string."
