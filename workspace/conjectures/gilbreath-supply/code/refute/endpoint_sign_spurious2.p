% Refute the committed formula in G-endpoint-comparison-density:
%
%   (-1)^{T(n,d)} =?  (-1)^{#runs(d)} * prod_R chi(r_{a_R}) chi(r_{b_R})
%
% Take d = 3 (binary 11). g = nu2(4) = 2, so #runs = 2^{popcount-2} = 1:
% the single run [0,3].  The down-set XOR telescopes: T(n,3) is the XOR of h
% over offsets 0..3 at base n-1-d, which telescopes to the single endpoint
% comparison [r_{n-1-d} != r_{n-1-d+4}]  (XOR of consecutive h toggles on a
% mismatch: sum of h over [a,b] = [r_{b+1} != r_a]).
%
% TRUE identity (each run telescopes with NO extra sign):
%   (-1)^{T} = chi(r_a) chi(r_b),  because [x!=y]=1 <=> chi(x)chi(y)=-1.
%
% COMMITTED formula inserts (-1)^{#runs} = (-1)^1 = -1, so it claims
%   (-1)^{T} = - chi(r_a) chi(r_b),
% which is the OPPOSITE sign for every string.
%
% We encode a concrete flag: mismatch = [r_a != r_b] (a single boolean for the
% single run).  True: (-1)^T == (+)chi_a*chi_b  <=>  the product sign matches
% the mismatch parity, i.e. (-1)^T = -1 iff mismatch, T=mismatch.
% Committed: (-1)^T = - chi_a chi_b, i.e. T = NOT mismatch.
%
% Conjecture (the committed claim): T == NOT mismatch.  A model with
% T == mismatch (any actual {0,1} h satisfies T = mismatch by construction)
% falsifies the committed formula.  Use h0=h1=h2=h3=0 => T=0, and all r equal
% => mismatch=0.  Then committed predicts T=1, truly T=0.
tff(declare_h, type, (h0: $o) & (h1: $o) & (h2: $o) & (h3: $o)).
tff(declare_r, type, (r0: $o) & (r1: $o) & (r2: $o) & (r3: $o) & (r4: $o)).
% h[j] = [ r_{j+1} != r_j ]
tff(h0_def, axiom, ( h0 <=> ( r0 xor r1 ) )).
tff(h1_def, axiom, ( h1 <=> ( r1 xor r2 ) )).
tff(h2_def, axiom, ( h2 <=> ( r2 xor r3 ) )).
tff(h3_def, axiom, ( h3 <=> ( r3 xor r4 ) )).
% T = XOR of h over the run offsets 0..3
tff(T_def, axiom, ( T <=> ( h0 xor h1 xor h2 xor h3 ) )).
% mismatch (the single run's endpoint comparison r_a vs r_b, a=0,b=4):
%   equals the parity T by telescoping.  State it.
tff(mismatch_def, axiom, ( mismatch <=> ( r0 xor r4 ) )).
tff(telescope, axiom, ( mismatch <=> T )).
% committed formula predicts T = NOT mismatch  (the spurious -1 per run)
fof(goal, conjecture, ( ~( T <=> mismatch ) )).
