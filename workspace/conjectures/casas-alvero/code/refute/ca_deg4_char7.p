% Refutation: CA in degree 4 over F_7 is FALSE (p=7 is a bad prime for n=4,
% in the Hasse formulation).  The refute folder already holds deg4 char3 and
% char5; this closes the third and last published bad prime for n=4
% ({3,5,7}, Castryck et al. 2012 Thm 4; also the run's verified
% badprimes-n4-minor-criterion: lcm_T J_T = 1575 = 3^2.5^2.7, so 7 | J_T).
%
% Witness: f = x^4 + x^3 + 4x over F_7.  THREE distinct roots {0,4,5}, so it
% is NOT a pure power (a pure power (x-a)^4 has a single root).  It shares a
% root with every Hasse derivative H_1, H_2, H_3:
%   H_1 = 4x^3+3x^2+4  : H_1(4)=4*64+3*16+4=308=44*7=0 mod 7; f(4)=256+64+
%                          16=336=48*7=0 mod 7  -> common root 4
%   H_2 = 6x^2+3x      : H_2(0)=0; f(0)=0  -> common root 0
%   H_3 = 4x+1         : H_3(5)=21=0; f(5)=625+125+20=770=110*7=0 -> common root 5
%
% Values on F_7 = {c0=0..c6=6}:
%   f   = x^4+x^3+4x  : f(0..6)=[0,6,4,1,0,0,3]
%   H_1 = 4x^3+3x^2+4 : [4,4,6,6,0,5,3]
%   H_2 = 6x^2+3x     : [0,2,2,0,3,4,3]
%   H_3 = 4x+1        : [1,5,2,6,3,0,4]
%
% Conclusion (CA degree 4): f is a pure power (x-a)^4 for some a in F_7.  The
% seven pure-power value tables (shown in the goal) never equal f's table, so
% f is not a pure power.  => counterexample over F_7 to "CA holds in degree 4".

% distinctness of all 28 unordered pairs, via pairwise axioms
fof(d1, axiom, c0 != c1). fof(d2, axiom, c0 != c2). fof(d3, axiom, c0 != c3).
fof(d4, axiom, c0 != c4). fof(d5, axiom, c0 != c5). fof(d6, axiom, c0 != c6).
fof(d7, axiom, c1 != c2). fof(d8, axiom, c1 != c3). fof(d9, axiom, c1 != c4).
fof(d10, axiom, c1 != c5). fof(d11, axiom, c1 != c6). fof(d12, axiom, c2 != c3).
fof(d13, axiom, c2 != c4). fof(d14, axiom, c2 != c5). fof(d15, axiom, c2 != c6).
fof(d16, axiom, c3 != c4). fof(d17, axiom, c3 != c5). fof(d18, axiom, c3 != c6).
fof(d19, axiom, c4 != c5). fof(d20, axiom, c4 != c6). fof(d21, axiom, c5 != c6).

% f = x^4 + x^3 + 4x  values on F_7: [0,6,4,1,0,0,3]
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c6).
fof(f2, axiom, f(c2) = c4).
fof(f3, axiom, f(c3) = c1).
fof(f4, axiom, f(c4) = c0).
fof(f5, axiom, f(c5) = c0).
fof(f6, axiom, f(c6) = c3).

% Hasse H_1 = 4x^3+3x^2+4 : [4,4,6,6,0,5,3]
fof(h10, axiom, h1(c0) = c4). fof(h11, axiom, h1(c1) = c4).
fof(h12, axiom, h1(c2) = c6). fof(h13, axiom, h1(c3) = c6).
fof(h14, axiom, h1(c4) = c0). fof(h15, axiom, h1(c5) = c5).
fof(h16, axiom, h1(c6) = c3).

% Hasse H_2 = 6x^2+3x : [0,2,2,0,3,4,3]
fof(h20, axiom, h2(c0) = c0). fof(h21, axiom, h2(c1) = c2).
fof(h22, axiom, h2(c2) = c2). fof(h23, axiom, h2(c3) = c0).
fof(h24, axiom, h2(c4) = c3). fof(h25, axiom, h2(c5) = c4).
fof(h26, axiom, h2(c6) = c3).

% Hasse H_3 = 4x+1 : [1,5,2,6,3,0,4]
fof(h30, axiom, h3(c0) = c1). fof(h31, axiom, h3(c1) = c5).
fof(h32, axiom, h3(c2) = c2). fof(h33, axiom, h3(c3) = c6).
fof(h34, axiom, h3(c4) = c3). fof(h35, axiom, h3(c5) = c0).
fof(h36, axiom, h3(c6) = c4).

% HYPOTHESIS: f shares a root with each Hasse derivative H_1, H_2, H_3
fof(hyp1, axiom, ?[X] : (f(X) = c0 & h1(X) = c0)).   % common root 4
fof(hyp2, axiom, ?[X] : (f(X) = c0 & h2(X) = c0)).   % common root 0
fof(hyp3, axiom, ?[X] : (f(X) = c0 & h3(X) = c0)).   % common root 5

% CONCLUSION (CA degree 4): f is a pure power (x-a)^4 for some a in F_7.
% Pure-power value tables, indexed c0..c6:
%   a=0: [0,1,2,4,4,2,1]   a=1: [1,0,1,2,4,4,2]   a=2: [2,1,0,1,2,4,4]
%   a=3: [4,2,1,0,1,2,4]   a=4: [4,4,2,1,0,1,2]   a=5: [2,4,4,2,1,0,1]
%   a=6: [1,2,4,4,2,1,0]
fof(goal, conjecture,
      (f(c0)=c0 & f(c1)=c1 & f(c2)=c2 & f(c3)=c4 & f(c4)=c4 & f(c5)=c2 & f(c6)=c1)
    | (f(c0)=c1 & f(c1)=c0 & f(c2)=c1 & f(c3)=c2 & f(c4)=c4 & f(c5)=c4 & f(c6)=c2)
    | (f(c0)=c2 & f(c1)=c1 & f(c2)=c0 & f(c3)=c1 & f(c4)=c2 & f(c5)=c4 & f(c6)=c4)
    | (f(c0)=c4 & f(c1)=c2 & f(c2)=c1 & f(c3)=c0 & f(c4)=c1 & f(c5)=c2 & f(c6)=c4)
    | (f(c0)=c4 & f(c1)=c4 & f(c2)=c2 & f(c3)=c1 & f(c4)=c0 & f(c5)=c1 & f(c6)=c2)
    | (f(c0)=c2 & f(c1)=c4 & f(c2)=c4 & f(c3)=c2 & f(c4)=c1 & f(c5)=c0 & f(c6)=c1)
    | (f(c0)=c1 & f(c1)=c2 & f(c2)=c4 & f(c3)=c4 & f(c4)=c2 & f(c5)=c1 & f(c6)=c0)
).
