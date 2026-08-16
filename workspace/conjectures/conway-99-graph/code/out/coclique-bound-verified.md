# Coclique bound verification for the k=14 λ=1 thread

Exact integer computation of the Wilbrink–Brouwer Lemma-2 coclique bound
`|S| <= n(-s)/(k-s)`, where s is the smallest (0,1)-eigenvalue, for the three
member families and the two positive controls.

Formula: for srg(v,k,λ,μ), s = (λ−μ − sqrt(4k−7))/2... actually the negative
root of x²+(μ−λ)x+(μ−k)=0. Coclique (independence) bound:
  alpha <= v·(−s)/(k−s).

| graph | v | k | λ | μ | r | s | −s/(k−s) | bound | true alpha |
|---|---|---|---|---|---|---|---|---|---|
| rook(3) | 9 | 4 | 1 | 2 | 1 | −2 | 2/6=1/3 | 3 | 3 (exact) |
| Conway (hyp) | 99 | 14 | 1 | 2 | 3 | −4 | 4/18=2/9 | 22 | open |
| BvLS | 243 | 22 | 1 | 2 | 4 | −5 | 5/27 | 45 | open |
| (57,14,1,4) | 57 | 14 | 1 | 4 | 2 | −5 | 5/19 | 15 | (used in proof) |

Check eigenvalues:
- rook(3): x²+(μ−λ)x+(μ−k) = x²+1x−2 = 0 → x∈{1,−2}. s=−2. α=3. ✓
- Conrad: x²+1x−12=0 → {3,−4}. s=−4. bound = 99·4/(14+4)=396/18=22. ✓
- BvLS: x²+1x−20=0 → {4,−5}. s=−5. bound=243·5/27=1215/27=45. ✓
- (57,14,1,4): x²+3x−10=0 → {2,−5}. s=−5. bound=57·5/19=15. ✓ (matches Wilbrink-Brouwer's "coclique at most 15")

KEY: the three coclique bounds are 3, 22, 45 for rook(3), 99, BvLS. They are
distinct, so a contradiction that exploits the SPECIFIC value 22 for 99 is
NOT refuted on arrival by the controls — it is parameter-specific. This is
the promising direction recorded in the thread.

Correction: an earlier draft of the thread note wrote rook(3)'s bound as 6;
it is 3 (alpha(rook(3))=3). The 99 bound is 22, BvLS 45. Distinction holds.

STATUS: verified by exact integer arithmetic (no floats); the eigenvalues are
from the standard srg formula and the library's exact spectrum records.
