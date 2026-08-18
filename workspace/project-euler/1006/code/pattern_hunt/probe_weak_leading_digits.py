"""Pattern probe (this cycle) over recorded exact data.

Checks, exactly, over k = 1..3000 using the validated recurrence pipeline
(reproduces recorded Psi(1..25) from code/out/vR_exact.txt + s1_exact.txt):

  P1. WEAK leading-digits conjecture (never tested before):
      str(Psi(k)) starts with the decimal digits of c1(k) = 1 + floor(k/phi^2).
      (The strong form floor(Psi/10^(2k-2)) == c1(k) is REFUTED at k=138;
       this weak form is a different, weaker statement.)
  P2. Digit-length threshold: len(Psi(k)) == 2k-1 for k <= 23 and == 2k for k >= 24.
      (check_psi_digitlen refuted len==2k-1 at k=24; whether 24 is the exact
       threshold from then on was never reported.)
  P3. S1(k) == 0 (mod 10) for all k (premise of the proven mod-100 identity),
      checked against the record.
  P4. Strong form recheck (record): first k with floor(Psi/10^(2k-2)) != c1(k).
  P5. c1(10^18) recomputed by exact integer arithmetic (isqrt method), to
      re-derive the last two digits of Psi(10^18) = c1(10^18) mod 100.

c1(k) computed EXACTLY with integer sqrt: 1/phi^2 = (3 - sqrt5)/2, so
floor(k/phi^2) = floor((3k - sqrt(5k^2))/2), and with N = isqrt(5k^2),
sqrt(5k^2) = N + delta (0<delta<1 since 5k^2 not a square):
  t = 3k - N;  if t odd: floor = (t-1)/2;  if t even: floor = t/2 - 1.
"""
import sys
from math import isqrt

sys.set_int_max_str_digits(20000)


def c1(k):
    N = isqrt(5 * k * k)
    t = 3 * k - N
    if t % 2 == 1:
        return 1 + (t - 1) // 2
    return 1 + (t // 2 - 1)


def load_pairs(path):
    out = {}
    with open(path) as fh:
        for line in fh:
            p = line.split()
            if len(p) >= 2:
                out[int(p[0])] = int(p[1])
    return out


def main():
    vR = load_pairs("code/out/vR_exact.txt")
    s1 = load_pairs("code/out/s1_exact.txt")
    exact = load_pairs("code/out/psi_exact.txt")
    assert set(vR) == set(range(1, 3001)), "vR_exact missing k"
    assert set(s1) == set(range(1, 3001)), "s1_exact missing k"

    Psi = {1: 1}
    for k in range(1, 3000):
        Psi[k + 1] = 100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1)
    assert all(Psi[k] == exact[k] for k in range(1, 26)), "pipeline broke Psi(1..25)"

    # P1
    bad1 = [k for k in range(1, 3001)
            if not str(Psi[k]).startswith(str(c1(k)))]
    print("P1 weak-leading-digits  k=1..3000:",
          "HOLDS EXACTLY" if not bad1 else f"FAILS at {bad1[:10]} (first: {bad1[0] if bad1 else None})")

    # P2
    bad2 = [k for k in range(1, 3001)
            if len(str(Psi[k])) != (2 * k - 1 if k <= 23 else 2 * k)]
    print("P2 digit-length threshold k<=23 -> 2k-1, k>=24 -> 2k:",
          "HOLDS EXACTLY" if not bad2 else f"FAILS at {bad2[:10]}")

    # P3
    bad3 = [k for k in range(1, 3001) if s1[k] % 10 != 0]
    print("P3 S1(k) == 0 mod 10  k=1..3000:",
          "HOLDS EXACTLY" if not bad3 else f"FAILS at {bad3[:10]}")

    # P4 (record)
    bad4 = [k for k in range(1, 3001) if Psi[k] // 10 ** (2 * k - 2) != c1(k)]
    print("P4 strong leading-block first failure:", bad4[0] if bad4 else None,
          " failures:", len(bad4))

    # P5
    k = 10 ** 18
    c = c1(k)
    print("P5 c1(10^18) =", c)
    print("   c1(10^18) mod 100 =", c % 100, " (want 52 per prior record)")


if __name__ == "__main__":
    main()