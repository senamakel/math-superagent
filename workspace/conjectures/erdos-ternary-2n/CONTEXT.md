# Shared context

**Problem in one line.** Erdős (1979): for `n > 8`, the base-3 expansion of `2^n`
contains a digit `2`; the only digit-2-free powers are `2^0=1`, `2^2=4=11_3`,
`2^8=256=100111_3`. Believed true, open since 1979. This workspace was cleared and
restarted deliberately: nothing in it is inherited, every claim starts unverified.
`GOAL.md` and `problem.md` are the authority; the deliverable is a partial result
(symbolic invariant, middle-digit constraint, subclass proof, sourced bound), not
the conjecture.

**Route this run is directed down.** 3-adic dynamics + a *symbolic invariant*
preserved by `x↦2x` on `Z_3` that the digit-`{0,1}` set `S` violates — not a bigger
sieve. The sieve is an instrument for the dynamics, never the deliverable.

## Established

**This section is current against disk.** `research/CLAIMS.md` holds 20+ claims
(claim blocks per source); `code/erdos/` holds `oracle.py` and `dh_classifier.py`;
`code/out/` holds capture files. Every item below is marked with its evidence
class — proved / checked (computed & cross-validated) / verified-numerically /
asserted-by-source / derived-here-unverified — and its capture file where it has
one. The three witnesses `n = 0, 2, 8` remain the falsification oracle for
every claimed obstruction.

- **SIEVE-EXACT — `|A_k| = 2^(k-1)` exactly for all k≥1** (proved by bijection).
  `A_k = { r mod 2·3^(k-1) : low k ternary digits of 2^r mod 3^k avoid 2 }`.
  Proof: 2 is a primitive root mod `3^k` (order `φ(3^k)=2·3^(k-1)`), so
  `Φ_k: r ↦ 2^r mod 3^k` bijects the period onto the units; a unit's digit
  pattern avoids 2 iff low digit is 1 and the other k-1 digits are in {0,1} —
  exactly `2^(k-1)` patterns. **Checked in THIS workspace**: `oracle_verify.captured.txt`
  confirms `|A_k| = 2^(k-1)` for k=1..26, with `direct_count` and `lift_count`
  agreeing for k≤11 (three agreeing routes); this settles the old `2^k` vs
  `2^(k-1)` contradiction in favour of `2^(k-1)` (k=1: `A_1={0}`, |A_1|=1=2^0).
- **CONSEQUENCE — the modular sieve can NEVER close by counting** (proved). `|A_k|`
  grows like `2^k` while density `(1/2)(2/3)^(k-1) → 0`. A proof must show only
  finitely many *paths* survive, not that the count decays. Reframing: the orbit
  of 1 under `×2` in `Z_3^×` (closure = all of `Z_3^×`) meets the Cantor set `S`
  (digits in {0,1}) in exactly `{1,4,256}`.
- **Oracle verified** (checked, THIS workspace, `oracle_verify.captured.txt`):
  `digit_free(0)=digit_free(2)=digit_free(8)=True`; `digit_free(1)=(3)=(5)=False`
  (`1=2_3`, `3=22_3`, `5=1012_3`). `finite_check([1,1000]) = {2, 8}`; the run's own
  verified digit-free range in [1,1000] is exactly {2,8} (plus 0). The literature
  bounds Gupta n<4374 / Vardi n≤2·3^20 / Saye n≤2·3^45 stay **sourced, NOT
  reproduced here**.
- **Order facts** (verified-numerically, prior + corroborated here): order of 2 mod
  `3^k` = `2·3^(k-1)`; `v_3(2^(2·3^(k-2))-1) = k-1`, so `2^(2·3^(k-2)) ≡ 1 + 3^(k-1)
  mod 3^k` (LTE, c=1).
- **mod-`3^j` injectivity of the survivor-class projection** (verified-numerically,
  `class_injectivity.captured.txt`): `|A_k mod 3^j| = 2^j` for every `k > j`,
  checked j=1..12, k≤24; the `2^(k-1)` survivors project onto exactly `2^j`
  distinct classes mod `3^j`, independent of k, forming a nested tower in j.
