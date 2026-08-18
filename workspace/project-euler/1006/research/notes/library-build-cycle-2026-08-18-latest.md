# Reference-library build cycle — 2026-08-18

## Search first
Searched Exa for the official PE1006 statement, Fibonacci/Sturmian factor complexity and mechanical words, explicit Fibonacci factor locations, and weighted Euclidean floor moments. Walked citation graphs from Cassaigne (DOI 10.1051/ita:2008003) and Sivasankar–Rama (arXiv:2207.04304).

## Triage and local holdings
The canonical and adjacent sources were already in `research/sources/` or represented by their exact summaries: Project Euler official statement, Perrin–Restivo, Lothaire/Berstel surveys, Sivasankar–Rama, Cassaigne, OEIS Fibonacci word records, AtCoder floor_sum, OI-Wiki/Chtholly universal-Euclidean material. Download attempts were correctly refused as duplicates. No source for a published Project Euler solution was sought or stored.

## Verified findings
- Perrin–Restivo: an infinite binary word is Sturmian iff it is mechanical with irrational slope; Sturmian complexity is exactly n+1.
- The PE word is the characteristic Fibonacci Sturmian word with digit density/slope 1/phi^2 in this convention.
- Sivasankar–Rama provides explicit finite occurrence/location results useful for independent window oracles.
- AtCoder establishes O(log) ordinary floor_sum; OI-Wiki/related local material supplies the universal-Euclidean weighted extension used by the executable route.

## Status
The library is broad and source-backed. The unresolved work is computational: verify the O(log) evaluator and its reduction to Psi at the target, rather than gather another duplicate bibliography.