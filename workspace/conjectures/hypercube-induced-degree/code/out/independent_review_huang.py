import itertools
import math
import random
import numpy as np
np.set_printoptions(linewidth=200)

def build_A(n):
    A = np.array([[0, 1], [1, 0]], dtype=float)
    for _ in range(1, n):
        N = A.shape[0]
        top = np.hstack([A, np.eye(N, dtype=float)])
        bot = np.hstack([np.eye(N, dtype=float), -A])
        A = np.vstack([top, bot])
    return A

def all_admissible(n):
    N = 2**n
    M = 2**(n-1) + 1
    for combo in itertools.combinations(range(N), M):
        yield list(combo)

failures = 0
total_sets = 0

for n in range(1, 5):
    A = build_A(n)
    N = A.shape[0]
    M = 2**(n-1) + 1
    diff = A @ A - n * np.eye(N)
    assert np.allclose(diff, 0), f"n={n}: A_n^2 != n I"
    assert np.all(np.diag(A) == 0), f"n={n}: nonzero diagonal"
    assert set(np.unique(A)) <= {0.0, 1.0, -1.0}, f"n={n}: entries not in {{0,+-1}}"
    w = np.linalg.eigvalsh(A)
    sq = math.sqrt(n)
    pos = np.sum(w > sq - 1e-9)
    neg = np.sum(w < -sq + 1e-9)
    assert pos == 2**(n-1) and neg == 2**(n-1), f"n={n}: spectrum mult wrong {pos},{neg}"

    cnt = 0
    for S in all_admissible(n):
        B = A[np.ix_(S, S)]
        lmax = np.linalg.eigvalsh(B)[-1]
        degs = np.sum(B != 0, axis=1)
        D = int(degs.max())
        assert lmax <= D + 1e-9, f"n={n}: lam_max {lmax} > D(S) {D}"
        assert lmax >= sq - 1e-9, f"n={n}: interlacing failed lam_max {lmax} < sqrt(n) {sq}"
        assert D >= sq - 1e-9, f"n={n}: D(S) {D} < sqrt(n)"
        cnt += 1
    total_sets += cnt
    print(f"n={n}: A_n^2=nI ok, spectrum ok; checked all {cnt} admissible sets: "
          f"lam_max>=sqrt(n) and lam_max<=D(S) hold")

random.seed(0)
for n in (5, 6):
    A = build_A(n)
    N = A.shape[0]
    M = 2**(n-1) + 1
    sq = math.sqrt(n)
    ok = 0
    trials = 3000 if n == 5 else 500
    for _ in range(trials):
        S = random.sample(range(N), M)
        B = A[np.ix_(S, S)]
        lmax = np.linalg.eigvalsh(B)[-1]
        degs = np.sum(B != 0, axis=1)
        D = int(degs.max())
        if not (lmax <= D + 1e-9 and lmax >= sq - 1e-9 and D >= sq - 1e-9):
            print(f"  n={n}: FAIL on sample lmax={lmax} D={D}")
            failures += 1
        else:
            ok += 1
    print(f"n={n}: {ok}/{trials} random admissible sets satisfy both legs")
    total_sets += trials

print(f"\nTOTAL sets checked: {total_sets}; failures: {failures}")
print("Interlacing bound lambda_max >= sqrt(n) confirmed on every set checked;")
print("degree bound lambda_max <= D(S) confirmed on every set checked.")
