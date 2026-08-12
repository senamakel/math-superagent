# Provenance of V_hexagon: the published literature leaves n>4 OPEN

## The finding (source-backed)

In **Abel, Akitaya, Demaine, Demaine, Hesterberg, Ku, Lynch, "Escaping a
Polygon" (arXiv:2007.08965v3)**, the paper's own **Open Problems** (item 4)
reads, verbatim:

> "Can we determine the exact critical speed ratio for regular n-gons for
> n>4? Our pursuer strategies for equilateral triangle (Section 4.5) and
> square (Section 4.6) generalize naturally, but we have been unable to find
> matching escaper strategies, suggesting these may not be tight."

So, as of this paper, **the exact critical speed ratio for a regular n-gon
with n>4 — including the hexagon n=6 — is an OPEN problem in the published
pursuit-escape literature.** Abel et al. establish exact values only for the
disk (4.603), equilateral triangle ((3+√5)√2 ≈ 7.405) and square
(√(5/2(7+√41)) ≈ 5.789) — Table 1, all matching the run's PE 761 validation
anchors — and they explicitly do NOT settle the hexagon.

The Hesterberg thesis (the primary source behind Abel et al.) likewise proves
circle and wedge only; its exact list is circle + wedge, with general-polygon
bounds (9.2504) too coarse for an 8-decimal answer.

## Sourcing tier check (this cycle, 2026)

"Escaping a Polygon" has NOT appeared in the SoCG 2021 proceedings: a search
of the SoCG 2021 table of contents (drops.dagstuhl.de LIPIcs-volume-189) for
that title finds nothing, and the dblp entry for arXiv:2007.08965 lists no
venue (Informal/Other Publication). So as of this cycle it is the **arXiv v3
preprint (2025-10-20)** plus Hesterberg's MIT thesis (2018), not a
peer-reviewed conference/journal item. Cite it accordingly — rigorous preprint,
with exact values proven only for disk/triangle/square.

## Consequence for the run's answer

V_hexagon = 2 + 2√21/3 ≈ **5.0550504633** rests **solely on the stewbasic
Math.SE general-n formula (q.1762665, used at n=6)**, cross-checked for
internal consistency (n=3/4/∞ anchors reproduce the paper-oracle values, and
the n=6 value reduces to an exact quadratic-surd closed form):
- V(4) = √(5/2(7+√41)) = 5.78859314 (matches Abel Table 1 AND statement oracle)
- V(3) = (3+√5)√2 = 7.404918 (matches Abel Theorem 4.5)
- V(∞) → 4.6033388 (matches disk / Ponder-This / Hesterberg)
- V(6) = 5.0550504633 = 2 + 2√21/3

These anchors make the *formula* trustworthy, and the n=6 value is
self-consistently closed-form, but **no held primary source independently
derives the hexagon value** — Abel et al. explicitly leaves n>4 open. The one
independent game-encoding solver built (`code/indep_game_encoding.py`) encodes
the straight-dash red herring and fails to reproduce even the square/circle
oracles, so it verifies nothing.

**Honest status:** the formula-route value is well-supported (three anchors +
exact closed form) but the hexagon itself is not independently confirmed by
any second, correct model or by the published literature. When the hexagon
value is reported, its provenance must be stated as formula-derived +
closed-form-confirmed, single-route, with the note that the peer-adjacent
literature flags n>4 as open.

## Confirmed again on the librarian pass (this run)

A fresh web/arXiv search (research papers, 2020–2025) for an exact regular-n /
hexagon critical speed found **no** source that settles the hexagon beyond the
stewbasic Math.SE formula: the only hits were Escaping a Polygon
(arXiv:2007.08965v3, Oct 2025), the Hesterberg thesis, and unrelated
microswimmer/pursuit-robotics work. The value stays **single-route**.

An `oeis_lookup` on the hexagon constant's leading digits
[5,0,5,5,0,5,0,4,6] returns **no matching catalogued sequence**, consistent
with the earlier decimal search (`oeis-search-hexagon-critical-speed.md`).
The hexagon constant 2+2√21/3 ≈ 5.05505046 is **not** in OEIS (nor is the
square 5.78859314); only the circle constant is catalogued (A328227, A115365).
So no OEIS closed form exists to look up; the run's own exact closed form
2+2√21/3 (code/hexagon_closed_form.py, hexagon_verify_exact.py) is the
authoritative expression.

```claim
id: abel-open-ngon-ngt4
statement: The exact critical speed ratio for a regular n-gon pursuit-escape game with n>4 (including the hexagon) is left OPEN by Abel et al. arXiv:2007.08965: the paper's strategies for triangle and square generalize but matching escaper strategies were not found, "suggesting these may not be tight"; exact values are given only for disk (4.603), triangle ((3+sqrt5)sqrt2=7.405) and square (sqrt(5/2(7+sqrt41))=5.789).
hypotheses: the pursuit-escape model of Abel et al. (escaper speed 1 inside a polygon, pursuer speed r constrained to the boundary/moat, escape = reach boundary a positive distance from the pursuer).
holds-here: partially - it confirms the run's n=3/4/disk anchors match published exact values, but it does NOT provide or confirm the hexagon (n=6) value; the run's V_hexagon relies on the stewbasic formula, not on Abel et al.
status: sourced (statement in the paper's Open Problems section, arXiv:2007.08965v3).
bearing: bounds how the hexagon value may be cited - it is formula-derived + exact-closed-form-confirmed, single-route, NOT confirmed by the peer-adjacent literature which leaves n>4 open.
anchor: research/sources/escaping-a-polygon-ab el-et-al.full.md
```
