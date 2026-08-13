import sys

def main(kmax):
    # Verify the splitting mechanism directly:
    # For a survivor class c at level k, the (k+1)-th digit of 2^(c+j*M) mod 3^(k+1),
    # M = 2*3^(k-1), must take every value in {0,1,2} as j ranges over {0,1,2}.
    # Equivalently: exactly one j gives digit 2, two give digits in {0,1}.
    # Mechanism: 2^M = 1 + c_k * 3^k with 3 ∤ c_k (LTE, v_3(2^M - 1) = k),
    # and 2^c is a unit mod 3, so j ↦ (b + j*c_k*a) mod 3 is a bijection.

    # Check LTE claim numerically: v_3(2^(2*3^(k-1)) - 1) == k
    for k in range(1, kmax+1):
        M = 2 * 3 ** (k - 1)
        x = pow(2, M, 3 ** (k + 1))
        if x != 1:
            # then 2^M != 1 mod 3^(k+1), so v_3 >= k exactly means x = 1 + c*3^k
            pass
        # compute v_3 exactly
        v = 0
        y = pow(2, M) - 1
        while y % 3 == 0:
            y //= 3
            v += 1
        assert v == k, (k, v)
    print(f"LTE check: v_3(2^(2*3^(k-1)) - 1) = k for k=1..{kmax}")

    # Check the unit claim: 2^c mod 3 never 0 (trivially true, but record it)
    for c in range(1000):
        assert pow(2, c, 3) in (1, 2)
    print("2^c mod 3 is never 0 (unit claim) for c<1000")

    # Now verify the digit-cycling directly for every survivor class at levels k=2..kmax-1:
    # the three lifts' (k+1)-th digits form the set {0,1,2} exactly.
    def good_low(k, x):
        for _ in range(k):
            if x % 3 == 2:
                return False
            x //= 3
        return True

    members = [n for n in range(2) if good_low(1, pow(2, n, 3))]
    mod_old = 2
    for k in range(2, kmax+1):
        p3k1 = 3 ** (k + 1)
        bad = 0
        nxt = []
        for c in members:
            digs = []
            for j in (0, 1, 2):
                cand = c + j * mod_old
                r = pow(2, cand, p3k1)
                d = (r // 3 ** (k-1)) % 3   # the k-th ternary digit (position k-1)
                digs.append(d)
                if good_low(k+1, pow(2, cand, 3 ** (k+1))):
                    nxt.append(cand)
            if sorted(digs) != [0, 1, 2]:
                bad += 1
                if bad <= 3:
                    print(f"  k={k} c={c}: digits {digs} not a full cycle")
        if bad:
            print(f"FAIL: {bad} classes at level k={k} do not cycle through digits")
            return
        members = nxt
        mod_old = 2 * 3 ** (k - 1)
    print(f"digit cycling through {{0,1,2}} over the three lifts verified for all classes, k=2..{kmax}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 14)