% Run-telescope identity with a THREE-VALUED boundary r -- NEGATIVE CONTROL.
%
% The run's load-bearing claim (G-run-telescope) is that for a TWO-VALUED
% boundary r (prime case r_j = q_j mod 4 in {1,3}), over any run [u,v] of the
% digital down-set,
%     XOR_{o in [u,v]} h[pos+o] = [ r_{pos+u} != r_{pos+v+1} ].
% The two-valuedness is load-bearing: for a THREE-valued start-of-chapter
% boundary the telescoping [a!=b]^[b!=c] = [a!=c] FAILS.
%
% Here we take d=3 (single run [0,3]) and a boundary r0..r4 with values in
% {0,1,2}, and CONJECTURE that the run-telescope identity still holds:
%     h[0]^h[1]^h[2]^h[3] == [r0 != r4],  h[j] = [r_j != r_{j+1}].
% This should be REFUTED (a three-valued assignment makes LHS != RHS).  This
% is the negative control proving the engine detects the break when it is
% there, so the two-valued case returning "no falsification" is meaningful.
%
% Hand witness: r0=0, r1=1, r2=2, r3=0, r4=1.
%   h[0]=[0!=1]=1, h[1]=[1!=2]=1, h[2]=[2!=0]=1, h[3]=[0!=1]=1,
%   LHS = 1^1^1^1 = 0.  RHS = [r0!=r4] = [0!=1] = 1.  0 != 1 -> REFUTED.
%
% r_j three-valued via exactly-one-of atoms rj0,rj1,rj2.

% ===== exactly-one-of-three per r_j =====
fof(e_o1, axiom, ( r0_0 | r0_1 | r0_2 )).
fof(e_o2, axiom, ( ~( r0_0 & r0_1 ) & ~( r0_0 & r0_2 ) & ~( r0_1 & r0_2 ) )).
fof(e_11, axiom, ( r1_0 | r1_1 | r1_2 )).
fof(e_12, axiom, ( ~( r1_0 & r1_1 ) & ~( r1_0 & r1_2 ) & ~( r1_1 & r1_2 ) )).
fof(e_21, axiom, ( r2_0 | r2_1 | r2_2 )).
fof(e_22, axiom, ( ~( r2_0 & r2_1 ) & ~( r2_0 & r2_2 ) & ~( r2_1 & r2_2 ) )).
fof(e_31, axiom, ( r3_0 | r3_1 | r3_2 )).
fof(e_32, axiom, ( ~( r3_0 & r3_1 ) & ~( r3_0 & r3_2 ) & ~( r3_1 & r3_2 ) )).
fof(e_41, axiom, ( r4_0 | r4_1 | r4_2 )).
fof(e_42, axiom, ( ~( r4_0 & r4_1 ) & ~( r4_0 & r4_2 ) & ~( r4_1 & r4_2 ) )).

% ===== h[j] = [r_j != r_{j+1}] : differ iff not(same value) =====
% same = (rj_0&rjp_0) | (rj_1&rjp_1) | (rj_2&rjp_2); h = NOT same
fof(h0_def, axiom, ( h0 <=> ~( ( r0_0 & r1_0 ) | ( r0_1 & r1_1 ) | ( r0_2 & r1_2 ) ) )).
fof(h1_def, axiom, ( h1 <=> ~( ( r1_0 & r2_0 ) | ( r1_1 & r2_1 ) | ( r1_2 & r2_2 ) ) )).
fof(h2_def, axiom, ( h2 <=> ~( ( r2_0 & r3_0 ) | ( r2_1 & r3_1 ) | ( r2_2 & r3_2 ) ) )).
fof(h3_def, axiom, ( h3 <=> ~( ( r3_0 & r4_0 ) | ( r3_1 & r4_1 ) | ( r3_2 & r4_2 ) ) )).

% ===== T = h0^h1^h2^h3 (single run d=3) =====
fof(x1, axiom, ( x1 <=> ~( h0 <=> h1 ) )).
fof(x2, axiom, ( x2 <=> ~( h2 <=> h3 ) )).
fof(T_def, axiom, ( T <=> ~( x1 <=> x2 ) )).

% ===== RHS = [r0 != r4] = not same((r0,r4)) =====
fof(rhs_def, axiom, ( rhs <=> ~( ( r0_0 & r4_0 ) | ( r0_1 & r4_1 ) | ( r0_2 & r4_2 ) ) )).

% ===== CONJECTURE: telescoping identity holds even for three-valued r =====
fof(goal, conjecture, ( T <=> rhs )).
