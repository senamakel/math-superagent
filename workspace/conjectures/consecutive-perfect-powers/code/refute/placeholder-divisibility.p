% Refute the problem.md "necessary condition" hint on an odd-prime solution:
%     p^2 | y^(p-1) - 1
% Claimed to hold for every hypothetical odd-prime solution.  But G-Cassels
% forces the co-tangent condition p | y.  For p | y, y = p m, so
% y^(p-1) - 1 == -1 (mod p): NOT divisible by p, hence NOT by p^2.  So the
% hint is false at every Cassels-consistent y.
%
% Smallest instance: p = 3, y = 3.  p | y (3 | 3) holds (Cassels-consistent).
% p^2 | y^(p-1)-1 is 9 | 3^2 - 1 = 8, which is FALSE.
%
% Present as: Cassels-consistent y=3 in the model, the necessary condition
% p2div(3) fails there, so the universal necessary condition is refuted.
%
% Encode the assertion to break as the conjecture "cassels_y(Y) =>
% p2div(Y) for all Y", with a model in which y=3 is cassels-consistent and
% p2div(3) is false.

% Domain: candidate y values that an odd-prime solution permits (>= 2),
% restricted to keep the model small; include the falsifying one.
fof(d1, axiom, yval(3)).
fof(d2, axiom, yval(5)).

% G-Cassels p|y holds at y=3 (multiple of p=3), fails at y=5.
fof(cassels_3, axiom, cassels_y(3)).

% The claimed necessary condition p^2 | y^(p-1)-1 evaluated at p=3:
%   y=3 : 9 | 8  -> false
%   y=5 : 9 | 24 -> false
fof(nc3, axiom, ~p2div(3)).
fof(nc5, axiom, ~p2div(5)).

% Assert the necessary condition: every Cassels-consistent y satisfies it.
fof(goal, conjecture, ![Y] : (cassels_y(Y) => p2div(Y))).
