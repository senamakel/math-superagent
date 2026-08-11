"""Verify the central reduction for PE 903.

Claim (factoradic + arithmetic gap function):
  Q(n) = (n!)^2 + A_n * Sigma_{m=1}^{n-1} m*m!
              + (B_n/2) * Sigma_{m=1}^{n-1} m*(m-1)*m!
with A_n = f_n(1) = f[0], B_n = f[1]-f[0] (for n>=3), from extend_f.json
(f_n(k) = #{(pi,i): 0<=i<n!, (pi^i)(k) < (pi^i)(0)}, exactly arithmetic in k:
f_n(k) = A_n + (k-1) B_n).

Derivation (from memory.md): rank(tau) = 1 + sum_j a_j(tau)*(n-1-j)! where
a_j is the Lehmer coefficient; M_j = sum_pi sum_i a_j(pi^i) = suffix sum of f;
Q(n) = (n!)^2 + sum_{j=0}^{n-2} (n-1-j)! * M_j.  Substituting r=n-1-j and
f(k)=A_n+(k-1)B_n gives the formula above.  Telescoping: Sigma_{m=1}^{n-1} m*m!
= n!-1, also verified below.

Note m in the sum is r = n-1-j (the descending factoradic weight index).
The formula handles n=2 as well: T(2)=0 so the B term vanishes and A_2=1 gives
Q(2)=4+1=5.

All arithmetic exact (Python big ints).  Compares against known Q values.
"""

import json
from math import factorial


def load_f(path="extend_f.json"):
    with open(path) as fh:
        return {int(k): v for k, v in json.load(fh).items()}


def q_formula(n, f):
    """Q(n) by the central reduction, exact big-int arithmetic."""
    A = f[0]
    # B_n = f[1]-f[0] needs len(f)>=2; for n=2 the B term is multiplied by
    # T(2)=0 so any B works; use 0 for definiteness.
    B = (f[1] - f[0]) if len(f) >= 2 else 0
    fact_n = factorial(n)
    # Sigma_{m=1}^{n-1} m*m!  (== n!-1, telescoping) and
    # T(n) = Sigma_{m=1}^{n-1} m*(m-1)*m!
    s_mm = sum(m * factorial(m) for m in range(1, n))
    t_n = sum(m * (m - 1) * factorial(m) for m in range(1, n))
    # B*T(n) is always even (each m(m-1) is even), so the halving is exact.
    return fact_n * fact_n + A * s_mm + (B * t_n) // 2


def main():
    f_by_n = load_f()
    known = {
        2: 5,
        3: 88,
        4: 4808,
        5: 597876,
        6: 133103808,
        7: 47124948960,
        8: 24768798220800,
    }

    print("Central reduction Q(n) = (n!)^2 + A_n*S(m*m!) + (B_n/2)*T(n)")
    print("T(n) = Sigma m(m-1)*m!,  S = Sigma m*m!  (telescopes to n!-1)\n")
    all_pass = True
    for n in sorted(known):
        f = f_by_n[n]
        A = f[0]
        B = (f[1] - f[0]) if len(f) >= 2 else 0
        # require the row to be exactly arithmetic in k as assumed
        arith = all(
            f[k] - f[k - 1] == B for k in range(1, len(f))
        ) if len(f) >= 2 else True
        got = q_formula(n, f)
        exp = known[n]
        ok = (got == exp) and arith
        all_pass &= ok
        print(f"n={n}: Q={got}  expected={exp}  "
              f"A_n={A} B_n={B} arith={arith}  -> {'PASS' if ok else 'FAIL'}")
    print("\nOverall:", "ALL PASS" if all_pass else "SOME FAIL")

    # Telescoping check: Sigma_{m=1}^{n-1} m*m! == n!-1
    print("\nTelescoping check  Sigma_{m=1}^{n-1} m*m! == n!-1:")
    for n in range(3, 9):
        lhs = sum(m * factorial(m) for m in range(1, n))
        rhs = factorial(n) - 1
        print(f"  n={n}: {lhs} == {rhs} -> {'OK' if lhs == rhs else 'FAIL'}")


if __name__ == "__main__":
    main()
