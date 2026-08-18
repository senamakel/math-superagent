# Reference-library digest for PE1006

The library was read against the current investigation. The full sources remain in `research/sources/`; this note records only claims actually supported by their summaries/full-text checks and their bearing here.

## Directly useful sources

### [[perrin-sturmian-words-lecture2-mechanical.full]]
URL: https://arxiv.org/abs/2207.04304
Perrin's mechanical-word treatment defines the lower word
` s_{α,ρ}(n)=floor((n+1)α+ρ)-floor(nα+ρ) `, gives its irrational-rotation coding, and states the factor-cylinder interval correspondence. For irrational slope, the factor language is independent of intercept; irrational mechanical words are Sturmian via Morse–Hedlund. Applied here with `α=(3−sqrt(5))/2=1/φ²`, this identifies the PE1006 limit word's length-k factors with the k+1 rotation cells. It supports the exact floor-difference model, but contains no formula for Ψ.

### [[lothaire-sturmian-words-C2.full]]
URL: https://doi.org/10.1017/CBO9781107326019.003
This is the book-level reference for Sturmian complexity, mechanical words, rotations, characteristic words, and standard factors. The downloaded PostScript is not reliably text-readable, so precise claims are cross-checked against Perrin–Restivo and readable Sturmian sources. It supports the governing framework and supplies no Ψ-specific result.

### [[richomme-saari-zamboni-standard-factors-sturmian.full]]
URL: https://www.numdam.org/item/ITA_2010__44_1_159_0.pdf
The paper characterizes standard factors of Sturmian words and explicitly identifies the Fibonacci characteristic word as the fixed point of `0→01,1→0` with slope `(3−sqrt(5))/2`; in the Fibonacci case its standard factors are `{φⁿ(1), φⁿ(10), φⁿ(101), φⁿ(0010010)}`. This confirms the slope and can support special-factor/rotation checks, but says nothing about decimal values or their square sum.

### [[fibonacci-1d-2d-enumerate-locate-factors-ar5iv.full]]
URL: https://arxiv.org/abs/2207.04304
The location theorem gives a compact contiguous-window representation of the k+1 length-k Fibonacci factors in a Fibonacci-length standard word (with a convention/complement translation). It supports an O(k) window evaluator and finite-range checks, but not the decimal second moment nor an O(log k) aggregation.

### [[chuan-fibonacci-words-fq1992.full]]
URL: https://www.fq.math.ca/Scanned/30-1/chuan.pdf
Theorem 6/7 says finite labelled Fibonacci words are cyclic shifts of one standard Fibonacci word; residue-position lemmas make the shifts explicit. This is useful for Fibonacci-length special cases and cyclic-rotation checks only. It does not establish the general-k window range or Ψ.

### [[cassaigne-extremal-properties-fibonacci-word.full]]
URL: https://www.numdam.org/item/ITA_2008__42_4_701_0/
The paper states the Fibonacci first-occurrence quotient `ρ'*=φ+1≈2.618`; hence prefixes of asymptotic length about 2.618k contain every length-k factor. This justifies bounded brute-force prefix checks, not full-size Ψ. Do not confuse it with the different recurrence quotient `ρ*=φ+2`.

### [[alessandri-berthe-three-distance-theorems.full]]
The three-distance theorem says irrational-rotation orbit gaps have at most three lengths; the rotation coding bridge identifies factor frequencies with interval lengths. This explains the geometry of intercept cells and may support special correlation identities, but it does not prove the required second-moment aggregation.

## Arithmetic sources

### [[universal-euclidean-geometric-weight-fhq.full]]
URL: https://www.cnblogs.com/dixiao/p/15719155.html
The universal Euclidean monoid recursion evaluates geometric-weighted floor paths and first/second floor moments in O(log max coefficient), independent of the iteration count. It is the correct fixed-intercept inner primitive after telescoping the decimal value into weighted floors. It does **not** prove that the k+1 intercept-cell second moments can be aggregated in fixed dimension.

