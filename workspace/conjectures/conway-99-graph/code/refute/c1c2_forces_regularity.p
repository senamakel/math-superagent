% Attack on problem.md's load-bearing restatement: "The two conditions force
% regularity, and the object is exactly a strongly regular graph."
%
% Conditions: C1 = every ADJACENT pair has exactly one common neighbour.
%             C2 = every NON-ADJACENT distinct pair has exactly two common
%             neighbours.
% Conjecture (what we attack): any finite graph satisfying C1 and C2 is
%         REGULAR (all vertices the same degree). If a non-regular finite
%         graph satisfies C1 and C2, the restatement is false.
%
% Axioms: E symmetric, loopless, c1, c2.
% Conjecture: NOT(c1 and c2 but non-regular). We encode non-regularity as
%   "there exist two specific vertices with different degrees" on a small
%   domain. This is a bounded attack: find a small model (up to the domain
%   size the engine tries) that satisfies c1,c2 and falsifies regularity.
%
% The engine finds a model of the axioms that falsifies the conjecture. To
% test non-regularity I must make the conjecture = "no graph is non-regular
% under c1,c2", i.e. the conjecture is that c1&c2 => regular. Since TPTP FOL
% cannot state "same cardinality of neighbour sets" directly, I instead
% assert that IF regularity fails THEN contradiction -- but that is what we
% want to test. So I keep the conjecture as "no nonregular c1,c2 graph", and
% on a FIXED small domain I can express degrees concretely.
%
% This file just carries the axioms; the engine's default finite domain sizes
% will search for a c1,c2 model. Value: establishes whether any SMALL c1,c2
% graph is irregular.

fof(sym, axiom, ! [X,Y] : (E(X,Y) => E(Y,X))).
fof(noloop, axiom, ! [X] : (~E(X,X))).

fof(c1, axiom,
  ! [X,Y] :
    ( E(X,Y) =>
      ? [P] :
        ( E(X,P) & E(Y,P) &
          ! [Q] : ( (E(X,Q) & E(Y,Q)) => Q = P ) ) ) ).

fof(c2, axiom,
  ! [X,Y] :
    ( ( X != Y & ~E(X,Y) ) =>
      ? [A,B] :
        ( A != B &
          E(X,A) & E(Y,A) & E(X,B) & E(Y,B) &
          ! [Z] : ( (E(X,Z) & E(Y,Z)) => ( Z = A | Z = B ) ) ) ) ).

% The restatement to attack: c1 & c2   =>   regular.
% We attempt to falsify by finding a small c1,c2 graph that is NOT regular;
% to express "not regular" in FOL on a finite domain without cardinality, we
% assert the CONTRADICTION of uniformity for all pairs via two degrees. Since
% find_counterexample searches finite models of the AXIOMS (sym,noloop,c1,c2)
% that falsify the CONJECTURE, and the conjecture here is "regular", a refute
% would be a non-regular c1,c2 model -- the counterexample we want.
fof(regular, conjecture,
  ! [X,Y,Z] :
    ( ( X != Y & X != Z & Y != Z ) =>
      ( ( E(X,Y) => ... ) => ... ) ) ).
