% Attack on G-threshold-analysis (bipartite-threshold-shadow skeleton).
%
% The G1 contrapositive requires: for some d, EVERY A subset E satisfies
%     |O_{<=d}(A)| <= 2^{n-1} - |A|.
% If that universal inequality holds for d, then f(n) >= d+1.
%
% Attack at the singleton case (a=1). Cube Q_2: E={00,11}, O={01,10}.
% Take A={00}, |A|=1. Every odd vertex (01,10) has exactly 1 or 0 neighbours
% in A, both <= d for any d>=1. Hence |O_{<=d}(A)| = 2 = 2^{2-1} = half,
% while the required bound is half - |A| = 1.  Since 2 > 1, the universal
% inequality FAILS at a=1 for EVERY d >= 1. Thus d*(n)=0 for all n>=2: the
% threshold-shadow route can prove at most f(n)>=1, never omega(log n).
% G-threshold-analysis is refuted, independent of G2.

% vertices: v00, v01, v10, v11 all distinct
fof(d01, axiom, v01 != v00).
fof(d02, axiom, v10 != v00).
fof(d03, axiom, v11 != v00).
fof(d04, axiom, v10 != v01).
fof(d05, axiom, v11 != v01).
fof(d06, axiom, v11 != v10).

% A = {v00} (a=1); v11 even and not in A
fof(a_00, axiom, a(v00)).
fof(a_not_11, axiom, ~ a(v11)).

% Odd vertices are v01, v10, each with <=1 neighbour in A (singleton), so both
% in O_{<=d} for every d>=1. That is |O_{<=d}(A)| = 2 = half.
fof(odd_01, axiom, inO1(v01)).
fof(odd_10, axiom, inO1(v10)).

% Attack: the universal inequality at a=1,d=1 would require |O_{<=1}(A)| <= 1,
% i.e. NOT both odd vertices in O_{<=1}.
fof(goal, conjecture, ~ ( inO1(v01) & inO1(v10) )).
