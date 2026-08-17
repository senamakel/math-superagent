% Refutation of claim G2's STATED slope formula a = F(n-1)/F(n), at k=3.
%
% The Fibonacci word factor set of length 3 is {001,010,100,101} (given by the
% problem itself: Psi(3) uses exactly these four).  For k=3 we need F(n) > 3,
% so F(n)=5 and the claim's formula gives a = F(n-1)/F(n) = F(4)/F(5) = 3/5.
%
% Cutting the circle at { -m*a mod 1 : m=0..3 } with a=3/5 and reading the
% arc midpoints yields the words {010, 011, 101, 110} (computed by hand),
% which is NOT the true factor set: it contains 011 and 110 (which never occur
% as Fibonacci factors) and omits 001 and 100.
%
% Axioms encode the two ground sets; the conjecture is the claim G2's
% equivalence statement.  find_counterexample should find that 011 is in the
% mechanical set but not in the true factor set.

% --- true length-3 Fibonacci factors (problem-given) ---
fof(ax_true_in, axiom, (
    true_factor(w0_0_1) & true_factor(w0_1_0) &
    true_factor(w1_0_0) & true_factor(w1_0_1))).

fof(ax_true_out, axiom, (
    ~true_factor(w0_0_0) & ~true_factor(w0_1_1) &
    ~true_factor(w1_1_0) & ~true_factor(w1_1_1))).

% --- mechanical construction with a = 3/5 (claim's formula) ---
fof(ax_mech_in, axiom, (
    mech35(w0_1_0) & mech35(w0_1_1) &
    mech35(w1_0_1) & mech35(w1_1_0))).

fof(ax_mech_out, axiom, (
    ~mech35(w0_0_0) & ~mech35(w0_0_1) &
    ~mech35(w1_0_0) & ~mech35(w1_1_1))).

% Claim G2 as stated: the mechanical words equal the true factors.
fof(goal, conjecture, (! [W] : (mech35(W) <=> true_factor(W)))).
