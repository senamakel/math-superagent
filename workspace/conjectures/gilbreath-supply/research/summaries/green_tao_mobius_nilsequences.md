# Green–Tao, "The Möbius function is strongly orthogonal to nilsequences"

Source: Ben Green & Terence Tao, arXiv:0807.1736 (v4 2011), published *Ann. of
Math.* (2) **175** (2012) 541–566 / 567–617 (companion pair). Source URL:
https://arxiv.org/pdf/0807.1736. Full text:
`research/sources/green_tao_mobius_nilsequences.full.md`.

## What it establishes

**Main theorem (Möbius–nilsequence orthogonality, MN(s)).** Let `G/Γ` be an
`s`-step nilmanifold (G a connected simply-connected nilpotent Lie group, Γ a
discrete cocompact subgroup), `g : Z → G` a polynomial sequence, `F : G/Γ → R`
Lipschitz. Then

```
| (1/N) Σ_{n≤N} μ(n) F(g(n)Γ) | ≪_{F,G,Γ,A} log^{−A} N   for all A > 0.
```

That is, the Möbius function is strongly asymptotically orthogonal to any
polynomial nilsequence. This proves the Möbius-and-nilsequence conjecture MN(s)
from the authors' earlier programme [8] for every `s ≥ 1`, and is one of the two
major ingredients toward the generalised Hardy–Littlewood conjecture.
Applications: μ is uncorrelated with any bracket polynomial such as `n√3 ⌊n√2⌋`;
and a result on the distribution of nilsequences `(a^n x Γ)` as `n` ranges over
the primes.

## Why it matters here

This is the **value-domain engine** the (now refuted)
`gowers-u2-nilsequence-uniformity` approach named. That approach asked whether the
Möbius-orthogonality machinery supplies the "h has no structural invariant for Φ"
step. **The approach is refuted (research/APPROACHES.md), on a basis mismatch:**
the fold cell `(−1)^{T(n,d)}` lives on the ANF/zeta (submask-XOR) basis, not the
Walsh/U² basis that the Gowers inverse theorem and nilsequence orthogonality
govern, so U²-uniformity does not bind S(n); and the object here is `χ(q_j)` at
prime index `j`, not μ at integer values. Green–Tao is a genuine value-domain
orthogonality theorem for μ against nilsequences; it does not reach the fold.

```claim
id: green-tao-mobius-orthogonal-to-nilsequences
statement: |(1/N)Σ_{n≤N} μ(n)F(g(n)Γ)| ≪_A log^{−A}N for every A>0, for any s-step nilmanifold G/Γ, polynomial sequence g:Z→G, and Lipschitz F:G/Γ→R. Proves MN(s) for all s≥1; implies μ is strongly orthogonal to bracket polynomials and to polynomial phases.
hypotheses: G/Γ finite-dimensional s-step nilmanifold with Q-rational Mal'cev basis (metric); g polynomial; F Lipschitz.
holds-here: Not directly — SUPPLY's object is the prime-character string s_j = χ(q_j) indexed by PRIMES, not μ(n) indexed by integers, and the relevant observable here is the fold's submask-XOR character, not a classical nilsequence. The Möbius orthogonality is the value-domain structural engine; whether the fold's h has a nilsequence/no-structural-invariant reading that this theorem controls is the open transfer, not inherited from this source.
status: sourced (verified verbatim against full text this pass: Thm 1.1 lines 89-108)
bearing: Supplies the value-domain engine the refuted `gowers-u2-nilsequence-uniformity` approach named, providing the strong-orthogonality template (μ/λ vs low-complexity phases). The approach is refuted on a basis mismatch (the fold lives on the ANF/zeta basis, not the Walsh/U² basis the theorem controls; object is χ(q_j) at prime index, not μ at integer values). Not a proof of SUPPLY.
anchor: research/sources/green_tao_mobius_nilsequences.full.md; summaries/green_tao_mobius_nilsequences.md
```

**Honest limit:** as with the MRT sources, this is an orthogonality statement for
μ over integers, not a weight bound on `wt(Φ_n h)` for the fixed prime-gap string.
The bridge is the open content.
