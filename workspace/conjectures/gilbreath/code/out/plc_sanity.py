"""Sanity checks for plc_measure before the full run (task item)."""
import random
from lib.fcsr import (fcsr_lambda_bits, fcsr_lambda_prefix, kernel_size,
                      zero_run_stats, hamming_weight, brute_lambda_bits)

# Check 1: imports work (already proven by import above). Print ack.
print("CHECK1 imports: OK (all six imported from lib.fcsr)")

# Check 2: validate fcsr_lambda_bits vs brute on random short strings (N<=10)
random.seed(12345)
fails = 0
trials = 200
for _ in range(trials):
    N = random.randint(1, 10)
    bits = [random.randint(0, 1) for _ in range(N)]
    lam_fast = fcsr_lambda_bits(bits)[0]
    lam_brute = brute_lambda_bits(bits)
    if lam_fast != lam_brute:
        fails += 1
        print("  MISMATCH bits=%s fast=%d brute=%d" % (bits, lam_fast, lam_brute))
print("CHECK2 fcsr_lambda_bits vs brute_lambda_bits: %s (%d trials, N<=10, %d mismatches)"
      % ("PASS" if fails == 0 else "FAIL", trials, fails))

# Check 3: Thue-Morse zeta witness. For h[j]=popcount(j)%2 with the 2-then-odds
# q built as q[0]=2, q[1]=3, q[n+1] = q[n] + (2 if h[j]==1 else 4),
# nu2(n)=#{2s in maximal {0,2} suffix}. Claim: for n=d+1 start indexing,
# nu2(n) = floor(log2 n)+1 at n=512 should be 10.
# Build 2-then-odds q from switch bits h[0.. ] and count nu2 via the
# right-diagonal maximal {0,2} suffix.
def popcount(j): return bin(j).count("1")
from lib.rightdiag import incremental_diagonals, cycle_and_nu2
N = 512
h = [popcount(j) & 1 for j in range(N)]
q = [2, 3]
for j in range(N):
    q.append(q[-1] + (2 if h[j] else 4))
# nu2 for prefixes n=1..N: track diagonals incrementally
yielder = incremental_diagonals(q)
nu2_by_prefix = []
for n in range(0, N + 1):
    dd = next(yielder)
    _, nu2 = cycle_and_nu2(dd)
    nu2_by_prefix.append(nu2)
nu2_512 = nu2_by_prefix[N]
print("CHECK3 Thue-Morse zeta: nu2(%d)=%d (expected 10 = floor(log2 512)+1) => %s"
      % (N, nu2_512, "PASS" if nu2_512 == 10 else "FAIL"))
