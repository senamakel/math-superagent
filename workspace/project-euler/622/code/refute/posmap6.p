% Attack: the out-faro position-map lemma (G-shuffle-order) at deck size n=6.
% Deck positions 0..5.  ONE out-faro on an even deck of size 6 (split in half,
% interleave left[right]): position of a card after one shuffle is given by the
% physical interleave.  We give ONLY the interleave as axioms (what the cards
% do), and attack the run's claimed formula: interior x -> 2x mod 5.
%
% Interleave for n=6: top half {0,1,2}, bottom half {3,4,5}.
%   new[0]=old[0], new[1]=old[3], new[2]=old[1], new[3]=old[4],
%   new[4]=old[2], new[5]=old[5]
% i.e. f(old position)=new position:  f(0)=0, f(3)=1, f(1)=2, f(4)=3,
%                                      f(2)=4, f(5)=5.
% The run claims f(x) = 2*x mod 5 for the interior x in {1,2,3,4},
% top (0) and bottom (5) fixed.

fof(interleave_0, axiom, f(0) = 0).
fof(interleave_1, axiom, f(1) = 2).
fof(interleave_2, axiom, f(2) = 4).
fof(interleave_3, axiom, f(3) = 1).
fof(interleave_4, axiom, f(4) = 3).
fof(interleave_5, axiom, f(5) = 5).

% Conjecture: f agrees with "interior x -> 2x mod 5, top/bottom fixed".
fof(goal, conjecture,
    (f(0) = 0 & f(1) = 2 & f(2) = 4 & f(3) = 1 & f(4) = 3 & f(5) = 5)).
