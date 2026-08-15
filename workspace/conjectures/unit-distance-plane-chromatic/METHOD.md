Solve by explicit construction and complete machine verification, not by
general theory. The problem reduces to finite unit-distance graphs, so the work
is: exact-arithmetic coordinate machinery first, a complete k-colourability
oracle second, calibration of both against the 7-vertex graph third, and only
then a search over structured constructions.

The oracle for this problem is a pair — an edge certifier that proves
|x - y|^2 = 1 symbolically over an algebraic number field, and a complete
k-colouring test that returns a witness colouring when one exists. Neither is
trusted until both reproduce chi = 4 on the 7-vertex graph in problem.md.

Coordinates are exact algebraic numbers throughout. Floating point is not
permitted anywhere in the construction or verification path, because a spurious
edge raises the apparent chromatic number and there is no self-correcting
pressure against it.
