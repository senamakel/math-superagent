"""Mechanical verification of the spectral chain in
research/backward/spectral-interlacing-sqrt-lower-bound.md

This is exactly Hao Huang's proof of the Sensitivity Conjecture; the three
lemmas are:

  G-signed-adjacency-matrix:  A_n symmetric over {0,+-1}, support = cube
      edges, A_n^2 = n*I, spectrum +-sqrt(n) (multiplicity 2^{n-1} each).
  G-interlacing-sqrt:         any principal submatrix B = A_n[S,S] on
      |S| = 2^{n-1}+1 rows has lambda_max(B) >= sqrt(n).
  G-eigenvalue-bounds-degree: lambda_max(B) <= Delta(H) for the induced
      subgraph H = Q_n[S].

Program parts:
  (1) exact sympy: A_n^2 == n*I for n=1..8, zero diagonal, support == edge set.
  (2) full spectrum of A_n for n=2..10 (sympy eigenvals small, numpy larger),
      confirmed eigenvalues are +-sqrt(n).
  (3) interlacing: for n=2..10, several random principal submatrices B on
      |S| = 2^{n-1}+1 rows, report whether lambda_max(B) >= sqrt(n) always.
  (4) quadratic-form/degree claim: for these same S, compute Delta(H) from the
      internal degree distribution and report lambda_max(B) <= Delta(H).

Exact integer arithmetic throughout parts (1) and the degree computation;
numerical only for spectra and lambda_max (floats, so compared with a
tolerance). Run as:
  timeout 540 python3 code/spectral_verify.py 2>&1 | tee code/out/huang_spectral.captured.txt
"""

import sympy as sp
import numpy as np
import math
import time

from lib.huang import huang_matrix, huang_matrix_np
from lib.qcube import is_edge, max_internal_degree


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def part1_exact_square_support(nmax=8):
    section("PART 1 — exact sympy: A_n^2 == n*I, zero diagonal, support == cube edges")
    all_ok = True
    for n in range(1, nmax + 1):
        t0 = time.time()
        A = huang_matrix(n)
        N = 1 << n
        M = A * A
        ok_square = (M == n * sp.eye(N))
        ok_diag = all(A[i, i] == 0 for i in range(N))
        # support check: (u,v) adjacent in Q_n iff A[u,v] != 0
        ok_support = True
        for u in range(N):
            for v in range(N):
                expect_nonzero = is_edge(u, v)
                val = A[u, v]
                if expect_nonzero:
                    if val == 0:
                        ok_support = False
                        break
                else:
                    if val != 0:
                        ok_support = False
                        break
            if not ok_support:
                break
        all_ok = all_ok and ok_square and ok_diag and ok_support
        print(f"n={n:2d} N=2^{n}={N:4d} A^2==n*I:{str(ok_square):5s} "
              f"zero-diag:{str(ok_diag):5s} support==edges(Q_n):{str(ok_support):5s} "
              f"({time.time()-t0:.1f}s)")
    print(f"\nPART 1 overall: {'ALL OK' if all_ok else 'FAILED'}")


def part2_spectrum(nmin=2, nmax=10):
    section("PART 2 — full spectrum of A_n, confirm eigenvalues are +-sqrt(n)")
    for n in range(nmin, nmax + 1):
        t0 = time.time()
        s = math.sqrt(n)
        s_exact = sp.sqrt(n)   # exact, so n=4 simplifies sqrt(4)=2
        if n <= 7:
            A = huang_matrix(n)
            evmap = A.eigenvals()
            # dedup into list of distinct eigenvalues with multiplicity
            pairs = [(sp.simplify(k), int(v)) for k, v in evmap.items()]
            mult_plus = mult_minus = 0
            distinct_ok = True
            for lam, m in pairs:
                if lam == s_exact:
                    mult_plus += m
                elif lam == -s_exact:
                    mult_minus += m
                else:
                    distinct_ok = False
            ok = distinct_ok and mult_plus == (1 << (n - 1)) and mult_minus == (1 << (n - 1))
            shown = ", ".join(f"{k}={v}" for k, v in pairs)
            print(f"n={n:2d} exact-eigenvals distinct=[{shown}] "
                  f"mult+= {mult_plus} mult-= {mult_minus} only+-sqrt(n): {ok} ({time.time()-t0:.1f}s)")
        else:
            A = huang_matrix_np(n)
            ev = np.linalg.eigvalsh(A)
            n_plus = np.sum(np.abs(ev - s) < 1e-6)
            n_minus = np.sum(np.abs(ev + s) < 1e-6)
            n_other = ev.size - n_plus - n_minus
            ok = n_plus == (1 << (n - 1)) and n_minus == (1 << (n - 1)) and n_other == 0
            print(f"n={n:2d} numeric-eigenvals: +sqrt(n) x {n_plus}, -sqrt(n) x {n_minus}, "
                  f"other {n_other}  (want {1<<(n-1)} each, 0 other): {ok} ({time.time()-t0:.1f}s)")


