# Weakened ladder: the dyadic-periodicity collapse of the ν₂ supply

> Complements — does not supersede — `granville-nu2-supply-corrected.md` and the
> regeneration/recharge ladders. Those ladders bottom out at "the supply side
> ν₂ ≥ c·n is named-open." This ladder is the mechanism *behind* that bottom:
> the two live tasks `test-dyadic-periodicity-prediction` and
> `prove-dyadic-periodicity-collapse-lemma` (Directive 57) have identified a
> concrete structural obstruction the other ladders only gesture at.

**The spine.** By the proved Rule-90/XOR fold (`rule90-interior-xor`), the halved
bits of the `{0,2}`-tail of diagonal `n` are each an F2-linear Pascal-mod-2 fold
of the halved gap bits `h[j] = (gap_{j+1}/2) mod 2` over the fixed window
`[2, n−1]`. By Lucas' theorem the Pascal weights `C(d,j) mod 2` are supported on
the binary submasks of `d`. The live conjecture (Directive 57) is that this makes
an **eventually period-2^k** bit string `h` collapse the fold: `ν₂(q_n) = O_k(1)`.
The two known counterexample families to the universal transfer — consecutive odds
(period 1) and alternating 2/4 (period 2), both *successful* yet `ν₂ = O(1)` while
`w ~ n/2` — are exactly the k = 0,1 cases. So the open supply bound is not a
combinatorial weight inequality (that died at `g-supply-transfer-universal-refuted`),
it is the statement that the prime bit string is **dyadically aperiodic in a way
that forces growth of the fold**. This ladder climbs that axis.

**The five difficulties.**

- `infinite-horizon` — the target quantifies over every `n ≥ N` (every row `k ≥ 1`);
  a finite measurement is a fact about those `n` only.
- `nu2-diagonal-indirection` — `ν₂` lives on the right diagonal of the nonlinear
  triangle, not on the input; the naive `|forward difference|` route is refuted
  (`fwd-diff-identity-refuted`). The fold is the bridge that makes `ν₂` a function
  of the input bit string.
- `dyadic-collapse` — for `h` eventually periodic with period a power of 2, the
  Pascal-mod-2 fold collapses and `ν₂(q_n) = O_k(1)`. This is the mechanism that
  kills the universal transfer and separates every periodic family from the primes.
- `anti-dyadic-certificate` — the precise aperiodicity property Π of the prime `h`
  that *provably* restores `ν₂ ≥ c·n`; this is the theorem to prove, and it is
  prime-free in its statement (Π ⟹ supply, for any `h`).
