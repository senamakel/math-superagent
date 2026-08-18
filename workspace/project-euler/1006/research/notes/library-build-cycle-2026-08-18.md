# Library build cycle: Fibonacci-factor location and Sturmian foundations

Searches were run for Project Euler 1006's underlying mathematics, Fibonacci-word factor locations, Sturmian/mechanical words, and weighted Euclidean floor sums. No Project Euler solution or published answer was searched.

## Sources already available and checked

- [Perrin–Restivo, *A note on Sturmian words*](https://hal.science/hal-00828351v1/file/noteSturmianWords.pdf), full text at `research/sources/perrin-restivo-sturmian-lecture.full.md`, digest at `research/summaries/perrin-restivo-sturmian-lecture.md`. It states Sturmian iff mechanical with irrational slope, defines the factor set, gives the balance criterion, and presents an algorithm generating factors lexicographically.
- [Sivasankar–Rama, *Two-dimensional Fibonacci Words: Tandem Repeats and Factor Complexity*](https://doi.org/10.48550/arxiv.2204.13977), found through Exa search and citation graph. The exact search result reports Theorem 7: if `F(n) <= k < F(n+1)`, explicit windows `z_j^(k)` at positions `j+1` for `0 <= j < F(n)` and `j+F(n+1)-k` for the remaining indices give all `k+1` factors in first-occurrence order. The source was not downloaded because the DOI is already represented by a citation summary in the library; the search result is a lead, not standalone evidence.
- [Cassaigne, *On extremal properties of the Fibonacci word*](https://doi.org/10.1051/ita:2008003), already represented locally; search confirms the Fibonacci slope `alpha=1/phi^2` and first-occurrence/recurrence framework.

## Algorithmic angle

Searches for the custom geometric-weighted floor-square primitive found no stronger primary source than the local AtCoder/OI-wiki/LOJ138 and Beck–Robins references. These are algorithmic analogues supporting Euclidean floor-sum recursion, while the universal second-moment monoid remains this run's derivation and executable evidence rather than a literature theorem.

## Durable result

The library now has a checked primary lecture-note source for the governing Sturmian/mechanical theory and a precise bibliographic/search lead for the factor-position theorem needed to avoid exhaustive factor enumeration. The source URL and local file paths are recorded above.
