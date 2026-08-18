#!/usr/bin/env python3
"""PE1006: NEW position-balance probes for the FIRST moment M1(k).

Prior (recorded) fact: at k = F_n - 1 every decimal position of the k+1
length-k factors carries exactly c1(k) = 1 + floor(k/phi^2) ones, so
M1(k) = c1(k) * R(k).  Verified k = F_n-1 <= 143.

Genuinely new checks here:
  (A) At GENERAL k, is the per-position one-count bounded by 1 around c1(k)?
      (transpose of the recorded "Toeplitz defect |d|<=1" finding).
      Report max |poscount(j) - c1(k)| and the first k where it exceeds 1.
  (B) At k = F_n - 1 (up to n=13, k=376), re-derive the balance from a
      long Fibonacci-word prefix (independent of the mechanical route) and
      compute S1(k) = sum V(w) over w in F_k with w*'1' in F_{k+1}, looking
      for a closed form in (n, c1, Fibonacci numbers).

All arithmetic exact (integer).  Factor sets from Fibonacci-word prefixes of
length >= Lmin(k+1) = (k+1) + NextFib(k+1) - 1, which the run has verified
suffices through k=6764.
"""

from math import isqrt

PHI2_INV_NUM = isqrt(5)  # placeholder, not used


def fib_prefix(n):
    a, b = '0', '01'
    while len(b) < n:
        a, b = b, b + a
    return b


def next_fib_strict(k):
    a, b = 0, 1
    while b <= k:
        a, b = b, a + b
    return b


def lmin(k):
    return k + next_fib_strict(k) - 1


def factors_of_len(w, k):
    return {w[i:i + k] for i in range(len(w) - k + 1)}


def c1(k):
    # 1 + floor(k/phi^2), phi = (1+sqrt5)/2  =>  phi^2 = (3+sqrt5)/2
    # floor(k/phi^2) computed exactly via Beatty: floor(k/phi^2) = floor(k*(3-sqrt5)/2)
    # use integer arithmetic: floor(k * (3 - sqrt(5)) / 2).
    # sqrt(5) to high precision via isqrt of scaled square.
    # k*(3-sqrt5)/2 = (3k - k*sqrt5)/2.  With s = isqrt(5*4^60), approx 3k/2 - k*s/2/4^30.
    SCALE = 4 ** 60
    s = isqrt(5 * SCALE * SCALE)
    val = (3 * k * SCALE - k * s) // (2 * SCALE)
    return 1 + val


def poscounts(factors, k):
    pc = [0] * k
    for w in factors:
        for j, ch in enumerate(w):
            if ch == '1':
                pc[j] += 1
    return pc


def main():
    KMAX = 200
    w = fib_prefix(lmin(KMAX + 1) + 10)
    worst = 0
    first_bad = None
    print("== (A) per-position one-count deviation |poscount(j) - c1(k)| at general k ==")
    print(f"k  maxdev  c1(k)  positions deviating")
    for k in range(1, KMAX + 1):
        Fk = factors_of_len(w, k)
        assert len(Fk) == k + 1, (k, len(Fk))
        pc = poscounts(Fk, k)
        c = c1(k)
        dev = [pc[j] - c for j in range(k)]
        md = max(abs(d) for d in dev)
        if md > worst:
            worst = md
        if md >= 2 and first_bad is None:
            first_bad = k
        if k <= 30 or md >= 1:
            ndev = sum(1 for d in dev if d != 0)
            print(f"{k:3d}  {md:3d}  {c:4d}  {ndev:3d}")
    print(f"\nmax deviation over k=1..{KMAX}: {worst}")
    print(f"first k with deviation >= 2: {first_bad}")

    print("\n== (B) at k = F_n - 1: balance + S1 closed-form hunt ==")
    fibs = []
    a, b = 1, 2
    while b - 1 <= 400:
        fibs.append(b)          # Fibonacci numbers 2,3,5,8,...  (k = F - 1 >= 1)
        a, b = b, a + b
    # Fibonacci numbers: 1,2,3,5,8,...  (F_2=1 convention); k = F_m - 1
    print("n  k      M1(k) == c1*R ?  S1(k)  S1/R ?  S1/c1 ?")
    for m, F in enumerate(fibs, start=2):
        k = F - 1
        ww = fib_prefix(lmin(k + 1) + 10)
        Fk = factors_of_len(ww, k)
        Fk1 = factors_of_len(ww, k + 1)
        assert len(Fk) == k + 1 and len(Fk1) == k + 2, (k, len(Fk), len(Fk1))
        pc = poscounts(Fk, k)
        c = c1(k)
        balanced = all(p == c for p in pc)
        R = (10 ** k - 1) // 9
        M1 = sum(pc[j] * 10 ** (k - 1 - j) for j in range(k))
        assert M1 == sum(int(w) for w in Fk)
        S1 = sum(int(w) for w in Fk if w + '1' in Fk1)
        tag = "OK " if balanced else "FAIL"
        print(f"{m:3d} {k:4d}  {tag}  {str(M1 == c * R):5s}  "
              f"{S1:>25d}  {str(S1 % R == 0):5s}  {str(S1 % c == 0):5s}")


if __name__ == '__main__':
    main()
