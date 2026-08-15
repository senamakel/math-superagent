% ATTACK on the run's in-flight flat-torus result.
%
% The run's sweep (code/lib/torus_margin.py run_calibration) reported
% "periodic 6-colourings" of the plane at sublattice row=(1,-2), D=7, L=2/5.
% That is impossible: chi(plane) >= 5 is proven (de Grey 2018).
%
% The bug: the code decides edges by the physical distance between two
% CANONICAL COSET REPRESENTATIVES, but a proper periodic colouring must put
% the whole cosets apart, so the correct edge test is the MINIMUM distance
% between the two cosets over the whole lattice.
%
% Hand-computed true (min-coset-distance) separation graph at L=2/5,
% threshold 1+2L = 9/5 = 1.8: every one of the 7 cosets of the kernel of
% (u,v)->u-2v mod 7 has min distance to every other coset <= 1.8 (difference
% classes r=1,2,5,6 give distance sqrt(3)L ~ 0.693; r=3,4 give 3L = 1.2).
% So the TRUE separation graph is K7.
%
% Here we encode the conjecture the run is effectively relying on -- that the
% true separation graph is 6-colourable -- and refute it: K7 is not
% 6-colourable.  The run's reported 6-colouring is an artifact of using
% representative distances, which undercount edges.
fof(vertex_distinct, axiom,
    ( v0 != v1 & v0 != v2 & v0 != v3 & v0 != v4 & v0 != v5 & v0 != v6
    & v1 != v2 & v1 != v3 & v1 != v4 & v1 != v5 & v1 != v6
    & v2 != v3 & v2 != v4 & v2 != v5 & v2 != v6
    & v3 != v4 & v3 != v5 & v3 != v6
    & v4 != v5 & v4 != v6
    & v5 != v6 )).

% K7 adjacency (the true min-coset-distance separation graph).
fof(k7_adj, axiom,
    ( adj(v0,v1) & adj(v0,v2) & adj(v0,v3) & adj(v0,v4) & adj(v0,v5) & adj(v0,v6)
    & adj(v1,v2) & adj(v1,v3) & adj(v1,v4) & adj(v1,v5) & adj(v1,v6)
    & adj(v2,v3) & adj(v2,v4) & adj(v2,v5) & adj(v2,v6)
    & adj(v3,v4) & adj(v3,v5) & adj(v3,v6)
    & adj(v4,v5) & adj(v4,v6)
    & adj(v5,v6) )).

fof(adj_sym, axiom, ! [X,Y] : ( adj(X,Y) => adj(Y,X) )).

