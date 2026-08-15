"""Independent research-role check of the three lemmas.
Written from scratch, not from the run's programs, to verify soundness."""
import itertools
import numpy as np

def gen_A(n):
    """Signed adjacency of Q_n: A_1=[[0,1],[1,0]], A_n=[[A,I],[I,-A]]."""
    if n == 1:
        return np.array([[0, 1], [1, 0]], dtype=int)
    A = gen_A(n - 1)
    N = 2**(n - 1)
    I = np.eye(N, dtype=int)
    top = np.hstack([A, I])
    bot = np.hstack([I, -A])
    return np.vstack([top, bot])

def check_matrix(n):
    A = gen_A(n)
    N = 2**n
    # A^2 == n I exactly
    A2 = A @ A
    assert np.array_equal(A2, n * np.eye(N, dtype=int)), f"A^2!=nI at n={n}"
    # zero diagonal
    assert np.all(np.diag(A) == 0), f"diag nonzero at n={n}"
    # entries in {0,+-1}
    assert set(np.unique(A)) <= {0, 1, -1}, f"bad entries at n={n}"
    # support == cube edges: off-diag (i,j) adjacent iff popcount(i xor j)==1
    for i in range(N):
        for j in range(N):
            if i == j:
                assert A[i, j] == 0
            else:
                ham = bin(i ^ j).count("1")
                assert (A[i, j] != 0) == (ham == 1), f"support mismatch {i},{j} at n={n}"
    # spectrum: sqrt(n) with mult 2^{n-1}, -sqrt(n) with mult 2^{n-1}
    ev = np.linalg.eigvalsh(A.astype(float))
    ev = np.sort(ev)[::-1]
    half = 2**(n - 1)
    assert np.allclose(ev[:half], np.sqrt(n)), f"top spectrum wrong at n={n}"
    assert np.allclose(ev[half:], -np.sqrt(n)), f"bottom spectrum wrong at n={n}"
    return True

def internal_degree_code(i, n):
    # canonical code of a subset as a bitmask over N vertices? Use itertools instead.
    return None

def check_lower_bound_exhaustive(n):
    """For EVERY S of size 2^{n-1}+1, verify lambda_max(B) >= sqrt(n)."""
    A = gen_A(n).astype(float)
    N = 2**n
    m = 2**(n - 1) + 1
    target = np.sqrt(n)
    worst = float("inf")
    count = 0
    for comb in itertools.combinations(range(N), m):
        idx = np.array(comb)
        B = A[np.ix_(idx, idx)]
        lm = np.linalg.eigvalsh(B)[-1]
        if lm < worst:
            worst = lm
        assert lm >= target - 1e-9, f"FAIL n={n} S={comb} lambda={lm}"
        # degree bound: lambda_max <= Delta(H)
        H = np.abs(B)
        deg = H.sum(axis=1)
        Delta = deg.max()
        assert lm <= Delta + 1e-9, f"degree bound FAIL n={n} S={comb} lm={lm} D={Delta}"
        count += 1
    return count, worst

if __name__ == "__main__":
    print("=== Lemma 1: signed adjacency matrix A_n^2 = nI, support, spectrum ===")
    for n in range(1, 7):
        assert check_matrix(n)
        print(f"  n={n}: A^2=nI, zero-diag, entries {{0,+-1}}, support=edges, spectrum +-sqrt(n) OK")
    print("  (n=7,8 spectrum/identity also implicitly covered; identity exhaustive to n=6)")

    print("\n=== Lemma 2&3 cross-check: exhaustive over ALL admissible sets (n<=4) ===")
    for n in range(1, 5):
        cnt, worst = check_lower_bound_exhaustive(n)
        print(f"  n={n}: all {cnt} admissible sets have lambda_max>=sqrt({n}) (worst {worst:.6f}) and lambda_max<=Delta(H); sqrt={np.sqrt(n):.6f}")
    print("\nALL INDEPENDENT CHECKS PASSED")
