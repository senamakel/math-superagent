# Shared context

What this run knows, in its own words. Carries what an agent would otherwise
rebuild from disk: established results with their basis, dead approaches and
why, computed numbers, durable memory, disagreements. Not a file catalogue
(`research/INDEX.md` is that) and not a narration of activity.

Budget 10,000 tokens. Length is a bill the whole run pays on every model call;
link the file holding any detail compressed away. (Current: Directive 58 — prove
the dyadic dichotomy, do not survey it, see Run state.)

## Run state (Directive 58 — prove the dyadic dichotomy, do not survey it)

**Directive 57's dyadic question is now a measured dichotomy — reproduce it,
then prove it.** Host-side stage-1 numbers (exact integers, periodic halved-gap
bit string `h`, gap = 2 if bit else 4, `ν₂` = #2s in the maximal {0,2} suffix
of the right diagonal): period 1 (`h=1`) `ν₂=1` at n=200,400,800,1200;
period 2 (`01`) `ν₂=2`; period 4 (`0001`) `ν₂=2`; period 8 (`00000001`)
`ν₂=2` — all four n; period 3 (`001`) `ν₂=133,264,533,798`; period 5
(`00001`) `104,210,424,638`; period 6 (`000001`) `134,264,534,796`; period 7
(`0000001`) `112,112,685,684`. **Dichotomy is sharp:** `ν₂ = O(1)` exactly on
power-of-2 periods, `ν₂ ~ c·n` otherwise (c ∈ [0.53, 0.67]); period 6 = 2·3
grows, so it is the ODD FACTOR that matters, not merely being non-dyadic.
**Skip straight to the theorem.** tool_builder: confirm the eight rows and
extend to periods 9..16 and to non-constant patterns of the SAME period (the
claim is about the period, not the specific word). theorem_prover: prove from
Lucas, prime-free, that `h` eventually periodic with period `2^k` forces
`ν₂ = O_k(1)` — and, the harder half, that an odd factor in the period forces
`ν₂ ≫ n`. Mechanism for the dyadic half is `rule90-interior-xor`: weights
`C(d,j) mod 2` are supported on the binary submasks of `d`, so period-`2^k` `h`
collapses the sums for all large `d` (consecutive odds = period 1; alternating
2/4 = period 2). **State the conclusion as the dichotomy theorem, then say
precisely what it does and does NOT give for the primes: aperiodicity alone is
weaker than the quantitative anti-dyadic input the supply bound needs — the gap
between them is the honest remaining statement. Do NOT claim it closes
G-supply.** Live tasks `test-dyadic-periodicity-prediction`,
`prove-dyadic-periodicity-collapse-lemma`, `state-dyadic-dichotomy-primes-gap`;
thread `research/threads/dyadic-periodicity-collapse.md`. The repair thread
`gsupply-transfer-repair` is DEAD (Directive 57).

## Run state (Directive 50 — first kernel-checked result)

**`code/lean/descent_lemma.lean` compiles clean — the first kernel-checked
result of the run.** `lean_check`: compiled true, verified true, no `sorryAx`;
axioms `absorbing` — none; `run_absorb` — `[propext]`; `run_high`, `run_inv`,
`descent_claim1`, `descent_claim2` — `[propext, Classical.choice, Quot.sound]`.
Statements NOT weakened: `runAbs` = genuine iterated `Nat.dist` fold,
`countOnes` = ν₁, `descent_claim1` (`w ≤ ν₁+1 ⟹ runAbs w el ∈ {0,1}`),
`descent_claim2` (`ν₁+1 < w ⟹ runAbs w el = w − ν₁` exactly). Filed as claim
`lemma54-descent-lean-formalised`, `status: formalised`
(`research/notes/lemma54-descent-lean-formalised.md`). **Scope — abstract core
only:** an arbitrary `{0,1}^L` pattern and arbitrary starting `w`; it does NOT
cover Link A (`v ≤ g*_n`), the composition `g*_n ≤ 2ν₂+2 ⟹ success`, the
reduction from real column dynamics to the `(pattern,v)` model, or the supply
side. **`lemma54-re-derived-proof` is NOT upgraded to proved on the strength of
it** — the full even-domain lemma is strictly more; the honest path is to
formalise Link A and the composition too. The defective "each 2 contributed −2"
passage in `research/notes/lemma54-re-derived-proof.md` is DELETED, superseded
by the kernel-checked case split.

**Directive 48 (audit) — CLOSED, both parts.** The verdict line was
self-contradictory ("ALL AUDIT CHECKS PASSED" after the diagonal-coordinate
erosion-law test refuted) and is fixed: `reduction_audit_corrected.captured.txt`
(and `.captured2.txt`) now print a factual verdict — 45150 cells / 281
columns, 0 violations, no "theorem"/"proved"/"proves" wording (Directive 51
standing rule fully enforced in code). The (D) 1133 constant-1 "violations"
were a transversal-quantity artifact, not a counterexample to the row block
lemma (`b_{k+1} ≥ b_k − 1`, 0 violations). The prefix-determinism identity is
PROVED and filed: `reduction-passage-exact` upgraded to `proved`
(`research/notes/prefix-determinism-proof.md`), the three-line argument
`δ_k(q_n) = |δ_{k−1}(q_n) − δ_{k−1}(q_{n−1})|` making every eps a
stored-prefix entry so the {0,2} cycle and ν₂ are fixed before q_n is seen —
kills Directive 38's circularity worry; machine-verified 0 mismatches (19,900
identity + 59,697 eps-prefix positions). Nothing here is in flight.

## Run state (Directive 36 pivot)

