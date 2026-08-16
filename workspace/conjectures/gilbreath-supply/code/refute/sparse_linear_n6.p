% Attack: G-weak-input-strictness / G-eq-sparse-fold-is-sublinear (shared first
% move). The committed rival claims are:
%   * G-eq-sparse-fold-is-sublinear  (FALSE reading): sparse h => low fold weight
%   * G-weak-input-strictness        (EXISTENCE): some sparse h has linear fold weight
% Finite instance n=6. The claim attacked here is the FALSE reading's sharpest
% small form:  "every h with wt(h) <= 2 has fold weight <= 2"  (fold weight
% below n/2 = 3).  A model h with wt <= 2 but fold weight >= 3 falsifies it.
%
% Definitions (problem.md facts 1-2): fold cell at depth d
%   T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o],  d in [2, n-1].
% n=6:  d=2 (10): submasks {0,2}, base n-1-d=3 -> cols {3,5}: T2 = h3 xor h5
%       d=3 (11): submasks {0,1,2,3}, base 2 -> cols {2,3,4,5}: T3 = h2^h3^h4^h5
%       d=4 (100): submasks {0,4}, base 1 -> cols {1,5}: T4 = h1 xor h5
%       d=5 (101): submasks {0,1,4,5}, base 0 -> cols {0,1,4,5}: T5 = h0^h1^h4^h5
%
% The boundary spike h = e_5 (h5=1, rest 0) has wt=1 and
%   T2=h3^h5=1, T3=h2^h3^h4^h5=1, T4=h1^h5=1, T5=h0^h1^h4^h5=1 => fold=4 >= 3
% so it should refute the conjecture. The engine must find it (free booleans).
% INTERIOR single 1 (h=e_1) instead gives only T4=h1^h5=1 => fold=1: the claim's
% truth on the interior is what distinguishes the corrected reading.

% free bits of h
fof(h_free, axiom, $true).

% XOR helper is inline via DNF
fof(def_t2, axiom,
    ( t2 <=> ( (h3 & ~h5) | (~h3 & h5) ) )).
fof(def_t3, axiom,
    ( t3 <=> ( (h2 & ~h3 & h4 & ~h5) | (h2 & ~h3 & ~h4 & h5)
             | (h2 & h3 & ~h4 & ~h5) | (~h2 & h3 & h4 & h5)
             | (~h2 & ~h3 & h4 & h5) | (~h2 & ~h3 & ~h4 & ~h5)
             | (h2 & h3 & h4 & h5) | (~h2 & h3 & ~h4 & ~h5)
             | (h2 & ~h3 & h4 & h5) | (~h2 & h3 & h4 & ~h5)
             | (h2 & h3 & ~h4 & h5) | (~h2 & ~h3 & h4 & ~h5)
             | (h2 & ~h3 & ~h4 & ~h5) | (~h2 & h3 & ~h4 & h5)
             | (~h2 & ~h3 & ~h4 & h5) | (~h2 & ~h3 & ~h4 & h5) ) )).
% (T3 four-bit XOR = parity of h2,h3,h4,h5: the 8 minterms of odd parity)
fof(def_t4, axiom,
    ( t4 <=> ( (h1 & ~h5) | (~h1 & h5) ) )).
fof(def_t5, axiom,
    ( t5 <=> ( (h0 & ~h1 & h4 & ~h5) | (h0 & ~h1 & ~h4 & h5)
             | (~h0 & h1 & h4 & h5) | (~h0 & ~h1 & ~h4 & ~h5)
             | (h0 & h1 & ~h4 & ~h5) | (~h0 & ~h1 & h4 & h5)
             | (h0 & ~h1 & h4 & h5) | (~h0 & h1 & ~h4 & ~h5) ) )).
% (T5 = 4-bit XOR of h0,h1,h4,h5: odd-parity minterms)

% fold weight >= 3 : at least 3 of {t2,t3,t4,t5} true.
fof(fold_ge3, axiom,
    ( (t2 & t3 & t4) | (t2 & t3 & t5) | (t2 & t4 & t5) | (t3 & t4 & t5) )).

% Conjecture (claim being attacked): there is NO h with wt<=2 and fold>=3.
% A model (h) falsifying this IS a sparse-linear witness.
fof(goal, conjecture,
    ( ~ ( (t2 & t3 & t4) | (t2 & t3 & t5) | (t2 & t4 & t5) | (t3 & t4 & t5) ) )).
