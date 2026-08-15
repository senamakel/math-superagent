# Scholar audit — the two load-bearing spines are faithful; one new corroboration

**Cycle:** this advisory cycle. The library is closed (Directives 39/46/56/62/64);
no new gathers. Scholar's value: spend scepticism on the digestions that exist
and are load-bearing, not on re-fetching.

## Spine 1 — G-supply two-point crux (the reason Route B is conditional)

Verified against the primary full text (`ash-beltis-gross-sinnott-2011-...full.md`):
- `abgs-2011-s9-mod4-switch-limit-open` quote verbatim ("we cannot tell whether
  they are tending toward a limiting ratio of 1"); already `abgs-s9-verbatim-verified`.
- ABGS Props 4.1 (power-of-2 residue-independence at m=2^k) and 4.2
  (antidiagonal symmetry) are the only rigorizable structural facts on the
  switch count; they delimit the shape of any supply bound but supply none.
- The linchpin `g-supply-switch-count-not-one-point` (proved, countermodel) is
  logically sound: the one-point marginals do not pin the switch count, because
  the ordering [1,…,1,3,…,3] is consistent with balanced classes and achieves
  exactly ONE switch. **Proof by inspection — no program required** (a residue
  multiset with counts {1:m,3:m'} permuted as all-1s then all-3s has exactly one
  boundary). A numeric restatement is handed to tool_builder for the record:
  `code/scholar/verify_countermodel_only.py` → capture
  `code/out/verify_two_point_countermodel.captured.txt`.

## Spine 2 — Granville Lemma 5.4 / Theorem 5.5

Verified against the FULLPDF (v3, cs.CR, 14 Jul 2026):
- Theorem 5.5 verbatim: if `g_n* < n^α` (record gap) and `ν₂(q_{n−1}) > n^β`
  with β>α, the sequence succeeds at q_n if it succeeds at q_{n−1}. Lemma 5.4:
  success iff `v_n ≤ 2ν₂(q_{n−1})+2`. The run's linear form `ν₂ ≥ c·n` implies
  the n^β form for large n (c·n > n^β for β<1) — consistent.
- **CRITICAL, CONFIRMED:** Route B does NOT rest on Granville's word. The
  theorem is anchored in the run's own even-domain proof
  (`lemma54-re-derived-proof`, handling the δ=0 case Granville discards; Lean
  kernel-checked abstract core). Granville's is a non-peer-reviewed business
  preprint (BondingAI.io) with an uneven §5. This re-derivation-independent
  anchor is the robust feature.

## New corroboration from the primary text (not previously a claim row)

Granville's **Conjecture 5.1(4)** (p. 18) states: "for the prime number
sequence, δ(q_n) is balanced for all n > 770 ... (11) is satisfied if β = 0.99
and n > 2535, or β = 0.55 and n > 16. To prove Gilbreath, β > 0.525 is enough
as it is tied to the best proven bound on prime gaps." So Granville himself
asserts ν₂ ~ n/2 (heuristic, explicitly *not* proved) and confirms α=0.525 is
not the operative bound — the supply side ν₂ ≥ c·n is the only real content.
This matches the run's measured weakest exponent 0.7658 at n≤1e5. A claim
block for this corroboration is below; it does not change the status (the
balancing is Granville's conjecture, not proved).

```claim
id: granville-conj51-supply-corroboration
statement: Granville's own Conjecture 5.1(4) (arXiv:2607.04166 v3, p.18) asserts the prime right diagonal δ(q_n) is balanced (ν₂ ~ n/2) and that the supply condition (11) ν₂(q_{n−1}) > n^β is satisfied with β=0.99 for n>2535 and β=0.55 for n>16; he states β>0.525 suffices to prove Gilbreath via the BHP record-gap bound. This matches the run's measured weakest implied exponent 0.7658 at n≤1e5 and corroborates that the demand exponent α∈{0.52,0.525} is not the operative bound — the linear supply bound ν₂ ≥ c·n is the entire open content of Route B. Granville explicitly treats the balancing (~n/2) as heuristic, NOT proved; so this corroborates the framing but leaves ν₂ ≥ c·n (abgs-2011-s9-mod4-switch-limit-open) a named-open hypothesis.
hypotheses: primes; right-diagonal δ(q_n); ν₂ = #2s in the 0-2 cycle; BHP record-gap bound α=0.525 unconditional.
holds-here: yes (matches run measurements)
status: asserted (Granville's conjecture, non-peer-reviewed; aligned with run measurement but not proved here)
bearing: reinforces that Route B reduces to the linear supply bound; does not close it. The conditional-theorem framing is unchanged.
anchor: research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md
```

## Handoff to tool_builder (scholar has no execution tool this cycle)

- `code/scholar/verify_countermodel_only.py` — numeric restatement of the
  linchpin countermodel (balanced classes → countermodel ordering gives exactly
  1 switch; also run on real primes ≤ 1000).
- Run: `timeout 60 python3 code/scholar/verify_countermodel_only.py 2>&1 |
  tee code/out/verify_two_point_countermodel.captured.txt`; echo EXIT_CODE=$?
- The claim is logically self-evident; this run is for the record only, so the
  `.captured.txt` does not exist until tool_builder runs it.

## Contradiction check vs recalled memory

No contradiction found. Recalled memory holds the same two-point crux, the
Granville reduction, and the honest conditional framing. The audit confirms the
deliverable is the CONDITIONAL theorem on the named-open two-point mod-4
correlation — not an unconditional claim. Nothing on disk over-reads ν₂~n/2.