def part3_interlacing(nmin=2, nmax=10, trials=5, seeds=None):
    section("PART 3 — interlacing: lambda_max(B[S,S]) >= sqrt(n) for |S|=2^{n-1}+1")
    if seeds is None:
        seeds = [1, 7, 42, 123, 2024]
    all_ok = True
    for n in range(nmin, nmax + 1):
        s = math.sqrt(n)
        N = 1 << n
        m = (1 << (n - 1)) + 1
        A = huang_matrix_np(n)
        worst = -1e18
        failures = 0
        for seed in seeds[:trials]:
            rng = np.random.default_rng(seed)
            S = rng.permutation(N)[:m].tolist()
            B = A[np.ix_(S, S)]
            lam = np.linalg.eigvalsh(B)[-1]
            worst = max(worst, lam)
            if lam < s - 1e-8:
                failures += 1
        ok = failures == 0
        all_ok = all_ok and ok
        print(f"n={n:2d} N={N:4d} m={m:4d} trials={trials:2d}: min-lambda_max over trials >= sqrt(n) "
              f"{'YES' if ok else 'NO'}  (worst lambda_max={worst:.4f}, sqrt(n)={s:.4f})")
    print(f"\nPART 3 overall: {'ALL lambda_max >= sqrt(n)' if all_ok else 'SOME FAILED'}")


def part4_degree_bound(nmin=2, nmax=10, trials=5, seeds=None):
    section("PART 4 — quadratic form / degree: lambda_max(B) <= Delta(H)")
    if seeds is None:
        seeds = [1, 7, 42, 123, 2024]
    all_ok = True
    for n in range(nmin, nmax + 1):
        s = math.sqrt(n)
        N = 1 << n
        m = (1 << (n - 1)) + 1
        A = huang_matrix_np(n)
        worst_lambda, worst_delta = 0.0, 0
        failures = 0
        for seed in seeds[:trials]:
            rng = np.random.default_rng(seed)
            S = rng.permutation(N)[:m].tolist()
            B = A[np.ix_(S, S)]
            lam = np.linalg.eigvalsh(B)[-1]
            delta = max_internal_degree(n, S)  # exact integer, Delta(H)
            worst_lambda = max(worst_lambda, lam)
            worst_delta = max(worst_delta, delta)
            if lam > delta + 1e-8:
                failures += 1
        ok = failures == 0
        all_ok = all_ok and ok
        print(f"n={n:2d} trials={trials:2d}: lambda_max <= Delta(H) "
              f"{'YES' if ok else 'NO'}  (worst lambda_max={worst_lambda:.2f}, "
              f"worst Delta(H)={worst_delta}, sqrt(n)={s:.2f})")
    print(f"\nPART 4 overall: {'ALL lambda_max <= Delta(H)' if all_ok else 'SOME FAILED'}")
    return all_ok


if __name__ == "__main__":
    t_start = time.time()
    part1_exact_square_support(nmax=8)
    part2_spectrum(nmin=2, nmax=10)
    part3_interlacing(nmin=2, nmax=10, trials=5)
    part4_degree_bound(nmin=2, nmax=10, trials=5)
    print(f"\nTotal runtime: {time.time()-t_start:.1f}s")
