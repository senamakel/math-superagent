% Refutation target: CB-dying-pair (skeleton counterexample-backward).
%
% Claim under attack (as the run needs it):
%   "At the first failure row K, the dying row K-1 satisfies b_{K-1} = 1,
%    A_{K-1}(0) = 1, and A_{K-1}(1) in {4,6,8,...}."
%
% We encode a REAL failing triangle: delete 7 from the primes,
% (2,3,5,11,13,17,19,23,...), a 2-then-odds sequence with a first-2 and a
% 6-gap (the Colonna class).  Hand-computed rows 0..3:
%
%   row0: 2  3  5 11 13 17 19 23
%   row1: 1  2  6  2  4  2  4  6
%   row2: 1  4  4  2  2  2  2  2
%   row3: 3  0  2  0  0  0
%
% The first row index K with A_K(0) != 1 is K = 3 (A_3(0) = 3).
% The "dying row" K-1 = 2 has A_2(1) = 4 (not in {0,2}), so its leading
% {0,2} block length is b_2 = 0.  The row with b = 1 is K-2 = 1.
%
% The conjecture asserted here is exactly the claim's b_{K-1} = 1 half:
% "the dying row K-1 has block length b = 1", i.e. A_{K-1}(1) in {0,2} and
% A_{K-1}(2) not in {0,2}.  find_counterexample is asked for a model of the
% axioms (the triangle, with first failure at K=3) that falsifies this.

% ---- triangle rows as axioms (function a(row,pos) = value) ----
fof(row0, axiom, a(0,0)=2 & a(0,1)=3 & a(0,2)=5 & a(0,3)=11 & a(0,4)=13 & a(0,5)=17 & a(0,6)=19 & a(0,7)=23).
fof(row1, axiom, a(1,0)=1 & a(1,1)=2 & a(1,2)=6 & a(1,3)=2 & a(1,4)=4 & a(1,5)=2 & a(1,6)=4 & a(1,7)=6).
fof(row2, axiom, a(2,0)=1 & a(2,1)=4 & a(2,2)=4 & a(2,3)=2 & a(2,4)=2 & a(2,5)=2 & a(2,6)=2 & a(2,7)=2).
fof(row3, axiom, a(3,0)=3 & a(3,1)=0 & a(3,2)=2 & a(3,3)=0 & a(3,4)=0 & a(3,5)=0).

% ---- first failure at K = 3: A_1(0)=1, A_2(0)=1, A_3(0) != 1 ----
fof(no_fail_1, axiom, a(1,0)=1).
fof(no_fail_2, axiom, a(2,0)=1).
fof(fail_at_3, axiom, a(3,0)!=1).

% ---- the claim's conclusion to attack: dying row K-1=2 has block length 1
% i.e. A_2(1) in {0,2} (b>=1) and A_2(2) not in {0,2} (block ends at pos 1)
fof(dying_pair_claim, conjecture, (a(2,1)=0 | a(2,1)=2) & ~(a(2,2)=0 | a(2,2)=2)).
