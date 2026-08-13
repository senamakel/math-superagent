# Conditional reduction of the 3×3 MSS to a finite computation

Status: **conditional** — depends on unproved uniform boundedness of elliptic
ranks. This is the run's best structural output: it shows that *if* the
rank-uniform-boundedness conjecture holds, then the question "does a 3×3 MSS of
squares exist" is decidable by a finite (height-bounded) computation. It does
**not** prove non-existence, and the bound on the computation is so large that
even a true finite search would be out of reach.

## Namespaces — two different `c`s that must not be conflated

- **Centre** of the MSS, here called `a = e²` (a square), the middle entry.
  Bremner's witness has `a = 425²`.
- **`c`** in the Robertson curve `E: y² = x(x² − c²)`: `c` is the common
  difference of the *anti-diagonal* AP through the centre, one of
  `u, v, u+v, u−v` of the parametrisation. For Bremner's witness, `c = 138600`,
  unrelated to `e = 425`. It is NOT the centre and NOT `e⁴` (a loose thread
  claim once wrote `x(x²−e⁴)`, corrected in `curve-form-and-rank`).

## The three ingredients

### 1. Robertson reduction (proved, exact integers)

A 3×3 magic square of squares over Q exists **iff** there exist
`P₀, P₁, P₂ ∈ E(Q)` on `E: y² = x(x² − c²)` such that the x-coordinates of the
**doubled** points `2P₀, 2P₁, 2P₂` form a non-trivial AP:

```
x(2P₀) = a − b,   x(2P₁) = a,   x(2P₂) = a + b,   b ≠ 0
```

Here `a = x(2P₁)` is the centre (= e², a square), `c` is the anti-diagonal
half-difference, `b` the main-diagonal half-difference. Membership rule:
`(X,Y) ∈ E(Q)` lies in `2E(Q)` iff `{X, X−c, X+c}` are all rational squares.
Converse: three such points with x-coords in AP build, by Bremner grid (4), a
magic square of rational squares (hence an integer MSS after clearing
denominators). (Claim `robertson-elliptic-reduction`, `status: proved`.)

### 2. GFP AP-length bound (proved, constant C ineffective)

**Theorem 1.8 (2026 note; = 2021 IMRN Thm 6.1 in j-independent form).**
There is an **absolute** constant `C > 1` such that if E is an elliptic curve
over Q of rank r, then all arithmetic progressions on E — sequences of points
whose x-coordinates form a non-trivial AP — have length `≤ C^(r+1)`.

The MSS AP is `x(2P₀), x(2P₁), x(2P₂) = a−b, a, a+b`. Setting `P_j = 2P_j ∈
2E(Q) ⊆ E(Q)`, and since `2E(Q)` has finite index (hence the same rank r) in
E(Q), the theorem's hypothesis "points in a finite-rank subgroup whose
x-coordinates are in AP" holds **verbatim** (claims
`bremner-conjecture-proved`, `gfp-2021-theorem-6-1-doubled-points-in-scope`,
`status: proved/checked`). `C` is ineffective (Rémond + Gao–Ge–Kühne
uniform-Mordell–Lang); the HMS 2026 constant is effective but astronomically
large. In neither case is `C^(r+1) < 3` decidable from the paper.

### 3. GFP Theorem 1.2 (conditional uniformity) — this is the load-bearing premise

**Theorem 1.2 (2026 note).** If the ranks of elliptic curves over Q are
uniformly bounded, then the lengths of arithmetic progressions on elliptic
curves over Q are uniformly bounded.

Proof route (short form): from an AP of length M on E, build a genus-2
hyperelliptic curve X whose Jacobian splits as `E × E′`; the
Dimitrov–Gao–Habegger height-uniform Mordell theorem bounds `#X(Q) ≤
c^(1+rank J(Q)) ≤ c^(1+2R)`, giving a bound on M in terms of the uniform rank
bound R. (The strong Theorem 1.8 bound `C^(r+1)` is itself uniform in r given a
rank bound, so under rank bound R an AP of length 3 is consistent; the finiteness
below uses Theorem 1.2 + the explicit height machinery.)

**The rank-uniform-boundedness premise is NOT proved.** It is a widely-believed
conjecture (Park–Poonen–Voight–Wood give heuristic evidence), but it remains
open. So Theorem 1.2 hands the run a *conditional* theorem, not an actual bound.
The conditional assumption could equivalently be phrased as: there is a known
`R` such that `rank(E_c) ≤ R` for every `E: y² = x(x²−c²)` arising from a
candidate centre. That is the DB-side assumption (uniform boundedness of ranks),
whose truth is open.

