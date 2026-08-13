#!/usr/bin/env python3
"""Pattern extraction and exact verification for the H_even / 3-Higgs data.

Source of all data being checked: arXiv:2605.20475, full text on disk at
research/sources/maciejewski-bounded-box-subbarao-warren.full.md.

3-Higgs definition (paper line 77, citing OEIS A057447 / Burris-Yeats):
    a prime p is 3-Higgs iff p-1 divides the CUBE of the product of the
    smaller 3-Higgs primes.
Since the product over smaller 3-Higgs primes contains each prime at most
once, this is exactly equivalent to the recursion used here:
    p is 3-Higgs  <=>  every prime factor q of p-1 is 3-Higgs and
                       v_q(p-1) <= 3.
(2 is 3-Higgs: 2-1 = 1 divides everything.)

Program outline:
  1. compute the 3-Higgs primes via an SPF sieve (exact);
  2. check the paper's explicit 3-Higgs / non-3-Higgs witness claims;
  3. check all prime divisors of the five known UPNs are 3-Higgs;
  4. REPRODUCE H_even cap [2,1200]: full factorization of 2^m+1 for m <= 122
     (k odd <= 61), plus a bounded partial-factor witness hunt for
     122 < m <= 1200 (finds non-3-Higgs witnesses where cheap; never claims
     membership from partial data);
  5. verify the frontier structure claims on ALL 272 numbers:
     m == 2 (mod 4); k = m/2 Higgs-cubefree; candidate set closed under odd
     divisors (Prop 4(3) necessity); exactly five composite-k candidates,
     each k the product of two primes p with 2p itself a candidate
     (inherited-from-unresolved-primes structure, paper Theorem 7 discussion);
  6. for every prime factor q of the verified 2^{2k}+1, verify
     ord_q(2) = 4d with d | k (exact), hence q = 1 + 4dt, and check
     v2(q-1) = 2 + v2(t) <= 3, a necessary condition for q to be 3-Higgs.

All exact integer arithmetic.  This is a check of sourced claims and a
sequence-extraction run, not a search.
"""
import sys
from functools import lru_cache

from sympy import factorint, isprime, primerange, pollard_rho

LIMIT = 10**6

# smallest prime factor sieve
_spf = list(range(LIMIT + 1))
for i in range(2, int(LIMIT**0.5) + 1):
    if _spf[i] == i:
        for j in range(i * i, LIMIT + 1, i):
            if _spf[j] == j:
                _spf[j] = i


def spf_factor(n):
    """Factor n (<= LIMIT**2, small enough for this use) by SPF."""
    fs = {}
    while n > 1:
        p = _spf[n] if n <= LIMIT else None
        if p is None:
            # n > LIMIT: fall back to sympy (only for big leftover)
            return fs, n
        c = 0
        while n % p == 0:
            n //= p
            c += 1
        fs[p] = c
    return fs, 1


@lru_cache(maxsize=None)
def higgs3(p):
    """p prime is 3-Higgs?  Recursion terminates since all q < p."""
    if p == 2:
        return True
    if not isprime(p):
        return False
    fs, left = spf_factor(p - 1)
    if left != 1:
        # p-1 has a factor above LIMIT; factor it exactly with sympy
        fs2 = factorint(p - 1)
        return all(higgs3(q) and e <= 3 for q, e in fs2.items())
    return all(higgs3(q) and e <= 3 for q, e in fs.items())


def higgs3_list(limit):
    return [p for p in primerange(2, limit + 1) if higgs3(p)]


_TDIV = 50_000      # trial division limit in split_rec
_RHO_STEPS = 40_000  # pollard-rho steps per attempt


