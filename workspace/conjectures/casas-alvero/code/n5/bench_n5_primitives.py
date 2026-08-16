"""Focused measurements for the n=5 verifier design (unbuffered).

1. SNF on ONE real 195x120 matrix, 480s hard alarm: does it finish, how long.
2. is_ca_hasse(x^{p+1}-x^p, p) for small in-list primes p=2,3,7,11 (large-p
   Hasse is O(p) gcds on degree-(p+1) polys — expected infeasible, noted).
3. ordinary is_ca(x^{p+1}-x^p, p) for p=8009 (all ordinary derivatives vanish
   mod p, so trivially true and cheap).
4. max |entry| of M_T across a sample of tuples (Hadamard-bound note).
"""
import signal
import time

from lib.badprimes import matrix_MT, jt_from_matrix
from lib.casas_alvero import is_ca_hasse, is_ca, charp_witness


class Timeout(Exception):
    pass


def _h(sig, frm):
    raise Timeout()


def main():
    # 1. SNF on one matrix with 480s cap
    signal.signal(signal.SIGALRM, _h)
    M = matrix_MT(5, (1, 1, 1, 1))
    print("M shape:", M.shape, flush=True)
    signal.alarm(480)
    t0 = time.time()
    try:
        J = jt_from_matrix(M)
        signal.alarm(0)
        print("SNF J_T(1,1,1,1) = %s  took %.1fs" % (J, time.time() - t0),
              flush=True)
    except Timeout:
        print("SNF on one 195x120 matrix did not finish within 480s cap",
              flush=True)

    # 2. is_ca_hasse for small in-list primes
    for p in (2, 3, 7, 11):
        t0 = time.time()
        f = charp_witness(p)
        ok = is_ca_hasse(f, p)
        print("is_ca_hasse(x^{%d}-x^{%d}, %d) = %s  took %.2fs"
              % (p + 1, p, p, ok, time.time() - t0), flush=True)

    # 3. ordinary is_ca for p=8009 (cheap: all ordinary derivatives are 0)
    t0 = time.time()
    f = charp_witness(8009)
    ok = is_ca(f, 8009)
    print("is_ca(x^{8010}-x^{8009}, 8009) = %s  took %.2fs"
          % (ok, time.time() - t0), flush=True)

    # 4. max |entry| over a sample of 40 tuples
    import random
    random.seed(7)
    maxe = 0
    for _ in range(40):
        T = tuple(random.randint(1, 5) for _ in range(4))
        Mt = matrix_MT(5, T)
        maxe = max(maxe, max(abs(int(v)) for v in Mt))
    print("max |entry| over 40 sampled tuples: %d" % maxe, flush=True)
    print("Hadamard bound (sqrt(C)*B)^C with C=120:",
          (120 ** 0.5 * maxe) ** 120, flush=True)


if __name__ == "__main__":
    main()
