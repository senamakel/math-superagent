# Scholar pass — independent verification of the last tick's digests; library state unchanged

Author: scholar. Date: this pass. Scope: the research agent finished; the task
says research/ has new material. Prior passes (`scholar_pass_new_material`,
`scholar_pass_newest_library_reconciliation`, `scholar_pass_verify_newest_digests_and_state`)
had already digested and re-audited the same tick (sources 44→50, summaries 58→69,
frontier 348→445, directive 30). This pass does not re-inventory; it **verifies
against full texts by its own reading** (rule 11) and records what the genuinely
new items establish and what they imply for the run.

## The genuinely new items, verified this pass

1. **Mauduit–Rivat 2010 primary** (`mauduit_rivat_gelfond_somme_chiffres_premiers_primary.md`).
   Verified verbatim at full text lines 284–305: Théorème 1 (power-saving
   exponential sum `Σ_{n≤x} Λ(n)e(αs_q(n)) = O(x^{1−σ})` for (q−1)α∉ℤ), Théorème 2
   (`(αs_q(p))` equidistributed mod 1 iff α∉ℚ), Théorème 3 (`#{p≤x: s_q(p)≡a (m)}
   = ((m,q−1)/m)π(x;a,(m,q−1)) + O(x^{1−σ})` for q,m>2). Answers Gelfond's second
   problem. Claim `mauduit-rivat-gelfond-sum-of-digits-primes-equidistributed`,
   proved. **Bearing:** the paradigm weak unconditional arithmetic input the
   primes provably satisfy (GOAL priority 2's shape). **Does not close
   `walsh-spectral-subset-b904`:** the statistic is s_q(p), the digit sum; the
   fold reads gap-parity h[j]=((q_{j+1}−q_j)/2) mod 2. Different objects, no
   transfer in the library.

2. **Shiu 2000 claim digest** (`shiu_strings_congruent_primes.md`). Verified via
   the expository full text line 33 (Theorem 1.1): arbitrarily long strings of
   consecutive primes ≡ a (mod q); q=4, a=1,3 both in A±, so arbitrarily long
   constant runs in h. **Bearing:** refutes closed door 3; equal-residue side is
   the fully understood, wrong direction for switch density. Claim
   `shiu-string-theorem`, proved.

3. **Takei 2017 Rule-90 rigidity** (`takei_limiting_measures_rule90.md`): among
   strong-mixing shift-invariant measures, Cesàro limits of Λ^n µ exist iff µ is
   δ₀ or the uniform product. Measure-level; complements Pivato–Yassawi Thm 7.1;
   no finite fixed-string bound. Claim `takei-rule90-mixing-limits-uniform`.

4. **7th citation file** (`citations_w2010510777.md`, Chebyshev's Bias /
   Rubinstein–Sarnak 1994): explicitly "filed by a citation-graph lookup, not
   read" — a lead, not evidence; its surface is the GRH+LI prime-race approach
   already refuted (`rubinstein-sarnak-prime-race-ergodic`). No claim, no change.

## What does not help (so nobody re-reads it)

The other six `citations_w*`; the four OEIS rows; `odlyzko_gilbreath`
(bibliography index); the Granville–Martin duplicate mirror;
`mauduit_rivat_gelfond_hal_page` (metadata); `ashikhmin_barg_litsyn_polynomial_method`
and `friedlander_macwilliams_krawtchouk` (metadata stubs, content held better by
macwilliams_1963 / guruswami notes); `matomaki_radziwill_tao_averaged_chowla`
(wrong-download quarantine). All previously flagged; re-confirmed.

## Contradictions

**None new.** No source contradicts recalled memory or another source beyond the
two known self-resolved stale-id artefacts (`r-finite-verified` vs its true range;
`rw-described-as-the-fold-itself` vs `rw-not-the-submask-xor-fold`). The derive-gap
(a dozen newer summary claim blocks absent from rendered CLAIMS.md) is bookkeeping:
`search_claims` reaches them (re-verified this pass for takei, both mauduit-rivat,
shiu). Read summaries, not the rendered table, to conclude what the library holds.

## The run's open state (unchanged, precisely)

1. **Finite-prefix transfer** — Pivato–Yassawi Thm 7.1 / Takei are ergodic
   density-one-times statements; neither gives `wt(Φ_n h) ≥ c·n` for the fixed
   prime string. The single largest missing tool; in no source.
2. **Request `walsh-spectral-subset-b904`** — genuinely open. MR/Green fix the
   weak-input paradigm (digit sum, no transfer); Shiu/Maynard/Freiberg close the
   equal-residue side only.
3. **`s2_N → 0` / finiteness of the exceptional set** — measured (Ratio B
   1.3155@40000) but unproved; in-house computation, not literature.

## The one actionable handoff (still unexecuted)

`code/scholar/mr_gap_correlation_probe.py` — probes whether the Mauduit–Rivat
digit-sum-parity statistic correlates with gap-parity h (P(h=1 | s₂(q_j) parity),
with a random-string negative control). Still **unexecuted** (no capture in
code/out/; the scholar role has no execution tool). It tests whether MR is truly
inert for the fold or does touch it. Hand to tool_builder/coder:
`python3 -m lib.capture --target code/out/mr_gap_correlation_probe.captured.txt -- python3 code/scholar/mr_gap_correlation_probe.py 300000`.
Until it runs and its output is read, it establishes nothing (its own header).

## Stored this pass

Single durable memory entry recording: MR 2010 Thms 1–3 verified verbatim
(lines 284–305), Shiu Thm 1.1 verified (expository line 33), Takei measure-level,
citations_w2010510777 lead-only; library mature (49 full texts, all digested); the
three open items; the unexecuted probe handoff. No source contradicts recalled
memory.