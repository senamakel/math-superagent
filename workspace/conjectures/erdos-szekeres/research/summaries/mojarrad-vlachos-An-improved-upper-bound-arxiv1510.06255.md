# Mojarrad & Vlachos, "An improved upper bound for the Erdős–Szekeres conjecture"

<!-- source: https://arxiv.org/abs/1510.06255 | full text at research/sources/mojarrad-vlachos-An-improved-upper-bound-arxiv1510.06255.full.md -->

**Publication.** H. N. Mojarrad and G. Vlachos, *Discrete & Computational Geometry* 56(1) (2016) 165–180. DOI 10.1007/s00454-016-9791-5. arXiv:1510.06255 (v2 merged with Vlachos's arXiv:1505.07549).

**Main result (binomial-form upper bound, the best of its kind before Suk).**
For $ES(n)$ the least $N$ such that every $N$ points in general position contain $n$ in convex position,
$$ES(n) \le {2n-5 \choose n-2} - {2n-8 \choose n-3} + 2 \approx \frac{7}{16}{2n-4 \choose n-2}.$$

This is a *binomial-form* bound: it still grows like the base-4 binomial `C(2n-4,n-2) ≈ 4^n/√n`, only with a better constant (7/16). It does **not** bear on the exact conjecture $ES(n)=2^{n-2}+1$ — it improves the constant on an upper bound that is already far above the truth, and is superseded for large $n$ by Suk's $2^{n+o(n)}$ (also in the library). It belongs in the record of how the binomial bound was successively subtracted from.

**Chain of binomial-form bounds (all asserted-by-source here; see ROOT.md).**
- Erdős–Szekeres 1935: $ES(n) \le {2n-4\choose n-2}+1$.
- Chung–Graham 1998: ${2n-4\choose n-2}$ (minus 1).
- Kleitman–Pachter 1998: ${2n-4\choose n-2}+7-2n$.
- Tóth–Valtr 1998: ${2n-5\choose n-2}+1$.
- Vlachos 2015 (arXiv:1505.07549): $\limsup ES(n)/{2n-5\choose n-2} \le 29/32$.
- Mojarrad–Vlachos 2016: ${2n-5\choose n-2}-{2n-8\choose n-3}+2$, i.e. $\limsup ES(n)/{2n-4\choose n-2}\le 7/16$.
- Norin–Yuditsky 2016: $\limsup ES(n)/{2n-4\choose n-2} \le 7/16$ (independent route, also in library from arXiv:1509.03332).

**claim block** (for CLAIMS.md)
```claim
id: MV2016-bin-form
statement: ES(n) ≤ C(2n-5,n-2) - C(2n-8,n-3) + 2 for n ≥ 2, ≈ (7/16)·C(2n-4,n-2).
hypotheses: none beyond the statement of ES(n) (general position, convex n-gon).
holds-here: true (this is the exact ES function), but it is a binomial-form bound far above the conjectured 2^{n-2}+1, so NOT bearing on the exact conjecture. Superseded for large n by Suk's 2^{n+o(n)}.
status: asserted-by-source (DCG 2016, peer-reviewed; full text in library).
bearing: completes the binomial-form record; establishes that before Suk the best binomial bound was 7/16 of the 1935 base. Not a path to the exact conjecture — do not mistake a constant improvement on 4^n/√n for progress toward 2^{n-2}.
anchor: research/sources/mojarrad-vlachos-An-improved-upper-bound-arxiv1510.06255.full.md
```
