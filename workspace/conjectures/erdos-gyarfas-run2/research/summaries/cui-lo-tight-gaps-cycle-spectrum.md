# Cui & Lo, "Tight gaps in the cycle spectrum of 3-connected planar graphs"

**Source:** arXiv:2009.02503 [math.CO] (Qing Cui, On-Hei Solomon Lo), submitted 5 Sep 2020, v2 15 Sep 2020. Full text at `research/sources/cui-lo-tight-gaps-cycle-spectrum.full.md` (captured abstract page; the PDF body was not captured by the download, so the detailed propositions below come from the `read_sources` triage of the arXiv page).
**Downloaded:** 2026 (librarian).

## What it establishes

The **cycle spectrum** C(G) is the set of cycle lengths of G. The **circumference** is the length of a longest cycle. For a positive integer k, define

- **f(k)** = the minimal integer ≥ k such that *every* 3-connected planar graph G of circumference ≥ k has a cycle whose length lies in the interval [k, f(k)].
- **f₃(k)** = the analogous minimal bound over 3-connected **cubic** planar graphs.

An interval [a,b] is a **gap** in C(G) if G has circumference ≥ a and no cycle of length in [a,b]. Then f(k) is the least endpoint such that [k, f(k)] is *not* a gap for any 3-connected planar graph of circumference ≥ k.

**History.** Merker (JCTB 2020) showed f₃(k) ≤ 2k+9 for k ≥ 2 and f₃(k) ≥ 2k+2 for even k ≥ 4, and conjectured f₃(k) ≤ 2k+2. Zamfirescu (Discrete Math 2022, arXiv lead) gave infinite families of counterexamples for every even k ≥ 6 with no cycle length in [k, 2k+2], i.e. f₃(k) ≥ 2k+3 for even k ≥ 6.

**Main results (Cui–Lo).**
- f₃(5) = 10, f₃(7) = 15, f₃(9) = 20.
- f₃(k) = 2k+3 for every k = 6, 8, or k ≥ 10.
- For general 3-connected planar graphs: f(k) = 5 for k ≤ 3, f(4) = 10, and f(k) = 2k+3 for all k ≥ 5. This **fully resolves Merker's conjecture** that f(k) ≤ 2k+c for some constant c (here c = 3).

**Characterization of gap intervals (Proposition 3, from the triaged text).** An interval [a,b] is a gap of some 3-connected planar graph iff: a=3 and b≤4, or a=4 and b≤9, or a≥5 and b ≤ 2a+2. For 3-connected **cubic** planar graphs it is a gap iff: a=3,b≤4; or a=4,b≤9; or a∈{5,7,9} with b ≤ 5(a-3); or a ∈ {6,8} ∪ {i ≥ 10} with b ≤ 2a+2.

## Why it matters for this run (obstruction)

This is primary-source confirmation of the exact obstruction `problem.md` names. In the class where the conjecture is *already settled* (3-connected cubic planar, Heckman–Krakovski), the achievable cycle lengths are captured by intervals like [k, 2k+3] — intervals whose length is only about k, while the gap between powers of two at length 2^k is 2^k. A graph can have enormous gaps in its cycle spectrum (e.g. cubic planar graphs avoiding the whole interval up to 2k+2 while having circumference k), and yet a power of two can still slip through as a single special length.

**Concrete bearing on forcing 2^k:** these gap results show interval-cycle techniques alone *cannot* force a power of two in 3-connected cubic planar graphs. The power of two must instead be caught by a *prescribed* length — exactly why the Heckman–Krakovski discharging argument (and not an interval result) is what settles that class. For the general δ≥3 problem this confirms no "cycle of every length in [a, 2a]" route can work, since the gap can be as large as [k, 2k+2].

Cites the classic Erdős 1997 problem paper (Discrete Math 165/166:227–231) — the primary statement source the library confirms is otherwise paywalled — and Merker 2020, Lyngsie–Merker 2019 (cycle lengths mod k), Milans–Pfender–Rautenbach–Regen–West (cycle spectra of Hamiltonian graphs), Thomassen, Sudakov–Verstraëte.

**Hypotheses to check before relying:** results are for *3-connected* cubic planar graphs (a settled class), not the general δ≥3 conjecture. They establish how *large* a gap can be, not the absence of powers of two — every 3-connected cubic planar graph does still contain a 2^m-cycle by Heckman–Krakovski. Note the cab be gaps are for circumference ≥ k; a counterexample to E–G could in principle be an entirely different, non-planar structure.
