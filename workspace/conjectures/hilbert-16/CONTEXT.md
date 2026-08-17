# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call.

**Token budget**: 10,000 default. This file is re-sent on every model call in
every role that reads it. Detail compressed away lives in
`research/notes/claims.md` (the claims ledger), `research/summaries/` (one per
source), and `research/threads/` (attack directions).

## Established

Each mark = its evidence class. `claims.md` holds the full rows with
hypotheses and falsifiers.

- **Individual finiteness (Dulac's problem) is settled-but-contested.** Écalle
  (1992) and Ilyashenko (1991) proved a planar polynomial field has finitely
  many limit cycles (`h16-dulac-finiteness-theorem`, sourced: Ilyashenko 2002
  held full). Bamón (1986) proved it for each individual quadratic field
  (`h16-bamon-quadratic-finiteness`, IHÉS 64, held). BUT: Yeung 2024-25 —
  arXiv:2402.12506, and peer-reviewed "Dulac's Theorem Revisited", Qual.
  Theory Dyn. Syst. 24 (2025) — claims the Ilyashenko monograph has a gap for
  non-hyperbolic polycycles and gives an explicit counterexample (held full
  text). The theorem is not claimed false; the *proof's completeness* is under
  live contention (`h16-gap-claims-2024`, `h16-dulac-proof-contested`,
  `h16-dulac-reopened-community-view`). No Ilyashenko-side rebuttal located.
- **The DRR 121-graphics reduction is the working frame.** H(2)<∞ ⇔ every one
  of the 121 graphics has finite cyclicity inside the quadratic family
  (Dumortier–Roussarie–Rousseau 1994, JDE 110:86–133; Ilyashenko 2002; RSZ
  2015; RR 2015 — latest three held full).
- **88 of 121 closed by 2015** (RSZ's own verbatim count). RR 2015 fully closes
  (I¹₁₄); closes only the boundary limit periodic sets of (I⁶b₁), (H₁₃³),
  (DI₂b); **exactly one graphic — (H³₁₄) — through a triple point at infinity
  had no partial result at all (RR 2015 line 63, held)**.
- **UPDATE (directive-carrying): Lu, arXiv:2607.13785 (2026, 80pp,
  UNREFEREED) claims local uniform finite cyclicity of exactly (H³₁₄)**,
  identified as B=0 in RR 2015 Theorem 3.1's five-parameter family (term-for-
  term match, both texts held). Ships a reproducibility bundle. **Its finite
  algebraic core was re-derived by hand with exact arithmetic in this run**:
  the four bridge identities, Darboux cofactors X(L)=(x+dy)L, X(F)=(2Bx+dy)F,
  the inverse-integrating-factor cofactor, and the degree-4 Bautin obstruction
  8L₄=AC+CD+2DF−EF all hold exactly (`lu-finite-core-partially-verified`,
  note `research/notes/lu-finite-core-verified.md`). The human-proof remainder
  (analytic root uniqueness, Hadamard divisibility, domain completeness, zero
  theorems) is NOT machine-checked; the preprint is not peer-reviewed; the
  claim is **asserted-by-source, NOT established**. Even if correct it closes
  ONE graphic — (I⁶b₁),(H₁₃³),(DI₂b) full graphics and ≥11 degenerate graphics
  (Shan 2013) remain.
- **Lower bounds (corrected):** H(2)≥4 (Shi; Chen–Wang), H(2)=4 standing
  conjecture OPEN; **H(3)≥13 (Li–Liu–Yang 2009)**, **H(4)≥28 (Prohens–
  Torregrosa 2018)**; M(2)=3 (Bautin); M(3)≥11 (Żołądek); **H(n) ≳ n² log n:
  liminf H(n)/((n+2)²log(n+2)) ≥ 1/(2 log 2)** (Christopher–Lloyd 1995,
  Han–Li; confirmed against Buzzi–Novaes 2024 held) — so no quadratic upper
  bound on H(n) can be right.
- **Hilbert–Arnold / elementary polycycles:** finite cyclicity with explicit
  bound 2^{25k²} (Kaloshin) for elementary singularities; Ilyashenko–Yakovenko
  finiteness. Elementary is the weight-bearing hypothesis.
- **Infinitesimal/tangential H16:** solved constructively — Varchenko/
  Khovanskii non-constructive; BNY 2010 double-exponential explicit;
  Binyamini–Dor linear-in-deg-ω: N ≤ exp⁺(n²)m + exp⁺(n²) (held).
- **Liénard:** Lins–de Melo–Pugh conjecture FALSE for n≥6 (DPR 2007, ≥4 cycles
  in deg 6); n=5 open (per Llibre–Zhang 2017); degree-5 max open as of held
  sources.
- **A 2024 closed-form solution attempt H(n)=2(n−1)(4(n−1)−2) is refuted**
  (Buzzi–Novaes 2024, held): contradicts the n² log n lower bound.
- **Petrovskii–Landis 1955-57 "solution" (H(2)=3) retracted** after
  Novikov–Ilyashenko counterexamples (held, Ilyashenko 2002).
- **DRR catalog count:** 121 in DRR1994/RSZ/RR/Ilyashenko; Shan 2013 thesis
  says 125 — unresolved discrepancy, DRR 1994 raw catalogue not held.

## Ruled out

- An "information-geometry" definition of limit cycle (Fisher scalar-curvature
  count) — neither necessary nor sufficient, so it cannot bound H(n)
  (`h16-geometry-limitcycle-defn-refuted`, Buzzi–Novaes held).
- Quadratic upper bounds on H(n) in general — collide with n² log n.
- Treating the DRR 1994 paywall as insurmountable — the list's content is
  reproduced across RSZ 2015 / RR 2015 (held) and the Rousseau–Zhu papers.
- Claiming H(2) = 4 or H(n) < ∞ outright — both out of reach; any such claim
  on this run's prior is an error until each step is certified.

## Numbers

- 88/121 graphics closed by 2015; exactly 1 graphic (H³₁₄) left fully open by
  RR 2015; Lu 2026 preprint claims it, unverified. Open count ≥ 32 + 11
  degenerate (not a full ledger — DRR 1994 not held).
- Re-derived exactly: 8L₄ = AC+CD+2DF−EF (degree-4 Bautin obstruction);
  Darboux cofactors; 4 bridge identities. Degree-6 30-monomial equality
  transcribed, not yet re-executed (pinned SHA-256).
- `lyap_audit.py` re-executed, all assertions PASS (L4=(AC+CD+2DF−EF)/8,
  L6=−P/192, 30 monomials). BUT `lyap_extend.py` (degree-8/10/12 + ideal
  membership L₈∈⟨L₄,L₆⟩, L₁₀/L₁₂∈⟨L₄,L₆,L₈⟩) CRASHED in `poly_terms`
  (TypeError after computing the degree-12 recurrence, 109s) — the extension
  and the "Bautin trick" ideal-membership statement are NOT established, and
  the axis-8/10/12 monomial counts are unrecorded.
- Lower bounds: H(2)≥4, H(3)≥13, H(4)≥28, H(n)≳n²log n, M(2)=3, M(3)≥11.

## Recalled

Cognee memory server is down this cycle; findings are persisted in
`research/notes/` and the claims ledger instead. Nothing further is recalled
from durable memory.

## Contradictions

- Ilyashenko/Écalle finiteness "settled" vs Yeung 2024-25 gap claim vs
  community view (Llibre 2024) that Dulac's problem is again open — the 
  theorem is not disproved; the published proof is contested.
- 121 vs 125 DRR graphics (DRR/RSZ/RR vs Shan 2013).
- `data-contamination-llibre-zhang`: the held file named
  "llibre-zhang-lienard-conjecture-survey" is actually an unrelated power-grid
  paper (Mureddu arXiv:1612.05532) — do not cite it for the Liénard survey.

## Gaps

1. **Complete current ledger of the 121 graphics** (which open, paper closing
   each): still NOT in the library. DRR 1994 raw catalogue paywalled; its
   content is partially reproduced in held RSZ/RR. Lu 2026's (H³₁₄) closure is
   the one named recent row.
2. **Verify Lu 2026**: run the two held scripts (+2 not yet fetched: 
   verify_h14_center_bautin.py, verify_h14_center_global_domains.py) against
   pinned SHA-256; then decide the preprint's standing. Its human-proof
   remainder is exactly the gap between algebraic certification and the theorem.
3. **`code/lean/Lib/Bautin.lean` fails to compile** — `compiled: false` in the
   last check; the real Bautin V₁,V₂,V₃ are still placeholders `0`, so
   `bautin_finitely_generated` is vacuous. The verified identities above are
   the concrete replacement.
4. **`code/lean/Lib/Statement.lean`** compiles as a statement with the
   deliberate `sorry` (h16_2 at line 121); `verified:false` is the expected
   hole, not a parse error. Mathlib gaps to report: no "limit cycle"/isolated
   periodic orbit, no packaged degree-≤n polynomial field, no flow of a
   polynomial field.

## Approach notes

- Certification concludes, numerics search. The four verified algebraic
  identities are the finite core to push to kernel-checked Lean theorems over
  `MvPolynomial` (decidable by `ring`/`norm_num` after expansion) — the
  preferred shape per the method policy.
- Every candidate argument passes the three `problem.md` tests; an argument
  never using analyticity is refuted (Dulac's error).
- Do not claim H(n) < ∞ nor H(2) = 4.