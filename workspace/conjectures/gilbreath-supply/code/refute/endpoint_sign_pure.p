% Refute the committed formula in G-endpoint-comparison-density, purest form.
%
% For d = 3 (single run [0,3]), the down-set XOR telescopes to a single
% endpoint comparison: T = [r_a != r_b] (call this boolean `mismatch`).
% The TRUE sign identity is  (-1)^T = chi(r_a)chi(r_b), i.e. T == mismatch.
%
% The COMMITTED formula inserts (-1)^{#runs} with #runs=1, claiming
%   (-1)^T = - chi(r_a)chi(r_b),  i.e.  T == ~mismatch.
%
% So the committed claim, specialized to d=3, asserts T == NOT mismatch.
% The structural (telescoping) truth is T == mismatch.  We encode the
% telescoping truth as the AXIOM and the committed claim as the CONJECTURE.
% A model with T=1, mismatch=1 satisfies the axiom (truth) and falsifies the
% committed conjecture -- a concrete counterexample to the committed formula.
tff(declare, type, (mismatch: $o) & (T: $o)).
% telescoping truth: for d=3 the XOR over the single run is exactly the
% endpoint mismatch
tff(truth, axiom, ( T <=> mismatch )).
% committed formula specialized to d=3: T == NOT mismatch
fof(goal, conjecture, ( T <=> ~ mismatch )).
