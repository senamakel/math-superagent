% Diagnostic: the SAME fragment as r-one-interior-n4.p but WITHOUT the
% at-most-one-interior axiom.  The conjecture is then: any 5 points in
% general position (abstract rank-3 chirotope fragment) contain a convex
% quadrilateral -- i.e. the 4-point-criterion version of the settled claim
% ES(4)=5 (library: es-exact-values, es35-four-criterion, proved).
%
% Purpose: check whether the interior axiom was load-bearing in the
% r-one-interior-n4.p proof, and whether this fragment independently proves
% ES(4)=5 in the abstract order-type setting.  Nothing here is new
% mathematics -- ES(4)=5 is proved (Klein) -- but a machine proof in this
% fragment is the first rung of the run's own encoder-validation ladder
% (reproduce a known answer before trusting an encoder).

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

fof(convex4_def, axiom,
    ![A,B,C,D] : ((A != B & A != C & A != D & B != C & B != D & C != D) =>
        ( convex4(A,B,C,D) <=>
            ~( inside(A,B,C,D) | inside(B,A,C,D)
             | inside(C,A,B,D) | inside(D,A,B,C) ) ))).

fof(goal, conjecture,
    ?[A,B,C,D] : ( A != B & A != C & A != D & B != C & B != D & C != D
                   & convex4(A,B,C,D) )).