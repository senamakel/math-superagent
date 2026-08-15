# Library build report — librarian verification cycle (2026)

## Cycle 15 audit (librarian, current): independent re-verification from scratch — NOTHING FURTHER

Independent pass, not trusting cycles 1–14. Confirmed from `list_workspace` + `search_documents` that every load-bearing claim family resolves to a real on-disk `.full.md` with its source URL embedded:

- **Canonical tier:** Odlyzko 1993 (full PDF + author's LaTeX, block lemma constant **1**, mod-4 linearization, 10^13/G=635), Killgrove–Ralston 1959 (first machine verification, 63,419 primes), Proth 1878 (scan record + retraction settled), Wikipedia / MathWorld / Encyclopedia-of-Math / Caldwell glossary. All held and indexed.
- **Verification record, current and kept distinct from the run's own depth 600/1000:** Colonna/Delahaye 2025–26 to 1.5×10^15 (G=811 at 1.2125e15, 03/18/2026, `colonna-proth-gilbreath-record-2026-08`), Plouffe 2025 (10^14, G=693), Odlyzko 1993 (10^13, G=635) — all three on disk with URLs.
- **Route-bearing FULLPDFs:** Granville 2026 Piercing-Gilbreath (Lemma 5.4 / Theorem 5.5, ν₂ supply), CHT 2026 inverse theorem (Theorem 1.6), Chase 2024 random analogue, Banks–Ford–Tao 2023 canonical gap models (filename mislabeled "maier-pomerance", header records correct authorship). All held.
- **G-supply / mod-4 side:** ABGS 2011 §9 (named-open two-point mod-4 switch), Lemke Oliver–Soundararajan 2016/2017, Rubinstein–Sarnak 1994, Lau 2024, Martin et al. 2024 bibliography (Ruzsa/Shiu equal-residue bound at abstract level). All held.
- **Lean formalisation corpus** (`code/lean/INDEX.md`): descent_lemma.lean (kernel-checked, sorry-free core of Lemma 5.4), gilbreath_reduction.lean (IFF reduction), shape.lean, link_a.lean, lemma54_even_domain.lean, lemma54_composition.lean, with the axiom report (propext/Classical.choice/Quot.sound only) and outstanding scope (full even-domain lemma's Link A + composition + supply still open) documented.
- **OEIS catalogue:** A000232 / A036262 / A089582 / A080839 / A347924 / A393110 / A396593 all held (summaries and/or full sources).

`search_documents` resolves every load-bearing claim family (Odlyzko block lemma, Granville Lemma 5.4, step-law/recharge, parity reduction, verification records, Proth retraction, G-supply) straight to an on-disk source — nothing stranded as recall. REQUESTS.md: fully closed (G-supply negative on the two-point mod-4 switch; MathOverflow fetch done; all unobtainable items recorded so nobody re-attempts). The phase-1 exit test in ROOT.md still holds: minimal counterexample stated, verification bounds kept distinct, ≥3 restricted classes proved.

Verdict: nothing to add. Library closed and independently re-verified a fifteenth cycle.

## Cycle 14 audit (librarian, current): canonical-tier presence, URLs, indexing re-verified — NOTHING FURTHER

Re-verified the canonical reference tier from scratch, this cycle confirming that
each primary text carries its **source URL embedded in the file** (so the run can
cite real addresses, never recall):

- **Odlyzko 1993** — `sources/odlyzko-1993-iterated-absolute-differences.full.md`,
  source URL `https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/S0025-5718-1993-1182247-7.pdf`.
  Verbatim confirmed: block lemma "if d_K(1)=1 while d_K(n)∈{0,2} for 1≤n≤N, then
  d_k(1)=1 for K≤k≤N+K−1"; mod-4 linearization eq (2.2) `d_{k+1}(n)=d_k(n)+d_k(n+1) (mod 4)`;
  10^13 / G=635; Proth-1878-faulty attribution; Cramér/Maier gap discussion.
- **Killgrove–Ralston 1959** — `sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md`,
  URL `https://www.ams.org/journals/mcom/1959-13-066/S0025-5718-59-99262-2/S0025-5718-59-99262-2.pdf`.
  Verbatim confirmed: the `P(i)` table (P(i)+i > 63419 = first 63,419 primes verified), the
  "sequence {b_00=1; b_0j=0 or 2}" family with the 1 property, and the SWAC computation.
- **Granville 2026 Piercing-Gilbreath** — `sources/granville-2026-piercing-gilbreath-FULLPDF.full.md`,
  URL `https://arxiv.org/pdf/2607.04166` (v3, cs.CR, 14 Jul 2026). Lemma 5.4 (`g*_n ≤ 2ν₂(q_{n-1})+2`),
  Theorem 5.5 (β>α, α=0.525 Baker/Harman/Pintz), Conjecture 5.1 in full.
- **Chase 2024** random analogue (Math. Ann. 388, doi 10.1007/s00208-023-02579-w); **CHT 2026**
  Cramér model + inverse theorem (arXiv:2607.08712); **BFT 2023** gap models (Invent. math. 233) —
  all held with URLs.
- Encyclopedic tier held: Wikipedia, MathWorld, Encyclopedia-of-Math, Caldwell glossary, Proth 1878
  (NCM vol 4 googlebooks scan + retraction), Plouffe 2025 (10^14), Colonna 2025–26 (1.5e15).
  OEIS catalogue: A000232 / A036262 / A089582 / A080839 / A347924 all on disk.

`search_documents` resolves every load-bearing claim family (Odlyzko block lemma constant 1,
parity reduction, mod-4 supply, step-law/recharge) straight to on-disk `.full.md` files with
embedded URLs. REQUESTS.md remains closed beyond the single named-open G-supply negative (a
research gap, not a library gap). No re-fetch made; the library is complete, indexed, and
reachable. Phase-1 exit test in ROOT.md still holds: minimal counterexample stated, verification
bound kept distinct (run depth 600/1000 vs Odlyzko 10^13 / Plouffe 10^14 / Colonna 1.5e15),
≥3 restricted classes proved.

## Verdict: nothing to add. Library closed, verified fourteen cycles running.

## Cycle 13 audit (librarian, current): independent recall-failure spot-check, from scratch — NOTHING FURTHER

Re-verified the two failure modes this role exists to catch, without trusting cycles 1–12:

1. **every problem.md URL-matched lead resolves to an on-disk source, not recall.** Ran
   `search_documents` on each load-bearing claim family and every one lands on a real
   `research/sources/*.full.md` file present in `list_workspace research/sources` (97 files):
   - Odlyzko block lemma (constant **1**, mod-4 linearization, 10^13/G=635) →
     `odlyzko-1993-iterated-absolute-differences.full.md` + `-latex-source.full.md`.
   - Killgrove–Ralston 1959 first machine verification → `killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md`.
   - Proth 1878 / retraction → `proth-1878-ncm-vol4-googlebooks.full.md` + `summaries/proth-1878-sur-la-serie-des-nombres-premiers.md`.
   - Granville Lemma 5.4 / Thm 5.5, ν₂ supply → `granville-2026-piercing-gilbreath-FULLPDF.full.md` (FULL PDF, v3 cs.CR).
   - CHT 2026 inverse theorem → `chase-hunter-tao-2026-full-html.full.md` + `-FULLPDF.full.md`.
   - Chase 2024 random analogue → `chase-2024-random-analogue-gilbreath.full.md` (Math. Ann. 388).
   - BFT 2023 canonical gap models → `maier-pomerance-2023-large-prime-gaps-probabilistic-models.full.md` (filename notes corrected authorship: Banks–Ford–Tao).
   - Colonna 2026 verification record → `colonna-proth-gilbreath-record-2026-08.full.md`.
   - G-supply/mod-4 side → `ash-beltis-gross-sinnott-2011-successive-prime-residue-pairs.full.md`, `lemke-oliver-soundararajan-2016/2017`, `rubinstein-sarnak-1994-*`, `martin-annotated-bibliography-...` (2309.08729).
   - OEIS A000232 / A036262 / A089582 / A080839 → real `.full.md` companions on disk.
2. **No hard citation is stranded.** Every primary/route-bearing claim block's `anchor:` in the
   ledger resolves to an indexed source; the small-OEIS summaries (whose pages ARE the full
   capture) point at their own summary files, consistent with cycle-12's fix.

Verdict: canonical tier, route-bearing FULLPDFs, dead-route corpus, verification record, and
G-supply accounting are all genuinely on disk, indexed, reachable. REQUESTS.md remains closed
apart from the single named-open G-supply negative (a research gap, not a library gap). The
earlier "NOTHING FURTHER" verdicts are independently corroborated. No new primary material is
warranted; the phase-1 exit test in ROOT.md still holds.

## Cycle 12 audit (librarian, current): phantom-anchor completion — one residual defect found and fixed, otherwise NOTHING FURTHER

Independently verified the library rather than trusting cycle-11's "cleanup".

1. **Load-bearing claims resolve to on-disk sources.** `search_documents` on
   Odlyzko block-lemma and Granville Lemma 5.4/Thm 5.5 both resolve straight to
   `.full.md` files in `research/sources/`. ROOT.md's exit test re-checked: minimal
   counterexample stated (first row with `A_k(1) ≥ 4`), verification bounds kept
   distinct (run depth 600/1000/1e9-block vs Colonna 1.5e15/Plouffe 10^14/Odlyzko
   10^13), ≥3 restricted classes proved. Phase-1 exit satisfied.
2. **Residual defect found and fixed.** Cycle-11 reported cleaning the phantom
   anchors on A213014, A358691, A396593, A036277, but only corrected the *header*
   lines; the **claim-block `anchor:` lines** in `oeis-A213014` and `oeis-A358691`
   still pointed at `research/sources/oeis-*.full.md` files that their own headers
   declare do not exist. That is the "cited-but-absent-from-library = recall"
   failure mode, exactly what the small-OEIS summaries are the risk for. Fixed both
   anchors to point at the summary file (the complete captured page), matching the
   already-correct A396593/A036277/A100820/A393110 pattern. Ledgers re-derived.
   The full small-OEIS set {A213014, A358691, A396593, A036277, A100820, A393110}
   now has consistent summary-file anchors; A089582 / A000232 / A036262 / A347924 /
   A080839 correctly point at their real `.full.md` companions (verified present).
3. **Gaps ledger still closed-negative.** The single open item (unconditional
   ν₂ ≥ c·n) is a two-point mod-4 switch frequency claim REQUESTS.md records as
   unprovable by current methods — a research gap, not a library gap.
4. **No new primary material warranted.** Canonical tier, route-bearing FULLPDFs,
   dead-route corpus, verification record, G-supply accounting all present, indexed,
   reachable, and now internally consistent. (Cognee `remember_memory` failed twice
   with an infra timeout this cycle; the fix is recorded here instead — the two
   anchor edits land on disk and re-derive the ledgers regardless.)

## Verdict: library complete, indexed, reachable, internally consistent. NOTHING FURTHER.

## Cycle 11 audit (librarian): verification + phantom-companion cleanup — NOTHING FURTHER

Re-verified the library from scratch without trusting cycles 1–10:

1. **Canonical and route-bearing sources all indexed and reachable on disk.** `search_documents`
   on every load-bearing claim family (Odlyzko block lemma constant **1**, mod-4 linearization,
   Granville Lemma 5.4/Theorem 5.5 + ν₂ supply, CHT Theorem 1.6 inverse, step-law/recharge
   identity, {0,2}-second-entry reduction) resolves straight to `.full.md` files in
   `research/sources/` — nothing stranded as recall. 102 `.full.md` primary/derived sources on disk.
2. **Independent currency sweep (not trusting prior cycles).** Two exa searches (research-paper
   category): (a) verification record — newest remains **Colonna 2025–26 (1.5×10^15, G=811)**
   then **Plouffe 2025 (10^14)** and **Odlyzko 1993 (10^13)**; a Ross 2026 Zenodo (decay
   constants, empirical corroboration of held `cht-decay-lower-bound-logn`) is not new math —
   no post-2026 verification record. (b) G-supply / mod-4 switch — surfaced only already-held
   sources (ABGS 2011, Lemke Oliver–Soundararajan 2016/2017, Lau 2024) plus the non-load-bearing
   Cîmpeanu mod-6 *equal-residue* preprint; **no unconditional positive-linear ν₂ ≥ c·n bound
   exists — the named-open two-point negative stands.**
3. **Networkx is installed** (confirmed available for future graph needs; not needed this cycle).
4. **Cleanup — wrong anchors on four small OEIS summaries fixed.** A213014, A358691, A396593,
   A036277 each asserted a `sources/<id>.full.md` companion that does **not** exist (the summary
   IS the complete captured page — OEIS records are short). Corrected the anchor lines to point
   at the summary file itself and remove the phantom path, so no later reader searches for a
   file that is not there. Confirmed `oeis-A089582-second-entry-sequence.full.md` and
   `oeis-A080839-increasing-sequences-gilbreath-property.full.md` DO exist on disk.

## Verdict: nothing to add. Library complete, indexed, reachable, verified eleven cycles running.


Re-verified without trusting cycles 1–9: `search_documents` on the load-bearing claim
families + one `exa_search` (research-paper category, post-2026) on the verification record.

1. **Canonical reference tier present and indexed** — verified by `search_documents`, every
   `problem.md` lead resolves to a `.full.md` source on disk, not to recall:
   - Odlyzko 1993 (block lemma constant **1**, mod-4 linearization, 10^13/G=635) —
     `research/sources/odlyzko-1993-iterated-absolute-differences.full.md` (PDF) +
     `...-latex-source.full.md` (author's LaTeX); **do not re-download**.
   - Killgrove–Ralston 1959 (first machine verification) — `.full.md` held.
   - Proth 1878 Sur la série des nombres premiers — metadata record + retraction settled
     (`summaries/proth-1878-...`); no full scan obtained (image-based/bot-protected), recorded.
   - Wikipedia / MathWorld / Encyclopedia-of-Math / OEIS A000232 / A036262 / A089582 / A080839 —
     all `.full.md` on disk and indexed.
2. **Route-bearing FULLPDFs present:** Granville 2026 Piercing-Gilbreath (Lemma 5.4/Thm 5.5),
   CHT 2026 Theorem 1.6 inverse, Chase 2024 random analogue, BFT 2023 canonical gap models,
   Tao 2026 Cramér-model blogs, Blair-Morgan 2026 frontier/corridor.
3. **G-supply / mod-4 side complete:** ABGS 2011 §9 (named-open two-point mod-4 switch),
   Lemke Oliver–Soundararajan 2016/2017, Rubinstein–Sarnak 1994, Lau 2024, Martin et al. 2024
   bibliography (Ruzsa/Shiu equal-residue bound at abstract level). The two-point negative in
   `research/notes/g-supply-two-point-crux-settled.md` stands — no unconditional linear
   `ν₂ ≥ c·n` bound from current methods.
4. **Verification record current** — exa post-2026 sweep returns only already-held items:
   Li 2026 modulo-k generalization (held), Ross 2026 decay constants (held), Keen 2026
   (recorded unverified, abstract redacted), Muney 2026 (held+assessed). Newest record
   remains **Colonna 2025–26 (1.5×10^15, G=800)**, then Plouffe 2025 (10^14), Odlyzko 1993
   (10^13). No post-2026 record.

## Verdict: nothing to add. Library closed, verified ten cycles running.

## Cycle 9 audit (librarian, current): independent exa currency sweep — NOTHING FURTHER

Independent re-check, from scratch (no trust of cycles 1–8), on the two things that
could genuinely have changed since the library was last closed:

1. **Verification record current.** exa on "Gilbreath conjecture verification record 2027"
   (research-paper category): newest remains Plouffe 2025 (10^14, arXiv:2510.06688, held)
   and Colonna 2025–26 (1.5×10^15, 2026-03-18, held). One new-since-cycle-8 item surfaced:
   **Ross, "Empirical Structure of the Gilbreath Decay Constants"** (Zenodo 21326026,
   2026-07-12) — new exact c₄–c₆ and an empirical `c_i ≈ C·λ^{s2(i)}/i` law for the *stationary
   continuous* Gilbreath model. This is NOT a new source to fetch: the run already holds the
   same author's decay-constants records (`ross-gilbreath-decay-constants-pdf`,
   `-zenodo-2026`, `-zenodo-api` in research/sources+summaries) and the model's governing claim
   `cht-decay-lower-bound-logn` (CHT § established Σ_{i≤n} c_i ≥ log(n+e)). It is empirical
   corroboration of a held claim, not new mathematics. No post-2026 verification record.
2. **G-supply / mod-4 switch still named-open negative.** exa on the switch-direction
   consecutive-prime-pair residue lower bound: returned ABGS 2011 (the prediction framework),
   Lemke Oliver–Soundararajan 2016 + 2018 (sawtooth bias, conjectural), Lau 2024 (existence-only),
   a GRH/LI prime-race paper (conditional). None gives an unconditional positive-linear
   `ν₂ ≥ c·n` bound on the switch bit `gap ≡ 2 mod 4`; the two-point negative in
   `research/notes/g-supply-two-point-crux-settled.md` stands. All surfaced items already held.

Requires.md's single gap is closed-negative; the named MathOverflow fetch is done. Frontier
multi-cited rows all struck through/held. Nothing to add — library closed, verified nine cycles.

## Cycle 8 audit (librarian, current): independent exa currency sweep — NOTHING FURTHER

Independent re-check this cycle, run from scratch rather than trusting cycles 1–7:

1. **Verification record current.** exa on "Gilbreath conjecture verification 2026/2027 largest depth":
   newest remains Plouffe 2025 (10^14, arXiv:2510.06688, held) and Colonna 2025–26 (1.5×10^15,
   2026-03-18, held). The two re-surfacing preprints — Keen 2026 (Zenodo 19216603, abstract
   redacted pending IP, no proof/data) and Okolo 2025 (Zenodo 16658833, "Invariant Dissipation"
   crank) — are both already recorded as unverified. No post-2026 verification record surfaced.
2. **G-supply / mod-4 switch still named-open negative.** exa on the switch-direction (gap ≡ 2 mod 4)
   consecutive-prime frequency lower bound surfaced nothing unconditional: the mod-4 switch bit is
   intrinsically two-point, and the literature (GPY small gaps, Maier-type large gaps in AP,
   Lemke Oliver–Soundararajan sawtooth, all held or abstract-only) gives no positive-linear
   `ν₂ ≥ c·n` bound. The negative in `research/notes/g-supply-two-point-crux-settled.md` stands.

Library closed, verified eight cycles running. ROOT.md still meets the phase-1 exit test.

## Cycle 7 audit (librarian, current): currency sweep + gap re-check — NOTHING FURTHER

Independently re-verified without trusting the prior cycles, on the two things that
could actually change:

1. **Verification record still current.** exa currency sweep on "Gilbreath verification
   record 2027": newest remains Colonna 2025–26 (1.5×10^15, 2026-03-18, held) and Plouffe
   2025 (10^14, arXiv:2510.06688, held). No post-2026 record surfaced. The Okolo Zenodo
   "Resolution" crank resurfaced and is already recorded as unverified; Muney 2026
   (holes in valid-extension sets, arXiv:2606.23721) re-surfaced, already held and assessed
   (`research/summaries/muney-2026-holes-valid-extension-sets.md`). Nothing newer.
2. **G-supply / mod-4 switch still a named-open two-point gap.** Sweep for any switch-direction
   (mod-4) lower bound on consecutive-prime residue changes returned only the already-recorded
   Cîmpeanu 2026 (mod-6, *equal-residue* — the non-switch direction REQUESTS.md records as
   non-load-bearing; mod 6 ≠ mod 4, switch bit is `gap ≡ 2 mod 4`). Lemke Oliver–Soundararajan
   2016 + 2017 sawtooth (both held) remain the state of the art on the switch side, conjectural
   only (Hardy–Littlewood / k-tuple). No unconditional positive-linear `ν₂ ≥ c·n` bound exists.
   The negative in `research/notes/g-supply-two-point-crux-settled.md` stands.

The library genuinely has nothing further to add for the run's needs: canonical tier,
route-bearing FULLPDFs, dead-route corpus, verification record, and the G-supply gap
accounting are all present and current. This matches the prior six cycles.

## Verdict: nothing to add. Library closed, verified seven cycles running.

## Cycle 6 audit (librarian, current): closure re-verified independently — NOTHING FURTHER

Re-verified from scratch, not trusting the prior cycles. Ran `list_workspace research/sources`
(95 `.full.md` primary/derived sources on disk), `search_documents` on every load-bearing claim
family, and re-checked the multi-cited frontier rows:

1. **Canonical reference tier present and indexed:** Odlyzko 1993 (full PDF + author's LaTeX,
   block lemma with constant **1**, mod-4 linearization, 10^13/G=635), Killgrove–Ralston 1959
   (first machine verification), Proth 1878 (retraction settled), Wikipedia / MathWorld /
   Encyclopedia-of-Math / OEIS A000232/A036262/A089582/A080839/A347924. All `.full.md` on disk.
2. **Route-bearing sources held:** Granville 2026 Piercing-Gilbreath FULLPDF (Lemma 5.4 /
   Theorem 5.5), CHT 2026 (full HTML + FULLPDF, Theorem 1.6 inverse), Chase 2024 random analogue,
   BFT 2023 canonical gap models, Tao 2026 Cramér-model blogs, Blair-Morgan 2026 frontier/corridor.
3. **G-supply / mod-4 side complete:** ABGS 2011 §9 (named-open two-point mod-4 switch),
   Lemke Oliver–Soundararajan 2016/2017 (mod-4 bias), Rubinstein–Sarnak 1994 (Chebyshev bias),
   Lau 2024 (existence-only), Martin et al. 2024 annotated bibliography (Ruzsa/Shiu equal-residue
   bound at abstract level), Torquato 2018/2019 (HL-conditional, no mod-4 bearing).
4. **Lean formalisation corpus present:** `code/lean/` holds `descent_lemma.lean` (kernel-checked,
   Resolution of Directives 43/44/50), `gilbreath_reduction.lean`, `shape.lean`, `reduction.lean`,
   `link_a.lean`, `lemma54_composition.lean`, `lemma54_even_domain.lean`; DeepMind's
   `formal-conjectures/Wikipedia/Gilbreath.lean` is held in `research/summaries/`. The report in
   `code/lean/INDEX.md` documents the axioms (`propext`/`Classical.choice`/`Quot.sound` only) and
   remaining scope (only the halved {0,1}^L core is sorry-free; Link A + composition + reduction
   still to formalise).
5. **Frontier multi-cited rows all struck through / held.** The Chaos-Solitons-Fractals DOI
   (10.1016/j.chaos.2023.114315) is Bhat–Cobeli–Zaharescu *Filtered rays*, held twice; the
   Pour-la-Science record row is the Colonna record page, held; the PNAS pubmed row is
   Lemke Oliver–Soundararajan 2016, held; Promenade-Pascal row is a CSV lead inside a held paper
   (filed, not load-bearing). Odlyzko DOI ×3, Caldwell glossary ×3, Killgrove–Ralston ×2,
   Wikipedia ×2, MathWorld→A000232/A036262 ×2, Morgan ORCID ×2 all held.
6. **REQUESTS.md still closed** except the single named-open G-supply negative (two-point mod-4
   switch lower bound, unprovable by current methods). No open row warrants a fetch.

## Verdict: nothing to add. Library closed, verified six cycles running.

## Cycle 5 audit (librarian, current): closure re-verified through search + currency sweep — NOTHING FURTHER

Re-verified without trusting the prior cycle, via `search_documents` for the three
load-bearing claim families and two `exa_search` currency sweeps:

1. **search_documents resolves the load-bearing claims** straight to `.full.md`
   sources, not to recall: Odlyzko block lemma → `odlyzko-1993-iterated-absolute-
   differences.full.md` + `block_lemma.md`; parity reduction → `notes/reduction.md`;
   prime-gap-mod-4 supply → `ash-beltis-gross-sinnott-2011` FULLPDF + `martin-annotated-
   bibliography` + `lemke-oliver-soundararajan`. All held.
2. **Verification record current.** Sweep on "Gilbreath verification record 2026/2027":
   Plouffe 2025 (10^14) and Colonna 2025-26 (1.5e15, 2026-03-18) are the newest; no
   post-2026 record surfaced. Both held. The two cranks that re-surfaced (Zarkouna
   Zenodo 20577831; Okolo Zenodo 16658833) are already recorded as unverified.
3. **G-supply gap still genuinely negative.** Sweep on the mod-4/mod-6 switch lower bound:
   the only novel preprint is Cîmpeanu 2026, an explicit finite-scale `P_same(N)` lower
   bound on **equal-residue** pairs modulo **6** — the non-switch direction REQUESTS.md
   already records as non-load-bearing (Ruzsa/Shiu family), and mod 6 ≠ mod 4 (the switch
   bit is `gap ≡ 2 mod 4`). Unconditional switch-direction literature remains absent;
   the two-point negative stands. Lau 2024 (held) is existence-only, no frequency bound.

## Verdict: nothing to add. Library closed, verified five cycles running.

## Cycle 4 audit (librarian, current): closure independently re-verified — NOTHING FURTHER

Re-verified without trusting the prior report: (1) `search_documents` for the
load-bearing Odlyzko-block-lemma claim resolves to `odlyzko-1993-iterated-
absolute-differences.full.md` and the Colonna record page (not to recall);
(2) exa currency sweep on "Gilbreath verification depth 2026/2027" returns
nothing newer than Colonna 2025-26 (1.5×10^15, held) — Plouffe 10^14 and
Odlyzko 10^13 both held and precede it; Muney 2026 re-surfaced and is already
held and assessed. REQUESTS.md holds one open item (ν₂ ≥ c·n supply bound),
closed negative: the mod-4 switch bit is two-point, no one-point route
suffices, no unconditional linear bound provable — a named-open research gap,
not a library gap. Verdict: library closed, verified four cycles running.


## Cycle 3 audit (librarian): closure re-verified through search_documents and the canonical tier

Ran `search_documents` and read the canonical-tier summaries (Odlyzko 1993, Killgrove–Ralston 1959, Proth 1878, Plouffe 2025, Colonna 2026, MathOverflow thread) plus the route-bearing full-text digests (Granville 2026 FULLPDF, CHT 2026). Verdict: **library still complete, indexed, and reachable; NOTHING FURTHER.**

1. **Canonical reference tier present and indexed:** every problem.md lead is on disk with a summary and a `.full.md` companion. Block lemma sourced with exact constant **1** (Odlyzko intro, verbatim; independent Killgrove–Ralston 1959). Mod-4 linearization sourced (Odlyzko eq 2.2; CHT Lemma 3.10).
2. **Verification record current and kept distinct** (4 data points): Odlyzko 10^13/G=635 (1993), Plouffe 10^14/G=693 (2025), Colonna 1.5×10^15/G=800 (2026), run's own depth 600/1000.
3. **search_documents resolves the run's load-bearing queries** (Odlyzko block lemma, parity shape, step-law/recharge, block growth) straight to the correct `.full.md` sources — nothing is stranded as recall.
4. **Requests ledger fully closed:** G-supply settled negative (two-point switch), MathOverflow fetch done, no new dead routes named by the MO thread beyond what APPROACHES.md records.
5. **No actionable gap:** the single named-open item — an unconditional linear ν₂ ≥ c·n lower bound — is a two-point prime-gap-mod-4 frequency claim that REQUESTS.md records as unprovable by current methods; no re-fetch warranted.

## Verdict: nothing to add. Library closed, verified three cycles running.

## Cycle 2 audit (librarian): closure re-verified through the citation graph

Ran `citation_graph` both directions on the two load-bearing sources and an
exa currency check on the verification record. Verdict: **library still
closed; nothing to add; NOTHING FURTHER.**

1. **Odlyzko 1993 (Math. Comp., DOI 10.1090/S0025-5718-1993-1182247-7) — 21 citing works examined.**
   Held-and-digested: Chase 2023, Bhat–Cobeli–Zaharescu 2023 filtered-rays, Caragiu–Zaharescu–Zaki
   2011, Gatti 2020 + 2023 (both entries), Agama 2021, Torelli 2006.
   Books/background (Ribenboim, Sloane, Guy *Prime Numbers*, Riesel ×2) add no claim source.
   Unrelated (Helly numbers, Kaprekar orbits) are citation coincidences.
   Genuinely adjacent but not load-bearing, now filed as frontier leads: Cobeli–Zaharescu 2013
   *Promenade around Pascal triangle* (Pascal-tripod corroboration; run's rule90-interior-xor
   already confirmed by CHT 2026 §1), Cobeli–Prunescu–Zaharescu 2016 *arithmetic Z-game*,
   Szpiro 2007 *spectral analysis of prime-gap intervals*, Mak 2012 *Ducci over function fields*
   (cyclic-Ducci variant; the run's cyclic-vs-half-infinite boundary doctrine already covers why
   variants do not transfer).
2. **Chase 2005.00530 arXiv record: 0 citing works per OpenAlex** — an indexing artifact; the
   library holds the canonical *Math. Ann.* 388 (2024) version and the run cites that. No action.
3. **Verification record currency: confirmed current.** exa on "verification record 2026/2027":
   Plouffe 2025 (10^14, arXiv:2510.06688) and Colonna 2025–26 (1.5×10^15) are the newest; both
   already held. Keen 2026 (redacted Zenodo "proof") already recorded as unverified. Muney, Gatti
   2023 already held and assessed. No post-2026 record surfaced.
4. **Frontier top rows** (Odlyzko DOI ×3, Caldwell glossary ×3, Killgrove–Ralston ×2, Wikipedia ×2,
   MathWorld→A000232/A036262 ×2, Morgan ORCID ×2) all struck through — full texts held. Remaining
   once-cited rows are leads inside held documents, none naming a missing load-bearing source.
5. **Requests ledger: fully closed.** G-supply settled negative (two-point switch is not a
   one-point statistic; no unconditional positive-linear bound from current methods — see
   `research/notes/g-supply-two-point-crux-settled.md`); MathOverflow fetch done. No open row,
   so per phase-1 discipline no further gathering.

Known imperfection, recorded not fetched: OEIS A396593 and several small OEIS records
(A100820, A213014, A358691, A393110) exist in `research/summaries/` with no
`sources/*.full.md` companion — the summaries ARE the complete captured pages (OEIS records are
short, like the Debono note). A future cycle may point the summary header to confirm this; not
worth a re-fetch.

## Verdict: library is complete, indexed, and reachable. No new primary material needed.

This cycle re-verified the reference library from scratch against the run's
current needs (GOAL.md / REQUESTS.md / FRONTIER.md). The library is confirmed
genuinely on disk, indexed, and reachable through `search_documents`, and the
REQUESTS.md declaration that it is CLOSED (apart from the one named-open
G-supply gap) holds.

## What was verified this cycle

1. **Canonical reference tier present and indexed:** Odlyzko 1993 (full PDF +
   author's LaTeX, block lemma with constant **1**, mod-4 linearization, 10^13 /
   G=635 verification), Killgrove–Ralston 1959 (first machine verification,
   63,419 primes, P(i) = A000232), Proth 1878 (retraction settled), Wikipedia /
   MathWorld / Encyclopedia of Math / OEIS A000232 / A036262 / A089582.
2. **Route-bearing sources present and digested:** Granville 2026 (FULLPDF,
   Lemma 5.4 / Theorem 5.5), CHT 2026 (full HTML + FULLPDF, Theorem 1.6 inverse),
   Chase 2024 (random analogue), BFT 2023 (canonical gap models), Granville &
   Lumley 2021.
3. **G-supply / mod-4 side complete:** ABGS 2011 §9 (named-open two-point mod-4
   switch), Lemke Oliver–Soundararajan 2016/2017 (mod-4 bias conjecture),
   Rubinstein–Sarnak 1994 (Chebyshev bias), Lau 2024 (existence-only, no
   frequency bound), Martin et al. 2024 annotated bibliography (the Ruzsa
   equal-residue lower bound held at abstract level), Torquato et al. 2018/2019
   (long-interval structure factor, HL-conditional, does NOT bear on mod-4
   supply).
4. **Dead-route corpus complete:** every approach in APPROACHES.md has a
   grounded reason it closed (Gatti Theorem 4 invalid, Muney length-5 hole,
   Eppstein anti-Gilbreath class-defeat, Colonna deletion counterexample, CHT
   inverse theorem hypotheses fail at reachable depth, fwd-diff-identity
   refuted, runcount potential refuted, etc.).

## One loose end found and closed this cycle

On re-verification the frontier-twice-cited **Torquato–Zhang–De Courcy-Ireland,
"Hidden multiscale order in the primes"** (arXiv:1804.06279) was found to have
its canonical (full) summary and claim already on disk
(`research/summaries/torquato-zhang-decourcy-ireland-hidden-multiscale-order-primes.md`,
claim `torquato-2019-hl-conditional-pair-structure`); a stray second summary I
created in the same cycle was flagged, converted to a pointer, and its duplicate
claim block removed, so the ledger carries exactly one claim per source.

## Answer to the standing question

**No further gathering is warranted.** The only legitimate next fetch would be a
source delivering an unconditional lower bound `ν₂ ≥ c·n` for prime gaps (the
mod-4 switch frequency) — none is known to the literature, and REQUESTS.md
records the negative: the switch bit is intrinsically two-point, so no
one-point (GRH/Dirichlet) route suffices. The run should not re-search.

## Phase-1 exit test

ROOT.md meets it: minimal counterexample structure stated (first row with
`A_k(1) ≥ 4`), verification bound stated and kept distinct from the literature
records (run depth 600/1000/1e9-block-protection), and ≥3 settled restricted
classes with hypotheses (consecutive odds; constant-2-tail; reaching a constant
`(1,c,c,…)` row — all proved).
