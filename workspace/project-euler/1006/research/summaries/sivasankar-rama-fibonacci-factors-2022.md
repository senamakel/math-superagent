# Sivasankar & Rama — Fibonacci Sequences of 1D and 2D Words: Enumerating and Locating the Factors (arXiv:2207.04304)

<!-- source: https://arxiv.org/html/2207.04304 | full text read 2026-08-19 -->

Full text: `research/sources/sivasankar-rama-fibonacci-factors-2022.full.md`

## What it establishes (the 1D part; the 2D part is off-topic)

**Convention.** 1D Fibonacci words f₀ = a, f₁ = b, fₙ = f_{n−1}f_{n−2}; f_∞ = abaababaabaab… (this is the a↔b, 0↔1 complement of PE1006's S_∞ = 0100101001001…). F(n) = |fₙ| is the n-th Fibonacci number (F(0)=F(1)=1, F(2)=2, F(3)=3, F(4)=5, …). T is the cyclic rotation operator: T(a₁…aₙ) = a₂…aₙa₁, T^{−1}(a₁…aₙ) = aₙa₁…a_{n−1}.

**Lemma 2 (the positional theorem, verbatim).** Let qₙ = T^{F(n)−1}(fₙ) if n even, T^{F(n−1)−1}(fₙ) if n odd (the "special conjugate" of fₙ). Then for each k with 1 ≤ k < F(n), the k+1 length-k prefixes of T⁰(qₙ), T^{−1}(qₙ), …, T^{−k}(qₙ) are the k+1 distinct factors of f_∞ of length k.

**Worked example (k=4, n=4).** f₄ = abaab, F(4)=5, q₄ = T⁴(abaab) = babaa. The five length-4 factors baba, abab, aaba, baab, abaa are exactly the length-4 prefixes of babaa, ababa, aabab, baaba, abaab.

## Why it matters for PE1006

- This is the **primary, sourced statement of the contiguous-window theorem** the run's `fibonacci-position-theorem-contiguous-windows` claim uses: the k+1 distinct length-k factors occur as consecutive windows (cyclic shifts) of a single finite Fibonacci word qₙ, not scattered over the infinite word.
- It gives the run a *finite* model: for k with F(n−1) ≤ k < F(n), all k+1 factors appear as prefixes of k+1 consecutive rotations of qₙ, so the factor set is a contiguous window family in a word of length F(n). This is the structural basis for the directive-9 window/prefix approach.
- The paper's Corollary 1 (1D reading): there are exactly k+1 subwords of length k — the same count as the Sturmian complexity p(k)=k+1, cross-validating the complexity claim from a different (DAWG/conjugation) direction.
- Convention caveat: a↔b swap sends f_∞ = abaab… to PE1006's S_∞ = 01001… = the same word under 0↔1; the rotation/prefix structure is invariant under letter relabeling, so the theorem transfers unchanged.

## What it does NOT establish

- No formula for Ψ(k) or any weighted sum of factors; it fixes *which* strings are the factors and *where* they occur, not their decimal values.
- The 2D extension (Theorems 1-5, Corollary 1, Example 1) is about the 2D Fibonacci array f_{∞,∞} and is irrelevant to PE1006.

## Claims anchored here

`fibonacci-position-theorem-contiguous-windows` (asserted, now source-pinned to Lemma 2 verbatim), corroborates `governing-factor-complexity` / `governing-sturmian`.
