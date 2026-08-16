% ATTACK: the claim in meet-join-parseval-self-duality.md (status: grounded)
%   "E_p[S^2] = F_n(1-2p) = O(n), uniformly in p in (0,1)".
%
% Falsifier mechanism: at p -> 0+, h is mostly 0, so every fold cell T(n,d)=0
% (all zeros XOR to 0), every eps_d = (-1)^T = +1, hence S(n) = n-2 and
% E[S^2] = (n-2)^2 = Theta(n^2), NOT O(n).
%
% Concrete witness at n=6 (rows d=2,3,4,5), h = (0,0,0,0,0,0) all zero.
%   T(6,d) = XOR over o submask of d of h[5-d+o] = 0 for every d.
% In TPTP, a <=> b is XNOR (equality), and ~(a <=> b) is XOR.
%
% T cells (XOR over submasks o of h[5-d+o]):
%   d=2 (10): submasks {0,2} -> h[3] xor h[5]
%   d=3 (11): submasks {0,1,2,3} -> h[2]^h[3]^h[4]^h[5]
%   d=4 (100): submasks {0,4} -> h[1] xor h[5]
%   d=5 (101): submasks {0,1,4,5} -> h[0]^h[1]^h[4]^h[5]
fof(witness_allzero, axiom, ( ~h0 & ~h1 & ~h2 & ~h3 & ~h4 & ~h5 )).
fof(t2, axiom, ( t2 <=> ~( h5 <=> h3 ) )).      % h3 xor h5 = 0 -> t2 FALSE
fof(t3, axiom, ( t3 <=> ~( h5 <=> h4 <=> h3 <=> h2 ) ) ).
fof(t4, axiom, ( t4 <=> ~( h5 <=> h1 ) )).
fof(t5, axiom, ( t5 <=> ~( h5 <=> h4 <=> h1 <=> h0 ) )).
fof(eps2, axiom, ( eps2 <=> ~t2 )).   % eps_d = +1 iff T=0
fof(eps3, axiom, ( eps3 <=> ~t3 )).
fof(eps4, axiom, ( eps4 <=> ~t4 )).
fof(eps5, axiom, ( eps5 <=> ~t5 )).
% With all-zero h, every T=0, every eps=+1, so S = 4 = n-2; S^2 = 16.
% Conjecture: every eps is +1 (the near-constant collapse giving S = n-2).
fof(goal, conjecture, ( eps2 & eps3 & eps4 & eps5 )).
