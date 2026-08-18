# Source audit for PE1006

## Useful sources

- **Lothaire/Berstel, Sturmian Words**: establishes the definitions of factor complexity and Sturmian words and the mechanical-word framework. It implies the PE1006 Fibonacci limit has k+1 length-k factors once the Fibonacci/Sturmian identification is checked. It does not prove the decimal moment evaluation.
- **Berstel–Vuillon, Coding rotations on intervals**: establishes the rotation-coding/Sturmian relationship. It supports the mechanical/irrational-rotation model, but not the exact PE1006 intercept aggregation.
- **Morse–Hedlund**: foundational minimal-complexity/Sturmian theory; useful for the named factor-count theorem, but the available digest does not contain the detailed computational reduction.
- **Perrin–Restivo lecture**: explicitly states “Sturmian iff mechanical of irrational slope” and p(n)=n+1, and gives balance facts. It is the most direct compact source for the governing theory; it does not evaluate Psi.
- **Sivasankar–Rama / Fibonacci-factor papers**: give structured first-occurrence positions for Fibonacci factors. They support a contiguous-window representation, but not automatically the stronger doubled-word interval claimed by the investigation.
- **AtCoder Library**: precisely specifies ordinary floor_sum and its O(log m) complexity, plus modular inverses. It supports the base Euclidean recursion and the use of inv(10) modulo M, not the full universal-geometric extension.
- **Universal-Euclidean sources (OI-Wiki, fhq note, LOJ138)**: describe the monoid/Euclidean flip and geometric-weighted first/second floor moments. They support the intended O(log) primitive, subject to checking the PE1006 reduction and indexing against the oracle.

## Sources that do not help with the final computation

The Lothaire, Berstel–Vuillon, Morse–Hedlund, and general Fibonacci-factor sources do not contain the decimal square-sum answer or the exact reduction to the target modulus. OEIS/catalogue pages, Wikipedia, and general automatic-sequence sources are descriptive or catalogual here and cannot replace a proof of the PE1006 evaluator. The official Project Euler page is only the specification and worked oracle. No answer-search or forum source was used.

## Contradictions / cautions

The recalled workspace explicitly records that `code/solution.py` is not a valid full evaluator: its wiring failed at k=1 and it declines the 10^18 computation. It also records that older Phase-4 anchor residues 16242174 and 77578256 are invalid, while 34432237 and 20938836 are asserted replacement anchors pending a valid in-container evaluator. The source library does not resolve this contradiction; it provides only the structural ingredients. In particular, source-backed universal-Euclidean theory does not prove that the current intercept aggregation has been reduced correctly.

Mechanical-word slope conventions conflict across sources because some use the complemented rabbit word. PE1006’s digit word uses ones-density 1/phi^2; this convention must be checked mechanically, not inferred from an unqualified “slope 1/phi” statement.
