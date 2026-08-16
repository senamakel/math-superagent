% Honest refutation test of the COMMITTED formula in G-endpoint-comparison-density.
%
% Committed statement (character-sum reduction in the live skeleton files):
%   (-1)^{T(n,d)} = (-1)^{#runs(d)} . prod_R chi(r_{a_R}) chi(r_{b_R})
%
% TRUE identity (each telescoped run carries chi(r_a)chi(r_b) with NO extra
% sign; XOR carries signs multiplicatively; the (-1)^{#runs} factor is
% spurious):
%   (-1)^{T(n,d)} = prod_R chi(r_{a_R}) chi(r_{b_R})
%
% For d = 3 (binary 11): g = nu2(4) = 2, so #runs = 2^{popcount-2} = 1: the
% single run [0,3]. Hence T = h0^h1^h2^h3 telescopes to r0^r4 (= mismatch), and
% the corrected identity is (T <=> mismatch), while the committed one inserts
% the extra factor -1 and claims T <=> ~mismatch.
%
% We give the structural axioms (h from r, T from h, mismatch from r, and the
% single-run telescoping T <=> mismatch) and put the COMMITTED formula as the
% conjecture.  A model satisfying the axioms (truth) but falsifying the
% conjecture (committed) is a counterexample: the committed formula is wrong
% for that string.  Because the axioms force T==mismatch and the conjecture
% demands T==~mismatch, every model of the axioms refutes the conjecture.
%
% Written in the style of the n4/n5 problems that the model-finder resolved:
% plain fof, boolean constants used directly, no tff/$o declarations.
fof(h0_def, axiom, ( h0 <=> ~( r0 <=> r1 ) )).
fof(h1_def, axiom, ( h1 <=> ~( r1 <=> r2 ) )).
fof(h2_def, axiom, ( h2 <=> ~( r2 <=> r3 ) )).
fof(h3_def, axiom, ( h3 <=> ~( r3 <=> r4 ) )).
% T = h0 xor h1 xor h2 xor h3  (parity)
fof(p1, axiom, ( p1 <=> ~( h0 <=> h1 ) )).
fof(p2, axiom, ( p2 <=> ~( p1 <=> h2 ) )).
fof(T_def, axiom, ( T <=> ~( p2 <=> h3 ) )).
% mismatch = r0 xor r4
fof(mismatch_def, axiom, ( mismatch <=> ~( r0 <=> r4 ) )).
% single-run telescoping truth: T <=> mismatch
fof(telescope, axiom, ( T <=> mismatch )).
% COMMITTED formula (conjecture, to be refuted): T <=> ~mismatch
fof(goal, conjecture, ( T <=> ~ mismatch )).