- **Value-domain `S ∩ S^{-1} = {1}` in `Z_3`** (proved, complete proof in
  `regularity_findings_7.md`; checked numerically to 3^12 and on the orbit to
  k=26): the only {0,1}-digit 3-adic unit whose multiplicative inverse is also
  {0,1}-digit is `1`. The key step: for `x = 1 + 3^m y` with `y ≡ 1 mod 3`,
  `digit_m(x^{-1}) = 2`.
- **Reflection-invariance refuted** (proved, `pattern_refl2.captured.txt`,
  k=2..26): `A_k` contains no nontrivial reflection pair `{r, P−r}`; only `r=0`
  is self-mirrored, for every k. The `frac→1/2` survivor distribution about the
  midpoint is an *almost*-1/2 limit, never a symmetry — a direct consequence of
  `S ∩ S^{-1} = {1}`.
- **Polarity invariants C1/C2 refuted** (checked, `z3_invariant.captured.txt` +
  `validate_invariant_models.captured.txt`): `Polarity = Σ(-1)^i a_i` with the
  asserted `≡ 0 mod 3` or `≡ 0 mod 2` fails at witness `n=0` (Polarity = 1). The
  proved `c1 even` lemma (G-cong(i)) stands and is consistent with the witnesses.
- **Vacuous-bounded-UNSAT finding** (verified-numerically, `z3_invariant.captured.txt`,
  bound L=40, nmax=63): "no digit-free `n>8`" is UNSAT only because NO digit-free
  `n>8` exists within the digit bound at all — independent of any invariant. **This is
  NOT a theorem**; a bounded `unsat` is never promoted to one. The encoding is tested
  and does find the witnesses 0,2,8 when unrestricted.
- **Dimitrov–Howe Lemma 3.1 and its n=3 examples** (sourced + hand-checked;
  `dh_classifier.py`, `verify_dh_n3.captured.txt`,
  `research/summaries/dh-n3-and-cross-modulus-gap.md`): determinate-power criterion
  `p^i` determinate mod M iff `v_p(M) ≥ i+1`; cross-orders `O'2(M)`, `O'3(M)`;
  Lemma 3.1 gives the extraneous-solution criterion. M1=5440=2^6·5·17 has an
  extraneous solution (2^6 on the 8-loop); M2=2^7·5·17·257 is clean (all summands
  determinate; `ord_257(3)=256` defeats the lemma).
- **`M = 3^k` as degenerate Lemma 3.1 instance / `|A_k|=2^(k-1)` as
  extraneous-solution count** (derived-here-UNVERIFIED, `dh_classifier.py` +
  `bertok-hajdu-cross-modulus-ladder.md`): at `M=3^k`, `M'=1` so `O'2=O'3=1`, both
  divisibility failures always hold, so Lemma 3.1 forces extraneous solutions for
  every datum — this is the pure-3-adic sieve never closing. **The connection to
  `|A_k|=2^(k-1)` as the extraneous count is the load-bearing step and is NOT yet
  established**; it is gated by task `dh-generalize-lemma31`.

## Ruled out

- **Sieve-as-proof** — closed, with the reason: `|A_k|=2^(k-1)`, so counting
  residue classes never kills the digit-2-free set at any finite 3-adic precision.
  This is the starting obstruction in `problem.md`; the run must get past it, and
  re-sieving to larger k after it is not progress.
- **Density trap** — "density of digit-2-free integers → 0" is true and irrelevant;
  it says nothing about the thin sequence `2^n`. Never recorded as a proof.
- **Probabilistic heuristic** `(2/3)^k` — explains why the conjecture is believed;
  proves nothing. Never recorded as a proof.

## Numbers

- `|A_k| = 2^(k-1)`: 1, 2, 4, 8, …, verified to k=26 in prior sessions (direct
  sieve to k=12, lift-count to k=11, order/LTE/witnesses to k=40).
- Literal count of `2`s in `2^n` base 3 (OEIS A260683, sourced): starts
  `0,1,0,2,1,1,1,2,0,4,2,4,…` — value 0 exactly at n=0,2,8.
- Verification bounds in the library (sourced, NOT reproduced here): Gupta 1978
  `n<4374`; Vardi 1991 `n≤2·3^20≈7·10^9`; Saye 2022 `n≤2·3^45≈5.9·10^21`
  (digit-2 AND digit-0 conjectures; Θ(2^K) recursive trailing-digit construction,
  not Θ(3^K) naive).

## Recalled

