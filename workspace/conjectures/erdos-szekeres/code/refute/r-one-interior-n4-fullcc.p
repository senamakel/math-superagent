% Refutation attempt, second fragment (FIXED): R-one-interior tightest case
% n=4, over full Knuth CC systems, convexity defined axiom-natively via hull
% edges.  Previous version had a bug: the hull_edge / hull_vertex guards
% demanded X != A & X != B & ... & (X = A | X = B | ...) simultaneously --
% contradictory, so the definitions were vacuous and the "refuted" was an
% artifact.  Fixed guard: X,Y are DISTINCT points chosen FROM the 4-set.
%
% The correct abstract statement (a consequence of every 5-point CC system
% being realizable -- first non-stretchable arrangements have 9 pseudolines,
% Ringel; ES(4)=5 is a proved library claim es-exact-values / es35-four-
% criterion) is: every 5-point CC system contains a convex quadrilateral.
% Wesley: if this fragment returns proved, the abstract analogue of ES(4)=5
% holds in the CC-system language, matching the library's proved claims.

fof(points_distinct, axiom,
    ( p0 != p1 & p0 != p2 & p0 != p3 & p0 != p4
    & p1 != p2 & p1 != p3 & p1 != p4
    & p2 != p3 & p2 != p4
    & p3 != p4 )).

% --- 1+2+3: cyclic symmetry + antisymmetry (exactly one of ccw/reverse) =
%     nondegeneracy + totality
fof(ccw_total, axiom,
    ![A,B,C] : ((A != B & B != C & A != C) =>
        ((ccw(A,B,C) & ~ccw(A,C,B)) | (~ccw(A,B,C) & ccw(A,C,B))))).

fof(ccw_cyclic, axiom,
    ![A,B,C] : ((A != B & B != C & A != C) =>
        (ccw(A,B,C) => ccw(B,C,A)))).

% --- 4: interiority
fof(interiority, axiom,
    ![T,Q,R,P] : ((T != Q & T != R & T != P & Q != R & Q != P & R != P) =>
        ((ccw(T,Q,R) & ccw(P,T,R) & ccw(P,Q,T)) => ccw(P,Q,R)))).

% --- 5: transitivity
fof(transitivity, axiom,
    ![T,S,P,Q,R] : ((T != S & T != P & T != Q & T != R
                     & S != P & S != Q & S != R
                     & P != Q & P != R & Q != R) =>
        ((ccw(T,S,P) & ccw(T,S,Q) & ccw(T,S,R) & ccw(T,P,Q) & ccw(T,Q,R))
         => ccw(T,P,R)))).

% --- hull edge WITHIN the 4-set {A,B,C,D}: the pair is an ordered pair of
%     distinct points of the set; both of the two remaining points lie on the
%     same side of the directed line XY (ccw(X,Y,Z) for every third Z).
fof(hull_edge_def, axiom,
    ![X,Y,A,B,C,D] : ((X != Y
                     & A != B & A != C & A != D & B != C & B != D & C != D
                     & ( (X = A & (Y = B | Y = C | Y = D))
                       | (X = B & (Y = A | Y = C | Y = D))
                       | (X = C & (Y = A | Y = B | Y = D))
                       | (X = D & (Y = A | Y = B | Y = C)) )) =>
        ( hull_edge(X,Y,A,B,C,D) <=>
            ! [Z] : ( (Z = A | Z = B | Z = C | Z = D)
                      & Z != X & Z != Y => ccw(X,Y,Z) ) ) )).

% --- hull vertex of the 4-set: incident with some hull edge
fof(hull_vertex_def, axiom,
    ![P,A,B,C,D] : ((A != B & A != C & A != D & B != C & B != D & C != D
                   & (P = A | P = B | P = C | P = D)) =>
        ( hull_vertex(P,A,B,C,D) <=>
            ? [Q] : ( (Q = A | Q = B | Q = C | Q = D) & Q != P
                      & ( hull_edge(P,Q,A,B,C,D)
                        | hull_edge(Q,P,A,B,C,D) ) ) ) )).

% --- convex quadrilateral: all four points are hull vertices
fof(convex4_def, axiom,
    ![A,B,C,D] : ((A != B & A != C & A != D & B != C & B != D & C != D) =>
        ( convex4(A,B,C,D) <=>
            ( hull_vertex(A,A,B,C,D) & hull_vertex(B,A,B,C,D)
            & hull_vertex(C,A,B,C,D) & hull_vertex(D,A,B,C,D) ) ) )).

% --- the claim: among the 5 points there is a convex quadrilateral
fof(goal, conjecture,
    ?[A,B,C,D] : ( A != B & A != C & A != D & B != C & B != D & C != D
                   & convex4(A,B,C,D) )).