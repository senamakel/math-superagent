% Cross-check of the oracle's claim that the Petersen graph has an 8-cycle.
% Petersen: outer 5-cycle 0-1-2-3-4-0, inner 5-point star 5-7-9-6-8-5,
% spokes i-(i+5). A known 8-cycle in Petersen: 0-1-2-3-4-9-6-8-0? verify. Use
% the canonical construction and the oracle in code/refute/heawood_n16.py
% instead; here we just pin the graph and conjecture an 8-cycle exists, as a
% second independent mechanism (find_counterexample proving it).
fof(edge_sym, axiom, ! [X,Y] : (edge(X,Y) => edge(Y,X))).
fof(irr, axiom, ! [X] : ~ edge(X,X)).
fof(structure, axiom,
  ! [X,Y] :
  ( edge(X,Y)
  <=> ( (X=o0 & Y=o1) | (X=o1 & Y=o2) | (X=o2 & Y=o3) | (X=o3 & Y=o4) | (X=o4 & Y=o0)
     | (X=i0 & Y=i2) | (X=i2 & Y=i4) | (X=i4 & Y=i1) | (X=i1 & Y=i3) | (X=i3 & Y=i0)
     | (X=o0 & Y=i0) | (X=o1 & Y=i1) | (X=o2 & Y=i2) | (X=o3 & Y=i3) | (X=o4 & Y=i4)
     ) ) ).
fof(distinct, axiom,
  ( o0!=o1 & o0!=o2 & o0!=o3 & o0!=o4 & o1!=o2 & o1!=o3 & o1!=o4 & o2!=o3 & o2!=o4 & o3!=o4 &
    i0!=i1 & i0!=i2 & i0!=i3 & i0!=i4 & i1!=i2 & i1!=i3 & i1!=i4 & i2!=i3 & i2!=i4 & i3!=i4 &
    o0!=i0 & o0!=i1 & o0!=i2 & o0!=i3 & o0!=i4 & o1!=i0 & o1!=i1 & o1!=i2 & o1!=i3 & o1!=i4 &
    o2!=i0 & o2!=i1 & o2!=i2 & o2!=i3 & o2!=i4 & o3!=i0 & o3!=i1 & o3!=i2 & o3!=i3 & o3!=i4 &
    o4!=i0 & o4!=i1 & o4!=i2 & o4!=i3 & o4!=i4 ) ).
% conjecture: Petersen has an 8-cycle.
fof(goal, conjecture,
  ? [A,B,C,D,E,F,G,H] :
    ( A!=B & A!=C & A!=D & A!=E & A!=F & A!=G & A!=H & B!=C & B!=D & B!=E &
      B!=F & B!=G & B!=H & C!=D & C!=E & C!=F & C!=G & C!=H & D!=E & D!=F &
      D!=G & D!=H & E!=F & E!=G & E!=H & F!=G & F!=H & G!=H &
      edge(A,B) & edge(B,C) & edge(C,D) & edge(D,E) & edge(E,F) & edge(F,G) &
      edge(G,H) & edge(H,A) ) ).
