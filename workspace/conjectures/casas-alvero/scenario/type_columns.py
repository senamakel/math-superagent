"""Fixed-type scenario counts as functions of degree d.

For degree d the number of scenarios of type t is S(d-1, t+1) (Stirling of the
second kind; established earlier in scenario_and_badprime_sequences.md).  For a
FIXED t, S(n, k) with n = d-1 and k = t+1 is a polynomial in the exponentials
1^n, 2^n, ..., k^n, because of the closed form
    S(n,k) = (1/k!) * sum_{j=0..k} (-1)^(k-j) binom(k,j) j^n.
So as a function of d (holding t fixed) the count satisfies a constant-
coefficient linear recurrence whose characteristic polynomial is
prod_{j=1..k} (x - j), of order k = t+1.  This run prints the columns and lets
find_linear_recurrence verify each exact recurrence.

Concrete predictions (to be checked against the tools, not assumed):
  t=0 (k=1): S(d-1,1) = 1                       -> recurrence a_n = a_{n-1}
  t=1 (k=2): S(d-1,2) = 2^(d-2) - 1             -> a_n = 3 a_{n-1} - 2 a_{n-2}
  t=2 (k=3): S(d-1,3) = (3^(d-1) - 3*2^(d-1) + 3)/6
                                               -> a_n = 6 a_{n-1} - 11 a_{n-2} + 6 a_{n-3}
"""
from sympy import binomial, factorial

def closed_S(n, k):
    return sum((-1)**(k-j) * binomial(k, j) * j**n for j in range(k+1)) // factorial(k)

# table: entry[d][t] = S(d-1, t+1) for d = 3..D, t = 0..(d-2)
D = 16
cols = {t: [] for t in range(D-2+1)}
for d in range(3, D+1):
    n = d - 1
    for t in range(0, d-1):   # type t valid when d-1 >= t+1, i.e. t <= d-2
        cols[t].append(closed_S(n, t+1))

for t in sorted(cols):
    print(f"type {t}: {cols[t]}")
