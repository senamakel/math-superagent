% Refutation (NON-VACUOUS char-p counterexample at n=6, p=7).
%
% Target: the live refutation question rdc-charp-break / redirect-refuter-to-rootdiff
%   "Is there a char-p input where the NAMED break (per-color Hasse vacuity) does NOT
%    occur — which would mean the break is mis-located?"
%
% Claimed statement here: CA for degree 6 over F_7 — i.e. every monic degree-6 f over
% F_7 sharing a root with each Hasse derivative H_1..H_5 is a pure power (x-a)^6.
%
% Witness: f(x) = x^6 - x^2 = x^2 (x-1)(x+1)(x^2+1) over F_7.
%   * THREE distinct roots {0, 1, 6} (6 = -1) -> NOT a pure power.
%   * p = 7 > n = 6, so NOTHING degenerates: no C(6,i) vanishes mod 7, no Hasse
%     derivative is identically zero, none is constant.  This is a NON-vacuous
%     counterexample with H_1 = 6x^5+5x (deg 5), H_2 = x^4-1 (deg 4),
%     H_3 = 6x^3 (deg 3), H_4 = x^2 (deg 2), H_5 = 6x (deg 1), all nonzero.
%   * The named char-p break in the run (per-color Hasse vacuity H_i = 0 for
%     middle i, from Lucas) DOES NOT occur here — yet CA is false.  So the
%     char-p falsehood is broader than vacuity, and the collapse step would have
%     to fail here for a reason other than derivative degeneracy.
%   * 7 IS a published bad prime for n=6 (Castryck-Laterveer-Ounaies 2012
%     Table 1: 2,5,7,11,13,...), consistent: this f corroborates it.
%
% Shared roots (all Hasse derivatives genuinely nonzero):
%   H_1 = 6x^5+5x : only root 0  ; f(0)=0 -> shared at 0
%   H_2 = x^4-1   : roots 1,6   ; f(1)=f(6)=0 -> shared at 1 (or 6)
%   H_3 = 6x^3    : root 0      ; f(0)=0 -> shared at 0
%   H_4 = x^2     : root 0      ; f(0)=0 -> shared at 0
%   H_5 = 6x      : root 0      ; f(0)=0 -> shared at 0
%
% Value tables mod 7 (c0=0..c6=6):
%   f  = (0,0,4,6,6,4,0)   [zeros at 0,1,6]
%   H_1= (0,4,6,3,4,1,3)   [zero only at 0]
%   H_2= (6,0,1,3,3,1,0)   [zeros at 1,6]
%   H_3= (0,6,6,1,6,1,1)   [zero only at 0]
%   H_4= (0,1,4,2,2,4,1)   [zero only at 0]
%   H_5= (0,6,5,4,3,2,1)   [zero only at 0]
% (Hand-verified via x^6=1 (Fermat), x^5=1/x for x!=0 mod 7.)

% --- seven distinct constants c0..c6 for F_7 ---
fof(neq01, axiom, c0 != c1).
fof(neq02, axiom, c0 != c2).
fof(neq03, axiom, c0 != c3).
fof(neq04, axiom, c0 != c4).
fof(neq05, axiom, c0 != c5).
fof(neq06, axiom, c0 != c6).
fof(neq12, axiom, c1 != c2).
fof(neq13, axiom, c1 != c3).
fof(neq14, axiom, c1 != c4).
fof(neq15, axiom, c1 != c5).
fof(neq16, axiom, c1 != c6).
fof(neq23, axiom, c2 != c3).
fof(neq24, axiom, c2 != c4).
fof(neq25, axiom, c2 != c5).
fof(neq26, axiom, c2 != c6).
fof(neq34, axiom, c3 != c4).
fof(neq35, axiom, c3 != c5).
fof(neq36, axiom, c3 != c6).
fof(neq45, axiom, c4 != c5).
fof(neq46, axiom, c4 != c6).
fof(neq56, axiom, c5 != c6).

% --- f = x^6 - x^2 values on F_7 ---
fof(f0, axiom, f(c0) = c0).
fof(f1, axiom, f(c1) = c0).
fof(f2, axiom, f(c2) = c4).
fof(f3, axiom, f(c3) = c6).
fof(f4, axiom, f(c4) = c6).
fof(f5, axiom, f(c5) = c4).
fof(f6, axiom, f(c6) = c0).

