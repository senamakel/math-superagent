# Harrison, Mudgal & Schmidt, "Uniform sum-product phenomenon for algebraic groups and Bremner's conjecture", arXiv:2603.06483 (2026) — full-text note

[[harrison-mudgal-schmidt-sum-product-bremner-2026]]
This is the full-text summary. The sibling file `research/summaries/harrison-mudgal-schmidt-sum-product-bremner-2026.html.md` carries the claim block `hms-2026-bremner-effective-constant`; complete text at `research/sources/harrison-mudgal-schmidt-sum-product-bremner-2026.html.full.md` (132 KB HTML, arXiv:2603.06483v1, 30 pp; the smaller `...-2026.full.md` is a PDF conversion of the same paper).

## What it establishes

**Theorem 1.1 — Bremner's conjecture with an effectively computable constant.**
There is an effectively computable C ≥ 1, independent of the curve and its
coefficients (a,b), such that: for E/Q in Weierstrass form y²=x³+ax+b of rank r,
with X = {x(P): P∈E(Q)}, Y = {y(P): P∈E(Q)}, and A any arithmetic progression,
geometric progression, or set of consecutive squares {u²,(u+d)²,…,(u+ld)²}, if
A ⊆ X or A ⊆ Y then |A| ≤ C^(1+r). The general form is Corollary 2.2: a proper
generalised arithmetic progression P of rank k contained in 𝒞(Γ) (𝒞 a
correspondence of degree ≤ d between an elliptic curve or Gm and a 1-dimensional
group) satisfies |P| ≤ D(d)^(1+r), independent of k.

**Method.** Additive combinatorics (weak PFR over Z, Gowers–Green–Manners–Tao)
+ Diophantine geometry (uniform Mordell–Lang, David–Philippon; S-unit bounds,
Evertse–Schlickewei–Schmidt).

## What this means for the MSS run

- It upgrades the constant in the adopted `uniform-height-bound-elliptic-ap`
  approach from ineffective (GFP 2026 Theorem 1.8) to **effectively computable in
  principle**, but the paper gives no explicit value: C is built from
  David–Philippon and PFR constants and is almost certainly astronomically large.
  The non-existence threshold C^(1+r) < 3 fails for any plausible rank, so the
  approach remains **blocked by constant size**, not by definitions.
- Corollary 2.2's GAP bound applies to the four-centre-AP configuration: even a
  generalised AP meeting the MSS conditions would be bounded — this is the
  strongest uniform statement currently known that touches the additive
  u,v,u+v,u−v structure, but again with an uncomputed constant.

```claim
id: hms-2026-bremner-effective-constant
statement: There is an effectively computable C ≥ 1 such that for any E/Q of rank r,
  any arithmetic or geometric progression, or set of consecutive squares, contained in
  the x- or y-coordinates of E(Q), has length ≤ C^(1+r). (Theorem 1.1; Corollary 2.2
  extends to generalised APs of arbitrary rank k, bound D(d)^(1+r) independent of k.)
hypotheses: E/Q Weierstrass form; pattern in X or Y coordinates
holds-here: yes (makes GFP's ineffective constant effective-in-principle; exact
  mapping of the MSS four-centre-AP to the three pattern classes is still open)
status: sourced (Harrison, Mudgal, Schmidt, arXiv:2603.06483, Theorem 1.1 and
  Corollary 2.2, read in full text)
bearing: reduces `uniform-height-bound-elliptic-ap`'s obstruction from ineffective
  to effective-but-uncomputed; the constant is built from David–Philippon + PFR and
  is almost certainly ≫ 3, so C^(1+r) < 3 is not decidable from the paper
anchor: research/sources/harrison-mudgal-schmidt-sum-product-bremner-2026.html.full.md
```

## Does this source help?

**Yes, but only to move one blocker.** It is the first source with an
effectively-computable constant for Bremner's conjecture (Theorem 1.1), and its
Corollary 2.2 is the only uniform statement whose scope includes generalised APs
(the shape of the four-AP-additive constraint). It does not close the approach:
no explicit C appears, and the effectiveness is in-principle only. It confirms,
does not contradict, the GFP/Robertson reduction.

## Source

Harrison, Joseph; Mudgal, Akshat; Schmidt, Harry. "Uniform sum-product phenomenon
for algebraic groups and Bremner's conjecture." arXiv:2603.06483v1 [math.NT],
6 Mar 2026. https://arxiv.org/abs/2603.06483
