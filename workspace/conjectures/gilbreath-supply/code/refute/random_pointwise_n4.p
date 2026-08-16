% n=4, rows d=2,3. R-random-pointwise threshold n/4 = 1, so "wt >= 1".
% Conjecture "every h has wt(Phi_4 h) >= 1" (too strong; run's note says
% P(wt<n/4)=1/4 at n=4).  Falsify with a wt=0 model.
%
% Fold cells:
%   d=2 (10): submasks {0,2} -> cols {1,3} : t2 = h1 xor h3
%   d=3 (11): submasks {0,1,2,3} -> cols {0,1,2,3} : t3 = h0^h1^h2^h3
% wt = t2 + t3.
fof(def_t2, axiom, ( t2 <=> ( (h1 & ~h3) | (~h1 & h3) ) )).
fof(def_t3, axiom, ( t3 <=> ( (h0 & h1 & h2 & ~h3) | (h0 & h1 & ~h2 & h3)
               | (h0 & ~h1 & h2 & h3) | (~h0 & h1 & h2 & h3)
               | (~h0 & ~h1 & ~h2 & h3) | (~h0 & ~h1 & h2 & ~h3)
               | (~h0 & h1 & ~h2 & ~h3) | (h0 & ~h1 & ~h2 & ~h3) ) )).
% Conjecture: wt >= 1.
fof(goal, conjecture, ( t2 | t3 )).
