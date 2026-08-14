"""Attack the order-3 recurrence found on H at primorials.

The tool found, on 6 terms n in {2,6,30,210,2310,30030}:
  a(n) = (1466670101/7181417)*a(n-1) + (-32059910968/7181417)*a(n-2)
         + (77044655822/7181417)*a(n-3)

6 terms, order 3, huge coefficients: almost certainly a spurious fit
(the record already killed one such recurrence at n=9).  The next term
is H(510510); compute it exactly by a fresh totient sieve (no shared
code with the stored files' producer), and compare with the recurrence's
prediction extended by one step.
"""
from fractions import Fraction

# ---- exact H by fresh sieve up to 510510 ----
N = 510510
phi = list(range(N + 1))
for i in range(2, N + 1):
    if phi[i] == i:
        for j in range(i, N + 1, i):
            phi[j] -= phi[j] // i
Phi = 0
for k in range(1, N + 1):
    Phi += phi[k]
H = 3 * N * N + 3 * N - 6 * Phi
print("H(510510) exact (fresh sieve):", H)
print("H(510510) mod 12:", H % 12, "(law predicts 6 since 510510 mod 4 =", N % 4, ")")

# ---- recurrence prediction for a(7) ----
c1 = Fraction(1466670101, 7181417)
c2 = Fraction(-32059910968, 7181417)
c3 = Fraction(77044655822, 7181417)
a = [Fraction(6), Fraction(54), Fraction(1122), Fraction(52446),
     Fraction(6281514), Fraction(1060784910)]
pred = c1 * a[5] + c2 * a[4] + c3 * a[3]
print("recurrence prediction for H(510510):", pred)
print("prediction is integer:", pred.denominator == 1)
print("MATCH" if pred == H else "FALSIFIED (prediction != true value)")
