# Scholar pass: verifying the newest digests against full texts; run state unchanged

Author: scholar. Date: this pass. Scope: the research agent finished again; the
task says the library has new material. Prior passes (`scholar_pass_newest_library_reconciliation`,
`scholar_pass_citation_audit`, `scholar_pass_mr_green_verify_and_probe`) already
identified what the agent's tick (sources 44 → 50, summaries 58 → 69, frontier
348 → 445, directive 30) added. This pass does not re-inventory; it **independently
verifies the claim-bearing digests against their full texts** (rule 11), checks
whether anything contradicts the run's beliefs, and records the state.

## What the new material genuinely is

1. **Mauduit–Rivat 2010 primary digest** (`mauduit_rivat_gelfond_somme_chiffres_premiers_primary.md`).
   **Verified this pass against the full text, lines 285–305:** Théorème 1
   (power-saving exponential-sum bound `Σ_{n≤x} Λ(n)e(αs_q(n)) = O(x^{1−σ})` for
   (q−1)α ∉ ℤ), Théorème 2 ((αs_q(p)) equidistributed mod 1 iff α ∉ ℚ), Théorème 3
   (`#{p≤x : s_q(p) ≡ a (mod m)} = ((m,q−1)/m)·π(x; a, (m,q−1)) + O(x^{1−σ})` for
   q,m > 2). Answers Gelfond's second problem. **Paradigm only:** the statistic is
   the digit sum of the prime; Φ reads the gap-parity string h. No transfer in the
   library; the request `walsh-spectral-subset-b904` stays open (both MR claim
   blocks already carry this caveat).

2. **Shiu 2000 claim digest** (`shiu_strings_congruent_primes.md`). **Verified this
   pass against the Ethan Yang expository full text** (Thms 1.1(1)(2), 1.2, 4.1):
   arbitrarily long strings of consecutive primes ≡ a (mod q) for (q,a)=1; length
   `k ≫ (loglog x/logloglog x)^{1/φ(q)}` for a ∈ A±. For q=4 both a=1 and a=3 lie
   in A±, so arbitrarily long constant runs in h — **refutes closed door 3** (no
   long constant runs) and resolves the earlier "Shiu unsourced here" caveat.
   Equal-residue direction only — the wrong direction for switch density.

3. **The 7th citation graph** (`citations_w2010510777.md`, Chebyshev's Bias /
   Rubinstein–Sarnak 1994). Lead only, explicitly "filed by a citation-graph
   lookup, not read". Its cited/cited-by surface (prime races, GRH+LI bias
   laws) is the approach already refuted (`rubinstein-sarnak-prime-race-ergodic`).
   No claim, no theorem, no change.

4. **The other six citation graphs + four OEIS rows + the HAL metadata page** —
   re-confirmed lead-only / metadata-only by prior passes; do not re-read.

## Digests re-verified this pass (own reading, not just prior passes' word)

- **Maynard 2016 Thm 3.3** (positive-density equal-residue strings, BV-based):
  `#{p_n ≤ x : p_n ≡ … ≡ p_{n+m} ≡ a (q), p_{n+m}−p_n ≤ εlog x} ≫_ε π(x)/(2q)^{exp(Cm)}`
  for `m ≤ cε loglog x` — unconditional for the full primes; the strongest wrong-
  direction (equal-side) statement. Digest matches.
- **Takei 2017** (Rule 90 measure rigidity): Cesàro means of Λⁿµ converge iff µ
  is δ₀ or the uniform product among strong-mixing shift-invariant measures;
  measure-level, does not give the finite fixed-string bound. Digest matches.
- **Szechtman 2024** (`szechtman-lucas-submask-corollary`): Lucas/Kummer with a
  matrix proof; p=2 submask reading `C(d,i) ≡ 1 mod 2 ⇔ i ⊆ d` is the fold's
  foundation. Background, not a weight bound. Digest matches.
