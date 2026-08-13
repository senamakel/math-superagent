```approach
id: kodaira-dimension-general-type
idea: Compute the Kodaira dimension of the full nine-square surface (the
  compactification of the affine variety parametrising all 3×3 magic
  squares of squares).  If the surface is of general type (κ = 2), then
  by the Bombieri–Lang conjecture — proved for surfaces over function
  fields and strongly supported for number fields — the rational points
  are not Zariski dense.  Combined with the known computational lower
  bounds, finiteness of rational points on the MSS surface reduces the
  problem to a finite check.
mechanism: The nine entries are linear forms Lᵢⱼ(c, u, v) in the
  parametrisation.  Substituting c = e² and requiring each entry = sᵢⱼ²
  gives 8 equations in (e, u, v, s₁, …, s₈).  Eliminate the sᵢ to get an
  affine surface V ⊂ A³_{(e,u,v)}, compactify to a projective surface S,
  and compute ω_S via the adjunction formula.  If ω_S is big (K_S·H > 0,
  h⁰(nK_S) ∼ n²), then κ(S) = 2.  The adjunction/formula computation is
  a finite exact Gröbner-basis problem nobody has run on the MSS surface.
status: refuted
killed-by: Bombieri–Lang (even granted, and it is UNPROVED for surfaces over
  number fields) says only "rational points are NOT ZARISKI-DENSE" — i.e.
  there is a proper closed subset Z with S(Q)\Z(Q) FINITE.  It says NOTHING
  effective: no explicit Z, no height bound, no bound on the finite residue
  set, and "finitely many points" is fully compatible with zero, one, or an
  actual MSS.  It does not reduce the problem to a finite check.  And it
  cannot separate Q from Q(√3,√133)/Q(√3), over which MSS provably exist
  (this run's extension-field-mss-exist), so the κ=2/Bombieri–Lang route
  proves too much if pushed and proves nothing usable if not pushed.
first-step: (moot.)  The Kodaira-dimension computation of the full
  nine-square surface is NOT in the literature — the only source touching
  the birational type of the full magic-square variety is a Warwick talk
  (Michaud–Rodgers 2019) that computes dimension 2 (surface, no lines,
  256 singular points) and explicitly disclaims proof.  Whether V is
  rational/unirational/K3/general-type genuinely has not been published.
  But even a clean κ=2 result would buy nothing for non-existence, because
  the Bombieri–Lang conclusion is an unquantified finiteness statement.
precedent: Bombieri–Lang conjecture (rational points of a variety of general
  type over a number field are not Zariski-dense) — UNPROVED for surfaces
  over number fields; the rational-distances paper (Geometriae Dedicata,
  arXiv/Springer 2025; the r≥4 surface-of-general-type case of the
  Erdős–Ulam problem) states the non-density consequence is conditional and
  "we lack methods to prove this" even for a natural simply-connected
  general-type surface — direct evidence that general-type ⇒ finite-check
  is not in reach.  The candidate cites "Noguchi 1981 solves surfaces over
  function fields": that is a mis-statement.  Noguchi's theorems concern
  integral points on abelian/semi-abelian varieties; the Lang conjecture for
  surfaces over function fields is NOT a clean theorem (isotriviality and
  Campana-program subtleties block the naive statement; the naive version is
  false in general).  On the object itself: michaud-rodgers-warwick-talk-2019
  asserts the full magic-square variety is a surface, no lines, 256 singular
  points (claim magic-variety-is-surface-no-lines, status asserted, talk-level
  only) — that is the closest anyone comes to the birational type of the MSS
  surface; no written source computes its Kodaira dimension.
speculation: (superseded.)  The κ=2 reading was the only route that could
  "reduce to a finite check," and it breaks at the exact point where
  Bombieri–Lang stops being effective.  A genuinely novel computation of
  κ(V) is open and could still be a structural result worth one paper, but it
  cannot be an impossibility route: κ=0/1/2 all leave the rational-point
  question open, and κ=2 does not quantify the finite exception set.
```

# Literature check: Kodaira dimension / general type (REFUTED)

Author: research specialist. Date: this round.

