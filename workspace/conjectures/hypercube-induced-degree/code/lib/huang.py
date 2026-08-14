"""Signed adjacency matrices of the hypercube (Hao Huang's A_n).

A_1 = [[0, 1], [1, 0]]  and  A_n = [[A_{n-1}, I], [I, -A_{n-1}]].

These are symmetric matrices over {0, +-1} whose support is the edge set of
Q_n (two vertices adjacent iff they differ in exactly one coordinate) and
which satisfy A_n^2 = n * I (so the spectrum is +-sqrt(n), each with
multiplicity 2^{n-1}).

huang_matrix   — exact sympy Matrix of Integer entries (for the A_n^2 = n*I
                 identity, the zero-diagonal check and the support check).
huang_matrix_np— numpy float64 array (for numerical spectra, interlacing).
"""

import sympy as sp
import numpy as np


def huang_matrix(n):
    """A_n as an exact sympy Matrix of Integer entries. n >= 1.

    Stored in dense form; for n=8 that is a 256x256 Integer matrix, which is
    the largest the exact identity check is run to. Every entry is a sympy
    Integer (exact, no floats).
    """
    N = 1 << n
    if n == 1:
        return sp.Matrix([[sp.Integer(0), sp.Integer(1)],
                          [sp.Integer(1), sp.Integer(0)]])
    h = N // 2
    A = huang_matrix(n - 1)
    I = sp.eye(h)
    M = sp.zeros(N)
    M[:h, :h] = A
    M[:h, h:] = I
    M[h:, :h] = I
    M[h:, h:] = -A
    return M


def huang_matrix_np(n):
    """A_n as a numpy float64 array (numerical spectrum / interlacing)."""
    if n == 1:
        return np.array([[0.0, 1.0], [1.0, 0.0]])
    A = huang_matrix_np(n - 1)
    h = A.shape[0]
    I = np.eye(h)
    return np.block([[A, I], [I, -A]])
