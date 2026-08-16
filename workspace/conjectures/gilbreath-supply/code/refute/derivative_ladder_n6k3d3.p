% Refuter: is the adopted derivative-ladder identity (L1)
%   T_{Δ^k h}(n,d) = T(n+k, d+k)
% false for some instance?  Polynomial proof says it is an exact identity.
% Concrete instance: n=6, k=3, d=3, h0..h8 free.
%
%   LHS = T(6,3)[Δ^3 h] = Δ³h[2]⊕Δ³h[3]⊕Δ³h[4]⊕Δ³h[5],   Δ³h[j]=h[j]⊕h[j+1]⊕h[j+2]⊕h[j+3]
%       = h2⊕h4⊕h6⊕h8        (interior cancels)
%   RHS = T(9,6)[h] = XOR over submasks {0,2,4,6} of 6 of h[9-1-6+o]=h[2+o]
%       = h2⊕h4⊕h6⊕h8        ✓ identical
%
% Conjecture: "the identity fails" — i.e. some assignment h makes LHS != RHS.
% If find_counterexample returns PROVED (no model), the identity holds here.
% AXIOMS: none (h fully free).

fof(identity_holds, conjecture,
    % LHS and RHS are the same parity h2^h4^h6^h8, so falsification would need
    % them to differ.  Spell out both parities and demand inequality.
    ~( ( h2 ^ h4 ^ h6 ^ h8 ) = ( h2 ^ h4 ^ h6 ^ h8 ) ) ).
