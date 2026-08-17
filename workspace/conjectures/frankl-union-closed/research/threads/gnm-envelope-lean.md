# Formalise the g(n,m) envelope theorem in Lean

## Question
Can `g(n,m) = max(1, m − 2^{n−1})` — the full general statement, tightness
included — be formalised in Lean 4 against Mathlib as a kernel-checked theorem,
rather than standing as a claim marked PROVED in prose?

## Why now (directive 17, steer)
This finite-combinatorics proof is a far better Lean target than the entropy
work already formalised (`code/lean/yu_gamma_half_is_phi_over_2.lean`): it has
no real analysis, no transcendental functions, no interval arithmetic, no
numerical certification. It is entirely about Finsets over `Fin n`, upward
closure as a predicate, and two explicit families. If it compiles, the run has a
kernel-checked general theorem. The directive marks this as a *suggestion*, not
an instruction — an open thread, not a mandate.

## What the theorem needs
- `g(n,m) = min over union-closed F ⊆ 2^[n], |F| = m, of rare(F)`, where
  `rare(F)` is the least frequent present element's count.
- Lower bound (elementary, no union-closure): sets avoiding x are subsets of
  `[n]∖{x}`, at most `2^{n−1}`; every present element has count ≥ 1. So
  `rare(F) ≥ max(1, m − 2^{n−1})`.
- Tightness, both constructions, proved constructively in
  `code/out/gnm_envelope_finding.md §Proof`:
  - **Size lemma**: every size `s` in `0..2^N` is realisable as an upset of
    `2^[N]`, by induction on `|U|` (complement of an upset is a downset; a
    maximal element of the non-empty complementary downset moves in and the
    result stays an upset).
  - **Construction A** (`m ≥ 2^{n−1}+1`): `F = 2^[n−1] ∪ {A∪{n} : A ∈ G}` with
    G an upset of size `c = m−2^{n−1}`.
  - **Construction B** (`m ≤ 2^{n−1}+1`): `F = H ∪ {U∪{n}}` with H an upset of
    size `m−1`, U its union.

## Reuses and precedent
- `code/lean/` is working and `lean_check` is wired; the existing
  `yu_gamma_half_is_phi_over_2.lean` verified with no sorries and only the
  standard Mathlib axioms (propext / Classical.choice / Quot.sound).
- Construction A and B are ALREADY verified computationally — do not
  re-derive them. `code/out/gnm_envelope_verify.captured.txt` ran both for
  every n in 1..6 and every m in 1..2^n, confirmed each family union-closed
  via lib.uc, |F|=m, and rare == max(1, m-2^(n-1)), with the upset size lemma
  checked for N in 0..6: ALL ASSERTIONS PASS. A scratch `is_upset` that walks
  every superset of every member is exponential-on-top-of-exponential and will
  never return at feed sizes; it destroyed ten minutes and is banned
  (directive 19).

## Directives 17/18/19 strategy for this thread
Directive 19 confirms the decision to WORK the formalisation, and fixes the
route: (1) NO re-verification scratch — read the capture at
`code/out/gnm_envelope_verify.captured.txt` for any pre-Lean sanity check;
(2) formalise AGAINST THE PROOF TEXT, not a fresh Python reimplementation — the
complete proof including the size-lemma induction is in
`code/out/gnm_envelope_finding.md §Proof`; (3) START WITH THE SIZE LEMMA ALONE
— upward-closed on Finset (Fin n), complement is a downset, move an
inclusion-maximal element across, induct on card — and get THAT compiling under
lean_check before touching the constructions; a first file with one theorem and
no sorry is worth more than a full development that does not elaborate; then
construction A and B, then the full general theorem if budget allows; (4) if
the Finset API is heavier than the upgrade justifies, DEFER with that as the
recorded reason — always acceptable; never consume budget on exponential
scratch checking what is already proved and verified. Keep the development in
the workspace (code/lean/gnm_envelope.lean), not /tmp — a /tmp script produces
no capture and vanishes.

## Deliverable
`code/lean/gnm_envelope.lean` (or similar) compiling with no `sorry`, whose
`#print axioms` output shows only the standard Mathlib axioms. First milestone:
the size lemma alone compiling under lean_check. If it does not compile / the
API proves too heavy, the closing reason is the specific lemma/step that
resisted (or the recorded deferral) — a known gap, not a silence.

## Deliverable
`code/lean/gnm_envelope.lean` (or similar) compiling with no `sorry`, whose
`#print axioms` output shows only the standard Mathlib axioms. If it does not
compile, the closing reason is the specific lemma/step that resisted — a known
gap, not a silence.
