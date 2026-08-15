% Refute the open lemma CB-dying-pair as stated.
%
% Lemma asserts, for the first failure row K, that the dying row K-1 satisfies
%   b_{K-1} = 1   AND   A_{K-1}(1) in {4,6,8,...}.
%
% Two facts from the run's own definitions:
%   (i)  b(r)=1 means the leading {0,2} block has length 1, i.e. the entry at
%        position 1 (the second entry) is in {0,2}:  b=1 -> in02(A(r,1)).
%   (ii) "dying" means A_{K-1}(1) NOT in {0,2}: this is exactly what makes
%        A_K(0)=|1-A_{K-1}(1)| != 1, i.e. K is the first failure row.
%
% Claim: no dying row (one whose second entry is outside {0,2}) can have
% block length 1.  We encode the real construct and ask the engine to find a
% model satisfying the axioms while falsifying "b(K-1)=1" (the lemma's
% assertion).  A model exists -- the dying row K-1 has b=0 -- so the lemma's
% b_{K-1}=1 is refutable.

tff(dom, type, nr: $i).
tff(dom2, type, elt: $tType).
tff(decl_in02, type, in02: elt > $o).
tff(decl_a, type, a: nr > elt).      % a(r) = A(r,1) = second entry of row r
tff(decl_bone, type, bone: nr > $o). % bone(r) = (block length of r is 1)
tff(decl_d, type, d: nr).            % d = K-1, the dying row
tff(decl_z, type, z: elt).           % 0
tff(decl_t, type, t: elt).           % 2 in {0,2}
tff(decl_f, type, f: elt).           % 4 (representative of {4,6,8,..})

% (i) definition: block length 1 at r requires second entry in {0,2}
tff(def_b1, axiom, ![R:nr]: ( bone(R) => in02(a(R)) )).

% (ii) dying: the dying row's second entry is NOT in {0,2}
tff(dying, axiom, ~ in02(a(d)) ).

% values: a(d) is one of the even numbers {0,2,4,6}
tff(dom_a, axiom, a(d)=z | a(d)=t | a(d)=f ).
tff(in02_z, axiom, in02(z)).
tff(in02_t, axiom, in02(t)).
tff(nin02_f, axiom, ~ in02(f)).
tff(z_ne_t, axiom, z != t).
tff(z_ne_f, axiom, z != f).
tff(t_ne_f, axiom, t != f).

% THE LEMMA'S ASSERTION UNDER ATTACK: the dying row has block length 1.
tff(dying_pair_claim, conjecture, bone(d)).
