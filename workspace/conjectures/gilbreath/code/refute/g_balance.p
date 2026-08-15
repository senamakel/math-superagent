% Attack: strong per-event form of G-balance.
%
% Claim: at every (2,4)-event the jump j >= d, where d = number of erosion
% rows since the previous event.
%
% Minimal falsifiable fragment, detached from the triangle dynamics: two
% consecutive events separated by two erosion rows.
%   b0 <= b1        (first event: b grows, j1 = b1-b0)
%   b2 = b1 - 1     (erosion)
%   b3 = b2 - 1     (erosion)   => two erosion rows since the event
%   b3 <= b4        (second event: jump j2 = b4-b3)
% Conjecture (the claim for this fragment): j2 = b4-b3 >= 2.
%
% The run's own depth-1000 oracle row gives
%   (b0,b1,b2,b3,b4) = (739, 873, 872, 871, 872):
%   first event 739->873 (j=134), erosions 873->872, 872->871 (d=2),
%   second event 871->872 (j=1). Here j2 = 1 < 2, so the conjecture is FALSE.
% We state the axioms and the *negation-witnessed* conjecture; find_counterexample
% should satisfy the axioms and falsify the conjecture by exhibiting the model.

fof(ax1, axiom, leq(b0, b1)).
fof(ax2, axiom, b2 = minus(b1, one)).
fof(ax3, axiom, b3 = minus(b2, one)).
fof(ax4, axiom, leq(b3, b4)).

fof(goal, conjecture, geq(minus(b4, b3), two)).
