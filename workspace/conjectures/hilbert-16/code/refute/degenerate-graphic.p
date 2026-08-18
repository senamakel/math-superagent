% Attack: the open weakened claim R-one-degenerate-graphic, reduced to its
% smallest logical fragment: finite cyclicity is asserted for every quadratic
% perturbation of a named open graphic. Model search tests whether the
% abstract hypotheses can force an infinite cyclicity counterexample.
fof(cyclic_nat, axiom, ![X] : (cyclicity(X) = 0 | cyclicity(X) = 1 | cyclicity(X) = 2 | cyclicity(X) = 3)).
fof(open_graphic, axiom, graphic(g0)).
fof(target, conjecture, cyclicity(g0) < 4).
