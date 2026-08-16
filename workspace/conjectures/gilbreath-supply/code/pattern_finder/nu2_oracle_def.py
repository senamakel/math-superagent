#!/usr/bin/env python3
"""nu2(n) straight from the problem.md definition (absolute-difference triangle).

This is the definition oracle: builds A_0(i)=q_{i+1}, iterates absolute
differences, reads the right diagonal through column n, and counts 2s in the
maximal {0,2} suffix over k in [2, n-1].
"""
import sympy


def primes_upto_index(n):
    return list(sympy.ntheory.generate.primerange(0, sympy.prime(n) + 1))[:n]


def nu2_from_def(n):
    qs = primes_upto_index(n)
    A = [list(qs)]
    for r in range(1, n):
        row = [abs(A[-1][i] - A[-1][i + 1]) for i in range(len(A[-1]) - 1)]
        A.append(row)
    cells = [A[k][n - 1 - k] for k in range(n)]
    seg = cells[2:n]
    # maximal {0,2} suffix starting at the bottom (k=n-1) end
    count2 = 0
    for v in reversed(seg):
        if v in (0, 2):
            if v == 2:
                count2 += 1
        else:
            break
    return count2, cells


if __name__ == "__main__":
    for n in [8, 10, 16, 20, 32, 53, 100]:
        c2, cells = nu2_from_def(n)
        print(n, c2, cells)
