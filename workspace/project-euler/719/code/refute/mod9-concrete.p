% Concrete refutation attempt on the mod-9 filter (claim partition-sum-invariant-mod9).
%
% Filter claim: an S-number n = m^2 is such that its root m satisfies
% m ≡ 0 or 1 (mod 9), because the block-sum (which equals m) is congruent to
% m^2 (mod 9).  We try to break it by exhibiting a root m ≡ 2 (mod 9) that is
% an S-root in the SMALLEST concrete cases.
%
% Candidate m = 11 (11^2 = 121, 11 ≡ 2 mod 9).  The three 2+-block splits of
% "121" are:
%    1|21  -> 22
%    12|1  -> 13
%    1|2|1 -> 4
% None equals 11, so 11 is not an S-root.  We encode this concretely and ask
% find_counterexample to model a root m ≡ 2 mod 9 being an S-root.  We also
% force residues: 11 mod 9 = 2.

% candidates for residue-2 roots and their splits
fof(root11, axiom, m = 11 ).                       % candidate root 11
fof(res2,   axiom, residue(m) = 2 ).               % 11 ≡ 2 mod 9

% 11^2 = 121, and the digit string "121" admits exactly these 2+-block sums:
% 1+21=22, 12+1=13, 1+2+1=4.
fof(split_a, axiom, block_sum = 22 | block_sum = 13 | block_sum = 4 ).

% For 11 to be an S-root the block-sum would have to equal m = 11.
fof(goal, conjecture, block_sum = m ).