**Directive 51 (audit wording, third recurrence) — CLOSED this attempt (items a and b).** Code/out/reduction_audit_corrected.captured.txt re-captures the fixed audit (sieve 2e6, M=300): identity CONFIRMED 45150 cells 0 violations; biconditional 281 columns 0 violations; verdict line factual with no "theorem". The defective "MACHINE-CONFIRMED as a theorem" line survived only in the stale reduction_audit.captured.txt, not in the source. `reduction-passage-exact` upgraded to status: proved (three-line identity — the fixed-pattern independence IS the triangle recurrence in right-diagonal coordinates; research/notes/prefix-determinism-proof.md; 0 mismatches over 49,873,204 model positions, 59,697 eps-prefix-locality positions).

**Empirical route at ceiling.** 1e9 run (W=50,847,534, 185s, 1.37 GiB):
row-248 STILL capped (b_land = W−248−1, floor=0, genuine=False;
jump ≥ 27,684,003). Geometric doubling (1.765× per giant, R²=0.968) means
each giant costs 1.5×–8× the width of the last; two more → 1e10–1e11
sieve → exceeds 8 GiB cap. **Do NOT queue larger sieve runs.** Settled:
max gap still 64 (175→239), ratio bound gap_i/(j_i+1) ≤ 0.01264
everywhere, oracle passed. Parity: 1 odd (161) of 15 genuine giants,
exact base-rate hypergeometric p = 1.82e-3 (binomial 0.0052; fair-coin 4.88e-4 —
corrected this run, `giant-parity-genuine-15-1e9`). Remaining work is theoretical:
Granville Lemma 5.4 (ν_2 reduction) and CHT Theorem 1.6 — both FULLPDFs
are read and digested (`research/notes/lemma54-re-derived-proof.md`,
`research/notes/cht-2026-summary.md`). **Lemma 5.4 is now PROVED on the even
domain** (claim `lemma54-re-derived-proof`; see Established). **Directive 44
correction:** the theorem is true but the written proof's descent step
("after the ν₂ twos, δ = v − 2ν₂") is FALSE on bounce trajectories
(0→2→0→2, e.g. v=0, ε=(2,2,2)), exactly the δ=0 case Granville discards.
The repair is a case split, not a machine check: if some δ_t ≤ 2 for t ≤ L
then δ_t ∈ {0,2} and absorption carries it; else every δ_k ≥ 4, every 2
subtracts 2, and δ_L = v − 2ν₂ ≤ 2 contradicts δ_L ≥ 4. Write the proof and
Lean-formalise it; **do not run another sampling sweep** — an invariant is
proved by argument, the Lean file only certifies it. The
entire surviving open *mathematical* content is the supply-side linear bound (see below — the abstract core is now kernel-checked in Lean, Directive 50, claim `lemma54-descent-lean-formalised`; the full even-domain lemma still needs Link A + composition + reduction)
ν_2 ≥ c·n. Route B (Granville ν_2) primary;
Route A (ratio bound) empirical fallback; Route C (CHT) calibrated by
authors' difficulty assessment.

**Directive 35 item 1 DONE (this run): right-half {0,d}-block scan.**
`code/cht/scan_right_half_0d.py` at 6e8/depth 400 (196 s, one row live,
exact int64, 3 oracles passed incl. zero b-profile mismatches over 400
rows): the longest {0,d}-block with d ≥ 2 in the right half (columns
j ≥ N′ = ⌊N/2⌋) is **25** (row 14, d=2); d ≥ 4 max is 24 (row 37, d=14);
247/401 rows contain some d ≥ 2 block. Smallest CHT length threshold
T_1 = R_1 − 3R_0 = 5.63e16 (M=8, L=2, R_0=3.36e9) exceeds every observed
block by ≥ 2.25e15×. The leading {0,2} block (d=1, category C, outside
(iii)) reaches 15.66M at row 247 but sits at j < N′ — the column
restriction is confirmed as trivially satisfied. **The {0,d}-block
obstruction family is absent at every scale Theorem 1.6 controls, in the
half where it matters; the theorem does not bite at reachable depths.**
Claim `cht-right-half-0d-scan-6e8`; anchor `research/notes/cht-right-half-scan.md`,
`code/out/cht_right_half_0d_scan.captured.txt`, `_6e8.json`.

## Established

- **Directive 44 dispositions — six new approach files settled.** Attached to G-supply (a):
  `chebyshev-bias-granville-nu2-supply` — the bound it would give is
  ν₂ = n/2 + O(n^{1/2+ε}) from the two-point consecutive-prime mod-4 correlation
  (bit_n = [p_{n+1} ≢ p_n (mod 4)]), conditional at Hardy–Littlewood / Lemke Oliver–Soundararajan
  level. Parked (b): `chip-firing-abelian-sandpile` (path critical group trivial, no conserved mass),
  `ifs-attractor-contraction` (no strict l1/linf contraction on the cone),
  `rsk-greene-growth-diagram-last-passage` (RSK first-row length monotone vs b_k drifts down),
  `ruin-theory-foster-lyapunov-surplus` (probabilistic-ruin machinery needs a measure the primes lack),
  `vectorial-subtractive-euclidean` (no classical subtractive scheme matches).
  **Search discipline (Directive 44 item 3):** the library is closed (Directive 39); the only search
  that may be launched is one chasing G-supply (prime gaps mod 4, Chebyshev bias, BHP-type density),
  and only after the gap is written in `research/REQUESTS.md`. Otherwise stop searching and prove things.

