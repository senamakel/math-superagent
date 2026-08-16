% Refutation attempt on claim `partition-sum-invariant-mod9`.
%
% The claim: for an S-number n = m^2 with any witness split of its decimal
% digits into contiguous blocks summing to m, the block-sum m is congruent to
% n modulo 9, so m ≡ m^2 (mod 9), forcing m ≡ 0 or 1 (mod 9).  The run uses
% this as a pruning filter over candidate roots.
%
% We test the SOUNDNESS of that filter in a finite domain of residues mod 9.
% The claim to falsify: "there is a root m, an S-number with a witness split,
% whose residue is 2 mod 9."  If the filter is sound no such m exists, i.e.
% the axioms force res(m) in {0,1}.
%
% Arithmetic mod 9, residues in {0..8}.  concat(a,b) of two decimal blocks
% satisfies concat(a,b) ≡ a+b (mod 9) because 10 ≡ 1 (mod 9).  This is the
% digit-sum rule that underlies the invariant.
%
% The conjecture below states that such a "bad-residue" model does not exist;
% find_counterexample looks for a model satisfying the axioms and falsifying
% the conjecture, i.e. a genuine counterexample to the mod-9 filter.

% --- decimal digit-sum rule, mod 9 (10 ≡ 1) ---
fof(digitsum, axiom, ! [A,B] : res(concat(A,B)) = res(A + B) ).

% --- a candidate S-root m with a generic 2-block witness: blocks a,b
%     concatenate to m^2 and sum to m ---
fof(witness_concat, axiom, concat(a,b) = m2 ).
fof(witness_sum,    axiom, a + b = m ).

% m is a proper square root of m2 (m2 = m*m):
fof(square, axiom, m2 = m * m ).

% residues live in 0..8 (range of res):
fof(res_range, axiom,
    ( res(0)=0 & res(1)=1 & res(2)=2 & res(3)=3 & res(4)=4
    & res(5)=5 & res(6)=6 & res(7)=7 & res(8)=8 ) ).

% candidate m is a large-ish root (so m2 has 13 digits), m > 100000:
fof(big, axiom, m > 100000 ).

% --- conjecture: the filter is sound; no bad-residue S-root exists.
%     If this is falsifiable, find_counterexample produces a model where
%     res(m) is NOT 0 or 1 -- a counterexample to the mod-9 filter.
fof(no_bad_root, conjecture, ( res(m) = 0 | res(m) = 1 ) ).
