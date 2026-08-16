% Refutation: the root-difference-coloring adopted approach's COLLAPSE step
% ("the n-1 Hasse-derivative colorings force all roots to coincide -> pure
% power") is FALSE in characteristic 5, at degree 6 -- the first degree the
% refute folder has never exercised.  This is exactly the char-p break the
% approach itself predicts: for n = p+1, the Hasse derivatives H_2, H_3, H_4
% all vanish IDENTICALLY over F_5 (i >= p degenerates the binomial
% coefficients mod p), so those colors impose no constraint, and the two
% roots 0, 1 never get forced together.
%
% Witness: f(x) = x^6 - x^5 = x^5 (x - 1) over F_5.  TWO distinct roots
% {0, 1} (0 with multiplicity 5, 1 with multiplicity 1) -> NOT a pure power.
% Hasse derivatives over F_5 (H_i = sum_j C(j,i) c_j x^{j-i}, c_6=1, c_5=-1):
%   H_1 = 6x^5 - 5x^4 = x^5      : gcd(f, H_1) = gcd(x^5(x-1), x^5) = x^5
%   H_2 = binom(6,2)x^4 - binom(5,2)x^3 = 15x^4 - 10x^3 = 0   (degens to 0)
%   H_3 = binom(6,3)x^3 - binom(5,3)x^2 = 20x^3 - 10x^2 = 0   (degens to 0)
%   H_4 = binom(6,4)x^2 - binom(5,4)x   = 15x^2 - 5x     = 0   (degens to 0)
%   H_5 = binom(6,5)x - binom(5,5)      = 6x - 1          = x - 1
%                                 : gcd(f, H_5) = gcd(x^5(x-1), x-1) = x-1
% Hypothesis (CA for degree 6): f shares a root with each H_i, i=1..5.
%   i=1: X=0 (f(0)=0, H_1(0)=0).   i=2,3,4: H_i = 0 vacuous (gcd(f,0)=f).
%   i=5: X=1 (f(1)=0, H_5(1)=0).
% Conclusion (CA degree 6): f is a pure power (x-a)^6.  A pure power has a
% SINGLE zero.  f=(0,0,2,1,2) has TWO zeros (at 0 and 1) -> not a pure power.
%
% Values on F_5 = {c0=0,c1=1,c2=2,c3=3,c4=4}:
%   f  : f(0)=0, f(1)=0, f(2)=2, f(3)=1, f(4)=2            -> (c0,c0,c2,c1,c2)
%   H_1 = x^5 (identity): (c0,c1,c2,c3,c4)
%   H_5 = x-1          : H5(0)=4, H5(1)=0, H5(2)=1, H5(3)=2, H5(4)=3
%                                                          -> (c4,c0,c1,c2,c3)
% (Hand-verified: f(2)=64-32=32=2, f(3)=729-243=486=1, f(4)=4096-1024=3072=2
%  mod 5; H1(3)=243=3, H1(4)=1024=4; H5 = x-1 values as listed.)

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

% f = x^6 - x^5 values on F_5
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c0).
fof(f2, axiom, f(c2) = c2).
fof(f3, axiom, f(c3) = c1).
fof(f4, axiom, f(c4) = c2).

% H_1 = x^5  (identity map on F_5)
fof(h10, axiom, h1(c0) = c0).
fof(h11, axiom, h1(c1) = c1).
fof(h12, axiom, h1(c2) = c2).
fof(h13, axiom, h1(c3) = c3).
fof(h14, axiom, h1(c4) = c4).

% H_5 = x - 1
fof(h50, axiom, h5(c0) = c4).
fof(h51, axiom, h5(c1) = c0).
fof(h52, axiom, h5(c2) = c1).
fof(h53, axiom, h5(c3) = c2).
fof(h54, axiom, h5(c4) = c3).

% HYPOTHESIS: f shares a root with H_1 and with H_5 (H_2, H_3, H_4 vanish
% identically mod 5, so the gcd condition gcd(f, H_i) = gcd(f, 0) = f is
% nonconstant automatically -- those colors are vacuous, which is precisely
% the per-color degeneracy the root-difference approach's char-p break states).
fof(hyp1, axiom, ?[X] : (f(X) = c0 & h1(X) = c0)).   % common root: X = 0
fof(hyp5, axiom, ?[X] : (f(X) = c0 & h5(X) = c0)).   % common root: X = 1

% CONCLUSION (CA degree 6): f is a pure power (x-a)^6 over F_5, i.e. has a
% single zero at exactly one a in {0,1,2,3,4} and is nonzero elsewhere.
fof(goal, conjecture,
      (f(c0)=c0 & f(c1)!=c0 & f(c2)!=c0 & f(c3)!=c0 & f(c4)!=c0)  % zero at 0
    | (f(c0)!=c0 & f(c1)=c0 & f(c2)!=c0 & f(c3)!=c0 & f(c4)!=c0)  % zero at 1
    | (f(c0)!=c0 & f(c1)!=c0 & f(c2)=c0 & f(c3)!=c0 & f(c4)!=c0)  % zero at 2
    | (f(c0)!=c0 & f(c1)!=c0 & f(c2)!=c0 & f(c3)=c0 & f(c4)!=c0)  % zero at 3
    | (f(c0)!=c0 & f(c1)!=c0 & f(c2)!=c0 & f(c3)!=c0 & f(c4)=c0)  % zero at 4
).
