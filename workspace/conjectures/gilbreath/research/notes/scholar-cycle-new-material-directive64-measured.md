# Scholar cycle — new material: Directive 64 gate swung; consistency checked

**What is genuinely new this cycle.** The dyadic-periodicity thread's gate
measurement (Directive 64, "drafted-but-unrun" in the thread text) is **on
disk, executed, captured, and filed**: `research/notes/dyadic-oddfactor-infimum-measured.md`
filing claim `dyadic-oddfactor-infimum-bounded` (status: checked). Two smaller
new notes (`gap-hypothesis-separation-finding.md`, `switch-conservation-identity.md`)
are also new this cycle. Everything else in `research/` was verified consistent
with prior cycles and needs no re-digest (see the five prior scholar-cycle
notes). The library itself remains CLOSED; no new source was fetched.

## 1. The Directive 64 measurement — read and cross-checked

**Claim `dyadic-oddfactor-infimum-bounded`** (checked; anchors the exact-int
captures `dyadic_inf_measure`, `dyadic_oddfactor_density_exact`,
`dyadic_oddfactor_infratio`). Verified the runs and arithmetic on disk:

- inf ν₂/n (n≥100, exact integers, n≤20000): P=3 → **0.6471**, P=5 → **0.5088**,
  P=7 → **0.2667**, P=9 → **0.3592**, P=15 → **0.1143** (argmin n ≤ 114 in every
  case).
- Second route (n≤3000): for P=3,5,7,9 the large-n infimum is set early
  (argmin ≤ 1040), **no late new low past n=1000** — the infimum is not decaying
  toward 0.
- Exact-linear companion (n≤24000): residual `ν₂(n) − c·n` stays **O(1)**
  (P=3, word 001, c=2/3: residual ∈ {−0.67, −1.33, −2.00}; P=5: c=0.5333,
  residual ∈ {−1.00, −2.67}).
- Power-of-2 periods confirm the proved collapse (`dyadic-collapse-proved`):
  P=1,2,4 give inf ν₂/n ≈ 0.

**What it establishes.** The dyadic dichotomy's odd-factor half is numerically
confirmed on the periodic families; the odd-factor converse
(`ν₂ ≥ c(P,h)·n` for all n) is **NOT refuted by an asymptotic plateau** up to
n=24000, and **each fixed odd-factor word satisfies a uniform `ν₂ ≥ c_P·n`**.
The thread's gate is swung.

**One scope over-reach worth flagging to the board (the only finding beyond
the captures).** `dyadic-oddfactor-infimum-bounded` concludes the converse
(odd part o>1 ⟹ ν₂ ≥ c(P,h)·n) is "not refuted", and its `bearing` says the
dichotomy "would be supply-useful on the periodic families". But **the theorem
`dyadic-collapse-proved` is stated for `2^k` with an eventual preperiod N₀, and
the measurement here is EXACT periodic words with NO preperiod and minimal
period P ≤ 15.** The combination "periodic with odd factor P, N₀=0, h the
whole period word" is a strictly smaller class than "eventually periodic with
preperiod": the converse that would matter for the primes (or for making the
dichotomy supply-useful) needs the bound to survive a nonzero preperiod N₀ and
*unbounded* P, and the measurement shows the infimum *decays* as P grows
(0.647→0.509→0.267→0.359→0.114) with **no uniform c across P**. So the
measurement settles the exact-period part of the gate, nothing more.
`rule90-periodic-window-collapse-refuted` (the over-general claim, checked)
already says the exact-factor-2 span matters; the preperiod gap remains open and
is not measured anywhere on disk.

**Contradictions.** None with the proved collapse (`dyadic-collapse-proved`):
the P=1 value 0 and the O(1) powers-of-2 values agree exactly. The earlier
period-2 "ν₂=1 vs 2" convention conflict (`scholar-dyadic-periodicity-collapse.md`)
is resolved by `dyadic-periodicity-correct.py`'s convention note (off-by-one in
the suffix window); the corrected oracle uses the run's canonical
`lib.rightdiag.cycle_and_nu2`.