### [[oiwiki-universal-euclidean-floor-sum-2026.full]]
The current OI-Wiki page states the exact merge/flip recursion and O(log) complexity for the universal Euclidean floor-path monoid. It corroborates the fixed-intercept primitive and the checked `ueuclid.py` implementation, but is not a joint-intercept theorem.

### [[atcoder-internal-math-hpp.full]]
URL: https://cdn.jsdelivr.net/gh/atcoder/ac-library@v1.5.1/atcoder/internal_math.hpp
The ordinary `floor_sum` Euclidean recursion and modular arithmetic internals are exact O(log m) primitives. They are a base case/reference implementation, not sufficient for geometric weights or Ψ by themselves.

### [[babichev-shpakova-weighted-floor-moments-2026.full]]
URL: https://arxiv.org/html/2607.17961v1
This source gives Euclidean closure for a different fixed family of weighted floor moments (mainly polynomial-index/lattice-rectangle kernels). It corroborates the general recursion principle but does not supply the base-10 geometric monoid or the intercept aggregation.

## Useful but non-solution/background

- [[berstel-vuillon-coding-rotations.full]] (https://arxiv.org/abs/math/0106217): recoding theorem for rotations on several intervals; supports rotation language only, with hypotheses not needed for the binary PE1006 model.
- [[bonardo-frid-shallit-valid-factorizations-fibonacci-prefixes-ar5iv.full]] (https://arxiv.org/abs/1806.09534): Zeckendorf/standard-prefix factorization structure; relevant to positional decompositions, not decimal square sums.
- [[rauzy-factor-frequencies-0902.0632.full]] (https://arxiv.org/abs/0902.0632): bounds the number of factor frequencies via Rauzy graphs; frequency structure is not Ψ's unweighted value moment.
- [[berstel-sturmian-episturmian-survey-2007.full]] and [[glen-justin-episturmian-words-survey-2009-ar5iv.full]]: broad Sturmian/episturmian background; no missing aggregation theorem.
- [[cassaigne-extremal-properties-fibonacci-word.full]]: repetition and recurrence facts only beyond the first-occurrence bound.

## Does not help / ruled out for this goal

Automatic-sequence and Cobham sources (including [[durand-rigo-on-cobham-theorem-ems-2021.full]], https://orbi.uliege.be/bitstream/2268/39461/1/Chapter26.pdf) establish incompatibility/ultimate-periodicity results for multiplicatively independent numeration systems, not a computation of Ψ. They explain why a Zeckendorf-to-decimal finite-automaton shortcut is unavailable, but do not solve the problem. Generic three-gap, factor-frequency, repetition, palindrome, standard-factor, and valid-factorization papers likewise stop before the decimal joint second moment.

`research/summaries/chtholly-universal-euclidean-oiwiki.md` is explicitly a failed 404/navigation fetch and contributes no usable theorem; use the current OI-Wiki/fhq/LOJ138 references instead.

## Contradictions/corrections flagged

1. The slope must be `1/φ²≈0.382` for the problem's digit convention. Sources using `1/φ≈0.618` generally use the complemented rabbit convention; treating those as the same factor set contradicts the PE1006 anchor.
2. Any Toeplitz/cyclic pair-correlation identity is special to Fibonacci-length boundary cases, not general k; the library's earlier unrestricted recollection is false and should not be used.
3. `ρ'*=φ+1` is first-occurrence prefix completeness; `ρ*=φ+2` is recurrence/block completeness. They must not be conflated.
4. The universal-Euclidean primitive is fixed-intercept arithmetic only. Claiming that it already evaluates Ψ(10^18) contradicts the documented G4 obstruction: no sourced fixed-dimensional joint-intercept aggregation is presently established.

## Durable-memory status

`remember_memory` was attempted for the direct Sturmian/mechanical finding but the memory service repeatedly failed its health check and explicitly rejected the write. This note is the durable local fallback; retry memory indexing only after service recovery.