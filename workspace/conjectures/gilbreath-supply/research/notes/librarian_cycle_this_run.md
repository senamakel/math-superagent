# Librarian cycle — this run's audit (fresh determination)

**Verdict: NOTHING FURTHER.** No new source this cycle. No fetch warranted.

Independent re-audit of the live on-disk state (not a rubber-stamp of the three
prior terminus determinations). Read ROOT.md, REQUESTS.md, FRONTIER.md top rows,
the open-request audit notes, and the zero-byte/no-material cycle notes directly.

## What I checked directly, and found consistent

1. **The library passes the phase-1 test** (`research/ROOT.md`): structure of a
   minimal counterexample (kernel collapse, single-sparse amplification, dyadic/
   2-regular structure — with the conjecture that no minimal counterexample
   exists and the counterexample shape to keep hunting is a prime-realizable h
   with o(n) ones yet linear fold weight), verification bounds (pointwise 40000,
   dyadic 2^25, dyadic 40000, second-moment 40000), and the three settled
   restricted classes with hypotheses (uniform-input rank-told; all-ones kernel;
   anti-dyadic balanced). This is the completion record phase 1 requires.

2. **No library gap is open.** The single request `walsh-spectral-subset-b904`
   is a theorem to be derived in-house from held sources: Yoshida Lemma 2
   supplies the leading-row weight floor `2^popcount(d_min)` (sublinear, does
   not close the request — the linear `c·n` gap is open, but it is a theorem
   gap, not a paper gap); Meshulam/Tao hold the Walsh-uncertainty side; the
   downset-row-intersection formula + Krawtchouk machinery hold the
   second-moment side.

3. **FRONTIER's ranked tier is fully held and digested.** Cited-by-3 (Hoi 2025
   comparative PNT bibliography; Granville–Martin *Prime Number Races*) and the
   cited-by-2 core (Tao HOF analysis, Allouche–Shallit k-regular/automatic,
   ABGS prime residues, Lacasa, LOS) are all on disk with claim-bearing
   digests. The 653 cited-once candidates are supply-chain noise or already-
   digested; naming one that answers the surviving question is not possible.

4. **The only flagged new lead is correctly left unfetched.** Saumard–Wellner
   2014 (log-concavity review) would make the hypergeometric strong-log-
   concavity fact behind the two open G-threshold lemmas *cited* rather than
   self-proved, but the run's own note judges it self-provable and no later
   role asked to lift the freeze for it. Fetching would be a directive-7/27/30
   freeze violation with no information gain.

## The surviving open gaps (all theorem gaps, none a library gap)

1. **G-threshold-asymptotic-zero** — `(1/n)Σ_d K_w(2^popcount(d);n)/C(n,w) → 0`
   for every fixed θ ∈ (0,1/2). Hypergeometric mode-bound engine
   `|E[(-1)^X]| ≤ max_j P[X=j] = O(1/√(1+Var X))`.
2. **G-threshold-concentration** — `Var(ν₂(n)) = o(n²)` at every fixed θ.
3. **`E[S(n)²]=O(n)`** for the prime gap-parity string (density-1 SUPPLY via
   Chebyshev); the subgaussian tail is the stronger pointwise route.
4. **Finite-prefix transfer** from Lucas-mixing randomization to the single
   fixed-string fold.

None of these is answerable by a downloaded paper; each is an in-house
F₂/hypergeometric derivation or number-theoretic theorem.

## Recorded state (for the next cycle)

- Cognee recall is 404 this run; memory misses are not evidence a subject is
  unrecorded — durable state lives in research/ROOT.md, research/CLAIMS.md,
  and the per-note claim blocks.
- The pass-3 head is concluded (CONCLUSION-PASS3.md: threshold weight
  sublinear, `w*(n) = n^0.555·P(log₂ n)`, exponent 0.555 fitted, log-periodic
  factor amplitude ~0.07; `1/2` and `log₂3−1` ruled out; `5/9` not separable).
- Three prior librarian determinations (audit_pass3_closed, pass3_terminus,
  audit_this_cycle) all reached NOTHING FURTHER; this cycle's independent
  re-check agrees and adds no new fetch.
