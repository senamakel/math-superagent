#!/usr/bin/env python3
"""2-adic (FCSR) complexity measurement for binary strings.

Exact-integer implementation of the classical rational-approximation /
Euclidean-algorithm route to the 2-adic linear complexity.

Definition (Goresky--Klapper).  Given a binary string s_0..s_{N-1} (s_0 the
first bit, LSB of the 2-adic integer alpha = sum_i s_i 2^i), a feedback-with-
carry (FCSR / rational) generator with odd connection integer q produces these
first N bits iff its generating rational p/q satisfies

    p  =  alpha * q  (mod 2^N),   q odd,  gcd(p,q) = 1.

The 2-adic linear complexity of the N-bit prefix is

    lambda_N  =  min{ max(|p|, |q|) : p = alpha q (mod 2^N), q odd,
                      gcd(p,q) = 1 }.

Writing p = alpha*q - 2^N*m we need alpha*q ~ 2^N*m, i.e. m/q best-
approximates r = alpha/2^N, and |p| = 2^N * |r*q - m|.  The best pairs are the
convergents (and semiconvergents) of the continued fraction of r, found by the
Euclidean algorithm on (2^N, alpha) in O(N) division steps (each step on
N-bit integers), i.e. O(N^3) bit operations worst case but ~O(N^2) in
practice with CPython big ints.

fcsr_lambda_bits(s)     : exact lambda_N for the prefix of length N = len(s);
                          also returns the witness (q, p, m).
fcsr_lambda_prefix(s)   : list [lambda_1..lambda_N] for every prefix.
brute_lambda_bits(s,cap): exhaustive oracle (only for small N) - the check the
                          fast method is validated against.
kernel_size(s)          : # distinct dyadic-substring subsequences
                          s[2^k*m .. 2^k*(m+1)-1] over all m>=0 and all k with
                          2^k*(m+1) <= N (the 2-kernel proxy).
zero_run_stats(s)       : (number of maximal zero-runs, longest zero-run,
                          main zero-run weights) over the bits.

Required: exact integer arithmetic only.
"""
from math import gcd as _gcd


def _alphabet_to_int(bits):
    """bits: list/str of 0/1, bits[0] is the first bit (LSB of the 2-adic
    integer).  Returns alpha = sum bits[i] * 2^i."""
    alpha = 0
    for bit in reversed(bits):
        alpha = (alpha << 1) | int(bit)
    return alpha


def _cf_terms(num, den):
    """Continued-fraction partial quotients of num/den (den>0)."""
    a, b = num, den
    out = []
    while b:
        q = a // b
        out.append(q)
        a, b = b, a - q * b
    return out


def _cf_convergents(num, den):
    """All convergents (m_k, q_k) of num/den as a list, in order of
    increasing denominator.  (num,den) any ratio; returns pairs."""
    terms = _cf_terms(num, den)
    # recurrence: n_{-2}=0, n_{-1}=1 ; n_k = a_k n_{k-1} + n_{k-2}
    nm2, nm1 = 0, 1
    dm2, dm1 = 1, 0
    convs = []
    for a in terms:
        n = a * nm1 + nm2
        d = a * dm1 + dm2
        convs.append((n, d))
        nm2, nm1 = nm1, n
        dm2, dm1 = dm1, d
    return convs


def _candidate_pairs(alpha, N):
    """Best (q, p) candidate pairs satisfying p = alpha*q mod 2^N, q odd,
    from the continued fraction of r = alpha/2^N plus the semiconvergents
    around each convergent (so the odd-q optimum is not missed).  Yields
    (q, p) with p the exact centered error p = alpha*q - 2^N*m."""
    rnum, rden = alpha, (1 << N)
    convs = _cf_convergents(rnum, rden)
    twon = 1 << N
    seen = set()
    # add convergents and their semiconvergents (c * prev + last, c>=1)
    cands = []
    # add semiconvergents explicitly by recomputing with the terms
    terms = _cf_terms(rnum, rden)
    nm2, nm1 = 0, 1
    dm2, dm1 = 1, 0
    for a in terms:
        # Semiconvergents with this partial quotient a_k are
        #   (j * p_{k-1} + p_{k-2}) / (j * q_{k-1} + q_{k-2}),  j = 0..a_k.
        # Here nm1/dm1 = (p_{k-1}, q_{k-1}), nm2/dm2 = (p_{k-2}, q_{k-2}).
        for c in range(0, a + 1):
            cands.append((c * nm1 + nm2, c * dm1 + dm2))
        # advance: new convergent, shift indices
        n = a * nm1 + nm2
        d = a * dm1 + dm2
        nm2, nm1 = nm1, n
        dm2, dm1 = dm1, d

    out = []
    for (m, q) in cands:
        if q == 0:
            continue
        if q % 2 == 0:
            continue            # FCSR requires odd q
        p = alpha * q - twon * m      # exact, satisfies the congruence
        out.append((q, p))
    return out


