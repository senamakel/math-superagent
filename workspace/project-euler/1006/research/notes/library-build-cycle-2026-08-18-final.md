# Reference-library build cycle — 2026-08-18

## Searches
Searched Exa for (i) Fibonacci/Sturmian factor complexity and mechanical words, (ii) explicit Fibonacci factor locations, (iii) universal Euclidean weighted floor sums, and (iv) the official PE1006 statement. Results identified Perrin–Restivo, Sivasankar–Rama, and OI-Wiki/Euclidean references.

## Local availability
The canonical sources were already present in `research/sources/` or their summaries: official Project Euler statement, Perrin–Restivo, Sivasankar–Rama, and universal-Euclidean/OI-Wiki material. Download attempts for those URLs were correctly refused as duplicates. The English OI-Wiki URL failed extraction/404 variants; the Chinese canonical page is already stored as `research/sources/oiwiki-universal-euclidean-floor-sum-2026.full.md` with source URL header.

## Verified usable findings
- Perrin–Restivo, Theorem 1: an infinite binary word is Sturmian iff it is mechanical of irrational slope; Sturmian complexity is exactly `n+1`.
- The PE word is the Fibonacci/Sturmian characteristic word with digit density/slope `1/phi^2`; this fixes the mechanical-floor representation.
- Sivasankar–Rama gives explicit enumeration/location structure for Fibonacci factors, useful for finite checks.
- OI-Wiki/AtCoder-style Euclidean floor-sum recursion is the algorithmic basis for constant-size weighted floor moments; the local run has already executed and verified the universal-Euclidean monoid.

No Project Euler solution or answer was searched/downloaded. Remaining PE1006 work is evaluator wiring and execution, not reference acquisition.
