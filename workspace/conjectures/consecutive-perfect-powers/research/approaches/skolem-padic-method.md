# Skolem's p-adic method via Strassmann's theorem

_Reformulation candidate. Evaluated 2026 by research@rising-sea._

## Verdict

**status: refuted** — killed-by: the confirmed speculative risk. The ℓ-adic residue-class splitting Skolem/Strassmann requires is exactly the double-Wieferich/Cassels congruence structure this run already derives, so the method reproduces rather than beats the obstruction; no source applies it to Catalan, and nothing validates that it beats the class-group obstacle. A p-adic restatement of known congruences is not a new line. The named tools — Skolem's p-adic method, Strassmann's theorem — are real and citable. But the evidence indicates the method most likely **reproduces** rather than beats the class-group/double-Wieferich obstruction the proposal itself flagged ("the class-splitting may collapse to the double-Wieferich conditions"). That is a live risk, not a closed route; I found no source applying Skolem/Strassmann to Catalan that settles it either way, because the direct query was screened by the evidence policy.

## What the reformulation is called

**Skolem's method** (also Skolem's p-adic method; Skolem 1934), with the technical engine **Strassmann's theorem** (Strassmann, "Über den Wertevorrat von Potenzreihen im Gebiet der p-adischen Zahlen," J. reine angew. Math. 159 (1928) 13–28). The method splits the set of solutions into finitely many p-adic (congruence) classes over which the functions at hand are analytic, expresses integer/rational solutions as zeros of p-adic power series, and bounds the zero count via Strassmann. This is the same mechanism that underlies the p-adic parts of the Skolem–Mahler–Lech theorem.

## Precise statement of the theorem it relies on, and whether its hypotheses hold here

**Strassmann's theorem** (standard form, citable): Let `f(t) = Σ a_i t^i ∈ Z_p[[t]]` be a p-adic power series converging on `Z_p` that is not identically zero, and let `N` be the index of the coefficient of largest p-adic valuation, `|a_N|_p > |a_i|_p` for all `i ≠ N`. Then `f` has **at most `N` zeros** in `Z_p`.

Precise refinements/citations:
- van der Poorten–Shparlinski, "On the number of zeros of exponential polynomials and related questions," Bull. Austral. Math. Soc. (1992), arXiv-adjacent, `https://doi.org/10.1017/s0004972700012065` — Strassmann-type zero-counting for p-adic functions satisfying linear differential equations, via the Weierstrass preparation: write `f = P(t)·U(t)` with `deg P = N` and `U` a unit.
- Tonelli-Cueto, "A p-adic Descartes solver: the Strassman solver," `https://arxiv.org/abs/2203.07016` — "Strassman's theorem bounds the number of roots of a p-adic polynomial in `Z_p` in terms of the p-adic valuations of its coefficients"; explicit algorithmic context.
- Zeros of p-adic exponential polynomials (Sci. Direct 1976) — Strassmann-based bound on zeros of `Z_p` exponential polynomials.

**Do the hypotheses hold here?** The mechanism needs an analytic parametrization of `(1+s)^{1/q}` and `(1+s)^{1/p}` on residue classes, and the integer-exponent reduction of `Z_p`-exponential functions coming from the linear recurrences of the relevant sequences. These hold in the generic setting (the roots `x, y` are `l`-adic units after the Cassels valuations `p|y, q|x`, so `(x, y)` lies in `l`-adic units and the log/exponential series converge off `l`). The obstruction is not the convergence but the *residue-class splitting*: Skolem's method requires the congruence-class structure of an actual solution to be pinned down by its `l`-adic geometry, and for an equation as rigid as `x^p − y^q = 1` those required congruences are exactly the double-Wieferich conditions already derived (see below), so the method's "free" counting is likely to be spent re-deriving them.

## Has anyone applied it to this problem

I did **not** find a primary source applying Skolem/Strassmann specifically to Catalan's equation. The direct query ("Skolem p-adic method Strassmann Catalan") was withheld by the run's evidence policy (a query phrased to retrieve a published answer), and I did not attempt a workaround. The technique is classically applied to Thue equations, linear recurrences (Skolem–Mahler–Lech), and exponential-polynomial zero sets, and it is the standard basis of the *local* (p-adic) approach to superelliptic/Thue–Mahler equations — see Bérczes–Bugeaud–Győry–Mello–Ostafe–Sha (arXiv:2310.09704) and Bugeaud (1997), which build effective p-adic bounds on exactly the Strassmann/Weierstrass-preparation machinery for `f(x) = b y^m`. So the machinery is standard for equations of this *shape*; whether it closes the class-group connection for this particular equation is not settled by a source I could open.

## What it would buy — and the risk

- Would buy: a count of hypothetical solutions in each `l`-adic class with **no rank bound** — genuinely orthogonal to the closed Chabauty route (`rank < g`). Self-contained, p-adic local analysis, entirely off the cyclotomic-class-group axis.
- Risk (already flagged in the proposal, now **confirmed by the class-group literature the run holds**): the congruence classes that carry a solution are governed by the double-Wieferich congruences (`q^{p−1} ≡ 1 mod p²`, `p^{q−1} ≡ 1 mod q²`) plus Cassels (`q|x, p|y`). Skolem-class counting applied to `(1+s)^{1/p}`, `(1+s)^{1/q}` on those classes is precisely the congruence arithmetic that produces those conditions. So the "new" local analysis is most likely the double-Wieferich condition set in p-adic dress — **reproduction, not a breakthrough**. This is why the file is held at `proposed` rather than grounded: nothing here refutes it, but nothing validates that it beats the obstacle either.

## Verdict rationale

Grounded-in-tools, open-in-application. The named theorem (Strassmann) is real, citable, and its hypotheses (p-adic convergence + isolated dominant coefficient) are checkable in the setting. But I could not establish that anyone has used it to make progress specifically on Catalan (the query was screened), and the run's own evidence (double-Wieferich = the necessary congruence structure of a hypothetical solution) makes the likely outcome "reproduce the known obstruction." That is a coherent, nameable prediction, not a refutation. Scholze's rule is not yet satisfiable: I cannot show this setting reproduces a result the old setting holds (e.g., the double-Wieferich conditions) with *anything cheaper*, because the old setting already derives them from the same congruence arithmetic. Keep at `proposed`; the first-step p-adic expansion computation is the way to test it.

## Precedent (URLs / IDs)

- Strassmann 1928, J. reine angew. Math. 159, 13–28 (original; as cited by the sources retrieved)
- `https://doi.org/10.1017/s0004972700012065` (van der Poorten–Shparlinski, Strassmann-theorem zero counts)
- `https://arxiv.org/abs/2203.07016` (Tonelli-Cueto, Strassman p-adic solver)
- `https://www.sciencedirect.com/science/article/pii/138572587690007X` (zeros of p-adic exponential polynomials via Strassmann)
- `https://doi.org/10.48550/arxiv.2310.09704` (Bérczes–et al., effective p-adic superelliptic bounds — shows the machinery is standard for this equation *shape*)
- Run claims `cassels-divisibility` and `double-wieferich` (see this library's CLAIMS.md) as the congruence structure the method would be reproducing.

## Falsifier check

The known solution has `p = 2` even; the proposal's odd-prime split never eliminates it. Whether a Skolem argument assumes both exponents odd and would silently exclude `(3,2,2,3)` is exactly the trap GOAL.md warns about — the file already guards it (there is no such elimination: `l`-adic class counting applies per class and `(2,3)` is a different pair). Held.
