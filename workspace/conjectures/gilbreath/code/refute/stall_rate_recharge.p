% R-stall-rate-insufficiency (recharge-balance-ladder, stance: open) -
% finite search for a DYING 2-then-odds triangle whose (2,4)-events (if any)
% are all stalls (jump 0) with row-gap <= G, up to its death row.
%
% We encode a concrete candidate gap word and its triangle arithmetic with
% small finite domains, and ask find_counterexample whether a dying triangle
% exists that satisfies the bounded-gap all-stall event condition.
%
% Because the engine returns 'undecided' on unbounded integer arithmetic in
% this environment, this is a FALLBACK encoding; the structural argument is
% the recharge identity (below), which is the real content.

% --- triangle arithmetic for a concrete 2-then-odds word ---
% top row A0 = (2, 3, 5, 7, 13, ...)  (a spike-6-like family)
% row1 = (|2-3|, |3-5|, |5-7|, |7-13|) = (1, 2, 2, 6)
fof(r0_0, axiom, a00=2). fof(r0_1, axiom, a01=3).
fof(r0_2, axiom, a02=5). fof(r0_3, axiom, a03=7). fof(r0_4, axiom, a04=13).
% a1(i) = |a0(i) - a0(i+1)|
fof(a1_0, axiom, a10=1). fof(a1_1, axiom, a11=2).
fof(a1_2, axiom, a12=2). fof(a1_3, axiom, a13=6).
% a2(i) = |a1(i)-a1(i+1)|
fof(a2_0, axiom, a20=1). fof(a2_1, axiom, a21=0).  % |2-2|=0
fof(a2_2, axiom, a22=4).  % |2-6|=4
% a3(i) = |a2(i)-a2(i+1)|
fof(a3_0, axiom, a30=1). fof(a3_1, axiom, a31=4).  % |1-0|? no: a3_1=|a2_1-a2_2|=|0-4|
% death: A_3(1)=4 not in {0,2}
% The block dies at row 3 because A_3(1) = 4.
%
% This spike-6 family has NO (2,4)-event before death, so it does NOT satisfy
% the rung's premise.  It is recorded to show the engine path; the real
% refutation needs events that ARE stalls.  See stall_rate_insufficiency.py.
fof(goal, conjecture, a31 = 4).
