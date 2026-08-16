# Librarian cycle 2 — Berger source, claimed-proof family update, OEIS misses

## Sources added this cycle

| File | What it is | Full text? |
| --- | --- | --- |
| `research/sources/berger_ens-lyon_casas-alvero-cours.full.md` | Laurent Berger (ENS Lyon, UMPA/CNRS/IUF), "The Casas-Alvero Conjecture", course-project handout (CApromys.pdf, perso.ens-lyon.fr) — university source | **YES** (indexed; summary digest at research/summaries/berger_ens-lyon_casas-alvero-cours.md) |

The Berger handout states the conjecture (monic, char 0, over C), the resultant/Nullstellensatz reduction, the Hasse-derivative char-p formulation with the F_23 witness x(x−1)^4(x−8)(x−18) (Exercise 12 — matches the run's `charp-witnesses` claim), and the p-adic valuation proof of the p^k / 2p^k theorem. **It says "It is known for d ≤ 19 as well as for any d which is a prime power or twice a prime power."** This is consistent with the held primary (Castryck et al. 2012, §6.5: open degrees for d ≤ 100 start at 20):

- d ≤ 7: Diaz-Toca–Gonzalez-Vega 2006 (Gröbner);
- 8=2^3, 9=3^2, 10=2·5, 11, 13, 16=2^4, 17, 19: prime powers / twice prime powers (Graf-von-Bothmer et al. 2007);
- 12: Castryck et al. 2012 (verified);
- 14=2·7, 18=2·3^2: twice prime powers;
- 15=3·5: 3p^k family, p=5 ≠ 2 (Draisma–de Jong).

So every d ≤ 19 is settled by a held family, and the smallest open degree remains 20. **Consistency confirmed by hand against the held settled-classes claim — no new claim needed.**

## Claimed-proof family updated (triage, NOT downloaded)

Two more 2025 "complete proofs", both Zenodo, both zero citations, both nonstandard frameworks, both triaged as data points for the claimed-proof family rather than evidence:

1. **Okolo 2025** — already recorded (research/notes/status-recheck-2026-and-new-leads.md).
2. **Keenan Leggett, "A Proof of the Casas-Alvero Conjecture within a Dyadic Dynamic System"** (Zenodo 17363753, 2025-10-16, 0 citations). NEW this cycle. Topics: dynamical systems / fractal systems. No peer validation. Not downloaded; recorded here so nobody chases it as a real proof.

Pattern stands (from `dobrowolski-2017-withdrawn`, `battiston-withdrawn`, `ghosh-2025-claim`): every claimed complete proof of CA is either withdrawn with a named error or remains an unverified preprint. CA remains open; Ghosh 2501.09272 v2 (Mar 2026) remains the strongest claim and still unverified.

## OEIS misses (recorded, do not search again)

- Degree-5 bad primes `[2,3,7,11,131,193,599,3541,8009]`: **no OEIS entry matches** (checked this cycle).
- Degree-20 certified-bad binomial-criterion primes `[2,3,5,7,11,13,17,19,37,67,89,103,109,113,173,419,1223,15269]`: **no OEIS entry matches** (checked this cycle).

Both are bad-prime *sets*, not growth sequences; no closed form is catalogued. Structure must come from the problem (the minor criterion J_T of Schaub–Spivakovsky 2411.13967).

## Status re-confirmation (live search, 2026)

- Ghosh arXiv:2501.09272 still: preprint, not withdrawn, not peer-reviewed, no independent validation found. (Frontier "cited by 0" via OpenAlex for the 2025 proof.)
- No new settled degree, no new counterexample construction found in 2025–2026 searches. Smallest open degree remains 20.
- Berger's "d ≤ 19" claim is the only phrasing that even looks like it could extend the boundary; the hand-check above shows it is exactly the union of held settled families, so no new claim arises.

## Gaps still open (both previously documented; re-filing blocked by claim-matching)

1. de Frutos Marín 2015 full text / 2013 thesis: resolves the L(7)=661-vs-366 discrepancy (uvadoc.uva.es network-blocked; see research/notes/defrutosmarin2015-combinatorios-corroborates-badprimes.md).
2. Casas-Alvero 2001 origin paper full text: primary statement of the conjecture (ScienceDirect 403; see research/notes/librarian-cycle-2026.md).

Neither is re-fetchable from this environment; both are recorded with the exact falsifier each would settle.
