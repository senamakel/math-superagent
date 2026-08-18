% Attack: the unrestricted membrane-avoidance lemma, reduced to its
% necessary consequence that every Jordan curve has some epsilon with no
% special trapezoid of that size. This first-order fragment only models
% four points and the special-trapezoid predicate; it is intentionally
% minimal and does not pretend to encode topology of S^1.
fof(distinct, axiom, ![A,B,C,D] : ( (A != B & A != C & A != D & B != C & B != D & C != D) -> distinct4(A,B,C,D) )).
fof(special_definition, axiom, ![A,B,C,D] : (special(A,B,C,D) -> (A != B & B != C & C != D & D != A))).
fof(goal, conjecture, ![A,B,C,D] : ~special(A,B,C,D)).
