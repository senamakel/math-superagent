# Reference-library build: PE1006

Date: 2026-08-18

## Search and triage

Searches were run before any new download, covering Fibonacci-word surveys, Sturmian/mechanical words, factor complexity, factor-location algorithms, and weighted Euclidean floor sums. Citation graphs were also queried for Perrin–Restivo's *A note on Sturmian words*, Berstel's *Fibonacci Words — A Survey*, and the representation-theorem literature. Existing-library duplicate protection correctly refused URLs already represented locally; one Berstel DOI attempt returned 404 and was not retried.

## Sources now available locally

The relevant library was already broad and remains available under `research/sources/` and `research/summaries/`, including:

- Official statement: `problem.md` and `research/summaries/projecteuler-1006-official.html.md`.
- Perrin–Restivo mechanical/Sturmian treatment: `perrin-sturmian-words-lecture2-mechanical.full.md`, `perrin-restivo-note-sturmian-words.full.md` where available, and summaries.
- Fibonacci surveys and factor structure: Berstel bibliographic record, Lothaire chapters, Chuan, Sivasankar–Rama, Fici, Richomme–Saari–Zamboni, and Wen–Wen.
- Canonical catalogue: `oeis-A003849-fibonacci-word.full.md`.
- Euclidean/floor-sum material: AtCoder references, Chtholly/OI-Wiki records, and weighted-floor-sum sources (`ueuclid.py` is the executable implementation).
- Adjacent structure: three-distance, Ostrowski, Christoffel, Rauzy-graph, automatic-sequence, and Fibonacci-factor-location sources.

## Verified mathematical bearing

Perrin's lecture summary records the exact lower mechanical rule
`s_{alpha,rho}(n)=floor((n+1)alpha+rho)-floor(n alpha+rho)`, rotation coding, factor/interval correspondence, and Morse–Hedlund equivalence. For this problem the Fibonacci word is the characteristic word of `alpha=1/phi^2`; hence its factor complexity is `p(k)=k+1`. This is the governing theory for the mechanical-word reduction, while the universal Euclidean monoid evaluates the resulting weighted floor moments.

No published Project Euler solution or answer was searched for or downloaded. The library contains source material and executable verification records, not a copied contest solution.
