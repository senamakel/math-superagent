% --- Refutation attempt: sharp-kernel-4color / S-universe-4color ---
%
% Conjecture: every finite graph with
%     (a) minimum degree >= 4
%     (b) K4-free
%     (c) K_{2,3}-free
%     (d) every vertex-neighbourhood induces max degree <= 2
% is 4-colourable.
%
% These four conditions ARE the finite "kernel" C_N that the size-bound
% skeleton reduces every candidate 5-chromatic unit-distance graph to.  If a
% finite model satisfies (a)-(d) but has no proper 4-colouring, the conjecture
% is refuted and the whole reduction to 4-colourability-of-the-kernel fails
% beyond that size.
%
% Intended obstruction: a 5-critical subgraph of a 5-chromatic graph of girth
% 5 satisfies (a) [critical => deg>=4], (b) [no triangles], (c) [no 4-cycles],
% (d) [triangle-free => neighbourhood independent].  Such graphs exist.
%
% Colours are the four constants c0,c1,c2,c3; has_colour(V,C) is the colour
% assignment.  The conjecture asserts a proper 4-colouring exists.

fof(irrefl, axiom, ![X]: ~edge(X,X)).
fof(symm, axiom, ![X,Y]: (edge(X,Y) => edge(Y,X))).

% (a) minimum degree >= 4
fof(mindeg, axiom,
    ![X] : ?[A,B,C,D] :
      ( A != B & A != C & A != D & B != C & B != D & C != D &
        edge(X,A) & edge(X,B) & edge(X,C) & edge(X,D) )).

% (b) K4-free
fof(k4free, axiom,
    ~?[A,B,C,D] :
      ( A != B & A != C & A != D & B != C & B != D & C != D &
        edge(A,B) & edge(A,C) & edge(A,D) &
        edge(B,C) & edge(B,D) & edge(C,D) )).

% (c) K_{2,3}-free : no two vertices share 3 distinct common neighbours
fof(k23free, axiom,
    ~?[A,B,C,D,E] :
      ( A != B &
        C != D & C != E & D != E &
        edge(A,C) & edge(A,D) & edge(A,E) &
        edge(B,C) & edge(B,D) & edge(B,E) )).

% (d) every vertex-neighbourhood induces max degree <= 2 : no neighbour Y of X
% shares >=3 neighbours U,V,W with X
fof(nbhdmaxdeg, axiom,
    ~?[X,Y,U,V,W] :
      ( U != V & U != W & V != W &
        edge(X,Y) & edge(X,U) & edge(X,V) & edge(X,W) &
        edge(Y,U) & edge(Y,V) & edge(Y,W) )).

% --- four distinct colours ---
fof(colordistinct, axiom,
    c0 != c1 & c0 != c2 & c0 != c3 & c1 != c2 & c1 != c3 & c2 != c3).

% --- conjecture: a proper 4-colouring exists ---
% every vertex gets at least one colour; adjacent vertices get no colour in
% common; each vertex gets a colour (at-least-one).  Also, to be a proper
% colouring, a vertex must not be forced to need more than 4 (covered by
% at-least-one with exactly 4 colours available).  No at-most-one needed since
% a vertex may vacuously take several, but we forbid equal adjacent colours
% which is the only requirement.
fof(claim, conjecture,
    ( ![X] : ( has_colour(X,c0) | has_colour(X,c1) |
               has_colour(X,c2) | has_colour(X,c3) ) &
      ![X,Y] : ( edge(X,Y) =>
                   ~( has_colour(X,c0) & has_colour(Y,c0) ) ) &
      ![X,Y] : ( edge(X,Y) =>
                   ~( has_colour(X,c1) & has_colour(Y,c1) ) ) &
      ![X,Y] : ( edge(X,Y) =>
                   ~( has_colour(X,c2) & has_colour(Y,c2) ) ) &
      ![X,Y] : ( edge(X,Y) =>
                   ~( has_colour(X,c3) & has_colour(Y,c3) ) ) )).
