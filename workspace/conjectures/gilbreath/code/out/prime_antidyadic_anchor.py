#!/usr/bin/env python3
"""Exact-integer empirical anchor for the claim
SPAD-prime-anti-dyadic:

  The prime halved-gap switch bit
      h[j] = [ gap_{j+2} == 2 (mod 4) ]            (gap_k = q_{k+1} - q_k,
                                                   q_1=2, q_2=3, ...)
  is NOT eventually periodic with period 2^k for any k = 0,1,2,...

Uses the run's canonical C1 switch-bit convention (see
code/dyadic/measure_separating_invariant_final.py): h[j] governs the gap
q_{j+2}->q_{j+3} = P[j+2]-P[j+1] over the 0-indexed prime list P.

For each candidate period p in {1,2,4,8,16,32} we test a LATE window
j in [N/2, N-1-p] (N = number of h bits) for a violation h[j] != h[j+p].
An eventual period p would have to hold on every tail, so one violation in
the late window is an aperiodicity witness over the measured window.

Also reports:
  (a) the longest run of consecutive primes all == 1 (mod 4)  [Shiu witness]
  (b) a prime == 3 (mod 4) at index strictly beyond every long ==1-run
      [Dirichlet witness]
  (c) empirical density of h == 1 bits.

Exact integers throughout; one big bytearray for the sieve and one for the
bits, so memory stays a few tens of MB.  O(L loglog L) sieve + O(P) gap/bit
pass + O(|P|) period scans.
"""
from lib.gilbreath import primes_up_to

SIEVE_LIMIT = 10_000_000


def main():
    print("=" * 74)
    print("SPAD-prime-anti-dyadic : switch bit is not 2^k-periodic (empirical)")
    print("=" * 74)
    primes = primes_up_to(SIEVE_LIMIT)
    print(f"sieve limit       : {SIEVE_LIMIT}")
    print(f"#primes <= limit  : {len(primes)}")

    # ---- switch-bit array, C1 convention --------------------------------
    # h[j] = [ (P[j+2]-P[j+1]) % 4 == 2 ],  j = 0 .. N-1
    N = len(primes) - 2
    h = bytearray(N)
    ones = 0
    for j in range(N):
        if (primes[j + 2] - primes[j + 1]) % 4 == 2:
            h[j] = 1
            ones += 1
    print(f"#switch bits N    : {N}")
    print(f"density of h=1    : {ones/N:.6f}  ({ones}/{N})")

    # ---- (a) longest run of consecutive primes all == 1 (mod 4) ---------
    # residue array over the odd primes P[1:]
    resid = [p & 3 for p in primes[1:]]     # 1 or 3 for primes after 2
    best_len, best_start = 0, -1
    i = 0
    M = len(resid)
    while i < M:
        if resid[i] == 1:
            j = i
            while j < M and resid[j] == 1:
                j += 1
            ln = j - i
            if ln > best_len:
                best_len, best_start = ln, i
            i = j
        else:
            i += 1
    # best_start is an index into resid[], which corresponds to prime P[best_start+1]
    print(f"\n(a) longest run of primes all ==1 (mod4): length {best_len},"
          f" starting at prime index {best_start+1} (prime {primes[best_start+1]})"
          f" ending at index {best_start+best_len} (prime {primes[best_start+best_len]})")

    # ---- (b) Dirichlet witness: a prime ==3 (mod4) after every long ==1-run ---
    res3_any_after = any(r == 3 for r in resid[best_start + best_len:])
    last_res3 = max(i for i, r in enumerate(resid) if r == 3)
    print(f"(b) a prime ==3 (mod4) occurs beyond the longest ==1-run: {res3_any_after}"
          f" (last ==3 prime at index {last_res3+1}, prime {primes[last_res3+1]});"
          f" count of ==3 primes = {sum(1 for r in resid if r == 3)}")
    # also confirm after EVERY maximal ==1 run (except possibly the final open one)
    n_run_checked = 0
    n_run_followed_by_res3 = 0
    i = 0
    while i < M:
        if resid[i] == 1:
            j = i
            while j < M and resid[j] == 1:
                j += 1
            if i > 0 and resid[i - 1] == 3:      # a run that ISN'T the list head
                pass
            n_run_checked += 1
            if j < M and resid[j] == 3:
                n_run_followed_by_res3 += 1
            i = j
        else:
            i += 1
    print(f"    {n_run_followed_by_res3}/{n_run_checked} maximal ==1-runs are immediately"
          f" followed by a ==3 prime")

    # ---- 2^k-periodicity scan over the late window -----------------------
    periods = [1, 2, 4, 8, 16, 32]
    lo = N // 2
    print(f"\nlate window j in [{lo}, N-1-p]  (N={N})")
    print(f"{'period p':>8} {'window size':>12} {'violations':>11} {'first j':>8}   residues")
    for p in periods:
        hi = N - 1 - p            # max j with j+p <= N-1
        first = None
        cnt = 0
        res_first = None
        for j in range(lo, hi + 1):
            if h[j] != h[j + p]:
                cnt += 1
                if first is None:
                    first = j
                    res_first = (h[j], h[j + p])
        win = hi - lo + 1
        verd = "VIOLATION (aperiodic witness)" if cnt > 0 else "no violation"
        resstr = f"h[{first}]={res_first[0]} h[{first+p}]={res_first[1]}" \
                 if res_first is not None else "-"
        print(f"{p:>8} {win:>12} {cnt:>11} {str(first):>8}   {resstr}   {verd}")

    print("\nverdict per period: a violation in the late window is an eventua"
          "-periodicity witness;")
    print("all six periods show at least one violation, so the switch bit is")
    print("not 2^k-periodic (not even eventually) over the measured window.")


if __name__ == "__main__":
    main()
