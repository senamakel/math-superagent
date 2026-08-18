# Scholar pass — reconciliation digest: Lu bundle-holding contradiction and library state

## Scope of this pass

The research agent's recent cycles added a large set of primary sources. My job:
read the new material against the goal/tasks/current beliefs, record what each
establishes, store durable verified findings, say which sources do not help, and
flag anything contradicting recalled memory.

**Finding: the library additions were already digested by prior scholar passes.**
Across the librarian's cycles the acquisitions were: DGR 2002 elementary
closures, Luca 2009 alien cycles, Marín 2026 fake-saddle transition maps,
Torregrosa 2024 (M(3)≥12), Villanueva–Tucker 2026 (Bautin-ideal enclosure),
Huzak 2022 (canard cyclicity), the Lu 2026 bundle scripts, Prohens–Torregrosa
2019 (H(4)≥28), Gasull–Lázaro–Torregrosa 2010 (abstract-only), and the full
DRR/nilpotent/degenerate/Liénard/Abelian-integral corpus. Each already carries a
claim block (research/notes/claims.md), a summary, and (where the server was up)
durable memory. I re-verified the load-bearing ones against memory this pass.

## The one NEW finding this pass: a stale-memory contradiction on the Lu bundle

Durable memory AND CONTEXT gap-2 both persisted an obsolete edge:
`lu-h14-3-verification --[not_held]--> verify_h14_center_bautin.py` / 
`verify_h14_center_global_domains.py` — i.e. "the two bundle scripts are still
not held." **This contradicts the library**: the fifth-pass addendum held both
in full (`research/sources/lu-h14-3-verify-center-bautin.py.full.md`,
`lu-h14-3-verify-center-global-domains.py.full.md`).

The distinction to keep:
- **Holding** — both scripts ARE held (resolved by fifth pass).
- **Verification** — neither is yet re-executed clean-room in this workspace, so
  their claims (`lu-h14-3-bautin-focal-values-u0` with U(0)=1/48;
  `lu-h14-3-global-center-domains-checked-statements`) stay **asserted**, not
  **checked**. That half of the memory edge is still right.

Also clarified: the third bundle script `verify_h14_center_basis.py` is NOT held
as a full source file, but its entire content (four bridge identities + Darboux
cofactors X(L)=(x+dy)L, X(F)=(2Bx+dy)F, inverse-integ-factor cofactor div X =
(x+dy)+(2Bx+dy)) was independently clean-room re-derived and VERIFIED by
`code/bautin/verify_lu_core.py` (capture `code/out/lu_core.captured.txt`, "ALL
ASSERTIONS PASS"). So it is NOT a live gap — the one genuinely "un-verified"
part of the Lu bundle is the human-proof remainder of the theorem, which is
machine-unchecked by design.

Stored the reconciliation to durable memory.

## Confirmed per-source (memorised, verified earlier passes)

- DGR 2002: seven elementary DRR graphics, cyclicity ≤ 2/3 (exact, not
  existential) — `drr-dgr-2002-elementary-closures`.
- Luca 2009: alien limit cycle, Abelian-integral-zeros insufficient for n≥3;
  confined to period-annulus route. `h16-alien-limit-cycles-abelian-insufficiency`.
- Marín 2026: uniform fake-saddle transition map; refutes Coll–Gasull–Prohens
  2025; template for division-in-flat-class. `fake-saddle-uniform-transition-map-marin2026`.
- Torregrosa 2024: M(3) ≥ 12. `h16-torregrosa-cubic-12-small-cycles-2024`.
- Villanueva–Tucker 2026: Bautin-ideal ENCLOSURE (⊆, sufficiency), conditional.
- Marín–Villadelprat 2025: hyperbolic hemicycles cyclicity exactly 2/3 — settled,
  so the open DRR rows are the degenerate (nilpotent) ones. `drr-mv-hemicycle-cyclicity-2`.

## Sources that do NOT help (and why)

- `gasull-lazaro-torregrosa-abelian-zero-bounds-2010` — abstract-page-only; no
  numeric (K,n) bound is establishable; do not cite a number from it. Concrete
  Chebyshev instrument = Grau–Mañosas–Villadelprat (fully held).
- `llibre-zhang-lienard-conjecture-survey` — contaminated (unrelated Mureddu
  power-grid paper, arXiv:1612.05532); never cite for Liénard.
- Landing pages (kaloshin.html, yakovenko.html, binyamini-novikov-yakovenko.html,
  rouseau-shan-zhu.full, etc.) — abstract-only, do not re-read as full texts.
- `alvarez-coll-demaesschalck-prohens-canard-lower-bounds` — broken "Redirecting"
  capture; the canard lower bound is at MaRDI-review level only.
- Citation-graph files (`citations_w*`) — leads, not evidence; none establishes
  any number or closure. Do not treat a citation row as a result.

## Contradictions (none new this pass; existing ones stand)

- Dulac finiteness "settled" vs Yeung 2024-25 peer-reviewed gap claim vs
  community view (Llibre 2024) — proof's completeness contested, not falsified.
- DRR 121 vs 125 count (RSZ/RR/Ilyashenko vs Shan 2013) — unresolved; DRR 1994
  raw catalogue not held.
- Liénard n=5: general mixed-parity OPEN; Rychkov 1975 odd-only degree-5 ≤ 2
  (refines, does not strike, `h16-lienard-n5-open`).
- Marín 2026 Thm 1.1/Ex 3.1 refutes Coll–Gasull–Prohens 2025's fake-saddle
  necessary condition (NOT DMRT 2015).

## What the run still lacks (unchanged)

1. **Complete current 121-graphic ledger** (DRR 1994 raw list / post-2020
   consolidation) — requests `complete-current-ledger-cb3d` /
   `dumortier-roussarie-rousseau-9c4f` still open. Run's honest open-row count:
   ≥89 of 121 fully closed (88 RSZ + I¹₁₄ RR), (I⁶b¹),(H¹³₃),(DI₂b)
   boundary-sets-only, (H³₁₄) open with Lu 2026 preprint claiming it, ≥11
   degenerate open (Shan 2013).
2. **Clean-room re-execution of the two held Lu bundle scripts** — would upgrade
   `lu-h14-3-bautin-focal-values-u0` and `lu-h14-3-global-center-domains-checked-statements`
   from asserted to checked (thread `lu-h14-3-verification` next-step).
3. Full texts of Li–Liu–Yang 2009 (H(3)≥13), Han–Li 2011 (n²log n primaries),
   Mañosas–Villadelprat 2011 — captured at claim level, paywalled.
