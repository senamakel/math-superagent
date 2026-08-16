% n=5, rows d=2,3,4.  For R-random-pointwise: wt(Phi_5 h) >= 5/4 = 1.25
% i.e. >= 2.  We encode the claim "every h has wt >= 2" as the conjecture and
% let find_counterexample try to falsify it: a model (h) with wt <= 1 is the
% small-n "failure" the run's own note reports (P(wt<n/4) = constant > 0).
%
% Fold cells (d in [2, n-1], T(n,d) = XOR over submasks o of d of h[n-1-d+o]):
%   d=2 (10): submasks {0,2} -> cols {2,4} : T2 = h2 xor h4
%   d=3 (11): submasks {0,1,2,3} -> cols {1,2,3,4} : T3 = h1^h2^h3^h4
%   d=4 (100): submasks {0,4} -> cols {0,4} : T4 = h0 xor h4

fof(h_free, axiom, $true).

fof(def_t2, axiom,
    ( t2 <=> ( (h2 & ~h4) | (~h2 & h4) ) )).
fof(def_t3, axiom,
    ( t3 <=> ( (h1 & h2 & h3 & ~h4) | (h1 & h2 & ~h3 & h4)
             | (h1 & ~h2 & h3 & h4) | (~h1 & h2 & h3 & h4)
             | (~h1 & ~h2 & ~h3 & h4) | (~h1 & ~h2 & h3 & ~h4)
             | (~h1 & h2 & ~h3 & ~h4) | (h1 & ~h2 & ~h3 & ~h4) ) )).
fof(def_t4, axiom,
    ( t4 <=> ( (h0 & ~h4) | (~h0 & h4) ) )).

% wt = t2 + t3 + t4.  Conjecture: wt >= 2 (holds for all h).
fof(goal, conjecture,
    ( (t2 & t3) | (t2 & t4) | (t3 & t4) )).
