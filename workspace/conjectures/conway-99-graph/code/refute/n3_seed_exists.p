% Attack on the n3 premise used by goal G-n3-positive: is the n3 configuration
% (a 2-edge-joined disjoint triangle pair) compatible with lambda=1 and mu=2 in
% ANY finite graph, or inherently contradictory under those two axioms alone?
%
% The run has established: seed locally consistent at radius 1 (extends to 2
% assignments); n3>=1 IS witnessed in the mu>=4 lambda=1 family (Brouwer-Haemers
% (81,20,1,6), Games (729,112,1,20)); but there is NO mu=2 witness known. This
% encoding asks: does ANY finite graph satisfying lambda=1,mu=2 contain a
% 2-edge-joined disjoint triangle pair? If yes, the n3 seed is NOT inherently
% contradictory under lambda=1,mu=2, and any obstruction must be 99/k=14-
% specific. If no, the seed is globally impossible under the axioms alone.
%
% Axioms: E symmetric, loopless, C1 (adjacent => exactly one common neighbour),
%         C2 (non-adjacent distinct => exactly two common neighbours).
% Conjecture (what we attack): no such graph contains the n3 seed.
%
% find_counterexample returns refuted iff it finds a finite lambda=1,mu=2 graph
% CONTAINING a 2-edge-joined disjoint triangle pair.

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

% The n3 seed: two disjoint triangles joined by exactly two cross edges.
% T1={a,b,c}, T2={d,e,f}; cross edges a-d, b-e; other seven cross pairs
% non-adjacent; all six distinct.
fof(no_seed, conjecture,
  ~ ( ? [A,B,C,D,Ee,F] :
    ( A != B & A != C & B != C &
      D != Ee & D != F & Ee != F &
      A != D & A != Ee & A != F &
      B != D & B != Ee & B != F &
      C != D & C != Ee & C != F &
      E(A,B) & E(A,C) & E(B,C) &
      E(D,Ee) & E(D,F) & E(Ee,F) &
      E(A,D) & E(B,Ee) &
      ~E(A,Ee) & ~E(A,F) & ~E(B,D) & ~E(B,F) &
      ~E(C,D) & ~E(C,Ee) & ~E(C,F) ) ) ).
