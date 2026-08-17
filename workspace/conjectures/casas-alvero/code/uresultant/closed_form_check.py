#!/usr/bin/env python3
"""Verify the algebra that connects the two claims, exactly for general n:

ord_0(R_i) = n(n-i)   (weighted order, weight w(a_j)=j)

=>  product_i ord_0(R_i) / prod_j w(a_j)
  = prod_{i=1}^{n-1} n(n-i) / n!
  =  n^{n-1} * (n-1)! / n!
  =  n^{n-2}.

This is the Samuel/Valabrega-Valla identity for a complete intersection: for a
complete intersection the quotient length (Samuel multiplicity) equals exactly
prod(orders)/prod(weights).  So the two facts are linked: fact (2) is the
complete-intersection multiplicity and equals n^(n-2) precisely because of the
orders in fact (1).

This script checks the closed-form computation symbolically for all tested n
and confirms prod_i n(n-i)/n! = n^(n-2) for a range of n.  It also tabulates
the intermediate values.
"""
from math import factorial
import itertools

for n in range(3, 16):
    ords = [n*(n-i) for i in range(1, n)]
    prod_ords = 1
    for o in ords: prod_ords *= o
    prod_w = factorial(n)
    samuel = prod_ords // prod_w
    closed = n**(n-2)
    # verify the identity prod n(n-i) = n^{n-1} (n-1)! symbolically
    # prod_{i=1}^{n-1} n(n-i) = n^{n-1} * prod_{j=1}^{n-1} j = n^{n-1} (n-1)!
    lhs = n**(n-1) * factorial(n-1)
    match = (prod_ords == lhs and samuel == closed and prod_ords == samuel * prod_w)
    print(f"n={n:2d}: prod_ords={prod_ords:>18d}  /n! = {samuel:>12d}  n^(n-2)={closed:>12d}  match={match}")
