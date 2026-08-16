# Tasks

- [x] Read problem.md, GOAL.md, AGENTS.md — the run targets the open 3x3 magic square of squares conjecture; deliverable is a genuine partial result, not a claim of resolution.
- [x] tool_builder: build code/lib/mss.py + code/check_near_misses.py (exact
      arithmetic): verifier, worked examples rerun fresh, both 7-square
      near-misses constructed+verified, incidence rank, (c,u,v) extraction,
      Pythagorean pairs; write code/out/near_misses.json with provenance for
      Sallows LS1 and Bremner's magic square.
- [x] tool_builder: exact-integer verification of the completed Robertson
      reduction on Bremner's 7-square witness — code/robertson_reduction_check.py
      (runs under sage), output code/out/robertson_reduction_check.txt, exit 0.
      All 8 sums 541875; a=425², b=41496, c=138600; 2 of 3 main-diagonal
      x-coords in 2E(Q) (139129, 180625), 222121 not (X and X+c not squares);
      doubling formula verified symbolically + on a rational point + Sage 2P;
      rank(E: y²=x³−19209960000x)=2 by mwrank 2-descent with
      generators [−88200,315000] and regulator 6.9103524178015 (cross-checked
      via E.rank/algorithm='all'/standalone mwrank; all 8 division preimages
      rational, quartics factor exactly for the two membership values, no
      rational root for X=222121); converse grid (4) from the AP is the
      witness transpose, all 8 sums 3a, non-squares exactly {360721,222121} —
      the witness is one doubled point short of an MSS.
- [x] Re-download Garcia-Fritz-Pasten and Rome-Yamagishi from PDF endpoints
      (both were abstract-page wrappers; now 21KB and 40KB — real papers).
- [x] Re-download Wu 2103.01784 from PDF endpoint (was 6.6KB abstract-page
      wrapper; now 78KB, real paper with theorems).
- [x] **Ferreira 1506.06621 — handle per steer directive 6.** Error located at
      (46)→(47); substituting z2 = m−√(m²−2nw−w²) into (46) yields the tautology
      0=0, not the paper's (47). Verified by sympy. Claim
      `ferreira-15060621-proof-invalid` in CLAIMS.md, status: checked.
- [x] **Run check_ferreira_proof.py.** Capture at
      `code/out/check_ferreira_proof.captured.txt`, EXIT_CODE=0, sympy agrees.
- [x] **Audited this run's own code for the Ferreira anti-pattern.** None found.
- [x] **Re-download Hulse et al. and Wolird from arXiv PDF endpoints.**
      Done; real papers on disk.
- [x] **Record the witness_padic_falsification result.** Claims
      `phi-padic-no-obstruction`, `phi-padic-consistent-with-witnesses`,
      `phi-padic-residue-closure` all `status: checked` in CLAIMS.md.
- [x] **Verify the parallel library.** PASS.
- [x] **Parallelise `phi_padic_closure_all.py`.** PASS.
- [x] **Run the remaining six p-adic/modular programs.** All exit 0, no
      obstruction found. Frontier closed as a proof route.
- [x] **FALSIFY EVERY P-ADIC/MODULAR OBSTRUCTION.** Both witnesses verified.
- [x] **k3_surface_checks.py exact rewrite.** DONE; S(Q) nonempty, Brauer-Manin
      cannot prove S(Q)=∅.
- [x] **Gathering phase OVER.** No further downloads without a new stated gap.
- [x] **Run the four Pell programs.** Captures on disk; claim
      `phi-suprema-are-pell-pairs` in CLAIMS.md, status: checked. CORRECTION:
      argmax NOT unique; Pell pairs always among the maximisers.
- [x] **side_census.py RUN by operator at M=400 — docstring hypothesis REFUTED.**
      Both=0 finding: 1−(q1+q2) rational square 325 times, 1+(q1+q2) 66 times,
      BOTH = 0. Claim `phi-pair-sides-never-both-square` in CLAIMS.md.
