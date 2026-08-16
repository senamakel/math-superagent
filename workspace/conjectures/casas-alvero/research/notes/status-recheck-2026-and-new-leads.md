# Status re-check (2026) and two new source leads

Id: status-recheck-2026-and-new-leads

## What this cycle re-confirmed (authoritative, from live web searches + deep research)

1. **Ghosh claimed proof (arXiv:2501.09272) is still unverified as of early-mid 2026.**
   A Google/Exa search and a `deep_research` on "current status of Ghosh's claimed proof"
   both report: no peer-reviewed publication, no independent confirmation, no published
   gap-finding or refutation, and no new degree settled that changes the open landscape.
   The conjecture remains open; refereed 2024 sources (Schaub–Spivakovsky) still state
   "the smallest degree for which CA_{n,0} is not known is n = 20."
   This is a **status confirmation**, consistent with the held v2 version record
   (research/notes/casas-alvero-status.md, claims ca-status-2025 / ghosh-v2-version-record).

2. **No new counterexamples or settled degrees in 2025-2026.** The searches returned
   only already-held references. Standing: degree 20 is the smallest open (sourced).

## New lead 1 — de Frutos Marín 2013 PhD thesis (arithmetic reformulation)

- Rosa María de Frutos Marín, *Perspectivas aritméticas para la Conjetura de Casas-Alvero*,
  PhD thesis, Universidad de Valladolid, 2013 (defended 11 June 2013), advisor Antonio
  Campillo López. Open access at UVaDOC: https://uvadoc.uva.es/handle/10324/3602 (DOI
  10.35376/10324/3602). Full text file TESIS367-130927.pdf (996.6 Kb).
- **Why it matters:** this is exactly the arithmetic/scheme axis this run's agenda is on.
  Per the UVaDOC abstract and the Portal de la Ciencia record, the thesis:
  1. proves CA is **equivalent to a purely arithmetic problem** — introduces, for each
     degree n, a discriminant Δ(n); its non-vanishing (i.e. Δ(n) ≠ 0) is equivalent to CA
     holding in degree n;
  2. proves equivalences with preservation-of-hypotheses conjectures (propagation to
     powers, to combinatorial variants, preservation under precise coefficient shifts);
  3. gives a **well-defined modular (characteristic p) formulation**: seven "weighted"
     projective schemes; absence of geometric points in characteristic zero is equivalent
     to validity of CA; reduces verification to finding suitable ("efficacious") primes;
  4. proves CA true for many n with at most three prime divisors; n with four or more
     divisors remain out of reach;
  5. concludes computation helps experimentation but its methods are inoperative for
     full verification.
- These claims align with (and predate) the Ghosh/Schaub–Spivakovsky bad-prime program
  the run has verified computationally. **In particular the discriminant Δ(n) with
  non-vanishing ⟺ CA(n) is the arithmetic criterion the run's bad-prime work calibrates.**
- **DOWNLOAD BLOCKED (this environment):** all four attempted URLs
  (uvadoc.uva.es/handle, /bitstream/10324/3602/1/, /bitstream/10324/3602/5/,
  ?format=pdf) failed at the network layer — the server is unreachable from here, not a
  404. The source record (abstract, file name, DOI) is confirmed obtainable-in-principle.
  A later run with working outbound access to uvadoc.uva.es should grab
  `TESIS367-130927.pdf` and digest it. The thesis is a survey + the arithmetic
  reformulation, so it is corroboration rather than new primary content for the already
  verified bad-prime claims — value is in the discriminant Δ(n) statement and the
  seven-scheme modular formulation.

## New lead 2 — Okolo 2025 crank "proof" (record for the claimed-proof family)

- Hanyelichukwu Paul Okolo, *A Resolution of the Casas-Alvero Conjecture and the
  Principle of Simplicity at Maximal Stability*, Zenodo 16651270, preprint 2025-07-31.
- This is a non-rigorous speculative preprint invoking new "forces" (Blackness,
  Retraction, Alignment Dissonance) and an "Organized Complexity" framework, claiming a
  universal law with consequences for particle physics and cosmology. It is a data point
  (the claimed-proof family keeps growing) but **not evidence** and not worth
  downloading. Recorded so nobody chases it as a real proof.

## Recorded, not established

The de Frutos Marín thesis's specific claims (the discriminant equivalence, the seven
schemes) are **asserted-by-abstract/source-record**, not verified here. They corroborate
the run's held claims (bad-prime-criterion, arithmetic-jet-lift) and provide
historical/independent grounding for the arithmetic reformulation, but nothing has been
checked against its full text because the text is unobtainable from this environment.
