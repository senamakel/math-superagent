"""Independent re-verification of the granville-nu2-density-measured claim.

Computes, for the prime Gilbreath triangle read along the right diagonal through
q_n (delta_k(q_n) = A_k[n-k]), the count nu_2(q_n) of 2s in the maximal {0,2}
suffix of the diagonal, and checks Granville's Lemma 5.4 hypothesis
g*_n <= 2*nu_2 + 2 where g*_n = max(g_2..g_n) (record gap).

This is a second, independent route to the same numbers (the on-disk claim
came from code/nu2_granville_check.py run on the host). Different sieve and
different row-generation order, same definitions.
"""
import math

def primes_upto(N):
    sieve = bytearray(b'\x01')*(N+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(N**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * len(range(i*i, N+1, i))
    return [i for i in range(N+1) if sieve[i]]

def main():
    N = 3_000_000
    M = 4000
    P = primes_upto(N)
    print("num primes below", N, "=", len(P))
    # rows list; keep row 1 (gaps) for g* and build rows incrementally
    # row[k] has length len(P)-k
    row = [P[i+1]-P[i] for i in range(len(P)-1)]      # gaps = A_1
    gstar_list = [0]*(M+2)
    # g*_n = max(g_2..g_n) with g_n = gap at position n = A_1[n-1]
    # We'll just recompute inside loop.
    max_gap = 0
    gstar = [0]*(M+2)
    for n in range(1, M+2):
        max_gap = max(max_gap, row[n-1])   # row[0]=g_2
        gstar[n] = max_gap

    # rows[0] is the primes themselves; we need ANY row generation to read
    # delta_k(q_n) = A_k[n-k]. Rather than store all rows, iterate.
    # A_k[n-k] for a fixed n needs the diagonal. We generate rows one at a time
    # but keep a running triangle would be O(M^2) memory. Instead reuse the
    # existing claim's exact data layout: store rows 0..M.
    rows = [P[:M+2]]
    for k in range(1, M+1):
        prev = rows[-1]
        rows.append([abs(prev[i+1]-prev[i]) for i in range(len(prev)-1)])
    print("rows built:", len(rows), "row0 len", len(rows[0]))

    def diag(n):
        return [rows[k][n-k] for k in range(n)]

    print("\nn      nu2      n^0.525    n/2     nu2/n   g*    2*nu2+2  lem54")
    bad = 0
    for n in [50,100,200,400,800,1600,3200,3999]:
        d = diag(n)
        tail = d[2:-1]
        i = len(tail)
        while i>0 and tail[i-1] in (0,2):
            i -= 1
        cyc = tail[i:]
        nu2 = cyc.count(2)
        g = gstar[n]
        ok = g <= 2*nu2+2
        if not ok: bad += 1
        print("%-6d %-8d %-10.1f %-8.1f %-8.3f %-6d %-8d %s"%(
            n, nu2, n**0.525, n/2, nu2/n, g, 2*nu2+2, ok))
    print("\nLemma 5.4 hypothesis failed at:", bad, "of the sampled n")

if __name__ == "__main__":
    main()
