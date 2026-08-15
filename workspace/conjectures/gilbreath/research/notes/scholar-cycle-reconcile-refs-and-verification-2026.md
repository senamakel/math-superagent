# Scholar cycle — reference reconciliation + two verification gaps closed

**Scope of this cycle:** the library is CLOSED and was digested across 12+
prior scholar cycles. No new source was fetched. This cycle verified
digest-completeness and internal consistency of the route-bearing sources and
fixed three durable-reference defects. Nothing new was gathered; everything
below was already on disk.

## 1. Digest-completeness re-confirmed (no re-digest warranted)

Spot-checked every live-route source against its summary and claim block:

- **Granville 2026 FULLPDF** — Lemma 5.4 (`g*_n ≤ 2ν₂+2 ⟹ success`) and
  Theorem 5.5 (`ν₂ > n^β, β>α ⟹ success`) confirmed verbatim on disk
  (claim `lemma54-rederivation-safe`, `lemma54-descent-lean-formalised`,
  `lemma54-descent-lean-formalised-even`, `lemma54-link-A-lean-formalised`).
- **ABGS 2011 §9** — the switch-limit-open claim is filed
  (`abgs-2011-s9-mod4-switch-limit-open`, asserted) with the verbatim quote
  cross-checked (`abgs-s9-verbatim-verified`, checked).
- **Thue–Morse / dyadic family** — `thue-morse-sublinear-supply-witness`
  (proved), `dyadic-collapse-proved` (proved), `dyadic-oddfactor-infimum-bounded`
  (checked), `dyadic-separating-invariant-three-strings` (checked) all present.
- **G-supply route** — `g-supply-switch-count-not-one-point` (proved),
  `g-supply-transfer-universal-refuted` (checked), `g-supply-transfer-measured`
  (checked), `anticlustering-markov-insufficient-for-gsupply` (checked).
- **Malyshev** — the Boolean-Pascal bound `ξ ≤ ⌈s(s+1)/3⌉` is a catalogue-level
  sourced fact (`malyshev-max-ones-boolean-pascal-bound`, quoted from the
  abstract, **not** run-verified); full text unobtainable. This is the honest
  status and it has not changed.

## 2. Entailment "cannot all be true" flag — RESOLVED (documented self-correction)

The one remaining entailment flag, `dyadic-oddfactor-infimum-bounded` resting
on `rule90-periodic-window-collapse-refuted` (which records `contradicts:
rule90-periodic-window-collapse`), is **by design, not a live dispute**. Per
Directive 65 a refuted claim must STAY in the ledger beside its refutation.
`rule90-periodic-window-collapse` (any period p ⟹ ν₂=O_p(1), holds-here: no) is
the deliberately-kept dead over-generalisation; its refutation and the proved
power-of-2 theorem `dyadic-collapse-proved` are the correct basis for the
infimum claim. **Do not re-open this as a contradiction.**

Stored to durable memory (scholar reconcile, source note).

## 3. Dangling `rests-on` ids — fixed (three threads)

The entailment/thread reconciliation flagged references to claim ids that no
block establishes. Fixed on disk:

- `research/threads/dyadic-periodicity-collapse.md`: `rests-on: dyadic-collapse-theorem`
  → `dyadic-collapse-proved` (the actual block id). **Done.**
- `research/threads/regeneration.md`: `rests-on: IFF, reduction` →
  `gilbreath-second-entry-equivalence, step-law-theorem-proved,
  lemma54-re-derived-proof, odlyzko-block-lemma-exact` (with the substantive
  blocked-by detail left intact). **Done.**
- `research/threads/rule90-regeneration.md`: `rests-on: Block, lemma` →
  `rule90-interior-xor, odlyzko-block-lemma-exact`. **Done.**

These were spelling/dangling-id defects in thread headers, not claims; the
entailment closure now resolves them (THREADS.md re-derived clean, no more
"Resting on nothing recorded" rows for these three).

## 4. Thue–Morse verification gap — closed by cross-reference

`thue-morse-sublinear-supply-witness` carried a stale "machine check not
executed" line. Cross-reference: the identity `ζ(h)[d] = 1 ⟺ d a power of two`
is **machine-confirmed to N=10^5** (claim
`thue-morse-subset-zeta-confirmed-identification-refuted`,
`research/notes/thue-morse-identification-refuted.md`). What that claim also
shows is the load-bearing identification `nu2(n) == #{d≤n : d a power of 2}`
does **NOT** hold for the Thue–Morse triangle (first mismatch at n=1; n=100:
27 vs 7) — the fold bit marks cell PARITY, not {0,2} membership. The witness
note's verification section was rewritten to say the exact identity is
machine-confirmed but the power-of-two-count formula must NOT be used for
nu2; the qualitative conclusion (Thue–Morse ν₂ sublinear, max ~219 over
n≤4000; aperiodicity does not force linear supply) survives.

Stored to durable memory (scholar reconcile, source note).

## 5. What the run still lacks (unchanged)

A proof or unconditional bound of `ν₂ ≥ c·n` (the named-open two-point mod-4
switch hypothesis, `abgs-2011-s9-mod4-switch-limit-open`); the odd-factor
converse of the dyadic dichotomy as a formal proof (preperiod N₀>0, unbounded
P — only exact-period words to P=15 are measured); the Malyshev bound as a
run-verified program (currently catalogue-level only). Every claim library
entry that is `proved` or `checked` survived; no new contradiction between
sources, and none contradicted recalled memory.

**No new claims filed this cycle** — this was a reconciliation pass over closed
material. The two durable findings (entailment-flag resolution and the
Thue–Morse power-of-two-count caveat) are stored in Cognee.
