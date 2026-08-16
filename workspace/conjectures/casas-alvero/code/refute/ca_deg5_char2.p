% Refutation: CA in degree 5 over F_2 is FALSE (p=2 is a bad prime for n=5,
% in the Hasse formulation, matching the run's verified degree-5 bad-prime
% list {2,3,7,11,131,193,599,3541,8009} -- Castryck et al. 2012 Thm 4).
%
% The refuter's TPTP set has reached degree 3, 4 and 6 but never degree 5.
% This closes that gap with a first n=5 refutation, by an independent
% semantic finite-model route (the run verified n=5 by rank-over-F_p and SNF
% at n=4, never by a finite-model search).
%
% Witness: f(x) = x^5 + x^4 = x^4 (x + 1) over F_2.  TWO distinct roots
% {0, 1} (0 with multiplicity 4, 1 with multiplicity 1) -> NOT a pure power.
% Hasse derivatives over F_2 (H_i = sum_j C(j,i) c_j x^{j-i}, c_5=1, c_4=1,
% c_3=c_2=c_1=c_0=0):
%   H_1 = 5x^4 + 4 c_4 x^3 + 3 c_3 x^2 + 2 c_2 x + c_1 = x^4
%                                 (5,4,3,2,1 mod 2 = 1,0,1,0,1)
%                                 : gcd(f, H_1) = gcd(x^4(x+1), x^4) = x^4
%   H_2 = binom(5,2)x^3 + binom(4,2)c4 x^2 + binom(3,2)c3 x + binom(2,2)c2
%       = 10x^3 + 6 c4 x^2 + 3 c3 x + c2 = 0  (10,6,3,1 mod 2 = 0,0,1,1; c3=c2=0)
%   H_3 = binom(5,3)x^2 + binom(4,3)c4 x + binom(3,3)c3 = 0 (c3=0)
%   H_4 = binom(5,4)x + binom(4,4)c4 = 5x + c4 = x + 1
%                                 : gcd(f, H_4) = gcd(x^4(x+1), x+1) = x+1
% Hypothesis (CA for degree 5): f shares a root with each H_i, i=1..4.
%   i=1: X=0 (f(0)=0, H_1(0)=0).   i=2: H_2=0 vacuous (gcd(f,0)=f).
%   i=3: H_3=0 vacuous.             i=4: X=1 (f(1)=0, H_4(1)=0).
% Conclusion (CA degree 5): f is a pure power (x-a)^5.  A pure power has a
% SINGLE zero.  f = (c0,c0) has zeros at BOTH 0 and 1 -> not a pure power.
%
% Values on F_2 = {c0=0, c1=1}:
%   f  : f(0)=0, f(1)=1+1=0        -> (c0, c0)
%   H_1 = x^4 : H1(0)=0, H1(1)=1   -> (c0, c1)
%   H_2 = 0   : (c0, c0)
%   H_3 = 0   : (c0, c0)
%   H_4 = x+1 : H4(0)=1, H4(1)=0   -> (c1, c0)

fof(neq, axiom, c0 != c1).

% f = x^5 + x^4 values on F_2
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c0).

% Hasse H_1 = x^4
fof(h10, axiom, h1(c0) = c0).
fof(h11, axiom, h1(c1) = c1).

% Hasse H_2 = 0 (identically)
fof(h20, axiom, h2(c0) = c0).
fof(h21, axiom, h2(c1) = c0).

% Hasse H_3 = 0 (identically)
fof(h30, axiom, h3(c0) = c0).
fof(h31, axiom, h3(c1) = c0).

% Hasse H_4 = x + 1
fof(h40, axiom, h4(c0) = c1).
fof(h41, axiom, h4(c1) = c0).

% HYPOTHESIS: f shares a root with each Hasse derivative H_1..H_4
fof(hyp1, axiom, ?[X] : (f(X) = c0 & h1(X) = c0)).   % common root with H_1: X=0
fof(hyp2, axiom, ?[X] : (f(X) = c0)).               % H_2 = 0, any root of f works
fof(hyp3, axiom, ?[X] : (f(X) = c0)).               % H_3 = 0, any root of f works
fof(hyp4, axiom, ?[X] : (f(X) = c0 & h4(X) = c0)).   % common root with H_4: X=1

% CONCLUSION (CA degree 5): f is a pure power (x-a)^5 over F_2, i.e. has a
% single zero at exactly one a in {0,1} and is nonzero at the other.
fof(goal, conjecture,
      (f(c0) = c0 & f(c1) != c0)   % zero at 0 only
    | (f(c0) != c0 & f(c1) = c0)   % zero at 1 only
).
