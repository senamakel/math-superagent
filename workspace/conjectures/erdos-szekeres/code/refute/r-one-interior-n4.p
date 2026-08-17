% Refutation attempt: weakened rung R-one-interior, tightest case n = 4.
%
% Statement attacked (research/weakened/es-conjecture.md, id R-one-interior):
%   "For every n >= 4, every set of 2^(n-2)+1 points in general position
%    with at most one interior point contains n points in convex position."
%
% Tightest case: n = 4 requires 2^(4-2)+1 = 5 points.  A counterexample
% would be 5 points in general position, at most one of them strictly
% inside the convex hull of the set, and NO convex quadrilateral.
%
% Encoding: abstract order-type (uniform rank-3 chirotope / CC-system)
% fragment, which is the run's own declared finite object for this problem.
%   * 5 points p0..p4, all distinct.
%   * ccw/3: total antisymmetric orientation per triple (general position:
%     every triple has exactly one of the two orientations).
%   * cyclic symmetry ccw(A,B,C) => ccw(B,C,A).
%   * inside(X,A,B,C): X lies strictly inside triangle ABC, defined by the
%     three edge tests having one common sign (the exact geometric rule).
%   * interior(X): X is strictly inside the triangle of some triple of the
%     other points (Caratheodory: in the plane a point is in the convex
%     hull of the others iff it is in some such triangle).
%   * convex4(A,B,C,D): the 4-point criterion -- no member lies inside the
%     triangle of the other three; for 4 points in general position this is
%     exactly "in convex position".
%   * Axiom: at most one interior point.
%   * Conjecture: a convex quadrilateral exists.
%
% A finite model satisfying the axioms and falsifying the conjecture is a
% counterexample to THIS ENCODING, not to the rung: every model must be
% checked for planar realizability (the abstract-chirotope trap; problem.md,
% and the library's own proved claim es35-four-criterion / es-exact-values,
% ES(4)=5).  The hand argument that no real counterexample exists is in
% code/out/refute_r_one_interior_claim.md.

fof(points_distinct, axiom,
    ( p0 != p1 & p0 != p2 & p0 != p3 & p0 != p4
    & p1 != p2 & p1 != p3 & p1 != p4
    & p2 != p3 & p2 != p4
    & p3 != p4 )).

% --- ccw: total antisymmetric orientation of every triple (general position)
fof(ccw_total, axiom,
    ![A,B,C] : ((A != B & B != C & A != C) =>
        ((ccw(A,B,C) & ~ccw(A,C,B)) | (~ccw(A,B,C) & ccw(A,C,B))))).

fof(ccw_cyclic, axiom,
    ![A,B,C] : (ccw(A,B,C) => ccw(B,C,A))).

% --- inside(X,A,B,C): X strictly inside triangle ABC (same sign on all 3 edges)
fof(inside_def, axiom,
    ![X,A,B,C] : ((X != A & X != B & X != C & A != B & B != C & A != C) =>
        ( inside(X,A,B,C) <=>
            ( (ccw(A,B,X) & ccw(B,C,X) & ccw(C,A,X))
            | (~ccw(A,B,X) & ~ccw(B,C,X) & ~ccw(C,A,X)) ) ))).

% --- interior(X): X strictly inside the convex hull of the other four points
fof(interior_def, axiom,
    ![X] : ( interior(X) <=> ?[A,B,C] :
        ( A != X & B != X & C != X & A != B & B != C & A != C
          & inside(X,A,B,C) ) )).

% --- the rung's hypothesis: at most one interior point
fof(at_most_one_interior, axiom,
    ![X,Y] : ((interior(X) & interior(Y)) => X = Y)).

% --- convex4(A,B,C,D): 4-point criterion, no member inside the other three's triangle
fof(convex4_def, axiom,
    ![A,B,C,D] : ((A != B & A != C & A != D & B != C & B != D & C != D) =>
        ( convex4(A,B,C,D) <=>
            ~( inside(A,B,C,D) | inside(B,A,C,D)
             | inside(C,A,B,D) | inside(D,A,B,C) ) ))).

% --- the claim: among the 5 points there is a convex quadrilateral
fof(goal, conjecture,
    ?[A,B,C,D] : ( A != B & A != C & A != D & B != C & B != D & C != D
                   & convex4(A,B,C,D) )).