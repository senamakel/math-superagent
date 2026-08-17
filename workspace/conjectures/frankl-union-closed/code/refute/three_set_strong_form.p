% Refutation target: STRONG form of R-uc-with-three-set.
%
%   STRONG: "Every union-closed family F != {empty} that contains a 3-element
%            set {x,y,z} has (at least) one of x,y,z in at least |F|/2 of its
%            members."
%
% Ellis-Ivan-Leader (claim ellis-ivan-leader-small-set-3-fails) refutes this
% STRONG form ASYMPTOTICALLY: for every eps>0 there is a union-closed family
% with unique smallest 3-set {x,y,z} whose elements each have frequency
% < (1+o(1))log_2 3 / 6  <  1/2.  But that construction is asymptotic; here we
% ask whether a SMALL finite witness (4-element ground set, 6 members) exists.
% A small explicit counterexample would be a concrete bankable witness
% complementing the asymptotic result.  (The WEAK rung -- some element anywhere
% abundant -- is NOT attacked here and stays open; this is only the strong form
% that EIL already says fails.)
%
% BOUNDED FRAGMENT: ground set {e1,e2,e3,e4}, family of exactly 6 DISTINCT
% members, contains the 3-set {e1,e2,e3}, union-closed, and e1,e2,e3 each in
% <= 2 of the 6 members (so none of the three is abundant, |F|=6 => abundant
% means in >= 3).  Conjecture: one of e1,e2,e3 IS abundant.  A model satisfying
% the axioms and falsifying this conjecture is a counterexample to the strong
% form.  find_counterexample: refuted => strong form false at this size;
% proved/undecided => no such small family (consistent with EIL being asymptotic).

fof(elements_distinct, axiom,
    ( e1 != e2 & e1 != e3 & e1 != e4
    & e2 != e3 & e2 != e4
    & e3 != e4 ) ).

% six member slots genuinely distinct objects (no collapse exploit)
fof(slots_pairwise_distinct_objects, axiom,
    ( s1 != s2 & s1 != s3 & s1 != s4 & s1 != s5 & s1 != s6
    & s2 != s3 & s2 != s4 & s2 != s5 & s2 != s6
    & s3 != s4 & s3 != s5 & s3 != s6
    & s4 != s5 & s4 != s6
    & s5 != s6 ) ).

% six member slots genuinely distinct as SETS (any pair differs on an element)
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

% contains the 3-element set {e1,e2,e3}: some slot has exactly these
fof(contains_threeset, axiom,
    ( ? [K] :
        ( ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
        & ! [E] : ( member(K,E)
                    <=> ( E = e1 | E = e2 | E = e3 ) ) ) ) ).

% F != {empty}: 6 distinct nonempty-aggregate members, automatic.

% --- e1, e2, e3 each appear in AT MOST 2 of the 6 DISTINCT members ---
% (negate: every triple of pairwise-distinct members avoids e_x)
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

% conjecture: one of e1,e2,e3 IS abundant (in >= 3 of the 6 distinct members).
% A model satisfying the axioms automatically falsifies this, since the axioms
% pin e1,e2,e3 each in <= 2 members.  So find_counterexample returning
% "refuted" means the axioms are satisfiable => a genuine UC family containing
% the 3-set with none of e1,e2,e3 abundant => strong form FALSE here.
fof(goal, conjecture,
    ( ? [E] :
        ( ( E = e1 | E = e2 | E = e3 )
        & ? [I,J,K] :
            ( ( I = s1 | I = s2 | I = s3 | I = s4 | I = s5 | I = s6 )
            & ( J = s1 | J = s2 | J = s3 | J = s4 | J = s5 | J = s6 )
            & ( K = s1 | K = s2 | K = s3 | K = s4 | K = s5 | K = s6 )
            & I != J & J != K & I != K
            & member(I,E) & member(J,E) & member(K,E) ) ) ) ).
