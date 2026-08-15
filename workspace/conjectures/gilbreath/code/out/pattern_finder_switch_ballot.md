# Pattern-finder: the switch-majority ballot — the one clean structural regularity

Status of every claim: **verified exactly** over the terms supplied (independent
recompute this pass over 41,536 consecutive-pair terms from a fresh sieve to
500000, plus the run's larger verifications cited). Regularities are
conjectures, not proofs; each is labelled with its falsifier.

## The structural fact: `e(n) ≥ 0` — the mod-4 switch-majority ballot

Let `u_k = +1` if `p_k ≡ 1 (mod 4)`, `-1` if `p_k ≡ 3 (mod 4)`, for consecutive
primes `p_k` (k ≥ 2; p_2 = 3). A consecutive pair `(p_j, p_{j+1})` is a
**switch** iff `p_{j+1} ≢ p_j (mod 4)`, i.e. iff `gap ≡ 2 (mod 4)`. Define

    e(n) = Σ_{k=3}^{n} (−u_k · u_{k+1})   =  (#switches) − (#nonswitches)
           among the first n consecutive prime pairs p_2..p_{n+1}.

`e` is a ±1 walk whose step is +1 on a switch and −1 on a non-switch; nonzero
only when `p_{j+1} ≢ p_j (mod 4)`.

**Claim (ballot):** `e(n) ≥ 0` for **all** n ≥ 2 — the mod-4 switches never
trail the non-switches in any prefix.

Verified: the run to 10^8 primes (min e over n≥1000 = 235; final e(10^8) =
9,922,915; only zeros at n=2,4,6,8), and my independent recompute over 41,536
terms (min e = 0 at n=4,6,8 only; final e = 6551). Equivalently `w(n) ≥ (n−2)/2`
where `w(n)` = switch count = Hamming weight of the halved gap bits feeding ν₂.

**Falsifier:** any n with more non-switch than switch pairs among the first n
consecutive primes. None found to 10^8.

## Why this is the condensation of Route B's whole open content

By the run's two numerically-verified transfer legs (must both hold; each is a
separate theorem needing proof):

- **(b)** `w(n)` is the ancestor-window weight of the {0,2}-tail of the prime
  right diagonal (union of row-1 ancestors is the fixed interval [2, n−1]),
  and `ν₂(q_n) ≥ w(n)/2` holds on every n in [17, 30000] (min ν₂/w = 0.5000 at
  n=44). So the ballot `w(n) ≥ (n−2)/2` composes to `ν₂ ≥ (n−2)/4`.
- `(n−2)/4 > n^{0.525}` from n=23 on, and `ν₂ ≥ (n−2)/4` has 0 violations over
  dense n in [23,30000] (min 4ν₂/(n−2) = 1.333 at n=32).

So **G-supply (`ν₂(q_n) ≥ c·n`, the only open step of the primary route
Granville Lemma 5.4 → Theorem 5.5) reduces to the always-nonnegativity of the
mod-4 consecutive-prime switch walk `e(n)`** — a two-point (Hardy–Littlewood /
Lemke-Oliver–Soundararajan-level) statistic. That it is genuinely open is
exactly `abgs-2011-s9-mod4-switch-limit-open`: whether N(a,d,m,x)/π(x) tends to
any limit is open, so no unconditional one-sided (let alone majority) bound on
the switch count exists in the literature. The ballot is the strongest
regularity consistent with (and far beyond what) the sources establish; the
sources (Shiu, Ruzsa, Knapowski–Turan) only push the *opposite* (non-switch)
direction with weak sub-density bounds.

## Sequence tools — negatives (structure is not a closed form)

- `analyze_sequence` on the e-walk: not a low-degree polynomial; residues do
  alternate with period 2 (the trivial parity fact: switch flips residue
  parity, so e only changes on switch steps — a parity bookkeeping identity).
- `find_linear_recurrence` (order ≤ 8): **no** constant-coefficient recurrence.
- ν₂ itself: no OEIS entry, no low-order recurrence, no polynomial (both the
  raw prefix and a sampled-100 of it) — already recorded as an OEIS-miss in
  `pattern_finder_nu2_report.md`; do not re-search.

Consistent with the honest pattern of the whole investigation: the sequences
are prime-number-theoretic — no low-order *arithmetic* lever. The regularity is
**qualitative** (an all-nonnegative ballot / switch-majority), and it is the
one fact whose proof is both necessary and (with the two transfer legs)
sufficient for the supply side.

## Recommendation

The exploitable structure is not a sequence closed form (none exists) but the
**monotone-in-expectation, always-nonnegative switch-majority walk** `e(n)`.
Route B's remaining content is exactly "prove `e(n) ≥ 0`", or name the
requisite two-point mod-4 correlation bound as the conditional hypothesis of a
theorem (Granville Theorem 5.5). The ballot survives a deliberate attack to
10^8 primes; its falsifier and its status (verified-numerically, not proved,
named-open in the literature) are stated above.
