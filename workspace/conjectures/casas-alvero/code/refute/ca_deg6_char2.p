% Refutation: CA in degree 6 over F_2 is FALSE (p=2 is a bad prime for n=6,
% in the Hasse formulation — p=2 is the FIRST entry of the published
% degree-6 bad-prime list, Castryck-Laterveer-Ounaies 2012 Table 1, which
% begins 2, 5, 7, 11, 13, 19, ...).
%
% Witness: f = x^6 + x^2 over F_2.  This is x^2(x^4+1) = x^2(x+1)^4, TWO
% distinct roots {0 (mult 2), 1 (mult 4)}, so NOT a pure power.  Yet it
% shares a root with every Hasse derivative H_1..H_5:
%   H_1 = 0 (identically: C(6,1)=6 and C(2,1)=2 vanish mod 2)   -> vacuous
%   H_2 = x^4 + 1, and x^4+1 divides f                            -> common root (any root of x^4+1)
%   H_3 = 0 (C(6,3)=20 vanishes mod 2)                           -> vacuous
%   H_4 = x^2, common root 0 with f                               -> common root 0
%   H_5 = 0 (C(6,5)=6 vanishes mod 2)                            -> vacuous
%
% This is the same algebraic shape as the canonical char-p family
% (x^{p+1} - x^p = x^2(x^p - 1), here at p=2 realized as x^2(x+1)^4 since
% x^4+1 = (x+1)^4 in char 2): the middle Hasse derivatives H_1,H_3,H_5
% vanish identically, removing the constraints that would collapse the two
% distinct roots in char 0.
%
% Values on F_2 = {c0=0, c1=1}:
%   f  = x^6+x^2     : f(0)=0, f(1)=0   ->  (c0, c0)
%   H_1 = 0          : (c0, c0)
%   H_2 = x^4+1      : H2(0)=1, H2(1)=0 ->  (c1, c0)
%   H_3 = 0          : (c0, c0)
%   H_4 = x^2        : H4(0)=0, H4(1)=1 ->  (c0, c1)
%   H_5 = 0          : (c0, c0)
%
% Hypothesis (CA for this f): shares a root with H_1 (any root of f, since
% H_1=0), with H_2 (X=1: f(1)=0, H2(1)=0), with H_3 (H_3=0, X=0), with H_4
% (X=0: f(0)=0, H4(0)=0), with H_5 (H_5=0, X=0).
% Conclusion (CA degree 6): f is a pure power of degree 6, i.e. one of
%   g0 = x^6            : (c0, c1)
%   g1 = (x+1)^6 = x^6+x^4+x^2+1 : (c1, c0)
% f = (c0, c0) is neither  =>  counterexample over F_2.

fof(neq, axiom, c0 != c1).

% f = x^6 + x^2
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c0).

% Hasse H_1 = 0
fof(h10, axiom, h1(c0) = c0).
fof(h11, axiom, h1(c1) = c0).

% Hasse H_2 = x^4 + 1
fof(h20, axiom, h2(c0) = c1).
fof(h21, axiom, h2(c1) = c0).

% Hasse H_3 = 0
fof(h30, axiom, h3(c0) = c0).
fof(h31, axiom, h3(c1) = c0).

% Hasse H_4 = x^2
fof(h40, axiom, h4(c0) = c0).
fof(h41, axiom, h4(c1) = c1).

% Hasse H_5 = 0
fof(h50, axiom, h5(c0) = c0).
fof(h51, axiom, h5(c1) = c0).

% HYPOTHESIS: f shares a root with each Hasse derivative H_1..H_5
fof(hyp1, axiom, ?[X] : (f(X) = c0 & h1(X) = c0)).   % H_1=0, X=0 works
fof(hyp2, axiom, ?[X] : (f(X) = c0 & h2(X) = c0)).   % common root with H_2: X=1
fof(hyp3, axiom, ?[X] : (f(X) = c0 & h3(X) = c0)).   % H_3=0, X=0 works
fof(hyp4, axiom, ?[X] : (f(X) = c0 & h4(X) = c0)).   % common root with H_4: X=0
fof(hyp5, axiom, ?[X] : (f(X) = c0 & h5(X) = c0)).   % H_5=0, X=0 works

% CONCLUSION (CA degree 6): f is a pure power of degree 6 over F_2
%   g0 = x^6              -> (c0, c1)
%   g1 = (x+1)^6 = x^6+x^4+x^2+1 -> (c1, c0)
fof(goal, conjecture,
    (f(c0) = c0 & f(c1) = c1)   % x^6
    | (f(c0) = c1 & f(c1) = c0) % (x+1)^6
).
