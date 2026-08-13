```approach
id: david-philippon-effective-E3
idea: Apply the David–Philippon (2007) explicit uniform Mordell–Lang theorem on
       self-products E³ of the Robertson curve to the AP-on-doubled-points
       subvariety V ⊂ E³.  This is the ONLY uniform Mordell–Lang lane with a
       completely explicit constant — every other bound (GFP 2026, DGH 2021,
       GGK 2021) has an ineffective C from Rémond's quantitative Mordell–Lang.
       The MSS Robertson reduction produces three points P₀, P₁, P₂ ∈ E(Q) on
       E: y² = x(x²−c²) such that x(2P₀), x(2P₁), x(2P₂) are in AP.  This is
       a condition on the triple (P₀, P₁, P₂) ∈ E³: the subvariety V ⊂ E³ cut
       out by x(2P₀) + x(2P₂) = 2x(2P₁) and the three "X, X±c all squares"
       membership conditions (each equivalent to descent to a specific 2-covering).
       David–Philippon (Ann. ENS 2007, Thm 1.13) bounds the height of points
       on V ⊂ E³ that lie outside the special subvariety (translates of
       algebraic subgroups), with an explicit constant depending only on
       [K:Q], the degree and height of V, and the Faltings height of E —
       all computable numbers for the Robertson curve family E_c, once c is
       an actual integer.  The AP condition is algebraic, so V is a curve or
       surface in E³; its geometric description determines whether V is
       special (a translate of a subgroup) — and if it IS, the MSS reduces
       to torsion properties which are already classified (E(Q)_tors = Z/2×Z/2
       for generic c).  If V is NOT special, DP07 gives an explicit height
       bound on all points in V(E), reducing non-existence to a finite
       computation per c.  This is the EFFECTIVE version of what the adopted
       uniform-height-bound-elliptic-ap approach does with an ineffective C.

mechanism: The Robertson reduction (claim `robertson-elliptic-reduction`) is:
  MSS over Q ⇔ three points P₀,P₁,P₂ ∈ E(Q) with x(2P₀), x(2P₁), x(2P₂) in AP
  and each X = x(2Pᵢ) satisfying {X, X±c} all rational squares (i.e. ∈ 2E(Q)).
  Each "∈ 2E(Q)" condition is equivalent to (ξᵢ, ηᵢ) lying on a specific 2-covering
  Cᵢ → E; the three coverings together with the AP condition define a
  subvariety V ⊂ E³ (fibered over the parameter c).  David–Philippon 2007
  (Ann. Sci. ENS 40, 889–921, Thm 1.13) states: for a subvariety V ⊂ A^n
  where A is an abelian variety over a number field, the set of points in
  V(A) that are NOT contained in a translate of a positive-dimensional
  algebraic subgroup of A^n has bounded height, with a completely explicit
  bound involving the Faltings height h_F(A), the degree and height of V,
  and [K:Q].  This is the one uniform ML theorem with NO hidden constants.
  For E_c: y² = x(x²−c²), the Faltings height is explicit: E_c is the
  quadratic twist by c of E₁: y² = x(x²−1), so h_F(E_c) = h_F(E₁) +
  (1/2)Σ_{p|c} log p + O(1) where the O(1) term is absolute (Silverman's
  formula for height under quadratic twist).  The degree of V is bounded by
  the degree of the duplication map (4) and the AP equation (degree 2 in
  the x-coordinates).  If the explicit bound from DP07 can be turned into
  an actual integer — a function of c and E_c — and this bound is below
  the Morgenstern/Buell bound (centre > 25×10²⁴), then non-existence is
  proved.  The decisive gap is whether V is special (a translate of a
  subgroup of E³) — if so, DP07 gives the special-point height asymptotics
  but not a finite bound; the special case reduces to whether the three
  doubled points form a subgroup configuration, which is testable from the
  duplication-map addition law.  Named mathematics: David–Philippon explicit
  uniform Mordell–Lang, Faltings height, Silverman's height-under-twist
  formula, 2-coverings of elliptic curves.

first-step: |
  1. Extract DP07 Theorem 1.13 from the primary source (Ann. Sci. ENS 40,
     2007, 889–921) — the exact statement of the explicit height bound,
     including every constant and its dependence on h_F(A), deg(V), and [K:Q].

  2. For a fixed test centre c (e.g. Bremner's c=138600), compute the
     subvariety V_c ⊂ E_c³ defined by the AP-on-doubled-points condition +
     the three 2E(Q)-membership equations.  Express V_c as the intersection
     of E_c³ with algebraic equations in the coordinates of P₀,P₁,P₂.
     Determine whether V_c is special (a translate of an algebraic subgroup)
     by computing its stabiliser in E_c³ and checking dimension.  Report:
     (a) dimension of V_c, (b) whether V_c is special, (c) if not special,
     the explicit DP07 height bound for points on V_c (as an actual integer
     or expression in c).

  3. Run the result against the Bremner witness: the witness has only TWO
     of its three doubled points in 2E(Q); its third main-diagonal entry
     fails the membership test.  So the witness is NOT a point on V_c.
     This is correct — V_c is empty for non-MSS centres.  The computation
     should confirm that the AP+membership system for c=138600 has NO
     rational solution triple (P₀,P₁,P₂).

status: proposed
precedent: |
  - David & Philippon, "Minorations des hauteurs normalisées des
    sous-variétés de variétés abéliennes II", Ann. Sci. École Norm. Sup.
    (4) 40 (2007), no. 6, 889–921.  Theorem 1.13: explicit height bound
    on non-special points of subvarieties of abelian varieties.
  - This run's claim `dp07-explicit-uniform-ml-elliptic-self-products`:
    "David–Philippon (DP07 Thm 1.13) is, per GGK, the only uniform
    Mordell–Lang-type result with a completely explicit constant, and it
    applies to subvarieties of self-products of a single elliptic curve."
  - The Robertson reduction: claim `robertson-elliptic-reduction` (proved,
    verified on witness).  Three doubled points on E: y²=x(x²−c²) with
    x-coordinates in AP.
  - Silverman, "Heights and elliptic curves" (Silverman's formula for
    Faltings height of quadratic twists): h_F(E_D) = h_F(E_1) + (1/2)
    Σ_{p|D} log p + c(E_1) for squarefree D.
  - NOT subsumed by uniform-height-bound-elliptic-ap: that approach uses
    Garcia-Fritz–Pastén with the ineffective constant C from Rémond.
    This approach uses the ONLY effective-constant theorem in the literature.

speculation: The mechanism assumes (a) DP07's explicit constant can actually be
  evaluated to a number for E_c, (b) the special-subvariety case does not occur
  (or reduces to torsion which eliminates generic c), and (c) the computed bound
  on ĥ(Pᵢ) translates to a bound on c below the known search frontier.  All
  three are what the first step checks, and any one failing — V_c special,
  constant too large, or c-bound above 10²⁵ — means the approach adds effective
  ML to the toolkit but does not settle the conjecture.
killed-by: _none yet_
```