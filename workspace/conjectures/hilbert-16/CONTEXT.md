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

- **Each verified identity must be an executed run.** A note saying an
  algebraic identity was "re-derived by hand with exact arithmetic" is a
  measurement nobody can reproduce; it is not a verified identity. Nothing is
  reported verified-computationally until a program exists, the program ran,
  and a capture (code/out/*.txt, first three lines naming what ran and by
  which definitions) asserts the identity on its produced data. State
  precision, step size and interval widths in every capture.
- **UPDATE (directive-carrying): Lu, arXiv:2607.13785 (2026, 80pp, UNREFEREED)
  claims local uniform finite cyclicity of exactly (H³₁₄)**, identified as B=0
  in RR 2015 Theorem 3.1's five-parameter family. **Its finite algebraic core is
  now VERIFIED-computationally in this run**: `code/bautin/verify_lu_core.py`
  (clean-room, exact sympy, without importing Lu's scripts) executed and its
  capture `code/out/lu_core.captured.txt` prints "ALL CLEAN-ROOM CHECKS PASS" —
  the bridge identities, Darboux cofactors X(L)=(x+dy)L and X(F)=(2Bx+dy)F, the
  inverse-integrating-factor cofactor div X=(x+dy)+(2Bx+dy), the degree-4
  obstruction 8L₄=AC+CD+2DF−EF, and the degree-6 192·L₆+P30=0 /
  12·weighted_g6+P30=0 with P30 having 30 monomials. Independently confirmed by
  `code/lyap_audit.py` (byte-level reconstruction of Lu's own
  verify_bautin_recurrence.py, PASS) and by `code/out/mono_counts.captured.txt`
  (L4, L6 residuals zero exactly). The cluster of 30 monomials is emitted in
  `code/out/p30_coeffs.txt` and transcribed into `code/lean/Lib/Generated/`.
  **What this does NOT establish**: Lu's Theorem 1 — the human-proof remainder
  (analytic root uniqueness, Hadamard divisibility, domain completeness, zero
  theorems) is not machine-checked, the preprint is unrefereed, and the
  cyclicity bound is **existential** (no explicit number). Claim status:
  **asserted-by-source, NOT established** (thread `lu-h14-3-verification`).
  Even if correct it closes ONE graphic — (I⁶b₁),(H₁₃³),(DI₂b) full graphics
  and ≥11 degenerate graphics (Shan 2013) remain. Still not held from the
  bundle: `verify_h14_center_bautin.py`, `verify_h14_center_global_domains.py`.
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
- **Pedregal's claimed variational resolution of H16.2 is UNREFEREED and
  suspect, not established** (arXiv:2103.07193, held full text; claims H(n)
  ≤ quartic-in-n bound and H(2)=4). It counts limit cycles as global
  minimizers of E0 = (1/2)∫(P y' − Q x')² dt via Morse inequalities +
  Bezout/Harnack on the divergence curve, with no use of analyticity of the
  return map — a prima-facie Test-1 (smooth-test) failure, Dulac's error shape.
  Its prior Llibre–Pedregal variant (arXiv:1411.6814) announced a mistake in
  counting limit cycles. Community still treats H16.2 as open (held Gasull
  2024). Thread `pedregal-variational-claim-test`; claim
  `h16-pedregal-variational-claim-unrefereed`.
- **The o-minimality route is a genuine independent method for uniform
  finiteness** (Speissegger arXiv:1804.03585, held). Roussarie's
  finite-cyclicity conjecture follows from the (OPEN) o-minimality of the
  language of parametric transition maps, via the uniform-finiteness principle;
  PROVED for the non-generic class NRH_d (only non-resonant hyperbolic
  singularities) by Kaiser–Rolin–Speissegger (Crelle 636 (2009) 1–45). This is
  where a valid uniform-finiteness proof must source its analyticity: tamed
  quasianalytic asymptotics of the return map — the structural opposite of the
  Pedregal claim. Claim `h16-ominimality-route-roussarie`.
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

- 88/121 closed by 2015 (+I¹₁₄ RR 2015 ⇒ 89 fully closed by this run's
  arithmetic, authors' count is 88); exactly 1 graphic (H³₁₄) left fully open
  by RR 2015; Lu 2026 preprint claims it — algebraic core VERIFIED here, full
  claim unverified. Open/partial: (I⁶b₁),(H₁₃³),(DI₂b) boundary-sets-only;
  ≥11 degenerate graphics open (Shan 2013) (not a full ledger — DRR 1994 not
  held).
- RE-EXECUTED exactly and captured: 8L₄ = AC+CD+2DF−EF (degree-4 Bautin
  obstruction); Darboux cofactors X(L)=(x+dy)L, X(F)=(2Bx+dy)F; the 4 bridge
  identities; the degree-6 30-monomial equality 192·L₆+P30=0 (λverif
  lyap_audit + verify_lu_core, both PASS, captures in code/out/). P30's 30
  monomials in code/out/p30_coeffs.txt + code/lean/Lib/Generated/P30Data.lean.
- Monomial counts of the focal-value obstructions L_d (NEW, computed in
  code/out/mono_counts.captured.txt, exact): L4 4 monomials, L6 30, L8 97, L10
  236, L12 485, L14 890 (d=4,6,8,10,12,14). Observation only: fraction of
  homogeneous-5-var space creeps toward ~1/2; no clean recurrence; OEIS no
  match. Do not chase a closed form.
- `lyap_audit.py` re-executed, PASS. BUT `lyap_extend.py` (degree-8/10/12 +
  ideal membership L₈∈⟨L₄,L₆⟩, L₁₀/L₁₂∈⟨L₄,L₆,L₈⟩) CRASHED in `poly_terms`
  (TypeError after computing the degree-12 recurrence, 109s) — the extension
  and the "Bautin trick" ideal-membership statement are NOT established
  (the monomial counts above were recovered by the separate mono_counts.py).
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
2. **Lu 2026's full claim is NOT verified; only its finite algebraic core is.**
   The Bautin-recurrence core passed clean-room exact re-derivation
   (code/out/lu_core.captured.txt, code/lyap_audit.py) and the direction added
   two bundle scripts still not held — `verify_h14_center_bautin.py`,
   `verify_h14_center_global_domains.py`. The human-proof remainder (root
   uniqueness, Hadamard divisibility, domain completeness, zero theorems) is
   machine-unchecked and the preprint unrefereed; the cyclicity bound is
   existential.
3. **`code/lean/Lib/BautinRecurrence.lean` and `code/lean/Lib/Bautin.lean` are
   host-fixed and both pass lean_check (Directive 5) — do NOT revert or redo.**
   `BautinRecurrence.lean` is VERIFIED (no sorry, no cited axiom):
   `h14_p30_check`, `p30_sound`, `bautin_L6_identity`, `L4num_ne_zero`,
   `param_identities`, `darboux_L_identity`, `darboux_F_identity`.
   `Bautin.lean` is CONDITIONAL (no sorry, resting only on `Cited` Bautin-1952
   axioms). Four anti-revert constraints, stated so nobody rebuilds them the
   hostile way: FIRST the kernel runs on ONE file with no lake root, so a
   second-module import fails — the P30 data is inline in a `Generated`
   namespace carrying no theorem, and `Lib/Generated/P30Data.lean` stays as
   provenance kept in step by `code/bautin/generate_p30.py`. SECOND `decide`
   over an MvPolynomial equality does not reduce — it is a Finsupp equality —
   so the check is coefficientwise over Fin 30 and `p30_sound` proves the
   bridge to the polynomial identity; never put `decide` back on a polynomial
   equality. THIRD MvPolynomial is not a division ring, so the degree-4
   obstruction is `L4num` with the denominator in the name, not `/8`. FOURTH
   the three focal values are real (computed exactly by
   code/bautin/lyapunov_quadratic.py, code/out/bautin_focal_values.captured.txt
   — V1 as a term, V2/V3 as data tables because a 220-term chain will not
   elaborate), NOT `V1=V2=V3=0`, and the family is the degree-2 one (six
   coefficients, no a30/a21/b12/b03). **Next Lean task**
   (`cofactor-certificate-L8-not-in-L4-L6`): membership.captured.txt already
   shows by exact Gröbner over ℚ that L8∉⟨L4,L6⟩, so three generators are
   genuinely needed — turn that into a kernel-checked theorem via a cofactor
   certificate. **MEMBERSHIP HALF SETTLED (Task G-lu-core):**
   `code/bautin/verify_membership.py` (capture
   `code/out/membership.captured.txt`, exact over ℚ, lex) recomputes
   L4..L12 and settles: L8∉⟨L4,L6⟩ (16-monomial remainder), L6∉⟨L4⟩
   (14-monomial remainder), **L10∈⟨L4,L6,L8⟩ and L12∈⟨L4,L6,L8⟩ (remainder
   0)** — the Bautin-trick step survives. Each decision triple-checked
   (remainder==0, G.contains, cofactor identity poly==Σqᵢbᵢ+rem) with
   positive controls all True. CAVEAT: an earlier capture reported
   L10,L12∉⟨L4,L6,L8⟩ from reading sympy 1.11 reduce()'s quotient list
   instead of its remainder — that is VOID; the corrected run is the one
   above. Next after L8-certificate: cofactor certificates for
   L10,L12∈⟨L4,L6,L8⟩. CAVEAT: the code/out/lean/*.json files are STALE (still report
   compiled:false and the pre-fix declarations) — re-capture lean_check against
   the restored files before trusting any VERIFIED claim on this disk.
4. **`code/lean/Lib/Statement.lean` compiles** (per the held lean JSON
   `compiled:true`) with the deliberate `sorry` in `h16_2`
   `(LimitCycleSet f.toMap).Finite ∧ ncard ≤ N`: the degree-≤n hypothesis is now
   real (`f.P f.Q : MvPolynomial (Fin 2) ℝ` with `totalDegree ≤ n`), and the
   `Set.ncard`-of-infinite-set-is-0 vacuity is closed by the explicit
   `.Finite ∧` conjunct. Mathlib gaps to report: no "limit cycle"/isolated
   periodic orbit (stated by hand), non-obvious import paths
   (`Data.Set.Finite.Basic`, `Data.Fin.VecNotation`), no packaged flow of a
   polynomial field. But the JSON also lists `outcome:"failed"` to reconcile —
   re-run lean_check on the current tree.

## Approach notes

- Certification concludes, numerics search. The four verified algebraic
  identities are the finite core to push to kernel-checked Lean theorems over
  `MvPolynomial` (decidable by `ring`/`norm_num` after expansion) — the
  preferred shape per the method policy.
- Every candidate argument passes the three `problem.md` tests; an argument
  never using analyticity is refuted (Dulac's error).
- Do not claim H(n) < ∞ nor H(2) = 4.