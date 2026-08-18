# Scholar digest: reference library against PE1006

## Sources that bear directly

- **Perrin–Restivo, Lothaire, Berstel–Vuillon, Brown characteristic-sequence paper.** Establish the definitions and equivalence: Sturmian words are exactly irrational mechanical words; the Fibonacci fixed point of `0→01, 1→0` is the characteristic word with slope `α=(3−√5)/2=1/φ²`; its length-`k` factors are represented by the `k+1` rotation intervals cut by `{−jα mod 1}`. This validates the factor/intercept model and the digit floor-difference rule. It does not evaluate `Ψ` or prove the target reduction. URLs: https://hal.science/hal-00828351v1/file/noteSturmianWords.pdf ; https://www.cambridge.org/core/product/identifier/CBO9781107326019A016/type/BOOK_PART ; https://arxiv.org/abs/math/0106217 ; https://doi.org/10.4153/CMB-1993-003-6.

- **Sivasankar–Rama, Fibonacci factors (2022).** Gives enumeration/location methods and first-occurrence structure for Fibonacci factors, useful as a finite oracle and possible contiguous-window support. The digest does not establish the exact one-dimensional window identity required by the present evaluator, and it says nothing about decimal square moments. URL: https://arxiv.org/html/2207.04304.

- **AtCoder ACL.** Establishes the ordinary floor-sum Euclidean recursion and logarithmic complexity, plus modular inverse machinery. It supports the base arithmetic primitive and `10^{-1} mod M` because `gcd(10,101001001)=1`; it does not establish geometric weights or the PE reduction. URL: https://atcoder.github.io/ac-library/production/document_en/math.html.

- **OI-Wiki universal Euclidean algorithm.** Establishes the operation-string/monoid staircase model, quotient stripping and reciprocal Euclidean step, with logarithmic Euclidean depth for fixed-size monoids. URL: https://oi.wiki/math/number-theory/euclidean/.

- **fhq universal-Euclidean geometric-weight note and LOJ138.** Describe fixed-size monoids/moment arrays for geometric-weighted first and second floor moments; these are candidate primitives for `Ψ`, not proofs of the PE1006 intercept aggregation. The implementation must prove its own boundary/index mapping against the brute oracle. URL: https://www.cnblogs.com/dixiao/p/15719155.html.

- **Binner reciprocity and Babichev–Shpakova/lattice-rectangle sources.** Independently support Euclidean transformations for polynomial floor moments or floor squares. They do not cover the geometric index weights, Fibonacci factors, or the complete `Ψ` reduction. URLs are in their companion summaries.

## Sources that do not help the final computation

OEIS A213975 and other OEIS entries are catalogues, not proofs, and use a complemented Fibonacci convention; factor counts transfer but decimal values do not. Wikipedia is useful for orientation only. Automatic-sequence/Cobham sources concern a rejected Zeckendorf-automatic route and do not supply the evaluator. The paywalled Morse–Hedlund original is redundant because open Perrin–Restivo/Lothaire sources state the needed theorem. Broad surveys and DOI landing pages add no load-bearing result beyond the above.

## Contradictions and cautions

No source certifies the current full PE evaluator or any target residue. Existing recalled investigation records that the current finite `solution.py`/directive-9 evaluator lacks the required joint Fibonacci-block boundary state and that no honest `Ψ(10^18)` value has been computed. This contradicts any earlier unverified claim that a finite linear evaluator or old phase-4 residue solved the problem. Old residues `16242174` and `77578256` are explicitly invalid; `34432237` and `20938836` are only anchors until reproduced by a valid independent evaluator. Mechanical slope conventions also differ under complementation; PE1006 requires `1/φ²`, not an unqualified `1/φ`.

## Memory status

Three `remember_memory` attempts failed because the memory service timed out. The durable source-backed digest is therefore saved here pending service recovery; no claim is presented as memory-stored.