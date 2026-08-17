% Refutation of the G-stabilization "first-step" candidate threshold.
%
% Claim under attack:  n0(k) = smallest n with |S_{n-1}| >= k is a valid
% stabilization threshold, i.e. the length-k factor set of S_{n0(k)} already
% equals the full set of k+1 distinct length-k factors of the infinite
% Fibonacci word f.
%
% Test case k=3.  |S_2| = 3  ( |S_0|=1, |S_1|=2, |S_2|=|S_1S_0|=3 ),
% so the candidate gives n0(3) = 3, i.e. the word S_3 = S_2 S_1 = "010" "01"
% = "01001".  Its length-3 substrings are {010, 100, 001} (three of them).
% The true length-3 factor set of f is {001,010,100,101}: the factor "101"
% IS a Fibonacci subword (it appears in S_4), but it does NOT appear in S_3.
%
% So the candidate word S_3 does not contain all four length-3 factors,
% falsifying the claim that S_{n0(3)} already has the stabilized factor set.
%
% Axioms: the actual bits of S_3 = 0 1 0 0 1 at positions 0..4.
% Conjecture to falsify: the string "101" occurs as a length-3 substring of S_3.
% A model = S_3 satisfies the axioms and falsifies this conjecture -> refuted.

fof(S3_bit0, axiom, bit0 = 0).
fof(S3_bit1, axiom, bit1 = 1).
fof(S3_bit2, axiom, bit2 = 0).
fof(S3_bit3, axiom, bit3 = 0).
fof(S3_bit4, axiom, bit4 = 1).

% "101" appears at some start position i in {0,1,2} of S_3.
fof(has_101, conjecture,
    ( (bit0 = 1 & bit1 = 0 & bit2 = 1)
    | (bit1 = 1 & bit2 = 0 & bit3 = 1)
    | (bit2 = 1 & bit3 = 0 & bit4 = 1) ) ).
