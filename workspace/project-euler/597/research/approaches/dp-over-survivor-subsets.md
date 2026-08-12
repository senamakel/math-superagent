# Approach: DP over survivor subsets with exact simplex-section transition probabilities

```approach
idea: Dynamic programming over the 2^n subsets of surviving (still-rowing) boats, with exact transition probabilities computed as simplex-section volumes using the Lasserre closed form.
mechanism: At any moment the state is the set S of boats still rowing. The next event is the earliest among |S| finish times and |S|(|S|−1)/2 bump times. All these times are ratios of linear forms in v, so the condition "event e is the earliest" defines a polyhedral cone in the positive orthant. After normalising v to the simplex, the probability of transition S → S\{j} (boat j finishes) or S → S\{i} (boat i bumps and is OUT) is an exact rational simplex-section volume — computable with the run's existing Lasserre-Latte machinery. The parity (±1) is a multiplicative weight that accumulates across transitions according to whether the new bump edge creates a new chain-pair (parity flips when the bumper i reaches a boat whose subtree contains an odd number of boats above the bumped boat k). The recursion is:

  F(S, parity_sign) = Σ_{j∈S} P(finish j | S) · F(S\{j}, parity_sign)
                    + Σ_{i<j∈S} P(bump i→j | S) · F(S\{i}, parity_sign ⊕ δ(i→j,S))

where δ(i→j,S) is the parity change from the new edge i→j given the existing bump-graph edges among S. The base case F(∅, p) = 1 if p = even else 0, and the answer is F({1..n}, even).

Number of states: 2^13 = 8192. Each state needs O(|S|²) transition probabilities, total ~640K integrals. But: (a) many transitions have probability 0 (deterministically, because the boat with the fastest finish-rate among surviving boats finishes before any bump can involve it); (b) the integrals for a given subset S depend only on the positions of boats in S and the finish-line distance, so the transition probabilities are rational functions of L; (c) if a closed-form rational expression for each transition probability can be derived (as a function of the active positions), the DP collapses to O(n·2^n) = O(10⁵) rational arithmetic operations — entirely feasible in exact arithmetic.
status: proposed
first-step: Derive and verify the exact transition probabilities for a 3-boat state (S = {a,b,c}) in closed rational form as functions of L, by the existing cell-exact machinery (code/cell_exact.py adapted to an arbitrary subset with arbitrary starting positions). Check against brute-force MC for 10³ random S and speed draws at n=5, L=1800.
```