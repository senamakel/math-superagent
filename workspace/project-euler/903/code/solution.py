#!/usr/bin/env python3
"""solution.py — full-size evaluator for PE 903.

Given the arithmetic constants A_n, B_n of the gap function
    f_n(k) = #{(pi, i) : 0 <= i < n!, (pi^i)(k) < (pi^i)(0)}
           = A + (k - 1) * B          (n = target; k = 1 .. n-1),
computes

    Q(n) = sum over all pi of sum_{i=1}^{n!} rank(pi^i)

modulo p with O(n) time and O(1) space (a single modular loop).

Derivation (recorded in memory.md, verified for n=2..8 against the
brute-force oracles brute.py / brute2.py):
  * rank(tau) = 1 + sum_{j=0}^{n-2} a_j(tau) * (n-1-j)!   (factoradic/Lehmer),
    a_j(tau) = #{m>j : tau[m] < tau[j]}.
  * Summing over pi and i and exchanging the order:
        Q(n) = (n!)^2 + sum_{j=0}^{n-2} (n-1-j)! * M_j,
    where the (n!)^2 term is the "+1 per power" (n! permutations x n! powers)
    and M_j = sum_{k=1}^{n-1-j} f_n(k)   (translation-invariant pairwise form).
  * Substituting f_n(k) = A + (k-1)B and w = n-1-j:
        Q = (n!)^2 + sum_{w=1}^{n-1} w! * (w*A + w*(w-1)*B/2)
          = (n!)^2 + A * (n! - 1) + (B/2) * T,
    where sum_{w=1}^{n-1} w!*w telescopes to n! - 1  and
        T = sum_{w=1}^{n-1} w! * w * (w-1)
    is accumulated in the same loop that builds the factorials mod p.
  * Division by 2 is exact in F_p via inv2 = (p+1)//2, valid since p is odd
    (p = 10^9+7 is prime).

Self-test (run as `python solution.py`): for n = 2..8 reads A = f(1),
B = f(2)-f(1) from extend_f.json and asserts q_from_ab reproduces the
brute-verified exact Q values reduced mod p:
Q(2)=5, Q(3)=88, Q(4)=4808, Q(5)=597876, Q(6)=133103808,
Q(7)=47124948960, Q(8)=24768798220800.  The mandated check is n=5..8;
n=2..4 are included as a bonus (B=0 when the row has a single entry).

CLI for the target n once A_n, B_n are known:
    python solution.py <n> <A> <B> [p]      # prints Q(n) mod p
Example (dummy constants, check only): python solution.py 1000000 0 0
"""

import json
import os
import sys

_MODP = 1_000_000_007
_INV2 = (_MODP + 1) // 2  # modular inverse of 2 mod p


def q_from_ab(n, A, B, p=_MODP):
    """Q(n) mod p from the arithmetic constants of f_n.

    Args:
        n: the permutation size (n >= 1).
        A: f_n(1): f_n(k) = A + (k-1)*B, exact integer (any sign ok, taken mod p).
        B: step of f_n (any sign ok, taken mod p).
        p: prime modulus, default 10^9+7.

    Returns:
        Q(n) mod p as an int in [0, p).

    Complexity: O(n) time, O(1) space; exact modular integer arithmetic
    (no floats, no division by 2 other than inv2).
    """
    fact = 1  # (m-1)! carried through the loop
    T = 0     # sum_{m=1}^{n-1} m! * m * (m-1) mod p
    for m in range(1, n):
        fact = fact * m % p            # fact = m!
        T = (T + fact * m % p * (m - 1)) % p
    fact = fact * n % p                # fact = n! = p -> 0 for n >= p, fine
    return (fact * fact
            + A * ((fact - 1) % p)
            + B * _INV2 % p * T) % p


def _selftest():
    """Check q_from_ab against brute-verified exact Q values (n = 2..8)."""
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "out", "extend_f.json")) as fh:
        data = json.load(fh)
    exact = {2: 5, 3: 88, 4: 4808, 5: 597876, 6: 133103808,
             7: 47124948960, 8: 24768798220800}
    p = _MODP
    ok = True
    for n in sorted(exact):
        row = data[str(n)]
        A = row[0]
        B = row[1] - row[0] if len(row) >= 2 else 0
        got = q_from_ab(n, A, B, p)
        want = exact[n] % p
        good = got == want
        ok = ok and good
        print(f"n={n}: A={A} B={B}  Q mod p = {got}  (expected {want})  "
              f"[{'OK' if good else 'FAIL'}]")
    return ok


def main(argv):
    if len(argv) >= 4:
        n, A, B = int(argv[1]), int(argv[2]), int(argv[3])
        p = int(argv[4]) if len(argv) >= 5 else _MODP
        print(q_from_ab(n, A, B, p))
        return 0
    return 0 if _selftest() else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))