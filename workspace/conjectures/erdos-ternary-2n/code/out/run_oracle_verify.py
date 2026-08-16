"""Verification of the Erdos ternary oracle (code/erdos/oracle.py).

Prints exactly the three required reports:

1. digit_free on the three witnesses (0, 2, 8 -> True) and on values known
   to contain a 2 (n=1 -> 2_3, n=3 -> 22_3, n=5 -> 1012_3 -> False), so
   digit_free works both ways.
2. sieve_count(k) for k = 1..26 with 2**(k-1) beside each and whether they
   match (reproduces the |A_k| = 2^(k-1) counting obstruction).  The closed
   form is additionally cross-checked against naive enumeration
   (direct_count) and survivor lifting (lift_count) for every feasible k.
3. finite_check(1, 1000): the digit-free n in [1,1000] (2 and 8 only).

Run via:
    timeout 540 python3 code/out/run_oracle_verify.py \
        2>&1 | tee code/out/oracle_verify.captured.txt
"""

from erdos.oracle import (
    digit_free,
    sieve_count,
    finite_check,
    direct_count,
    lift_count,
)


def witness_table():
    print("=== 1. digit_free witness table ===")
    # The three exceptions must be digit-free.
    expected_free = {0: "1_3", 2: "11_3", 8: "100111_3"}
    ok = True
    for n, expansion in expected_free.items():
        got = digit_free(n)
        match = got is True
        ok = ok and match
        print(f"digit_free({n}) = {got}   (2^{n} = {2**n} = {expansion})"
              f"   {'OK' if match else 'MISMATCH'}")
    # Values known to contain a 2: n=1 -> 2_3, n=3 -> 22_3, n=5 -> 1012_3.
    contains_two = {1: "2_3", 3: "22_3", 5: "1012_3"}
    for n, expansion in contains_two.items():
        got = digit_free(n)
        match = got is False
        ok = ok and match
        print(f"digit_free({n}) = {got}   (2^{n} = {2**n} = {expansion})"
              f"   {'OK, contains 2' if match else 'MISMATCH'}")
    print("Witness check (0,2,8 free; 1,3,5 contain 2):",
          "PASSED" if ok else "FAILED")
    print()
    return ok


def sieve_table(kmx=26):
    print(f"=== 2. sieve_count(k) vs 2^(k-1) for k=1..{kmx} "
          f"(counting obstruction) ===")
    print(f"{'k':>3} {'|A_k|':>8} {'2^(k-1)':>8} {'equal':>6} "
          f"{'direct':>8} {'lift':>8}")
    all_ok = True
    for k in range(1, kmx + 1):
        sk = sieve_count(k)
        target = 2 ** (k - 1)
        eq = sk == target
        all_ok = all_ok and eq
        # Independent checks where feasible.
        if k <= 11:
            dc = direct_count(k)
            lc = lift_count(k)
            agree = (dc == sk == lc)
            all_ok = all_ok and agree
            flag = "" if agree else "  <-- direct/lift MISMATCH"
            print(f"{k:>3} {sk:>8} {target:>8} {str(eq):>6} {dc:>8} {lc:>8}"
                  f"{flag}")
        else:
            print(f"{k:>3} {sk:>8} {target:>8} {str(eq):>6} {'--':>8} {'--':>8}")
    print(f"|A_k| == 2^(k-1) for all k in [1,{kmx}]: "
          f"{'YES' if all_ok else 'NO'}")
    print(f"(direct_count and lift_count agree with sieve_count for "
          f"k in [1,11]: see rows above)")
    print()
    return all_ok


def finite_check_report():
    print("=== 3. finite_check over [1, 1000] ===")
    exempt = finite_check(1, 1000)
    print("digit-free n in [1,1000]:", exempt)
    for w in (2, 8):
        print(f"contains witness {w}: {w in exempt}")
    print("Size of exempt set in [1,1000]:", len(exempt))
    print()
    return exempt


def main():
    ok1 = witness_table()
    ok2 = sieve_table()
    exempt = finite_check_report()
    print("=== Summary ===")
    print("witness OK:", ok1)
    print("sieve |A_k|==2^(k-1) (and direct/lift agreement) OK:", ok2)
    print("exempt set in [1,1000]:", exempt)
    print("VERIFY:", "ALL PASS" if (ok1 and ok2) else "FAILURE")


if __name__ == "__main__":
    main()
