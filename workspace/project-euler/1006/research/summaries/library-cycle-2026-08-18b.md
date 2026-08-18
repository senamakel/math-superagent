# Reference-library cycle (2026-08-18)

## Scope searched
Queries covered Fibonacci factor location, Rauzy graphs, Sturmian weighted factor statistics, formal intercepts/Ostrowski numeration, and symbolic-k aggregation. Triage used Exa and read_sources; no Project Euler solution/forum was searched.

## New locally readable sources
- `research/sources/formal-intercepts-sturmian-2018.full.md` (URL: https://ar5iv.labs.arxiv.org/html/1803.02073). Formal intercepts, Ostrowski representations, and Rauzy graphs; structural framework only, no weighted decimal second-moment algorithm.
- `research/sources/rauzy-ell-graphs-fibonacci-2022.full.md` (URL: https://arxiv.org/abs/2210.08629). Proves strong connectivity of ell-Rauzy graphs of the Fibonacci word; graph structure only, no moment aggregation.

## Triage findings
`read_sources` checked the above plus the factor-location source at arXiv:2207.04304 (already held locally). The factor-location paper gives first occurrences and location formulas; formal-intercept work gives a bijection between fixed-slope Sturmian words and Ostrowski formal intercepts; the Rauzy paper proves strong connectivity. None supplies the missing fixed-dimensional exact aggregation for
\[\sum_{x\in F_k}\operatorname{val}(x)^2\pmod M.\]

The ScienceDirect factor-location page was found but its direct download returned HTTP 403; it was not cited as evidence. Existing local Sivasankar–Rama material covers the same structural direction.

## Durable conclusion
The library now covers the canonical Sturmian/Fibonacci theory, factor-location and Rauzy-graph methods, Ostrowski/formal-intercept methods, and universal Euclidean floor sums. The open mathematical gap remains a proved finite-state/fixed-dimensional aggregation of decimal-weighted second moments over all k+1 factors. Scaling brute force or merely scaling existing O(k) evaluators would not settle that gap.