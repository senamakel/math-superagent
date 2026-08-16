% Attack on claim c7: in a graph with lambda=1 (every edge in exactly one
% triangle) and mu=2 (every non-adjacent pair has exactly two common
% neighbours), the two common neighbours of any non-adjacent pair are
% NON-adjacent to each other.
%
% Axioms: E symmetric, loopless, C1 (adjacent => exactly one common neighbour),
%         C2 (non-adjacent => exactly two common neighbours).
% Conjecture (the claim being attacked): the two common neighbours of any
%         non-adjacent pair are non-adjacent.
%
% If find_counterexample returns refuted, there is a graph satisfying C1,C2
% where some non-adjacent pair has two ADJACENT common neighbours -> c7 false.
%
% Hand-check: if nonadjacent u,w share two common neighbours a,b with a~b,
% then edge ab lies in triangle {u,a,b} AND in triangle {w,a,b}, two distinct
% triangles, contradicting C1 (ab in exactly one triangle). So c7 should hold.

fof(sym, axiom, ! [X,Y] : (E(X,Y) => E(Y,X))).
fof(noloop, axiom, ! [X] : (~E(X,X))).

% C1: adjacent pair has exactly one common neighbour.
fof(c1, axiom,
  ! [X,Y] :
    ( E(X,Y) =>
      ? [P] :
        ( E(X,P) & E(Y,P) &
          ! [Q] : ( (E(X,Q) & E(Y,Q)) => Q = P ) ) ) ).

% C2: non-adjacent distinct pair has exactly two common neighbours.
fof(c2, axiom,
  ! [X,Y] :
    ( ( X != Y & ~E(X,Y) ) =>
      ? [A,B] :
        ( A != B &
          E(X,A) & E(Y,A) & E(X,B) & E(Y,B) &
          ! [Z] : ( (E(X,Z) & E(Y,Z)) => ( Z = A | Z = B ) ) ) ) ).

% The claim being attacked (c7): common neighbours of a non-adjacent pair are
% mutually non-adjacent.
fof(c7, conjecture,
  ! [A,B,U,W] :
    ( ( U != W & ~E(U,W) & A != B &
        E(U,A) & E(W,A) & E(U,B) & E(W,B) ) =>
      ~E(A,B) ) ).
