# Narkiewicz bound — exact statement and method

- Statement: N_1(X) = #{n ≤ X : (2^n)_3 omits digit 2} ≤ 1.62 X^{α_0}, α_0 = log_3 2 ≈ 0.63092 (Narkiewicz, Univ. Beograd. Publ. Elektrotehn. Fak. Ser. Mat. Fiz. No. 678-715 (1980), 173-174).
- Method (from Stoll's slides, which is the only detailed exposition in the library): write 2^n = 3^{m_0}+...+3^{m_s}; mod 3^k the RHS is a unit with low k digits in {0,1} — 2^{k-1} possibilities; 2 is a primitive root mod 3^k; so n lies in 2^{k-1} residue classes mod 2·3^{k-1}; count gives the bound with constant ~1.62.
- This is the identical count that gives |A_k| = 2^{k-1} exactly in SIEVE-EXACT and the run's own computation.
- Original Narkiewicz note: JSTOR https://www.jstor.org/stable/43667894 (likely paywalled); the run holds the second-hand exposition, not the original. The exact numerical constant 1.62 is from the second-hand sources (EP-406, LAG-1, STOLL-1) and is not yet independently recomputed.

```claim
id: LAG-1 (see research/summaries/lagarias-ar5iv-full.md)
statement: N_1(X) ≤ 1.62 X^{α_0}, α_0 = log_3 2.
hypotheses: X ≥ some threshold.
holds-here: yes.
status: asserted-by-source (not proved here; the method is reproduced in STOLL-1).
bearing: the target improvement is any bound with exponent < α_0 or a smaller constant.
anchor: research/summaries/lagarias-ar5iv-full.md, research/summaries/stoll-erdos-termary-digits-slides.md
```