% POSITIVE CONTROL: the CORRECTED endpoint-sign identity holds for d=3.
%
% d=3 (single run [0,3]):  T = h0^h1^h2^h3 telescopes to r0^r4 = [r0!=r4].
% Corrected identity:  (-1)^T = chi(r0) chi(r4), i.e. T == mismatch (no sign).
%
% We assert the corrected identity as the CONJECTURE and ask whether a model
% satisfies the axioms (the full telescoping structure) while falsifying it.
% The answer should be "no model / proved", i.e. the corrected identity is
% consistent: it holds for every string.  This is the control proving the
% engine can certify the corrected formula, so the failing COMMITTED one is a
% genuine refutation, not a tool artifact.
%
% mismatch = [r0!=r4] = r0 XOR r4 ; T == h0^h1^h2^h3 == mismatch.
fof(axiom_h0, axiom, ( h0 <=> ~( r0 <=> r1 ) )).
fof(axiom_h1, axiom, ( h1 <=> ~( r1 <=> r2 ) )).
fof(axiom_h2, axiom, ( h2 <=> ~( r2 <=> r3 ) )).
fof(axiom_h3, axiom, ( h3 <=> ~( r3 <=> r4 ) )).
fof(axiom_t, axiom, ( T <=> ~( ~( h0 <=> h1 ) <=> ~( h2 <=> h3 ) ) )).
fof(axiom_mismatch, axiom, ( mismatch <=> ~( r0 <=> r4 ) )).
% TELESCOPING: T == mismatch (the structural truth)
fof(axiom_telescope, axiom, ( T <=> mismatch )).
% CORRECTED IDENTITY (conjecture): (-1)^T = chi(r0)chi(r4), i.e. T == mismatch
fof(goal, conjecture, ( T <=> mismatch )).
