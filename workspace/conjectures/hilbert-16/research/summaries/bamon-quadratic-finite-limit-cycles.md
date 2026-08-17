# Bamón 1986 — quadratic fields have finitely many limit cycles

Full text: [[bamon-quadratic-finite-limit-cycles.full]].
Publ. Math. IHÉS 64 (1986) 111–142, doi:10.1007/BF02699193. Note: the stored file is
the **landing/record page** (title, bibtex, references); the paper's proofs are not
held. Claim sourced at title/metadata level, and cross-confirmed by the Ilyashenko
survey's history (Dulac→gap→Écalle/Ilyashenko) — Bamón 1986 is the n=2 case solved
before the general theorem, explicitly a special case of Dulac's problem.

## What the source establishes

Every individual quadratic planar vector field has a **finite** number of limit
cycles. This is the n=2 instance of the individual-finiteness (Dulac) theorem —
proved in 1986, before Écalle (1992) / Ilyashenko (1991) settled the general case
(gap in Dulac's 1923 proof found 1981). It is pointwise, per field; it gives no
uniform bound over the quadratic family — H(2) < ∞ remains open.

## What it implies here

- Confirms the classical folklore "finiteness for a fixed quadratic field was
  known before Écalle/Ilyashenko" — the pointwise pillar holds for n=2
  independently of the contested general proof (Yeung 2024). So even if the
  general Dulac proof has a gap, the n=2 pointwise statement stands on Bamón.
- It does NOT make progress on uniformity: H(2) < ∞ still requires the DRR
  finite-cyclicity reduction. The value: isolates Bamón as a distinct source for
  pointwise quadratic finiteness, removing dependence on the contested step for
  the n=2 frame.

```claim
id: h16-bamon-quadratic-finiteness
statement: Every quadratic planar vector field (each individual field, P,Q of
  degree <= 2) has finitely many limit cycles.
hypotheses: fixed individual quadratic field; no uniformity in coefficients.
holds-here: yes
status: asserted
bearing: the pointwise-finiteness pillar for n=2 held independently of the
  contested general Dulac proof (Bamon 1986) -- the n=2 frame does not depend on
  the Yeung 2024 contention. Uniformity (H(2) < infinity) remains open.
anchor: research/sources/bamon-quadratic-finite-limit-cycles.full.md
```