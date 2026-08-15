"""Pattern-finder recheck: sequences extracted from solution.txt and the
Euclidean ladder that explains them.  Prints, for the tools to consume:
  - Euclid remainders of (M,A)
  - partial quotients of the continued fraction of M/A
  - run quotients q_k (steps per run)
and checks three exact regularities:
  R1 run length q_k == odd-indexed CF partial quotient b_{2k+1}
  R2 coin values reconstructed exactly from the ladder (dedupe boundaries)
  R3 index step D_k satisfies A*D_k == -r_{2k} (mod M)
plus the count identity 1 + sum(q) == 102.
"""
import re

A = 1504170715041707
M = 4503599627370517


def euc_remainders(a, b):
    """Euclid on (a,b), a>b>0; returns [r1, r2, ...] with r1 = b, ... , 1."""
    r = []
    while b > 0:
        r.append(b)
        a, b = b, a % b
    return r


def cf_quotients(a, b):
    """Partial quotients of the continued fraction a/b."""
    qs = []
    while b > 0:
        qs.append(a // b)
        a, b = b, a % b
    return qs


def main():
    # reference coins
    txt = open('code/out/solution.txt').read()
    ref_idx, ref_val = [], []
    for line in txt.splitlines():
        m = re.match(r'coin #\s*\d+:\s*n =\s*(\d+)\s+c_n = (\d+)', line)
        if m:
            ref_idx.append(int(m.group(1)))
            ref_val.append(int(m.group(2)))

    r = euc_remainders(M, A)
    b = cf_quotients(M, A)          # b_0 = M//A, b_1 = A//r2, ...
    print('num remainders:', len(r), ' last:', r[-1])
    print('remainders =', r)
    print('cf quotients of M/A =', b)
    print('num cf quotients:', len(b), ' sum:', sum(b))

    starts = r[0::2]                # run-start coin values
    steps = r[1::2]                 # AP step magnitudes
    q = [starts[k] // steps[k] for k in range(len(starts))]
    print('q (run lengths) =', q, ' sum:', sum(q), ' -> 1+sum =', 1 + sum(q))

    # R1: q_k == b_{2k+1}
    odd_b = b[1::2]
    print('R1 q == odd-indexed cf quotients:', q == odd_b)
    print('   odd cf quotients =', odd_b)

    # R2: reconstruct values from ladder
    coins = []
    prev = None
    for k in range(len(starts)):
        s, st, qk = starts[k], steps[k], q[k]
        run = [s - j * st for j in range(qk + 1)]
        if prev is not None:
            assert run[0] == prev, (k, run[0], prev)
        coins.extend(run[1:] if prev is not None else run)
        prev = run[-1]
    print('R2 ladder reconstruction == solution values:', coins == ref_val,
          ' count:', len(coins), ' sum:', sum(coins))

    # R3: index steps vs remainders
    # index steps within each run from ref_idx
    D = []
    i = 0
    k = 0
    for k in range(len(starts)):
        # run k spans q[k] index steps, all equal
        base = None
        for j in range(q[k]):
            d = ref_idx[i + 1] - ref_idx[i]
            if base is None:
                base = d
            assert d == base, (k, i, d, base)
            i += 1
        D.append(base)
    ok = all((A * D[k]) % M == (M - steps[k]) % M for k in range(len(D)))
    print('R3 A*D == -step (mod M) all runs:', ok)
    print('index steps D =', D)
    print('D count:', len(D), ' vs runs:', len(starts))

    # tail of remainders reversed (small-to-large Euclid climb)
    print('reversed remainders =', list(reversed(r)))


if __name__ == '__main__':
    main()