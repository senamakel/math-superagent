# Scholar pass — analytic-NT tier verified verbatim, digests corrected

Author: scholar. Date: this pass. Mandate: read what is now in `research/` against
the goal, record what each new source establishes, store durable findings, flag
contradictions.

## What was actually new

The library is mature (all 42 full texts have digests; all 51 claim blocks live in
`research/summaries/`). The one substantive gap in coverage was **verification**:
the librarian's three analytic-NT digests (Matomäki–Radziwiłł 2016, MRT 2020,
Green–Tao 2012) carried `status: asserted` / `holds-here: unchecked` — nobody had
read them against the full texts. This pass did.

## Verified verbatim (line citations in the digests)

1. **MR 2016** (`matomaki_radziwill_multiplicative_short_intervals.full.md`):
   Thm 1 (lines 25–40) — exact exception-set bound
   `CX((log h)^{1/3}/(δ²h^{δ/25}) + 1/(δ²(log X)^{1/50}))`, `C′ = 20000`; Cor 1
   (smooth numbers, lines 49–64); Cor 2 (Liouville two-point, **all shifts
   h ≥ 1**, lines 75–100). **Corrected:** the digest's "O(δh) for all but
   `O_C(X(log h)^{−1/100})`" is the special case `δ=(log h)^{−1/200}`, not the
   general statement.
2. **MRT 2020** (`matomaki_radziwill_tao_fourier_uniformity_averaged.full.md`):
   Thm 1.2 (lines 165–178) `∫ sup_α |Σ λ(n)e(−αn)| dx = o(XH)` for H = X^θ,
   any θ>0 (first below θ=5/8, Zhan); Cor 1.3 (lines 215–225) averaged
   λΛΛ correlation; **Thm 1.4 (lines 304–314) is a dichotomy, not a
   generalization**: 1-bounded multiplicative f with large average Fourier
   mass ⇒ f is *pretentious* (`D(f; X²/H^{2−ρ}; Q) ≪ 1`); Cor 1.5 (lines
   335–360) handles general 1-bounded f against sieve-majorant sequences
   `a(n), b(n) ≪ 1 + Λ(n)`. **Corrected:** the digest's "same statement for
   non-pretentious f" was the dichotomy's contrapositive, stated loosely.
3. **GT 2012** (`green_tao_mobius_nilsequences.full.md`): Thm 1.1 (lines
   89–108) — `|E_{n∈[N]}μ(n)F(g(n)Γ)| ≪_{m,d,A} Q^{O(1)}(1+‖F‖_Lip) log^{−A}N`,
   **ineffective** (Siegel zeros). The digest omitted the Q/Lip dependence and
   the ineffectiveness; both matter (ineffective ⇒ no quantitative constant).

## Bearing — unchanged, now verified

All three are **value-domain** statements for multiplicative functions (μ, λ) at
integer arguments. SUPPLY's object is `s_j = χ(q_j)` at **prime indices**, read by
the fold's submask-XOR transform. The two approaches these sources were named for
are **refuted in the ledger** with precise reasons (`matomaki-radziwill-
index-autocorrelation`: index-domain object not multiplicative in the prime index,
g=0 is the parity barrier; `gowers-u2-nilsequence-uniformity`: basis mismatch,
fold lives on the ANF/zeta basis, not the Walsh/U² basis the theorem controls).
The sources therefore do **not** close request `walsh-spectral-subset-b904`; the
finite prime-index transfer is the unclosed step. This confirms (now with
line-level verification) the position every prior pass reached.

## What does not help (so nobody re-reads)

- The seven `citations_w*` files — citation-graph leads, self-flagged "not
  evidence"; covered by prior passes.
- `matomaki_radziwill_tao_averaged_chowla` — correct quarantine pointer to the
  MRT 2020 source; nothing to read.
- OEIS rows, Odlyzko bibliography page, Ashikhmin–Barg–Litsyn and
  Friedlander–MacWilliams stubs — already flagged do-not-re-read.

## Contradictions with recalled memory

**None.** Cognee recall remains 404 (empty/broken backend); CONTEXT.md's
"Recalled" section matches the on-disk state. The one live bookkeeping item is the
known derive gap: `claims-md-derive-gap-newer-summary-blocks` — the rendered
CLAIMS.md still misses several newer summary blocks (mr-short-averages,
mrt-fourier, mauduit-rivat-*, shiu-string, takei-rule90, rw-runlength-is-2regular,
rowland-nonzero, szechtman-lucas, gilbreath-verified-10^13). The knowledge is on
disk in the summaries; absence from CLAIMS.md is not absence from the library.

## Handed on (still unexecuted, third time)

`code/scholar/mr_gap_correlation_probe.py` — whether the Mauduit–Rivat digit-sum
statistic `s_q(p)` correlates with the gap-parity string `h` the fold reads — has
**no capture** in `code/out/`. It tests whether MR/Green (the digit-sum theorems)
are truly inert for the fold or touch it. Needs a tool with execution:
`python3 -m lib.capture --target code/out/mr_gap_correlation_probe.captured.txt -- python3 code/scholar/mr_gap_correlation_probe.py 300000`

## Open state (unchanged, re-confirmed)

1. Finite-prefix transfer (ergodic Lucas mixing → quantitative `wt(Φ_n h) ≥ c·n`)
   — the single largest missing tool; in no source.
2. Request `walsh-spectral-subset-b904` — Walsh/subset-sum lower bound on
   `wt(Φ_n x)` for non-complicated x — open.
3. `E[S(n)²] = O(n)` for the real prime h — the one open arithmetic input between
   the settled geometry and density-1 SUPPLY.
