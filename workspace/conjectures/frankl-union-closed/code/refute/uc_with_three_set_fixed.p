% Refutation target: R-uc-with-three-set (open rung of the Frankl ladder).
%
%   "Every union-closed family F != {empty} that contains a 3-element set
%    {x,y,z} has an element (not necessarily in {x,y,z}) in at least |F|/2
%    members."
%
% A counterexample = a union-closed family containing a 3-set with NO element
% in >= |F|/2 members.
%
% CORRECTED ENCODING. The earlier uc_with_three_set.p let a sat model collapse
% several member slots onto one object (s1=s2=s3=s4), so the genuine |F| was 3
% not 6 and "no element in >=3 of the 6 slots" was satisfied by multiplicity.
% This file FORCES the six slots to be six genuinely DISTINCT member sets:
% for every pair of distinct slots there is an element on which they differ.
% That removes the collapse exploit, so a CounterSatisfiable verdict here would
% be a GENUINE bounded counterexample (which the literature's n<=12 / |F|<=50
% verification says cannot exist on a 4-element ground set).
%
% BOUNDED FRAGMENT: ground set = 4 elements {e1,e2,e3,e4}, family of exactly 6
% distinct members containing the 3-set {e1,e2,e3}, union-closed, no element in
% >= 3 members (|F|=6 so abundant means >=3).

fof(elements_distinct, axiom,
    ( e1 != e2 & e1 != e3 & e1 != e4
    & e2 != e3 & e2 != e4
    & e3 != e4 ) ).

% the six member slots are pairwise DISTINCT objects (else the finder collapses
% several onto one domain value and the |F|=6 counting is abetted by multiplicity)
fof(slots_pairwise_distinct_objects, axiom,
    ( s1 != s2 & s1 != s3 & s1 != s4 & s1 != s5 & s1 != s6
    & s2 != s3 & s2 != s4 & s2 != s5 & s2 != s6
    & s3 != s4 & s3 != s5 & s3 != s6
    & s4 != s5 & s4 != s6
    & s5 != s6 ) ).

% six member slots are six genuinely DISTINCT member sets: every pair of
% distinct slots differs on some element (member-in-one xor member-in-other).
fof(slots_pairwise_distinct_sets, axiom,
    ( ! [I,J] :
        ( ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
          & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 )
          & I != J )
        => ? [E] :
            ( ( member(I,E) & ~ member(J,E) )
            | ( ~ member(I,E) & member(J,E) ) ) ) ) ).

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

% no element is in >= 3 of the 6 distinct members  ==  every element in <= 2.
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

% conjecture: some element IS abundant (in >= 3 of the 6 distinct members)
fof(goal, conjecture,
    ( ? [E] :
        ( ( E = e1 | E = e2 | E = e3 | E = e4 )
        & ? [I,J,K] :
            ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
            & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 )
            & ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
            & I != J & J != K & I != K
            & member(I,E) & member(J,E) & member(K,E) ) ) ) ).
