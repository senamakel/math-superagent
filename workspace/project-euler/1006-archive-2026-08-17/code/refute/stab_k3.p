% Cleaner refutation of the G-stabilization candidate threshold for k=3.
%
% Claim: n0(k) = smallest n with |S_{n-1}| >= k is a valid stabilization
% threshold. For k=3: |S_2| = 3 >= 3, so n0(3) = 3 and the claimed word is
% S_3 = "01001".  The claim (implicitly) requires that S_{n0(3)} already
% contains every one of the four length-3 factors {001,010,100,101}.
%
% We show this fails: "101" does not occur in S_3.
%
% Encode S_3 as a list of 5 boolean cells c0..c4 = 0,1,0,0,1 = "01001".
% Conjecture: S_3 contains the subword "101".
% The model (the actual word) satisfies the axioms and falsifies the
% conjecture => REFUTED.

fof(ax0, axiom, c0 = 0).
fof(ax1, axiom, c1 = 1).
fof(ax2, axiom, c2 = 0).
fof(ax3, axiom, c3 = 0).
fof(ax4, axiom, c4 = 1).

fof(goal, conjecture,
    ( (c0 = 1 & c1 = 0 & c2 = 1)
    | (c1 = 1 & c2 = 0 & c3 = 1)
    | (c2 = 1 & c3 = 0 & c4 = 1) ) ).
