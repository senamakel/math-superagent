#!/usr/bin/env python3
"""Test the second-entry bit process s_k = A_k(1)/2 in {0,1} against iid Bernoulli.

The run's earlier note said the s-sequence is "Bernoulli-like" (520 zeros/480
twos, 234 runs each) but never tested the run-length distribution formally.
Under iid Bernoulli(p), run lengths of a value follow a geometric distribution:
  P(run of value v has length >= m) = (1-p_v)^{m-1}
where p_v is the probability of the OTHER value (the run of v ends when the
other value appears), with a correction at the sequence boundary.

We test this against the real s-bits (k=1..1000), and against fresh data
beyond what suggested the hypothesis: the depth-600 rows from a fresh sieve.

Exact integers only.
"""
import math
from lib.gilbreath import primes_up_to

def s_bits(primes, depth):
    """Second-entry bits A_k(1)/2 for k=1..depth, iterated abs diff, one row live."""
    # row 0 = primes
    row = primes[:]
    bits = []
    a1 = row[1]  # entry 1 of row 0 (second entry of primes = 3 -> bit? we start k=1)
    # Build iterated rows; each row[1] is the second entry.
    for k in range(1, depth+1):
        # next row = |adjacent diffs|
        nxt = [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
        bits.append(nxt[1]//2)  # second entry /2 -> {0,1}
        row = nxt
    return bits

def run_stats(bits_range):
    """Return (list of zero-run lengths, list of two-run lengths)."""
    zr = []
    tr = []
    cur = bits_range[0]
    L = 1
    for x in bits_range[1:]:
        if x == cur:
            L += 1
        else:
            if cur == 0: zr.append(L)
            else: tr.append(L)
            cur = x
            L = 1
    if cur == 0: zr.append(L)
    else: tr.append(L)
    return zr, tr

def expected_runs(n, p0, p2):
    """Expected number of runs of each value under iid Bernoulli.
    Number of positions where a run of value v STARTS = [first is v] + #(transitions into v).
    Expected runs of 0 = p0 + (n-1)*p2*p0 ; runs of 2 = p2 + (n-1)*p0*p2."""
    e0 = p0 + (n-1)*p2*p0
    e2 = p2 + (n-1)*p0*p2
    return e0, e2

def main():
    print("="*70)
    print("Second-entry bit process test vs iid Bernoulli (run-length structure)")
    print("="*70)
    for label, sieve, depth in [("depth-1000 data (sieve 2e7)", 20_000_000, 1000),
                                ("fresh depth-600 (sieve 2e7)", 20_000_000, 600)]:
        primes = primes_up_to(sieve)
        bits = s_bits(primes, depth)
        n = len(bits)
        # bits are halved: bit 0 = second entry 0, bit 1 = second entry 2
        n0 = bits.count(0); n2 = n - n0
        p0 = n0/n; p2 = n2/n
        zr, tr = run_stats(bits)
        print(f"\n--- {label}: n={n}, #0={n0}, #2={n2}, p0={p0:.3f}, p2={p2:.3f}")
        print(f"    runs of 0: {len(zr)}, runs of 2: {len(tr)}")
        e0, e2 = expected_runs(n, p0, p2)
        print(f"    expected runs under iid: 0->{e0:.1f}, 2->{e2:.1f}")
        # Geometric surge test: P(run of 0 of length >= m) vs (p2)^{m-1}
        # (run of 0 continues while next is 0; conditional prob a 0-run continues = p0)
        # Under iid, a run of 0 continues with prob p0, so P(len>=m|starts) = p0^{m-1}.
        print("    zero-run length survival: m=1..8  observed vs iid p0^{m-1}")
        obs = []
        for m in range(1, 9):
            cnt = sum(1 for r in zr if r >= m)
            obs.append(cnt)
        tot0 = len(zr)
        for m, c in zip(range(1,9), obs):
            iid = tot0 * (p0**(m-1))
            print(f"      m={m}: observed={c}  iid={iid:.1f}")
        print("    two-run length survival: m=1..8")
        for m in range(1, 9):
            c = sum(1 for r in tr if r >= m)
            iid = len(tr) * (p2**(m-1))
            print(f"      m={m}: observed={c}  iid={iid:.1f}")

if __name__ == "__main__":
    main()
