% Attack: the supply-side transfer claim G-supply-transfer is FALSE.
%
% Claim (research/BACKWARD.md): for every SUCCESSFUL 2-then-odds prefix
% q_1..q_n, with w = #{j in [2,n-1] : q_{j+1}-q_j ≡ 2 mod 4} and
% nu2 = # of 2s in the maximal {0,2} suffix of the right diagonal,
% one has nu2 >= (2/3)*w.
%
% Concrete instance that violates it (hand-verified, also from the run's own
% oracle): the SUCCESSFUL consecutive-odds prefix q = (2,3,5,7,9), n = 4.
%   - successful: A_3(0) = 1.                 (hypothesis holds)
%   - gaps g_2 = 7-5 = 2, g_3 = 9-7 = 2, both ≡ 2 mod 4, so w = 2.
%   - right diagonal delta(q_4) = (9,2,0,0); its {0,2}-suffix is (2,0,0),
%     so nu2 = 1 (0 under the run's tail convention d[2:-1] that drops delta_1).
%   - either way nu2 in {0,1} < (2/3)*2 = 4/3, so nu2 >= (2/3)w is FALSE.
%
% The axioms instantiate exactly that successful prefix and its counts; the
% conjecture asserts the (false) transfer bound, so find_counterexample should
% return a model (CounterSatisfiable) exhibiting nu2 < (2/3)w.

tff(decl, type, nu2: $int).
tff(decl, type, w: $int).
tff(decl, type, is_successful: $o).

% the instance is a successful prefix
tff(ax_success, axiom, is_successful).

% w = 2 (gaps g_2, g_3 both ≡ 2 mod 4)
tff(ax_w, axiom, w = 2).

% nu2 = 1 (the {0,2} suffix (2,0,0) of the diagonal has exactly one 2;
%          the run's stricter tail convention gives nu2 = 0, falsifying even
%          harder)
tff(ax_nu2, axiom, nu2 = 1).

% consistency: nu2 < (2/3) w, i.e. 3*nu2 < 2*w  (= 3 < 4)
tff(ax_violation, axiom, $less( $product(3, nu2), $product(2, w) )).

% the claim being attacked: nu2 >= (2/3) w, i.e. 3*nu2 >= 2*w
tff(goal, conjecture, $greatereq( $product(3, nu2), $product(2, w) )).
