% ATTACK on G-kstar-budget / R-budget-n32 (the load-bearing budget claim):
%   K*(n) = ceil(n/2) for all n >= 6.
% At n = 8 the claim says K*(8) = 4: NO pair h,h' in F_2^8 with identical
% order-4 correlation vector C_4 (identical 5-gram histograms) has different
% S^2.  The run's own exact computation orderk_correlation_brute reports
% K*(8)=5 (i.e. a C_4-separating pair EXISTS), so this is disputed.
%
% I ask find_counterexample to decide the exact question:
%   does there exist h,h' in F_2^8 with IDENTICAL C_4 (equal multiset of the
%   4 overlapping 5-bit windows) but DIFFERENT S^2 ?
% Conjecture = the claim under attack: NOT(exists such a pair).
% find_counterexample searches for h,h' falsifying it = the refuting witness.
%
% n=8 fold cells T_d = XOR over submasks o of d of h[7-d+o]:
%   T2 = h5 xor h7          (d=2: {0,2} -> cols 5,7)
%   T3 = h4^h5^h6^h7        (d=3: {0,1,2,3} -> cols 4,5,6,7)
%   T4 = h3 xor h7          (d=4: {0,4} -> cols 3,7)
%   T5 = h2^h3^h6^h7        (d=5: {0,1,4,5} -> cols 2,3,6,7)
%   T6 = h1^h3^h5^h7        (d=6: {0,2,4,6} -> cols 1,3,5,7)
%   T7 = h0^h1^h2^h3^h4^h5^h6^h7   (d=7: all cols)
% S = 6 - 2*tot, tot = #{T_d=1, d=2..7} in {0..6}; S^2 values {36,16,4,0}.
% S^2(h) != S^2(h')  iff  tot(h) !in { tot(h'), 6 - tot(h') }.
% Equality of C_4 = equality of the multiset {W0,W1,W2,W3}, W_i = h[i..i+4],
% = exists a permutation p of {0,1,2,3} with W_i^h = W_{p(i)}^{h'} for all i.

% ================= h fold cells =================
fof(a_t2, axiom, ( t2 <=> ~( h5 <=> h7 ) )).
fof(a_c3a, axiom, ( c3a <=> ~( h4 <=> h5 ) )).
fof(a_c3b, axiom, ( c3b <=> ~( c3a <=> h6 ) )).
fof(a_t3, axiom, ( t3 <=> ~( c3b <=> h7 ) )).
fof(a_t4, axiom, ( t4 <=> ~( h3 <=> h7 ) )).
fof(a_c5a, axiom, ( c5a <=> ~( h2 <=> h3 ) )).
fof(a_c5b, axiom, ( c5b <=> ~( c5a <=> h6 ) )).
fof(a_t5, axiom, ( t5 <=> ~( c5b <=> h7 ) )).
fof(a_c6a, axiom, ( c6a <=> ~( h1 <=> h3 ) )).
fof(a_c6b, axiom, ( c6b <=> ~( c6a <=> h5 ) )).
fof(a_t6, axiom, ( t6 <=> ~( c6b <=> h7 ) )).
fof(a_s7a, axiom, ( s7a <=> ~( h0 <=> h1 ) )).
fof(a_s7b, axiom, ( s7b <=> ~( s7a <=> h2 ) )).
fof(a_s7c, axiom, ( s7c <=> ~( s7b <=> h3 ) )).
fof(a_s7d, axiom, ( s7d <=> ~( s7c <=> h4 ) )).
fof(a_s7e, axiom, ( s7e <=> ~( s7d <=> h5 ) )).
fof(a_s7f, axiom, ( s7f <=> ~( s7e <=> h6 ) )).
fof(a_t7, axiom, ( t7 <=> ~( s7f <=> h7 ) )).

% ================= h' fold cells =================
fof(b_t2, axiom, ( tp2 <=> ~( hp5 <=> hp7 ) )).
fof(b_c3a, axiom, ( cp3a <=> ~( hp4 <=> hp5 ) )).
fof(b_c3b, axiom, ( cp3b <=> ~( cp3a <=> hp6 ) )).
fof(b_t3, axiom, ( tp3 <=> ~( cp3b <=> hp7 ) )).
fof(b_t4, axiom, ( tp4 <=> ~( hp3 <=> hp7 ) )).
fof(b_c5a, axiom, ( cp5a <=> ~( hp2 <=> hp3 ) )).
fof(b_c5b, axiom, ( cp5b <=> ~( cp5a <=> hp6 ) )).
fof(b_t5, axiom, ( tp5 <=> ~( cp5b <=> hp7 ) )).
fof(b_c6a, axiom, ( cp6a <=> ~( hp1 <=> hp3 ) )).
fof(b_c6b, axiom, ( cp6b <=> ~( cp6a <=> hp5 ) )).
fof(b_t6, axiom, ( tp6 <=> ~( cp6b <=> hp7 ) )).
fof(b_s7a, axiom, ( sp7a <=> ~( hp0 <=> hp1 ) )).
fof(b_s7b, axiom, ( sp7b <=> ~( sp7a <=> hp2 ) )).
fof(b_s7c, axiom, ( sp7c <=> ~( sp7b <=> hp3 ) )).
fof(b_s7d, axiom, ( sp7d <=> ~( sp7c <=> hp4 ) )).
fof(b_s7e, axiom, ( sp7e <=> ~( sp7d <=> hp5 ) )).
fof(b_s7f, axiom, ( sp7f <=> ~( sp7e <=> hp6 ) )).
fof(b_t7, axiom, ( tp7 <=> ~( sp7f <=> hp7 ) )).

% ============ S^2 difference via tot ("exactly k of the six cells = 1") ====
% h: tot_h_eq_k means exactly k of {t2..t7} are true, k=0..6.
fof(dh0, axiom, ( th0 <=> ( ~t2 & ~t3 & ~t4 & ~t5 & ~t6 & ~t7 ) )).
fof(dh1, axiom, ( th1 <=> ( ( t2 & ~t3 & ~t4 & ~t5 & ~t6 & ~t7 )
                        | ( ~t2 & t3 & ~t4 & ~t5 & ~t6 & ~t7 )
                        | ( ~t2 & ~t3 & t4 & ~t5 & ~t6 & ~t7 )
                        | ( ~t2 & ~t3 & ~t4 & t5 & ~t6 & ~t7 )
                        | ( ~t2 & ~t3 & ~t4 & ~t5 & t6 & ~t7 )
                        | ( ~t2 & ~t3 & ~t4 & ~t5 & ~t6 & t7 ) ) )).
fof(dh2, axiom, ( th2 <=> ( ( t2 & t3 & ~t4 & ~t5 & ~t6 & ~t7 )
                        | ( t2 & ~t3 & t4 & ~t5 & ~t6 & ~t7 )
                        | ( t2 & ~t3 & ~t4 & t5 & ~t6 & ~t7 )
                        | ( t2 & ~t3 & ~t4 & ~t5 & t6 & ~t7 )
                        | ( t2 & ~t3 & ~t4 & ~t5 & ~t6 & t7 )
                        | ( ~t2 & t3 & t4 & ~t5 & ~t6 & ~t7 )
                        | ( ~t2 & t3 & ~t4 & t5 & ~t6 & ~t7 )
                        | ( ~t2 & t3 & ~t4 & ~t5 & t6 & ~t7 )
                        | ( ~t2 & t3 & ~t4 & ~t5 & ~t6 & t7 )
                        | ( ~t2 & ~t3 & t4 & t5 & ~t6 & ~t7 )
                        | ( ~t2 & ~t3 & t4 & ~t5 & t6 & ~t7 )
                        | ( ~t2 & ~t3 & t4 & ~t5 & ~t6 & t7 )
                        | ( ~t2 & ~t3 & ~t4 & t5 & t6 & ~t7 )
                        | ( ~t2 & ~t3 & ~t4 & t5 & ~t6 & t7 )
                        | ( ~t2 & ~t3 & ~t4 & ~t5 & t6 & t7 ) ) )).
fof(dh3, axiom, ( th3 <=> ( ( t2 & t3 & t4 & ~t5 & ~t6 & ~t7 )
                        | ( t2 & t3 & ~t4 & t5 & ~t6 & ~t7 )
                        | ( t2 & t3 & ~t4 & ~t5 & t6 & ~t7 )
                        | ( t2 & t3 & ~t4 & ~t5 & ~t6 & t7 )
                        | ( t2 & ~t3 & t4 & t5 & ~t6 & ~t7 )
                        | ( t2 & ~t3 & t4 & ~t5 & t6 & ~t7 )
                        | ( t2 & ~t3 & t4 & ~t5 & ~t6 & t7 )
                        | ( t2 & ~t3 & ~t4 & t5 & t6 & ~t7 )
                        | ( t2 & ~t3 & ~t4 & t5 & ~t6 & t7 )
                        | ( t2 & ~t3 & ~t4 & ~t5 & t6 & t7 )
                        | ( ~t2 & t3 & t4 & t5 & ~t6 & ~t7 )
                        | ( ~t2 & t3 & t4 & ~t5 & t6 & ~t7 )
                        | ( ~t2 & t3 & t4 & ~t5 & ~t6 & t7 )
                        | ( ~t2 & t3 & ~t4 & t5 & t6 & ~t7 )
                        | ( ~t2 & t3 & ~t4 & t5 & ~t6 & t7 )
                        | ( ~t2 & t3 & ~t4 & ~t5 & t6 & t7 )
                        | ( ~t2 & ~t3 & t4 & t5 & t6 & ~t7 )
                        | ( ~t2 & ~t3 & t4 & t5 & ~t6 & t7 )
                        | ( ~t2 & ~t3 & t4 & ~t5 & t6 & t7 )
                        | ( ~t2 & ~t3 & ~t4 & t5 & t6 & t7 ) ) )).
fof(dh4, axiom, ( th4 <=> ( ( t2 & t3 & t4 & t5 & ~t6 & ~t7 )
                        | ( t2 & t3 & t4 & ~t5 & t6 & ~t7 )
                        | ( t2 & t3 & t4 & ~t5 & ~t6 & t7 )
                        | ( t2 & t3 & ~t4 & t5 & t6 & ~t7 )
                        | ( t2 & t3 & ~t4 & t5 & ~t6 & t7 )
                        | ( t2 & t3 & ~t4 & ~t5 & t6 & t7 )
                        | ( t2 & ~t3 & t4 & t5 & t6 & ~t7 )
                        | ( t2 & ~t3 & t4 & t5 & ~t6 & t7 )
                        | ( t2 & ~t3 & t4 & ~t5 & t6 & t7 )
                        | ( t2 & ~t3 & ~t4 & t5 & t6 & t7 )
                        | ( ~t2 & t3 & t4 & t5 & t6 & ~t7 )
                        | ( ~t2 & t3 & t4 & t5 & ~t6 & t7 )
                        | ( ~t2 & t3 & t4 & ~t5 & t6 & t7 )
                        | ( ~t2 & t3 & ~t4 & t5 & t6 & t7 )
                        | ( ~t2 & ~t3 & t4 & t5 & t6 & t7 ) ) )).
fof(dh5, axiom, ( th5 <=> ( ( t2 & t3 & t4 & t5 & t6 & ~t7 )
                        | ( t2 & t3 & t4 & t5 & ~t6 & t7 )
                        | ( t2 & t3 & t4 & ~t5 & t6 & t7 )
                        | ( t2 & t3 & ~t4 & t5 & t6 & t7 )
                        | ( t2 & ~t3 & t4 & t5 & t6 & t7 )
                        | ( ~t2 & t3 & t4 & t5 & t6 & t7 ) ) )).
fof(dh6, axiom, ( th6 <=> ( t2 & t3 & t4 & t5 & t6 & t7 ) )).

% h': tot_p_eq_k
fof(dp0, axiom, ( tp0 <=> ( ~tp2 & ~tp3 & ~tp4 & ~tp5 & ~tp6 & ~tp7 ) )).
fof(dp1, axiom, ( tp1 <=> ( ( tp2 & ~tp3 & ~tp4 & ~tp5 & ~tp6 & ~tp7 )
                        | ( ~tp2 & tp3 & ~tp4 & ~tp5 & ~tp6 & ~tp7 )
                        | ( ~tp2 & ~tp3 & tp4 & ~tp5 & ~tp6 & ~tp7 )
                        | ( ~tp2 & ~tp3 & ~tp4 & tp5 & ~tp6 & ~tp7 )
                        | ( ~tp2 & ~tp3 & ~tp4 & ~tp5 & tp6 & ~tp7 )
                        | ( ~tp2 & ~tp3 & ~tp4 & ~tp5 & ~tp6 & tp7 ) ) )).
fof(dp2, axiom, ( tp2eq <=> ( ( tp2 & tp3 & ~tp4 & ~tp5 & ~tp6 & ~tp7 )
                        | ( tp2 & ~tp3 & tp4 & ~tp5 & ~tp6 & ~tp7 )
                        | ( tp2 & ~tp3 & ~tp4 & tp5 & ~tp6 & ~tp7 )
                        | ( tp2 & ~tp3 & ~tp4 & ~tp5 & tp6 & ~tp7 )
                        | ( tp2 & ~tp3 & ~tp4 & ~tp5 & ~tp6 & tp7 )
                        | ( ~tp2 & tp3 & tp4 & ~tp5 & ~tp6 & ~tp7 )
                        | ( ~tp2 & tp3 & ~tp4 & tp5 & ~tp6 & ~tp7 )
                        | ( ~tp2 & tp3 & ~tp4 & ~tp5 & tp6 & ~tp7 )
                        | ( ~tp2 & tp3 & ~tp4 & ~tp5 & ~tp6 & tp7 )
                        | ( ~tp2 & ~tp3 & tp4 & tp5 & ~tp6 & ~tp7 )
                        | ( ~tp2 & ~tp3 & tp4 & ~tp5 & tp6 & ~tp7 )
                        | ( ~tp2 & ~tp3 & tp4 & ~tp5 & ~tp6 & tp7 )
                        | ( ~tp2 & ~tp3 & ~tp4 & tp5 & tp6 & ~tp7 )
                        | ( ~tp2 & ~tp3 & ~tp4 & tp5 & ~tp6 & tp7 )
                        | ( ~tp2 & ~tp3 & ~tp4 & ~tp5 & tp6 & tp7 ) ) )).
fof(dp3, axiom, ( tp3eq <=> ( ( tp2 & tp3 & tp4 & ~tp5 & ~tp6 & ~tp7 )
                        | ( tp2 & tp3 & ~tp4 & tp5 & ~tp6 & ~tp7 )
                        | ( tp2 & tp3 & ~tp4 & ~tp5 & tp6 & ~tp7 )
                        | ( tp2 & tp3 & ~tp4 & ~tp5 & ~tp6 & tp7 )
                        | ( tp2 & ~tp3 & tp4 & tp5 & ~tp6 & ~tp7 )
                        | ( tp2 & ~tp3 & tp4 & ~tp5 & tp6 & ~tp7 )
                        | ( tp2 & ~tp3 & tp4 & ~tp5 & ~tp6 & tp7 )
                        | ( tp2 & ~tp3 & ~tp4 & tp5 & tp6 & ~tp7 )
                        | ( tp2 & ~tp3 & ~tp4 & tp5 & ~tp6 & tp7 )
                        | ( tp2 & ~tp3 & ~tp4 & ~tp5 & tp6 & tp7 )
                        | ( ~tp2 & tp3 & tp4 & tp5 & ~tp6 & ~tp7 )
                        | ( ~tp2 & tp3 & tp4 & ~tp5 & tp6 & ~tp7 )
                        | ( ~tp2 & tp3 & tp4 & ~tp5 & ~tp6 & tp7 )
                        | ( ~tp2 & tp3 & ~tp4 & tp5 & tp6 & ~tp7 )
                        | ( ~tp2 & tp3 & ~tp4 & tp5 & ~tp6 & tp7 )
                        | ( ~tp2 & tp3 & ~tp4 & ~tp5 & tp6 & tp7 )
                        | ( ~tp2 & ~tp3 & tp4 & tp5 & tp6 & ~tp7 )
                        | ( ~tp2 & ~tp3 & tp4 & tp5 & ~tp6 & tp7 )
                        | ( ~tp2 & ~tp3 & tp4 & ~tp5 & tp6 & tp7 )
                        | ( ~tp2 & ~tp3 & ~tp4 & tp5 & tp6 & tp7 ) ) )).
fof(dp4, axiom, ( tp4eq <=> ( ( tp2 & tp3 & tp4 & tp5 & ~tp6 & ~tp7 )
                        | ( tp2 & tp3 & tp4 & ~tp5 & tp6 & ~tp7 )
                        | ( tp2 & tp3 & tp4 & ~tp5 & ~tp6 & tp7 )
                        | ( tp2 & tp3 & ~tp4 & tp5 & tp6 & ~tp7 )
                        | ( tp2 & tp3 & ~tp4 & tp5 & ~tp6 & tp7 )
                        | ( tp2 & tp3 & ~tp4 & ~tp5 & tp6 & tp7 )
                        | ( tp2 & ~tp3 & tp4 & tp5 & tp6 & ~tp7 )
                        | ( tp2 & ~tp3 & tp4 & tp5 & ~tp6 & tp7 )
                        | ( tp2 & ~tp3 & tp4 & ~tp5 & tp6 & tp7 )
                        | ( tp2 & ~tp3 & ~tp4 & tp5 & tp6 & tp7 )
                        | ( ~tp2 & tp3 & tp4 & tp5 & tp6 & ~tp7 )
                        | ( ~tp2 & tp3 & tp4 & tp5 & ~tp6 & tp7 )
                        | ( ~tp2 & tp3 & tp4 & ~tp5 & tp6 & tp7 )
                        | ( ~tp2 & tp3 & ~tp4 & tp5 & tp6 & tp7 )
                        | ( ~tp2 & ~tp3 & tp4 & tp5 & tp6 & tp7 ) ) )).
fof(dp5, axiom, ( tp5eq <=> ( ( tp2 & tp3 & tp4 & tp5 & tp6 & ~tp7 )
                        | ( tp2 & tp3 & tp4 & tp5 & ~tp6 & tp7 )
                        | ( tp2 & tp3 & tp4 & ~tp5 & tp6 & tp7 )
                        | ( tp2 & tp3 & ~tp4 & tp5 & tp6 & tp7 )
                        | ( tp2 & ~tp3 & tp4 & tp5 & tp6 & tp7 )
                        | ( ~tp2 & tp3 & tp4 & tp5 & tp6 & tp7 ) ) )).
fof(dp6, axiom, ( tp6eq <=> ( tp2 & tp3 & tp4 & tp5 & tp6 & tp7 ) )).

% S^2 different  <=>  NOT( exists k : (th_k & tp_k) or (th_k & tp_{6-k}) )
fof(s2diff, axiom, ( s2diff <=> ~( ( (th0&tp0)|(th1&tp1)|(th2&tp2eq)|(th3&tp3eq)|(th4&tp4eq)|(th5&tp5eq)|(th6&tp6eq) )
                      | ( (th0&tp6eq)|(th1&tp5eq)|(th2&tp4eq)|(th3&tp3eq)|(th4&tp2eq)|(th5&tp1)|(th6&tp0) ) ) )).

% ============ Equal C_4: multiset of 5-gram windows equal ============ 
% windows of h: W_i = h[i..i+4], i=0..3; of h': Wp_i.
% e_ij = (W_i^h == W_j^{h'})
fof(e00, axiom, ( e00 <=> ( h0<=>hp0)&(h1<=>hp1)&(h2<=>hp2)&(h3<=>hp3)&(h4<=>hp4) )).
fof(e01, axiom, ( e01 <=> ( h0<=>hp1)&(h1<=>hp2)&(h2<=>hp3)&(h3<=>hp4)&(h4<=>hp5) )).
fof(e02, axiom, ( e02 <=> ( h0<=>hp2)&(h1<=>hp3)&(h2<=>hp4)&(h3<=>hp5)&(h4<=>hp6) )).
fof(e03, axiom, ( e03 <=> ( h0<=>hp3)&(h1<=>hp4)&(h2<=>hp5)&(h3<=>hp6)&(h4<=>hp7) )).
fof(e10, axiom, ( e10 <=> ( h1<=>hp0)&(h2<=>hp1)&(h3<=>hp2)&(h4<=>hp3)&(h5<=>hp4) )).
fof(e11, axiom, ( e11 <=> ( h1<=>hp1)&(h2<=>hp2)&(h3<=>hp3)&(h4<=>hp4)&(h5<=>hp5) )).
fof(e12, axiom, ( e12 <=> ( h1<=>hp2)&(h2<=>hp3)&(h3<=>hp4)&(h4<=>hp5)&(h5<=>hp6) )).
fof(e13, axiom, ( e13 <=> ( h1<=>hp3)&(h2<=>hp4)&(h3<=>hp5)&(h4<=>hp6)&(h5<=>hp7) )).
fof(e20, axiom, ( e20 <=> ( h2<=>hp0)&(h3<=>hp1)&(h4<=>hp2)&(h5<=>hp3)&(h6<=>hp4) )).
fof(e21, axiom, ( e21 <=> ( h2<=>hp1)&(h3<=>hp2)&(h4<=>hp3)&(h5<=>hp4)&(h6<=>hp5) )).
fof(e22, axiom, ( e22 <=> ( h2<=>hp2)&(h3<=>hp3)&(h4<=>hp4)&(h5<=>hp5)&(h6<=>hp6) )).
fof(e23, axiom, ( e23 <=> ( h2<=>hp3)&(h3<=>hp4)&(h4<=>hp5)&(h5<=>hp6)&(h6<=>hp7) )).
fof(e30, axiom, ( e30 <=> ( h3<=>hp0)&(h4<=>hp1)&(h5<=>hp2)&(h6<=>hp3)&(h7<=>hp4) )).
fof(e31, axiom, ( e31 <=> ( h3<=>hp1)&(h4<=>hp2)&(h5<=>hp3)&(h6<=>hp4)&(h7<=>hp5) )).
fof(e32, axiom, ( e32 <=> ( h3<=>hp2)&(h4<=>hp3)&(h5<=>hp4)&(h6<=>hp5)&(h7<=>hp6) )).
fof(e33, axiom, ( e33 <=> ( h3<=>hp3)&(h4<=>hp4)&(h5<=>hp5)&(h6<=>hp6)&(h7<=>hp7) )).

% multiset equality = exists permutation.  24 permutations listed explicitly.
fof(p00, axiom, ( m0  <=> ( e00&e11&e22&e33 ) )).
fof(p01, axiom, ( m1  <=> ( e00&e12&e21&e33 ) )).
fof(p02, axiom, ( m2  <=> ( e00&e13&e22&e31 ) )).
fof(p03, axiom, ( m3  <=> ( e00&e13&e21&e32 ) )).
fof(p04, axiom, ( m4  <=> ( e01&e10&e22&e33 ) )).
fof(p05, axiom, ( m5  <=> ( e01&e12&e20&e33 ) )).
fof(p06, axiom, ( m6  <=> ( e01&e13&e20&e32 ) )).
fof(p07, axiom, ( m7  <=> ( e01&e13&e22&e30 ) )).
fof(p08, axiom, ( m8  <=> ( e02&e10&e21&e33 ) )).
fof(p09, axiom, ( m9  <=> ( e02&e11&e20&e33 ) )).
fof(p10, axiom, ( m10 <=> ( e02&e13&e20&e31 ) )).
fof(p11, axiom, ( m11 <=> ( e02&e13&e21&e30 ) )).
fof(p12, axiom, ( m12 <=> ( e03&e10&e21&e32 ) )).
fof(p13, axiom, ( m13 <=> ( e03&e11&e20&e32 ) )).
fof(p14, axiom, ( m14 <=> ( e03&e12&e20&e31 ) )).
fof(p15, axiom, ( m15 <=> ( e03&e12&e21&e30 ) )).
fof(p16, axiom, ( m16 <=> ( e00&e11&e23&e32 ) )).
fof(p17, axiom, ( m17 <=> ( e00&e12&e23&e31 ) )).
fof(p18, axiom, ( m18 <=> ( e00&e13&e23&e30 ) )).
fof(p19, axiom, ( m19 <=> ( e00&e12&e23&e30 ) )).
fof(p20, axiom, ( m20 <=> ( e01&e10&e23&e32 ) )).
fof(p21, axiom, ( m21 <=> ( e01&e12&e23&e30 ) )).
fof(p22, axiom, ( m22 <=> ( e02&e10&e23&e31 ) )).
fof(p23, axiom, ( m23 <=> ( e01&e13&e20&e32 ) )).
fof(multeq, axiom, ( c4eq <=> ( m0|m1|m2|m3|m4|m5|m6|m7|m8|m9|m10|m11|m12|m13|m14|m15|m16|m17|m18|m19|m20|m21|m22|m23 ) )).

% Also require the two strings are not trivially the same string via identity
% (the interesting witness has h != h'); not strictly necessary but avoids the
% trivial answer.  Include: distinct.
fof(distinct, axiom, ~( (h0<=>hp0)&(h1<=>hp1)&(h2<=>hp2)&(h3<=>hp3)&(h4<=>hp4)&(h5<=>hp5)&(h6<=>hp6)&(h7<=>hp7) )).

% ============ CONJECTURE (the claim under attack): NO such pair ============
fof(goal, conjecture, ~( c4eq & s2diff )).
