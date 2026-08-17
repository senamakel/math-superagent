# Librarian cycle — 2026 status confirmation, L(7) discrepancy RESOLVED

## What this cycle confirmed (no change to the status)

Re-verified from the live web that the run's status record is current through
2026:

- **CA is still open** as an accepted result; the only candidate for a full
  proof remains **Soham Ghosh arXiv:2501.09272** (v1 Jan 2025, v2 Mar 2026
  "Major revisions"), and a targeted deep-research query found **no independent
  verification, no refutation, no published (peer-reviewed) version, and no
  refereed commentary** on its correctness through mid-2026. It remains an
  unverified preprint; the refereed 2024-25 sources (Schaub–Spivakovsky JCA
  2025, Res. Math. Sci. 2024) still treat CA as open.
- **Smallest open degree = 20** remains correct (Castryck et al. 2012,
  Schaub–Spivakovsky 2024/25). No new degree verification (16/18/etc.) has
  changed it.
- All top-of-`derived/FRONTIER.md` leads already held: Schaub–Spivakovsky note
  (2312.08742), bad-primes 2024 (s40687-024-00444-z), upper-bound 2024
  (2411.13967), Draisma–de Jong survey, Polstra convex-hulls, Massri degree-20,
  Castryck degree-12, de Frutos thesis.

## Genuine finding this cycle: L(7) discrepancy RESOLVED (366, not 661)

The previously-"unresolved" degree-7 bad-prime count discrepancy is now
**resolved from a primary source**. Sequence of events this cycle:

1. Found that de Frutos Marín's **2013 PhD thesis full text** (an existing
   held source, never checked against this question) explicitly says "Consta
   de 661 primos" for the degree-7 CA-bad primes, attributed to Castryck
   [CLO-2] — upgrading the discrepancy from "abstract-vs-source" to
   two-held-primary-sources.
2. Checked the thesis's own "niveles de ineficacia" (Def 4.4.1): its
   "ineficaz" set is {p : Y_n(F_p) ≠ ∅}, the CA-bad notion — so the 661 was
   not merely a different scheme (the scheme refines *levels*, not the set).
3. **Downloaded the author's own companion file `badprimes7.txt`** from
   Castryck's homepage
   (`https://homes.esat.kuleuven.be/~wcastryc/code/badprimes7.txt`), now held
   at `research/sources/castryck2012_badprimes7.txt.full.md`.
4. **Counted it: 366 primes**, largest equal to the paper's quoted 135-digit
   prime, no 7, no 127, every prime <127 except 7 present — exactly matching
   the arXiv Theorem 4 sentence.

**Conclusion: the strict degree-7 CA-bad-prime count is 366** (author's own
data). The "661" in de Frutos Marín (thesis + 2015 abstract) is either a
distinct scheme-level ineficaces superset or a misreport; it is NOT the strict
CA-bad-prime list. The run must cite 366 for the d=7 count.

Exact-count script written: `code/librarian/count_badprimes7.py` (mechanical
parse + structural checks + verdict). Pending: a tool_builder/coder execution
for a captured verified run.

## What the library now covers (assessment)

Every angle of GOAL.md is served by a held full text: the status/proof-claims
tier, the minimal-counterexample constraints, the verification bound, the
restricted settled classes, the computational attacks (bad primes n≤5
verified independently of Castryck; n=7 list now held from the author),
the char-p negative controls, the convex-hull/Abel-Gontcharoff analytic side,
and the claimed-proof stress-tests (Ghosh, Lu, Battiston, Dobrowolski). Fewer
than a handful of gaps remain and each is recorded as a blocked/paywalled
fetch (Casas-Alvero 2001 origin, Díaz-Toca–Gonzalez-Vega 2006, Levinson 1944,
de Frutos 2015 note PDF, Sudbery 1973), none of them load-bearing for the
run's scheme-theoretic agenda.
