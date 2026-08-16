% (L1) of the ADOPTED derivative-ladder approach (k=1, n=4, d=2):
%   T_{Delta h}(4,2) = T(5,3)  where (Delta h)[j] = h[j] ^ h[j+1].

% submasks of 2 = {0,2} -> indices n-1-d+o = 4-1-2+o = 1+o = {1,3}
%   T_{Delta h}(4,2) = (Delta h)[1] ^ (Delta h)[3]
%                   = (h1^h2) ^ (h3^h4)
% submasks of 3 = {0,1,2,3} -> indices 5-1-3+o = 1+o = {1,2,3,4}
%   T(5,3) = h1 ^ h2 ^ h3 ^ h4
% These are equal (associativity). Conjecture = the identity.
% h0..h4 free; universal identity iff no model falsifies.
fof(def_dh1, axiom, ( dh1 <=> ~(h1 <=> h2) )).
fof(def_dh3, axiom, ( dh3 <=> ~(h3 <=> h4) )).
fof(def_td42, axiom, ( td42 <=> ~(dh1 <=> dh3) )).
fof(def_t53, axiom,
    ( t53 <=> ( (h1 & h2 & h3 & ~h4) | (h1 & h2 & ~h3 & h4)
              | (h1 & ~h2 & h3 & h4) | (~h1 & h2 & h3 & h4)
              | (~h1 & ~h2 & ~h3 & h4) | (~h1 & ~h2 & h3 & ~h4)
              | (~h1 & h2 & ~h3 & ~h4) | (h1 & ~h2 & ~h3 & ~h4) ) )).
% Conjecture: T_{Delta h}(4,2) == T(5,3)
fof(L1_identity, conjecture, ( td42 <=> t53 )).
