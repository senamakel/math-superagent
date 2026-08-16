% Refutation target: R-uc-with-three-set (open rung of the Frankl ladder).
%
%   "Every union-closed family F != {empty} that contains a 3-element set
%    {x,y,z} has an element (not necessarily in {x,y,z}) in at least |F|/2
%    members."
%
% A counterexample = a union-closed family containing a 3-set with NO element
% in >= |F|/2 members.  This is exactly a UC counterexample among families
% that contain a 3-set, so none is known at small size.
%
% BOUNDED FRAGMENT we actually search: ground set = 4 elements {e1,e2,e3,e4},
% family of exactly 6 distinct members (slots s1..s6), containing the 3-set
% {e1,e2,e3}, union-closed within itself, with NO element in >= 3 of the 6
% members (|F|=6, so abundant means in >= 3).  This is the SMALLEST 3-set
% containing fragment where the element may lie outside {e1,e2,e3} (we add e4).
%
% The engine looks for a finite structure satisfying the axioms below and
% falsifying the conjecture "some element is abundant".  refuted => found such
% a family (a genuine counterexample to the rung, and UC).  proved/undecided =>
% none at this bounded size, which matches the known verification.

% --- genuine distinctness: the 4 elements and the 6 member slots must be
% --- genuinely distinct objects, else the finder collapses everything onto
% --- one domain value and every distinctness-guarded clause is vacuous.
fof(elements_distinct, axiom,
    ( e1 != e2 & e1 != e3 & e1 != e4
    & e2 != e3 & e2 != e4
    & e3 != e4 ) ).

% the six member slots must be distinct AS SETS (two distinct slots differ on
% some element); otherwise duplicates let abundance over slots betray |F|.
fof(slots_distinct_sets, axiom,
    ( ! [I,J] :
        ( ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
          & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 ) )
        => ( I = J
          | ? [E] : ( ( member(I,E) & ~ member(J,E) )
                    | ( ~ member(I,E) & member(J,E) ) ) ) ) ) ).

% union-closed: for every pair of slots, some slot equals their union
fof(union_closed, axiom,
    ( ! [I,J] :
        ( ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
          & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 ) )
        => ? [K] :
            ( ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
            & ! [E] : ( member(K,E)
                        <=> ( member(I,E) | member(J,E) ) ) ) ) ) ).

% contains the 3-element set {e1,e2,e3} (some slot has exactly these)
fof(contains_threeset, axiom,
    ( ? [K] :
        ( ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
        & ! [E] : ( member(K,E)
                    <=> ( E = e1 | E = e2 | E = e3 ) ) ) ) ).

% F != {empty}: the family is nonempty (6 slots), so automatically.

% no element is in >= 3 of the 6 members  ==  every element in <= 2 members.
fof(no_abundant_e1, axiom,
    ( ! [I,J,K] :
        ( ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
          & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 )
          & ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
          & I != J & J != K & I != K )
        => ( ~ member(I,e1) | ~ member(J,e1) | ~ member(K,e1) ) ) ) ).

fof(no_abundant_e2, axiom,
    ( ! [I,J,K] :
        ( ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
          & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 )
          & ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
          & I != J & J != K & I != K )
        => ( ~ member(I,e2) | ~ member(J,e2) | ~ member(K,e2) ) ) ) ).

fof(no_abundant_e3, axiom,
    ( ! [I,J,K] :
        ( ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
          & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 )
          & ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
          & I != J & J != K & I != K )
        => ( ~ member(I,e3) | ~ member(J,e3) | ~ member(K,e3) ) ) ) ).

fof(no_abundant_e4, axiom,
    ( ! [I,J,K] :
        ( ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
          & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 )
          & ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
          & I != J & J != K & I != K )
        => ( ~ member(I,e4) | ~ member(J,e4) | ~ member(K,e4) ) ) ) ).

% conjecture: some element IS abundant (in >= 3 of the 6 members)
fof(goal, conjecture,
    ( ? [E] :
        ( ( E = e1 | E = e2 | E = e3 | E = e4 )
        & ? [I,J,K] :
            ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
            & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 )
            & ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
            & I != J & J != K & I != K
            & member(I,E) & member(J,E) & member(K,E) ) ) ) ).
