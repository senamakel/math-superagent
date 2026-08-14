# MathWorld Headline News — "Mathematica's Google Aptitude" (Oct 13 2004)

**Source:** https://mathworld.wolfram.com/news/2004-10-13/google/ . Full text: `[[mathworld-google-aptitude.full]]` — `research/sources/mathworld-google-aptitude.full.md`.

Ed Pegg Jr. & Eric W. Weisstein's contemporary report on the Google Labs Aptitude Test, including a worked solution to the exact puzzle that became PE156's d=1 case. Useful as **provenance**, not as a method source.

## What it establishes

- **Historical provenance:** the Google Labs Aptitude Test (Sept 30 2004) contained, as item 17, exactly: "Consider a function which, for a given whole number n, returns the number of ones required when writing out all numbers between 0 and n. For example, f(13)=6. Notice that f(1)=1. What is the next largest n such that f(n)=n?" This is the same puzzle as PE156 (d=1) and Khovanova & Marton's §2.
- **Answer for d=1:** the Mathematica computation prints the fixed points of f(n)=n (f(1)=1, f(n)=n for n in 199981..199990, 200000, 200001) and identifies the sequence as **A014778**. The article's data = MapIndexed[#1 − #2[[1]] &, ...] plot is the "excess" f(n)−n.
- Confirms f(199981)=199981 by direct count ("Checking by hand confirms …").

## Hypotheses and hold-here

- Counts 0..n for digit 1 — exactly PE156's f(n,1). The article does not treat digits 2..9, so it does not cover the full PE156 sum.

## Implication for this run

- Primary-source confirmation that PE156's d=1 problem is the 2004 Google Labs puzzle and that its solution sequence is A014778 (the same sequence whose b-file the run already holds). 
- Corroborates the oracle: 199981..199990, 200000, 200001 are fixed points (matches `code/brute.py`).

## Does not settle

Nothing about the full per-digit sum; nothing about digits 2–9; no bound proof. Not the answer source for the sum.

```claim
id: mathworld-provenance
statement: The Google Labs Aptitude Test (Sept 30 2004, item 17) asked exactly the PE156 d=1 question (f(n) = number of 1s in 0..n; find the next n with f(n)=n), and its published solution identifies the fixed points (199981..199990, 200000, 200001) as OEIS A014778.
hypotheses: decimal base, digit 1, counting 0..n.
holds-here: yes
status: asserted (contemporary news report; matches the oracle brute.py and the A014778 b-file)
bearing: provenance for the puzzle family and for A014778; corroborates the oracle's d=1 solutions.
anchor: research/sources/mathworld-google-aptitude.full.md
```
