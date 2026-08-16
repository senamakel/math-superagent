"""Verify Ellis's counterexample to Gilmer's conjecture (arXiv:2211.12401).

Claims checked:
  p(0) = p({1,2}) = x, p({1}) = p({2}) = 1/2 - x, with x = 0.3.
  Then Prob[1 in A] = Prob[2 in A] = 1/2, yet
    LHS = sum_{s} q_s log2(1/p_s) - sum_{s} p_s log2(1/p_s)  < -0.04
  where q is the distribution of A union B (A,B iid from p).

Exact rational arithmetic in both (a) direct evaluation and (b) the closed form
from the note: (1/2 + 2x^2 - 2x)log2(1/x) + (-1/2 - 2x^2 + 2x)log2(1/(1/2 - x)).
"""
from fractions import Fraction
import math

def log2(x): return math.log(x) / math.log(2)

def check(x):
    x = Fraction(x)
    # p over {0,1}^2 index by bitmask
    p = {0b00: x, 0b11: x, 0b01: Fraction(1,2)-x, 0b10: Fraction(1,2)-x}
    # q_s = sum_{A,B : A or B = s} p(A)p(B)
    q = {m: Fraction(0) for m in range(4)}
    for A in range(4):
        for B in range(4):
            q[A | B] += p[A]*p[B]
    # element 1 (bit 0) present iff bit set
    def in1(s): return (s & 1) != 0
    def in2(s): return (s & 2) != 0
    P1 = sum(p[s] for s in range(4) if in1(s))
    P2 = sum(p[s] for s in range(4) if in2(s))
    # cross entropy term
    lhs = sum(q[s]*(log2(1/float(p[s]))) for s in range(4)) \
        - sum(p[s]*(log2(1/float(p[s]))) for s in range(4))
    # closed form from the note
    closed = (Fraction(1,2)+2*x*x-2*x)*log2(1/float(x)) \
           + (-Fraction(1,2)-2*x*x+2*x)*log2(1/(Fraction(1,2)-x))
    return P1, P2, float(lhs), float(closed), {s: float(q[s]) for s in range(4)}

if __name__ == "__main__":
    x = Fraction(3,10)
    P1, P2, lhs, closed, q = check(x)
    print("x = 0.3")
    print("Prob[1 in A] =", P1, " Prob[2 in A] =", P2)
    print("q distribution:", q)
    print("LHS (direct)   =", lhs)
    print("LHS (closed)   =", closed)
    assert P1 == Fraction(1,2) and P2 == Fraction(1,2)
    assert lhs < -0.04 and closed < -0.04
    print("ALL CHECKS PASS: marginals = 1/2, LHS < -0.04")
