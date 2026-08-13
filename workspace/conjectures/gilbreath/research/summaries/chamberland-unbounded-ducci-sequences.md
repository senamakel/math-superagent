# Chamberland — Unbounded Ducci sequences

**Full text:** `research/sources/chamberland-unbounded-ducci-sequences.full.md`
**Source URL:** https://chamberland.math.grinnell.edu/papers/ducci_unbounded.pdf
**Published:** Journal of Difference Equations and Applications (2003); author's own PDF.

Studies the Ducci map `f(x1,…,xn) = (|x1−x2|, …, |xn−x1|)` and weighted generalizations. The weighting `(1,−1)` (the classical map) is **bounded**: "the maximum of any string does not increase under iteration" — stated here as the fact that makes Ducci sequences eventually periodic. The paper's main object is the *unbounded* weighting `(−1,2,−1)`.

**Classical theorem quoted (Ciamberlini–Marengoni 1937, restated and reproved many times):**
> **Theorem 1.1.** Every integer string of length n iterates to the zero-string in finitely many steps **iff n = 2^m** for some positive integer m.

The paper's references give the history: reproved in [Andriychenko–Chamberland, Freedman 1948, Miller 1978, Pompili 1996, Sprague 1963, Thwaites 1996, Zvengrowski 1979]; survey bibliography in Meyers 1982.

**Results directly relevant to this run's two Ducci-grounded approaches:**
1. **Max-decrease is the standard proof engine.** Theorem 3.2 ("all integer 4-strings iterate to zero" for the (−1,2,−1) weighting) is proved by exactly the potential argument the `ducci-potential-max-decrease` approach proposes: show the maximum at most doubles in two iterations, then **factor out a power of two** and show the *factored* maximum strictly decreases in every non-borderline case; the borderline cases (where the maximum does not decrease) are exactly strings of the rigid forms `(0,b,d,d)`, `(0,0,c,d)`, `(a,0,c,2a)`, `(a,a,c,c)`, `(a,b,a,b)` (Lemma 3.1), which then iterate to zero by direct check. So the pair (factored maximum, rigidity classification of the equality case) is an established, named technique in this literature — the approach's facts (1) and (2) are its exact ingredients.
2. **Rigidity classification = the complement of where the maximum drops.** The "borderline situations" in the proof are precisely two-valued / structured configurations, matching both CHT's long-{0,d}-block obstruction and this run's `closure-0d-double-edge` (the {0,d} closure that preserves disturbances).
3. **Dimension-dependence is delicate.** The same weighting that makes all rational 4-strings converge has a divergent real 4-string `(1, φ, 2+φ·√5 …, …)` — the dynamics on ℝⁿ do not determine behavior on ℤⁿ, a caution for any continuous-model transfer.
4. **Webb's observation (quoted):** 4-strings may take arbitrarily long to reach zero (Tribonacci): `3·f⁴(tn, tn−1, tn−2, tn−3) = 2(tn−2, tn−3, tn−4, tn−5)`. So even in the power-of-2 (convergent) case there is **no uniform bound on the number of iterations** — the Ducci analogue of "consumption has no uniform bound," which is the run's regeneration obstruction restated in the cyclic setting. A bounded-absorption-time claim in *any* Ducci-based mechanism is false; only a potential/monotone argument can work.

**Status:** sourced (author's PDF of the JDEA paper, primary). The Ciamberlini–Marengoni theorem and max-factoring technique are exactly what the `ducci-potential-max-decrease` approach needs as precedent; note again the paper is about **cyclic** strings — transfer to the half-infinite Gilbreath triangle is this run's deduction, not in the paper.