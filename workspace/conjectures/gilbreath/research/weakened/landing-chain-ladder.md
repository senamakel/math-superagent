```ladder
goal: For A_0 = (2,3,5,7,11,...) the primes in order and A_{k+1}(i) = |A_k(i) - A_k(i+1)|, prove A_k(0) = 1 for every k >= 1 (Gilbreath's conjecture). By the proved step law (claim step-law-theorem-proved, b_1 = 2) this is exactly: the (2,4)-events at rows tau_1 < tau_2 < ... recharge the leading {0,2} block fast enough that sum_{i<m} (j_i + 1) >= tau_m - 2 for all m.
difficulties: infinite-horizon, uncontrolled-far-entries, two-step-arrival-unproved, prime-arrangement
status: open
```

```rung
id: R-halving-lipschitz
statement: For even nonnegative a,b, |a-b| in {0,2} if and only if |a/2 - b/2| <= 1. Equivalently, a child cell A_{k+1}(i) = |A_k(i) - A_k(i+1)| lies in {0,2} iff the halved parent entries h_k(i) = A_k(i)/2 and h_k(i+1) = A_k(i+1)/2 differ by at most 1. This is the exact bridge between the {0,2} block and the 1-Lipschitz property of the halved row.
off: infinite-horizon, uncontrolled-far-entries, two-step-arrival-unproved, prime-arrangement
stance: open
merge: one-line proof — for nonnegative u,v, |u-v| <= 1 iff 2|u-v| in {0,2} iff |2u-2v| in {0,2}, and the failure |u-v| >= 2 gives |2u-2v| = 2|u-v| >= 4. File it as a proved claim and Lean-formalise the even-domain bi-implication. Turning `uncontrolled-far-entries` back on is R-landing-lipschitz-prefix, which applies this equivalence at every column of the continuation past the block boundary.
```

```rung
id: R-landing-lipschitz-prefix
statement: At a (2,4)-event (edge x_k = A_k(b_k) = 2, intruder y_k = A_k(b_k+1) = 4), the landing jump j_k = b_{k+1} - b_k equals the length of the maximal 1-Lipschitz run of the halved parent row h_k = A_k/2 starting at the boundary pair (b_k, b_k+1): the number of consecutive indices i >= b_k with |h_k(i) - h_k(i+1)| <= 1 before the first adjacent pair with |h_k(i) - h_k(i+1)| >= 2. So the landing block b_{k+1} is exactly the 1-Lipschitz continuation of the halved row past the old boundary, and the jump is decided by how far right that continuation reaches before a 2-step.
off: infinite-horizon, two-step-arrival-unproved, prime-arrangement
stance: open
merge: compose R-halving-lipschitz with the proved step law (claim step-law-theorem-proved): the boundary pair (2,4) gives h_k(b_k)=1, h_k(b_k+1)=2, so A_{k+1}(b_k) = |2-4| = 2 lies in {0,2}, and each further child column is {0,2} exactly while its halved parent pair is 1-Lipschitz. This promotes the run's "giant-jump mechanism" from computed (depth 147, claim bigjump-cap-characterization-1000) to a theorem. Turning `two-step-arrival-unproved` back on is R-two-step-arrival-conditional: the run length, hence the jump, is the first-2-step hitting time in the halved chain.
```

```rung
id: R-two-step-arrival-conditional
statement: At a (2,4)-event with intruder 4 (so h_k(b_k+1) = 2), the jump is a stall j_k = 0 exactly when the next halved entry satisfies h_k(b_k+2) >= 4, i.e. A_k(b_k+2) >= 8 (equivalently |h_k(b_k+1) - h_k(b_k+2)| >= 2 at the very first step past the boundary); it is a non-stall j_k >= 1 exactly when A_k(b_k+2) in {2,4,6}. More generally, if the halved continuation contains an adjacent pair with |h_i - h_{i+1}| >= 2 within every window of length L (2-step arrival at rate 1/L), then 0 <= j_k <= L-1 and the stall condition is the single-column local fact above.
off: infinite-horizon, prime-arrangement
stance: open
merge: the local half (j=0 iff A_k(b_k+2) >= 8) is an immediate corollary of R-landing-lipschitz-prefix and is settleable now; the 2-step-arrival hypothesis is the genuinely open chain content. Discharge it for the primes by measuring the density of |h_i - h_{i+1}| >= 2 in the halved row at the recorded event rows (the run's "0-2/2-0 adjacency" data), then seek a theorem rather than a measurement. Turning `prime-arrangement` back on is R-events-infinitely-often: the primes' deterministic halved chain must actually realize 2-step arrival repeatedly.
```

```rung
id: R-events-infinitely-often
statement: For the prime triangle (A_0 = primes), (2,4)-events occur at infinitely many rows tau_1 < tau_2 < ..., i.e. the recharge sum sum_{i<m} (j_i + 1) is unbounded in m. This is the qualitative regeneration half of the conjecture: events keep arriving, with the quantitative budget (never falling tau_m - 2 behind) still switched off.
off: infinite-horizon
stance: open
merge: strictly weaker than the goal and not established — numeric only to depth 1000 (60 events, claim bigjump-cap-characterization-1000) and 15 giants to depth 400. First move: use R-landing-lipschitz-prefix + R-two-step-arrival-conditional to re-express "event fires at row k" as a finite local condition on the halved row, then ask whether the primes' halved chain hits it infinitely often. Turning `infinite-horizon` back on — from "unbounded recharge" to "recharge never falls tau_m - 2 behind" — is the full-strength goal.
```
