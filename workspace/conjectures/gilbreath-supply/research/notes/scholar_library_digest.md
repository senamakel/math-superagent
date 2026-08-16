# Scholar library digest — what the reference library establishes for SUPPLY

This is the scholar's pass over the full reference library, recorded after
recalling the run's established state (CLAIMS.md, ROOT.md, threads) and the
durable memory. It answers: which sources bear on the single hypothesis (can the
fold Φ do work the switch-density form cannot see), which do not help, and which
contradict each other or recalled memory. Each source-backed finding was also
stored with `remember_memory`.

## The single hypothesis and what the library converges on

The run exists to test: **can the fold Φ = Pascal-mod-2 (Rule-90) submask-XOR map
force `wt(Φ_n h) ≥ c·n` from an arithmetic input weaker than positive mod-4
switch density?** Every source relevant to the arithmetic-input side of SUPPLY
converges on the same picture (thread `switch-side-gap`):

- **ABGS 2011 §1:** the consecutive-pair frequency problem is open and
  "cannot be treated using L-functions". §9: even equality of pair-class
  frequencies is open.
- **Lau 2024:** even ONE non-constant 2-term pattern (1,3)/(3,1) mod 4 is not
  known to occur infinitely often.
- **Shiu 2000, Freiberg 2011, Maynard 2016:** the EQUAL (constant-pair) side is
  fully proved (arbitrarily long, in short intervals, positive density) — the
  WRONG direction.
- **LOS 2016:** switch side conjecturally PREFERRED (≥1/2) but only a conjecture.
- **Rubinstein–Sarnak / Granville–Martin:** single-residue races already
  oscillate with positive-density leads — pair races are strictly harder.

So the arithmetic input SUPPLY's reduction needs is unproved and
L-function-inaccessible; that is why the fold attack is the live route (GOAL
priority 2, request `walsh-spectral-subset-b904`).

## Sources that bear directly on the fold route (help)

| Source | What it establishes | How it bears |
| --- | --- | --- |
| **Szechtman** (arXiv:2405.10352) | Lucas + Kummer restated; subspace of "p=2 not special" | Confirms the submask-XOR foundation of Φ; supplies the row-sum cancellations that drive dyadic collapse |
| **Mestrovic** (Lucas survey) | `lucas-submask-odd`: C(n,m) odd iff m binary submask of n | The exact engine making each Φ cell an XOR over submasks |
| **Meshulam** (2003/2006) | divisor-sharpened Walsh uncertainty on (Z/2)^n | Primary ref for the Walsh-coordinate side of `walsh-spectral-subset-b904`; extremals = subspace indicators = exactly the low-weight structured inputs the closed doors forbid |
| **Tao** (2005) | additive bound |supp f|+|supp f̂|≥p+1, + Meshulam iteration, sharp | Additive companion; same directional caveat |
| **Matusiak–Özaydın–Przebinda** (2004) | Donoho–Stark product bound, equality = subgroup indicators | Canonical ref; equality cases = the obstruction |
| **Pivato** (math/0210241) | entropy neither necessary nor sufficient for randomization by Rule 90 | Formally kills the "h is complicated" family (matches five closed doors) |
| **Pivato–Yassawi** (0108083, affine-limit-II) | harmonic mixing + diffusive ⇒ F^j µ→Haar at density-one times; MRF harmonically mixing | Names "harmonic mixing" as the arithmetic property of h to check for the density-1 form |
| **Pivato–Yassawi** (2006 Thm 7.1) | Φ=1+σ randomizes µ iff µ is Lucas mixing | Sharp characterization; the finite-prefix transfer from it is the central gap |
| **Takei** (2017) | Rule 90 drives strong-mixing input to uniform (Cesàro) | Measure-rigidity confirmation of the same picture |
| **Rampersad–Wiebe** (2309.04012) | run-length transforms 2-regular; Thm 20 exact 0/1 structure; averages ~1.2^r nonlinear | Precedent that F₂-binomial sums can have exact structure; CAUTION: not the fold itself, average nonlinear |
| **Bacher** (0708.1430) | mod-2 Pascal determinant/LU via recurrence matrices | Structural context; does NOT give the rank of the rectangular Φ_n |
| **Binary Steinhaus** (Rule 90) | symmetric subspaces dim ~n/2, ~n/3; binomial det detects generating sets | Quantifies that Φ's linear structure already contains O(n) collapse subspaces — reinforces wt must come from h's arithmetic |
| **Odlyzko 1993** | {0,2} reduction quick; deep-large cells rare & gap-driven | Situates ν₂ as suffix length; the object exists and is well-behaved |

