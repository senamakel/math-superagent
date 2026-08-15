# Scholar digest — the reference library, read in full this session

This session read every source file and summary in `research/` against the goal
(f(n) = min{ D(S) : |S|=2^{n-1}+1 }, max internal degree, known
f(1..5)=1,2,2,2,3 = ceil(sqrt(n))). Prior scholar notes already digested
Liu–Zhou, Barber, Ellis-2011, the four OEIS negative verdicts, and the four
citation digests. What is new here, and what the library as a whole establishes.

## What each new/fully-read source establishes (all under the obstruction)

Every isoperimetric/influence source bounds an **average or outer-boundary**
quantity and none can reach the **maximum internal degree** D(S). This is the
single unbroken conclusion of the library, and it is consistent across all of:

- Harper 1964 (edge isoperimetric: binary initial segments minimise |∂_e S|) —
  an outer total, not D(S).
- Harper 1999 / Keevash–Long 2018 (vertex boundary minimised by Hamming balls,
  near-minimisers close to balls) — outer vertex boundary.
- KKL 1988 / Beckner 1975 / Falik–Samorodnitsky 2007 (max per-coordinate
  *influence* ≥ c·log n/n for balanced f) — a flipping sensitivity, i.e. an
  S→complement edge fraction, not a vertex's internal neighbours. The
  Falik–Samorodnitsky note itself flags: D(S) needs a per-coordinate
  *internal* influence, which these do not give.
- Friedgut 1998 (low average sensitivity ⇒ few coordinates) — total-influence
  structure.
- Ellis 2011 / Ellis–Keller–Lifshitz 2018 / Keevash–Long 2017 (edge
  near-isoperimetric sets are close to subcubes) — stability of boundary
  minimisers.
- Beltrán–Ivanisvili–Madrid 2023 / Durcik–Ivanisvili–Roos 2024 — sharpest known,
  but E[h_A^β] (average of an outer-boundary count). At µ=1/2+1/2^n no max
  internal-degree conclusion.
- Barber–Erde 2018 — survey; boundary profiles only.

So the four "stuck techniques" in problem.md (averaging, edge-counting,
isoperimetry, coordinate/compression induction) are each confirmed stuck: they
bind the growth of *averages*, and the goal is a *maximum* D(S). This is a
recognised dead end worth repeating to other schools.

## Two sources that do help the structure, not the D(S) bound

- **Liu–Zhou 2022** (plain adjacency spectrum: d−2i, mult C(d,i), top d):
  confirms the sqrt(n) lower bound can only come from the SIGNED matrix
  (A_n²=n·I). Any attempt to read sqrt(n) off the plain spectrum is wrong.
- **Barber 2012** (max independent sets of Q_n are exactly the two parity
  classes; balanced ones smaller): pins the d=0 extremal scaffold — S of size
  2^{n-1}+1 is a parity class plus one crossing vertex (internal degree n).
  Not a D(S) bound.

## The OEIS stubs — completed this session (three were unread placeholders)

A007895 (Zeckendorf term count), A033307 (Champernowne constant digits),
A238279 (compositions by runs) — **none is f(n)**, none has any link to the
hypercube. Catalogue noise from an over-eager closed-form lookup. Written as
full verdicts replacing the "not read" placeholders. Same verdict as the prior
four OEIS negatives: no catalogue closed form for f(n); f's sqrt is
A_n²=nI, not any enumerative index.

## Contradictions found

1. **Barber balanced-set /2 — RESOLVED.** The source file's prose wrote the odd-n
   maximum balanced independent set as 2^{n-1}−2^{n-2}(n−1); the claim
   block/ledger has 2^{n-1}−2^{n-2}(n−1)/2. Hand-check at n=3 (no balanced set of
   size 4; max = 2 = {000,111}) proves the **/2 form is correct**, refuting the
   prose (which gives 0). Even-n edge n=2 degenerates to 0 (formula invalid there);
   claim holds from n=3. Not load-bearing for D(S). Checker at
   `code/out/verify_barber_balanced.py` (needs a runner for n=4,5).
2. **Duplicate-claim status disagreement.** `falik-samorodnitsky-edge-isoperimetric`
   and `kkl-balance-influence` each appear twice in CLAIMS.md — once
   `holds-here: unchecked` (from the source note) and once `holds-here: yes`
   (from the summary note). The cautious read (source note: "µ just over 1/2,
   above the stated regime; quantity is total not max") is the right one. These
   bound the wrong quantity for D(S); do not treat them as holding.

## The decisive closed result

The run holds **f(n) >= sqrt(n) for every n**, proved on its own derivation
(A_n signed adjacency with A_n²=n·I; Cauchy interlacing forces λ_max(A_n[S,S])
>= sqrt(n) for the (2^{n-1}+1)-principal submatrix; λ_max <= Δ). This closes
the log–sqrt gap from below (f(n)=Θ(sqrt(n))=ω(log n)) and is independent of
the withheld Huang source. Scheolze's rule satisfied: Liu–Zhou's exact spectrum
gives the base object re-derived.

## What the run still lacks (the gap, stated precisely)

The matching **upper construction** f(n) <= ceil(sqrt(n)) is not on disk (Huang's
source withheld). Until it is rebuilt and its D(S) measured, the certified
statement is `sqrt(n) <= f(n)` (all n) + agreement f(1..5)=ceil(sqrt(n)) — not
exact equality f(n)=ceil(sqrt(n)). That is the single open step on the spectral
thread, and the Clifford/Dirac approach
(`approaches/clifford-dirac-fermionic.md`) is the live speculative overshoot.
Actionable lead (not evidence): Ambainis et al. 2014 sensitivity-complexity
relations, transfer to D(S) unproved.
