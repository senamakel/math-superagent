"""Empirical probe: does the Mauduit-Rivat statistic correlate with the gap-parity
string h that the SUPPLY fold reads?

h[j] = ((q_{j+1} - q_j)/2) mod 2  (gap parity, index-domain pairwise)
MR statistic: s_2(q_j) mod 2  (binary digit-sum parity of the prime VALUE)

If h is independent of digit-sum parity, MR gives no structural leverage to
SUPPLY (the transfer is genuinely absent). If correlated, there is a concrete
thread worth pursuing.

Only a probe: correlation on a finite range is not a theorem. Negative control:
the analogous correlation against a purely random string will be ~0.5 both ways.

STATUS: UNEXECUTED — the scholar role has no execution tool. This is a handoff:
tool_builder/coder run it with the capture runner
    python3 -m lib.capture --target code/out/mr_gap_correlation_probe.captured.txt -- python3 code/scholar/mr_gap_correlation_probe.py 300000
and report the printed conditional probabilities. Until it runs and its output
is read, it establishes nothing and must not be cited.
"""
import sys

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            step = i
            start = i*i
            sieve[start:n+1:step] = b'\x00' * (((n-start)//step)+1)
    return [i for i in range(n+1) if sieve[i]]

def s2_parity(x):
    # binary digit-sum mod 2 of x
    p = 0
    while x:
        p ^= (x & 1)
        x >>= 1
    return p

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
    limit = 8_000_000
    while True:
        ps = primes_upto(limit)
        if len(ps) >= N+2:
            break
        limit *= 2

    # h[j] = ((q_{j+1}-q_j)/2) mod 2, for the first N primes q_j = ps[j]
    # index in ps: q_j = ps[j] (0-based), so h[j] uses ps[j], ps[j+1]
    h = [(((ps[j+1]-ps[j])//2) & 1) for j in range(N)]
    # digit-sum parity of prime value q_j (the prime itself)
    dp = [s2_parity(ps[j]) & 1 for j in range(N)]

    # contingency: P(h=1) split by digit-sum parity of q_j and of q_{j+1}
    def cond(selector):
        n0 = n1 = c0 = c1 = 0
        for j in range(N):
            if selector(j):
                if h[j]:
                    c1 += 1
                else:
                    c0 += 1
                n0 += (not h[j])
                n1 += h[j]
        return (c1/(n0+n1)), (n0+n1)  # P(h=1 | group), group size

    print(f"N={N} primes (up to {ps[N+1]}); fraction of h=1: {sum(h)/N:.4f}")
    print(f"P(h=1 | s2(q_j) even): size,frac:{cond(lambda j: dp[j]==0)}")
    print(f"P(h=1 | s2(q_j) odd ): size,frac:{cond(lambda j: dp[j]==1)}")
    print(f"P(h=1 | s2(q_{j+1}) even): {cond(lambda j: dp[j+1]==0)}")
    print(f"P(h=1 | s2(q_{j+1}) odd ): {cond(lambda j: dp[j+1]==1)}")
    # pointwise independence check: P(h=1 & dp both even) vs product
    both = sum(1 for j in range(N) if h[j] and dp[j]==0)
    print(f"P(h=1 & s2(q_j) even)={both/N:.4f} vs P(h=1)*P(even)={ (sum(h)/N)*(sum(1 for v in dp if v==0)/N):.4f}")

if __name__ == "__main__":
    main()
