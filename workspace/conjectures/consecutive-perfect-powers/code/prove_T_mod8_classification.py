#!/usr/bin/env python3
"""Complete mod-8 classification of T(c,p) = sum_{k=0}^{p-1}(c^2+1)^k,
the Case-B key quantity (m^2 = T(c,p) for x^p - y^2 = 1, p odd prime,
x = c^2+1, y = c*m).

Every class is decided by c mod 8 and p mod 8 because T's residue depends only
on x = c^2+1 mod 8 and p.  The program certifies the three residue FORMULAS by
direct exact computation over wide ranges, then states exactly which (c,p)
classes survive the mod-8 obstruction (i.e. could be a square) and which are
eliminated (provably non-square).

Hand derivation:
  c odd   => c^2 == 1 (mod 8), x = c^2+1 == 2 (mod 8).  u^k == 0 (mod 8) for
            u==2 (mod 8), k>=3.  T == 1+2+4 == 7 (mod 8) for any p>=3.
            squares mod 8 = {0,1,4}  => 7 is a NON-square.  -> c odd elim'd.
  c == 0 (mod 4) => x == 1 (mod 8), x^k == 1, T == p (mod 8).  Square iff
            p == 1 (mod 8)  (p odd prime => p==1,3,5,7 mod 8; only 1 in
            {0,1,4}).  -> c==0 mod4, p != 1 mod 8 eliminated; p==1 mod 8 open.
  c == 2 (mod 4) => x == 5 (mod 8).  T == (#even k)*1 + (#odd k)*5 (mod 8)
            with p terms k=0..p-1, p odd: #odd k = (p-1)/2, #even k=(p+1)/2.
            T == (p+1)/2 + 5(p-1)/2 == 3p-2 (mod 8).  Square iff 3p-2 in
            {0,1,4} mod 8, i.e. p==1 (mod 8).  -> c==2 mod4, p!=1 mod8 elim'd;
            p==1 mod8 open.

So the ONLY (c,p) residue combinations mod 8 that can even be a square are
c even with p == 1 (mod 8).  Everything else is proved non-square by mod 8
alone.  The program verifies all three formulas exactly and then enumerates
the surviving classes confirmed by direct isqrt over a box.

All arithmetic exact (Python ints).  No floats.
"""
from math import isqrt


def is_odd_prime(n):
    if n < 3:
        return False
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def T_mod8(c, p):
    x = c * c + 1
    return (pow(x, p) - 1) // (x - 1) % 8


SQR8 = {0, 1, 4}


def main():
    ok = True
    print("=== Complete mod-8 classification of T(c,p), c>=1 odd prime p >= 3 ===\n")

    # ---- certify the three residue formulas over wide exact ranges ----
    # Formula A: c odd => T == 7 (mod 8)
    A_ok = all(T_mod8(c, p) == 7
               for c in range(1, 5000, 2)
               for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
    print(f"A) c odd  =>  T == 7 mod 8   (odd c<=5000, p in {[3,5,7,11,13,17,19,23,29,31,37]}): {A_ok}")
    ok = ok and A_ok

    # Formula B: c == 0 (mod 4) => T == p (mod 8)
    B_ok = all(T_mod8(c, p) == p % 8
               for c in [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
               for p in range(3, 200) if is_odd_prime(p))
    print(f"B) c==0 mod4  =>  T == p mod 8  (c in {[4,8,12,16,20,24,28,32,36,40,44,48]}, odd prime p<200): {B_ok}")
    ok = ok and B_ok

    # Formula C: c == 2 (mod 4) => T == (3p-2) (mod 8)
    C_ok = all(T_mod8(c, p) == (3 * p - 2) % 8
               for c in [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46]
               for p in range(3, 200) if is_odd_prime(p))
    print(f"C) c==2 mod4  =>  T == (3p-2) mod 8  (c in {[2,6,10,14,18,22,26,30,34,38,42,46]}, odd prime p<200): {C_ok}")
    ok = ok and C_ok

    # ---- classify every (c mod 8, p mod 8) class ----
    print("\n=== (c mod 8, p mod 8) classes of T(c,p): square-viable? ===")
    print("      (each row = one c mod 8; columns p mod 8 = 1..7; 'x'=eliminated,")
    print("       'O'=open, i.e. mod-8 alone cannot rule it out)")
    header = "c\\p  " + "".join(f"{m:>5}" for m in (1, 3, 5, 7))
    print(header)
    open_classes = []
    for cmod in range(8):
        row = []
        c_even = (cmod % 2 == 0)
        for pmod in (1, 3, 5, 7):
            # representative residues
            c = cmod + 8
            p = pmod
            while not is_odd_prime(p):
                p += 8
            r = T_mod8(c, p)
            elim = (r not in SQR8)
            if elim:
                row.append("   x ")
            else:
                row.append("   O ")
                open_classes.append((cmod, pmod))
        tag = f"c=={cmod} mod8"
        print(f"{tag:<7}" + "".join(row))
    print("\nOpen (square-viable) (c mod 8, p mod 8) classes:",
          open_classes if open_classes else "NONE")

    # ---- direct isqrt confirmation that every eliminated c,p is non-square ----
    elim_bad = 0
    elim_cnt = 0
    open_bad = 0
    open_cnt = 0
    for c in range(1, 4001):
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
            r = T_mod8(c, p)  # c includes all mod-8 classes
            t = (pow(c * c + 1, p) - 1) // (c * c)  # (x^p-1)/(x-1)
            sq = isqrt(t)
            is_sq = sq * sq == t
            if r in SQR8:      # class says 'open'
                open_cnt += 1
                if is_sq:
                    open_bad += 1
            else:              # class says eliminated -> must be non-square
                elim_cnt += 1
                if is_sq:
                    elim_bad += 1
    print(f"\nDirect isqrt over c in [1,4000], p in first 13 odd primes:")
    print(f"  eliminated classes: {elim_cnt} checked, {elim_bad} that WERE squares (must be 0)")
    print(f"  open classes:       {open_cnt} checked, {open_bad} actual squares found")

    ok = ok and A_ok and B_ok and C_ok and elim_bad == 0
    print("\nRESULT:", "ALL FORMULAS HOLD" if ok else "FAILED")
    print("=> The mod-8 obstruction alone proves T(c,p) is a non-square for")
    print("   EVERY (c,p) except possibly c even AND p == 1 (mod 8).  In")
    print("   particular the entire c-odd branch (which is x even in Case B)")
    print("   is settled, and only c even, p==1 mod 8 remains for Ljunggren.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
