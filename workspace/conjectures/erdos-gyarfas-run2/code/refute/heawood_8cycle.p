% Refutation probe: the Heawood graph (smallest cubic girth-6 graph, n=14).
%
% Danger case for the settled rung R-delta3-n16-three-targets:
% "every delta>=3 graph on <=16 vertices has a 4/8/16-cycle."
% Girth 6 kills C4 and n<=16 kills C16, so the rung's truth for this graph
% rests entirely on whether it has an 8-cycle.
%
% If find_counterexample returns "proved", the 8-cycle is entailed by the
% exact structure => the Heawood danger case does NOT refute the rung.
% If it returns "refuted" (a model with these exact incidences but no 8-cycle
% exists) => the rung is FALSE.
%
% Structure: points p0..p6, lines l0..l6. Line i contains points i,i+1,i+3
% mod 7 (Fano-plane incidence => Heawood graph, the (3,6)-cage).
fof(edge_sym, axiom, ! [X,Y] : (edge(X,Y) => edge(Y,X))).
fof(irreflexive, axiom, ! [X] : ~ edge(X,X)).
% exact structure: edge iff one of the 42 Heawood incidences (as undirected).
fof(structure, axiom,
  ! [X,Y] :
  ( edge(X,Y)
  <=> ( (X=p0 & Y=l0) | (X=p1 & Y=l0) | (X=p3 & Y=l0)
     | (X=p1 & Y=l1) | (X=p2 & Y=l1) | (X=p4 & Y=l1)
     | (X=p2 & Y=l2) | (X=p3 & Y=l2) | (X=p5 & Y=l2)
     | (X=p3 & Y=l3) | (X=p4 & Y=l3) | (X=p6 & Y=l3)
     | (X=p4 & Y=l4) | (X=p5 & Y=l4) | (X=p0 & Y=l4)
     | (X=p5 & Y=l5) | (X=p6 & Y=l5) | (X=p1 & Y=l5)
     | (X=p6 & Y=l6) | (X=p0 & Y=l6) | (X=p2 & Y=l6)
     ) ) ).
% distinctness of the 14 constants
fof(distinct_points, axiom,
  ( p0!=p1 & p0!=p2 & p0!=p3 & p0!=p4 & p0!=p5 & p0!=p6 &
    p1!=p2 & p1!=p3 & p1!=p4 & p1!=p5 & p1!=p6 & p2!=p3 &
    p2!=p4 & p2!=p5 & p2!=p6 & p3!=p4 & p3!=p5 & p3!=p6 &
    p4!=p5 & p4!=p6 & p5!=p6 &
    l0!=l1 & l0!=l2 & l0!=l3 & l0!=l4 & l0!=l5 & l0!=l6 &
    l1!=l2 & l1!=l3 & l1!=l4 & l1!=l5 & l1!=l6 & l2!=l3 &
    l2!=l4 & l2!=l5 & l2!=l6 & l3!=l4 & l3!=l5 & l3!=l6 &
    l4!=l5 & l4!=l6 & l5!=l6 ) ).
% conjecture: the Heawood graph contains a (simple) 8-cycle.
fof(goal, conjecture,
  ? [A,B,C,D,E,F,G,H] :
    ( A!=B & A!=C & A!=D & A!=E & A!=F & A!=G & A!=H &
      B!=C & B!=D & B!=E & B!=F & B!=G & B!=H & C!=D &
      C!=E & C!=F & C!=G & C!=H & D!=E & D!=F & D!=G &
      D!=H & E!=F & E!=G & E!=H & F!=G & F!=H & G!=H &
      edge(A,B) & edge(B,C) & edge(C,D) & edge(D,E) &
      edge(E,F) & edge(F,G) & edge(G,H) & edge(H,A) ) ).
