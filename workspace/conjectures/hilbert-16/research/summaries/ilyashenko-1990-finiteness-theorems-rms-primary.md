# Ilyashenko 1990 — Finiteness theorems for limit cycles (first half)

Full text: [[ilyashenko-1990-finiteness-theorems-rms-primary.full]]
(Uspekhi Mat. Nauk 45:2 (1990) 143–200; Russian Math. Surveys 45:2 (1990) 129–203).
This is the first half of a two-part paper; the second, far longer part was published as
the book (1991, "Finiteness theorems for limit cycles", AMS Translations).

## What the source establishes (held full text, verbatim)

**Theorem I.** A polynomial vector field on the real plane has only finitely many limit cycles.
**Theorem II.** An analytic vector field on a closed two-dimensional surface has only finitely many limit cycles.
**Theorem III.** A singular point of an analytic vector field on the real plane has a neighbourhood free from limit cycles.
**Theorem IV.** An elementary compound cycle (polycycle) of an analytic vector field on a two-dimensional surface has a neighbourhood free from limit cycles — Poincaré–Dulac showed I follows from IV; Ilyashenko proves I directly and IV is "an obvious corollary".

**Theorem V (identity theorem).** A monodromy transformation of a compound cycle of an
analytic vector field that has countably many fixed points is the identity.

**Structure of the method (the part that matters for this run):** the proof constructs a
set of germs (ℝ₊,0)→(ℝ₊,0) containing monodromy transformations of compound cycles, with
two properties: **expandability** (each germ is assigned an asymptotic series carrying
power AND exponential asymptotic information) and **extensibility** (the germ extends to
an almost-regular map on a complex quadratic standard domain). The identity theorem is a
quasianalyticity statement: a monodromy with countably many fixed points has trivial
expansion hence is identity. §1 expands monodromy transformations of class 1 into terms
with incommensurable rates of decrease; §2–§3 develop function-theoretic properties
(simple and sectorial cochains) and a Phragmén–Lindelöf theorem; §4 superaccurate
asymptotic series.

## What it lets this run conclude

- The pointwise-finiteness pillar is anchored here as a two-part paper; the 1990 part
  carries the statement and the method digest, the 1991 book the full general proof.
- **This is the exact place where analyticity/quasianalyticity enters** (Test 1 of
  problem.md): the identity theorem is a quasianalyticity statement for the return-map
  germ class. A C^∞ version is false (flat germs with countably many zeros, e.g.
  exp(−1/x)sin(1/x)); this is the structural fact every candidate finiteness argument
  must reproduce.
- The Yeung 2024/25 contention (`h16-dulac-proof-contested`) attacks exactly the
  ordering-of-asymptotics step inside this machinery for non-hyperbolic polycycles; the
  theorem is not claimed false, the proof completeness for semi-hyperbolic equilibria is
  contested. See `research/summaries/yeung-ilyashenko-finiteness-gap.md`.

```claim
id: h16-ilyashenko-1990-finiteness-theorems
statement: Ilyashenko (1990, first half of a two-part paper) states: Theorem I — a polynomial vector field on the real plane has only finitely many limit cycles; Theorem II — an analytic vector field on a closed two-dimensional surface has finitely many limit cycles; Theorem III — a singular point of an analytic vector field has a neighbourhood free from limit cycles; Theorem IV — an elementary compound cycle of an analytic vector field has a neighbourhood free from limit cycles; Theorem V (identity theorem) — a monodromy transformation of a compound cycle with countably many fixed points is the identity. The 1990 part gives the special case proof and the method digest; the general proof is the 1991 book.
hypotheses: analytic (in particular polynomial) planar vector fields; elementary compound cycles for Theorem IV; the identity theorem holds in the almost-regular germ class on quadratic standard domains.
holds-here: yes — this is the pointwise (individual-field) finiteness pillar; it gives no uniform-in-family bound.
status: asserted
evidence: full text held at research/sources/ilyashenko-1990-finiteness-theorems-rms-primary.full.md, theorems verbatim at lines 24-66.
falsifier: a polynomial planar field with infinitely many limit cycles (would refute Theorem I); or the Yeung contention upheld against Ilyashenko's proof for semi-hyperbolic polycycles (contests completeness, not the statement).
sources: https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=4718&what=fullteng&option_lang=eng
anchor: research/sources/ilyashenko-1990-finiteness-theorems-rms-primary.full.md
follows-from:
answers:
```
