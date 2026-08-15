% Attack S1-nu2-transfer-weight (universal case): is wt(Phi_n h) >= wt(h)/2
% for ALL bit strings h?  For n=6 the tail cells of the halved diagonal are:
%   cell k=2 : h4 XOR h5
%   cell k=3 : h3 XOR h5
%   cell k=4 : h2 XOR h3 XOR h4 XOR h5
% where h2..h5 are the halved row-1 gap bits at columns j=2..5.
% nu2 = number of nonzero cells; w = weight of h.
% The universal claim is: forall h, 2*nu2 >= w.
% We ask whether a counterexample exists (2*nu2 < w).

fof(h2_val, axiom, ( h2 = 0 | h2 = 1 )).
fof(h3_val, axiom, ( h3 = 0 | h3 = 1 )).
fof(h4_val, axiom, ( h4 = 0 | h4 = 1 )).
fof(h5_val, axiom, ( h5 = 0 | h5 = 1 )).

% cells are 1 iff the XOR is odd (nonzero)
fof(c2_def, axiom, ( c2 = 1 <=> ( h4 != h5 ) )).
fof(c3_def, axiom, ( c3 = 1 <=> ( h3 != h5 ) )).
fof(c4_def, axiom, ( c4 = 1 <=> ( $mod($sum(h2,$sum(h3,$sum(h4,h5))),2) = 1 ) )).

% c2,c3,c4 are 0/1
fof(c2_val, axiom, ( c2 = 0 | c2 = 1 )).
fof(c3_val, axiom, ( c3 = 0 | c3 = 1 )).
fof(c4_val, axiom, ( c4 = 0 | c4 = 1 )).

% nu2 = c2+c3+c4, w = h2+h3+h4+h5
fof(nu2_def, axiom, ( nu2 = $sum(c2,$sum(c3,c4)) )).
fof(w_def, axiom, ( w = $sum(h2,$sum(h3,$sum(h4,h5))) )).

% The universal claim we believe (the run's transfer lemma).
fof(transfer_claim, conjecture, ( $greatereq($product(2,nu2), w) )).
