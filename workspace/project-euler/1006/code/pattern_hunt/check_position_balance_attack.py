#!/usr/bin/env python3
"""PE1006: attack the NEW bounded-deviation conjecture for the first moment.

Conjecture under attack: for every k >= 1, writing poscount(j) for the number
of length-k Fibonacci-word factors with a '1' at position j,
    |poscount(j) - c1(k)| <= 1  for all j,
with equality-to-0 for all j iff k = F_n - 1.  Equivalently
    M1(k) - c1(k)*R(k) = sum_j dev(j) 10^(k-1-j),  dev(j) in {-1,0,+1}
(a "balanced-digit" deviation from the balanced repunit c1(k)*R(k)).

This is the first-moment transpose of the recorded Toeplitz-defect finding
(|C(i,j)-C(i-1,j-1)| <= 1 everywhere, zero iff k = F_n - 1) and of the
recorded k = F_n - 1 position balance.  Both recorded facts are finite
verifications; the new claim is the boundedness at GENERAL k, which was
untested.

Attack plan:
  (A) verify |dev| <= 1 for k = 1..400, report first falsifier if any;
  (B) report the zero-deviation set and compare with {F_n - 1};
  (C) report the deviation digit pattern for sample k (positions of +1/-1)
      to see if the +/- pattern is itself Fibonacci/Sturmian-structured;
  (D) confirm dev(0) = dev(k-1) = 0 (first/last position balanced) for all k.

Exact integer arithmetic; factor sets from Fibonacci-word prefixes of length
>= Lmin(k+1)+10 (Lmin verified sufficient through k=6764).
"""

from math import isqrt

SCALE = 4 ** 60
SQRT5 = isqrt(5 * SCALE * SCALE)


def c1_formula(k):
    return 1 + (3 * k * SCALE - k * SQRT5) // (2 * SCALE)


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


def main():
    KMAX = 400
    w = fib_prefix(lmin(KMAX + 1) + 10)
    fibs = set()
    a, b = 1, 2
    while b - 1 <= KMAX:
        fibs.add(b - 1)
        a, b = b, a + b

    first_fail = None
    zero_set = []
    end_ok = True
    print("== (A) |poscount(j) - c1(k)| <= 1 for k = 1..%d ==" % KMAX)
    for k in range(1, KMAX + 1):
        Fk = {w[i:i + k] for i in range(len(w) - k + 1)}
        assert len(Fk) == k + 1
        c = c1_formula(k)
        dev = []
        for j in range(k):
            cnt = sum(1 for f in Fk if f[j] == '1')
            dev.append(cnt - c)
        md = max(abs(d) for d in dev)
        if md > 1 and first_fail is None:
            first_fail = (k, md)
        if md == 0:
            zero_set.append(k)
        if dev[0] != 0 or dev[-1] != 0:
            end_ok = False
            print("  END-POSITION FAILURE at k =", k)
    print("  first k with |dev| >= 2:", first_fail)
    print("  zero-deviation set (k=1..%d):" % KMAX, zero_set)
    print("  equals {F_n - 1} list:", zero_set == sorted(fibs))
    print("  dev(0)=dev(k-1)=0 for all k:", end_ok)

    print("\n== (C) deviation digit pattern for sample k ==")
    for k in (3, 5, 6, 8, 9, 10, 13, 21, 34, 55, 89, 144, 233, 377):
        if k > KMAX:
            continue
        Fk = {w[i:i + k] for i in range(len(w) - k + 1)}
        c = c1_formula(k)
        dev = [sum(1 for f in Fk if f[j] == '1') - c for j in range(k)]
        print(f"  k={k:3d}: dev = {''.join('+' if d > 0 else '-' if d < 0 else '.' for d in dev)}")

    print("\n== (D) balanced-digit form M1 - c1*R for k = 1..40 ==")
    bad_balanced = None
    for k in range(1, 41):
        Fk = {w[i:i + k] for i in range(len(w) - k + 1)}
        c = c1_formula(k)
        R = (10 ** k - 1) // 9
        M1 = sum(int(f) for f in Fk)
        diff = M1 - c * R
        # diff has digits in {-1,0,+1} iff adding R*(c+1) gives digits 0..2? use direct check:
        # each dev(j) in {-1,0,1} already verified; diff = sum dev(j) 10^(k-1-j)
        dev = [sum(1 for f in Fk if f[j] == '1') - c for j in range(k)]
        if any(abs(d) > 1 for d in dev):
            bad_balanced = k
            break
        if k <= 12:
            print(f"  k={k:2d}: M1-c*R = {diff:+d}")
    print("  balanced-digit form holds k=1..40:", bad_balanced is None)
    print("\n  Note: |dev|<=1 at general k is the FIRST-moment transpose of the")
    print("  recorded Toeplitz-defect |C(i,j)-C(i-1,j-1)|<=1 (pattern-hunt cycle 3),")
    print("  and reduces to the recorded exact balance at k = F_n-1.")


if __name__ == '__main__':
    main()