- **Gatti 2020's claimed class-level/prime proof is invalid — located flaw (full text in library).** Gatti, *Gilbreath's Sequences and Proof of Conditions for Gilbreath's Conjecture* (Preprints 202003.0145.v1, 2020; the earlier downloadable form of the MDPI-403 "Gilbreath polynomials" paper) proves the valid-extension machinery (Eq. 2: `k = ±s^{n−1}_1 ± … ± s^1_{n−1} + s_n ± 1`, global anti-diagonal criterion; parity alternation Lemmas 1–3 — the general-class half of the run's parity wave) but **Theorem 4's proof of `min K ≤ p_n ≤ max K` for the primes is invalid**: the right-inequality step assumes its own conclusion ("If p_n ≤ max K, then subtracting 2p_{n−1}…") and derives only a trivial `min K ≤ α` via Bertrand. Also his Lemma 4 (valid-extension set = whole parity interval) is **false in general** — Muney 2026's length-5 hole; even `dim K_S = 2^{n−1}` fails on `{2,3,5}`: `|K_S|=5` (solutions `{1,3,5,7,9}`, machine-checked this run). **No published deterministic bounded-gap/prime-class theorem exists.** Claims: `gatti-2020-theorem4-proof-invalid`, `gatti-2020-lemma4-interval-completeness-refuted`, `gatti-2020-valid-extension-global-formula`. Anchor: `research/sources/gatti-2020-preprints-gilbreath-conditions.full.md`.
- **Older claimed "proofs" and LLM-era preprints — Granville 2026 now re-graded; most others not-load-bearing, do not cite.** Proth 1878 gave no proof (Williams's retraction, quoted in Chase 2024 §7: the actual paper states the property as a theorem). **Granville 2026 "Piercing Gilbreath" (arXiv:2607.04166, cs.CR) — RE-GRADED (Directive 34).** The "not-load-bearing" classification was made off the 6.8 KB `/abs/` landing page; the full PDF (175 KB, 70 theorem/lemma/proof hits, `research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md`) contains Lemma 5.4 (supply-vs-demand budget inequality in right-diagonal coordinates, equivalent to this run's own recharge identity) and Theorem 5.5 (reduces GC to lower-bound ν_2 > n^β, β > α, demand side α = 0.525 unconditional by Baker-Harman-Pintz, shaved to α = 0.52 by Li 2023 — but the demand α is NOT the bottleneck; see `li2023-not-bottleneck`: measured ν_2 ≈ n/2 means any ν_2 ≥ c·n bound suffices, so the real open statement is the linear supply bound ν_2 ≥ c·n). The paper is not peer reviewed; proofs are uneven (Theorem 2.5 is not proved; Lemma 5.4 discards a delta=0 case occurring in 100% of columns). The value is the reduction, not the proofs. Operator measured ν_2/n ≈ 0.49–0.52 on primes below 3e6 (`research/notes/granville-2607-04166-actually-read.md`, `research/notes/lemma54-discarded-case-is-universal.md`). Maréchal, ZARKOUNA, Keen, Ross-class preprints are unverified claims.
- **Verification record, CURRENT (sourced; 4 data points kept distinct):** Odlyzko 1993 to 10^13 (G=635); Plouffe 2025 to 10^14 (arXiv:2510.06688); Colonna 2025–26 to 1.5×10^15 (G=800 at both 6.15e14 and 1.5e15); run's own: depth 1000 (1.27M primes) and wider depth 240 (16.25M primes). Do not conflate.
- **Parity wave (proved, Ross 2026):** any (2, odd, odd, ...) sequence has every row's leading term odd — but odd is NOT 1. The conjecture lives strictly between "odd" and "1".
- **{0,d} closure double edge (proved, one line):** {0,d} is closed under absolute differencing for every d≥2, so the mechanism pinning 1 at d=2 also preserves large disturbances at d≥4 (the CHT obstruction).
- **2-separation is the operative general-class hypothesis** (Ross 2026; consistent with CHT condition (ii) and Eppstein). Chase 2024 gives the first rigorous form (random analogue).
- **The whole conjecture = "the second entry of every row lies in {0,2}".** `A_1=(1, even, even, ...)` because 2 is the only even prime; (odd, even, even, ...) is preserved by the operator; `A_{k+1}(0)=|1−A_k(1)|` is 1 iff `A_k(1)∈{0,2}`. **Proved** (parity induction), checked over full rows to depth 599 + stored slices, and formalised in Lean 4 (IFF, sorry-free). Anchor: `research/notes/reduction.md`.
- **Oracle exists and is checked.** `witnesses.json` (sieve 400000, 33860 primes) reproduces problem.md's rows A_1..A_5 exactly; depth 600, `second_entry_always_0_or_2=true`; second-entry sequence reproduces OEIS A089582's 105 terms exactly. Depth 1000 (sieve 2e7): `first_bad=None`. Wider record: `code/out/wider_width_b.json` (sieve 3e8, depth 240) matches the depth-1000 b-profile rows 1..161 with zero mismatches.
- **Odlyzko's block lemma — RE-DERIVED AND PROVED by this run.** A leading `{0,2}` block of length `n` (positions 1..n) forces `A_{k+d}(1)∈{0,2}` for `d=0..n−1` and `A_{k+d}(0)=1` for `d=0..n`: **exactly n+1 rows; protection constant = 1 (one row per block entry), not the ≈n/2 of problem.md/ROOT.md** (the n/2 claim appears in no source and is refuted). Proved by diagonal-subtriangle argument; verified exhaustively over all 2^n block patterns with adversarial even completions, n=1..11 (122,820 pairs, zero violations). GOAL.md deliverable. The subtriangle apex is exactly the Sierpinski/XOR-fold of the block's bit pattern. Anchor: `research/notes/block_lemma.md`.
- **Rule 90 interior dynamics — PROVED.** Within any {0,2} block, halved entries evolve under XOR (= Wolfram Rule 90 = Pascal mod 2); at depth d the halved entry is the XOR of binom(d,j)-selected initial bits; at d = 2^j the kernel is all-1 (Sierpinski). Confirmed independently by CHT 2026 §1. **The regeneration-TIMING corollary is CLOSED (null, tolerance-dependent) — do not re-assert.** The value identification stands; it says nothing about when the boundary regenerates. Anchor: `research/notes/block_lemma.md`, `research/approaches/rule90-absorbing-boundary.md`.
- **Step law + recharge identity — PROVED as general theorems (this run, any array, no parity/primes needed).** With intruder pair `(x,y)=(row[b_k], row[b_k+1])`: `b_{k+1} ≥ b_k ⟺ (x,y)=(2,4)`, else `b_{k+1} = b_k − 1` (erosion rate exactly 1); recharge `b_k = b_1 + Σ_{events i<k}(j_i+1) − (k−1)` — the `−(k−1)` term IS the Odlyzko constant 1, and (2,4)-events are the ONLY growth mechanism. Drain law (proved corollary): `y_{k+1} = y_k − 2·[x_k=2]` on erosion. Verified on primes (depth 1000, 60 events), 400 random arrays (3,521 rows, 610 events), and all 1,154 sweep sequences — zero failures. Anchor: `research/notes/step_law_proved.md`. **Only the (2,4)-event RATE is open — now sharpened to the inter-giant gap (Run state).**
- **Regeneration = single-row local fact (edge 2, intruder 4), established depth 1000.** Earlier "non-local" refutations were an off-by-one (correct edge index is `A_k[b_k]`, not `A_k[b_k−1]`); the corrected criterion has zero failures over all 998 transitions, exactly 60 events. `c_k ≥ 6` forces erosion (`b_{k+1}=b_k−1`). Do not let stale off-by-one notes block this.
- **Giant-jump mechanism, characterised (computed, depth 147, exact; `code/out/giant_stretches.md`).** At a (2,4)-event, the landing block of row k+1 is the maximal prefix where the halved row k is 1-Lipschitz: `A_{k+1}(i)∈{0,2} ⟺ |h_k(i)−h_k(i+1)| ≤ 1`. The generating stretch over `[b_k, b_{k+1}+1]` (length j+2) is a {0,1,2}-valued chain with step statistics ~ 50% flat, 25% up, 25% down (a random-walk-like 3-state chain; dominant value 0 or 1 at ≈50%), ending at the first adjacent pair differing by 2 (a 0–2/2–0 adjacency, i.e. the first 2 NOT isolated inside 1s); landing bits balanced #0≈#1. The container `[1, b_{k+1}+1]` is the longest 1-Lipschitz stretch of its row in 10/12 giants (k=56 rank 4, k=110 rank 2). Total fresh {0,2} entries generated by the 12 giants: 1,091,362. Giant jumps ≈ current block length (each refills ~1×); jumps grow sublinearly with b overall (log-log slope 0.388, all 43 positive-jump events). **This frames regeneration as a hitting-time problem on a 1-Lipschitz chain — the giants are long ±1-excursions before a 2-step.** Computed, not proved.
- **Edge-sliding mechanism test (computed, refutation budget 0).** Over 1509 random-family runs + 60 prime runs: edge is 0 before depth D (rightmost-2 depth) and 2 at K+D; no early events; 1462/1509 random runs hit the event exactly at E==K+D (primes 44/60, 16 late-unpinned with y≠4, 0 late-2, 0 profile-bad). D: random median 0 max 13; prime median 0 max 4. Prime event gaps mean 2.68 rows, sd/mean 1.13 vs geometric null 0.79 (overdispersed, sim p=0.0024). Confirms the edge-timing mechanism; does not bound it. Anchor: `code/out/event_gap_analysis.captured.txt`.
- **Wider-width record (Directives 27/30/36, computed).** Sieve 3e8 (16,252,325 primes, depth 240, 32.4s): k*=239, 14 live giants. **Sieve 6e8 (31,324,703 primes, depth 400, 96.2s):** resolves row-238 cap — landing 23,163,290, GENUINE. **Sieve 1e9 (50,847,534 primes, depth 400, 185s):** row-248 STILL capped (b_land = W−248−1, floor=0, jump ≥ 27,684,003). 15 genuine giants (0-based [34,56,64,68,94,96,110,112,126,130,134,146,161,174,238]), gaps [22,8,4,26,2,14,2,14,4,4,12,15,13,64], max=64. Ratio bound ≤ 0.01264 everywhere. Parity: 1/15 odd (161), base-rate p=0.0052. **Parity CORRECTED this run (exact without-replacement p = 1.82e-3; see `giant-parity-genuine-15-1e9`).** Geometric fit R²=0.968, factor 1.765/event — empirical route now at ceiling. Anchors: `code/out/pattern_finder_6e8_giants.captured.txt`, `code/out/pattern_finder_1e9_giants.captured.txt`, `code/out/1e9_settlement.md`, `code/out/giant_parity_genuine.captured.txt`.
- **Ducci literature (sourced, four primary papers) — cyclic boundary drawn.** Classical Ducci theorems are CYCLIC (wraparound) and do NOT transfer to the half-infinite Gilbreath operator; Eppstein's escape is the standing witness the half-infinite object differs. What transfers: the mod-2/Pascal law (= this run's proved rule90-interior-xor, now in four peer-reviewed sources) and Chamberland's factored-max + rigidity-equality-case template — the shape any surviving potential must take. Anchor: `research/notes/library-state.md` Ducci section.
- **Mod-4 linearization (invariant candidate).** For k≥1, n≥2 (entries even), `d_{k+1}(n) ≡ d_k(n)+d_k(n+1) (mod 4)` (Odlyzko §2 eq.201; CHT Lemma 3.10 parity formula). Cleanest algebraic handle; parity-only, never fixes the exact {0,2} value (see Ruled out: lift ceiling).
- **CHT 2026 inverse theorem (sourced):** the only ways an array with small non-negative initial data fails to decay to `{0,1}` are long zero-blocks or long shallow {0,d}-blocks (d≥2); random analogue a.s. holds under 2-separated non-concentration. Hypothesis check on the real primes: M=7, L=2, R_0≈4.2e8 ≫ 1000 — **holds-here: no**, the inverse theorem does not bite at any reachable depth. Do NOT re-run the check (`cht-inverse-theorem-hyp-check`).
- **Generalisation families sourced:** Li 2026 modulo-k (primes kn+2, leading entry stabilises to k; odd k<100,000, preprint); Croft's bounded-gap generalisation FALSE via Eppstein (triple-sourced); Chase 2024 = Math. Ann. 388, arXiv:2005.00530; BFT 2023 settles the canonical probabilistic gap models (Banks–Ford–Tao).
- **Restricted classes proved (this run, from the reduction's mechanism):** consecutive odds; any `A_1=(1,2,...,2)`; any triangle reaching a row `(1,c,c,c,...)`, c∈{0,2} — leading 1 persists forever. Proves the mechanism, not that regeneration is entered infinitely often.
- **`block_profile(k) = A000232(k) − 1`**, checked vs OEIS b-file k=1..16; the shifted sequence itself is uncatalogued (nobody should re-search).

## Ruled out

- **Gatti 2020 "prime-class proof" — REFUTED** (invalid Theorem 4; Lemma 4 interval-completeness false in general; see Established). No published deterministic bounded-gap/prime-class theorem exists.
- **`A_k(i) = |Δ_k(i)|` (absolute difference = |signed forward difference|) — REFUTED.** First violation at (k,i)=(3,2): |Δ_3(2)|=4 but A_3(2)=0 — INSIDE the leading {0,2} block; first violation at position 1 is k=4 (|Δ_4(1)|=6 vs A_4(1)=2; 17/20 rows fail). Mechanism: |u−v|=||u|−|v|| iff u·v≥0, and the signed triangle has adjacent opposite signs (first pair (D_3(2),D_3(3))=(2,−2)); any strict local extremum of the gaps (primes: gaps 2,4 at i=2) kills it. Independent sampler: all 60 random 2-then-odds fail within 3 rows. Claim `fwd-diff-identity-refuted`. Approach `sign-coherence-forward-differences` is dead; any linearization must survive cell (3,2).
- **"Jump = next-row {0,2}-run past the block front" — REFUTED as a universal law.** Holds at the giants (13/13 where the run is contiguous with the block) but fails globally: 10 conflicting rows (3,5,6,7,11,13,...), e.g. stall row k=13 has j=0 while the next row's {0,2}-run past the old front is 77 (not contiguous with the block). The correct frame is the 1-Lipschitz chain characterization (Established). Anchor: `code/out/jump_closure_law.captured.txt`.
- **"Route A refuted by sweep" — WITHDRAWN (Directive 16).** Sweep deaths are g_0 startup (all k≤10, 90% by k≤3); they do not bear on the asymptotic event rate. Route A (event rate) is live but superseded as the target by the inter-giant gap (Run state).
- **Small gaps alone do NOT suffice (Eppstein 2011 anti-Gilbreath, sourced, quoted in CHT).** For any unbounded monotone f(n)≥2 there is a 2-then-odds sequence with gaps ≤ f(n) whose right edge leaves and re-enters 1 infinitely often. Kills the blanket "general class with gaps ≤ g" strategy; Colonna's record-page footnote sharpens: deleting 5 (or 7) from the primes gives a 2-then-odds sequence with gaps ≤ 4 (≤ 6) whose second entry is 4 — only g ≤ 3 survives as a plain bounded-gap class. Any general-class claim must state how it beats Eppstein's construction.
- **Bounded-support re-scope "gaps ⊆ {2,4,6}, first gap = 2" — REFUTED as vacuous (Directive 13).** The primes violate every finite gap-support condition; such a theorem says nothing about Gilbreath.
- **Proth "failed proof" — retracted myth; nothing to locate an error in** (Williams's 2020 retraction via email, quoted in Chase 2024 §7). The corrected result is the retraction itself.
- **Rule 90 uniform boundary absorption — REFUTED** (approach `rule90-absorbing-boundary.md`): CHT Lemma 3.7(iii) shows {0,d}-valued blocks persist in all descendants without decrease; Eppstein builds escapes of arbitrary delay. The Rule 90 interior identification is proved and survives; the absorption mechanism is dead.
- **Rule 90 depth-prediction timing corollary — CLOSED (null).** Absolute-depth and jump-timing forms refuted; the relative-depth form is tolerance-dependent (p=0.68 after conditioning) — mild concentration, not a mechanism.
- **Raw run-count/runcount potential r(T) ≤ r — MACHINE-REFUTED** (6,725,600 strings, worst (6,6,6,6,6,6,5,5)); fails even in the {0,2} regime: halved (0,0,1,1)→(0,1,0) (2 runs → 3). Only a corrected weighted/max-factored potential (Chamberland Ducci template) survives, untested.
- **Block-apex pattern-class forcing — REFUTED.** CHT Lemma 3.7(iii): {0,d} blocks persist in ALL descendants regardless of pattern; depth-1000 record fires regeneration on boundary (edge,intruder)=(2,4) only (60/60 at y=4, 0/65 at y≥6). Constant blocks occur in the class (Eppstein). Do not re-propose.
- **Prime-gap mod-6 structure — REFUTED as a constraint machine.** No reduction mod 3 exists (|a−b| mod 3 not a function of residues: (0,1)/(3,1)); "H_k(1) mod 3 ∈ {0,1}" is the conjecture restated. The mod-6 gap statistics never percolate to the left edge in any source.
- **Mod-4 lift is the ceiling — mod 8 and above dead.** `|a−b| ≡ a+b (mod 2^t)` over evens holds iff the smaller entry is divisible by 2^{t−1}: holds t=2, fails t=3 (|2−6|=4 ≢ 0 (mod 8)). Mod 4 conflates exactly the failure values (0↔4, 2↔6). Any invariant on a higher modulus is dead.
- **Backward-extension automaton / minimal-counterexample geometry — REFUTED.** Valid-extension criteria (Alkan et al. 2023 factorial K-criterion; Muney 2026 subset-sum analogue with interior holes, smallest at length 5 for (2,3,5,9,15)) are GLOBAL over the whole prefix — no bounded window, no finite state; Muney's valid-extension set re-describes the regeneration obstruction. Eppstein's class defeat stands.
- **Martingale edge-stall — REFUTED (self-corrected).** The edge is a two-tap coupled XOR recurrence, not a running XOR of fresh bits — no Doob/Azuma bound at the one-bit-per-step filtration.
- **G-supply via generic Markov mixing/anti-clustering of the switch bit — REFUTED as a PROOF STRATEGY (Directive 52).** `code/out/anticlustering_hypothesis.captured.txt`: prime-like (0.55,0.60) worst-min ν₂/w = 0.0714, 11/30 trials violate; Bernoulli/clustered 12–13/30; stationary-0.59 family 11–17/30. Real prime gaps are not a Markov chain and 30 trials of a worst-min statistic is noisy, so this refutes the *strategy*, not G-supply for the primes. **Bet: G-supply stays a named open hypothesis; the deliverable is the conditional theorem at Hardy–Littlewood / Lemke Oliver–Soundararajan two-point level.**
- **"Prime-free provable half" of G-supply — refuted for the SECOND time (Directive 55).** The F₂ covering bound wt(M_n h) ≥ (2/3)wt(h) is dead as a universal statement: consecutive odds (all gaps = 2) has w = n−2 maximal yet ν₂ = 0 (transfer-matrix kernel = span(all-ones); `g-supply-transfer-universal-refuted`, `transfer-matrix-kernel-allones`). This kills G-supply-transfer AS A UNIVERSAL LEMMA ONLY — not the primes (ν₂/w ∈ [0.689,0.867] to N=30000), not the general-class theorem "successful 2-then-odds with w(n) ≥ 2n^0.526", not Route B (Lemma 5.4 budget unaffected). **Repair CLOSED by Directive 57 — the transfer is dead, characterise the
dyadic collapse instead.** The two counterexamples (consecutive odds, period-1;
alternating 2/4, period-2) are both eventually periodic with period a power of
2, so by Lucas their binomial-window XOR sums collapse for large d and
ν₂ = O(1); the live question is which anti-dyadic property of the prime
halved-gap bit string restores ν₂ ≥ c·n (tasks
`test-dyadic-periodicity-prediction`,
`prove-dyadic-periodicity-collapse-lemma`). **Board lesson: a "prime-free
provable half" of this reduction keeps turning out to need a prime hypothesis**
— first Markov anti-clustering (Directive 52), now the F₂ covering bound.
- **Gross/net: "regeneration iff (edge,intruder)=(2,4)" earlier refutations — WITHDRAWN (off-by-one); the criterion is ESTABLISHED** (see Established). The stale note records the failure of the literal wrong-index reading, not of the criterion.

## Numbers

- **Event-rate sweep (2-then-odds class, DONE):** 1154 sequences, 26 families×seeds, batches D=600/W=200k ×48, D=1200/W=400k ×10, D=4000/W=2M ×4, 26 workers, 278 s, exact. Step law + recharge identity fail 0 times everywhere (46,528 rows, 20,013 events). **852/1154 (73.8%) reach b_k=0, ALL within k≤10 (89.7% by k≤3) — death is g_0 startup (rand24 dies iff g_0=4, survives iff g_0=2).** The sweep does not measure the asymptotic rate (Directive 16). Oracle 4/4 numpy-vs-pure-Python. `code/out/event_rate_sweep.notes.md`.
- **Conditional-rate experiment (DONE, Directive 19):** post-startup (k>10) event rate family-independent — pooled λ̂=0.585 (1098/1876), Pearson X² p=0.68 over 8 families, D=400, W=200000, 118 survivors, 0 deaths by D=400. Inter-event gaps k≥11: mean 1.70, median 1, max 14. **λ̂ is a MEAN — superseded as the target: the heavy tail dominates (a mean-rate bound controls the wrong quantity).** Do NOT cite D=40 smoke (predates sign fix). `code/out/conditional_rate_experiment.notes.md`.
- **Depth-1000 stats:** min b=2 (k=1), max b=1,270,444 (k=162); 60 regeneration events in 999 transitions; max single jump 360,698 (k=146); intruder min 4 max 14, 59.6% exactly 4, all ≡ 0 or 2 (mod 4); all 60 regen rows had intruder==4 but intruder==4 is NOT sufficient (36 erosion rows also have y=4). Genuine live-regime longest pure-erosion run: **13** (k=97..109); the "838-row run" at k=162..999 is the finite-width artifact of that record.
- **Block minima record (depth 1000):** `[13,24,96,97,175,2762,5939,31525,31533,31534,733574,1094263]` — the block grows across the computed range; dwell at each minimum 1–4 rows. Block length is not merely bounded away from 0, it increases.
- **Recharge surplus heavy-tailed (depth 1000):** S_1000 = 1,270,603 vs required 998; giants (j>1000) supply 99.76%; the largest are NOT erosion-recovery events (mean gap before big jumps 3.54 vs 2.48 before small; they arrive 1–13 rows after the previous event — "energy stored during erosion" is dead) and do NOT sit on Rule-90/power-of-2 offsets (no separation). Jumps grow sublinearly with b (log-log slope 0.388 over all events) yet each giant ≈ current block length. `code/out/surplus_renewal_structure.md`.
- **Edge-zero-run sharpening — PROVED and machine-checked this run (non-vacuous).** The halved-edge map h ↦ e of a {0,2} block under pure erosion (e_d = XOR_{j≤d} [C(d,j) mod 2]·h[(n-1-d)+j], the Rule-90 convolution) is an F2-linear map, unitriangular in reversed column order, hence invertible: **e = 0 ⟺ h = 0**. So every nonzero block shows edge 2 at least once in its n erosion reads — worst zero-run ≤ n−1 (the original checker's ≤ 2n was vacuous: the sequence has only n entries and the all-zero block achieves n), sharp, achieved only by [1,0,...,0] and mirror. Interior half of regeneration timing: the block's own pattern cannot suppress the edge-2 needed for a (2,4)-event for the whole block life; intruder-4 timing untouched. Three routes (Pascal convolution, literal |a-b| erosion, matrix product) agree over all 262,143 nonzero patterns n≤18; unitriangularity n≤1024. Claim `edge-interior-invertibility-sharpened`; anchors `code/out/edge_map_invertibility.captured.txt`, `.notes.md`. Also executed the run's two other orphaned programs: A089582 crosscheck (run's oracle reproduces the OEIS catalogue's 105 second-entry terms 105/105 — `oeis-A089582-second-entry-catalogue` upgraded from catalogue-read to run-reproduced) and verify_rule90_against_sources (|a−b|/2 = (a/2) XOR (b/2) over 2^8 patterns).
- **ν₂ supply, extended to n=1e5 (incremental run, exact, sieve 2e7):**
  `code/out/nu2_incremental_1e5.txt`. ν₂ stays within `3√(n log n)` of n/2 for
  every n in 1000..100000 (max |ν₂−n/2| = 624 at n=78536); min ν₂/n over all
  n≥1000 = 0.4587; weakest implied exponent min(log ν₂/log n) over samples =
  **0.7658** (» 0.525). Lemma 5.4 hypothesis `g*_n ≤ 2·ν₂(n−1)+2` fails 1 time
  in 99,999. **This sets the honest proof target:** ν₂ = n/2 + O(√(n log n))
  holds numerically to 1e5, so the realistic theorem is a variance / LIL bound
  on the halved-gap XOR-folds, not a super-linear growth statement. Mod-4
  transfer (`code/out/nu2_vs_gap_parity.captured.txt`): the {0,2}-tail cells'
  row-1 ancestor union is the fixed interval [2,n−1] of A_1; halved bits are 1
  iff `gap ≡ 2 (mod 4)`; `ν₂ ≥ w/2` holds at every sample (min ratio ν₂/w =
  0.689 on the sparse {50..3999} set; the dense n∈[50,3000] scan hits a lower
  min 0.5152 at n=53 — same statistic, denser samples, reconciled in
  `code/out/reconcile_nu2w.notes.md`, claim `nu2w-minima-reconciled`). So G-supply reduces to a prime-gap-mod-4 frequency bound, not to the
  absolute-difference dynamics. **Numerical only; not a proof.**
- **Block profile rows 1..40:** `2,7,13,13,24,23,22,21,24,58,97,96,97,96,173,175,175,175,175,290,289,288,739,873,872,871,872,871,870,869,868,867,866,865,2179,2178,2177,2176,2770,2769` (growth by roughly-doubling bursts at k≈15,20,23,35,39).

## Recalled

Durable memory holds the reduction, the oracle generator
(`code/lib/gilbreath.py`), the Odlyzko 1993 full text, the step-law/recharge
proof, the Ducci primary sources, BFT 2023 canonical gap models,
`block-growth-literature-not-covered` (no source studies block-length growth,
jumps, or renewal structure — the geometric-growth/renewal direction is
original to this run and unclaimed). The inter-giant max gap is 64 (15 genuine
giants, 6e8 run; resolved from the earlier 26-vs-64 convention disagreement by
Directive 30). Everything else recalled agrees with what the run has
independently computed; no recalled claim is relied on whose hypotheses fail
here.

## Contradictions

- **Inter-giant max gap: 26 vs 64 — RESOLVED by Directive 30.** The 3e8 run
  capped row 238 (flooring 1), giving live-regime max 26 over 14 giants. The
  6e8 run resolved the cap: row 238 lands at 23,163,290 with flooring
  8,161,173 — genuine. So there are 15 genuine giants, gaps
  [22,8,4,26,2,14,2,14,4,4,12,15,13,64], max=64. The earlier 26 figure was a
  width artifact. Row 248 (0-based 247) is the 6e8 cap (flooring 0) and must
  be excluded. Claim `wider-width-giant-record-3e8` is superseded by the 6e8
  record. The ratio bound gap_i ≤ j_i+1 (verified with 2+ orders margin)
  supersedes "gap bounded" as the conjecture target.
- **Block-protection constant: n/2 vs N — RESOLVED by proof.** Primary sources (Odlyzko 1993 §2, Killgrove–Ralston 1959) and this run's re-derivation give constant **1** (n+1 rows per length-n block); the n/2 claim (`odlyzko-block-lemma-asserted`) is refuted. Treat the proved n+1 as correct.
- **"General-class" framing vs Eppstein — unresolved.** The honest position: the class must be carved down (non-concentration or primes only). Colonna's g=4 deletion example sharpens it. Do not claim a bounded-gap class theorem.
- **`research/CLAIMS.md` is a generated ledger; the contradictions section is clean** (one legitimate row besides the gap figure above). `research/notes/library-state.md` is the authoritative hand-maintained ledger.

## Gaps

- **The open question — theoretical routes only (Directive 36).**
  The empirical route is at its ceiling: row-248 STILL capped at 1e9,
  geometric doubling means next giants need 1e10–1e11 sieve (exceeds 8 GiB).
  **Route B (Granville ν_2 — PRIMARY):** Lemma 5.4 → Theorem 5.5 reduces GC
  to ν_2 > n^β with β > 0.525. Demand α=0.525 unconditional (BHP). **Lemma 5.4
  is now PROVED on the even domain** (claim `lemma54-re-derived-proof`,
  `research/notes/lemma54-re-derived-proof.md`): parity-preserving descent that
  handles the delta=0 case Granville discards as a normal closure case (0→2
  bounce), machine-forced over all {0,2}^L patterns L=1..16 (2.6M even pairs,
  0 violations) and validated on 281 real prime diagonals. The failing-side
  sufficiency test HAS been run non-vacuously with zero counterexamples
  (`lemma54-sufficiency-survives-proper-domain`). The **entire remaining open
  content is the supply-side linear bound ν_2(q_{n−1}) ≥ c·n** (measured c ≈
  0.5, unproved); α ∈ {0.52,0.525} is immaterial once that holds
  (`li2023-not-bottleneck`). **Concrete form of the open bound (measured,
  `code/gap_analysis/nu2_vs_gap_parity.py`, 8 samples n=50..3999)**:
  ν₂'s ancestor window in row-1 is the FIXED interval [2,n−1] of A_1 (the
  k=n−2 cell alone reaches column 2), halved bit h[j]=1 iff gap ≡ 2 (mod 4),
  w(n)=Hamming weight of that window. Measured w/n ≈ 0.60, ν₂/w ∈
  [0.689, 0.867] on the sparse {50..3999} set (min 0.689 at n=100); the dense
  n∈[50,3000] scan (reconciled, claim `nu2w-minima-reconciled`,
  `code/out/reconcile_nu2w.notes.md`) reaches a lower min 0.5152 at n=53. Both
  give ν₂ ≥ w/2 at every sample, so ν₂ ≥ w/2 holds on every sample and a clean
  transfer ν₂ ≥ w/c (small c) is plausible at these scales. So G-supply
  reduces to a prime-gap-mod-4 frequency bound — how often p_{n+1}−p_n ≡ 2
  (mod 4) — NOT to the absolute-difference dynamics. Numerical at 8 samples,
  not proved; this is the one open step of Route B. **Route A (ratio
  bound — fallback):** gap_i ≤ j_i+1, verified 2+ orders slack on 15 giants
  at 6e8/1e9. **Route C (CHT — calibrated):** needs Cramér (open, >BHP);
  Theorem 1.6's right-half {0,d}-block obstruction absent at every reachable
  scale (6e8 scan: max 25 vs threshold 5.63e16).
- **CHT Theorem 1.6 column restriction (Directive 35) — DONE.** The {0,d}-block
  obstruction (iii) is restricted to the RIGHT HALF (j ≥ N′). Right-half scan
  at 6e8/depth 400 (claim `cht-right-half-0d-scan-6e8`): longest d≥2 block is
  25 vs smallest threshold T_1 = 5.63e16 (≥2.25e15× gap) — the obstruction is
  absent at every scale the theorem controls; the theorem does not bite at
  reachable depths. (i) and (ii) remain open (Cramér).
- **The 1-Lipschitz chain reformulation** — computed mechanism, not proved.
- **What remains toward a GOAL.md partial result:** block lemma, Lean IFF, and
  edge-map invertibility are delivered, and Lemma 5.4 is re-derived and PROVED
  on the even domain (`lemma54-re-derived-proof`). **Its abstract core is
  kernel-checked in Lean (Directive 50, claim
  `lemma54-descent-lean-formalised`, `status: formalised`) — the first
  kernel-checked result of the run; but that file covers only the halved
  {0,1}^L core with arbitrary starting w, so the full even-domain lemma's
  abstract core IS kernel-checked in Lean (descent_lemma.lean + link_a.lean +
  lemma54_even_domain.lean + lemma54_composition.lean, all sorry-free; claims
  lemma54-link-A-lean-formalised, lemma54-composition-lean-formalised,
  lemma54-even-domain-lean-formalised); what is NOT yet in Lean is only the
  definitional geometry (g*_n and the right-diagonal reduction from real column
  dynamics), not a gap in the abstract core.** **Directive 47:** the
  supply side is a NAMED OPEN problem, not a gap in the run's own argument —
  ABGS 2011 §9 (claim `abgs-2011-s9-mod4-switch-limit-open`): whether
  `N(a,d,m,x)/π(x)` tends to any limit is open, so no unconditional linear
  lower bound on the mod-4 switch count exists. Route B is therefore a
  CONDITIONAL theorem with that two-point mod-4 correlation bound as its
  hypothesis; a conditional theorem with a precisely identified open
  hypothesis is a genuine deliverable.
- **Library CLOSED except the single G-supply request (Directive 46) + one
  named fetch (Directive 47).** The only searchable gap is a lower bound
  ν_2 ≥ c·n, reduced by rising-sea to a prime-gap-mod-4 frequency claim
  (gap ≡ 2 mod 4 switch bit) — now named-open via ABGS 2011 §9; settling
  literature = prime gaps mod 4 / Chebyshev bias, not Gilbreath. The single
  fetch-and-close target is the MathOverflow "what is known" thread
  (questions/34669): expect no new mathematics, the payload is which routes
  practitioners consider dead. Do not sweep outward from it.