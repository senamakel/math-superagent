# Scholar report — reference library digested, verified state recorded

## What this pass did

Two jobs: (1) complete the per-source digestion of the six sources the librarian
added this session; (2) reconcile the prose records with the host-verified Lean
state the operator's directive reports, and record the new computational facts
the verification captures establish.

### 1. Digestion completed — every source now has a real note

The six new full texts now have proper notes (all "Digest only — read this
first" placeholders eliminated from `research/summaries/`):

- **Dumortier–Rousseau 2009** (DF1a/DF2a degenerate graphics): exact 5-parameter
  normal forms for the 13 degenerate graphics, Theorem 3.1 (DF1a ≤ 3 cycles,
  DF2a ≤ 5), the single open point P\* = (0,0,0,1) where the family cannot be
  desingularized — the concrete shape of the smooth-test obstruction.
- **Roussarie–Rousseau 2008** (nilpotent pp-graphics around a center): exact
  cyclicity 2 for (H¹₇), (H³₁₁) and 2-except-discrete for (F¹₇a), (I¹₆a);
  `Cycl ≤ ord(Γ)` principle.
- **Zhu 2005** (pp-graphics survey): Theorem 1.2 — all 16 pp-graphics finite;
  Theorem 1.1 — cyclicity ≤ n from a non-vanishing nth derivative of the
  regular transition map.
- **Zhu–Rousseau 2002** (nilpotent saddle/elliptic machinery): Definition 1.1
  (finite cyclicity), the blow-up + two Dulac-map types + derivation–division
  method; hyperbolicity-ratio-1 well-ordered expansions.
- **DIR 2002** (saddle-node normal forms): Theorems 1–3 (C^∞ orbital
  equivalence to polynomial normal form, analytic outside the stable manifold),
  Theorem 3.1 (lips ensembles, cyclicity ≤ n), 3.2 (malignant frown,
  spadesuit), 3.3.
- **DMRT 2015 postprint** (fake saddle): cyclicity ≥ 2 for quadratic fake
  saddle, ≤ 2 in (1:1) for the symmetric family, R11 region; **critical caveat
  recorded: no contribution to the DRR degree-2 programme** — so fake-saddle
  cyclicity does not by itself close a DRR row.

Also replaced: Ilyashenko 2002 centennial (verified: e^{2500n⁴} for critically
balanced H; Ver 7.1 Exactness/Corollary 7.1 (n²+n)/2 − 1 tangential cycles;
Kaloshin E(k) ≤ 2^{25k²}), RSZ 2015 full text (88-verbatim; the a₀ = −1/2
Hamiltonian-completion mechanism), the peer-reviewed Yeung 2025 record page,
and record/bibliography pages (Bamón IHÉS record, Rousseau publications page,
Llibre–Zhang UAB record, DMRT UAB record, DMRT 2014 redirect stub). The
`drr-list.md` stale line about DMRT 2015 being "paywalled" was corrected.

### 2. Reconciliation with the host-verified Lean state (directive applied)

The directive reports BautinRecurrence.lean VERIFIED and Bautin.lean CONDITIONAL.
Verified on disk: `p30_sound` (coefficientwise over Fin 30, bridging to the
polynomial identity), no `sorry`, no cited axiom in BautinRecurrence.lean;
Bautin.lean rests only on `Cited` axioms for Bautin 1952. The four facts I
recorded so the run does not undo them:

1. **One file per kernel run** — no second-module import; data inline in a
   `Generated` namespace carrying no theorem. `Lib/Generated/P30Data.lean`
   stays as provenance only.
2. **`decide` over an MvPolynomial equality does not reduce** (Finsupp
   equality); the check is coefficientwise over Fin 30 and `p30_sound` proves
   the bridge.
3. **MvPolynomial is not a division ring** — the degree-4 obstruction is
   `L4num` (factor in the name).
4. **The quadratic family has six coefficients and no cubic terms** — the old
   a30,a21,b12,b03 normal form is gone.

Updated the stale prose: `research/summaries/lean-statement-bautin-recurrence.md`
rewritten to the verified state; `research/backward/h16-2-h14-3-finite-cyclicity.md`
G-lean-cert marked DISCHARGED (certificate closed), with the new open step named:
a cofactor certificate for "L8 needs a third generator".

### 3. New verified-computational claim: the chart-ring membership facts

From the two captures (`bautin_focal_values.captured.txt`,
`membership.captured.txt`), the exact Gröbner results over Q in the five-
coefficient chart ring are:

- L8 ∉ ⟨L4,L6⟩ (9-monomial remainder) — **three generators genuinely needed**
  in the chart ring; L6 ∉ ⟨L4⟩.
- **L10 ∉ ⟨L4,L6,L8⟩ (38-monomial), L12 ∉ ⟨L4,L6,L8⟩ (110-monomial)** — the
  Bautin-trick closure step "the next focal value lies in the ideal of the
  earlier ones" fails at L10 and L12 in this chart. This is a finding bearing
  on Bautin finite generation for this chart.
- Sanity guards pass: 8L4 = AC+CD+2DF−EF; 192L6+P30 = 0 (30 monomials).

Filed as claim `bautin-chart-membership-l8-l10-l12` (status: checked,
search-frame: exact sympy over QQ, lex, degrees 4..12, with the explicit
warning that the chart ring is NOT the full six-coefficient quadratic family and
must not be quoted as M(2)=3 evidence either way).

## Contradictions flagged

- The entailment ledger now shows the critical tension: `h16-dulac-proof-contested`
  recorded as contradicting `h16-dulac-finiteness-theorem`, propagated through
  the three claims that rest on the contested proof. This is the library's most
  important structural fact: **Dulac's finiteness theorem is held as a theorem
  but its Ilyashenko-approach proof is contested (peer-reviewed, 2025)**; the
  n=2 pointwise pillar stands independently (Bamón, Romanovskii, Chicone–Shafer).
- Repaired the dangling `contradicts: h16-dulac-finiteness-individual` edge
  (nonexistent id) to the real `h16-dulac-finiteness-theorem`.

## Sources that do not help (and why)

- `rousseau-publications-page` — bibliography only; no mathematics.
- `bamon-quadratic-finite-limit-cycles-pdf` — IHÉS record page; title alone
  anchors the claim.
- `llibre-zhang-lienard-survey-expmath-2017.uab` — UAB record page; the full
  postprint is the anchor.
- `demaesschalck-rebollo-torregrosa-fake-saddle-2015` — UAB record page; the
  postprint is the anchor.
- `demaesschalck-rebollo-torregrosa-fake-saddle-2014` — DOI redirect stub
  (110 bytes); superseded by the postprint.
- `yakovenko-quantitative-ode-*` — landing pages only; the 78-page course body
  is not held.
- `oeis_a019274` — checked and NOT a match for the L_d monomial counts; the
  counts are explained by the recurrence, not by any OEIS closed form.
- `liang-torregrosa` — paywalled preview; abstract-level only, exact numbers
  must not be cited beyond the abstract.
- `landing-pages-inventory` — the record of which files are landing pages; kept
  so nobody re-reads them expecting content.

## Gaps still open (unchanged)

- The complete DRR 121-graphics ledger (DRR 1994 paywalled; no post-2020
  consolidation exists) — request `dumortier-roussarie-rousseau-9c4f` and
  `complete-current-ledger-cb3d` stay open. Library's honest statement: ≥ 89 of
  121 fully closed (88 RSZ verbatim + I¹₁₄ RR), (I⁶b¹),(H¹³₃),(DI₂b)
  boundary-sets-only, (H³₁₄) open with Lu 2026 preprint claiming it (algebraic
  core verified here), ≥ 11 degenerate open (Shan 2013).
- Lu 2026's full claim unverified (human-proof remainder); two bundle scripts
  still not held.
- The L10/L12 non-membership cofactor certificate (next Lean task).

## Memory server

`remember_memory` was attempted twice this pass and refused both times (health
check timeout — "the memory server cannot index right now"). All durable
findings are persisted in workspace files (claims ledger, summaries, backward
files) per the workspace rule; store to Cognee when it recovers.