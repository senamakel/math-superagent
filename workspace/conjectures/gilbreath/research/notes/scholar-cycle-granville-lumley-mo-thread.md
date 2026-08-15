# Scholar cycle — Granville–Lumley 2021 and MathOverflow thread verified; both off-target for Route B

This cycle the librarian added two sources and both are already carrying digests
with claim blocks. I verified each against its full text and against the live
Route B target. Verdict: both confirm the existing ledger; neither closes nor
contradicts the one open gap (G-supply).

## 1. Granville–Lumley 2021, "Primes in short intervals: heuristics and calculations" (arXiv:2009.05000; verified against full PDF)

**What it actually establishes** (full text read this cycle, matches the digest):
an explicitly *heuristic* (conjectural, data-supported, not proved) analysis of the
range of the prime count over short intervals `[X, X+y]` inside `(x, 2x]`:

- **M(x,y) = max_X π(X+y)−π(X)**, **m(x,y) = min_X π(X+y)−π(X)**.
- Conjectures by range of `y`: for `y ≤ log x` (up to `(1−ε) log x`), `M(x,y) = S(y)`
  (max admissible-set size); intermediate `log x ≤ y = o((log x)²)`:
  `M(x,y) ~ log x / log((log x)²/y)`; at `y = t(log x)²`:
  `m ~ u₋(c₋t)log x`, `M ~ u₊(c₊t)log x` with `c₊ ≥ 1.015…`, `c₋ ≤ e^γ/2 = 0.8905…`;
  for `y = (log x)^A`, `m ~ σ₋(A)y/log x`, `M ~ σ₊(A)y/log x`.
- Conjectures the **largest prime gap** `max_{x<pn≤2x}(p_{n+1}−p_n) ~ c₋^{-1}(log x)² ≥ 2e^{−γ}(log x)²`
  — *larger* than Cramér's `(log x)²`. Data (worst gap ratio 0.9206 of (log x)²)
  is short of either.

**Where its hypotheses fail / hold here.** It is a *short-interval extremal-count*
paper with no bearing on the **mod-4 distribution of consecutive primes**. The
atomic bit feeding Granville's ν₂ (`gap ≡ 2 mod 4`, a two-point pair switch) is
entirely absent. So `holds-here: n/a` from the digest is correct; the search_claims
ledger rendering (`holds-here: unchecked`) is a mild wording drift but not
harmful — the source simply does not make a ν₂ claim. **Do not cite it for ν₂.**
It is the canonical *demand-side* companion (consistent with BFT 2023: both
reject plain Cramér via divisibility-by-small-primes).

**Bearing worth recording (Route A, not Route B).** The conjectural max-gap law
`~ c₋^{-1}(log x)²` is the *demand-side* of **Route A** (the run's empirical
ratio-bound fallback): if true, gaps grow only like (log x)² — far slower than any
power — while Route A needs gaps to grow slower than the giant-jump `j`.
This *supports* Route A's assumption, but it is **conjectural** (Granville's own
family, not unconditional); the unconditional demand bound remains BHP `0.525`
(and Li `0.52`). Flag as heuristic support only.

```claim
id: granville-lumley-no-nu2-bearing (confirmed)
statement: Granville–Lumley 2021 is a short-interval extremal-count heuristic
  (range of pi(X+y)-pi(X)); it contains NO statement about the mod-4 distribution
  of consecutive primes, hence says nothing about the nu2 supply bound Route B
  needs. Its conjectural max-gap law ~ c_-^{-1} (log x)^2 is demand-side support
  for Route A only, and is heuristic (not unconditional; BHP 0.525 remains the
  unconditional demand bound).
hypotheses: primes; short intervals; heuristic (modified Cramer) reasoning.
holds-here: n/a (no nu2 claim; the source does not touch the two-point mod-4 switch)
status: sourced (full PDF verified this cycle against the digest)
bearing: confirms the digest; do not cite for nu2; may cite as demand-side Cramer/
  Granville short-interval heuristic, flagged conjectural
anchor: research/sources/granville-lumley-primes-short-intervals-heuristics.FULL.full.md
```

## 2. MathOverflow thread (Directive 47 fetch-and-close) — confirms, no new mathematics

Verified against the digest: the thread (Zaimi 2010, Tao 2024) adds **no dead
route** beyond what `research/APPROACHES.md` already records. It independently
confirms three held items:

- **Srilakshmi 2012** hit the run's refuted `fwd-diff-identity` ("forgot about the
  absolute values of the differences") — an independent specialist confirmation of
  that dead end.
- **Tao's** account of Chase 2024's mechanism ("stuck on a long {0,2d}-block",
  ruled out for even d by differences mod 4, harder for odd d) is *exactly* the
  CHT Theorem 1.6 {0,d}-block obstruction and the run's regeneration problem —
  the open content matches the specialists'.
- **Proth 1878** retraction independently confirmed (Tao: "since retracted").

No contradiction with recalled memory. Library is fully closed; the only open
gap (G-supply, the two-point mod-4 switch count) is untouched by both sources.

## Contradictions checked
None. Both sources agree with every established claim; neither conflicts with
recalled memory. The only ledger wording drift found is `granville-lumley-short-intervals-heuristics`
rendered `holds-here: unchecked` in CLAIMS.md vs `n/a` in the digest — cosmetic.

## Sources that do not help (so nobody re-reads)
- **Granville–Lumley 2021** — no ν₂ content; short-interval heuristic only. Use
  for Route A demand-side framing at most, flagged conjectural.
- **MathOverflow thread** — no new mathematics; confirmed-closed already.

## What the run still lacks (unchanged)
The proved supply-side linear bound `ν₂(q_{n−1}) ≥ c·n` (two-point mod-4 switch
count, conditional at Hardy–Littlewood / Lemke Oliver–Soundararajan level) —
see `g-supply-two-point-crux-settled.md`. Nothing in either new source bears on it.
