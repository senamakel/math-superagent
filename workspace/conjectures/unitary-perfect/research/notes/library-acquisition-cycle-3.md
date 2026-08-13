# Library acquisition cycle 3 — Fibonacci Quarterly primary tier, and the 10^102 provenance resolved

## What was added

| Path | What it is | Verdict |
| --- | --- | --- |
| `research/sources/wall-1983-unitary-harmonic-numbers.full.md` | Wall, *Unitary Harmonic Numbers*, Fib. Quart. 21(1):18–25 (1983), from fq.math.ca (open archive) | **PRIMARY** — classifies unitary harmonic numbers: exactly 23 with `ω(n)<4`, exactly 43 with `n<10^6`; 2-adic-budget/divisibility technique |
| `research/sources/hagis-1987-biunitary-amicable-multiperfect.full.md` | Hagis, *Bi-Unitary Amicable and Multiperfect Numbers*, Fib. Quart. 25(2):144–151 (1987), from fq.math.ca (open archive) | **PRIMARY + provenance-critical** — its intro carries the `n > 10^102` bound for unitary *multiperfect* (triperfect) numbers, and Theorem 1 (no odd bi-unitary multiperfect), amicable scaling rules 4.1–4.3 |

Both summaries written (`research/summaries/…-unitary-harmonic-numbers.md`,
`…-biunitary-amicable-multiperfect.md`) with fenced claim blocks
(`wall1983-unitary-harmonic-classified`, `hagis1987-10e102-is-ump-triperfect-bound`);
both files indexed.

## The 10^102 provenance — RESOLVED as a category confusion

**The held Hagis 1987 text states: "if `n` is a unitary multiperfect number,
then `n > 10^102` and `n` has at least 46 distinct prime factors," citing
Hagis 1984 (Theorem 3, held).** So the previously-orphan "10^102" figure in
GOAL.md/ROOT.md is a **genuine sourced bound — but for the wrong class**:

- It is Hagis's **lower bound for unitary multiperfect (k≥3, triperfect)
  numbers** — a class with *no known members at all*.
- Wall 1975's actual search bound for the *fifth unitary perfect number* is
  `N < W ≈ 1.46e23` (k=2). No 10^102 there.

So "Wall searched past 10^102" was a conflation: the 10^102 bound belongs to
Hagis, applies only to k≥3 multiperfect numbers (not to the UPN case this run
attacks), and is not a search bound at all. This strengthens the existing
`wall1975-bound-is-1e23-not-1e102` claim and resolves the provenance hole
recorded in `research/notes/wall-1975-bounds-and-102-claim.md`.

## Why these two, and why now

FRONTIER lists Wall 1983 (cited 2×: CrossRef chain Fib. Quart. 21(1)) and
Hagis 1987 (cited 2×) among the top-gap rows. Both are free at the official
Fibonacci Quarterly archive (fq.math.ca), which is the canonical source tier for
this exact subject's secondary literature. Neither was in the library. The
unitary-harmonic paper overlaps the budget technique; the bi-unitary paper is
the provenance anchor resolving the 10^102 orphan. Both are adjacent-class
material, not load-bearing for the active divisor-level thread — the
justification is provenance and canonical-tier coverage, per the librarian
mandate to keep the encyclopedic/problem-collection tier complete.

## What this cycle confirms for REQUESTS.md

- **Frei 1978** and **Goto 2007** remain unobtainable (captcha/paywall;
  blocked routes already recorded). Nothing in this cycle grants access.
- The Subbarao–Cook–Newberry–Weber 1972 Delta paper (PDF URL in FRONTIER) is
  a **scanned PDF with no text layer** — download fails with no extractable
  text. New dead end to record: an alternate OCR'd source would be needed; the
  paper is a 1972 Delta note, low value, and not needed for the branch.