## What the reformulation is actually called

The object is the *auxiliary/enriched magic-square surface*: the affine variety
`V ⊂ A³_{(e,u,v)}` cut out by the nine "entry = square" equations after eliminating
the `sᵢⱼ`. (Note: do not conflate with the *magic-square variety* `X ⊂ P⁸` of
Michaud–Rodgers, whose coordinates are the entries and which carries only the seven
line-sum equalities — that is a surface with no lines / 256 singular points, but it is
NOT the square-of-squares surface; the square-of-squares surface has the eight extra
"= square" equations and is a different object that nobody has studied birationally.)

The proposed tool is the **Bombieri–Lang conjecture** (Lang's conjecture in dimension
two): a smooth projective surface of general type over a number field has rational
points that are not Zariski-dense.

## Precise statement and whether its hypotheses hold here

**Theorem (hypothetical).** If S is a smooth projective surface of general type over a
number field k, then S(k) is not Zariski-dense: there is a proper closed subset Z ⊂ S
such that S(k) \ Z(k) is finite.

- This is a **conjecture, not a theorem**, for surfaces over number fields. It is open.
  It is not "strongly supported" in any sense that helps: no effective version, no
  exceptional-set control, no quantative finiteness is known or conjecturally available
  from it.
- Even granting it verbatim, `S(Q) \ Z(Q)` finite is fully compatible with an MSS
  existing: an MSS is a single Q-point. Bombieri–Lang would say "at most finitely many
  Q-points off some closed Z" — it says nothing about whether a given one exists, and
  gives no bound to check. **The "reduces to a finite check" step is a non-sequitur.**

## Is there any published analogue/applied to this problem?

No. The only source this library has that touches the birational type of the MSS
variety is `michaud-rodgers-warwick-talk-2019` (claim `magic-variety-is-surface-no-lines`),
and it is a talk-level sketch (dimension 2, no lines, 256 singular points) with the
square-of-squares surface itself unstudied. My open-web/literature search found no
paper computing κ of the MSS surface. The candidate's own premise — "nobody has
computed the Kodaira dimension" — is true, but the premise that a κ=2 answer would
settle anything is false.

The closest genuinely-published precedent is the rational-distances / Erdős–Ulam
literature (Geometriae Dedicata 2025, arXiv): for r ≥ 4 fixed rational points the
rational-distance problem is a surface of general type whose non-density is *conjectured*
and explicitly said to be beyond current methods because it is simply connected. This
is a first-hand demonstration that "surface of general type" does not currently buy an
arithmetic finiteness statement about a specific Diophantine set.

The candidate also attributes "Noguchi 1981, proved for surfaces over function fields".
This is inaccurate: the Lang-type statement over function fields is not a clean theorem
attributable to Noguchi 1981 (which is about integral points on abelian varieties), and
the naive general-type statement over function fields has genuine isotriviality
obstructions. Even in the best case it would be a statement over C(t), irrelevant to Q.

## What it would buy

Nothing for non-existence. κ = 2 (+ unproved Bombieri–Lang) ⇒ "not Zariski dense" ⇒ a
finite set of possibly-special points, with no way to decide if an MSS is among them.
κ = 0 (K3), κ = 1 (elliptic fibration), κ = −∞ (rational/unirational) all leave the
Q-rational-point question open (and rational/unirational would in fact predict rational
points are DENSE, the opposite direction). So whichever value κ takes, the route cannot
close non-existence. And it has no mechanism to separate Q from Q(√3,√133), where MSS
provably exist — a Q-arithmetic Bombieri–Lang statement cannot distinguish a point
defined over an extension from one over Q.

## Verdict

**Refuted as a route to non-existence.** The Kodaira dimension computation itself
remains a legitimately-untouched finite Gröbner/adjunction problem that could be a
structural paper (it is NOT in the library, NOT on the web search), but the proposed
leverage — Bombieri–Lang ⇒ finite check — fails as a matter of the meaning of the
theorem. Recorded as a known dead end so nobody re-proposes "compute κ, then apply
Bombieri–Lang" as if it could prove emptiness.
