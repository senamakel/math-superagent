% Attack: the multiplicative-order-for-8 worked example, as a structural claim
% the run's G-ord-criterion rests on.
%
% For k=8: ord_m(2) = 8  iff  m | 2^8 - 1 = 255 and m does not divide
% 2^d - 1 for any proper divisor d of 8.  The proper divisors of 8 are 1,2,4;
% 2^1-1=1, 2^2-1=3, 2^4-1=15.  So ord_m(2)=8 iff m|255 and m does not divide
% any of 1,3,15 -- i.e. m is not 1,3,5,15 (the divisors of 15).
%
% The genuine claim:  m | 255   and   NOT divides any proper-power-2-free divisor
% of 15  =>  ord_m(2)=8.  We encode the finite outcome set {17,51,85,255} implied
% by m | 255 with m coprime to 15 (so 3,5 not dividing m).
%
% 255 = 3*5*17.  If m | 255 and 3 !| m and 5 !| m, then m | 17, so m = 1 or 17.
% m=17 -> ord=8.  So m=17 (=> n=18) is the only such deck beyond the formula.
%
% Below we encode a FINITE algebraic model: a monoid (units of ZMod m) with a
% distinguished element a=2, binary op g, identity e, and the claim that the
% least n>0 with g-power = e is 8.  A finite model where axioms hold but the
% order is not 8 falsifies the worked example.
% We work with m=17: g = multiplication mod 17 on units {1,2,..,16}, a = 2.
% order of 2 mod 17 is 8:  2^8 = 256 = 1 (mod 17);  2^1..2^4 = 2,4,8,16 != 1.

fof(units_distinct, axiom,
    ! [X] : (g(e,X) = X & g(X,e) = X)).            % e neutral
fof(a_not_e, axiom, ~ (a = e)).                      % 2 != 1
fof(a2, axiom, g(a,a) = a2).                         % 4
fof(a3, axiom, g(g(a,a),a) = a3).                    % 8
fof(a4, axiom, g(g(g(a,a),a),a) = a4).               % 16
fof(a8, axiom, g(g(g(g(a,a),a),a),g(g(g(a,a),a),a)) = e).
% conjecture: least power giving e is exactly 8 (no lower power does).
fof(goal, conjecture,
    ~ (a = e) & ~ (g(a,a) = e) & ~ (g(g(a,a),a) = e) & ~ (g(g(g(a,a),a),a) = e)).
