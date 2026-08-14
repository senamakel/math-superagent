% Attack on the G-stabilization first-step candidate threshold.
%
% Claim under attack (from the G-stabilization lemma's first step):
%   n0(k) = the smallest n with |S_{n-1}| >= k, and for every n >= n0(k)
%   the length-k factor set of S_n equals the full set of length-k factors
%   of the infinite Fibonacci word (cardinality k+1).
%
% Counterexample addressed here: k = 3.  |S_m| = F_{m+2}, so the candidate
% n0(3) = smallest n with F_{n+1} >= 3  = n0(3) = 3.  But S_3 = "01001"
% realizes only the THREE length-3 factors {010,100,001}; the factor 101
% (which IS a factor of the infinite Fibonacci word, and is needed for the
% full set of k+1 = 4 factors) is missing.  So the factor set at n0(3)=3 is
% NOT the full set and is not constant from n0(3) onward (it grows to size 4
% at n=4).  Hence the candidate threshold is false.
%
% Encoding: axioms fix the characters of S_3 = "01001" at positions 0..4.
% char(P,L) means position P holds letter L, with letters z=0, o=1.
% The conjecture asserts that the length-3 factor "101" (o z o) occurs as a
% contiguous substring of S_3.  If the tool reports "refuted", it confirms
% that S_3 does NOT contain 101, i.e. the k=3 factor set at n0(3)=3 is not
% the full set of size 4.
fof(axiom_p0, axiom, char(0, z)).
fof(axiom_p1, axiom, char(1, o)).
fof(axiom_p2, axiom, char(2, z)).
fof(axiom_p3, axiom, char(3, z)).
fof(axiom_p4, axiom, char(4, o)).
% Letters are distinct.
fof(axiom_letters, axiom, z != o).
% A position holds at most one letter.
fof(axiom_unique0, axiom, ! [L] : (char(0,L) => L = z)).
fof(axiom_unique1, axiom, ! [L] : (char(1,L) => L = o)).
fof(axiom_unique2, axiom, ! [L] : (char(2,L) => L = z)).
fof(axiom_unique3, axiom, ! [L] : (char(3,L) => L = z)).
fof(axiom_unique4, axiom, ! [L] : (char(4,L) => L = o)).

% Conjecture: the length-3 factor "101" (= o z o) occurs contiguously in S_3.
fof(goal, conjecture,
    (char(0,o) & char(1,z) & char(2,o))
    | (char(1,o) & char(2,z) & char(3,o))
    | (char(2,o) & char(3,z) & char(4,o))).
