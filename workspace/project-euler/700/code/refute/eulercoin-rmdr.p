% Refutation of the run's method claim for the Eulercoin descent.
%
% Claim attacked (research/weakened/eulercoin.md, rung R-small-descent merge):
%   "the coins are the successive remainders in the Euclidean algorithm on
%    (M, A); each coin's index recovered from the quotients."
%
% On the run's own tiny oracle (M,A) = (17,7), the claim makes the SECOND
% Eulercoin equal to the first Euclidean remainder 17 mod 7 = 3.
%
% Truth: a_n = 7n mod 17. Record lows are 7@1, 4@3, 1@5, 0@17. The second
% Eulercoin is 4 at n=3. Value 3 first occurs at n=15, after the smaller coin
% 1, so 3 is not an Eulercoin. The second coin value is 4, NOT 3.
%
% Minimal ground encoding: two positions matter to the false claim --
%   q3 carries value b (the true second coin, 4)
%   q15 carries value d (the Euclidean remainder, 3)
% secondcoin(V) <=> V = b. Conjecture: secondcoin(d). A model with b != d
% refutes it.

tff(decl1, type, pos: $tType).
tff(decl2, type, val: $tType).
tff(decl3, type, value_of: pos > val).
tff(decl4, type, secondcoin: val > $o).

% q3 is the least index >1 whose 7n mod 17 drops below the first coin (7);
% its value b = 4 is the second Eulercoin. q15 is where the Euclidean
% remainder value d = 3 first occurs.
tff(p3, axiom, value_of(q3) = b).   % n=3 -> 4  (true second coin)
tff(p15, axiom, value_of(q15) = d). % n=15 -> 3 (Euclidean remainder, NOT a coin)

% q3 is the earlier index (n=3 < n=15).
tff(e3, axiom, q3 != q15).
% the true second coin value 4 (b) and the Euclidean remainder 3 (d) differ.
tff(dval, axiom, b != d).

% secondcoin(V) <=> V is the value at the smallest index >1 whose value is
% below the first coin value; that position is q3, so secondcoin(V) <=> V = b.
tff(second_def, axiom, ![V]: (secondcoin(V) <=> V = b)).

% Conjecture (the method claim): the second Eulercoin value is the first
% Euclidean remainder 17 mod 7 = 3, i.e. d.
tff(goal, conjecture, secondcoin(d)).
