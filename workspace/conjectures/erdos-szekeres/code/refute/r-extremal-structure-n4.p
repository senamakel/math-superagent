% Refutation attempt: R-extremal-structure, smallest faithful fragment, n=4.
%
% Rung statement (research/weakened/es-conjecture.md, id R-extremal-structure):
%   "Any set S of 2^(n-2) points in general position with no convex n-gon has
%    convex hull of size at most n-1, hence at least 2^(n-2)-(n-1) interior
%    points; in particular every such extremal set has nonempty interior for
%    n >= 5."
%
% Tightest smallest case: n=4 needs 2^(4-2) = 4 points. "No convex n-gon" means
% no convex quadrilateral; "hull size <= n-1 = 3" means not all 4 points are
% extreme (at least one point strictly inside the triangle of the other three,
% since a 4-point set with hull of size 4 is exactly a convex quadrilateral).
%
% So the claim to attack at n=4 is:
%     (4 points in general position, and NO convex quadrilateral)
%        ==>  at least one point is interior (inside the triangle of the
%              other three).
%
% A finite model satisfying the axioms and falsifying the conjecture would be
% 4 points in general position, no convex quadrilateral, yet ALL extreme
% (hull of size 4) -- impossible, because 4 points in convex position ARE a
% convex quadrilateral (4-point criterion, claim es35-four-criterion).  So the
% expected honest verdict is `proved`; a `refuted` would contradict the
% established 4-point criterion and must be re-checked by hand.
%
% This rung was NOT touched by the prior refuter sessions (they covered only
% R-one-interior / R-k-interior); it is a fresh, first-order, small, non-
% settled-value claim.
%
% Encoding: abstract order-type (uniform rank-3 chirotope / CC fragment),
% same faithful fragment as r-one-interior-n4.p: ccw totals + cyclic
% symmetry, interior via Caratheodory triangle, convex4 via the 4-point
% criterion (no member inside the other three's triangle).
%
%   * 4 points p0..p3, all distinct.
%   * ccw/3: total antisymmetric orientation per triple (general position).
%   * cyclic symmetry.
%   * inside(X,A,B,C): X strictly inside triangle ABC (three edge tests).
%   * interior(X): X strictly inside the convex hull of the others.
%   * convex4(A,B,C,D): no member inside the other three's triangle.
%   * Axiom: no convex quadrilateral.
%   * Conjecture: some point is interior.

fof(points_distinct, axiom,
    ( p0 != p1 & p0 != p2 & p0 != p3
    & p1 != p2 & p1 != p3
    & p2 != p3 )).

fof(ccw_total, axiom,
    ![A,B,C] : ((A != B & B != C & A != C) =>
        ((ccw(A,B,C) & ~ccw(A,C,B)) | (~ccw(A,B,C) & ccw(A,C,B))))).

fof(ccw_cyclic, axiom,
    ![A,B,C] : (ccw(A,B,C) => ccw(B,C,A))).

fof(inside_def, axiom,
    ![X,A,B,C] : ((X != A & X != B & X != C & A != B & B != C & A != C) =>
        ( inside(X,A,B,C) <=>
            ( (ccw(A,B,X) & ccw(B,C,X) & ccw(C,A,X))
            | (~ccw(A,B,X) & ~ccw(B,C,X) & ~ccw(C,A,X)) ) ))).

fof(interior_def, axiom,
    ![X] : ( interior(X) <=> ?[A,B,C] :
        ( A != X & B != X & C != X & A != B & B != C & A != C
          & inside(X,A,B,C) ) )).

fof(convex4_def, axiom,
    ![A,B,C,D] : ((A != B & A != C & A != D & B != C & B != D & C != D) =>
        ( convex4(A,B,C,D) <=>
            ~( inside(A,B,C,D) | inside(B,A,C,D)
             | inside(C,A,B,D) | inside(D,A,B,C) ) ))).

% --- the rung's hypothesis at n=4: no convex n-gon (no convex quadrilateral)
fof(no_convex_quad, axiom,
    ![A,B,C,D] : ((A != B & A != C & A != D & B != C & B != D & C != D) =>
        ~convex4(A,B,C,D))).

% --- conjecture: some point is interior (hull size <= 3)
fof(goal, conjecture,
    ?[X] : interior(X)).
