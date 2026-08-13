# Literature check of three proposed approaches (2026-08): Kodaira dimension, Hecke L-character product, X₀(32) Jacobian torsion

Author: research specialist. Report per candidate: what the reformulation is called,
the exact theorem it invokes and whether its hypotheses hold here, whether anyone has
applied it to this problem, and what it would buy. All three were `status: proposed`;
all three are now `status: refuted` with `killed-by` lines in their approach files.

---

## 1. `kodaira-dimension-general-type` → REFUTED

**What the reformulation is called.** The object is the *square-of-squares surface*:
the affine variety `V ⊂ A³_{(e,u,v)}` cut out by the nine "entry = square" equations
after eliminating the `sᵢⱼ`. This is NOT the "magic-square variety" `X ⊂ P⁸` of
Michaud–Rodgers (coordinates = entries, seven line-sum equalities only), which is the
only object in the library whose birational type anyone has touched at all
(`magic-variety-is-surface-no-lines`: surface, no lines, 256 singular points — and that
is a talk-level sketch). The square-of-squares surface's Kodaira dimension is genuinely
unpublished (my searches found nothing).

**The theorem.** Bombieri–Lang (conjecture, dimension-two Lang): a smooth projective
surface of general type over a number field has rational points **not Zariski-dense**,
i.e. `S(k)\Z(k)` finite for a proper closed `Z`. 

**Why the hypotheses/wanted conclusion do not hold here.**
- Unproved for surfaces over number fields; no effective/quantitative version exists.
- Even granted verbatim, "not Zariski-dense ⇒ finitely many points off a closed Z" is
  fully compatible with an MSS existing (a single point). It says nothing about whether
  a specific point exists and gives no bound to check. **The "reduces to a finite
  check" step is a non-sequitur.**
- It cannot separate Q from Q(√3,√133)/Q(√3), over which MSS provably exist
  (`extension-field-mss-exist`), so pushed strictly it over-proves, un-pushed it buys
  nothing.

**Applied to this problem?** Nobody has computed κ of the MSS surface. The closest
published precedent (rational-distances / Erdős–Ulam, Geometriae Dedicata 2025) is a
general-type surface whose non-density is *conjectured* and explicitly said to be beyond
current methods because it is simply connected — first-hand evidence that general type
does not currently buy arithmetic finiteness.
**The "Noguchi 1981 proved surfaces over function fields" attribution is inaccurate**:
Noguchi's work is on integral points on abelian/semi-abelian varieties; the naive
general-type statement over function fields is not a clean theorem.

**What it would buy.** Nothing for non-existence — whichever κ ∈ {−∞, 0, 1, 2},
the Q-rational-point question stays open. (κ = −∞ rational/unirational would even
predict density, the wrong direction.) Recorded so nobody re-proposes
"compute κ, then apply Bombieri–Lang" as an emptiness route. The κ-computation itself
remains a legitimate untouched Gröbner/adjunction problem that could be a structural
paper, but not an impossibility lever.

---

## 2. `hecke-character-product-l` → REFUTED

**What the reformulation is called.** Congruent-number curve L-function product:
the four AP differences give four congruent-number curves `E_d: y² = x³ − d²x`
(CM by Z[i], j=1728), Hecke L-functions `L(s,ψ_d)`; additive `u+v=u+v` relations are
hoped to give a multiplicative L-function product, and Gross–Zagier a cross-curve first
derivative/height relation.

**The theorem.** Gross–Zagier (1986): for a single E/Q of analytic rank 1, a Heegner
point has `ĥ = c·L'(E,1)/Ω`. **Per curve.** It never gives a relation among
`L'(E_u,1), L'(E_v,1), L'(E_{u+v},1)`.

**Why the mechanism fails here.** The required identity
`L(s,ψ_u)·L(s,ψ_v) = L(s,ψ_{u+v})×(corrections)` **does not exist**. Quadratic twists
of an elliptic L-function do not multiply into the twist L-function of a *sum* of twist
parameters. The only product object is the **Rankin–Selberg convolution** `L(E_u×E_v)`
(degree 4), which is not `L(E_{u+v})` at s=1. So additive relations among u,v,u+v,u−v
transfer to no multiplicative constraint; the candidate's own Step 1 ("derive the
identity") is the mathematically false step.