def split_rec(m, fs, depth):
    """Recursively split m: fill fs with primes found; return leftover (1 if
    complete).  Bounded by depth; never loops forever."""
    if m == 1:
        return 1
    if isprime(m):
        fs[m] = fs.get(m, 0) + 1
        return 1
    if depth <= 0:
        return m
    mm = m
    for p in primerange(2, _TDIV + 1):
        if p * p > mm:
            break
        if mm % p == 0:
            c = 0
            while mm % p == 0:
                mm //= p
                c += 1
            fs[p] = fs.get(p, 0) + c
    if mm == 1:
        return 1
    if isprime(mm):
        fs[mm] = fs.get(mm, 0) + 1
        return 1
    try:
        d = pollard_rho(mm, retries=3, max_steps=_RHO_STEPS)
    except TypeError:
        d = pollard_rho(mm, retries=3)
    if d is None or d == mm or d == 1:
        return mm
    r1 = split_rec(d, fs, depth - 1)
    r2 = split_rec(mm // d, fs, depth - 1)
    if r1 != 1 or r2 != 1:
        return (r1 if r1 != 1 else 1) * (r2 if r2 != 1 else 1)
    return 1


def partial_factor(n, tdiv=100_000, rho_iters=30000, rho_tries=6):
    """Return ({p: e} of found prime factors, leftover).

    leftover == 1 iff n was completely factored.  Bounded work: trial
    division to a fixed limit then a bounded number of pollard-rho splits.
    """
    fs = {}
    left = split_rec(n, fs, depth=6)
    if left != 1 and isprime(left):
        fs[left] = fs.get(left, 0) + 1
        return fs, 1
    return fs, left


def order_mod(gen, base, mod):
    """Order of base mod mod: smallest divisor of gen (even) with pow == 1."""
    for m in sorted(_divisors(gen)):
        if pow(base, m, mod) == 1:
            return m
    raise AssertionError("order not found among divisors of gen")


def _divisors(n):
    out = {1}
    for p, e in factorint(n).items():
        out = {d * p**j for d in out for j in range(e + 1)}
    return sorted(out)


VERIFIED = [2, 6, 10, 18, 26, 30, 46, 62, 82, 122]

CANDIDATES = {
    2426, 2602,
    3398, 3518, 4166, 4502, 4622,
    5114, 5774, 7846, 8966, 9326,
    10118, 10454, 11062, 11794, 11878, 12778, 13382, 13966, 14642, 14698,
    15122, 15182, 15206, 15214, 15754, 15758, 16358, 16574, 16778,
    16838, 16922, 17086, 17126, 17162, 17338, 17726, 18134,
    18418, 18934, 18958, 19078, 19226, 19322, 19718, 19802, 19846, 19862,
    20138, 20338, 20506, 20662, 20926, 20974, 21118, 21302,
    21334, 21466, 21818, 21958, 22054, 22234, 22262, 22394, 22486,
    22642, 22706, 23194, 23402, 23578, 23878, 23942, 24082, 24298, 24914,
    25022, 25082, 25106, 25294, 25486, 25526, 25646, 25778, 25786,
    25822, 26066, 26098, 26198, 26302, 26342, 26438, 26482, 26534,
    26618, 26654, 26662, 26678, 26798, 26902, 27374, 27446, 27526,
    27662, 27806, 27926, 27978, 27998, 28058, 28102, 28174, 28214,
    28318, 28442, 28586, 28654, 28862, 29098, 29114, 29126, 29558,
    29642, 29662, 29914,
    30354, 30386, 30542, 30878, 30994, 31162, 31258, 31454,
    31466, 31538, 31634, 31802, 31918, 31942, 31982, 32126, 32174,
    32534, 32762, 32902, 33134, 33214, 33382, 33386, 33574, 33778,
    33806, 33974, 34058, 34246, 34834, 34934,
    35038, 35194, 35366, 35654, 35678, 35818, 35858, 35878, 35942,
    35978, 36094, 36122, 36298, 36458, 36574, 36602, 36682, 36794,
    36986, 37234, 37322, 37358, 37382, 38174, 38282, 38518, 38954,
    39014, 39062, 39154, 39502, 39706, 39826, 39926, 39958,
    40234, 40466, 40538, 40574, 40822, 40886, 41126, 41326, 41386,
    41714, 41758, 41878, 41898, 42134, 42314, 42358, 42646, 42766,
    43058, 43154, 43322, 43402, 43574, 43634, 43642, 43678, 43786,
    44054, 44186, 44294, 44378, 44518, 44582,
    45142, 45286, 45394, 45434, 45478, 45566, 45622, 45706, 45842,
    46022, 46042, 46058, 46394, 46454, 46630, 46714, 46862, 47206,
    47246, 47342, 47378, 47438, 47506, 47858, 47962, 47986, 48086,
    48218, 48338, 48362, 48838, 49354, 49466, 49694, 49834, 49906,
    49958, 49978,
}

UPN5 = [6, 60, 90, 87360, 146361946186458562560000]


def main():
    out = sys.stdout

    # ---- 1. 3-Higgs primes -------------------------------------------
    h_small = higgs3_list(10_000)
    first64 = h_small[:64]
    out.write(f"3-Higgs primes, first 64: {first64}\n")
    out.write(f"count of 3-Higgs primes <= 10^4: {len(h_small)}\n")
    out.write(f"count of 3-Higgs primes <= 10^6: {len(higgs3_list(LIMIT))}\n")
    out.write("SEQUENCE_HIGGS3=" + ",".join(map(str, first64)) + "\n")

    # ---- 2. witness claims --------------------------------------------
    claims = {
        "17 (v2(16)=4, non)": (17, False), "97 (v2(96)=5, non)": (97, False),
        "113 (v2(112)=4, non)": (113, False), "593 (v2(592)=4, non)": (593, False),
        "493169 (v2=4 in -1, non)": (493169, False),
        "20127043 (v3=4 in -1, non)": (20127043, False),
        "343081 (chain 953>17, non)": (343081, False),
        "953 (17|952, non)": (953, False),
        "4513 (v2(4512)=5, non)": (4513, False),
        "2": (2, True), "3": (3, True), "5": (5, True), "7": (7, True),
        "13": (13, True), "19": (19, True), "37": (37, True),
        "41": (41, True), "61": (61, True), "73": (73, True),
        "89": (89, True), "109": (109, True), "257 (v2=8, non)": (257, False),
        "1213": (1213, True), "4663": (4663, True), "5059": (5059, True),
        "6983": (6983, True),
    }
    out.write("\n== witness 3-Higgs status checks (paper's claims) ==\n")
    bad = []
    for label, (p, want) in sorted(claims.items(), key=lambda kv: kv[1][0]):
        got = higgs3(p)
        mark = "ok" if got == want else "MISMATCH"
        if got != want:
            bad.append((label, p, want, got))
        out.write(f"  {label}: got={got} want={want} [{mark}]\n")
    out.write(f"  all witness claims reproduced: {not bad}\n")

    # ---- 3. UPN prime divisors ----------------------------------------
    out.write("\n== prime divisors of the five UPNs are all 3-Higgs ==\n")
    ok_upn = True
    for n in UPN5:
        prims = sorted(factorint(n))
        badp = [p for p in prims if not higgs3(p)]
        out.write(f"  n={n}: primes={prims} {'ALL 3-HIGGS' if not badp else 'BAD: ' + str(badp)}\n")
        ok_upn &= not badp
    out.write(f"  all five UPNs have only 3-Higgs prime divisors: {ok_upn}\n")

    # ---- 4. reproduce H_even cap [2,1200] ------------------------------
    out.write("\n== H_even cap [2,1200] (full factorization for m <= 122) ==\n")
    found = []
    for k in range(1, 601, 2):
        m = 2 * k
        n = 2**m + 1
        small = (m <= 122)
        fs, left = partial_factor(n, tdiv=500_000 if small else 200_000,
                                  rho_iters=40000, rho_tries=6)
        complete = (left == 1)
        all3 = complete and all(higgs3(p) for p in fs)
        if complete and all3:
            found.append(m)
            out.write(f"  m={m:4d} k={k:3d} 2^m+1 fully factored, all 3-Higgs "
                      f"-> IN: {sorted(fs)}\n")
        elif complete:
            badp = [p for p in fs if not higgs3(p)]
            out.write(f"  m={m:4d} k={k:3d} fully factored, witness {badp} "
                      f"-> excluded\n")
        else:
            badp = [p for p in fs if not higgs3(p)]
            if badp:
                out.write(f"  m={m:4d} k={k:3d} PARTIAL, witness {badp} "
                          f"-> excluded (rigorous)\n")
            else:
                out.write(f"  m={m:4d} k={k:3d} PARTIAL, leftover "
                          f"{len(str(left))} digits, unres. locally\n")
    out.write(f"  verified through 1200: {sorted(found)}\n")
    out.write(f"  matches paper {VERIFIED}: {sorted(found) == sorted(VERIFIED)}\n")
    out.write(f"  paper count: H_even cap [2,1200] = the 10 above\n")

    hcf = [k for k in range(1, 601, 2)
           if all(higgs3(p) and e <= 3 for p, e in factorint(k).items())]
    out.write(f"  Higgs-cubefree odd k in [1,600]: {len(hcf)} "
              f"(paper Theorem 8 says 246 of 300)  "
              f"match: {len(hcf) == 246}\n")

    # ---- 5. frontier structure -----------------------------------------
    out.write("\n== frontier structure: 10 verified + candidates ==")
    allm = sorted(VERIFIED + sorted(CANDIDATES))
    n_total = len(VERIFIED) + len(CANDIDATES)
    out.write(f"\n  |verified| + |candidates| = {n_total} (paper bound 272: "
              f"{n_total == 272})\n")
    bad_mod = [m for m in allm if m % 4 != 2]
    out.write(f"  every m == 2 mod 4 (paper: H_even subset {m % 4 == 2}"
              f"{'' if not bad_mod else '; VIOLATIONS ' + str(bad_mod[:5])}): "
              f"{not bad_mod}\n")
    bad_hcf = [(m, factorint(m // 2)) for m in allm
               if not all(higgs3(p) and e <= 3
                          for p, e in factorint(m // 2).items())]
    out.write(f"  every k = m/2 Higgs-cubefree: {not bad_hcf}\n")
    if bad_hcf:
        out.write(f"    VIOLATIONS: {bad_hcf[:5]}\n")
    universe = set(VERIFIED) | CANDIDATES
    viol = []
    for m in sorted(CANDIDATES):
        k = m // 2
        for d in _divisors(k):
            if d % 2 == 0 or d == k:
                continue
            if 2 * d not in universe:
                viol.append((m, d, 2 * d))
    out.write(f"  candidate set closed under odd divisors (Prop 4(3) "
              f"necessity): {not viol}\n")
    if viol:
        out.write(f"    VIOLATIONS: {viol[:5]}\n")
    comp = [(m, m // 2, factorint(m // 2)) for m in sorted(CANDIDATES)
            if len(factorint(m // 2)) >= 2]
    out.write(f"  candidates with composite k: {len(comp)}\n")
    for m, k, fs in comp:
        pr = sorted(fs)
        inher = all(2 * p in universe for p in pr)
        out.write(f"    m={m} k={k} = {fs}; each prime inherits from a "
                  f"candidate (2p in set): {inher}\n")
    prim_k = sorted(m // 2 for m in allm)
    upd = [k for k in prim_k if isprime(k)]
    out.write(f"  prime candidate k's: {len(upd)} of {len(prim_k)}\n")
    out.write(f"  prime k: min {upd[0]}, max {upd[-1]}\n")
    from collections import Counter
    for mod in (3, 4, 8, 16, 24):
        c = Counter(k % mod for k in upd)
        out.write(f"    residue dist of prime k mod {mod}: "
                  f"{dict(sorted(c.items()))}\n")

    out.write("\n  SEQUENCE_CANDM=" + ",".join(map(str, sorted(CANDIDATES))) + "\n")
    out.write("  SEQUENCE_PRIMEK=" + ",".join(map(str, upd)) + "\n")

    # ---- 6. order structure for verified elements -----------------------
    out.write("\n== order structure: q | 2^{2k}+1 => ord_q(2) = 4d, d | k ==\n")
    out.write("   (then q = 1 + 4dt; 3-Higgs requires v2(q-1) <= 3, i.e. "
              "v2(t) <= 1)\n")
    for k in [1, 3, 5, 9, 13, 15, 23, 31, 41, 61]:
        n = 4**k + 1
        fs, left = partial_factor(n, tdiv=1_000_000, rho_iters=60000,
                                  rho_tries=8)
        if left != 1:
            out.write(f"  k={k}: UNFACTORED (leftover {len(str(left))} "
                      f"digits) -- skipped\n")
            continue
        ok_ord = ok_v2 = True
        lines = []
        for q in sorted(fs):
            ordq = order_mod(4 * k, 2, q)
            d = ordq // 4
            cond = (ordq % 4 == 0 and (4 * k) % ordq == 0 and k % d == 0)
            ok_ord &= cond
            t = (q - 1) // (4 * d)
            v2q1 = (q - 1 & -(q - 1)).bit_length() - 1
            v2t = (t & -t).bit_length() - 1
            ok_v2 &= (v2t <= 1)
            lines.append(f"      q={q}: ord={ordq} d={d} (d|k: {k % d == 0}) "
                         f"q-1=4dt t={t} v2(q-1)={v2q1} v2(t)={v2t} "
                         f"3-Higgs={higgs3(q)}")
        out.write(f"  k={k:3d} m={2*k}: factors {sorted(fs)}\n")
        out.write("\n".join(lines) + "\n")
        out.write(f"     ord=4d with d|k holds: {ok_ord}; "
                  f"v2(t)<=1 for every factor: {ok_v2}\n")

    out.write("\nSEQUENCE_M=" + ",".join(map(str, VERIFIED)) + "\n")
    out.write("SEQUENCE_K=" + ",".join(str(m // 2) for m in VERIFIED) + "\n")
    out.write("DONE\n")


if __name__ == "__main__":
    main()