- `prime-gap-dynamics` — showing the prime gap sequence's `h` actually satisfies Π;
  this is the number-theoretic, named-open content (ABGS 2011 §9,
  `abgs-2011-s9-mod4-switch-limit-open`).

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958), equivalently A_k(1) ∈ {0,2} for every k ≥ 1.
difficulties: infinite-horizon, nu2-diagonal-indirection, dyadic-collapse, anti-dyadic-certificate, prime-gap-dynamics
status: open
```

## Rungs, bottom to top

```rung
id: R-nu2-fold-window
statement: The halved bits of the maximal {0,2} suffix of diagonal n (cells (k, n−k), k = K..n−2) of the prime triangle are each an F2-linear Pascal-mod-2 (XOR / Rule-90) fold of the halved gap bits h[j] = (gap_{j+1}/2) mod 2 = [gap_{j+1} ≡ 2 (mod 4)] over the fixed window j ∈ [2, n−1], independent of where the suffix starts K. The weights are C(k−1, j−(n−k)) mod 2. This is the exact bridge that turns the diagonal quantity ν₂ into a function of the input bit string h.
off: infinite-horizon, nu2-diagonal-indirection, dyadic-collapse, anti-dyadic-certificate, prime-gap-dynamics
stance: settled
merge: This is the base mechanism, already owned: `rule90-interior-xor` (proved) plus the fixed-window union index arithmetic (`g-supply-transfer-measured`, checked). It is a lemma about the target quantity, not a weakened goal — but it is the floor every rung above stands on. Turning `dyadic-collapse` back on is the first move: the next rung records that the fold is *not* weight-preserving, by the two period-2^k counterexamples.
```

```rung
id: R-dyadic-counterexamples
statement: For the two dyadic-periodic families — consecutive odds (all gaps 2, so h ≡ 1, period 1) and alternating 2/4 (h = 1010..., period 2) — the triangle is SUCCESSFUL (A_k(0) = 1 for all measured k) yet ν₂(q_n) = O(1) = O_k(1) while the window weight w(n) = #{j ∈ [2,n−1] : h_j = 1} is ~ n/2. So the fold collapses both families to bounded ν₂ despite maximal switch weight.
off: infinite-horizon, nu2-diagonal-indirection, anti-dyadic-certificate, prime-gap-dynamics
stance: settled
merge: Both families are recorded and checked (`g-supply-transfer-universal-refuted` for period 1, `nu2-transfer-not-restored-by-nondegeneracy` for period 2 and all period-dividing-4 families). They refute only the universal transfer LEMMA ν₂ ≥ c·w, never the general-class theorem — the triangles survive. The next rung generalises these two facts into one theorem: every period-2^k bit string collapses. That is the live task `prove-dyadic-periodicity-collapse-lemma` and it is the first genuinely open rung.
```

```rung
id: R-dyadic-periodicity-dichotomy
statement: Let h : ℕ → F₂ be the halved-gap bit string of a 2-then-odds sequence, and suppose h is eventually periodic. Prediction (Directive 57): ν₂(q_n) = O_k(1) exactly when the period is a power of 2 (P = 2^k); if the period P has an odd factor, ν₂(q_n) grows. Concretely, for periods P = 1,2,4,8 collapse (bounded ν₂) and for P = 3,5,6,7 growth — the dyadic periods are precisely the degenerate ones.
off: nu2-diagonal-indirection, anti-dyadic-certificate, prime-gap-dynamics
stance: open
merge: This is the live task `test-dyadic-periodicity-prediction` (tool_builder): measure ν₂(n) over n = 200..5000 for periodic h with P = 1,2,4,8,3,5,6,7. It is settleable today — a short exact computation, no proof required. If a period-3 or period-5 family also gives ν₂ = O(1), the dyadic story is wrong and this ladder abandons at this rung (record it `failed`). If the prediction holds, the next rung is the prime-free proof of the dyadic half.
```

```rung
id: R-dyadic-collapse-lemma
statement: For h eventually periodic with period 2^k, ν₂(q_n) = O_k(1) as n → ∞. Mechanism (to be proved from Lucas' theorem alone, prime-free): the depth-d diagonal cell is an XOR of h over a binomial window with weights C(d,j) mod 2; by Lucas those weights are supported on the binary submasks of d, so a period-2^k h collapses the sums for all large d.
off: anti-dyadic-certificate, prime-gap-dynamics
stance: open
merge: This is the live task `prove-dyadic-periodicity-collapse-lemma` (theorem_prover), gated on the dichotomy rung holding. It upgrades the two measured counterexamples into a theorem covering every period-2^k family, and it explains the *whole* dead universal transfer in one sentence: the kernel vector all-ones is the period-1 collapse. First move: state the binomial-window identity exactly, apply Lucas to C(d,j) mod 2 = [j ⊆ d] (bitmask containment), and show the period-2^k tail makes the XOR constant for d ≥ 2^k. Turning `anti-dyadic-certificate` back on is the next step: which anti-dyadic property of h is the complement that restores growth.
```

```rung
id: R-anti-dyadic-certificate-implies-supply
statement: There is a precise, checkable, prime-free property Π of the halved-gap bit string h — a natural strengthening of "h is not eventually periodic with period 2^k for any k" (e.g. the fold of h over the submasks of d has positive density of weight 1, or every 2^k-periodic tail model fails) — such that Π(h) implies ν₂(q_n) ≥ c·n for all n ≥ N, for an absolute c > 0.
off: prime-gap-dynamics
stance: open
merge: This is the rung that *defines* the anti-dyadic content, and it is the place the ladder is expected to bite. The dyadic collapse lemma says period-2^k is fatal; this rung asks for the converse-shaped complement — the weakest aperiodicity condition that forces the fold's Hamming weight to grow linearly. First move: prove the *contrapositive* of the collapse lemma — if ν₂(q_n) = O(1) then h must carry an eventual period-2^k structure — and read off Π as its negation. If the contrapositive fails (an O(1)-fold string with no dyadic period exists), the ladder is blocked at this rung and that negative is itself the finding. Turn `prime-gap-dynamics` back on next.
```

```rung
id: R-primes-anti-dyadic
statement: The prime gap sequence's halved-gap bit string h[j] = [p_{j+2} − p_{j+1} ≡ 2 (mod 4)] satisfies the anti-dyadic property Π (whatever precise Π the rung below supplies). Equivalently, ν₂(q_n) ≥ c·n for all n ≥ N. Measured: ν₂/n ∈ [0.42, 0.52] (sampled to 3e6), ν₂ ≥ w/2 at every measured n (min 0.5152 dense, `nu2w-minima-reconciled`), and min(log ν₂/log n) = 0.7658 to n = 1e5.
off:
stance: open
merge: The mean n/2 is unconditional (PNT in arithmetic progressions) but a one-sided lower bound must survive Littlewood-type oscillation, and ABGS 2011 §9 records that whether the consecutive-pair mod-4 frequency tends to ANY limit is open (`abgs-2011-s9-mod4-switch-limit-open`). So this rung is the named-open core; reaching it means `prime-gap-dynamics` has been turned back on and survived. The honest deliverable is the *conditional* theorem: Π(h) ⟹ ν₂ ≥ c·n ⟹ Gilbreath, with Π identified as a two-point mod-4 correlation lower bound.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1, equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently Σ_{events i<k}(j_i+1) ≥ k−2 for all k (recharge identity), equivalently ν₂(q_n) ≥ c·n for all n ≥ N (Route B, Lemma 5.4 proved on the even domain + BHP/Li demand bound).
off:
stance: open
merge: n/a — top of the ladder. The ladder is exhausted exactly when this rung is settled: the anti-dyadic certificate has been proved for the prime bit string with a rate that keeps the fold's weight linear, which is exactly the open supply statement every other ladder bottoms out at.
```

---

## Summary

- **Settled floor:** R-nu2-fold-window (`rule90-interior-xor` proved + fixed-window
  arithmetic checked) and R-dyadic-counterexamples (`g-supply-transfer-universal-refuted`,
  `nu2-transfer-not-restored-by-nondegeneracy` — checked). These are the two facts the
  live tasks already own, reframed as rungs.
- **Attack next:** R-dyadic-periodicity-dichotomy (tool_builder, one short computation,
  settleable today), then R-dyadic-collapse-lemma (theorem_prover, Lucas-only, prime-free).
  Both are already live tasks, so this ladder is exactly the climb the director has
  queued — it does not invent new work, it states the work as a ladder.
- **Difficulty expected to bite:** `anti-dyadic-certificate` — the collapse lemma says
  period-2^k is fatal, but the *converse* (an O(1) fold forces a dyadic-periodic tail)
  is what Π would need, and that converse is not in the library and may fail; if it
  fails, the honest finding is a negative characterisation, which is still a result.
  Behind it, `prime-gap-dynamics` is the named-open mod-4 switch frequency, the same
  core every ladder locates — this ladder pins *which mechanism* the primes must
  defeat, rather than restating the density gap.
