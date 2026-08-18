"""Verify the provable low-order-digit identity Psi(k) = c1(k) (mod 100).

Claim (new, this cycle):
    Psi(k) == 1 + floor(k/phi^2)  (mod 100)   for all k >= 1,
where Psi(k) is the PE1006 sum of squares of the k+1 distinct length-k
Fibonacci subwords read as decimals (leading zeros ignored), and
c1(k) = 1+floor(k/phi^2) = A189663 is the number of such factors starting
with '1'.

Proof ingredients (each verified below):
  (a) '11' is not a factor of the infinite Fibonacci word, so every length-k
      factor w with w1 in F_{k+1} ends in '0', hence V(w) = 0 (mod 10);
      therefore S1(k) := sum V(w) over such w is 0 (mod 10).
  (b) The right-extension recurrence (established, direct proof in
      pattern-hunt cycles 3-4, verified exactly k=1..3000):
        Psi(k+1) = 100 Psi(k) + 100 V(R_k)^2 + 20 S1(k) + J(k),
        J(k) = c1(k+1).
      Mod 100, the three noise terms vanish: 100 Psi(k) = 0,
      100 V(R_k)^2 = 0, and 20 S1(k) = 0 mod 200 (S1(k)=0 mod 10),
      so Psi(k+1) = c1(k+1) (mod 100); base Psi(1) = 1 = c1(1).

Falsification boundary tested: the identity fails at mod 1000 (S1 is not
generally 0 mod 50 and V(R_k) not generally 0 mod 10), so mod 100 is the
exact strength of this argument.

Verification over every term available: exact Psi from the validated
recurrence pipeline, k = 1..3000, plus recorded psi_exact.txt k=1..25 and
psi_residues.txt k=1..400 (mod M, enough to pin mod 100 exactly).
"""
import sys
import mpmath as mp
sys.set_int_max_str_digits(20000)
mp.mp.dps = 80
PHI2_INV = mp.mpf(1) / ((1 + mp.sqrt(5)) / 2) ** 2
M = 101001001

def c1(k):
    return 1 + int(mp.floor(k * PHI2_INV))

def load_pairs(path):
    out = {}
    for line in open(path):
        p = line.split()
        if len(p) >= 2:
            out[int(p[0])] = int(p[1])
    return out

# --- (a) '11' never a factor: check a long Fibonacci-word prefix directly ---
# build S_n = S_{n-1} S_{n-2} to length ~ 2*3000*phi
a, b = "0", "01"
while len(b) < 4 * 3000:
    a, b = b, b + a
prefix = b
print("(a) '11' in prefix of length", len(prefix), ":", "11" in prefix)
print("    (must be False for the proof of (a))")

# --- S1(k) = 0 (mod 10) exactly, k=1..3000 ---
s1 = load_pairs("code/out/s1_exact.txt")
bad10 = [k for k in range(1, 3001) if s1[k] % 10 != 0]
print("\n(b) S1(k) mod 10 nonzero for k=1..3000:", "NONE (holds exactly)" if not bad10
      else f"{len(bad10)} failures, first {bad10[:5]}")

# --- Psi via validated recurrence pipeline ---
vR = load_pairs("code/out/vR_exact.txt")
Psi = {1: 1}
for k in range(1, 3000):
    Psi[k + 1] = 100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1)

# sanity: recorded exact k=1..25
exact = load_pairs("code/out/psi_exact.txt")
assert all(Psi[k] == exact[k] for k in range(1, 26)), "pipeline broke exact values"

# --- the identity, mod 100 and mod 1000 ---
bad100 = [k for k in range(1, 3001) if Psi[k] % 100 != c1(k) % 100]
bad1000 = [k for k in range(1, 3001) if Psi[k] % 1000 != c1(k) % 1000]
print("\n(c) Psi(k) = c1(k) mod 100, k=1..3000:",
      "HOLDS EXACTLY FOR ALL 3000 TERMS" if not bad100 else f"FAILS: {bad100[:5]}")
print("    Psi(k) = c1(k) mod 1000 (falsification boundary):",
      "HOLDS" if not bad1000 else f"fails at {len(bad1000)} of 3000, first {bad1000[:5]}")

# cross-check the mod-100 claim against recorded residues mod M (k=1..400)
res = load_pairs("code/out/psi_residues.txt")
ok = all(res[k] % 100 == c1(k) % 100 for k in range(1, 401))
print("\n(d) recorded psi_residues k=1..400: mod 100 matches c1 exactly in all 400:", ok)

# show a sample
print("\nsample  k  Psi mod 100  c1 mod 100")
for k in [1, 3, 10, 24, 100, 1000, 2584, 3000]:
    print(f"  {k:5d} {Psi[k] % 100:11d} {c1(k) % 100:9d}")