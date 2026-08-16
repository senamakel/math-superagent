% REFUTATION of the LIVE proposed claim abel-boundary-recurrence:
%   T(n,d) == T(n-1,d)  XOR  T(n-1,d-1)   (claimed for any {0,1} string h)
%
% Concrete instance n=4, d=2.  Fold cell T(n,d) = XOR_{o subseteq d} h[n-1-d+o].
%   T(4,2) = submasks of 2 = {0,2} -> h[1] xor h[3]
%   T(3,2) = submasks of 2 -> h[0] xor h[2]
%   T(3,1) = submasks of 1 = {0,1} -> h[1] xor h[2]
% so  RHS = T(3,2) xor T(3,1) = h[0] xor h[1].
% The claimed identity  T(4,2) == T(3,2) xor T(3,1)  is
%   h[1] xor h[3]  ==  h[0] xor h[1]  <=>  h[3] == h[0],  NOT true for all h.
%
% We make h0,h1,h2,h3 FREE, define the three T cells by their definitions,
% and assert the claimed identity as the CONJECTURE.  A model with h3 != h0
% (e.g. h = 0001) satisfies the axioms and falsifies the conjecture.
% TPTP uses ~(A <=> B) for A xor B.

fof(def_T42, axiom, ( T42 <=> ~( h1 <=> h3 ) )).   % h1 xor h3
fof(def_T32, axiom, ( T32 <=> ~( h0 <=> h2 ) )).   % h0 xor h2
fof(def_T31, axiom, ( T31 <=> ~( h1 <=> h2 ) )).   % h1 xor h2
fof(def_rhs, axiom, ( rhs <=> ~( T32 <=> T31 ) )). % T32 xor T31
% abel-boundary-recurrence claim at this (n,d):
fof(goal, conjecture, ( T42 <=> rhs )).
