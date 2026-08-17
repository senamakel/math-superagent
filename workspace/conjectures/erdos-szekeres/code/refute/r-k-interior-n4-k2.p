% Refutation attempt: weakened rung R-k-interior, deepest small nontrivial
% instance: n=4, k=2 (maximal interior count for 5 points).
%
% Statement (research/weakened/es-conjecture.md, id R-k-interior):
%   "For every n >= 4 and every fixed k >= 0, every set of 2^(n-2)+1 points
%    in general position with at most k interior points contains n points
%    in convex position."
%
% Tightest nontrivial small case: n=4 needs 2^(4-2)+1 = 5 points.  When the
% interior count is maximal for 5 points (k=2), the hull is a triangle and
% the trivial hull-vertex argument dies (a triangle has only 3 vertices, too
% few for a convex quadrilateral).  So this is the worst case of R-k-interior
% over the four points.
%
% A finite model satisfying the axioms below and falsifying the conjecture
% would be 5 points in general position with at most 2 interior points and
% NO convex quadrilateral -- i.e. a counterexample to ES(4)=5 itself, which
% is an ESTABLISHED value in this library (claim es-exact-values).  So the
% expected and only honest verdict is `proved`; a `refuted` would contradict
% a checkable settled value and must be re-checked by hand before reporting.
% The abstract-chirotope trap (non-realizable model) applies exactly as in
% r-one-interior-n4.
%
% Encoding: abstract order-type (uniform rank-3 chirotope / CC fragment),
% same as r-one-interior-n4.p with the at-most-one-interior axiom relaxed to
% at-most-two-interior (the maximum possible for 5 points in the plane).
%
%   * 5 points p0..p4, all distinct.
%   * ccw/3: total antisymmetric orientation per triple (general position).
%   * cyclic symmetry.
%   * inside(X,A,B,C): X strictly inside triangle ABC (three edge tests,
%     one common sign -- exact geometric rule).
%   * interior(X): X strictly inside the convex hull of the other points
%     (Caratheodory: in the plane, inside the hull iff inside some triangle
%     of the others).
%   * convex4(A,B,C,D): 4-point criterion, no member inside the other
%     three's triangle.
%   * Axiom: at most two interior points (the max for 5 points).
%   * Conjecture: a convex quadrilateral exists.

fof(points_distinct, axiom,
    ( p0 != p1 & p0 != p2 & p0 != p3 & p0 != p4
    & p1 != p2 & p1 != p3 & p1 != p4
    & p2 != p3 & p2 != p4
    & p3 != p4 )).

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

% --- the rung's hypothesis: at most two interior points (R-k-interior, k=2;
%     the maximum achievable for 5 points in the plane, so this is the worst
%     case)
fof(at_most_two_interior, axiom,
    ![X,Y,Z] : ((interior(X) & interior(Y) & interior(Z)) =>
        ( X = Y | X = Z | Y = Z ))).

fof(convex4_def, axiom,
    ![A,B,C,D] : ((A != B & A != C & A != D & B != C & B != D & C != D) =>
        ( convex4(A,B,C,D) <=>
            ~( inside(A,B,C,D) | inside(B,A,C,D)
             | inside(C,A,B,D) | inside(D,A,B,C) ) ))).

fof(goal, conjecture,
    ?[A,B,C,D] : ( A != B & A != C & A != D & B != C & B != D & C != D
                   & convex4(A,B,C,D) )).
