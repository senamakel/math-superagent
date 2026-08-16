% Attack the character-sum formula asserted in G-endpoint-comparison-density
% (research/backward/supply-from-endpoint-parity.md):
%
%   (-1)^{T(n,d)} = (-1)^{#runs(d)} * PROD_R chi(r_{a_R}) chi(r_{b_R})
%
% The adopted approach dyadic-gap-character-correlation.md claims the
% (-1)^{#runs(d)} factor is SPURIOUS and the correct formula is
%
%   (-1)^{T(n,d)} = PROD_R chi(r_{a_R}) chi(r_{b_R})
%
% with NO extra sign.
%
% Concrete instance to decide the dispute: n=5, d=3, pos = n-1-d = 1.
%   down-set(3) = {0,1,2,3} = single run [0,3]  ->  #runs = 1 (odd).
%   The run telescopes: T(5,3) = XOR_{o in [0,3]} h[1+o]
%                        = h1^h2^h3^h4 = [r1 != r5].
%   So the CORRECT formula gives (-1)^T = chi(r1)*chi(r5)   (no sign factor).
%   The SKELETON formula gives (-1)^T = (-1)^{#runs=1} * chi(r1)*chi(r5)
%                                   = - chi(r1)*chi(r5).
%
% We encode the SKELETON formula as the conjecture over free residues and let
% find_counterexample search for residues making it false.  Since
% chi(r1)*chi(r5) = +-1 always and the two sides differ by a global minus,
% a model should be found immediately, confirming the skeleton sign is wrong.
%
% Encoding: r_j in {1,3}.  Represent with Boolean R_j := (r_j = 3), so
% chi(r_j) = -1 iff R_j  (chi(1)=+1, chi(3)=-1).
% h[j] = [r[j+1] != r[j]] = R[j+1] XOR R[j].
% T(5,3) = h1^h2^h3^h4 (positions 1..4 since pos=1, run [0,3]).

% free residues
fof(r_free, axiom, $true).

% T(5,3) = R1 xor R2 xor R3 xor R4 xor ... wait T = h1^h2^h3^h4 and
% h[j] = R[j+1]^R[j], so h1=R2^R1, h2=R3^R2, h3=R4^R3, h4=R5^R4.
% XOR all: (R2^R1)^(R3^R2)^(R4^R3)^(R5^R4) = R1 ^ R5 (everything cancels).
% Two constraints encode the XOR: define t~~R1^R5.
% t is true iff exactly one of R1,R5: (R1 & ~R5) | (~R1 & R5).

fof(def_t, axiom,
    ( t <=> ( (R1 & ~R5) | (~R1 & R5) ) )).

% chi(r_a)*chi(r_b) = +1 iff R_a = R_b, -1 iff R_a != R_b.
% Define the product value p in {+1,-1}: p = +1 iff R1 = R5.
%   p_plus  := (R1 & R5) | (~R1 & ~R5)

fof(def_p, axiom,
    ( pplus <=> ( (R1 & R5) | (~R1 & ~R5) ) )).

% LHS: (-1)^T = +1 iff t = 0  (T is a parity bit; T=1 -> -1, T=0 -> +1)
%   pleft_plus := (NOT t)
fof(def_lhs, axiom,
    ( pleftplus <=> ~t )).

% SKELETON RHS: (-1)^{#runs=1} * p = -p.
%   pright_plus = NOT pplus.
fof(def_rhs, axiom,
    ( prightplus <=> ~pplus )).

% Conjecture: the skeleton formula holds: LHS equals RHS (both +indicators equal).
fof(goal, conjecture,
    ( pleftplus <=> prightplus )).