**Applied to this problem?** No publication establishes such a product identity (my
searches of moments/ratios/p-adic properties of quadratic-twist L-functions found only
Rankin–Selberg convolutions and individual-twist objects). The four-curve framing is
already closed ground: `root-number-parity-four-curves` (parity only) and
`simultaneous-congruent-numbers-2selmer` (subsumed by Bremner II's K3 NS) are refuted.
An MSS over Q(√3,√133) (`extension-field-mss-exist`) means any "impossible cross-curve
relation" would also fire over the extension, where the configuration exists — it cannot
be the Q-vs-extension separator.

**Verdict.** Refuted; the lever (product identity) is the false step.

---

## 3. `modular-jacobian-torsion-x0-32` → REFUTED

**What the reformulation is called.** Use the Mordell–Weil group of `J₀(32)(Q)`
(= `E₁: y²=x³−x`, genus 1, conductor 32, rank 0, torsion Z/2×Z/2 cusps) to trap the
MSS: rational points of the Robertson curve inject into this finite torsion group.

**The precise facts, and whether they hold here.** True facts: `E: y²=x³−c²x` is the
quadratic twist of `E₁: y²=x³−x` by the squarefree class of c; `J₀(32)(Q)=E₁(Q)` has
rank 0/torsion Z/2×Z/2 (Fermat/Euler: 1 not a congruent number; Feng–Xiong 2004,
"On elliptic curves y²=x³−n²x with rank zero", JNT).

**The failure.** A point of a *nontrivial quadratic twist* does not live on `E₁` and
does not map to `J₀(32)(Q)`. Twisting changes the Mordell–Weil group completely; there
is no map MSS-data → J₀(32)(Q), so "every rational class is torsion ⇒ cuspidal" never
engages. **Self-inconsistency in the write-up:** it calls `E: y²=x(x²−e⁴)` the
"e-twist of X₀(32)", but `x³−e⁴x` with e⁴ a square-class 1 is the *trivial twist*,
Q-isomorphic to `y²=x³−x`. The real Robertson curve is `E: y²=x³−c²x` with c = the
**anti-diagonal** half-difference (`robertson-elliptic-reduction`), c = 138600 for the
Bremner witness, twist class 154 (nontrivial), and **this run computed rank 2** — a
positive-rank twist carrying the actual configuration. So "rank 0, only torsion" is
false for every genuine MSS curve. The primitive degenerate case it does trap is not
the curve an MSS lives on; and that case's torsion (x∈{0,±1}) is consistent, no AP
forced (no contradiction even there).

**Applied / closed ground.** Nobody has applied it; it stands on the same X₀(4)/modular
isogeny ground as the already-refuted `freys-curve-four-q-isogenies`
(`freys-4-isogeny-misidentifies-doubling`). My search of twist/Selmer literature
confirms twist ranks are governed by the twist class, not base rank (positive-proportion
rank-0 twist results leave positive-rank twists abundant).

**Verdict.** Refuted; the torsion trap applies only to the trivial twist, not the
curves an MSS's points live on.

---

## Sources consulted (research papers / web)

- Bombieri–Lang / general-type non-density: rational-distances surface of general type,
  Geometriae Dedicata (2025), https://link.springer.com/article/10.1007/s10711-025-01019-0
  ("we lack methods to prove this" for a natural simply-connected general-type surface).
- Gross–Zagier 1986 (Ann. Math. 124); Coates–Wiles 1977 (Invent. Math. 39) — per-curve,
  no cross-curve relation.
- Rankin–Selberg / quadratic-twist L-function literature (moments, ratios, p-adic
  properties): no additivity-to-multiplicativity product identity exists.
- Feng–Xiong, "On elliptic curves y²=x³−n²x with rank zero", J. Number Theory (2004),
  https://www.sciencedirect.com/science/article/pii/S0022314X04000113 — rank-0 congruent
  number curves.
- Library's own: `magic-variety-is-surface-no-lines` (michaud-rodgers-warwick-talk-2019);
  `robertson-elliptic-reduction`; `extension-field-mss-exist`; `freys-4-isogeny-misidentifies-doubling`;
  witness rank-2 computation (`tool-builder` run, `research/sources/...`).

## Sources rejected, and why

- The general general-type surface papers (Severi conjecture, Kulikov surfaces, canonical
  surfaces) are classification theorems, not arithmetic density statements; irrelevant to
  whether Bombieri–Lang buys a finite check.
- The Mordell's-equation / conductor-10⁶ rank-data hits are descriptive, not about the
  twist-injection question; the Feng–Xiong paper was the only one directly on point for
  the rank-0 congruent-number claim.
- The moments/ratios/nonvanishing L-function papers were all about individual twists or
  Rankin–Selberg convolutions; none claimed the product identity the candidate needs,
  which is consistent with it being false.

## Claim blocks

```claim
id: kodaira-bombieri-lang-not-an-emptiness-route
statement: The Bombieri–Lang conjecture (even granted) says only that a general-type
  surface over a number field has rational points not Zariski-dense (S(Q)\Z(Q) finite
  for a proper closed Z); it gives no exceptional set, no height bound, and no decision
  on whether a specific point exists, and it cannot separate Q from Q(√3,√133)/Q(√3)
  over which MSS provably exist. Hence computing κ of the MSS square-of-squares surface
  cannot reduce non-existence to a finite check.
hypotheses: Bombieri–Lang conjecture (unproved for surfaces over number fields) would be
  granted; κ(S)=2 would need to hold.
holds-here: n/a (approach refuted; the wanted conclusion does not follow even from its
  hypotheses)
status: refuted
bearing: closes kodaira-dimension-general-type as an emptiness route; the κ-computation
  itself remains an unpublished structural computation but is not an impossibility lever.
anchor: research/approaches/kodaira-dimension-general-type.md
```

```claim
id: hecke-twist-l-product-identity-does-not-exist
statement: For quadratic twists of a CM elliptic curve there is NO identity
  L(s,ψ_u)L(s,ψ_v) = L(s,ψ_{u+v})×(local corrections): products of twist L-functions do
  not multiply into the twist L-function of a sum; the only product object is the
  Rankin–Selberg convolution L(E_u×E_v), which is not L(E_{u+v}) at s=1. Gross–Zagier is
  per-curve (analytic rank 1) and gives no cross-curve height relation. Hence the
  Hecke-character L-function product approach to the four AP differences is empty.
hypotheses: E_d: y²=x³−d²x CM curves; additive relation u+v=(u+v).
holds-here: n/a (the mechanism's identity is the false step)
status: refuted
bearing: closes hecke-character-product-l; it is a re-skin of the refuted four-curve
  root-number and 2-Selmer approaches and an MSS over Q(√3,√133) would over-prove it.
anchor: research/approaches/hecke-character-product-l.md
```

```claim
id: x0-32-torsion-traps-only-trivial-twist
statement: E: y²=x³−e⁴x is the trivial twist (Q-isomorphic to y²=x³−x, rank 0), not the
  Robertson curve; the Robertson curve is y²=x³−c²x with c the anti-diagonal half-
  difference (c=138600, twist class 154 nontrivial, this run computed rank 2). Rational
  points of a nontrivial quadratic twist do not inject into J₀(32)(Q)=E₁(Q), so the
  "rank 0, only torsion, hence cuspidal" trap never engages for a genuine MSS curve.
hypotheses: Robertson reduction (c = anti-diagonal half-difference, not the centre).
holds-here: n/a (approach refuted; the map MSS→J₀(32)(Q) does not exist)
status: refuted
bearing: closes modular-jacobian-torsion-x0-32; re-skins freys-curve-four-q-isogenies.
anchor: research/approaches/modular-jacobian-torsion-x0-32.md
```
