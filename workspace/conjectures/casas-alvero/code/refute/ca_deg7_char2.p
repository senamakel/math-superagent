% Refutation: CA in degree 7 over F_2 is FALSE (p=2 is a bad prime for n=7).
%
% This is the first n=7 refutation in the refute set (which had reached only
% n=3,4,5,6) and an independent finite-model check of the published degree-7
% bad-prime claim (Castryck et al. 2012 Thm 4: for d=7 the smallest non-bad
% prime apart from 7 is 127, so every prime < 127 except 7 -- in particular
% p=2 -- is a bad prime for degree 7).  The n=6/n=7 bad-prime lists were
% previously taken only on source word (the J_T minors criterion is infeasible
% at n=6, and n=7 was never exercised by the refute set); this is the first
% independent finite-model confirmation of the degree-7 list.
%
% Witness: f(x) = x^7 + x^3 = x^3 (x+1)^4 over F_2.  TWO distinct roots
% {0, 1} (0 with multiplicity 3, 1 with multiplicity 4) -> NOT a pure power.
%
% Hasse derivatives over F_2 (H_i = sum_j C(j,i) c_j x^{j-i}; c7=1, c3=1):
%   H_1 = 7x^6 + 3x^2  = x^6 + x^2    : common root 0  (f(0)=0, H_1(0)=0)
%   H_2 = 21x^5 + 3x   = x^5 + x      : common root 0
%   H_3 = 35x^4 + 1    = x^4 + 1      : common root 1  (f(1)=0, H_3(1)=0)
%   H_4 = 35x^3        = x^3          : common root 0
%   H_5 = 21x^2        = x^2          : common root 0
%   H_6 = 7x           = x            : common root 0
% (binomial coefficients C(7,1)=7,C(3,1)=3,C(7,2)=21,C(7,3)=35 reduced mod 2;
%  H_3 picks up the j=3 term C(3,3)=1 constant, giving x^4+1.)
%
% Values on F_2 = {c0=0, c1=1}:
%   f    : f(0)=0, f(1)=0                       -> (c0, c0)
%   H_1  : 0, 1+1=0                             -> (c0, c0)
%   H_2  : 0, 1+1=0                             -> (c0, c0)
%   H_3  : 0+1=1, 1+1=0                         -> (c1, c0)
%   H_4  : 0, 1                                 -> (c0, c1)
%   H_5  : 0, 1                                 -> (c0, c1)
%   H_6  : 0, 1                                 -> (c0, c1)

fof(neq, axiom, c0 != c1).

% f = x^7 + x^3 values on F_2
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c0).

% Hasse H_1 = x^6 + x^2
fof(h10, axiom, h1(c0) = c0).
fof(h11, axiom, h1(c1) = c0).

% Hasse H_2 = x^5 + x
fof(h20, axiom, h2(c0) = c0).
fof(h21, axiom, h2(c1) = c0).

% Hasse H_3 = x^4 + 1
fof(h30, axiom, h3(c0) = c1).
fof(h31, axiom, h3(c1) = c0).

% Hasse H_4 = x^3
fof(h40, axiom, h4(c0) = c0).
fof(h41, axiom, h4(c1) = c1).

% Hasse H_5 = x^2
fof(h50, axiom, h5(c0) = c0).
fof(h51, axiom, h5(c1) = c1).

% Hasse H_6 = x
fof(h60, axiom, h6(c0) = c0).
fof(h61, axiom, h6(c1) = c1).

% HYPOTHESIS: f shares a root with each Hasse derivative H_1..H_6.
fof(hyp1, axiom, ?[X] : (f(X) = c0 & h1(X) = c0)).   % X = 0
fof(hyp2, axiom, ?[X] : (f(X) = c0 & h2(X) = c0)).   % X = 0
fof(hyp3, axiom, ?[X] : (f(X) = c0 & h3(X) = c0)).   % X = 1
fof(hyp4, axiom, ?[X] : (f(X) = c0 & h4(X) = c0)).   % X = 0
fof(hyp5, axiom, ?[X] : (f(X) = c0 & h5(X) = c0)).   % X = 0
fof(hyp6, axiom, ?[X] : (f(X) = c0 & h6(X) = c0)).   % X = 0

% CONCLUSION (CA degree 7): f is a pure power (x-a)^7 over F_2, i.e. has a
% single zero at exactly one a in {0,1} and is nonzero at the other.
fof(goal, conjecture,
      (f(c0) = c0 & f(c1) != c0)   % zero at 0 only
    | (f(c0) != c0 & f(c1) = c0)   % zero at 1 only
).
