# Graf von Bothmer, Labs, Schicho, van de Woestijne — "The Casas-Alvero conjecture for infinitely many degrees" (J. Algebra 316 (2007) 224–230; arXiv:math/0605090v2)

Full text held at `research/sources/grafvonbothmer2007_infinitely_many_html.full.md` (arXiv HTML v2).
Journal DOI: https://doi.org/10.1016/j.jalgebra.2007.06.017. Source URL: https://arxiv.org/html/math/0605090v2

## What the paper establishes

1. **Theorem (CA for p^k and 2p^k in char 0).** Let d = p^k or d = 2p^k for a prime p. Then the Casas-Alvero Conjecture holds in characteristic 0 for polynomials of degree d. This is the paper's headline result, the first infinite family of degrees settled.
   - Method (Section 2, "Mixing characteristics, or There and Back Again"): it proves the contrapositive over finite fields. Proposition 2.2: if the variety X_d(F̄_p) of degree-d CA-polynomials over F̄_p is empty for some prime p, then X_d(K) is empty for every char-0 field K. Proposition 2.5: X_d(F̄_p) is empty for d = p^k. For d = 2p^k: Proposition 2.3 excludes nontrivial quadratic examples in char p, and Proposition 2.6 shows X_d(F̄_p) empty. The key mechanism: in char p, the (ordinary) derivative P^(p) vanishes identically, so the conditions P_i = 0 for the Hasse derivatives are *stronger* than the ordinary-derivative hypothesis; the char-p degeneracy is used to force collapse.
   - Note the derivative convention: the paper states explicitly that the correct char-p formulation uses **Hasse derivatives** P_i = P^(i)/i!, which never vanish identically, and that this strengthens the conditions in positive characteristic (Introduction, "Notations and definitions"). This is the same convention the run's `is_ca_hasse` oracle uses and that the published bad-prime lists assume (see claims hasse-vs-ordinary-definitions, bad-prime-lists-hasse-formulation).

2. **Proposition 3.1 (char-p counterexamples).** For each prime p, P = X^{p+1} − X^p ∈ F_p[X] has degree d = p+1, is NOT a d-th power, yet has a nontrivial common factor with every Hasse derivative P_i, i = 1,…,d−1. Proof: P = X^p(X−1); X divides P_i for i = 1,…,d−2, and P_{d−1} = dX − 1 ≡ X − 1 (mod p), and X−1 divides P. **This is the canonical char-p witness the run's oracle tests** (see claims charp-false, charp-witness-xpp1-xp, charp-witness-xpp1-xp-hasse-recheck).

3. **Remark 3.2 (bad primes are bounded; explicit huge bad prime).** If CA holds in degree d over char 0, then the primes p for which counterexamples exist over F_p are bounded. Example: for d = 3, CA is true over every characteristic except 2; by Prop 2.6 this implies CA holds in char 0 for all degrees under 30 except possibly 12, 20, 24, 28. Also: the quadrinomial P = X^6 + 3144481702696843 X^4 + X^3 + 2707944513497181 X^2 is a counterexample in characteristic 7390044713023799, even though CA holds for d = 6 over Q. (This explicit bad prime for degree 6 is a data point the run's bad-prime lists must contain or explain.)

4. **Section 4 (computational aspects).** Discusses the Gröbner-basis connection: X_d is defined by the ideal of resultants (f, P_i); computation over char p is dramatically faster than over Q, which is why the char-p route wins. This is the methodological origin of the run's "reduce mod p to verify in char 0" strategy.

## Relationship to the run's other claims

- Confirms the p^k / 2p^k case attributed to this paper in ROOT.md and claim `gvb-lift` (which quotes Theorem 3 of Castryck et al as reformulated from this paper's Prop 2.2-2.6).
- Proposition 3.1 is the direct source for the claim `charp-witness-xpp1-xp`.
- Remark 3.2's "degrees under 30 except 12, 20, 24, 28" is the origin of the run's open-degree analysis (see research/patterns/open_degree_complement_and_sequences.md); degree 12 was later settled by Castryck et al 2012, leaving 20 as smallest open (per ROOT.md and claims `smallest-open-degree`).
- Historical note in the Introduction: "For d ≤ 7 … proved in [DG05] using Gröbner basis computations. Since then the authors of [DG05] have settled the case of d = 8 as well (personal communication)." This is a primary-source confirmation of the verification bound (claims `computational-boundary`, `verification-bound`).

## Caveats

- This is the journal paper's arXiv v2; the journal version (J. Algebra 316, 224–230, 2007) is paywalled at ScienceDirect but the arXiv HTML is the authors' own final version and matches the journal abstract.
- Proposition 2.1–2.6 chain is stated with proofs in the full text; the char-p argument's load-bearing steps are Prop 2.2 (empty F̄_p fibre ⇒ empty char-0 fibre) and the per-degree emptyness proofs.

## What it implies for this run

The paper gives the run its central methodological template (verify emptiness over F̄_p to conclude over char 0) and its canonical char-p witness, and pins the verification bound d ≤ 8 (2007 state of the art). Its degree list "12, 20, 24, 28" as the open cases under 30 is the arithmetic skeleton the run's bad-prime program refines.