- [x] **MIRROR ALL code/out/ claim blocks into research/notes/ (directive 22).**
      Created four note files carrying the 7 claims that were invisible to the
      deriver:
      - `research/notes/phi-pair-sides-census.md` — `phi-pair-sides-both-square-zero-through-M800`,
        `phi-pair-sides-never-both-square`
      - `research/notes/phi-universal-set-claims.md` — `phi-universal-set`,
        `phi-no-triple-m400`
      - `research/notes/padic-witness-falsification.md` — `witness-padic-falsification`
      - `research/notes/phi-pell-records.md` — `phi-suprema-are-pell-pairs`,
        `phi-pell-record`
      All seven now appear in `search_claims` output with `research/notes/` anchor
      paths. The remaining `code/out/` claims already had dual visibility.
      `phi-pair-sides-both-square-zero-through-M800` (2.5B pairs, both=0) is
      now in the ledger.

### Kamel–Sadek status (directive 22)

The 6093-byte file `kamel-sadek-consecutive-squares-elliptic-2016.full.md` is
the arXiv abstract page and has no theorems — expected. The 26208-byte file
`kamel-sadek-consecutive-squares-elliptic-2016-body.full.md` IS the full HTML
paper body with Theorem 3.3, Corollary 3.4, Proposition 2.2, and all proofs.
The claim `kamel-sadek-consecutive-squares-rank-5` correctly anchors through
`research/summaries/kamel-sadek-consecutive-squares-elliptic-2016-body.md` to
the body file. Status `proved` is correct: peer-reviewed journal (Glasnik
Matematicki 52/1, 2017). No change needed.

### Captured-output count (directive 22)

`commands.log` appeared (132149 bytes — was missing in directive 17), so the
count went up by at least one. Without a before-state I cannot identify which
individual `.captured.txt` disappeared.
- [x] **Five phi_triple_variety programs now run.** verify_two_side_equiv (exit 0),
      verify_triple_square (exit 0), verify_prefilter (exit 0), benchmark (exit 0),
      verify_pell_symbolic (exit 0). All captured in code/out/.
- [x] **magic_variety_check.py RUN.** Exit 0, captured. X = P² ⊂ P⁸, rank 7
      incidence / rank 6 differences, kernel dim 3. Claim
      `magic-variety-is-surface-no-lines` REFUTED for the linear variety (P² is
      saturated with lines); the no-lines/256-singular-points claim refers to the
      quadric-cut variety, a different object.
- [x] **side_census M=800 COMPLETE RUN.** Parallel `side_census_par.py` over 26
      workers finished the full outer index; captured at
      code/out/side_census_M800_complete.captured.txt, checkpoint
      code/out/side_census_stages_M800.jsonl. **COMPLETE**: 2,509,516,913 pairs,
      minus=718 plus=150 both=0. The earlier 17.7%-partial capture
      (6/11/0) is superseded and must not be quoted. Claim
      `phi-pair-sides-both-square-zero-through-M800`, status: checked, in
      CLAIMS.md. Serial-vs-parallel agreement verified at M=100 and M=200;
      example witnesses independently re-verified via lib.phi.in_phi.
- [x] **ratio_search M=700 RUN.** Budget-exhausted at i=27861/99407 (28.0%).
      Captured; no triple through the covered range.

---

- [x] **source-quality sweep (directive 21).** Seven arXiv abstract landing pages under
      20KB in research/sources/; every one has a real-paper sibling on disk. Zero claims
      above `catalogued` rest on landing pages. kamel-sadek-consecutive-squares-rank-5
      is `proved` from the 26KB body file (Corollary 3.4 + MAGMA verification + Glasnik
      Matematički publication), not the 6KB vestigial abstract. concordant-forms-iff-ell-torsion-order-2
      is `proved` from the 49KB Selder-Spindler HTML (Theorem 2.2). No status changes needed.
      The seven vestigial files are harmless — no claim is mis-statused by them — but are
      redundant clutter. Delete any that are byte-identical to arXiv abstract pages
      (they all are) when the operator confirms.

## BLOCKING — must complete before any new approach

### EXA_SEARCH — STOPPED (directive 17)

