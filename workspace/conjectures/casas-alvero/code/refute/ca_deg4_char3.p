% Refutation: CA in degree 4 over F_3 is FALSE (p=3 is a bad prime for n=4,
% in the Hasse formulation, matching the published lists {3,5,7}).
%
% Witness: f = x^4 + x over F_3.  This is x(x+1)^3, TWO distinct roots,
% so it is NOT a pure power.  Yet it shares a root with every Hasse
% derivative H_1, H_2, H_3:
%   H_1 = x^3 + 1,  H_2 = 0 (identically),  H_3 = x
%   f = x(x^3+1) = x*H_1, so f shares its roots with H_1; f and H_3 share
%   root 0; H_2 = 0 shares everything.
%
% Values on F_3 = {c0=0, c1=1, c2=2}:
%   f  = x^4+x     : f(0)=0, f(1)=2, f(2)=0     ->  (c0, c2, c0)
%   H1 = x^3+1     : H1(0)=1, H1(1)=2, H1(2)=0  ->  (c1, c2, c0)
%   H2 = 0         : (c0, c0, c0)
%   H3 = x         : (c0, c1, c2)
% Hypothesis: common root with H_1 (X=2), with H_2 (any), with H_3 (X=0).
% Conclusion (CA for degree 4): f is a pure power, i.e. equals one of
%   g0 = x^4        = (c0, c1, c1)
%   g1 = (x-1)^4    = (c1, c0, c1)
%   g2 = (x-2)^4    = (c1, c1, c0)
% f = (c0, c2, c0) is none of these (the c1-entry is 2, never 0 or 1).
% => counterexample over F_3 to "CA holds in degree 4".

fof(neq, axiom, c0 != c1).
fof(neq2, axiom, c0 != c2).
fof(neq3, axiom, c1 != c2).

% f = x^4 + x values on F_3
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c2).
fof(f2, axiom, f(c2) = c0).

% Hasse H_1 = x^3 + 1
fof(h10, axiom, h1(c0) = c1).
fof(h11, axiom, h1(c1) = c2).
fof(h12, axiom, h1(c2) = c0).

% Hasse H_2 = 0 (identically)
fof(h20, axiom, h2(c0) = c0).
fof(h21, axiom, h2(c1) = c0).
fof(h22, axiom, h2(c2) = c0).

% Hasse H_3 = x
fof(h30, axiom, h3(c0) = c0).
fof(h31, axiom, h3(c1) = c1).
fof(h32, axiom, h3(c2) = c2).

% HYPOTHESIS: f shares a root with each Hasse derivative H_1, H_2, H_3
fof(hyp1, axiom, ?[X] : (f(X) = c0 & h1(X) = c0)).   % common root with H_1: X=2
fof(hyp2, axiom, ?[X] : (f(X) = c0)).               % H_2 = 0, any root of f works
fof(hyp3, axiom, ?[X] : (f(X) = c0 & h3(X) = c0)).   % common root with H_3: X=0

% CONCLUSION (CA degree 4): f is a pure power of degree 4
fof(goal, conjecture,
    (f(c0) = c0 & f(c1) = c1 & f(c2) = c1)   % x^4
    | (f(c0) = c1 & f(c1) = c0 & f(c2) = c1) % (x-1)^4
    | (f(c0) = c1 & f(c1) = c1 & f(c2) = c0) % (x-2)^4
).