- **Rowland 2011** (`rowland-nonzero-binomial-prime-power`): Fine's count
  `2^{s₂(n)}` of odd binomials on row n, generalised to p^α; confirms the submask
  cardinality behind Φ's cells. Does not bound wt(Φ_n h). Digest matches.
- **Rampersad–Wiebe 2309.04012 full text** (`rw-runlength-is-2regular`,
  `rw-thm20-binomialsum-structure`, `rw-average-nonlinear`,
  `rw-not-the-submask-xor-fold`): the run-length transform machinery is NOT
  SUPPLY's submask-XOR fold — the correction contradicts the earlier abstract-
  based overstatement (flagged in CLAIMS.md as `rw-described-as-the-fold-itself`).
  Digest matches the full text.
- **Freiberg 1005.4703** (`freiberg-short-equal-residue-pairs`): infinitely many
  short-gap (gap < εlog p) equal-residue consecutive pairs. Wrong direction for
  switch density. Digest matches.
- **LOS sawtooth 2018** (`los-sawtooth-averaged-bias-equidistributed`):
  average-across-q equidistribution of the bias structure; pointwise pair
  frequency remains conjectural (Hardy–Littlewood). Supports the averaged-form
  route's porosity; transfer to wt(Φ_n h) not made. Digest matches (body paywalled).

## What this establishes for the run

**The library's position is unchanged.** None of the new material is a theorem
about `wt(Φ_n h) ≥ c·n` for the fixed prime string. The three open items
re-confirmed:

1. **Finite-prefix transfer** (Pivato–Yassawi Thm 7.1 / Takei are ergodic,
   density-one-times; no quantitative bound for the fixed h) — the single largest
   missing technical tool; in no source.
2. **Request `walsh-spectral-subset-b904`** — genuinely open; MR/Green fix the
   paradigm (weak unconditional prime input), Shiu/Maynard/Freiberg close the
   equal-residue side only.
3. **`s2_N → 0` / finiteness of the exceptional set for the prime h** — measured
   (Ratio B 1.3155@40000) but unproved; in-house computation, not literature. The
   sharpest claim remains `prime-E-S2-On-sharp-conjecture` (directive 31, mirrored
   in ROOT.md): E[S(n)²]=O(n) gives only density-1 SUPPLY; the subgaussian tail on
   Z(n)=S(n)/√n upgrades to pointwise (finiteness of every exceptional set).

And the gate: directive 30's release condition for the absolute search freeze is
the Ratio B decrement-ratio discriminator at N=160000. `code/out/ratio_b_extension.txt`
and `code/out/goals_attempt2_status.md` record that **N=160000 was NOT run** —
projected ~22 min, over the per-command budget, with the note "only attempt 160000
if 80000 finished well under budget" (it did not). So the unaffordable-runtime
note leg of the release condition arguably exists on disk; the freeze remains in
force until steer accepts it.

## Contradictions

