% Attack on G-weak-input-strictness's proposed first step (per-window SAT):
% "encode 'exists h in F2^n with wt(h)<=delta n and wt(Phi_n h)>=eps n' and
% report SAT witnesses."
%
% We show this SAT is TRIVIALLY satisfiable by the boundary spike, so it cannot
% distinguish G-weak-input-strictness (fixed string, all large n) from its rival
% G-eq-sparse-fold-is-sublinear. n = 8, h = h0..h7.
%
% The attacked claim (weakest form of "sparse -> sublinear weight"):
%   "no very-sparse h (<=1 one) can have wt(Phi_8 h) > 2."
% We encode the fold cells and sparseness as axioms and this claim as the
% conjecture; find_counterexample searches for a sparse h that violates it.
%
% Fold cells were derived by hand from T(n,d) = XOR of h[n-1-d+o] over submasks o
% of d. For n=8, d in [2,7]:
%   d=2(010): submasks{0,2} -> cols {5,7}: t2 = h5 xor h7
%   d=3(011): submasks{0,1,2,3} -> cols {4,5,6,7}: t3 = h4^h5^h6^h7
%   d=4(100): submasks{0,4} -> cols {3,7}: t4 = h3 xor h7
%   d=5(101): submasks{0,1,4,5} -> cols {2,3,6,7}: t5 = h2^h3^h6^h7
%   d=6(110): submasks{0,2,4,6} -> cols {1,3,5,7}: t6 = h1^h3^h5^h7
%   d=7(111): all -> cols {0,1,2,3,4,5,6,7}: t7 = h0^..^h7

% ---- fold cell definitions (XOR as ~(a <=> b)) ----
fof(t2, axiom, ( t2 <=> ~( h5 <=> h7 ) )).
fof(c31, axiom, ( c31 <=> ~( h4 <=> h5 ) )).
fof(c32, axiom, ( c32 <=> ~( c31 <=> h6 ) )).
fof(t3, axiom, ( t3 <=> ~( c32 <=> h7 ) )).
fof(t4, axiom, ( t4 <=> ~( h3 <=> h7 ) )).
fof(c51, axiom, ( c51 <=> ~( h2 <=> h3 ) )).
fof(c52, axiom, ( c52 <=> ~( c51 <=> h6 ) )).
fof(t5, axiom, ( t5 <=> ~( c52 <=> h7 ) )).
fof(c61, axiom, ( c61 <=> ~( h1 <=> h3 ) )).
fof(c62, axiom, ( c62 <=> ~( c61 <=> h5 ) )).
fof(t6, axiom, ( t6 <=> ~( c62 <=> h7 ) )).
fof(s71, axiom, ( s71 <=> ~( h0 <=> h1 ) )).
fof(s72, axiom, ( s72 <=> ~( s71 <=> h2 ) )).
fof(s73, axiom, ( s73 <=> ~( s72 <=> h3 ) )).
fof(s74, axiom, ( s74 <=> ~( s73 <=> h4 ) )).
fof(s75, axiom, ( s75 <=> ~( s74 <=> h5 ) )).
fof(s76, axiom, ( s76 <=> ~( s75 <=> h6 ) )).
fof(t7, axiom, ( t7 <=> ~( s76 <=> h7 ) )).

% ---- sparseness: wt(h) <= 1 (no two h_i both 1) ----
fof(sp01, axiom, ~( h0 & h1 )).
fof(sp02, axiom, ~( h0 & h2 )).
fof(sp03, axiom, ~( h0 & h3 )).
fof(sp04, axiom, ~( h0 & h4 )).
fof(sp05, axiom, ~( h0 & h5 )).
fof(sp06, axiom, ~( h0 & h6 )).
fof(sp07, axiom, ~( h0 & h7 )).
fof(sp12, axiom, ~( h1 & h2 )).
fof(sp13, axiom, ~( h1 & h3 )).
fof(sp14, axiom, ~( h1 & h4 )).
fof(sp15, axiom, ~( h1 & h5 )).
fof(sp16, axiom, ~( h1 & h6 )).
fof(sp17, axiom, ~( h1 & h7 )).
fof(sp23, axiom, ~( h2 & h3 )).
fof(sp24, axiom, ~( h2 & h4 )).
fof(sp25, axiom, ~( h2 & h5 )).
fof(sp26, axiom, ~( h2 & h6 )).
fof(sp27, axiom, ~( h2 & h7 )).
fof(sp34, axiom, ~( h3 & h4 )).
fof(sp35, axiom, ~( h3 & h5 )).
fof(sp36, axiom, ~( h3 & h6 )).
fof(sp37, axiom, ~( h3 & h7 )).
fof(sp45, axiom, ~( h4 & h5 )).
fof(sp46, axiom, ~( h4 & h6 )).
fof(sp47, axiom, ~( h4 & h7 )).
fof(sp56, axiom, ~( h5 & h6 )).
fof(sp57, axiom, ~( h5 & h7 )).
fof(sp67, axiom, ~( h6 & h7 )).

% ---- CONJECTURE (the claim under attack): wt(Phi_8 h) <= 2 ----
% i.e. no three of the six cells are simultaneously 1. 20 triples.
fof(g1, conjecture, ~( t2 & t3 & t4 )).
fof(g2, conjecture, ~( t2 & t3 & t5 )).
fof(g3, conjecture, ~( t2 & t3 & t6 )).
fof(g4, conjecture, ~( t2 & t3 & t7 )).
fof(g5, conjecture, ~( t2 & t4 & t5 )).
fof(g6, conjecture, ~( t2 & t4 & t6 )).
fof(g7, conjecture, ~( t2 & t4 & t7 )).
fof(g8, conjecture, ~( t2 & t5 & t6 )).
fof(g9, conjecture, ~( t2 & t5 & t7 )).
fof(g10, conjecture, ~( t2 & t6 & t7 )).
fof(g11, conjecture, ~( t3 & t4 & t5 )).
fof(g12, conjecture, ~( t3 & t4 & t6 )).
fof(g13, conjecture, ~( t3 & t4 & t7 )).
fof(g14, conjecture, ~( t3 & t5 & t6 )).
fof(g15, conjecture, ~( t3 & t5 & t7 )).
fof(g16, conjecture, ~( t3 & t6 & t7 )).
fof(g17, conjecture, ~( t4 & t5 & t6 )).
fof(g18, conjecture, ~( t4 & t5 & t7 )).
fof(g19, conjecture, ~( t4 & t6 & t7 )).
fof(g20, conjecture, ~( t5 & t6 & t7 )).
% The model-finder should find h with wt(h)<=1 and weight(Phi_8 h)>=3, e.g.
% the boundary spike h=e_7 (only h7=1) which makes ALL six cells 1.