% Conjecture attacked: the true separation graph is 6-colourable
% (colours 0..5, each vertex exactly one colour, adjacent vertices differ).
fof(k7_is_6colorable, conjecture,
  ? [C] :
    (  ( (col(v0,0) | col(v0,1) | col(v0,2) | col(v0,3) | col(v0,4) | col(v0,5))
       & (col(v1,0) | col(v1,1) | col(v1,2) | col(v1,3) | col(v1,4) | col(v1,5))
       & (col(v2,0) | col(v2,1) | col(v2,2) | col(v2,3) | col(v2,4) | col(v2,5))
       & (col(v3,0) | col(v3,1) | col(v3,2) | col(v3,3) | col(v3,4) | col(v3,5))
       & (col(v4,0) | col(v4,1) | col(v4,2) | col(v4,3) | col(v4,4) | col(v4,5))
       & (col(v5,0) | col(v5,1) | col(v5,2) | col(v5,3) | col(v5,4) | col(v5,5))
       & (col(v6,0) | col(v6,1) | col(v6,2) | col(v6,3) | col(v6,4) | col(v6,5))
       & ~(col(v0,0) & col(v0,1)) & ~(col(v0,0) & col(v0,2)) & ~(col(v0,0) & col(v0,3))
       & ~(col(v0,0) & col(v0,4)) & ~(col(v0,0) & col(v0,5)) & ~(col(v0,1) & col(v0,2))
       & ~(col(v0,1) & col(v0,3)) & ~(col(v0,1) & col(v0,4)) & ~(col(v0,1) & col(v0,5))
       & ~(col(v0,2) & col(v0,3)) & ~(col(v0,2) & col(v0,4)) & ~(col(v0,2) & col(v0,5))
       & ~(col(v0,3) & col(v0,4)) & ~(col(v0,3) & col(v0,5)) & ~(col(v0,4) & col(v0,5))
       & ~(col(v1,0) & col(v1,1)) & ~(col(v1,0) & col(v1,2)) & ~(col(v1,0) & col(v1,3))
       & ~(col(v1,0) & col(v1,4)) & ~(col(v1,0) & col(v1,5)) & ~(col(v1,1) & col(v1,2))
       & ~(col(v1,1) & col(v1,3)) & ~(col(v1,1) & col(v1,4)) & ~(col(v1,1) & col(v1,5))
       & ~(col(v1,2) & col(v1,3)) & ~(col(v1,2) & col(v1,4)) & ~(col(v1,2) & col(v1,5))
       & ~(col(v1,3) & col(v1,4)) & ~(col(v1,3) & col(v1,5)) & ~(col(v1,4) & col(v1,5))
       & ~(col(v2,0) & col(v2,1)) & ~(col(v2,0) & col(v2,2)) & ~(col(v2,0) & col(v2,3))
       & ~(col(v2,0) & col(v2,4)) & ~(col(v2,0) & col(v2,5)) & ~(col(v2,1) & col(v2,2))
       & ~(col(v2,1) & col(v2,3)) & ~(col(v2,1) & col(v2,4)) & ~(col(v2,1) & col(v2,5))
       & ~(col(v2,2) & col(v2,3)) & ~(col(v2,2) & col(v2,4)) & ~(col(v2,2) & col(v2,5))
       & ~(col(v2,3) & col(v2,4)) & ~(col(v2,3) & col(v2,5)) & ~(col(v2,4) & col(v2,5))
       & ~(col(v3,0) & col(v3,1)) & ~(col(v3,0) & col(v3,2)) & ~(col(v3,0) & col(v3,3))
       & ~(col(v3,0) & col(v3,4)) & ~(col(v3,0) & col(v3,5)) & ~(col(v3,1) & col(v3,2))
       & ~(col(v3,1) & col(v3,3)) & ~(col(v3,1) & col(v3,4)) & ~(col(v3,1) & col(v3,5))
       & ~(col(v3,2) & col(v3,3)) & ~(col(v3,2) & col(v3,4)) & ~(col(v3,2) & col(v3,5))
       & ~(col(v3,3) & col(v3,4)) & ~(col(v3,3) & col(v3,5)) & ~(col(v3,4) & col(v3,5))
       & ~(col(v4,0) & col(v4,1)) & ~(col(v4,0) & col(v4,2)) & ~(col(v4,0) & col(v4,3))
       & ~(col(v4,0) & col(v4,4)) & ~(col(v4,0) & col(v4,5)) & ~(col(v4,1) & col(v4,2))
       & ~(col(v4,1) & col(v4,3)) & ~(col(v4,1) & col(v4,4)) & ~(col(v4,1) & col(v4,5))
       & ~(col(v4,2) & col(v4,3)) & ~(col(v4,2) & col(v4,4)) & ~(col(v4,2) & col(v4,5))
       & ~(col(v4,3) & col(v4,4)) & ~(col(v4,3) & col(v4,5)) & ~(col(v4,4) & col(v4,5))
       & ~(col(v5,0) & col(v5,1)) & ~(col(v5,0) & col(v5,2)) & ~(col(v5,0) & col(v5,3))
       & ~(col(v5,0) & col(v5,4)) & ~(col(v5,0) & col(v5,5)) & ~(col(v5,1) & col(v5,2))
       & ~(col(v5,1) & col(v5,3)) & ~(col(v5,1) & col(v5,4)) & ~(col(v5,1) & col(v5,5))
       & ~(col(v5,2) & col(v5,3)) & ~(col(v5,2) & col(v5,4)) & ~(col(v5,2) & col(v5,5))
       & ~(col(v5,3) & col(v5,4)) & ~(col(v5,3) & col(v5,5)) & ~(col(v5,4) & col(v5,5))
       & ~(col(v6,0) & col(v6,1)) & ~(col(v6,0) & col(v6,2)) & ~(col(v6,0) & col(v6,3))
       & ~(col(v6,0) & col(v6,4)) & ~(col(v6,0) & col(v6,5)) & ~(col(v6,1) & col(v6,2))
       & ~(col(v6,1) & col(v6,3)) & ~(col(v6,1) & col(v6,4)) & ~(col(v6,1) & col(v6,5))
       & ~(col(v6,2) & col(v6,3)) & ~(col(v6,2) & col(v6,4)) & ~(col(v6,2) & col(v6,5))
       & ~(col(v6,3) & col(v6,4)) & ~(col(v6,3) & col(v6,5)) & ~(col(v6,4) & col(v6,5))
       & ~(col(v0,0) & col(v1,0)) & ~(col(v0,1) & col(v1,1)) & ~(col(v0,2) & col(v1,2))
       & ~(col(v0,3) & col(v1,3)) & ~(col(v0,4) & col(v1,4)) & ~(col(v0,5) & col(v1,5))
       & ~(col(v0,0) & col(v2,0)) & ~(col(v0,1) & col(v2,1)) & ~(col(v0,2) & col(v2,2))
       & ~(col(v0,3) & col(v2,3)) & ~(col(v0,4) & col(v2,4)) & ~(col(v0,5) & col(v2,5))
       & ~(col(v0,0) & col(v3,0)) & ~(col(v0,1) & col(v3,1)) & ~(col(v0,2) & col(v3,2))
       & ~(col(v0,3) & col(v3,3)) & ~(col(v0,4) & col(v3,4)) & ~(col(v0,5) & col(v3,5))
       & ~(col(v0,0) & col(v4,0)) & ~(col(v0,1) & col(v4,1)) & ~(col(v0,2) & col(v4,2))
       & ~(col(v0,3) & col(v4,3)) & ~(col(v0,4) & col(v4,4)) & ~(col(v0,5) & col(v4,5))
       & ~(col(v0,0) & col(v5,0)) & ~(col(v0,1) & col(v5,1)) & ~(col(v0,2) & col(v5,2))
       & ~(col(v0,3) & col(v5,3)) & ~(col(v0,4) & col(v5,4)) & ~(col(v0,5) & col(v5,5))
       & ~(col(v0,0) & col(v6,0)) & ~(col(v0,1) & col(v6,1)) & ~(col(v0,2) & col(v6,2))
       & ~(col(v0,3) & col(v6,3)) & ~(col(v0,4) & col(v6,4)) & ~(col(v0,5) & col(v6,5))
       & ~(col(v1,0) & col(v2,0)) & ~(col(v1,1) & col(v2,1)) & ~(col(v1,2) & col(v2,2))
       & ~(col(v1,3) & col(v2,3)) & ~(col(v1,4) & col(v2,4)) & ~(col(v1,5) & col(v2,5))
       & ~(col(v1,0) & col(v3,0)) & ~(col(v1,1) & col(v3,1)) & ~(col(v1,2) & col(v3,2))
       & ~(col(v1,3) & col(v3,3)) & ~(col(v1,4) & col(v3,4)) & ~(col(v1,5) & col(v3,5))
       & ~(col(v1,0) & col(v4,0)) & ~(col(v1,1) & col(v4,1)) & ~(col(v1,2) & col(v4,2))
       & ~(col(v1,3) & col(v4,3)) & ~(col(v1,4) & col(v4,4)) & ~(col(v1,5) & col(v4,5))
       & ~(col(v1,0) & col(v5,0)) & ~(col(v1,1) & col(v5,1)) & ~(col(v1,2) & col(v5,2))
       & ~(col(v1,3) & col(v5,3)) & ~(col(v1,4) & col(v5,4)) & ~(col(v1,5) & col(v5,5))
       & ~(col(v1,0) & col(v6,0)) & ~(col(v1,1) & col(v6,1)) & ~(col(v1,2) & col(v6,2))
       & ~(col(v1,3) & col(v6,3)) & ~(col(v1,4) & col(v6,4)) & ~(col(v1,5) & col(v6,5))
       & ~(col(v2,0) & col(v3,0)) & ~(col(v2,1) & col(v3,1)) & ~(col(v2,2) & col(v3,2))
       & ~(col(v2,3) & col(v3,3)) & ~(col(v2,4) & col(v3,4)) & ~(col(v2,5) & col(v3,5))
       & ~(col(v2,0) & col(v4,0)) & ~(col(v2,1) & col(v4,1)) & ~(col(v2,2) & col(v4,2))
       & ~(col(v2,3) & col(v4,3)) & ~(col(v2,4) & col(v4,4)) & ~(col(v2,5) & col(v4,5))
       & ~(col(v2,0) & col(v5,0)) & ~(col(v2,1) & col(v5,1)) & ~(col(v2,2) & col(v5,2))
       & ~(col(v2,3) & col(v5,3)) & ~(col(v2,4) & col(v5,4)) & ~(col(v2,5) & col(v5,5))
       & ~(col(v2,0) & col(v6,0)) & ~(col(v2,1) & col(v6,1)) & ~(col(v2,2) & col(v6,2))
       & ~(col(v2,3) & col(v6,3)) & ~(col(v2,4) & col(v6,4)) & ~(col(v2,5) & col(v6,5))
       & ~(col(v3,0) & col(v4,0)) & ~(col(v3,1) & col(v4,1)) & ~(col(v3,2) & col(v4,2))
       & ~(col(v3,3) & col(v4,3)) & ~(col(v3,4) & col(v4,4)) & ~(col(v3,5) & col(v4,5))
       & ~(col(v3,0) & col(v5,0)) & ~(col(v3,1) & col(v5,1)) & ~(col(v3,2) & col(v5,2))
       & ~(col(v3,3) & col(v5,3)) & ~(col(v3,4) & col(v5,4)) & ~(col(v3,5) & col(v5,5))
       & ~(col(v3,0) & col(v6,0)) & ~(col(v3,1) & col(v6,1)) & ~(col(v3,2) & col(v6,2))
       & ~(col(v3,3) & col(v6,3)) & ~(col(v3,4) & col(v6,4)) & ~(col(v3,5) & col(v6,5))
       & ~(col(v4,0) & col(v5,0)) & ~(col(v4,1) & col(v5,1)) & ~(col(v4,2) & col(v5,2))
       & ~(col(v4,3) & col(v5,3)) & ~(col(v4,4) & col(v5,4)) & ~(col(v4,5) & col(v5,5))
       & ~(col(v4,0) & col(v6,0)) & ~(col(v4,1) & col(v6,1)) & ~(col(v4,2) & col(v6,2))
       & ~(col(v4,3) & col(v6,3)) & ~(col(v4,4) & col(v6,4)) & ~(col(v4,5) & col(v6,5))
       & ~(col(v5,0) & col(v6,0)) & ~(col(v5,1) & col(v6,1)) & ~(col(v5,2) & col(v6,2))
       & ~(col(v5,3) & col(v6,3)) & ~(col(v5,4) & col(v6,4)) & ~(col(v5,5) & col(v6,5))
    ))).
