"""Verify the atomic-bit identity behind Granville's nu2 supply, the claim
these analytic-number-theory sources (RS 1994, Lau 2024, Maynard 2015) bear on.

bit_n = [p_{n+1} not-= p_n (mod 4)] = [gap_n == 2 (mod 4)]   (the c_s=2 descent bit)
nu2(N) = #{n <= N : p_{n+1} not-= p_n mod 4}

Check:
  1. bit agrees with the gap-mod-4 form on every consecutive pair.
  2. nu2/N ~ 1/2 to first order (the measured density feeding Lemma 5.4).

The identity in check 1 is exact arithmetic, not empirical: p, q odd (>=3)
have residues 1 or 3 mod 4, and p != q (mod 4) iff q-p == 2 (mod 4). So
bit_n = [p_{n+1} != p_n mod 4] == [gap_n == 2 mod 4] always; check 1 is a
sanity confirmation, not the load-bearing fact. Check 2 reproduces the on-disk
measurement (claim `granville-nu2-density-measured`), which this run already
holds from exact sieve data. Run with `python3 code/scholar/verify_two_point.py`
to re-confirm; it is UNEXECUTED here (scholar role has no exec tool), so the
density figure below is not newly measured this run.
"""
print("NOTE: this script documents the exact bit identity and a to-run density check.")
print("The identity bit_n = [p_{n+1} not= p_n mod 4] == [gap_n == 2 mod 4] is EXACT")
print("arithmetic for odd primes, not empirical. Run me to re-measure nu2 density.")
from sympy import primerange

LIMIT = 2_000_000  # primes below this

primes = list(primerange(3, LIMIT))  # starts at 3; pairs p_n, p_{n+1} with p_n>=3
nu2 = 0
mismatch = 0
tot = 0
seen = {}
for i in range(len(primes) - 1):
    p, q = primes[i], primes[i + 1]
    gap = q - p
    bit_residue = 1 if (q % 4) != (p % 4) else 0
    bit_gap = 1 if (gap % 4) == 2 else 0
    if bit_residue != bit_gap:
        mismatch += 1
    nu2 += bit_residue
    tot += 1
    # sample the running density
    if tot in (1_000, 10_000, 100_000, len(primes) - 1):
        seen[tot] = nu2 / tot

print(f"primes in [3,{LIMIT}): {len(primes)}")
print(f"pairs checked: {tot}")
print(f"residue-identity mismatches (should be 0): {mismatch}")
print(f"nu2 total: {nu2}")
for k, v in seen.items():
    print(f"  nu2/density at n={k}: {v:.4f}")
print(f"overall density nu2/{tot}: {nu2/tot:.4f}")
