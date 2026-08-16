% Refute the committed formula in G-endpoint-comparison-density:
%
%   (-1)^{T(n,d)} = (-1)^{#runs(d)} * prod_R chi(r_{a_R}) chi(r_{b_R})
%
% Take d=3 (binary 11). g = nu2(4) = 2, popcount=2, so #runs = 2^0 = 1:
% a single run [0,3].  Then T(n,3) = [r_b != r_a] with a=n-4, b=n, and
% (-1)^{T} = chi(r_a) chi(r_b)  (each run telescopes, and
% [r_a!=r_b]=1 <=> chi(r_a)chi(r_b)=-1, so (-1)^{[r_a!=r_b]} = chi chi, no
% extra sign).
%
% The committed formula inserts an extra (-1)^{#runs} = (-1)^1 = -1 factor.
% Here we fix r_a = 1, r_b = 3  (so [r_a!=r_b] = 1, T=1, true value -1).
%   chi(1)=1, chi(3)=-1 -> chi chi = -1.
%   committed = (-1)^1 * (-1) = +1.
% The committed formula predicts +1; the true value is -1.  So the
% committed identity is FALSE.  We encode "committed == -1" as the
% conjecture; CounterSatisfiable (a model exists) refutes it.
%
% sign values: use integers -1 and +1 (the only values chi takes).
tff(declare_type, type, sign: $int).
% r_a = 1 (i.e. ra_eq_3 = false), r_b = 3 (rb_eq_3 = true)
tff(fact_ra, axiom, ra_eq_3 = $false).
tff(fact_rb, axiom, rb_eq_3 = $true).
% chi(x) = -1 iff x==3 else +1
tff(chi_a, axiom, ( ra_eq_3 = $true ) => chi_a = -1 ).
tff(chi_a0, axiom, ( ra_eq_3 = $false ) => chi_a = 1 ).
tff(chi_b, axiom, ( rb_eq_3 = $true ) => chi_b = -1 ).
tff(chi_b0, axiom, ( rb_eq_3 = $false ) => chi_b = 1 ).
% true value of (-1)^T = chi_a*chi_b
tff(prod, axiom, chichi = chi_a * chi_b ).
% committed value = (-1)^#runs * chichi = -1 * chichi (since #runs=1)
tff(nruns, axiom, nruns = 1 ).
tff(committed, axiom, committed_val = ( (-1) ** nruns ) * chichi ).
% conjecture: the committed formula equals the true value (-1) here
fof(goal, conjecture, ( committed_val = -1 )).