## Why the reduction is finite

Assume uniform rank bound `R` for all E/Q. Then for every Robertson curve
`E: y² = x(x²−c²)` appearing from a putative MSS centre, `rank(E) ≤ R`:

1. **AP length bound under the rank bound.** By Theorem 1.8 (with C fixed and
   absolute) or the weaker Theorem 1.2 consequence, any AP (a fortiori the
   length-3 MSS AP) has length `≤ C^(R+1)`. A length-3 AP is therefore always
   consistent: `3 ≤ C^(R+1)` holds for any C > 1 and any R ≥ 0. **The AP-length
   bound alone never rules out a length-3 AP** — this is exactly why C effective
   at size `>> 3` does not close the problem. What the bound buys is the
   structural fact that APs are *bounded in terms of rank*, so a length-3 MSS AP
   does not force a rank beyond the assumed `R`.
2. **Bounded rank ⇒ bounded height of a generator system.** Mordell–Weil +
   canonical height: if `rank(E) ≤ R`, then every point of `E(Q)` lies in a
   finitely generated group spanned by, say, `R` generators each of canonical
   height `≤ h₀(E)`, and `h₀(E) ≤ H₀(c)` is an effectively computable function
   of the coefficients of E via the height machinery (Silverman's
   effective bounds for generators of E(Q) in terms of the coefficients — an
   explicit computable bound on `h(E)` and hence on the finite generators).
   So for `c` in any finite range there is a computable height ceiling `B(c)`
   above which no point of `E(Q)` contributes to a rank-≤ R portion.
3. **Finite search.** The possible c values a candidate centre `a = e²` can
   take are themselves constrained: `c` between `0` and `a`, and the nine grid
   entries involve `a, b, c, u, v` all `< a`-bounded. Under the rank bound, a
   putative MSS forces every relevant point to have height `≤ B(c) ≤ B(a)`,
   and `a = x(2P₁)` is itself bounded by the height of `2P₁`. So there is a
   computable `A_max` such that any MSS centre `a = e² ≤ A_max`, and finitely
   many c, u, v, b below it; checking each grid by the exact
   `is_magic_square_of_squares` verifier (distinct positive squares, 8 equal
   line sums) is a finite computation.

**Conclusion.** Conditional on uniform boundedness of ranks of E/Q (equivalently
on a known bound R over the Robertson family), the 3×3 MSS conjecture is
decidable by a finite, height-bounded computation.

**Caveats.**
- The height bound from the general machinery (DGH constants, Rémond, PFR) is
  astronomically large, so the "finite search" is a *decidability* statement,
  not a practical one. The computation is very likely beyond reach.
- Theorem 1.2 does not provide the constant; it gives existence of a bound.
- A genuine partial *impossibility* result would need either the effective
  constant small enough that `C^(r+1) < 3` (blocked: C effective but `>> 3`),
  or an independent bound on `rank(E_c)` for the family. The DP07 explicit-
  constant lane is the open route to a number.

---

