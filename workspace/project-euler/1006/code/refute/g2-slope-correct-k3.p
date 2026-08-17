% Check of the CORRECTED slope a = F(n-2)/F(n) = 2/5 for k=3 (the slope the
% implemented mech_psi.py actually uses: p = fib[-3] = F(n-2)).
% With a=2/5 the arc-midpoint words are {001,010,100,101}, which for k=3 IS
% the true factor set.  Conjecture should hold (no counterexample).

fof(ax_true_in, axiom, (
    true_factor(w0_0_1) & true_factor(w0_1_0) &
    true_factor(w1_0_0) & true_factor(w1_0_1))).
fof(ax_true_out, axiom, (
    ~true_factor(w0_0_0) & ~true_factor(w0_1_1) &
    ~true_factor(w1_1_0) & ~true_factor(w1_1_1))).

fof(ax_mech_in, axiom, (
    mech25(w0_0_1) & mech25(w0_1_0) &
    mech25(w1_0_0) & mech25(w1_0_1))).
fof(ax_mech_out, axiom, (
    ~mech25(w0_0_0) & ~mech25(w0_1_1) &
    ~mech25(w1_1_0) & ~mech25(w1_1_1))).

fof(goal, conjecture, (! [W] : (mech25(W) <=> true_factor(W)))).
