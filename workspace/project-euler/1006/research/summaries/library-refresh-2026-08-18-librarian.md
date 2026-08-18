# Reference-library refresh: PE1006

Date: 2026-08-18

## Search coverage

Searched independently for (i) Fibonacci/Sturmian factor complexity and mechanical rotations, (ii) explicit Fibonacci factor-location algorithms, (iii) weighted Euclidean/floor-moment algorithms, and (iv) the official Project Euler statement. Citation graphs were walked for Perrin–Restivo's *A note on Sturmian words*, Cassaigne's *On extremal properties of the Fibonacci word*, and Sivasankar–Rama's factor-location paper. Existing local sources already cover the algorithmic Euclidean primitive and the canonical Sturmian literature; duplicate downloads were refused by the library.

## Sources read or triaged

- Official statement: https://projecteuler.net/minimal=1006 (already held locally as `research/summaries/projecteuler-1006-official.html.md`; full source is `problem.md`). It defines S_0=0, S_1=01, S_n=S_{n-1}S_{n-2}, Fibonacci subwords, and Psi, with Psi(3)=20302 and Psi(10) mod 101001001 = 10699667.
- Perrin–Restivo, *A note on Sturmian words*: https://hal.science/hal-00828351v1/file/noteSturmianWords.pdf (already held locally). Theorem 1: Sturmian iff mechanical of irrational slope; Sturmian factor set has n+1 factors; Theorem 2 characterizes consecutive factors; Theorem 3 gives a linear-time next-factor algorithm.
- Bucci–De Luca–Zamboni, *Some Characterizations of Sturmian Words in Terms of the Lexicographic Order*: https://arxiv.org/pdf/1205.5946 (new full text: `research/sources/bucci-deluca-zamboni-sturmian-lex-order-arxiv.full.md`). It independently states the Fibonacci fixed point 0100101001001..., p(n)=n+1, rotation coding by irrational slope, and balance characterization.
- Sivasankar–Rama, *Fibonacci Sequences of 1D, 2D Words: Enumerating and Locating the Factors of the Fixed Points*: https://arxiv.org/pdf/2207.04304 (already held locally). It records first-occurrence and Fibonacci-representation descriptions of Fibonacci-factor positions.
- Weighted-floor algorithm sources already held: `research/sources/oi-wiki-universal-euclidean-floor-sum.full.md`, `research/sources/atcoder-internal-math-hpp.full.md`, `research/sources/universal-euclidean-geometric-weight-fhq.full.md`, and `research/sources/loj138-universal-euclidean-floor-moments.full.md`. These support the executable Euclidean recursion/monoid, while the exact PE reduction remains established by in-container tests rather than a published PE answer.

## Durable mathematical takeaways

The governing theory is Sturmian-word theory (Morse–Hedlund/Hedlund–Morse): the Fibonacci fixed point is a characteristic Sturmian word of slope alpha=1/phi^2, and its length-k factor complexity is exactly k+1. Mechanical-word rotation partitions identify factors with intervals in the circle; the decimal value of a factor is a geometrically weighted digit sum of floor differences. The efficient evaluation reduces the second moment of that weighted floor sum to an O(log) Euclidean recursion carrying count, geometric sum, first floor moment, and second floor moment. This is implemented and tested locally in `code/lib/ueuclid.py`.

## Fetch failures / non-duplication

Attempts to re-download already held Perrin–Restivo, Sivasankar–Rama, Cassaigne, and Project Euler URLs were correctly refused as duplicates. The Bucci–De Luca–Zamboni arXiv copy downloaded successfully. The IOS Press landing page returned 403; its arXiv copy is held instead. A guessed HAL Cassaigne filename returned 404 and was not retained. No Project Euler solution, answer, forum thread, or published contest answer was searched or downloaded.
