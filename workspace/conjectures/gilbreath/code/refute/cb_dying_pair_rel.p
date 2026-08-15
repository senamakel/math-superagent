% Purely relational refutation of the open lemma CB-dying-pair.
%
% Two facts from the run's own definitions:
%   (i)  bone(r)  = "row r has leading {0,2} block length 1"
%        definitional truth: bone(r) => second entry of r is in {0,2}
%   (ii) dying(r) = "row r's second entry is NOT in {0,2}" (this is what
%        makes the NEXT row's leading entry fail: |1 - A(r,1)| != 1).
%
% A row cannot be both bone and dying: bone(r) -> in02(A(r,1)) while
% dying(r) -> ~in02(A(r,1)).
%
% The lemma selects d = K-1 (the dying row) and asserts it is bone.
% We fix d as both the dying row (axiom) and the row the lemma calls bone
% (the conjecture).  The axioms force ~bone(d); the engine is asked for a
% model of the axioms refuting the conjecture --- i.e. one with bone(d)
% FALSE.  Such a model is exactly the real dying row K-1 (b=0).

tff(dom, type, nr: $i).
tff(decl_dying, type, dying: nr > $o).
tff(decl_bone, type, bone: nr > $o).
tff(decl_second02, type, second02: nr > $o).
tff(decl_d, type, d: nr).
tff(decl_e, type, e: nr).   % some other row, only to give the sort content

% (i) block length 1 forces the second entry into {0,2}
tff(def_b1, axiom, ![R:nr]: ( bone(R) => second02(R) )).
% (ii) dying means second entry NOT in {0,2}
tff(dying_def, axiom, ![R:nr]: ( dying(R) => ~ second02(R) )).
% d is the dying row
tff(d_is_dying, axiom, dying(d)).
% e is not dying, not bone -- a witness so the sort nr is not empty
tff(e_not, axiom, ~ dying(e)).

% THE LEMMA'S ASSERTION: the dying row d has block length 1.
tff(dying_pair_claim, conjecture, bone(d)).
