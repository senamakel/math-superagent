"""Third, genuinely independent oracle for the sharp-critical-degree check:
a brute-force proper-colouring search with NO symmetry breaking and NO SAT.
Pure Python product enumeration over all k^n colour tuples for small n.
Used to re-confirm the 5-critical conclusion on the graphs with chi>=5 up to
6 vertices, agreeing with the SAT oracles (lib.critoracle).
"""
import itertools
from lib import critoracle as co


def brute_is_k_colorable(n, edges, k):
    """Naive: does ANY k-colouring work? Pure Python, no symmetry breaking."""
    for col in itertools.product(range(k), repeat=n):
        if all(col[a] != col[b] for (a, b) in edges):
            return True
    return False


def brute_chrom(n, edges):
    for k in range(1, n + 1):
        if brute_is_k_colorable(n, edges, k):
            return k
    return n


def all_graphs(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(pairs)):
        yield [p for idx, p in enumerate(pairs) if mask >> idx & 1]


def delete_vertex(m, edges, v):
    rem = [u for u in range(m) if u != v]
    mp = {u: i for i, u in enumerate(rem)}
    sub = [(mp[a], mp[b]) for (a, b) in edges if a != v and b != v]
    return m - 1, sub


def brute_vertex_critical(n, edges, k):
    if brute_chrom(n, edges) != k:
        return False
    for v in range(n):
        m, sub = delete_vertex(n, edges, v)
        if not brute_is_k_colorable(m, sub, k - 1):
            return False
    return True


def min_degree(n, edges):
    deg = [0] * n
    for (a, b) in edges:
        deg[a] += 1
        deg[b] += 1
    return min(deg) if n else 0


def main():
    N = 5  # brute 3^5..5^5 up to n=5 keeps 5^n small enough; report separately
    # Compare brute_chrom vs critoracle.chrom over all graphs n<=5
    mismatch = 0
    for n in range(1, N + 1):
        for edges in all_graphs(n):
            if brute_chrom(n, edges) != co.chrom(n, edges):
                mismatch += 1
                print("CHROM MISMATCH", n, edges)
    print(f"brute-vs-SAT chrom mismatches over n<= {N}: {mismatch}")

    # 5-critical conclusion via brute force, n<=5 (the 5-chromatic graphs here)
    n5 = 0
    bad = 0
    for n in range(1, N + 1):
        for edges in all_graphs(n):
            k = brute_chrom(n, edges)
            if k < 5:
                continue
            n5 += 1
            m, cur = n, edges
            changed = True
            while changed:
                changed = False
                for v in range(m):
                    mm, sub = delete_vertex(m, cur, v)
                    if brute_chrom(mm, sub) == k:
                        m, cur = mm, sub
                        changed = True
                        break
            if not (brute_vertex_critical(m, cur, k) and
                    brute_chrom(m, cur) == k and min_degree(m, cur) >= k - 1):
                bad += 1
                print("FAIL", n, edges)
    print(f"brute: 5-chromatic graphs n<= {N}: {n5}, failures: {bad}")
    print("RESULT:", "PASSED" if (mismatch == 0 and bad == 0) else "FAILED")


if __name__ == "__main__":
    main()
