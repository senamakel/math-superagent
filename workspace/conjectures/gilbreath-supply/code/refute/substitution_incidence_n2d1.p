% REFUTATION of the LIVE proposed claim substitution-incidence-perron:
%   T(2n, 2d) == T(n, d)   (one of the four claimed substitution rules,
%                           for any {0,1} string h)
%
% Instance n=2, d=1:
%   T(4,2) = XOR_{o subseteq 2} h[4-1-2+o] : submasks of 2 are {0,2}
%          = h[1] xor h[3]
%   T(2,1) = XOR_{o subseteq 1} h[2-1-1+o] : submasks of 1 are {0,1}
%          = h[0] xor h[1]
% Claim  T(4,2) == T(2,1)  <=>  h1^h3 == h0^h1  <=>  h3 == h0,  false for
% general h.  h = 0001 gives T(4,2)=1, T(2,1)=0.
%
% h0..h3 free; define the cells; assert the claim as conjecture.

fof(def_T42, axiom, ( T42 <=> ~( h1 <=> h3 ) )).
fof(def_T21, axiom, ( T21 <=> ~( h0 <=> h1 ) )).
fof(goal, conjecture, ( T42 <=> T21 )).
