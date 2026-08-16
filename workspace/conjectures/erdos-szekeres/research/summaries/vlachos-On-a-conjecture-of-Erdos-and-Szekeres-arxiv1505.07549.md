# Vlachos, "On a conjecture of Erdős and Szekeres"

<!-- source: https://arxiv.org/abs/1505.07549 | full text at research/sources/vlachos-On-a-conjecture-of-Erdos-and-Szekeres-arxiv1505.07549.full.md -->

**Publication.** G. Vlachos, arXiv:1505.07549 (2015). Later merged into Mojarrad–Vlachos DCG 2016 (see the sibling summary `mojarrad-vlachos-An-improved-upper-bound-arxiv1510.06255.md`).

**Main result (binomial-form asymptotic upper bound).**
For $f(n) = ES(n)$,
$$\limsup_{n\to\infty} \frac{f(n)}{{2n-5\choose n-2}} \le \frac{29}{32}.$$

This is one of the intermediate subtractive improvements to the classic binomial bound $ES(n)\le{2n-4\choose n-2}+1$. As with all binomial-form results it improves the *constant* on a base-4 bound and does **not** bear on the exact conjecture $ES(n)=2^{n-2}+1$. Kept in the library to complete the chain below Suk.

**claim block** (for CLAIMS.md)
```claim
id: Vlachos2015-bin-form
statement: limsup_{n→∞} ES(n)/C(2n-5,n-2) ≤ 29/32.
hypotheses: as for ES(n).
holds-here: true, but asymptotic and binomial-form — NOT bearing on the exact conjecture. Superseded by Mojarrad–Vlachos (7/16) and Norin–Yuditsky (7/16), then by Suk's 2^{n+o(n)}.
status: asserted-by-source (arXiv preprint 2015; merged into peer-reviewed DCG 2016).
bearing: records an intermediate step in the binomial-bound subtraction; not a route to the exact conjecture.
anchor: research/sources/vlachos-On-a-conjecture-of-Erdos-and-Szekeres-arxiv1505.07549.full.md
```
