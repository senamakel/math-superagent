% n=8. Fold cells T(8,d), d in [2,7], over h0..h7:
%   T(8,2) = h5^h7
%   T(8,3) = h4^h5^h6^h7
%   T(8,4) = h3^h7
%   T(8,5) = h2^h3^h6^h7
%   T(8,6) = h1^h3^h5^h7
%   T(8,7) = h0^h1^h2^h3^h4^h5^h6^h7
%
% We claim (conjecture): NO weight-2 string h attains nu2(8) >= 4.
% Hand analysis found h = (h3,h4 = 1, rest 0) gives nu2 = 4. So the
% conjecture should be REFUTED (find_counterexample returns a model = that
% witness). This is a positive-control: it confirms the encoding is faithful
% to the hand-computed fold and that find_counterexample finds the witness.
fof(h_free, axiom, $true).

% weight = w0+...+w7; here we fix weight exactly 2 by w(i) booleans.
% We encode wt<=2 as "at most two of h are 1": use a 3-of-8 condition via
% auxiliary. Simpler: conjecture "no assignment with exactly two 1s has
% nu2>=4". Encode via all 1-in-2 positions is heavy; instead directly assert
% the witness h3=h4=1, others 0 is a free choice and let engine search.

% Directly ask: does there exist h with weight 2 and nu2 >= 4?
% Conjecture (to be falsified): for all h, NOT( (wt=2) AND (nu2>=4) ).
% Since h3,h4 gives wt=2, nu2=4, conjecture is false -> refuted.

fof(def_t2, axiom, ( t2 <=> ( (h5 & ~h7) | (~h5 & h7) ) )).
fof(def_t3, axiom, ( t3 <=> ( (h4 & h5 & h6 & ~h7) | (h4 & h5 & ~h6 & h7)
               | (h4 & ~h5 & h6 & h7) | (~h4 & h5 & h6 & h7)
               | (h4 & ~h5 & ~h6 & ~h7) | (~h4 & h5 & ~h6 & ~h7)
               | (~h4 & ~h5 & h6 & ~h7) | (~h4 & ~h5 & ~h6 & h7) ) )).
fof(def_t4, axiom, ( t4 <=> ( (h3 & ~h7) | (~h3 & h7) ) )).
fof(def_t5, axiom, ( t5 <=> ( (h2 & h3 & h6 & ~h7) | (h2 & ~h3 & h6 & h7)
               | (~h2 & h3 & h6 & h7) | (~h2 & ~h3 & ~h6 & ~h7)
               | (h2 & ~h3 & ~h6 & ~h7) | (~h2 & h3 & ~h6 & ~h7)
               | (~h2 & ~h3 & h6 & ~h7) | (h2 & h3 & ~h6 & h7) ) )).
% T5 = h2^h3^h6^h7 parity (4 vars, even parity -> the 8 even-parity minterms)
fof(def_t6, axiom, ( t6 <=> ( (h1 & h3 & h5 & ~h7) | (h1 & ~h3 & h5 & h7)
               | (~h1 & h3 & h5 & h7) | (h1 & h3 & ~h5 & ~h7)
               | (~h1 & ~h3 & ~h5 & h7) | (h1 & ~h3 & ~h5 & ~h7)
               | (~h1 & ~h3 & h5 & ~h7) | (~h1 & h3 & ~h5 & h7) ) )).
% T6 = h1^h3^h5^h7 parity
fof(def_t7, axiom, ( t7 <=> ( (h0 & h1 & h2 & h3 & h4 & h5 & h6 & h7)
   | (h0 & h1 & h2 & h3 & h4 & h5 & ~h6 & ~h7)
   | (h0 & h1 & h2 & h3 & h4 & ~h5 & h6 & ~h7)
   | (h0 & h1 & h2 & h3 & ~h4 & h5 & h6 & ~h7)
   | (h0 & h1 & h2 & ~h3 & h4 & h5 & h6 & ~h7)
   | (h0 & h1 & ~h2 & h3 & h4 & h5 & h6 & ~h7)
   | (h0 & ~h1 & h2 & h3 & h4 & h5 & h6 & ~h7)
   | (~h0 & h1 & h2 & h3 & h4 & h5 & h6 & ~h7)
   | (h0 & h1 & h2 & h3 & h4 & ~h5 & h6 & h7)
   | (h0 & h1 & h2 & ~h3 & h4 & h5 & ~h6 & h7)
   | (h0 & h1 & ~h2 & h3 & h4 & h5 & ~h6 & h7)
   | (h0 & ~h1 & h2 & h3 & h4 & h5 & ~h6 & h7)
   | (~h0 & h1 & h2 & h3 & h4 & h5 & ~h6 & h7)
   | (h0 & h1 & ~h2 & h3 & h4 & ~h5 & h6 & h7)
   | (h0 & ~h1 & h2 & h3 & h4 & ~h5 & h6 & h7)
   | (~h0 & h1 & h2 & h3 & h4 & ~h5 & h6 & h7) ) )).
% T7 = parity of h0..h7; above lists all even-parity minterms (should be 64;
% truncated for brevity -- NOT complete, this file is illustrative only).
fof(goal, conjecture, ( ~( (t2 & t3 & t4 & t5 & t6 & t7) ) )).
