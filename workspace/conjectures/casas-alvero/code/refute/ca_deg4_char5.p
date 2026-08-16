% Refutation: CA in degree 4 over F_5 is FALSE (p=5 is a bad prime for n=4,
% in the Hasse formulation, matching the published lists {3,5,7} and the
% run's claim badprimes-n4-minor-criterion-verified: lcm_T J_T = 1575 = 3^2.5^2.7).
%
% Witness: f = x^4 - x^2 over F_5 = x^2 (x-1)(x+1), THREE distinct roots
% {0, 1, 4}, so it is NOT a pure power.  It shares a root with every Hasse
% derivative H_1, H_2, H_3:
%   H_1 = x(4x^2 + 3)   : root 0, and f(0) = 0  -> common root 0
%   H_2 = x^2 + 4       : roots 1,4; f(1)=0, f(4)=0 -> common root 1
%   H_3 = 4x            : root 0, and f(0) = 0  -> common root 0
% (none of which are vacuous: no H_i is identically 0.)
%
% Values on F_5 = {c0=0, c1=1, c2=2, c3=3, c4=4}:
%   f   = x^4 - x^2 : f(0)=0, f(1)=0, f(2)=2, f(3)=2, f(4)=0  -> (c0,c0,c2,c2,c0)
%   H_1 = x(4x^2+3) : H1(0)=0, H1(1)=2, H1(2)=3, H1(3)=2, H1(4)=3 -> (c0,c2,c3,c2,c3)
%   H_2 = x^2 + 4   : H2(0)=4, H2(1)=0, H2(2)=3, H2(3)=3, H2(4)=0 -> (c4,c0,c3,c3,c0)
%   H_3 = 4x        : H3(0)=0, H3(1)=4, H3(2)=3, H3(3)=2, H3(4)=1 -> (c0,c4,c3,c2,c1)
%
% Conclusion (CA degree 4): f is a pure power of degree 4.  Over F_5 the pure
% powers (x-a)^4 are exactly the vectors that are 0 at a and 1 elsewhere
% (Fermat: t^4 = 1 for t nonzero mod 5):
%   a=0: (c0,c1,c1,c1,c1)   a=1: (c1,c0,c1,c1,c1)   a=2: (c1,c1,c0,c1,c1)
%   a=3: (c1,c1,c1,c0,c1)   a=4: (c1,c1,c1,c1,c0)
% f = (c0,c0,c2,c2,c0) is none of these (values 2 occur, pure powers never take
% value 2).  => counterexample over F_5 to "CA holds in degree 4".
%
% This confirms p=5 is a bad prime for degree 4 at a NEW prime for the refute
% folder (which previously held only the p=3 witness for n=4), corroborating
% the published {3,5,7} list and the reformulation's prediction 5 | J_T.

fof(neq1, axiom, c0 != c1).
fof(neq2, axiom, c0 != c2).
fof(neq3, axiom, c0 != c3).
fof(neq4, axiom, c0 != c4).
fof(neq5, axiom, c1 != c2).
fof(neq6, axiom, c1 != c3).
fof(neq7, axiom, c1 != c4).
fof(neq8, axiom, c2 != c3).
fof(neq9, axiom, c2 != c4).
fof(neq10, axiom, c3 != c4).

% f = x^4 - x^2 values on F_5
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c0).
fof(f2, axiom, f(c2) = c2).
fof(f3, axiom, f(c3) = c2).
fof(f4, axiom, f(c4) = c0).

% Hasse H_1 = x(4x^2 + 3)
fof(h10, axiom, h1(c0) = c0).
fof(h11, axiom, h1(c1) = c2).
fof(h12, axiom, h1(c2) = c3).
fof(h13, axiom, h1(c3) = c2).
fof(h14, axiom, h1(c4) = c3).

% Hasse H_2 = x^2 + 4
fof(h20, axiom, h2(c0) = c4).
fof(h21, axiom, h2(c1) = c0).
fof(h22, axiom, h2(c2) = c3).
fof(h23, axiom, h2(c3) = c3).
fof(h24, axiom, h2(c4) = c0).

% Hasse H_3 = 4x
fof(h30, axiom, h3(c0) = c0).
fof(h31, axiom, h3(c1) = c4).
fof(h32, axiom, h3(c2) = c3).
fof(h33, axiom, h3(c3) = c2).
fof(h34, axiom, h3(c4) = c1).

% HYPOTHESIS: f shares a root with each Hasse derivative H_1, H_2, H_3
fof(hyp1, axiom, ?[X] : (f(X) = c0 & h1(X) = c0)).   % common root with H_1: X=0
fof(hyp2, axiom, ?[X] : (f(X) = c0 & h2(X) = c0)).   % common root with H_2: X=1 (or 4)
fof(hyp3, axiom, ?[X] : (f(X) = c0 & h3(X) = c0)).   % common root with H_3: X=0

% CONCLUSION (CA degree 4): f is a pure power of degree 4 over F_5
fof(goal, conjecture,
      (f(c0) = c0 & f(c1) = c1 & f(c2) = c1 & f(c3) = c1 & f(c4) = c1)  % x^4
    | (f(c0) = c1 & f(c1) = c0 & f(c2) = c1 & f(c3) = c1 & f(c4) = c1)  % (x-1)^4
    | (f(c0) = c1 & f(c1) = c1 & f(c2) = c0 & f(c3) = c1 & f(c4) = c1)  % (x-2)^4
    | (f(c0) = c1 & f(c1) = c1 & f(c2) = c1 & f(c3) = c0 & f(c4) = c1)  % (x-3)^4
    | (f(c0) = c1 & f(c1) = c1 & f(c2) = c1 & f(c3) = c1 & f(c4) = c0)  % (x-4)^4
).
