% Refute the committed identity in G-endpoint-comparison-density for d=3.
%
% d = 3 (binary 11): g = nu2(4) = 2, popcount = 2, so #runs = 2^(2-2) = 1
% (single run [0,3]).  The depth-3 fold cell is
%     T = XOR_{o in submasks-of-3} h[n-4+o] = h[base]^h[base+1]^h[base+2]^h[base+3]
% with base = n-4.  With h[j] = [r_{j+1} != r_j] (j indexed 0..), and writing
% h = (h0,h1,h2,h3) at base and r = (r0,r1,r2,r3,r4), the XOR of consecutive h
% telescopes:
%     h0^h1^h2^h3 = (r0^r1)^(r1^r2)^(r2^r3)^(r3^r4) = r0 ^ r4.
% So T = [r0 != r4] (a single endpoint comparison).
%
% TRUE sign identity (each telescoped run carries chi(r_a)chi(r_b), NO extra
% sign, because [r_a!=r_b] = 1 <=> chi(r_a)chi(r_b) = -1):
%     (-1)^T = chi(r0) chi(r4).
%
% COMMITTED formula:  (-1)^T = (-1)^{#runs} * prod_R chi(r_a)chi(r_b)
%                    = (-1)^1 * chi(r0) chi(r4) = - chi(r0) chi(r4).
%
% The committed formula therefore predicts T = NOT [r0!=r4] = [r0==r4],
% the exact opposite of the true T = [r0!=r4], for EVERY string.
%
% We encode the committed claim and show it is contradicted by the
% telescoping truth (T = mismatch).  All operators standard TPTP: explicit
% XOR via NOT(x <=> y).
%
% Concrete: r all equal (r0=r1=r2=r3=r4=1) => h=0000, T=0, mismatch=0.
%   True (-1)^T = +1, chi chi = +1.
%   Committed predicts (-1)^T = -1, i.e. T = 1.  FALSE.
tff(declare, type, (r0: $o) & (r1: $o) & (r2: $o) & (r3: $o) & (r4: $o)
                  & (h0: $o) & (h1: $o) & (h2: $o) & (h3: $o)
                  & (T: $o) & (mismatch: $o)
                  & (x12: $o) & (x123: $o)).
% h[j] = [ r_{j+1} != r_j ]  i.e. h_j = r_j XOR r_{j+1}
tff(h0_def, axiom, ( h0 <=> ~( r0 <=> r1 ) )).
tff(h1_def, axiom, ( h1 <=> ~( r1 <=> r2 ) )).
tff(h2_def, axiom, ( h2 <=> ~( r2 <=> r3 ) )).
tff(h3_def, axiom, ( h3 <=> ~( r3 <=> r4 ) )).
% T = h0^h1^h2^h3  (XOR)
tff(x12, axiom, ( x12 <=> ~( h0 <=> h1 ) )).
tff(x123, axiom, ( x123 <=> ~( x12 <=> h2 ) )).
tff(T_1, axiom, ( T <=> ~( x123 <=> h3 ) )).
% mismatch = [r0 != r4] = r0 XOR r4
tff(mismatch_def, axiom, ( mismatch <=> ~( r0 <=> r4 ) )).
% Telescoping truth: T == mismatch
tff(telescope, axiom, ( T <=> mismatch )).
% COMMITTED claim (to be refuted): T == NOT mismatch
fof(goal, conjecture, ( T <=> ~ mismatch )).
