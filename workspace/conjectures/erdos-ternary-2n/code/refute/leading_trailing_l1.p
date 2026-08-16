% Refuting rung R-leading-trailing of the Erdos ternary ladder at L=1.
%
% Rung (off: middle-digits, density-gap, independence):
%   "For a stated L, for every integer n > 8, the base-3 expansion of 2^n
%    contains a digit 2 among its first L leading digits OR its last L
%    trailing digits."
%
% Counterexample at L=1, n=10: 2^10 = 1024 = 1101221_3, whose
%   first-1 leading digit (most significant) = 1, and
%   last-1  trailing digit (least significant) = 1,
% neither of which is 2.  n=10 > 8.  The two 2s of 1024_3 sit strictly in
% the middle (positions 2 and 3), so they do not touch the windows.
%
% Exact integer check: 1024 = 1*3^6 + 1*3^5 + 0*3^4 + 1*3^3 + 2*3^2 + 2*3^1
%                          + 1*3^0
%                      = 729 + 243 + 0 + 27 + 18 + 6 + 1 = 1024.  Oracled.
%
% The axioms are exactly the ground digit facts of 1024 (position 6 = leading
% digit, position 0 = trailing digit).  The conjecture is the rung claim at
% L=1 applied to n=10; a model satisfying all axioms and falsifying it is the
% counterexample n=10.

% --- ground digit facts of 1024 = 1101221_3 ---
fof(facts, axiom,
    ( ~digit(6,2) & ~digit(0,2) & digit(6,1) & digit(0,1)
    & digit(5,1) & digit(4,0) & digit(3,1) & digit(2,2) & digit(1,2) )).

% --- rung claim: a 2 in the first-1 or last-1 digit ---
fof(conj, conjecture, ( digit(6,2) | digit(0,2) )).