Marked recalled from Cognee; hypotheses are this exact problem so they hold, but
each needs a primary source re-fetched in this workspace.

- **Narkiewicz (1980):** `#{n≤X : (2^n)_3 omits 2} ≤ 1.62·X^(log_3 2)`, `log_3 2 ≈
  0.63092`. Method: 2 primitive mod `3^k`, only `2^(k-1)` of `2·3^(k-1)` residues
  omit 2. Source noted: Lagarias math/0512006.
- **Dimitrov–Howe (2021, arXiv:2105.06440; Rocky Mountain J. Math):** outside
  `{0,2,8}`, base-3 expansion of `2^x` contains a digit 2 **or ≥ 26 ones**. So any
  counterexample must have `≥26` ones and zero 2s. Residual open case exactly
  "≥26 ones and no 2s". Improving the 26 is the DH-frontier, needing their
  nested-moduli/determinate-power-lifting method handled for larger sums of
  distinct powers of 3.
- **Kaneko–Stoll (2018):** patterns of 0/1 digits are abundant in the exponent
  set — powers of 2 with prescribed ternary trailing patterns exist in a positive
  proportion of n. Shows digit-0/1 patterns alone never run out; reinforces that
  the kill must come from middle/high coupling.
- **Middle digits (Lagarias 2009 §1.6):** combining real top-digit and 3-adic
  bottom-digit control to reach the ~`log_3 2 · n` middle digits is **open**;
  whether high and low digits are "uncorrelated" in a quantifiable way is
  unresolved. The low digits are what the sieve reaches, the high digits what size
  arguments reach; nobody touches the middle. This is the target.

## Contradictions

- **`|A_k| = 2^k` vs `2^(k-1)` — RESOLVED in favour of `2^(k-1)`.** `oracle_verify.captured.txt`
  (checked this workspace, k=1..26) and the `oracle_verify_claim.md` settle it: the hand check
  k=1 (`A_1={0}`, |A_1|=1=2^0) forces `2^(k-1)`; the earlier `2^k` value was wrong.
- Saye's "n≤2·3^45" and Dimitrov–Howe's "≥26 ones" are both sourced-but-not-this-run-reproduced;
  treat as asserted-by-source until re-derived here.
- **`dh_gate_independent.captured.txt` 'MISMATCH' rows are a spot-check bug, not a refutation.** The gate's spot-check sets `actually_det = (canonical-min-exponent == i)`, which is True even for loop powers (e.g. `2^6` on the 8-loop), so every `i ≥ v_p(M)` prints MISMATCH; the criterion `p^i` determinate iff `i < v_p(M)` is confirmed correct by `dh_classifier.py` Part 0 (tail/loop diagram). Fix + re-run + checked claim queued as task `fix-dh-gate-determinacy-spotcheck`; M1/M2 verdicts stand (both PASS).

## Gaps

- **The middle-digit coupling** is the live open piece: a symbolic invariant,
  weight/carry/transducer statistic on the base-2→base-3 conversion, or an
  automaton-invariance argument that the {0,1}-digit set `S` violates but `x↦2x`
  preserves — checked against n=0,2,8. Improving DH's 26-ones bound, or any
  middle-digit constraint, also counts. The value-domain `S∩S^{-1}={1}` result
  (proved) and the anti-orbit result (proved) are the strongest exact structural
  facts held so far; they exclude the reflection-symmetric subclass of
  counterexamples, not all counterexamples.
- **`dh-generalize-lemma31` (open)**: the load-bearing, unverified step of the
  adopted cross-modulus route. The correct mod-q consistency for the unbounded
  equation `Σ_{a∈A}3^a = 2^n` was shown to be **vacuous** (`Dr(q) = F_q` for every
  q coprime to 3 — proven in `cross_modulus_corrected.py`), so the earlier q=19
  "kills" were artifacts of a wrong s=0 proxy. Remains open: is a mixed modulus
  that actually drives the survivor count strictly below `2^(k-1)` (H1) and a
  k+1-term Lemma 3.1 with the same threshold structure (H2) possible at all? The
  coverage proof already suggests H1/H2 may be structurally non-binding in the
  unbounded case.
- No claim in this workspace goes beyond the run's own verified bound (k≤26 /
  [1,1000]) into the literature's cited ranges (Gupta/Vardi/Saye) — those remain
  sourced-not-reproduced.
