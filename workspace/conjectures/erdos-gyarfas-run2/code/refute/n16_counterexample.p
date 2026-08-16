% Probe: is the n<=16 rung (R-delta3-n16-three-targets) FALSE?
% Claim (asserted settled): every delta>=3 graph on at most 16 vertices has
% a cycle of length 4, 8, or 16.
%
% Counterexample search formulated as a MODEL search. The signature is a
% single edge predicate on 16 vertices v0..v15. Axioms say edge is a simple,
% symmetric, minimum-degree-3 graph. Conjecture says such a graph has a
% 4/8/16-cycle. find_counterexample searches for a model satisfying the axioms
% and FALSIFYING the conjecture -- i.e. a delta>=3 graph on 16 vertices with NO
% cycle of length 4, 8 or 16. Such a model IS a counterexample to the rung
% (and to the asserted Balaji 31-vertex bound).
%
% If the tool returns "refuted" with a model, that graph is the refutation.
% "proved" = every delta>=3 graph on these vertices has a 4/8/16-cycle (no
% counterexample). "undecided" = inconclusive.
fof(sym, axiom, ! [X,Y] : (edge(X,Y) => edge(Y,X))).
fof(irr, axiom, ! [X] : ~ edge(X,X)).
% minimum degree >= 3 for every vertex:
fof(d3_v0, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v0,A) & edge(v0,B) & edge(v0,C) )).
fof(d3_v1, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v1,A) & edge(v1,B) & edge(v1,C) )).
fof(d3_v2, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v2,A) & edge(v2,B) & edge(v2,C) )).
fof(d3_v3, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v3,A) & edge(v3,B) & edge(v3,C) )).
fof(d3_v4, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v4,A) & edge(v4,B) & edge(v4,C) )).
fof(d3_v5, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v5,A) & edge(v5,B) & edge(v5,C) )).
fof(d3_v6, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v6,A) & edge(v6,B) & edge(v6,C) )).
fof(d3_v7, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v7,A) & edge(v7,B) & edge(v7,C) )).
fof(d3_v8, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v8,A) & edge(v8,B) & edge(v8,C) )).
fof(d3_v9, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v9,A) & edge(v9,B) & edge(v9,C) )).
fof(d3_v10, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v10,A) & edge(v10,B) & edge(v10,C) )).
fof(d3_v11, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v11,A) & edge(v11,B) & edge(v11,C) )).
fof(d3_v12, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v12,A) & edge(v12,B) & edge(v12,C) )).
fof(d3_v13, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v13,A) & edge(v13,B) & edge(v13,C) )).
fof(d3_v14, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v14,A) & edge(v14,B) & edge(v14,C) )).
fof(d3_v15, axiom, ? [A,B,C] : ( A!=B & A!=C & B!=C & edge(v15,A) & edge(v15,B) & edge(v15,C) )).
% distinctness of 16 vertices
fof(distinct, axiom, ! [X,Y] : (X!=Y) ).
% conjecture: the graph contains a cycle of length 4, 8, or 16.
fof(goal, conjecture,
  ( ? [A,B,C,D] : ( A!=B & A!=C & A!=D & B!=C & B!=D & C!=D &
                    edge(A,B) & edge(B,C) & edge(C,D) & edge(D,A) ) )
  |
  ( ? [A,B,C,D,E,F,G,H] : ( A!=B & A!=C & A!=D & A!=E & A!=F & A!=G & A!=H &
                    B!=C & B!=D & B!=E & B!=F & B!=G & B!=H & C!=D & C!=E &
                    C!=F & C!=G & C!=H & D!=E & D!=F & D!=G & D!=H & E!=F &
                    E!=G & E!=H & F!=G & F!=H & G!=H &
                    edge(A,B)&edge(B,C)&edge(C,D)&edge(D,E)&edge(E,F)&edge(F,G)&edge(G,H)&edge(H,A) ) )
  |
  ( ? [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P] : ( edge(A,B)&edge(B,C)&edge(C,D)&edge(D,E)&edge(E,F)&edge(F,G)&edge(G,H)&edge(H,I)&edge(I,J)&edge(J,K)&edge(K,L)&edge(L,M)&edge(M,N)&edge(N,O)&edge(O,P)&edge(P,A) ) )
  ) ).
