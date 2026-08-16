% CONFIRM that the skeleton's extra (-1)^{#runs(d)} sign is spurious.
%
% Instance: n=5, d=3, pos = n-1-d = 1.  down-set(3)={0,1,2,3} = one run [0,3],
% so #runs=1.  T(5,3) = h1^h2^h3^h4 = [r1 != r5] (telescoping).
%
%   correct formula:   (-1)^T = chi(r1)*chi(r5)            (no sign factor)
%   skeleton formula:  (-1)^T = (-1)^{#runs=1}*chi(r1)*chi(r5) = -chi(r1)*chi(r5)
%
% Encode with r_j in {1,3}, R_j := (r_j=3), chi(r_j) = -1 iff R_j.
% h[j] = [r[j+1]!=r[j]] = R[j+1] xor R[j].
% T = h1^h2^h3^h4 = R1 ^ R5 (telescope).
%   tpar := T (1 bit).  tpar = R1 xor R5.
%   correct_plus := (-1)^T = +1  iff  tpar = 0  iff  R1 == R5.
%   skeleton_plus := -chi(r1)chi(r5) = +1 iff chi(r1)chi(r5) = -1  iff R1 != R5.
% Conjecture (skeleton formula correct): correct_plus <=> skeleton_plus,
% i.e. (R1==R5) <=> (R1!=R5)  -- ALWAYS FALSE.
% A model (any R1,R5) falsifies it -> refuted confirms skeleton is wrong.

% free residue indicators
fof(free, axiom, $true).

% R1 xor R5: tpar
fof(def_tpar, axiom,
    ( tpar <=> ( (R1 & ~R5) | (~R1 & R5) ) )).

% correct_plus := (tpar = 0) := (R1 == R5)
fof(def_correct, axiom,
    ( correct_plus <=> ( (R1 & R5) | (~R1 & ~R5) ) )).

% skeleton_plus := (R1 != R5)
fof(def_skel, axiom,
    ( skeleton_plus <=> ( (R1 & ~R5) | (~R1 & R5) ) )).

% Conjecture: the skeleton formula is correct (never true).
fof(goal, conjecture,
    ( correct_plus <=> skeleton_plus )).