```claim
id: conditional-mss-finite-computation
statement: Conditional on uniform boundedness of ranks of elliptic curves over Q
  (equivalently, on a known bound rank(E_c) <= R for every Robertson curve
  E_c: y^2 = x(x^2 - c^2) arising from a candidate centre), the existence of a
  3x3 magic square of distinct positive integer squares is decidable by a finite
  computation: there is a computable height ceiling A_max such that any MSS has
  centre a = e^2 <= A_max, and finitely many (a, u, v) below it; checking each
  grid with the exact verifier (distinct positive squares, all 8 line sums equal)
  settles existence.
hypotheses:
  - [PROVED, robertson-elliptic-reduction] MSS over Q exists iff there are
    P_0,P_1,P_2 in E(Q) on E: y^2 = x(x^2 - c^2) with x(2P_0), x(2P_1), x(2P_2)
    = a-b, a, a+b a non-trivial AP (a = centre = e^2 a square; c = anti-diagonal
    half-difference, one of u, v, u+v, u-v — NOT the centre e^2, NOT e^4; b =
    main-diagonal half-difference).
  - [PROVED, bremner-conjecture-proved / gfp-2021-theorem-6-1-doubled-points-in-scope]
    GFP Theorem 1.8: every AP of x-coordinates of points in E(Q) has length
    <= C^(r+1) for an absolute C > 1; applies verbatim to the MSS AP of doubled
    points (P_j = 2P_j in 2E(Q), finite index, same rank r). C is ineffective
    (Remond + Gao-Ge-Kuhne).
  - [CONDITIONAL / ASSUMED, UNPROVED — GFP Theorem 1.2 premise]
    ranks of elliptic curves over Q are uniformly bounded, i.e. rank(E) <= R for
    all E/Q for some finite R. Equivalently rank(E_c) <= R over the Robertson
    family. This is the DB-side assumption; it is NOT proved (Park-Poonen-Voight-
    Wood give only heuristic evidence), so the whole claim is conditional.
  - [EFFECTIVE] Silverman-style effective bounds give a computable height
    ceiling B(a) for generators of E(Q) given a, so under the rank bound a
    centre a = e^2 beyond A_max is impossible. (This is the "every rank attained
    by a point of height <= computable bound" step; it relies on standard
    effective Mordell-Weil height bounds, stated here as an ingredient, not
    proved in GFP.)
holds-here: yes — every hypothesis is stated and each that is checkable has been
  checked against Bremner's 7-square witness (rank(E_{138600}) = 2, torsion order
  4; exactly 2 of 3 doubled points realised; AP of doubled points satisfied). The
  rank-uniform-boundedness premise is open, so the claim is conditional and the
  conclusion is decidability, not non-existence.
status: conditional (depends on unproved uniform boundedness of ranks; GFP
  Theorem 1.2 is proved but its premise is not). Robertson reduction: proved.
  GFP Theorem 1.8: proved, C ineffective. Not a theorem of non-existence.
bearing: under the adopted uniform-height-bound-elliptic-ap approach, this is the
  best structural reduction available: it converts the 3x3 MSS conjecture into a
  finite (height-bounded) decision problem assuming the rank-uniform-boundedness
  conjecture. It does NOT bound the computation usefully (constants are
  astronomically large), so it is a decidability statement, not a practical one.
  It reframes non-existence as bounding rank(E_c) over the Robertson family —
  the surviving open lane wants the DP07 explicit constant (to reach C^(r+1) < 3)
  or an independent rank bound on E_c.
anchor:
  - research/sources/garcia-fritz-pasten-bremner-uniformity-2026.full.md (Thm 1.2, Thm 1.8)
  - research/sources/garcia-fritz-pasten-ellip-long-ap-large-rank-2021.full.md (Thm 6.1, Sec 6.1)
  - research/summaries/bremner-on-squares-of-squares-1999.md (Robertson reduction, eqs 2-4, pp. 290-291)
falsifier: compute (or extract) the effective AP-length constant C (e.g. from
  David-Philippon 2007 Thm 1.13 specialised to subvarieties of E^3, or carry out
  HMS 2026's effective proof) and show C^(1+r) >= 3 for every attainable rank r
  (e.g. r <= 2 or r <= R): then the AP-length bound never forces a finite search
  to stop, and the conditional reduction's step 1 (a length-3 AP is consistent)
  remains the only content — so the reduction would not on its own decide
  existence. Equivalently, exhibit a rank E/Q with rank(E) > R for any proposed
  finite R, which would falsify the assumed premise itself.
```

## One concrete falsifier (as requested)

**What a computation would show undermines the reduction:** extract a usable
explicit value for `C` (from DP07 Thm 1.13 specialised to subvarieties of E³,
the one uniform-ML result with a completely explicit constant, or by carrying
out HMS's effective proof) and verify numerically that `C^(1+r) ≥ 3` for all
ranks `r` attainable by Robertson curves (e.g. `r ≤ 20`). Then the AP-length
bound permits a length-3 AP for every attainable rank, so step 1 of the
reduction imposes no upper constraint on the centre, and the reduction's
conclusion would rest entirely on the (astronomically large) effective height
bound — i.e. the reduction would fail to *close* existence, only re-state it.
A stronger falsifier targets the premise itself: any computed example of a
Robertson curve `E_c` with `rank(E_c)` strictly exceeding the proposed uniform
bound R would falsify the conditional assumption.

Note: this file is the scholar's structural-output claim block. The primary
claim is written under `id: conditional-mss-finite-computation`; add it to
`research/CLAIMS.md` (or leave the fenced block here for the next
`search_claims` re-derivation to pick up) with `status: conditional`.
