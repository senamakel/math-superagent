% Honest test of the CORRECTED endpoint-sign identity for d=3, over every
% residue string r in {1,3}^4 (encoded as booleans r0..r4; the set {1,3} is a
% 2-element set so r_j is a boolean, value conventions irrelevant).
%
% d = 3 (binary 11) has the SINGLE run [0,3], so
%   T = h[base] ^ h[base+1] ^ h[base+2] ^ h[base+3]
% with h[j] = [ r_{j+1} != r_j ] = r_j XOR r_{j+1}.
% Telescoping:  T = r0 XOR r4 = mismatch.
%
% CORRECTED identity: (-1)^T = chi(r0)chi(r4), i.e. T == mismatch.
% COMMITTED identity inserts an extra (-1)^{#runs} = -1, i.e. T == ~mismatch.
%
% We test BOTH as separate conjectures.  Defs only; NO telescope axiom.
tff(declare, type, (r0: $o) & (r1: $o) & (r2: $o) & (r3: $o) & (r4: $o)
                  & (h0: $o) & (h1: $o) & (h2: $o) & (h3: $o)
                  & (T: $o) & (mismatch: $o)).
% h[j] = r_j XOR r_{j+1}
tff(h0_def, axiom, ( h0 <=> ~( r0 <=> r1 ) )).
tff(h1_def, axiom, ( h1 <=> ~( r1 <=> r2 ) )).
tff(h2_def, axiom, ( h2 <=> ~( r2 <=> r3 ) )).
tff(h3_def, axiom, ( h3 <=> ~( r3 <=> r4 ) )).
% T = h0 XOR h1 XOR h2 XOR h3
tff(p12, axiom, ( p12 <=> ~( h0 <=> h1 ) )).
tff(p123, axiom, ( p123 <=> ~( p12 <=> h2 ) )).
tff(T_def, axiom, ( T <=> ~( p123 <=> h3 ) )).
% mismatch = r0 XOR r4
tff(mismatch_def, axiom, ( mismatch <=> ~( r0 <=> r4 ) )).
% CORRECTED identity (conjecture): T == mismatch
fof(goal_corr, conjecture, ( T <=> mismatch )).
