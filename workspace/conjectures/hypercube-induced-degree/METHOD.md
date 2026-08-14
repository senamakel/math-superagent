Solve by extremal combinatorics on the hypercube, with a solver-backed exact
oracle underneath every claim. The deliverable is a proof or a proved partial
result, not a computation, but no conjecture is worth stating until f(n) is
known exactly for as many n as a SAT or ILP encoding can reach.

The oracle for this problem is a decision procedure — given n and d, is there a
subset S of {0,1}^n with |S| = 2^(n-1)+1 and maximum internal degree at most d?
— together with a direct checker that takes an explicit S and returns its full
internal degree distribution.

Never enumerate subsets. The search space is doubly exponential and the problem
is a constraint satisfaction instance, not a search.