def fcsr_lambda_bits(bits):
    """Exact 2-adic linear complexity lambda_N for the prefix bits (bits[0]
    first).  Returns (lambda_value, witness (q,p,m)) where witness minimizes
    max(|p|,|q|) among valid odd-q pairs found by the CF search.  For small N
    use brute_lambda_bits to confirm the CF search captures the optimum."""
    alpha = _alphabet_to_int(bits)
    N = len(bits)
    if N == 0:
        return 0, (0, 0, 0)
    elif N == 1:
        # bits: [1] -> alpha=1, p=q=1;  [0] -> alpha=0, p=0, q=1
        if alpha == 0:
            return 1, (1, 0, 0)
        return 1, (1, 1, 0)
    cands = _candidate_pairs(alpha, N)
    best = None
    bestpair = None
    for (q, p) in cands:
        if _gcd(abs(p), abs(q)) != 1:
            continue
        val = max(abs(p), abs(q))
        if best is None or val < best:
            best = val
            bestpair = (q, p)
    if bestpair is None:
        # fall back to q = 1 : p = alpha,  lambda = max(alpha, 1)
        q, p = 1, alpha
        return max(abs(p), abs(q)), (q, p, 0)
    m = (alpha * bestpair[0] - bestpair[1]) >> N
    return best, (bestpair[0], bestpair[1], m)


def fcsr_lambda_prefix(bits, start=1):
    """lambda_N for N = start..len(bits), as a list aligned so
    result[N - start] = lambda_N."""
    out = []
    for N in range(start, len(bits) + 1):
        lam, _ = fcsr_lambda_bits(bits[:N])
        out.append(lam)
    return out


def brute_lambda_bits(bits, qcap=None):
    """Exhaustive oracle (small N only): enumerate every odd q <= qcap,
    compute centered p = alpha*q mod 2^N, take min max(|p|,|q|) over
    gcd(p,q)=1.  qcap default = 2^{N//2+1} (generous; optimum ~2^{N/2})."""
    alpha = _alphabet_to_int(bits)
    N = len(bits)
    twon = 1 << N
    half = 1 << (N - 1) if N > 0 else 0
    if qcap is None:
        # The lattice-minimising q can be as large as ~2^(N/2)+; give the
        # oracle generous headroom so it sees the true optimum.
        qcap = max(1, 1 << (N // 2 + 5))
    best = None
    for q in range(1, qcap + 1, 2):
        # centered representative of alpha*q mod 2^N in (-half, half]
        p = (alpha * q) % twon
        if p > half:
            p -= twon
        if _gcd(abs(p), abs(q)) != 1:
            continue
        val = max(abs(p), abs(q))
        if best is None or val < best:
            best = val
    return best


def kernel_size(bits):
    """Size of the 2-kernel: number of distinct substrings
    s[2^k*m .. 2^k*(m+1)-1] over all m>=0 and all k with 2^k*(m+1) <= N,
    i.e. consecutive blocks of length 2^k at dyadic-dividing offsets that lie
    wholly inside the string.  Returns an int.  This is a well-defined proxy
    (an automatic / 2-automatic sequence like Thue-Morse must have a finite
    2-kernel, hence a small count; a random string has ~ N^2/2 of them)."""
    N = len(bits)
    seen = set()
    k = 0
    while (1 << k) * 1 <= N:
        L = 1 << k
        # all dyadic-aligned blocks: start m*L for m>=0 with (m+1)*L <= N
        # (i.e. the whole block inside the string)
        for m in range(0, N // L):
            start = m * L
            block = tuple(bits[start:start + L])
            seen.add(block)
        k += 1
    return len(seen)


def zero_run_stats(bits):
    """(num_zero_runs, longest_zero_run) over the bit string: maximal runs of
    consecutive 0 valued bits."""
    num = 0
    longest = 0
    cur = 0
    for b in bits:
        if b == 0:
            cur += 1
            longest = max(longest, cur)
        else:
            if cur:
                num += 1
            cur = 0
    if cur:
        num += 1
    return num, longest


def hamming_weight(bits):
    return sum(1 for b in bits if b)
