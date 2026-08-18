"""Check the mod-100 regularity Psi(k) == 1+floor(k/phi^2) (mod 100) beyond the
verified range k=1..3000, using the verified mechanical construction.

If it fails, find the first failing k.  Also verify the boundary values from
code/out/boundary_psi_modM.txt independently at k=4180 by re-running mech_psi
with a different slope approximant (factor=2) — the construction must be
insensitive to the rational approximation of alpha.
"""
import sys

sys.path.insert(0, "code/mech")
sys.path.insert(0, "code")
from mech_psi import mech_psi  # noqa: E402

sys.set_int_max_str_digits(20000)
import math

PHI2 = (3 + math.sqrt(5)) / 2


def c1(k):
    return 1 + int(k / PHI2)


def main():
    # 1. re-verify the recorded boundary values, and check mod 100 at each
    print("== boundary points: Psi mod 100 vs c1(k) mod 100 ==")
    for k in [609, 986, 1596, 2583, 4180]:
        tA, tB, vA, vB = mech_psi(k)
        assert tA == tB
        print(f"  k={k:5d}  Psi%100={tA%100:2d}  c1(k)%100={c1(k)%100:2d}  "
              f"match={tA%100==c1(k)%100}")

    # 2. walk k around the 3000 boundary to find the first failure, if any
    print("\n== scan for first failure of Psi(k) == c1(k) mod 100 ==")
    first = None
    for k in range(3001, 4181):
        tA, tB, vA, vB = mech_psi(k)
        assert tA == tB
        if tA % 100 != c1(k) % 100:
            first = k
            break
    if first is None:
        print("  no failure in 3001..4180 (range end exclusive of check)")
    else:
        tA, _, _, _ = mech_psi(first)
        print(f"  FIRST FAILURE at k={first}: Psi%100={tA%100} "
              f"c1(k)%100={c1(first)%100}")

    # 3. slope-insensitivity recheck at k=4180 with a larger denominator
    print("\n== slope insensitivity at k=4180 (q minimal vs q>3k) ==")
    a1, b1, _, _ = mech_psi(4180)
    a2, b2, _, _ = mech_psi(4180, factor=4)
    print(f"  minimal q: {a1 % 101001001}    larger q: {a2 % 101001001}   "
          f"same={a1 == a2}")


if __name__ == "__main__":
    main()
