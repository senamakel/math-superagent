# Scholar digest — 2026 fifth-pass (Huzak 2022, Torregrosa 2024, Lu bundle scripts, Villanueva–Tucker 2026, Gasull–Lázaro–Torregrosa 2010)

## What the research agent added this cycle, and what I did with each

The fifth-pass addendum added five items. I read each against the goal (attack
H16.2, DRR inventory, Bautin/oracle instrumentation) and digested the ones not
already covered.

### 1. Huzak 2022 (JDE 320, canard cycles, hyperbolic saddle off the slow curve) — WRITTEN
The `.md` was a partial "Digest only" with the theorem statements but no
hypothesis/bearing analysis. I rewrote it as a proper note from the full text:
Thm 2.1 Cycl ≤ 1 (hyperbolic cycle), Thm 2.2 S non-neutral r≠1 → breaking-
mechanism bounds, Thm 2.3 saddle at one corner ≤3 (connection breaks) / ≤2
(extra slow singularities), Thms 2.4–2.6 corner singularities both ends ≤2–3.
Methods family blow-up + slow divergence integral. It is instrument-route
evidence (per-individual-cycle bounds, not uniform), not a DRR-ledger row.
Claim `h16-huzak-canard-hyperbolic-saddles-2022` retained.

### 2. Torregrosa 2024 (São Paulo JMS, cubic 12 small cycles) — ALREADY COMPLETE
Verified the note and claim `h16-torregrosa-cubic-12-small-cycles-2024`: M(3) ≥ 12
(supersedes Żołądek's 11), Theorems 1.1/1.2, degree-14 α polynomial, two systems,
exact CAS + Sturm. No change needed; it already carries the claim and the
escalation note (`approach-certified-lower-bound-target-escalated`) correctly
recast the certified-lower-bound target.

### 3. The two Lu 2026 bundle scripts — WRITTEN (both), upgraded in thread
Previously CONTEXT gap‑2 "two bundle scripts still not held." Both now held.
I read each fully and wrote two notes with **new claim blocks**:

- `lu-h14-3-bautin-focal-values-u0` — from verify_h14_center_bautin.py (B9–B10):
  L₁=(AC+CD+2DF−EF)/8, H14 ω-parametrization, reduced ℓ₁ numerator over 8w⁵,
  both centre components (a=0,d=0; m=−B,d=−a) annihilate L₂, and L₂|ℓ₁=0 =
  (a(B+m)/48)ε² → **U(0)=1/48**.
- `lu-h14-3-global-center-domains-checked-statements` — from
  verify_h14_center_global_domains.py: reversible first integral (zero Lie
  derivative), extra critical point (0,1/m), source-minus-saddle barrier
  identity; quadratic inverse integrating factor (1+y)k/(a²−1) with gate point
  (−a/B,−1/B), gate Jacobian (B−1)(a−1)(a+1)/B, axis factor on x=ay.

**Critical caveat recorded in both**: the scripts are HELD but **NOT re-executed
in this workspace**. The identity half shared with the clean-room run (8L₄,
192L₆+P30, Darboux cofactors) IS verified here (code/out/lu_core.captured.txt);
the U(0)=1/48 / both-components / global-barrier statements are **asserted-by-source**
until a clean-room re-run is captured (next-step, would upgrade to `checked`).
Both claims use `status: asserted`, not `checked`, and `follows-from:
lu-h14-3-bundle-scripts-now-held` (+ the identity-half claim for the bautin one).
The `lu-h14-3-verification` thread is updated to reflect the scripts now held
and the remaining assert→check step. CONTEXT gap‑2 is closed at the *holding*
level, not verification.

`lu-h14-3-bundle-scripts-now-held` (from the librarian) is kept as the umbrella.

### 4. Villanueva–Tucker 2026 (arXiv:2602.22558v2) — VERIFIED ACCURATE, no change
The `.arxiv.full` (generic-bautin-cyclicity) is a landing page; the real body is
`darboux-center-bautin-ideal-2026.full.md`. I read the actual theorem/proof
(§1–§4): Theorem 1 gives the **inclusion** 𝔅(ℱ_h(n)) ⊆ ⟨v_{n+1,*}⟩ (even n) or
⊆ ⟨L_{(n−1)/2}, v_{n+1,*}⟩ (odd n), V_{n+1}=0 (+L_{(n−1)/2}=0) as sufficient
center conditions, explicit caveat "there are center conditions not captured by
V_{n+1}=0"; Prop 2 Darboux interpretation; the inductive structure making all
Lyapunov constants linear in the coefficients of V_{n+1}. The existing note and
claim `h16-villanueva-tucker-darboux-bautin-enclosure-2026` are an accurate
rendering — the enclosure is correctly read as ⊆ (sufficiency), precisely the
claim's falsifier. **No edit needed.**

### 5. Gasull–Lázaro–Torregrosa 2010 (arXiv:1012.5201) — REWRITTEN, landing-page-only
The held `.full.md` is **only the arXiv abstract/browse page** (no mathematics
beyond the abstract). I rewrote the note to record honestly: the abstract-level
statement (K straight lines {G=0}, degree-n perturbation, explicit bound in K and
n via explicit Abelian integral + a new real-function zero bound), that **no
exact numeric bound is establishable from the held file**, and the bearing
(open-access sibling of paywalled Mañosas–Villadelprat JDE 251; same
Chebyshev/Wronskian machinery). Explicitly flagged: do not cite a number from
this source — it would be fabricated. Claim
`h16-gasull-lazaro-torregrosa-abelian-zero-bounds-2010` retained at abstract
level.

## Contradictions flagged / noted
- **Marín 2026 vs Coll–Gasull–Prohens [2]** (fake-saddle class boundary): Marín
  Thm 1.1 + Example 3.1 — X₄=(x+y)²∂x+y⁴∂y IS a fake saddle (d=4), refuting
  CGP's necessary condition (h₀,₁−a₁,₁)²+4(h₁,₀−1)<0 or h₁,₀=1,h₀,₁=a₁,₁; X₃,
  invariants (2,0,0)∈{d=0}∩{a²−b²=4}, is NOT a fake saddle. I initially mis-stored
  this as "vs DMRT 2015"; corrected the durable memory to name Coll–Gasull–Prohens.
- Re-checked the pre-existing library contradictions (Dulac proof contested vs
  finiteness; 121-vs-125 DRR count; Liénard n=5) — unchanged and still live.

## Memory server status
Up this cycle. Stored durable findings: Lu bundle-script content (via the two
new claims' sources), Huzak 2022 cyclicity bounds, Gasull–Lázaro–Torregrosa
landing-page-only caveat, and the corrected Marín-vs-CGP contradiction.

## What the run still lacks (unchanged)
- Clean-room re-execution of the two now-held Lu bundle scripts (would upgrade
  both new claims to `checked`) — recorded as next-step in the thread and the
  claims' bearings.
- Complete current 121-graphic ledger (DRR 1994 raw list; post-2020
  consolidation) — the standing gap, requests
  `complete-current-ledger-cb3d` / `dumortier-roussarie-rousseau-9c4f` still open.
- Full texts of Li–Liu–Yang 2009 (H(3)≥13), Han–Li 2011, Mañosas–Villadelprat
  2011 (all paywalled) — captured at claim level only.
