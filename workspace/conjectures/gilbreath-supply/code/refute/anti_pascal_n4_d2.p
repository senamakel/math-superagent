% Anti-Pascal relation (L4) of the ADOPTED derivative-ladder approach:
%   T(n+1,d) = T(n,d) ^ T(n+1,d+1)
% claimed as a universal F2 identity over all {0,1} strings h.
% Concrete instance used to kill the Abel boundary route: n=4, d=2.
%   T(4,2) = h1 ^ h3          (submasks of 2 = {0,2}, indices 1,3)
%   T(3,2) = h0 ^ h2          (n=3,d=2: indices 3-1-2+o = 0,2)
%   T(4,3) = h0^h1^h2^h3      (submasks of 3 = {0,1,2,3}, indices 0,1,2,3)
% Conjecture: T(4,2) <=> T(3,2) XOR T(4,3), i.e. the anti-Pascal identity.
% h0..h3 are free; if the identity is universal no model falsifies it.
% Conjecture = antiP := (t42 <=> ~(t32 <=> t43)).
fof(def_t42, axiom, ( t42 <=> ( (h1 & ~h3) | (~h1 & h3) ) )).
fof(def_t32, axiom, ( t32 <=> ( (h0 & ~h2) | (~h0 & h2) ) )).
fof(def_t43, axiom,
    ( t43 <=> ( (h0 & h1 & h2 & ~h3) | (h0 & h1 & ~h2 & h3)
              | (h0 & ~h1 & h2 & h3) | (~h0 & h1 & h2 & h3)
              | (~h0 & ~h1 & ~h2 & h3) | (~h0 & ~h1 & h2 & ~h3)
              | (~h0 & h1 & ~h2 & ~h3) | (h0 & ~h1 & ~h2 & ~h3) ) )).
fof(antiPascal_identity, conjecture,
    ( t42 <=> ~( t32 <=> t43 ) )).
