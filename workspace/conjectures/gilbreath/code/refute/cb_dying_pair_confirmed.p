% Confirmation channel: the axioms FORCE that the dying row d does NOT have
% block length 1.  So "the dying row has block length 1" (the lemma's
% assertion) is impossible.
%
% bone(d): row d has leading {0,2} block length 1  -> second entry in {0,2}
% dying(d): row d's second entry is NOT in {0,2}
% These are incompatible; if d is dying then bone(d) is forced false.
% Conjecture: the dying row does NOT have block length 1.

tff(dom, type, nr: $i).
tff(decl_dying, type, dying: nr > $o).
tff(decl_bone, type, bone: nr > $o).
tff(decl_second02, type, second02: nr > $o).
tff(decl_d, type, d: nr).

tff(def_b1, axiom, ![R:nr]: ( bone(R) => second02(R) )).
tff(dying_def, axiom, ![R:nr]: ( dying(R) => ~ second02(R) )).
tff(d_is_dying, axiom, dying(d)).

% Conjecture: the dying row is NOT bone (block length is not 1).
tff(conj, conjecture, ~ bone(d)).
