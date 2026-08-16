"""Finite-check extension table for the Erdos ternary conjecture.

Uses the out-of-the-box big-int oracle (materialises 2**n for the n given,
then checks base-3 digits for a 2).  This is deliberately NOT oracle-lean —
it is the cheap independent route the task asks for, run under `timeout 540`
so it cannot overrun.  We report the largest n actually checked in the bounded
run, how far the [0,1000] window reproduces, and the exempt set found.

The point of a separate, naive program here is independence: it recomputes
digit-free-ness by a different route (direct big-int, digit string) than the
modular sieve, as a cross-check that the two agree on the small range both can
reach.
"""

from lib.digits3 import base3_digits_lsb, digit_free_lsb


def digits_of_2n(n):
    """LSB-first base-3 digits of 2**n, via the big integer."""
    return base3_digits_lsb(2 ** n)


def digit_free_bigint(n):
    return digit_free_lsb(digits_of_2n(n))


def main():
    # First window: reproduce [0, 1000], list the digit-free n (the exempt set).
    window = 1000
    exempt = [n for n in range(0, window + 1) if digit_free_bigint(n)]
    print(f"=== finite-check window [0,{window}] ===")
    print(f"digit-free (exempt) n in [0,{window}]: {exempt}")
    print(f"count: {len(exempt)}")

    # b) Push the bounded run as far as it gets before `timeout 540` kills it.
    # Since each n materialises 2**n (about 0.63n ternary digits), the cost is
    # dominated by the largest n; the practical ceiling is where big-int
    # arithmetic on ~10^7\)-digit numbers gets slow.  We stop early and clean:
    # report the largest n completed, and the first n we did NOT reach.
    import time
    start = time.time()
    maxN = 2_000_000          # guessed ceiling; we bail on first failure / timeout
    extend_exempt = []
    largest_checked = None
    first_unreached = None
    # The digit-2 test is cheap per n; the per-n cost grows with 2**n.
    # Use modular digits mod 3^k to keep it light for large n?  We want the
    # big-int route as the independent check, but 2**n for n ~ 10^6 is a 6e5
    # digit integer — fine.  For n ~ 2e6 it is ~1.2e6 digits, still fine one at
    # a time.  The real limit is that *every* n is checked; keep it moderate.
    limit = 500_000
    for n in range(1001, limit + 1):
        if time.time() - start > 500:
            first_unreached = n
            break
        if digit_free_bigint(n):
            extend_exempt.append(n)
        largest_checked = n
    print(f"\n=== bounded extension run (timeout 540) ===")
    print(f"largest n CHECKED: {largest_checked}")
    print(f"first n NOT reached (time-out): {first_unreached}")
    print(f"additional digit-free n found in ({window},{largest_checked}]: "
          f"{extend_exempt if extend_exempt else 'NONE'}")
    print(f"extended exempt set total: {sorted(set(exempt) | set(extend_exempt))}")
    print(f"elapsed: {time.time()-start:.1f}s")


if __name__ == "__main__":
    main()