exa_search is at 122 (was 99 two directives ago). The frontier is 442 with
365 unworked. Twenty-three searches changed nothing. This is a fact about the
search, not about the literature: further downloads will not change a claim.
**No more exa_search calls.** No new sources fetched without a stated gap in
REQUESTS.md.

### Proved-count drift (directive 17)

Proved went 20→17 while checked went 15→17 and asserted 19→20. This was a
deliberate re-classification (not lost claims): `bremner-conjecture-proved`,
`n-by-n-mss-exist-for-n-ge-4`, and `dgh-uniform-mordell-lang-curves` were
demoted because `holds-here: no` — they are true theorems proved by their
authors, but do not apply to THIS problem. The shift 20→17 is a tightening
of the holds-here/proved intersection. **NOT a bug; a correction.**

### Ledger (directive 19)

Proved 17→19, captured 49→51, code flat at 71, zero failures. Keep that shape.

---

## ACTIVE — directive 20 (M=800 complete census now in CLAIMS.md)

### Concordant-forms elliptic curve on the M=800 both=0 witnesses (directive 19 + 20)

Sage is NOT available. Use Pari/GP (`ellrank`/`elltors`), or `mwrank` if present,
and say in the capture which tool and which version produced each rank.

Grep the MINUS and PLUS lines from `code/out/side_census_M800_complete.captured.txt`
to extract the 718 minus-witness (q1, q2) pairs and the 150 plus-witness (q1, q2)
pairs. For each pair, s = q1+q2. The concordant condition "both 1−s and 1+s are
rational squares" ⇔ E_{M,N}: y² = x(x+M)(x+N) has a point of order > 2, where
M,N derive from s via the dictionary in `concordant-forms-iff-ell-torsion-order-2`.

- [ ] **Extract witnesses.** Write a script that parses the capture, extracts
      every MINUS and PLUS line as (q1, q2), deduplicates if needed, and writes
      `code/out/concordant_witnesses_M800.json`.
- [ ] **Form E_{M,N} for each of the 150 plus-witnesses and the 718 minus-witnesses.**
      Compute rank and torsion for each curve using Pari/GP (`ellrank` + `elltors`)
      or `mwrank`. The question: do the minus-witnesses and plus-witnesses split
      cleanly by rank or by torsion? That is the only mechanism left after
      `hilbert-symbol-of-two-squares-trivially-split` ruled out every Q-level
      local obstruction. both=0 over 2.5 billion pairs is a global statement or
      it is nothing.
      Write to `code/out/concordant_witness_curves_M800.captured.txt`.
- [ ] **State any split found as a claim.** A rank you cannot name the provenance
      of is asserted.

### Both=0 claim — already in CLAIMS.md, verify

- [x] Claim `phi-pair-sides-both-square-zero-through-M800` entered, status: checked.
      **Supersedes the M=400 `phi-pair-sides-never-both-square`** (156988030 pairs,
      325 minus, 66 plus) which is now obsolete. A completed census is a different
      object from a partial sweep and must not be filed beside one.

### Structural work — the run's deliverable

- [ ] **WRITE THE CONDITIONAL RESULT AS A CLAIM.**
      Assumption: uniform boundedness of ranks of E/Q → 3×3 MSS existence reduces
      to a finite computation. Specialise to E: y² = x(x²−c²), cite Robertson→GFP
      Theorem 1.2. Write to `code/out/conditional_reduction_claim.md`.

- [ ] **BOUND THE HMS CONSTANT C, OR RECORD THE PRECISE OBSTRUCTION.**
      The claim block now names DP07, BZ, and JS as the three ingredients.
      Check each source for an explicit value. If none extractable, record the
      dependency chain and why each constant is not computed. Write to
      `code/out/hms_constant_bound.md`.

## After the blocking section is cleared

- [ ] scholar: claim-block HMS 2026 from the full HTML text (132KB on disk).
- [ ] scholar: claim-block Hulse et al. (arXiv:2007.14324, 68KB).
- [ ] scholar: claim-block Wolird (arXiv:2310.12164, 11KB).
- [ ] research: write research/ROOT.md.
- [ ] Establish ~1 structural impossibility lemma and run it against witness set.
- [ ] Formalise the Robertson reduction and GFP bound in Lean.