## 2. The two smaller new notes

**`gap-hypothesis-separation-finding.md`** (claim `gap-size-hypotheses-do-not-separate`,
checked): none of the three candidate gap-size hypotheses (bounded window mean,
bounded freq gap>G, Cramér g_n=O(log²p_n)) separates the prime column from the
sweep's dying {2..20} families — where they differ, the primes have the HEAVIER
tail (max gap 86 vs 20), the WRONG direction for separation. This redirects the
sweep-death question to order/autocorrelation (pairing of consecutive gaps), not
the gap marginal. Consistent with the established `torelli-prime-gap-bound`.

**`switch-conservation-identity.md`** (claim `switch-conservation-identity`,
proved, pure counting): N_switch(x) + N_nonswitch(x) = π(x)−1, so a
positive-density switch lower bound (G-supply, ν₂ ≥ c·n) is EXACTLY equivalent
to a below-density-1 **upper** bound on the equal-residue consecutive-pair count.
Explains why the held Ruzsa/Shiu/Martin lower bounds on non-switch pairs give
nothing to ν₂ (they push the wrong way). This is a reframing, not a closure; it
confirms `abgs-2011-s9-mod4-switch-limit-open`.

## 3. Everything else verified consistent (no re-digest warranted)

The five prior scholar-cycle notes (`scholar-cycle-new-library-material.md`,
`-malyshev-northshield-verification.md`, `-blair-morgan-corridor-verified.md`,
`-granville-lumley-mo-thread.md`, `-lean-plan-completed.md`,
`-nu2-supply-grounded.md`, `scholar-reconciliation-lean-and-linkA-current.md`,
`scholar-cycle-library-verified-coherent-directive58.md`) hold. The Lean
formalisation corpus (`descent_lemma.lean`, `lemma54_even_domain.lean`,
`lemma54_composition.lean`) is kernel-checked sorry-free with axioms within
propext/Classical.choice/Quot.sound; `link_a.lean` remains dead code (import
cannot build oleans in this container) but its content lives in the
kernel-checked composition file. The G-supply crux
(`g-supply-two-point-crux-settled.md`), the conditional theorem
(`g-supply-conditional-theorem.md`), and the LOS overstatement correction
(`los-2016-consecutive-pair-mod4-bias` "main term conditional, not PNT-in-AP")
all stand. No claim contradicts recalled memory.

## 4. Sources that do not help (so nobody re-reads)

- **Malyshev 2021 / Northshield 2010** — interior-frequency leads on the
  regeneration edge-2 rate; not regeneration proofs; full texts unobtainable
  (no text layer / DSpace stub). Digests complete. **The Malyshev verifier
  (`code/scholar/verify_malyshev_bound.py`, exhaustive s=1..14) remains UNRUN
  in captured form** — cross-checked only by hand to s=5 this cycle; the claim
  stays `asserted`. Do not re-fetch the sources.
- **Granville–Lumley 2021** — demand-side heuristic only, no ν₂ content. Do not
  cite for ν₂.
- **MathOverflow thread, zarkouna, okolo, Maréchal, Keen, Gatti-2023** —
  already recorded; no new dead route, no proof.

## 5. What the run still lacks (unchanged)

A proof or unconditional bound of `ν₂ ≥ c·n`. Everything else is proved,
machine-checked, or a recorded refutation. **Open items this cycle's read
confirmed:** (a) the odd-factor converse for the dyadic dichotomy — preperiod
N₀ > 0 and unbounded P, not just exact periodic words to P=15; (b) the supply
bound for the aperiodic primes (named-open `abgs-2011-s9-mod4-switch-limit-open`);
(c) the Malyshev verifier execution; (d) the dyadic odd-factor converse as a
formal proof.

## Stored

- Cognee: the Directive-64 measurement result + the scope over-reach flag + the
  switch-conservation reframing (durable, source-backed).