## Sources that do NOT help (and why, so nobody reads them again)

- **Odlyzko index page** (odlyzko_gilbreath): bibliography, no claims; the real
  source is Odlyzko 1993 already held.
- **Chase random-Gilbreath** (2005.00530): proves convergence for *random*
  small-gap sequences; the primes are deterministic, and it's about the leading
  term (Gilbreath), not ν₂'s suffix length. Plausibility only.
- **Encyclopedia Gilbreath**: definitional.
- **Maynard dense-clusters, Freiberg, Shiu expository**: all strengthen the
  EQUAL side — the direction SUPPLY does not need; they only *confirm* the
  switch side is the barrier (useful as contradiction/context, not as tools).
- **granville_martin / rubinstein_sarnak**: single-residue races; pair races are
  strictly harder; context for the barrier, no tool that crosses it.

## What the library does NOT settle (gaps handed to research)

1. **Finite-prefix transfer** (thread `finite-prefix-transfer`): converting the
   ergodic "Lucas mixing ⟺ randomization at density-one times" into a
   quantitative `wt(Φ_n h) ≥ c·n` for the single prime string at all large n.
   Not in any source. This is the run's central gap.
2. **A Walsh/subset-sum lower bound on `wt(Mx)` for a submask-XOR map M**
   independent of h's complexity (request `walsh-spectral-subset-b904`).
   Meshulam/Tao/Donoho-Stark fix the Walsh-side support bounds and their
   extremals, but these are support bounds, not image weights; the extremals are
   exactly the forbidden low-weight inputs.
3. **The weakest arithmetic input on h forcing wt(Φ_n h) ≥ c·n** (GOAL priority
   2): bounded autocorrelation / second-moment / Walsh-coefficient / submask-XOR
   input — none priced yet.
4. **s2_N → 0** (density-1 form via Chebyshev) or finiteness of the exceptional
   set (stronger pointwise) — in-house computation, not literature.

## Contradictions flagged

1. **`rw-not-the-submask-xor-fold` contradicts `rw-described-as-the-fold-itself`.**
   Earlier abstract-based note called Rampersad–Wiebe "the fold itself"; reading
   the full text shows their sums are over k of products C(·)C(n,k) (run-length
   transforms), NOT the submask-XOR zeta transform. The corrected reading stands;
   the paper does not bound wt(Φ_n h). (Recorded in `research/CLAIMS.md`, and now
   in memory.)
2. **`r-finite-verified-contradicted` vs the settled rung R-finite-verified.**
   The "ν₂/n ≥ 0.42 for all [50,4000]" rung is false (10 counterexamples, all
   ≤274); the correct statement is ν₂/n ≥ 0.42 for all n ≥ 500.
3. **ABGS vs LOS (emphasis, not fact):** ABGS leave even positivity of switch
   density open; LOS conjecture it is ≥1/2 always. Both can be true (ABGS = open,
   LOS = conjecture); the summary flags this so nobody treats LOS as a proof of
   switch density. Not a factual contradiction.
4. **nu2_terms.txt superseded:** ν₂(53)=19/ν₂(64)=28 in the old file are wrong;
   three exact routes give 18/27.
5. **ν₂/w row:** 0.7049 quoted is UNVERIFIED (independent recompute 0.597@105);
   must not be cited.

## Memory status note

Cognee `recall_memory`/`relate_memory` returned 404 ("No data found") for the
whole run, even though this run's `remember_memory` calls returned stored note
IDs — a read-back inconsistency on the backend. The durable findings ARE stored
via the 11 successful `remember_memory` calls (they returned IDs), so a later run
with working recall should see them; if recall is still broken, the claims live
in `research/CLAIMS.md` and `research/ROOT.md` and the summaries on disk.

## What was added this pass

- Persisted 11 durable, source-backed findings to Cognee (one per memory call):
  the SUPPLY linearisation + excess identity, the fold-rank/binomial fact, the
  five closed doors, the switch-density parity barrier, the measured values, the
  counterexample-structure trio, Lucas/submask, the Walsh-side uncertainty
  bounds, the Pivato–Yassawi/Takei mixing facts, the fold machinery (Bacher,
  Szechtman, Rampersad–Wiebe), the equal-side literature, and the computed
  contradictions.
- Classified every source in the library as help / no-help with the reason.
- Flagged the contradictions (Rampersad–Wiebe overstatement; the 0.42 rung; the
  ABGS/LOS emphasis difference; the superseded tables; the unverified ν₂/w row).
- Named the gaps the library still leaves open (finite-prefix transfer, the Walsh
  subset-sum lower bound, the weakest-arithmetic-input question, s2_N→0).
