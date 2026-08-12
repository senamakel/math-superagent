"""Moore-bound threshold for avoiding power-of-two cycle lengths.

A counterexample to the Erdos-Gyarfas conjecture (min-degree-3, no 2-power
cycle) must in particular have no cycle of length 4, 8, 16, ...  Avoiding all
2-powers <= 2^m requires girth >= 2^m + 1.  The Moore bound says a graph with
minimum degree d and girth g has at least 1 + d*sum_{i=0}^{r-1}(d-1)^i vertices,
where r = floor((g-1)/2), because a BFS ball of radius r around any vertex is a
regular tree (no two vertices at distance < g can share an edge, else a cycle
shorter than g forms).

For d=3 and g = 2^m+1, r = 2^(m-1), so
    n_min(m) = 1 + 3*sum_{i=0}^{2^(m-1)-1} 2^i = 3*2^(2^(m-1)) - 2.

This is a THEOREM (Moore bound), closed form checked here against the direct
geometric sum.  Reported so the run has the exact vertex threshold at which
clearing each successive 2-power barrier becomes possible.
"""


def moore_sum(d, g):
    r = (g - 1) // 2
    return 1 + d * sum((d - 1) ** i for i in range(r))


def closed_form(m):
    return 3 * (2 ** (2 ** (m - 1))) - 2


def main():
    print("avoid 2-powers<=2^m | min girth | Moore n_min (d=3) | closed 3*2^(2^(m-1))-2 | ok")
    for m in range(2, 8):
        g = 2**m + 1
        n = moore_sum(3, g)
        cf = closed_form(m)
        print(f"  m={m} (<=2^{m}) | {g:>5} | {n:>14} | {cf:>14} | {n == cf}")
    print()
    print("Sequence of thresholds:", [moore_sum(3, 2**m + 1) for m in range(2, 8)])


if __name__ == "__main__":
    main()
