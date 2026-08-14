% ---------------------------------------------------------------
% Refutation attempt against G-hexorchard-visibility, first step:
%   "the six boundary axes contribute n visible points each"
% Fragment that could still be false: the axis points at axial
% distance 1 and 2 in the order-2 hexagonal orchard.
%
% Definition (from the problem statement): a point is hidden from the
% centre when some lattice point lies strictly between it and the centre
% on the same ray (a point closer to it).  In true lattice geometry,
% (1,0), (0,1), (1,-1) and their negatives lie strictly between the
% origin and (2,0), (0,2), (2,-2) and their negatives: gcd(2,0)=2>1,
% so all six distance-2 axis points are HIDDEN.  Hence each of the six
% axis rays carries exactly ONE visible non-origin point at any order
% n >= 1, not n.  The claim is false at n = 2.
%
% Constants (axial coordinates of order-2 hexagon):
%   x1=(1,0)  x2=(2,0)   nx1=(-1,0)  nx2=(-2,0)
%   y1=(0,1)  y2=(0,2)   ny1=(0,-1)  ny2=(0,-2)
%   d1=(1,-1) d2=(2,-2)  nd1=(-1,1)  nd2=(-2,2)
% blocks(Q,P): Q is a lattice point strictly between the origin and P
%              on the same ray.
% ---------------------------------------------------------------

fof(blocks_facts, axiom,
    blocks(x1, x2) & blocks(nx1, nx2) &
    blocks(y1, y2) & blocks(ny1, ny2) &
    blocks(d1, d2) & blocks(nd1, nd2)).

fof(visible_definition, axiom,
    ! [P] : (visible(P) <=> ~ ? [Q] : blocks(Q, P))).

fof(axis_points, axiom,
    axis_point(x1) & axis_point(x2) &
    axis_point(nx1) & axis_point(nx2) &
    axis_point(y1) & axis_point(y2) &
    axis_point(ny1) & axis_point(ny2) &
    axis_point(d1) & axis_point(d2) &
    axis_point(nd1) & axis_point(nd2)).

fof(distinct_points, axiom,
    x1 != x2 & x1 != nx1 & x1 != nx2 & x1 != y1 & x1 != y2 &
    x1 != ny1 & x1 != ny2 & x1 != d1 & x1 != d2 & x1 != nd1 & x1 != nd2 &
    x2 != nx1 & x2 != nx2 & x2 != y1 & x2 != y2 &
    x2 != ny1 & x2 != ny2 & x2 != d1 & x2 != d2 & x2 != nd1 & x2 != nd2 &
    nx1 != nx2 & nx1 != y1 & nx1 != y2 & nx1 != ny1 & nx1 != ny2 &
    nx1 != d1 & nx1 != d2 & nx1 != nd1 & nx1 != nd2 &
    nx2 != y1 & nx2 != y2 & nx2 != ny1 & nx2 != ny2 &
    nx2 != d1 & nx2 != d2 & nx2 != nd1 & nx2 != nd2 &
    y1 != y2 & y1 != ny1 & y1 != ny2 & y1 != d1 & y1 != d2 &
    y1 != nd1 & y1 != nd2 &
    y2 != ny1 & y2 != ny2 & y2 != d1 & y2 != d2 & y2 != nd1 & y2 != nd2 &
    ny1 != ny2 & ny1 != d1 & ny1 != d2 & ny1 != nd1 & ny1 != nd2 &
    ny2 != d1 & ny2 != d2 & ny2 != nd1 & ny2 != nd2 &
    d1 != d2 & d1 != nd1 & d1 != nd2 & d2 != nd1 & d2 != nd2 &
    nd1 != nd2).

% The statement being attacked: the six boundary axes contribute n
% visible points each; for order n=2 that means all twelve axis points
% (distance 1 and 2 on each ray) are visible from the centre.
fof(axis_claim, conjecture,
    ! [P] : (axis_point(P) => visible(P))).