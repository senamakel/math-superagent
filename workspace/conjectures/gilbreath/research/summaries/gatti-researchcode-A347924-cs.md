# Gatti, rescode GitHub repo and OEIS/A347924.cs — the Gilbreath-polynomial generator

<!-- source: https://github.com/gttrcr/ResearchCode (and /blob/main/OEIS/A347924.cs) | full texts: sources/gatti-researchcode-github.full.md, sources/gatti-researchcode-A347924-cs.full.md -->

Riccardo Gatti's research-code repository (gttrcr/rescode, 45 commits, folders OEIS/astro/
mathematica) and the specific C# generator for the Gilbreath polynomials of A347924.

## What it establishes (the algorithm, from the code)

`GenMthGilbreathPolynomial(m)`:

1. Generate the first m+1 primes.
2. For i = m..(len−1): build the **upper-bound extension** `GC.MaxK(seq[0..i], terms+3)` —
   repeatedly append the largest prime candidate k for which the extended finite sequence
   is still a Gilbreath sequence (`isg`: after absolute differencing, every row's leading
   entry is 1, check via Wolfram). Take m+3 extension values.
3. `res = Table[t[[n]] − 2^(n + (i−1)), {n, 1, Length[t]}]`, then
   `FindSequenceFunction[res, n]` (Mathematica symbolic interpolation) ⇒ P_m.
4. Clear P_m by the lcm of coefficient denominators (A347925) and emit the numerator
   triangle (A347924).

So P_m is the unique degree ≤ m−1 polynomial interpolating the m+3 points
(x, U(S)_x − 2^(m+x−1)); the OEIS values confirm P_6 = (−57−55x−15x²−2x³)/3, U(S_6)_x =
2^(x+5) + P_6(x). Code depends on a custom WolframLink harness (gttrcr/ParallelWolf) and a
primes generator; parallel over i with 8 workers.

## Bearing on this run

This makes the claimed Gilbreath-polynomial reduction **implementable and checkable**: a
later role can reproduce P_m for m ≤ ~12 with sympy (exact polynomial fit through m+3
upper-bound extensions, where "largest prime candidate k keeping G_n+1" is a finite,
decidable test — the primes' own gap structure is not used beyond producing candidates), and
verify whether p_m − 2^{m−1} ≤ P_{m−1}(1) actually holds term by term, and — the real
question — whether the paper's claimed implication "this inequality ⟹ GC(n)" has a proof
that survives scrutiny. The inequality itself is trivially true numerically for large m
(P grows factorially in the denominators, but as a *value* at x=1 it stays within a
small multiple of 2^{m−1}+…; the claim's content is the derivation, not the truth of the
bound). Until the MDPI text lands, the implication remains asserted-by-source, with its
mechanism now checkable.

## Source status

GitHub (MIT-visible public repo, no licence file), author confirmed Riccardo Gatti
(OEIS user gttrcr; h-index 0; also The Open University affiliation per Preprints). 0 stars;
not peer-reviewed beyond the OEIS records and the MDPI paper (Mathematics 2023, 11(18),
4006, doi 10.3390/math11184006, published 21 Sep 2023 — full text unobtainable: MDPI page,
MDPI /pdf, Preprints.org v4 all return HTTP 403 to this run's downloader).