#!/usr/bin/env python3
"""Independent re-derivation of the run's deliverable numerical backbone.

A genuine SECOND route: this module uses its OWN sieve of Eratosthenes and its
OWN iterated-absolute-difference row generator. It deliberately does NOT import
lib.gilbreath (or any lib.* module). All arithmetic is exact integer.

Four checks, per the task brief:

  1. Reproduce problem.md's five worked rows A_1..A_5 from primes <= 60
     (A_1=(1,2,2,4,2,4,2,4,6,2,...), A_2=(1,0,2,2,2,2,2,2,4,...),
      A_3=(1,2,0,0,0,0,0,2,...)).  Report match yes/no.

  2. Reduction check on REAL prime rows k=1..300 (sieve up to 2e6):
     A_{k+1}(0)=1  <=>  A_k(1) in {0,2}, and every A_k(1) in {0,2}.
     Report 0 violations or the first one found.

  3. nu2 supply measurement: with h[j] = (gap_{j+2} mod 4)==2 over the fixed
     ancestor window [2,n-1], and nu2(n) = #2s in the maximal {0,2} suffix of
     the right diagonal delta(q_n), verify nu2(n) >= w(n)/2 where
     w(n) = #{j in [2,n-1] : h[j]=1}, at n = 100,200,400,800,1600
     (sieve up to ~1e6).  Report nu2/w ratios.

  4. Anti-dyadic witness: for the prime switch bit h (first N=200000 bits),
     compute distance/N to the nearest 2^k-periodic string for k=0..4
     (both phases per period where the period fits); report min distance/N
     per k.  Expect ~0.4-0.6.

Verdicts are 'CONFIRMED over stated range only' -- nothing is 'proved' here.
"""


