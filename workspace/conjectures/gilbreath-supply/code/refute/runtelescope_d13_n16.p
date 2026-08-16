% Independent engine verification of the run-telescope identity
% (G-run-telescope) on a NON-TRIVIAL multi-run instance, via a different
% engine than the run's own Python brute-force.
%
% The run-telescope reduction (research/notes/g_run_telescope_verified.md,
% adopted by the endpoint-parity approach) says: the digital down-set of d
% decomposes into maximal consecutive-integer runs, and over ANY run [u,v]
% the fold cell telescopes:
%     XOR_{o in [u,v]} h[pos+o] = [ r_{pos+u} != r_{pos+v+1} ]
% for a two-valued boundary r (prime case r_j = q_j mod 4), with
% h[j] = [ r_j != r_{j+1} ].
%
% d = 13 (binary 1101), down-set {0,1,4,5,8,9,12,13} =
%     [0,1] U [4,5] U [8,9] U [12,13]   (g=nu2(14)=1, run length 2, 4 runs).
% At n=16, pos = n-1-d = 2, so the fold cell reads
%     T(16,13) = h[2]^h[3]^h[6]^h[7]^h[10]^h[11]^h[14]^h[15].
% The four runs telescope independently:
%     [0,1]  -> [r_2 != r_4],  [4,5] -> [r_6 != r_8],
%     [8,9]  -> [r_10 != r_12], [12,13] -> [r_14 != r_16].
% Identity:  T == m := m1^m2^m3^m4, for EVERY two-valued boundary string r.
%
% XOR(a,b) = ~(a <=> b).  XOR of k bits built with explicit auxiliaries to
% avoid double-negation errors.  A counterexample (model satisfying axioms,
% falsifying conjecture) would refute the reduction; "proved" certifies d=13
% case.

% --- helper XOR definitions (XOR(a,b) = ~(a<=>b)) ---
% T = h2^h3^h6^h7^h10^h11^h14^h15 via pairwise XOR auxiliaries
fof(ax_x1, axiom, ( x1 <=> ~( h2 <=> h3 ) )).    % x1 = h2^h3
fof(ax_x2, axiom, ( x2 <=> ~( h6 <=> h7 ) )).    % x2 = h6^h7
fof(ax_y1, axiom, ( y1 <=> ~( x1 <=> x2 ) )).    % y1 = h2^h3^h6^h7
fof(ax_x3, axiom, ( x3 <=> ~( h10 <=> h11 ) )).  % x3 = h10^h11
fof(ax_x4, axiom, ( x4 <=> ~( h14 <=> h15 ) )).  % x4 = h14^h15
fof(ax_y2, axiom, ( y2 <=> ~( x3 <=> x4 ) )).    % y2 = h10^h11^h14^h15
fof(ax_T,  axiom, ( T  <=> ~( y1 <=> y2 ) )).    % T = all eight

% --- h bits as boundary differences: h[j] = [r_j != r_{j+1}] ---
fof(ax_h2,  axiom, ( h2  <=> ~( r2  <=> r3  ) )).
fof(ax_h3,  axiom, ( h3  <=> ~( r3  <=> r4  ) )).
fof(ax_h6,  axiom, ( h6  <=> ~( r6  <=> r7  ) )).
fof(ax_h7,  axiom, ( h7  <=> ~( r7  <=> r8  ) )).
fof(ax_h10, axiom, ( h10 <=> ~( r10 <=> r11 ) )).
fof(ax_h11, axiom, ( h11 <=> ~( r11 <=> r12 ) )).
fof(ax_h14, axiom, ( h14 <=> ~( r14 <=> r15 ) )).
fof(ax_h15, axiom, ( h15 <=> ~( r15 <=> r16 ) )).

% --- run-endpoint mismatch bits ---
fof(ax_m1, axiom, ( m1 <=> ~( r2  <=> r4  ) )).
fof(ax_m2, axiom, ( m2 <=> ~( r6  <=> r8  ) )).
fof(ax_m3, axiom, ( m3 <=> ~( r10 <=> r12 ) )).
fof(ax_m4, axiom, ( m4 <=> ~( r14 <=> r16 ) )).

% --- m = m1^m2^m3^m4 (auxiliaries) ---
fof(ax_w1, axiom, ( w1 <=> ~( m1 <=> m2 ) )).    % w1 = m1^m2
fof(ax_w2, axiom, ( w2 <=> ~( m3 <=> m4 ) )).    % w2 = m3^m4
fof(ax_m,  axiom, ( m  <=> ~( w1 <=> w2 ) )).    % m = all four

% --- CONJECTURE: the run-telescope reduction holds for every r ---
fof(goal, conjecture, ( T <=> m )).
