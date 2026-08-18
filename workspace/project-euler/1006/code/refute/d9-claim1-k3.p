% Refutation check of steering-directive 9, Claim 1, at its own k=3 example.
%
% Claim 1: the k+1 DISTINCT length-k factors of the Fibonacci word are exactly
% the k+1 contiguous windows at positions r = F_n-k-1 .. F_n-1 of the doubled
% standard word q_n q_n.  For k=3, n=4: F_4=5, q_4=01001, q_4 q_4=0100101001.
% The windows at positions r = 5-3-1 .. 5-1 = 1..4 are the length-3 substrings
% 100, 001, 010, 101.
%
% The TRUE length-3 Fibonacci factor set (problem-given, used for Psi(3)=20302)
% is {001, 010, 100, 101}.
%
% Axioms fix the two ground sets (the true factors, and the claim-1 windows).
% The conjecture is claim-1's assertion that the two sets are equal.  If claim 1
% were FALSE at this k there would be a word in one set but not the other, and
% find_counterexample would produce a model.  Expected outcome (claim true):
% "proved from these axioms" / no counterexample found.

% --- true length-3 Fibonacci factors (problem-given) ---
fof(ax_true_in, axiom, (
    true_factor(w0_0_1) & true_factor(w0_1_0) &
    true_factor(w1_0_0) & true_factor(w1_0_1))).
fof(ax_true_out, axiom, (
    ~true_factor(w0_0_0) & ~true_factor(w0_1_1) &
    ~true_factor(w1_1_0) & ~true_factor(w1_1_1))).

% --- directive-9 claim-1 windows at positions 1..4 of q_4 q_4 = 0100101001 ---
% q_4 q_4 = 010 010 100 1 -> indices: 0=0,1=1,2=0,3=0,4=1,5=0,6=1,7=0,8=0,9=1
%   window@1 = idx1..3 = 100
%   window@2 = idx2..4 = 001
%   window@3 = idx3..5 = 010
%   window@4 = idx4..6 = 101
fof(ax_claim_in, axiom, (
    claim_window(w1_0_0) & claim_window(w0_0_1) &
    claim_window(w0_1_0) & claim_window(w1_0_1))).
fof(ax_claim_out, axiom, (
    ~claim_window(w0_0_0) & ~claim_window(w0_1_1) &
    ~claim_window(w1_1_0) & ~claim_window(w1_1_1))).

% The four words 001,010,100,101 are genuinely DISTINCT strings.  The engine
% otherwise collapses them into one domain element and trivially falsifies the
% equivalence (a degeneracy artifact, not a counterexample).  Assert pairwise
% distinctness of the distinct words.
fof(ax_word_distinct, axiom, (
    w0_0_1 != w0_1_0 & w0_0_1 != w1_0_0 & w0_0_1 != w1_0_1 &
    w0_1_0 != w1_0_0 & w0_1_0 != w1_0_1 &
    w1_0_0 != w1_0_1 )).

% The claim is about the set of all length-3 binary words (8 of them).  Bound
% the conjecture to exactly these eight words so the finite-model finder cannot
% introduce arbitrary extra domain elements.
fof(ax_is_word, axiom, (
    is_word(w0_0_0) & is_word(w0_0_1) & is_word(w0_1_0) & is_word(w0_1_1) &
    is_word(w1_0_0) & is_word(w1_0_1) & is_word(w1_1_0) & is_word(w1_1_1))).
% (the four given words are already pairwise distinct in ax_word_distinct)

% Claim 1: the claim-1 window set equals the true factor set, over the words.
fof(goal, conjecture, (! [W] : (is_word(W) => (claim_window(W) <=> true_factor(W))))).
