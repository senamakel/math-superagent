#!/usr/bin/env python3
"""Build an S subset of Q_n of size 2^{n-1}+1 with every internal degree <= d=4.

Question folder for the gap between c log n and sqrt(n): we test whether the
hypercube Q_n admits a subset S with |S| = 2^{n-1}+1 whose internal-degree
maximum is at most d=4, for n=10 and n=11. Feasibility at d=4 gives an upper
bound f(n) <= 4 (a constant), a counterexample to f(n) = ceil(sqrt n).

Method: CP-SAT decision problem. N=2^n boolean vars x[v]; sum(x)==m forces
|S|=m; for every v the constraint sum(x[u] for u adjacent to v) <= d bounds the
internal degree. This is exactly the decision form of f_exact(n) <= d from
GOAL.md. It costs O(N) vars and O(n*N) linear constraints; feasible n=10 is
2^10 vars, n=11 is 2^11 vars — a polynomial-size ILP instance, not an
enumeration of subsets.
"""

from ortools.sat.python import cp_model


def max_degree(S, n):
    """Full internal degree distribution of S inside Q_n.

    S: set of ints (vertices of Q_n = bitstrings of length n).
    Returns (max_deg, Counter of degrees). Vertex v's internal degree is the
    number of u in S at Hamming distance 1 from v.
    """
    from collections import Counter
    deg = Counter()
    for v in S:
        c = 0
        for k in range(n):
            if (v ^ (1 << k)) in S:
                c += 1
        deg[c] += 1
    return (max(deg) if deg else 0, deg)


def solve(n, d, timeout_seconds=540):
    N = 1 << n
    m = (1 << (n - 1)) + 1
    model = cp_model.CpModel()
    x = [model.NewBoolVar(f"x{i}") for i in range(N)]
    model.Add(sum(x) == m)
    for v in range(N):
        model.Add(sum(x[v ^ (1 << k)] for k in range(n)) <= d)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = timeout_seconds
    status = solver.Solve(model)
    feasible = status in (cp_model.OPTIMAL, cp_model.FEASIBLE)
    S = None
    if feasible:
        S = {v for v in range(N) if solver.Value(x[v]) == 1}
    return feasible, status, S


def main():
    results = {}
    for n in (10, 11):
        d = 4
        feasible, status, S = solve(n, d)
        results[n] = (feasible, status, S)
        line = f"n={n} d={d} feasible={feasible} status={status}"
        print(line, flush=True)
        if feasible:
            (mx, dist) = max_degree(S, n)
            print(f"  |S|={len(S)} max_internal_deg={mx} degree_distribution={dict(sorted(dist.items()))}", flush=True)
            if n == 10:
                with open("/workspace/code/out/witness_n10.txt", "w") as f:
                    for v in sorted(S):
                        f.write(f"{v:0{n}b}\n")
                print("  wrote /workspace/code/out/witness_n10.txt", flush=True)
        else:
            # infeasible would be a counterexample to f(n) = ceil(sqrt n)
            print(f"  *** INFEASIBLE at d={d}: f({n}) > {d} (counterexample) ***", flush=True)

    ok = all(results[n][0] for n in (10, 11))
    print("ALL_FEASIBLE_AT_D4" if ok else "SOME_INFEASIBLE", flush=True)


if __name__ == "__main__":
    main()
