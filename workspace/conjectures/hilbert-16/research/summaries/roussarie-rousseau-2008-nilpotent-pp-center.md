# Roussarie–Rousseau 2008, nilpotent pp-graphics around a center

Source: `research/sources/roussarie-rousseau-2008-nilpotent-pp-center.full.md` [[roussarie-rousseau-2008-nilpotent-pp-center.full]] — from `http://www.dms.umontreal.ca/~rousseac/Roussarie_Rousseau.pdf`.

## What the source establishes

Proves finite cyclicity of **4 DRR graphics** through a **triple nilpotent point
of elliptic type surrounding a center**: (H¹₇), (F¹₇a), (H³₁₁), (I¹₆a) — all of
**pp-type** (join two parabolic sectors of the nilpotent point).

- Exact cyclicity **= 2** for (H¹₇) and (H³₁₁).
- (F¹₇a) and (I¹₆a) occur in **continuous families**; exact cyclicity = 2 except
  for a **discrete subset** of members.
- The method is stated to extend to most other graphics through a triple
  nilpotent point surrounding a center.

### Core machinery (normal forms + transition maps)
- Proposition 2.1/2.3: normal forms `ẋ = y + ax² − y² + ε4xy + ε1`,
  `ẏ = xy + ε2 + ε3y` (and the infinity version) for a nilpotent saddle/elliptic
  point + a center.
- Proposition 4.10: the regular transition `y → R4(y, 0)` is **not affine**
  (`∂²R4/∂y² ≢ 0`); hence for each y₀ some derivative `∂ᵏR4(y₀,0) ≠ 0`, with
  k(y₀) = 2 for all but a discrete subset.
- Theorem 6.1/6.2: `Cycl(X̄, Γ₀) ≤ ord(Γ) < ∞` — **cyclicity bounded by the
  order of the graphic** (the first nonzero derivative of the transition map).
  This is the derivation–division principle in the nilpotent setting.
- Theorems 6.3, 7.5, 7.6 give cyclicity ≤ 2 for the named graphics.

## What it implies here

Primary source that upgrades those four rows from "reported" (Shan 2013) to
**sourced-held** — claim `drr-rousseau-2008-pp-center-cyclicity2-sourced`. It is
the concrete instance of the general principle: *a graphic has finite cyclicity
bounded by the order of its regular transition map when that map is not flat*,
which is the argument shape a Lean `ord(Γ) < ∞ → Cycl ≤ ord(Γ)` statement would
capture.

Evidence class: sourced-held — read from the held full text. Hypotheses: n=2,
pp-graphics through a triple nilpotent elliptic point surrounding a center.
Falsifier: a member (outside the discrete subset) with a stable limit cycle
count > 2.

Claim id `drr-rousseau-2008-pp-center-cyclicity2-sourced` (full statement in
`research/notes/claims.md`).