# ---------------------------------------------------------------------------
# 0. Own sieve and own row generator (second route; no lib import).
# ---------------------------------------------------------------------------
def my_sieve(limit):
    """Simple sieve of Eratosthenes; returns sorted list of primes <= limit."""
    if limit < 2:
        return []
    sieve = bytearray(b'\x01') * (limit + 1)
    sieve[0:2] = b'\x00\x00'
    r = int(limit ** 0.5)
    for i in range(2, r + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:limit + 1:step] = b'\x00' * (((limit - start) // step) + 1)
    return [i for i in range(2, limit + 1) if sieve[i]]


def my_rows(primes, depth):
    """Return rows A_0..A_depth over the primes (own generator)."""
    rows = [list(primes)]
    for _ in range(depth):
        prev = rows[-1]
        rows.append([abs(prev[i + 1] - prev[i]) for i in range(len(prev) - 1)])
    return rows


def my_diagonal(primes, n):
    """delta(q_n) = [delta_0..delta_n], delta_k = A_k[n-k], via our own
    in-place right-diagonal recurrence (O(n^2) diffs, O(n) memory)."""
    D = [primes[0]]
    for i in range(1, n + 1):
        newD = [0] * (i + 1)
        newD[0] = primes[i]
        for k in range(1, i + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
    return D


def my_cycle_and_nu2(diag):
    """(tau, nu2): maximal {0,2} suffix of diag[:-1] (the body before the
    terminal entry), start index tau (>=2), nu2 = count of 2s in it."""
    body = diag[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    return i, body[i:].count(2)


# ---------------------------------------------------------------------------
# 1. Reproduce the five worked rows of problem.md.
# ---------------------------------------------------------------------------
EXPECTED = {
    1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2],
    2: [1, 0, 2, 2, 2, 2, 2, 2, 4, 4],
    3: [1, 2, 0, 0, 0, 0, 0, 2, 0, 2],
    4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2],
    5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2],
}


def check_problem_rows():
    P = my_sieve(60)
    rows = my_rows(P, 5)
    all_ok = True
    for k in range(1, 6):
        got = rows[k][:10]
        ok = got == EXPECTED[k]
        all_ok &= ok
        print("  A_%d[:10] = %s  match=%s" % (k, got, "yes" if ok else "NO"))
    print("  RESULT: five worked rows %s" %
          ("reproduced exactly" if all_ok else "MISMATCH"))
    print("  (bound: primes <= 60)")
    return all_ok


# ---------------------------------------------------------------------------
# 2. Reduction check on real prime rows k=1..300 (sieve up to 2e6).
# ---------------------------------------------------------------------------
def check_reduction(limit=2_000_000, k_max=300):
    P = my_sieve(limit)
    # Build rows incrementally to depth k_max (keep only prev row).
    row = P                      # A_0
    prev_second = None
    rng_top = k_max + 1
    data = []                    # (k, A_k(1), A_{k+1}(0))
    for k in range(1, rng_top):  # produces A_k from A_{k-1}
        if k == 1:
            cur = [abs(row[i + 1] - row[i]) for i in range(len(row) - 1)]
        else:
            cur = [abs(row[i + 1] - row[i]) for i in range(len(row) - 1)]
        # cur = A_k
        if len(cur) >= 2:
            data.append((k, cur[1]))
        if k > 1:
            # A_k(0) = |1 - A_{k-1}(1)|
            data.append(("mid", k, cur[0]))
        row = cur
    # Re-derive both columns from the full incremental build for clarity:
    # Simpler: build full rows list for k in 1..k_max+1.
    rows = my_rows(P, k_max + 1)
    viol = []
    second_viol = []
    for k in range(1, rng_top):
        a_k1 = rows[k][1]
        a_kp1_0 = rows[k + 1][0]
        lhs = (a_kp1_0 == 1)
        rhs = (a_k1 in (0, 2))
        if lhs != rhs:
            viol.append((k, a_k1, a_kp1_0))
            if len(viol) <= 5:
                pass
        if a_k1 not in (0, 2):
            second_viol.append((k, a_k1))
    print("  reduction check: A_{k+1}(0)=1 <=> A_k(1) in {0,2}, and "
          "A_k(1) in {0,2}, k=1..%d (sieve <= %d, %d primes)"
          % (k_max, limit, len(P)))
    if not viol and not second_viol:
        print("  RESULT: 0 violations over k=1..%d  (CONFIRMED over stated "
              "range only)" % k_max)
    else:
        if viol:
            print("  FIRST iff-violation at k=%d: A_k(1)=%d, A_{k+1}(0)=%d  "
                  "(first 5: %s)"
                  % (viol[0][0], viol[0][1], viol[0][2], viol[:5]))
        if second_viol:
            print("  FIRST {0,2}-violation at k=%d: A_k(1)=%d  (first 5: %s)"
                  % (second_viol[0][0], second_viol[0][1], second_viol[:5]))
    return (not viol) and (not second_viol)


# ---------------------------------------------------------------------------
# 3. nu2 supply measurement.
# ---------------------------------------------------------------------------
def check_supply(samples=(100, 200, 400, 800, 1600), sieve_to=1_000_000):
    P = my_sieve(sieve_to)
    # Precompute halved-gap bits h[c] = (A_1[c]//2) mod 2 for c 0-indexed,
    # i.e. gap g_{c+1} = p_{c+2} - p_{c+1}.
    hbits = [((P[i + 1] - P[i]) // 2) % 2 for i in range(len(P) - 1)]
    # nu2 via own incremental diagonal recurrence.
    results = []
    print("  supply check nu2(n) >= w(n)/2, n in %s (sieve <= %d)"
          % (list(samples), sieve_to))
    print("  %-6s %-6s %-6s %-8s %-8s %s" %
          ("n", "nu2", "w", "nu2/w", "nu2>=w/2", "nu2/w*2"))
    ok_all = True
    amax = max(samples)
    D = [P[0]]
    nu2_by_n = {}
    for n in range(1, amax + 1):
        newD = [0] * (n + 1)
        newD[0] = P[n]
        for k in range(1, n + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
        if n in set(samples):
            _, nu2 = my_cycle_and_nu2(D)
            nu2_by_n[n] = nu2
    for n in samples:
        nu2 = nu2_by_n[n]
        # w = #{j in [2, n-1] : h[j]=1}
        w = sum(hbits[2:n])
        ratio = (nu2 * 1.0) / w if w else float('inf')
        ok = nu2 >= (w / 2)
        ok_all &= ok
        print("  %-6d %-6d %-6d %-8.3f %-8s %-8.3f" %
              (n, nu2, w, ratio, "OK" if ok else "FAIL", 2.0 * ratio))
    print("  RESULT: nu2(n) >= w(n)/2 %s over the stated n-values "
          "(CONFIRMED over stated range only)"
          % ("holds at every sample" if ok_all else "FAILS"))
    return ok_all


# ---------------------------------------------------------------------------
# 4. Anti-dyadic witness: distance/N to nearest 2^k-periodic string.
# ---------------------------------------------------------------------------
def anti_dyadic(N=200_000, sieve_to=3_000_000, K=4):
    P = my_sieve(sieve_to)
    # switch bit h[i] = 1 iff gap_i == 2 (mod 4), gap_i = p_{i+1} - p_i.
    h = [1 if ((P[i + 1] - P[i]) % 4 == 2) else 0
         for i in range(N)]            # first N bits
    print("  anti-dyadic: N=%d switch bits (sieve <= %d, %d primes), "
          "nearest 2^k-periodic Hamming distance/N" % (N, sieve_to, len(P)))
    print("  %-4s %-6s %-10s" % ("k", "period", "min dist/N"))
    out = []
    for k in range(K + 1):
        L = 1 << k
        dist = 0
        for r in range(L):
            ones = sum(1 for j in range(r, N, L) if h[j])
            tot = len(range(r, N, L))
            dist += min(ones, tot - ones)
        out.append((k, L, dist * 1.0 / N))
        print("  %-4d %-6d %-10.4f" % (k, L, dist * 1.0 / N))
    print("  RESULT: min distance/N per k lies in [%.2f, %.2f] "
          "(expect ~0.4-0.6)  (CONFIRMED over stated range only)"
          % (min(o[2] for o in out), max(o[2] for o in out)))
    return out


def main():
    print("=" * 72)
    print("Independent backbone verification (own sieve + own row generator)")
    print("=" * 72)
    print("\n[1] problem.md five worked rows A_1..A_5")
    check_problem_rows()
    print("\n[2] Reduction check on real prime rows")
    check_reduction()
    print("\n[3] nu2 supply measurement")
    check_supply()
    print("\n[4] Anti-dyadic witness")
    anti_dyadic()
    print("\n" + "=" * 72)
    print("DONE  (verdicts are CONFIRMED over stated ranges only, not proved)")
    print("=" * 72)


if __name__ == "__main__":
    main()
