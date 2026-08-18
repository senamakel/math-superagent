#!/usr/bin/env python3
"""Verify the conjectured closed form for the Bautin monomial-count sequence.

Data (all from executed runs, exact sympy):
  a_d = monomial count of L_d, the degree-d focal-value obstruction of the
        5-parameter chart family Q1=A u^2+C u v+D v^2, Q2=E u v+F v^2 with
        rotation linear part (R(p) = -v p_u + u p_v):
    d :  4    6    8   10   12   14   16
    a :  4   30   97  236  485  890  1505
  terms 4..890 from code/out/mono_counts.captured.txt (d=4..14);
  term 1505 from code/out/.d16.tmp.txt (d=16, SUMMARY line).

With h = d-2 (homogeneous degree of L_d in the 5 parameters) and
dim(h) = C(h+4,4) = number of monomials of degree h in 5 variables,
the complement c(h) = dim(h) - 2*a_d takes the values
  h :  2    4    6    8   10   12   14
  c :  7   10   16   23   31   40   50
Conjecture (this file's subject):  c(h) = (h^2 + 14 h + 8)/8 for even h >= 4
(so a_d = (dim(h) - (h^2+14h+8)/8)/2 for d >= 6, and a_4 = 4 is exceptional).

Falsifier: the first even degree the formula does not match. The next
untested degree is d = 18 (h = 16): the formula predicts a_18 = 2392.
"""
import math
from fractions import Fraction

# exact data from executed runs
a_data = {4: 4, 6: 30, 8: 97, 10: 236, 12: 485, 14: 890, 16: 1505}


def dim(h):
    return math.comb(h + 4, 4)


def q(h):
    """Conjectured complement: c(h) = dim(h) - 2*a_d."""
    return (h * h + 14 * h + 8) // 8


def conj_a(d):
    h = d - 2
    if h == 2:
        return 4
    return (dim(h) - q(h)) // 2


# 1. formula matches every computed term?
all_ok = True
print("d     h      a_d   dim(h)  c(h)   q(h)   conj_a   match")
for d in sorted(a_data):
    h = d - 2
    c = dim(h) - 2 * a_data[d]
    ca = conj_a(d)
    ok = (ca == a_data[d]) and (c == q(h))
    all_ok &= ok
    print(f"{d:4d}  {h:4d}  {a_data[d]:6d}  {dim(h):5d}  {c:5d}  {q(h):5d}  {ca:7d}  {ok}")
print("\nALL COMPUTED TERMS MATCH:", all_ok)

# 2. c(h) - q(h) residuals (the conjecture claims these are all 0)
print("\nc(h) - q(h) residuals:", [dim(d - 2) - 2 * a_data[d] - q(d - 2)
                                   for d in sorted(a_data)])

# 3. integrality/parity check: q(h) has the same parity as dim(h), so the
#    quotient is an integer for every even h >= 4, h <= 40 (exact)
bad_parity = []
for k in range(2, 21):          # h = 2k, k = 2..20
    h = 2 * k
    if (dim(h) - q(h)) % 2 != 0:
        bad_parity.append(h)
print("\nparity failures (h even, 4..40):", bad_parity,
      "-> none" if not bad_parity else "-> FOUND")

# 4. predictions — the falsifier values
print("\npredictions (conjecture):")
for h in (16, 18, 20, 22, 24):
    d = h + 2
    print(f"  a_{d:2d} (h={h:2d}) = (C({h+4},4) - q({h}))/2 = "
          f"({dim(h)} - {q(h)})/2 = {conj_a(d)}")

print("\nFALSIFIER: first term that would refute the conjecture is a_18;")
print("the predicted value is 2392. If the d=18 recurrence gives anything")
print("else, the quadratic complement conjecture dies.")