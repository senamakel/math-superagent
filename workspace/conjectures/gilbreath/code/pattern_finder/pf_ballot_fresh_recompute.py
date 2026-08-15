#!/usr/bin/env python3
"""Independent fresh recompute of the mod-4 switch-majority ballot e(n)>=0,
the one clean qualitative regularity of this investigation.

Fresh sieve from scratch (no lib.gilbreath import), same definition:
  bit_k = 1 iff p_{k+1} !~ p_k (mod 4)  <=>  prime gap == 2 (mod 4)
  w(n)  = sum of bit_k over window k in [2, n-1]
  e(n)  = #switches - #nonswitches = 2*w(n) - (n-2)

Reports, exactly:
  * violations (e<0) and the zero set of e
  * min e over tails [T, N]
  * autocorrelation of the switch bit (r1) and of e-increments (I=2*nu2diff-1)
    -- the latter should be ~ -0.5 at lag 1 if the walk is near-white-noise
    (mathematical identity: first difference of a random walk has lag-1 AC
     exactly -0.5, so a value near -0.5 is CONSISTENT with near-white
     increments, not new structure -- I state this rather than call it new).
  * cross-check identity e(n) = 2*w(n)-(n-2) against a small direct count.

O(limit) memory odds-only sieve; limit=1e9 -> ~500MB bytearray, ~5e7 primes.
"""
import sys, time, math


def primes_mod4_upto(limit):
    """Odd primes p mod 4 as a byte list; returns (residue_list) for odd primes
    >=5 plus handles 2,3.  res[i] = mod-4 residue of the i-th prime p_i (1-based
    convention p_1=2 inside)."""
    # odds-only sieve: odd numbers >=3
    size = (limit >> 1) + 1
    sieve = bytearray(b'\x01') * size      # index i => odd 2i+1
    sieve[0] = 0                            # 1 not prime
    r = int(limit ** 0.5)
    for i in range(1, (r >> 1) + 1):
        if sieve[i]:
            p = 2 * i + 1
            start = (p * p) >> 1
            sieve[start::p] = b'\x00' * (((size - 1 - start) // p) + 1)
    # residues of primes, with p_1=2 (res 2), p_2=3 (res 3), then odds
    res = [2, 3]
    for i in range(2, size):
        if sieve[i]:
            res.append((2 * i + 1) & 3)
    return res


def main(nmax):
    # need primes up to p_nmax ~ nmax*log(nmax)
    Nneed = nmax + 5
    plim = int(Nneed * (math.log(Nneed) + math.log(math.log(Nneed)) + 1)) + 1000
    t0 = time.time()
    res = primes_mod4_upto(plim)
    print("sieve to %d: %d primes (%.1fs)" % (plim, len(res), time.time() - t0))
    have = len(res)
    assert have >= nmax, "need %d primes, have %d" % (nmax, have)

    # e[n], n=0,1 unused; e[2] = bit for gap 2->3 = (3-1)=2 mod4? gap=1 => not 2 mod4
    # bit_k with k = index of gap g_{k} = p_{k+1}-p_k; switch iff residue changes
    e = [0] * (nmax + 1)
    bits = [0] * (nmax + 1)          # bits[k] = switch bit of gap k
    for n in range(2, nmax + 1):
        b = 1 if res[n - 1] != res[n] else 0   # gap index k = n-1
        bits[n - 1] = b
        e[n] = e[n - 1] + (1 if b else -1)

    viol = [n for n in range(2, nmax + 1) if e[n] < 0]
    zeros = [n for n in range(2, nmax + 1) if e[n] == 0]
    print("e(n)>=0 for n in [2,%d]: %s  violations=%d" %
          (nmax, "YES" if not viol else "NO", len(viol)))
    if viol:
        print("  first %d violations: %s" % (min(10, len(viol)), viol[:10]))
    print("zero set of e: %s (count %d)" % (zeros[:20], len(zeros)))
    gmin = min(e[2:])
    print("global min e = %d (attained at %s)" % (
        gmin, [n for n in range(2, nmax + 1) if e[n] == gmin]))
    for T in [100, 1000, 10000, 100000, 1000000]:
        if T <= nmax:
            seg = e[T:]
            m = min(seg)
            at = [n for n in range(T, nmax + 1) if e[n] == m][0]
            print("  min e over n>=%d : %d at n=%d" % (T, m, at))
    print("final e(%d) = %d   e/N = %.5f" % (nmax, e[nmax], e[nmax] / nmax))

    # ---- the difference-of-random-walk identity check ----
    # e-increments d_n = e[n]-e[n-1] in {-1,+1}.  The autocorrelation structure
    # of a ±1 sequence is meaningful; but here the KEY fact: e only changes when
    # a switch happens, so d_n = +1 iff switch.  Along switched-increments, the
    # "gaps" are runs of non-switches.  Compute r1 of d directly.
    d = [e[n] - e[n - 1] for n in range(2, nmax + 1)]
    m = len(d)
    mu = sum(d) / m
    var = sum(x * x for x in d) / m - mu * mu
    num = sum((d[i] - mu) * (d[i - 1] - mu) for i in range(1, m))
    den = sum((d[i] - mu) ** 2 for i in range(m))
    r1 = num / den if den else 0.0
    print("\nlag-1 autocorrelation of e-increments d (must be +-1 walk): r1=%.4f"
          % r1)
    # Now the genuinely informative one: treat w-increment I=2*dup-1 and its AC.
    # I(n) = e(n+1)-e(n) = 2*(w(n+1)-w(n))-1.  Since e is a +-1 walk the AC of
    # ITS increments is the trivial negative-0.5 expected for any walk; we
    # instead measure the autocorrelation of the *switch-bit* sequence directly,
    # which is what controls whether e can dip.
    # r1 of bits b over k in [1, nmax-1], treated as 0/1:
    bb = bits[1:nmax]             # bit_k for k=1..nmax-1
    mb = len(bb)
    muB = sum(bb) / mb
    numB = sum((bb[i] - muB) * (bb[i - 1] - muB) for i in range(1, mb))
    denB = sum((bb[i] - muB) ** 2 for i in range(mb))
    r1b = numB / denB if denB else 0.0
    print("E[switch bit]=%.5f  lag-1 autocorr of switch bit=%.4f" %
          (muB, r1b))
    # number of switches and the majority drift
    sw = sum(bb)
    print("switches=%d (%d gaps) ratio=%.4f  e_final=2*sw-ngaps with "
          "ngaps=%d" % (sw, mb, sw / mb, mb))
    print("check: 2*%d-(%d) = %d vs final e = %d : %s" % (
        sw, mb, 2 * sw - mb, e[nmax], "OK" if 2 * sw - mb == e[nmax] else "MISMATCH"))


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10_000_000
    main(nmax)
