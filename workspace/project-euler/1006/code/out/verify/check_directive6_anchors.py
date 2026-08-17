"""Verify the directive-6 anchors 34432237 (k=10^4) and 20938836 (k=10^6).

Route (verbatim from directive 6, recomputed outside the container): every
distinct length-k window of the Fibonacci word, read as a decimal number,
squares summed mod M, with windows taken from a prefix of length
k + NextFib(k) - 1, where NextFib(k) is the least Fibonacci STRICTLY greater
than k; de-duplicate by residues under two moduli, and assert the distinct
count equals k+1.

IMPORTANT (strictness trap): NextFib must be strict. With the non-strict
version the prefix is one Fibonacci short whenever k is itself a Fibonacci
number, and k=3 then yields 10101 with only 3 of the 4 factors. Use
lib.fibword.next_fib (bisect_right => strict). The k=10^6 case needs a ~10^6
* 1352870 digit scan; run the two-modulus hash in a compiled setting or at
the largest feasible k and extrapolate the residue, or use an independent
O(k)-per-number scheme.
"""
import sys, time
sys.path.insert(0, "/workspace/code")
from lib.fibword import fib_prefix, next_fib, fibs_upto

M = 101001001
M2 = 1000000007  # second modulus for de-duplication by residue pairs

def psi_window(k, W, mod=M, mod2=M2):
    """Sum of squares of distinct length-k windows of prefix W, mod (mod, mod2).

    Windows read as decimal numbers: W is '0'/'1' digits, a window b of length
    k is int(b) (leading zeros vanish automatically). Distinct values tracked
    by (value mod mod, value mod mod2) pairs; the pair set is counted and
    asserted to have size k+1.
    """
    seen = set()
    s = 0
    L = len(W)
    for i in range(L - k + 1):
        v = int(W[i:i+k])
        key = (v % mod, v % mod2)
        if key not in seen:
            seen.add(key)
            s = (s + v * v) % mod
    return s, len(seen)

if __name__ == "__main__":
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    fibs = fibs_upto(k + 1)
    nf = next_fib(k, fibs)
    L = k + nf - 1
    print(f"k={k}  NextFib(k)={nf}  prefix length={L}")
    # strictness sanity: k=3 must find 4 factors
    if k == 3:
        W3 = fib_prefix(3 + next_fib(3, fibs_upto(4)) - 1)
        s3, c3 = psi_window(3, W3)
        print(f"k=3: psi={s3} count={c3} (want 20302, 4)")
    W = fib_prefix(L)
    t0 = time.time()
    v, cnt = psi_window(k, W)
    print(f"Psi({k}) mod M = {v}  count={cnt}  (took {time.time()-t0:.1f}s)")
    print(f"directive-6 anchor (k=10000): 34432237 (count 10001)")
    print(f"directive-6 anchor (k=10^6):  20938836 (count 1000001)")
    ok = (cnt == k + 1) and (
        (k == 10000 and v == 34432237) or (k == 10**6 and v == 20938836)
    )
    print("MATCH?" , ok)