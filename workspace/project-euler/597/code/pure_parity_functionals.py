"""Exact small-n values of the two pure-race 'parity' functionals, computed
from first principles with closed forms, for the research note
research/pure_ballistic_final_order_parity.md.

Functional A -- parity of the NUMBER OF CLUSTERS (== number of cycles of a uniform
permutation).  Closed form: #permutations with even #cycles == # with odd #cycles = n!/2
for every n>=2 (Bona, Levande, Shattuck).  Verified here by building the unsigned
Stirling triangle S1(n,k) and checking even==odd==n!/2.

Functional B -- parity of sum over clusters of C(size,2) (the 'cluster-block' proxy
that the run REFUTED as the torpids parity).  EGF  A(z)=exp(sum_k (-1)^C(k,2) z^k/k)
       = exp(arctan z)/sqrt(1+z^2);  P(even)=1/2(1+[z^n]A(z)).
Computed exactly by the differential recurrence n*A_n = sum_{i=1..n} i*B_i*A_{n-i}.

Outputs are checked against the run's recorded exact values in
research/pure_ballistic_final_order_parity.md and code/cycle_parity.py.
"""
import math
from fractions import Fraction


def C2(k):
    return k * (k - 1) // 2


def functional_B(n):
    """Return exact P(sum over clusters C(size,2) even) under the uniform-permutation
    cycle-composition law, via A(z)=exp(B(z)),  B(z)=sum_k (-1)^C(k,2) z^k/k."""
    A = [Fraction(1)]
    dB = [Fraction(0)] + [Fraction((-1) ** (C2(k) % 2), 1) for k in range(1, n + 1)]
    # dB[i] = i * B_i ;  B_i = (-1)^C(i,2) / i  => i*B_i = (-1)^C(i,2)
    for m in range(1, n + 1):
        s = sum(dB[i] * A[m - i] for i in range(1, m + 1))
        A.append(s / m)
    A_n = A[n]
    return Fraction(1, 2) * (1 + A_n)


print("=== Functional A: P(number of clusters even), uniform permutation ===")
for n in range(1, 13):
    S1 = [[0] * (n + 1) for _ in range(n + 1)]
    S1[0][0] = 1
    for m in range(1, n + 1):
        for k in range(1, m + 1):
            S1[m][k] = S1[m - 1][k - 1] + (m - 1) * S1[m - 1][k]
    even = sum(S1[n][k] for k in range(1, n + 1) if k % 2 == 0)
    odd = sum(S1[n][k] for k in range(1, n + 1) if k % 2 == 1)
    frac = Fraction(even, math.factorial(n))
    tag = "balanced" if (even == odd) else "IMBALANCED"
    print(f"  n={n:2d}: P(#clusters even) = {frac}   ({tag})    [assert even==odd: {even==odd}]")

print("\n=== Functional B: P(sum over clusters C(size,2) even), cycle law ===")
for n in [2, 3, 4, 5, 6, 8, 13]:
    p = functional_B(n)
    print(f"  n={n:2d}: {p.numerator}/{p.denominator} = {float(p):.6f}")

print("\n=== Run's verified TORPIDS pure-race parity (NOT functional B) ===")
print("  p(2,inf)=1/2;  p(3,inf)=7/18=0.38889;  p(4,inf)=19/36=0.52778")
print("  => functional B n=3: 1/6 != 7/18 ; n=4: 5/12 != 19/36 (functional B REFUTED as torpids parity)")
