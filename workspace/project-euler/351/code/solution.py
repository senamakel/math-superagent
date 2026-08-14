"""Project Euler 351, exact solution via the totient identity.

Identity (given, and verified by brute force at n = 5, 10, 1000, see below):

    H(n) = total points - visible points
         = (3n^2 + 3n + 1) - (6*Phi(n) + 1)
         = 3n^2 + 3n - 6*Phi(n),
    Phi(n) = sum_{k=1..n} phi(k).

Derivation of "visible points = 6*Phi(n) + 1": the rays from the origin
(hidden-point test only depends on the direction, i.e. on a primitive
vector) host 6*Phi(n) non-origin points because each of the six copies of
the fundamental cone 0 < b < a <= n, gcd(a,b)=1 contributes Phi(n) of them,
and the origin is visible.
"""

from lib.totient import sum_phi, H_hexagon


def main():
    # -- parity check against the brute-force oracle --------------------
    # (O(n log n), n = 1000, a check rather than the method)
    from math import gcd

    def brute(n):
        cnt = 0  # origin is NOT counted as hidden
        for a in range(-n, n + 1):
            for b in range(-n, n + 1):
                if abs(a + b) <= n and not (a == 0 and b == 0) \
                        and gcd(abs(a), abs(b)) > 1:
                    cnt += 1
        return cnt

    expected = {5: 30, 10: 138, 1000: 1177848}
    for n in (5, 10, 1000):
        Phi_n = sum_phi(n)
        H_ident = H_hexagon(n, Phi_n)
        H_oracle = brute(n)
        status = "OK" if H_ident == H_oracle == expected[n] else "MISMATCH"
        print(f"n={n:4d}  Phi(n)={Phi_n:>8d}  H_ident={H_ident:>8d}  "
              f"H_brute={H_oracle:>8d}  expected={expected[n]:>8d}  {status}")
        assert H_ident == H_oracle == expected[n], (n, H_ident, H_oracle)

    # -- the big exact computation --------------------------------------
    N = 10**8
    Phi_N = sum_phi(N)          # int32 phi table, exact integer result
    H_N = H_hexagon(N, Phi_N)
    print()
    print(f"Phi(10^8) = {Phi_N}")
    print(f"H(10^8)   = {H_N}")
    # sanity: rough growth check (not a proof):
    #   Phi ~ 3/pi^2 * N^2 ~ 3.0396e15, H ~ 3N^2 - 6*Phi ~ 0 (growth ~ C*N^2)
    rel = Phi_N / (N * N)
    print(f"Phi(N)/N^2 = {rel:.6f}  (3/pi^2 = {3 / 3.141592653589793**2:.6f})")


if __name__ == "__main__":
    main()