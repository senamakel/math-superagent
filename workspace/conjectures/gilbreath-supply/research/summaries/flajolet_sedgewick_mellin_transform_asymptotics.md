# Flajolet–Sedgewick — Average case analysis of algorithms: Mellin transform asymptotics

<!-- source: https://inria.hal.science/file/index/docid/73742/filename/RR-2956.pdf | INRIA RR-2956, 1996 -->

**What this establishes for SUPPLY (librarian — the Mellin-primary behind the
log-periodic phenomenon).** This is the foundational report by which
log-periodic fluctuations in asymptotic expansions of divide-and-conquer /
digital-sum recurrences are derived from the singularities of a Mellin
transform. It is the canonical methodological source for the claim the run's
`log-periodic-oscillation-test-d47` relies on — that
`a(n) = n^α·P(log_b n)` with P periodic is the *generic* signature of
recursions like A006046's `a(2k)=3a(k)`, `a(2k+1)=2a(k)+a(k+1)` — and for why a
straight log-log fit over a bounded window is biased when such a periodic
correction is present (the reason directive 48 warns that the fitted
E = 0.5568 ± 0.002 may be a window artifact of a log₂3−1 truth).

**Importance to this problem.** It does not itself compute A006046 or w*(n);
it supplies the analytic method (harmonic sums → Mellin transform → singularity
extraction → Fourier-expansion of the periodic fluctuation) that *explains* the
oscillation the run is testing for. Together with the
Hwang–Janson–Tsai theorem (explicit F₂(n) = n^ρ P(log₂n), ρ = log₂3−1) it
completes the local grounding of the log-periodic hypothesis: HJT gives the
exact prototype statement, this report the general method that makes such
statements systematic.

**Neither proves nor disproves SUPPLY.** Method/background. Status: sourced.

Full text: `research/sources/flajolet_sedgewick_mellin_transform_asymptotics.full.md`
