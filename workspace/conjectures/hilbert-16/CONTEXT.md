# Established — 2026-08-18, refreshed 2026-08-19 (workspace survey)

## The DRR target inventory
Synthesis in `research/drr-list.md`; individual rows are claims `h16-drr-121-graphics`, `h16-drr-closed-rows-2015`, `h16-drr-open-rows`, `drr-rr-closes-i14`, `drr-rr-boundary-only-for-3-graphics`, `drr-shan-2013-table11-ledger`, `drr-DI2a-partial-only`.

- H(2)<∞ is equivalent to finite cyclicity of the **121 DRR graphics** (DRR 1994, JDE 110:86–133; equivalence sourced-held in RSZ 2015 / Ilyashenko 2002 / RR 2015).
- **≥89/121 fully closed by 2015**: 88 (RSZ 2015) + `I^1_14` (Roussarie–Rousseau 2015 Thm 1.2). "89" is this run's arithmetic, not the authors' count.
- **Boundary-only:** `I^1_6b`, `H^3_13`, `DI_2b` — RR 2015 Thm 1.1 proves finite cyclicity only of the boundary limit periodic set; the full graphics are explicitly left to future work.
- **`H^3_14` open** in the settled record (the one triple-point-at-infinity graphic with no partial result in RR 2015). Lu arXiv:2607.13785 (Jul 2026, **unrefereed**) claims local uniform finite cyclicity; its finite algebraic core is independently verified, the analytic remainder (`G-remainder`) is not.
- **≥11 degenerate graphics open** (Shan 2013 thesis): `DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4, DH5`. `DF1a`/`DF2a` closed (DF2a's non-desingularizable P* point by Huzak 2018, CPAA 17:1305–1316); `DI2a` has partial results only (ADL 2009).
- **No complete post-2015 graphic-by-graphic ledger exists** in the public record (`drr-ledger-no-consolidated-post2020`); the 121-vs-125 count discrepancy is a convention difference, unresolved.

## Kernel-checked (fresh captures 2026-08-18, `code/out/lean/*.json`; axioms as stated)
- `Bautin.V3_not_mem_span_V1_V2` — **L8 ∉ ⟨L4,L6⟩** over Q, evaluation witness certPt=(-2,-2,1,-1,-1,1) (V1=V2=0, V3=25/64≠0), two independent routes; **conditional** on the Cited Bautin-1952 axioms. File `code/lean/Lib/Bautin.lean`. **M(2)=3 itself is a Cited axiom, not kernel-proved.**
- `BautinRecurrence` — 192·L6+P30=0 (P30's 30 monomials, coefficientwise `decide` over Fin 30), L4num=AC+CD+2DF−EF ≠ 0, Darboux cofactor identities; **verified, no cited axiom, no sorry**.
- `SlowDivergenceECTPartial.full_graphic_zero_bound` — sorry **closed**: ECTReduction (representation ∧ nonzero ∧ ect_property) ⇒ uniform zero bound N = dimension−1 over compact K; axioms = kernel's three. The analytic content (four second-type endpoint germs, uniform remainder) is the open gap — exactly task `i6b-four-passage-analytic-gap`.
- `Statement.h16_2` — H16.2 stated with real degree-≤n polynomials and `Finite ∧ ncard ≤ N` (the ncard-alone vacuity hole is closed); one deliberate `sorry`. Mathlib gaps (no limit-cycle/return-map/polycycle/Bautin-ideal notions) recorded in `research/mathlib-coverage-h16.md`.
- Lu H^3_14 finite core, identity half: kernel-closed (`lu_finite_core_identity_half_checked`, `G-lean-cert`); clean-room capture `code/out/lu_core.captured.txt` (ALL CLEAN-ROOM CHECKS PASS).

## Computed boundary (exact, over Q, lex Gröbner — `code/out/membership.captured.txt`)
Focal-value monomial counts d=4..12: 4, 30, 97, 236, 485. L8∉⟨L4,L6⟩ (remainder 16 mono), L6∉⟨L4⟩, **L10,L12 ∈ ⟨L4,L6,L8⟩** (remainder 0, positive controls True). Task `bautin-membership-l14-l16` extends the chain to L14/L16; task `bautin-m2-oracle` reproduces M(2)=3 via the Bautin ideal.

## Ruled out (kept; the approaches ledger carries 30+ more with reasons — read before re-proposing)
- **Asymptotic-expansion-only route** — fails the smooth test; an expansion does not determine a displacement germ (Dulac's 1923 error).
- **Four-passage ECT shortcut for `I^1_6b`** — individually-ECT passages do not imply their sum is ECT: exact toy (1,x)+(−1,−x)=0 with W=1 each; (a,ax) loses rank at a=0. `research/approaches/i6b-four-second-type-toy.md`. Refutes the inference only, not the dynamics.
- O-minimality of L_trans is itself the open conjecture (`h16-ominimality-route-roussarie`); the Rolin–Servi generalized-quasianalytic algebra was adopted as its testable substructure (synthesis record: `research/findings/convergence-quasianalytic-displacement-module.md`).

## Live frontier (ledgers carry the detail)
Standing thesis `bautin-ideal-kernel-checked-then-drr`: next bankable step is the cofactor lift L10/L12/L14 ∈ ⟨L4,L6,L8⟩ to Lean; the analytic remainder G-remainder is the real mathematical gate after the algebraic core. Open goals: `h16-2-finite-cyclicity` (frame), `h16-2-h14-3-finite-cyclicity` (G-remainder), `h16-sharp-abelian-named-family` (first instantiation Yang 2025, cyclicity n−1), `h16-2-degenerate-graphics-finite-cyclicity` (DI2a first). Fishkin 2010 constants remain unverified (thread `restricted-h2-bounds`).

## Memory / operational
- **Cognee is down** (409 on every recall/remember this cycle). Durable record = on-disk findings + ledgers. When it recovers: store the Rolin–Servi synthesis decision and the Ilyashenko 1990/2016 holdings (librarian handoff 2026-08-19).
- Wrong-fetch lesson (mathnet paperids are not derivable from DOIs; verify first lines before trusting a fetch) — `research/findings/wrong-fetch-rozanova-mislabeled-ilyashenko-1990.md`.
- `GOAL.md` was destroyed and restored 2026-08-18 (see its header); write_tool_file calls must never target bare workspace-root filenames.
