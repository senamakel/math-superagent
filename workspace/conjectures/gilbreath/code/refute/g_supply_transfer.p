% Attack: G-supply-transfer (universal transfer) is FALSE on the successful
% consecutive-odds family.
%
% The claim: for every SUCCESSFUL 2-then-odds prefix q with
%   w   = #{j in [2,n-1] : gap_j ≡ 2 mod 4}
%   nu2 = # of 2s in the maximal {0,2} suffix of the right diagonal
% one has  nu2 >= (2/3) * w.
%
% Instance: q = (2,3,5,7,9) (consecutive odds, n=4), a SETTLED-successful
% prefix (R2-consecutive-odds-class: A_k(0)=1 for all k).
%   - successful: bottom entry A_3(0)=1.
%   - gaps g_2=7-5=2, g_3=9-7=2, both ≡2 mod4  ==> w = 2.
%   - right diagonal delta(q_4) = (A0(4),A1(3),A2(2),A3(1)) = (9,2,0,0).
%     The maximal {0,2} suffix is (2,0,0)  ==> nu2 = 1 (run's stricter tail
%     convention delta[2:-1]=(0) gives nu2 = 0).
%   - nu2 in {0,1} < (2/3)*2 = 4/3, so the claim's conclusion fails.
%
% This file encodes the concrete relation structure of the n=4 diagonal and
% the transfer bound purely relationally (no integer arithmetic), so the
% finite-model builder can exhibit the violating object.
%
% Objects: the four diagonal cells d0,d1,d2,d3 (d0 is the large odd apex 9,
% d1=2, d2=0, d3=0).  Predicate two(X): X == 2.  Predicate in02(X): X in
% {0,2}.  success: boolean.  gap_weight: the number of j in [2,3] with
% gap≡2 mod4 is 2 (g2,g3 both).  tail02: the suffix cells d1,d2,d3.
%
% We want a model where:
%   - success holds, gap2 and gap3 hold (w=2),
%   - d1,d2,d3 are the {0,2}-tail, with exactly one 2 among them (nu2=1),
%   - the transfer "the tail has at least (2/3)*the gap weight many 2s"
%     fails, i.e. it does NOT have at least 2 twos.

tff(dom, type, cell: $i).
tff(decl, type, d0: cell).
tff(decl, type, d1: cell).
tff(decl, type, d2: cell).
tff(decl, type, d3: cell).
tff(decl, type, two: cell > $o).
tff(decl, type, success: $o).
tff(decl, type, gap2: $o).
tff(decl, type, gap3: $o).

% the diagonal values
tff(d0_val, axiom, ~two(d0)).          % d0 = 9, odd, not 2
tff(d1_val, axiom,  two(d1)).          % d1 = 2
tff(d2_val, axiom, ~two(d2)).          % d2 = 0
tff(d3_val, axiom, ~two(d3)).          % d3 = 0

% success (the prefix is successful)
tff(success_ax, axiom, success).

% both relevant gaps are ≡ 2 mod 4   ==> w = 2
tff(gap2_ax, axiom, gap2).
tff(gap3_ax, axiom, gap3).

% the {0,2}-suffix of the diagonal is {d1,d2,d3}; its 2-count is nu2 = 1
% (only d1 is 2).  The transfer bound nu2 >= (2/3)w with w=2 demands nu2 >= 2,
% i.e. at least two of the three suffix cells are 2.  Axiom: NOT (the suffix
% has >= 2 twos) is what we want to be true for the model, and the conjecture
% asserts it does have >= 2 twos.

% model side: exactly one 2 in the suffix (nu2 = 1)
tff(exactly_one_suffix_two,
    axiom,
    ( two(d1) & ~two(d2) & ~two(d3) ) ).

% conjecture: the transfer holds for this instance:
% nu2 >= (2/3) w  with w=2  =>  nu2 >= 4/3  =>  nu2 >= 2, i.e. at least two
% 2s among the three suffix cells.
tff(goal, conjecture,
    ( ( two(d1) & two(d2) ) | ( two(d1) & two(d3) ) | ( two(d2) & two(d3) ) ) ).
