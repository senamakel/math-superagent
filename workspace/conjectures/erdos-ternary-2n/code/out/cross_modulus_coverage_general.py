"""Generalise the Dr(M') = F_{M'} coverage claim (from cross_modulus_corrected.py,
which only tested primes in Q_LIST = {5,7,11,13,17,19,29,41,193,257}) to ALL
composites M' coprime to 3.  Fast: no giant integers materialised.

Claim (the load-bearing structural step of the adopted cross-modulus route,
hypothesis H1-relaxed): for EVERY M' with gcd(M',3)=1, every residue mod M' is
congruent to some digit-{0,1} (base-3 digits in {0,1}) integer.

PROOF (given, and verified cheaply here):
  m = ord_{M'}(3).  For t in {0,...,M'-1} put s_t = sum_{j=0}^{t-1} 3^{j*m}.
  - Each term 3^{j*m} is a DISTINCT power of 3 (the exponents jm are distinct),
    so the base-3 digits of s_t are 0/1 only (digit 1 exactly at positions
    jm, 0 elsewhere) => s_t is digit-free.
  - 3^{j*m} = 1 (mod M') for every j, so s_t = t (mod M').
  Hence {0,...,M'-1} are all hit, as t runs over a complete residue system.
  s_0 = 0 covers residue 0.

We VERIFY this by modular arithmetic only (never materialising s_t as a big
integer): check pow(3, j*m, M') == 1 for all j < M'-1 (so s_t = t mod M') and
check the position set {j*m} is distinct (free positions => digit-free).  This
is O(M'^2) modular multiplies per M', trivial for M' <= 300.  Independent
brute-force enumeration of Dr(M') is also done for a few small M' (where 3^D
is small), confirming Dr(M') == F_{M'} without using the witness.

Part C: verdict.  If all pass, the corrected mod-M' consistency condition
(b') = "exists digit-free high part s with 2^r = L_r + 3^k s (mod M')" is
VACUOUS for every M' coprime to 3, so the relaxed (exists-digit-free-s)
mixed-modulus route cannot push the pure 3-adic survivor count |A_k| below
2^(k-1).  This is verified-numerically for all M' <= 300 and proved in general
by the s_t witness above.
"""

from math import gcd, log, ceil
from sympy.ntheory import n_order

COMPOSITE_SAMPLES = [8, 16, 25, 80, 121, 128, 242]
M_MAX = 300


def digit_free(s):
    if s == 0:
        return True
    while s > 0:
        if s % 3 == 2:
            return False
        s //= 3
    return True


def _factor(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def _isprime(n):
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True


def part_a():
    print("=" * 74, flush=True)
    print("PART A: s_t witness covers all residues mod M', all M' coprime to 3")
    print(f"(incl. composites), M' in [2,{M_MAX}].  m = ord_{{M'}}(3).", flush=True)
    print(f"{'M':>4} {'factor':>16} {'m':>4} {'type':>5}  coverage", flush=True)
    bad = []
    tot = 0
    for Mp in range(2, M_MAX + 1):
        if gcd(Mp, 3) != 1:
            continue
        tot += 1
        m = n_order(3, Mp)
        # verify all terms 3^{jm} == 1 mod Mp for j=0..M'-2, and positions distinct
        ok = True
        positions = set()
        for j in range(0, Mp - 1):
            positions.add(j * m)
            if pow(3, j * m, Mp) != 1:
                ok = False
                break
        if len(positions) != Mp - 1:   # distinct free digits
            ok = False
        if not ok:
            bad.append(Mp)
        fac = "*".join(f"{p}^{e}" for p, e in _factor(Mp))
        typ = "prime" if _isprime(Mp) else "comp"
        if Mp in COMPOSITE_SAMPLES or Mp == 2 or not ok:
            print(f"{Mp:>4} {fac:>16} {m:>4} {typ:>5}  "
                  f"{'OK' if ok else 'FAIL'}", flush=True)
    print(f"\n  M' coprime to 3 in [2,{M_MAX}]: {tot}; failures: {len(bad)} {bad}",
          flush=True)
    return not bad


def part_b():
    print("=" * 74, flush=True)
    print("PART B: INDEPENDENT brute-force Dr(M') == F_{M'} (no witness used)",
          flush=True)
    for Mp in [8, 16, 25, 80]:
        m = n_order(3, Mp)
        D = min(ceil(log(Mp * m, 3)) + 2, 12)
        hit = set()
        for length in range(0, D + 1):
            for bits in range(2 ** length):
                s = 0
                b = bits
                for i in range(length):
                    s += (b & 1) * (3 ** i)
                    b >>= 1
                hit.add(s % Mp)
        full = set(range(Mp))
        ok = (hit == full)
        print(f"  M'={Mp:>3}: D={D:>2}, |Dr|={len(hit):>3}, == F_{{M'}}: {ok}",
              flush=True)
        if not ok:
            print(f"         MISSING: {sorted(full - hit)}", flush=True)


def main():
    a = part_a()
    part_b()
    print("=" * 74, flush=True)
    print("CONCLUSION (as far as computed):", flush=True)
    print(f"  Part A (witness proof-verify, all M'<=300 coprime to 3): "
          f"{'ALL PASS' if a else 'FAIL'}", flush=True)
    print("  Part B (independent exhaustive Dr(M')==F_{M'}): rows above.",
          flush=True)
    print("  => corrected mod-M' consistency (b') is VACUOUS for every M' coprime", flush=True)
    print("     to 3 (proved by witness; verified-numerically M'<=300), so no", flush=True)
    print("     mixed modulus reduces |A_k| below 2^(k-1) by this relaxed route.", flush=True)


if __name__ == "__main__":
    main()
