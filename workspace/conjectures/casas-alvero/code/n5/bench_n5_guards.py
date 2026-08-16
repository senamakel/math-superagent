"""Measure the last unknowns for the n=5 verifier (unbuffered):
1. max |entry| of M_T over a sample of tuples (SNF-cost context).
2. is_ca_hasse(x^{p+1}-x^p, p) wall time for in-list primes 131, 193, 599
   (p=2,3,7,11 are cheap; p=3541, 8009 likely infeasible - measured).
3. is_pure_power(charp_witness(p), p) for p=3541 and p=8009 with caps.
"""
import signal
import time

from lib.badprimes import matrix_MT
from lib.casas_alvero import is_ca_hasse, is_pure_power, charp_witness


class Timeout(Exception):
    pass


def _h(sig, frm):
    raise Timeout()


def main():
    import random
    random.seed(7)
    maxe = 0
    for _ in range(20):
        T = tuple(random.randint(1, 5) for _ in range(4))
        Mt = matrix_MT(5, T)
        maxe = max(maxe, max(abs(int(v)) for v in Mt))
    print("max |entry| over 20 sampled tuples:", maxe, flush=True)

    signal.signal(signal.SIGALRM, _h)
    for p in (131, 193, 599):
        signal.alarm(90)
        t0 = time.time()
        try:
            f = charp_witness(p)
            ok = is_ca_hasse(f, p)
            signal.alarm(0)
            print("is_ca_hasse(x^{%d}-x^{%d}, %d) = %s  took %.2fs"
                  % (p + 1, p, p, ok, time.time() - t0), flush=True)
        except Timeout:
            print("is_ca_hasse p=%d exceeded 90s cap" % p, flush=True)
    for p in (3541, 8009):
        signal.alarm(120)
        t0 = time.time()
        try:
            f = charp_witness(p)
            pp = is_pure_power(f, p)
            signal.alarm(0)
            print("is_pure_power(x^{%d}-x^{%d}, %d) = %s  took %.2fs"
                  % (p + 1, p, p, pp, time.time() - t0), flush=True)
        except Timeout:
            print("is_pure_power p=%d exceeded 120s cap" % p, flush=True)


if __name__ == "__main__":
    main()
