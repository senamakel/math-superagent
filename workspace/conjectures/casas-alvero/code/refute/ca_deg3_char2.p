% Refutation: CA in degree 3 over F_2 is FALSE (the char-p falsification).
% Witness: f = x^3+x^2 over F_2, the canonical x^{p+1}-x^p family at p=2.
%
% Build the hypothesis and conclusion directly as first-order statements over
% a 2-element domain {c0,c1} with distinct constants.  No arithmetic tables.
%
% Over F_2 with f = x^3+x^2:
%   f(c0)=c0 (0), f(c1)=c0 (0)     [f vanishes at both 0 and 1]
%   f'(c0)=c0 (0), f'(c1)=c1 (1)   [f' = x^2]
% Hypothesis: f shares a root with f' and with f''.
%   common root with f': c0      common root with f'': c0
% Pure powers of degree 3 over F_2:
%   g0 = (x-0)^3 = x^3        : g0(c0)=c0, g0(c1)=c1
%   g1 = (x-1)^3 = x^3+x^2+x+1: g1(c0)=c1, g1(c1)=c0
% Conclusion (CA for this f): f equals g0 or g1.
% Model: f=(c0,c0) satisfies hypothesis, equals neither g0=(c0,c1) nor
% g1=(c1,c0)  =>  counterexample.

fof(neq, axiom, c0 != c1).

% f, fp data
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c0).
fof(fp0, axiom, fp(c0) = c0).
fof(fp1, axiom, fp(c1) = c1).

% HYPOTHESIS: exists a root common to f and f'; exists a root common to f and f''
fof(h1, axiom, ?[X] : (f(X) = c0 & fp(X) = c0)).
fof(h2, axiom, ?[X] : (f(X) = c0)).   % f'' vanishes identically mod 2, so any root of f works

% CONCLUSION (CA): f is a pure power of degree 3
fof(goal, conjecture,
    (f(c0) = c0 & f(c1) = c1) | (f(c0) = c1 & f(c1) = c0)).
