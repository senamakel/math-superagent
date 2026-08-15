% Attack: the strong per-event form of G-balance.
% Claim being attacked (G-balance, strong form): at every (2,4)-event the jump
% j >= d, where d = number of erosion rows since the previous event.
%
% This is a claim about real rows, so the primary falsifier is the run's own
% depth-1000 oracle record (counterexample: b sequence
% 739,873,872,871,872 with events at 739->873 (j=134) and 871->872 (j=1),
% two erosions 873->872->871 in between, so d=2 and j=1 < 2).
%
% Here we encode the *pure numerical* fragment of the claim, detached from the
% triangle dynamics: five consecutive block lengths A,B,C,D,E with
%   B-A >= 0   (first event)
%   C = B-1    (erosion)
%   D = C-1    (erosion)
%   E-D >= 0   (second event)
% and conjecture that the second event's jump E-D >= 2 (= the number of
% intermediate erosions). This fragment is FALSE in general, witnessed by
% (739,873,872,871,872), i.e. A=739,B=873,C=872,D=871,E=872 with E-D=1.
%
% We negate the claim: we ask find_counterexample to search for a model
% satisfying the axioms (the five-block pattern) and falsifying the conjecture
% (E-D >= 2). The model (739,873,872,871,872) is a counterexample.

fof(pattern_1, axiom, leq_b(b0, b1)).                  % B-A >= 0
fof(erosion_1, axiom, b2 = minus(b1, one)).            % C = B-1
fof(erosion_2, axiom, b3 = minus(b2, one)).            % D = C-1
fof(pattern_2, axiom, leq_b(b3, b4)).                  % E-D >= 0
fof(integers, axiom, all_pos_ints).                    % placeholder, removed below

fof(conjecture, conjecture, geq(minus(b4, b3), two)).
