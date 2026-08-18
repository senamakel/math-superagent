# Reference-build status

## Search and library coverage

This cycle searched for: Fibonacci/Sturmian factor complexity; exact factor-position and factor-enumeration theorems; weighted factor statistics; Fibonacci/Ostrowski automata; Rauzy graphs; and universal Euclidean weighted floor sums. Existing sources were checked before fetching. The library already contains the official statement, Sturmian references, Fibonacci-automatic decision algorithms, factor-position papers, Rauzy-graph papers, Ostrowski addition, and universal-Euclidean notes.

Newly stored source: `research/sources/subword-complexity-decomposition-2014.full.md`, with digest `research/summaries/subword-complexity-decomposition-2014.md`. It establishes that Sturmian languages lie in the linear-complexity class W2, but does not establish a weighted decimal second-moment algorithm.

Several attempted downloads were correctly refused because the URLs already existed in the library; their digests were read instead:
- `research/summaries/mousavi-schaeffer-shallit-fibonacci-automatic-ar5iv.md`
- `research/summaries/sivasankar-rama-fibonacci-factors-2022.md`
- `research/summaries/ostrowski-numeration-addition-finite-automata.pdf.md`
- `research/summaries/rauzy-ell-graphs-fibonacci-2022.md`

## Mathematical status

The governing theory is Sturmian word theory: the limit of the finite Fibonacci words is the characteristic Fibonacci Sturmian word, hence it has exactly k+1 distinct length-k factors. Mechanical-word and Ostrowski/Fibonacci-automatic descriptions give structural access to factors. They do not, by themselves, compress the decimal-weighted square sum to fixed dimension.

## Computation status

The required naive oracle exists at `code/brute.py` and was executed by the delegated builder. It reproduced:

- F3 = {001,010,100,101}, Psi(3) = 20302.
- Psi(10) mod 101001001 = 10699667.

The current `code/solution.py` is intentionally a placeholder because the only validated evaluators are O(k). No full-size value is claimed. Scaling them would answer only more bounded samples and would not resolve the missing structural theorem.