- **With recalled memory:** none — durable memory reads return 404 (known
  environment fault, 20+ failures this run against successful writes; the store
  side is populated by prior passes' `remember_memory`).
- **Between sources / within library:** only the two known stale-id artefacts
  (`r-finite-verified` vs its true range; `rw-described-as-the-fold-itself` vs
  `rw-not-the-submask-xor-fold`), both self-resolved and flagged in CLAIMS.md.
  MR primary and Green's binary-case agree (same theorem, different q).
- **Derive gap re-confirmed (bookkeeping):** `research/CLAIMS.md` still does not
  carry its own rows for `mauduit-rivat-prime-digit-sum-equidistributed`,
  `mauduit-rivat-gelfond-sum-of-digits-primes-equidistributed`, `shiu-string-theorem`,
  `takei-rule90-mixing-limits-uniform`, `szechtman-lucas-submask-corollary`,
  `rw-runlength-is-2regular`, `gilbreath-verified-10^13` — they appear only inside
  the `claims-md-derive-gap-newer-summary-blocks` row. The knowledge is reachable
  via `search_claims` (verified: the MR, Shiu, and Takei claims all return). Do not
  read absence from the rendered table as absence from the library.
- **FRONTIER.md contamination (persistent):** ~40 "DEFINING SUPPLY CHAIN
  MANAGEMENT" citation rows (business domain, Mentzer 2001) still rank above the
  math rows by cited-by count. Read FRONTIER by subject, not by rank; exclude the
  contamination ring.

## Sources that do not help this pass (so nobody re-reads them)

- The seven `citations_w*` files — citation-graph lookup tables, lead only.
- The four OEIS rows (base-4 digits of e/π, 3-adic √−2, fractal ternary) — nothing
  to do with the fold.
- `odlyzko_gilbreath` (bibliography index), `chase_random_gilbreath`
  (holds-here: no), `encyclopedia_gilbreath` (out of scope), the Granville–Martin
  duplicate mirror, `mauduit_rivat_gelfond_hal_page` (metadata only), the
  quarantined `matomaki_radziwill_tao_averaged_chowla` (wrong download, pointer
  only).

## Durable findings stored this pass

1. MR 2010 Théorèmes 1–3 verified verbatim (lines 285–305): digit-sum-of-primes
   equidistribution with power-saving error; paradigm weak input, no transfer to
   gap-parity h.
2. Shiu 2000 verified via Ethan Yang expository: arbitrarily long constant runs in
   h for q=4 — closed door 3 refuted, wrong direction for switch density.
3. Maynard 3.3 / Freiberg / LOS-sawtooth re-verified: equal-side and average-side
   statements only; none forces weight on the fold.
4. State unchanged: finite-prefix transfer, walsh-spectral-subset-b904, s2_N→0
   remain open; freeze release gate (N=160000) blocked on runtime, note on disk.

```claim
id: newest-digests-verified-state-unchanged
statement: This pass independently verified the two new claim-bearing digests against full texts (Mauduit–Rivat 2010 Théorèmes 1–3 verbatim lines 285–305; Shiu 2000 via the Ethan Yang expository Thms 1.1/1.2/4.1) and re-read Maynard 3.3, Takei, Szechtman, Rowland, Rampersad–Wiebe full text, Freiberg, and LOS sawtooth. All digests match their sources. Nothing in the new material is a theorem about wt(Φ_n h) ≥ c·n for the fixed prime string: MR/Green set the weak-input paradigm (digit sum, no transfer), Shiu/Maynard/Freiberg close only the equal-residue side, Takei/Pivato–Yassawi stay measure-level. The run's open state is unchanged: finite-prefix transfer, request walsh-spectral-subset-b904, and s2_N→0 (Ratio B 1.3155@40000, unproved) remain the three gaps; the directive-30 freeze gate (N=160000 Ratio B) is blocked on projected ~22 min runtime with the unaffordable note on disk.
hypotheses: the claim-bearing digests exist and are reachable via search_claims even where the rendered CLAIMS.md row is absent (derive gap).
holds-here: yes — this is an audit statement about library contents and run state.
status: checked (verbatim line verification of MR 285–305; own re-reading of the listed digests; grep of CLAIMS.md vs summaries for the derive gap)
bearing: nobody should re-fetch Chebyshev-race, equal-residue-string, or digit-sum material expecting a way past the parity barrier; the next loop should attack the in-house computation (E[S²]=O(n) or the N=160000 discriminator) per the freeze, not the library.
anchor: research/notes/scholar_pass_verify_newest_digests_and_state.md; research/summaries/mauduit_rivat_gelfond_somme_chiffres_premiers_primary.md (lines 285–305 of full text); research/summaries/shiu_strings_congruent_primes.md; research/summaries/citations_w2010510777.md
contradicts: none
answers: does not answer walsh-spectral-subset-b904 — recorded precisely so a later reader does not re-fetch expecting closure.
```