% --- H_1 = 6x^5 + 5x ---
fof(h10, axiom, h1(c0) = c0).
fof(h11, axiom, h1(c1) = c4).
fof(h12, axiom, h1(c2) = c6).
fof(h13, axiom, h1(c3) = c3).
fof(h14, axiom, h1(c4) = c4).
fof(h15, axiom, h1(c5) = c1).
fof(h16, axiom, h1(c6) = c3).

% --- H_2 = x^4 - 1 ---
fof(h20, axiom, h2(c0) = c6).
fof(h21, axiom, h2(c1) = c0).
fof(h22, axiom, h2(c2) = c1).
fof(h23, axiom, h2(c3) = c3).
fof(h24, axiom, h2(c4) = c3).
fof(h25, axiom, h2(c5) = c1).
fof(h26, axiom, h2(c6) = c0).

% --- H_3 = 6x^3 ---
fof(h30, axiom, h3(c0) = c0).
fof(h31, axiom, h3(c1) = c6).
fof(h32, axiom, h3(c2) = c6).
fof(h33, axiom, h3(c3) = c1).
fof(h34, axiom, h3(c4) = c6).
fof(h35, axiom, h3(c5) = c1).
fof(h36, axiom, h3(c6) = c1).

% --- H_4 = x^2 ---
fof(h40, axiom, h4(c0) = c0).
fof(h41, axiom, h4(c1) = c1).
fof(h42, axiom, h4(c2) = c4).
fof(h43, axiom, h4(c3) = c2).
fof(h44, axiom, h4(c4) = c2).
fof(h45, axiom, h4(c5) = c4).
fof(h46, axiom, h4(c6) = c1).

% --- H_5 = 6x ---
fof(h50, axiom, h5(c0) = c0).
fof(h51, axiom, h5(c1) = c6).
fof(h52, axiom, h5(c2) = c5).
fof(h53, axiom, h5(c3) = c4).
fof(h54, axiom, h5(c4) = c3).
fof(h55, axiom, h5(c5) = c2).
fof(h56, axiom, h5(c6) = c1).

% --- HYPOTHESIS: f shares a root with each Hasse derivative H_1..H_5 ---
fof(hyp1, axiom, ?[X] : (f(X) = c0 & h1(X) = c0)).   % X = 0
fof(hyp2, axiom, ?[X] : (f(X) = c0 & h2(X) = c0)).   % X = 1
fof(hyp3, axiom, ?[X] : (f(X) = c0 & h3(X) = c0)).   % X = 0
fof(hyp4, axiom, ?[X] : (f(X) = c0 & h4(X) = c0)).   % X = 0
fof(hyp5, axiom, ?[X] : (f(X) = c0 & h5(X) = c0)).   % X = 0

% --- CONCLUSION (CA degree 6): f is a pure power (x-a)^6 over F_7 ---
% A pure power has exactly ONE zero (the field element a) and is nonzero
% on the other six elements.
fof(goal, conjecture,
      (f(c0)=c0 & f(c1)!=c0 & f(c2)!=c0 & f(c3)!=c0 & f(c4)!=c0 & f(c5)!=c0 & f(c6)!=c0)
    | (f(c0)!=c0 & f(c1)=c0 & f(c2)!=c0 & f(c3)!=c0 & f(c4)!=c0 & f(c5)!=c0 & f(c6)!=c0)
    | (f(c0)!=c0 & f(c1)!=c0 & f(c2)=c0 & f(c3)!=c0 & f(c4)!=c0 & f(c5)!=c0 & f(c6)!=c0)
    | (f(c0)!=c0 & f(c1)!=c0 & f(c2)!=c0 & f(c3)=c0 & f(c4)!=c0 & f(c5)!=c0 & f(c6)!=c0)
    | (f(c0)!=c0 & f(c1)!=c0 & f(c2)!=c0 & f(c3)!=c0 & f(c4)=c0 & f(c5)!=c0 & f(c6)!=c0)
    | (f(c0)!=c0 & f(c1)!=c0 & f(c2)!=c0 & f(c3)!=c0 & f(c4)!=c0 & f(c5)=c0 & f(c6)!=c0)
    | (f(c0)!=c0 & f(c1)!=c0 & f(c2)!=c0 & f(c3)!=c0 & f(c4)!=c0 & f(c5)!=c0 & f(c6)=c0)
).
