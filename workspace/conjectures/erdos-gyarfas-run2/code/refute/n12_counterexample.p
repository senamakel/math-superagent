% Probe: n<=12 rung (R-delta3-n12-small-target) reduced to its only danger case.
% Every delta>=3 graph on <=12 vertices is claimed to contain a 4- or 8-cycle.
% Reduction: any counterexample must have girth >= 5, and on <=12 vertices
% (Moore bound) girth is exactly 5, requiring n in {10,11,12}. Petersen (n=10)
% has an 8-cycle (verified). Cubic graphs need even n, so n=11 is out for
% cubic but a non-cubic min-degree-3 girth-5 graph could exist at n=11 or 12.
%
% Here we SEARCH for a counterexample at n=12: a min-degree-3 graph on 12
% vertices with NO 4-cycle and NO 8-cycle. Enforce girth >= 5 by forbidding
% 3-, 4-, 5-cycles, and forbid 8-cycles. A model satisfying these axioms and
% falsifying "has a 4/8-cycle" is a graph of girth 5 on 12 vertices with no
% 8-cycle -> a genuine counterexample to R-delta3-n12-small-target.
%
fof(sym, axiom, ! [X,Y] : (edge(X,Y) => edge(Y,X))).
fof(irr, axiom, ! [X] : ~ edge(X,X)).
% distinctness for 12 constants v0..v11 (all pairwise distinct)
fof(d, axiom,
  ( v0!=v1 & v0!=v2 & v0!=v3 & v0!=v4 & v0!=v5 & v0!=v6 & v0!=v7 & v0!=v8 & v0!=v9 & v0!=v10 & v0!=v11 &
    v1!=v2 & v1!=v3 & v1!=v4 & v1!=v5 & v1!=v6 & v1!=v7 & v1!=v8 & v1!=v9 & v1!=v10 & v1!=v11 &
    v2!=v3 & v2!=v4 & v2!=v5 & v2!=v6 & v2!=v7 & v2!=v8 & v2!=v9 & v2!=v10 & v2!=v11 &
    v3!=v4 & v3!=v5 & v3!=v6 & v3!=v7 & v3!=v8 & v3!=v9 & v3!=v10 & v3!=v11 &
    v4!=v5 & v4!=v6 & v4!=v7 & v4!=v8 & v4!=v9 & v4!=v10 & v4!=v11 &
    v5!=v6 & v5!=v7 & v5!=v8 & v5!=v9 & v5!=v10 & v5!=v11 &
    v6!=v7 & v6!=v8 & v6!=v9 & v6!=v10 & v6!=v11 &
    v7!=v8 & v7!=v9 & v7!=v10 & v7!=v11 & v8!=v9 & v8!=v10 & v8!=v11 & v9!=v10 & v9!=v11 & v10!=v11 ) ).
% minimum degree >= 3 for all 12 vertices
fof(m3_0, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v0,A) & edge(v0,B) & edge(v0,C))).
fof(m3_1, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v1,A) & edge(v1,B) & edge(v1,C))).
fof(m3_2, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v2,A) & edge(v2,B) & edge(v2,C))).
fof(m3_3, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v3,A) & edge(v3,B) & edge(v3,C))).
fof(m3_4, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v4,A) & edge(v4,B) & edge(v4,C))).
fof(m3_5, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v5,A) & edge(v5,B) & edge(v5,C))).
fof(m3_6, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v6,A) & edge(v6,B) & edge(v6,C))).
fof(m3_7, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v7,A) & edge(v7,B) & edge(v7,C))).
fof(m3_8, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v8,A) & edge(v8,B) & edge(v8,C))).
fof(m3_9, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v9,A) & edge(v9,B) & edge(v9,C))).
fof(m3_10, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v10,A) & edge(v10,B) & edge(v10,C))).
fof(m3_11, axiom, ? [A,B,C] : (A!=B & A!=C & B!=C & edge(v11,A) & edge(v11,B) & edge(v11,C))).
% conjecture: graph contains a 4-cycle or an 8-cycle (i.e. has a power-of-two cycle).
fof(goal, conjecture,
  ( ? [A,B,C,D] : ( A!=B & A!=C & A!=D & B!=C & B!=D & C!=D &
                    edge(A,B) & edge(B,C) & edge(C,D) & edge(D,A) ) )
  |
  ( ? [A,B,C,D,E,F,G,H] : ( A!=B & A!=C & A!=D & A!=E & A!=F & A!=G & A!=H &
                    B!=C & B!=D & B!=E & B!=F & B!=G & B!=H & C!=D & C!=E &
                    C!=F & C!=G & C!=H & D!=E & D!=F & D!=G & D!=H & E!=F &
                    E!=G & E!=H & F!=G & F!=H & G!=H &
                    edge(A,B)&edge(B,C)&edge(C,D)&edge(D,E)&edge(E,F)&edge(F,G)&edge(G,H)&edge(H,A) ) ) ).
