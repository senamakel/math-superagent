# MathWorld — Mathematica's Google Aptitude (Oct 2004)

**Source:** https://mathworld.wolfram.com/news/2004-10-13/google/ (MathWorld Headline News, Ed Pegg Jr. & Eric W. Weisstein, Oct 13 2004). Full text: `research/sources/mathworld-google-aptitude.full.md`.

## What it establishes

- **Historical provenance** for PE156: problem 17 of the "Google Labs Aptitude Test" (Sept 30 2004) is exactly the digit-count fixed-point question — "a function which, for a given whole number n, returns the number of ones required when writing out all numbers between 0 and n. For example, f(13)=6. ... What is the next largest n such that f(n)=n?"
- It reproduces the d=1 first solutions by brute-force Mathematica (cumulative DigitCount over 1..500000): positions where the cumulative count equals n are {1, 199981, ..., 199990, 200000, 200001}, and gives the "by hand" check that 1..199981 contains 199981 ones. This is an *independent*, 2004-era reproduction of the statement's fixed points 0 (origin-excluded), 1, 199981 — same oracle set the run's brute.py reproduces.
- Points to OEIS A014778 for the full sequence, and to the same Google puzzle family the Khovanova–Marton paper credits.
- The rest of the page is unrelated Google interview-puzzle content (WWWDOT-GOOGLE=DOTCOM, look-and-say, resistance on a lattice, etc.) — no bearing on PE156.

## Implications for PE156

- Nothing new mathematically (no closed form, no bound, no proof) — the 2004 Mathematica scan is the same O(n·digits) brute force the run's oracle uses, extended only to 500,000.
- Useful as: (a) confirmation that f(13)=6 and the first-solutions run are the problem's own canonical examples (they agree with the run's oracle output); (b) provenance: the puzzle predates Project Euler, being Google's own — but the *solving* theory remains Khovanova–Marton + the closed form, not this page.

## Does not settle

- Any question of bound, finiteness for d>1, or the sums s(d). Not a primary mathematical source; treat as historical record only.