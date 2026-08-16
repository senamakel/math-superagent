#!/usr/bin/env python3
"""SUPPLY endpoint-comparison density: T(n,d) and S(n).

SUPPLY (problem.md): nu2(n) = wt(Phi_n h) over F2, h[j] = [q_{j+1} != q_j mod 4],
q the primes. The depth-d fold cell is

    T(n,d) = XOR over submasks o of d of  h[n-1-d+o],

with h[j] = [r_{j+1} != r_j], r_j = q_j mod 4. We study

    S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)}

and the empirical density of T(n,d)=1 over d in [2, n-1]. Expected (balanced /
uncorrelated endpoint comparisons): density ~ 1/2 and S(n) small, i.e.
|S(n)| <= (1-2c)n as the lemma's equivalent form.

KEY IDENTITY (the mathematical reduction everything below rests on):
with s = d - o, as o runs over bitwise submasks of d there is no borrow
(since o <= d bitwise), so s also runs over the submasks of d and
n - 1 - d + o = n - 1 - (d - o) = n - 1 - s. Hence

    T(n,d) = XOR_{s subseteq d} h[n-1-s],

T(n,d) is the digital submask zeta-XOR of the reversed window, and

    (-1)^{T(n,d)} = prod_{s subseteq d} tau_{n-1-s},   tau_j = (-1)^{h[j]}.

So S(n) and the density are computed by a submask-product SOS transform in
O(n log n) per n, checked against the direct submask-XOR oracle.

NOTE on T(n,d): indices n-1-d .. n-1, so h must be defined through index n-1;
for the primes that means r up to q_{n+1}.

All arithmetic exact (parities / +-1 products); only the ratio density is a float.
"""


def h_from_r(r):
    """h[j] = [r[j+1] != r[j]] for j = 0..len(r)-2. r[j] = q_{j+1} mod 4."""
    return [1 if r[j + 1] != r[j] else 0 for j in range(len(r) - 1)]


def t_direct(n, d, h):
    """Oracle: T(n,d) by the literal definition, XOR over bitwise submasks o of
    d of h[n-1-d+o]. Exact. h indexed 0..n-1 (min length n)."""
    x = 0
    for o in range(d + 1):
        if (o & d) == o:          # o is a bitwise submask of d
            x ^= h[n - 1 - d + o]
    return x


def s_direct(n, h):
    """Oracle: S(n) by literal definition, sum of (-1)^{T(n,d)} over
    d = 2..n-1, each T computed by t_direct. Exact. O(n * 2^w) worst case."""
    total = 0
    ones = 0
    for d in range(2, n):
        t = t_direct(n, d, h)
        total += -1 if t else 1
        ones += t
    return total, ones


def _next_pow2(k):
    p = 1
    while p < k:
        p <<= 1
    return p


def s_sos(n, h):
    """S(n) and the count of T=1 via the submask-product transform.

    With tau_j = (-1)^{h[j]}, (-1)^{T(n,d)} = prod_{s subseteq d} tau_{n-1-s}.
    Let b_t = tau_{n-1-t} for t = 0..n-1; then the d-th term is the product
    over submasks s of d of b_s, computed by the AND/submask SOS product:
    for each bit, g[x] *= g[x ^ bit]. Pad b with 1s to a power of two >= n.

    O(n log n) time and O(n) space, exact. Returns (S(n), count_of_T_equals_1)
    for d in [2, n-1].
    """
    b = [1 - 2 * h[j] for j in range(n)]            # tau's in original order
    # reindex to b_t = tau_{n-1-t}: b_t = tau_{n-1-t} -> list[ t ] = tau[n-1-t]
    barray = [b[n - 1 - t] for t in range(n)]
    size = _next_pow2(n)
    g = [1] * size
    for t in range(n):
        g[t] = barray[t]
    # submask product: for x with bit set, g[x] *= g[x ^ bit]
    bit = 1
    while bit < size:
        for x in range(size):
            if x & bit:
                g[x] *= g[x ^ bit]
        bit <<= 1
    total = 0
    ones = 0
    for d in range(2, n):
        term = g[d]
        total += term
        if term == -1:
            ones += 1
    return total, ones


def s_terms_sos(n, h):
    """List of per-depth terms t[d] = (-1)^{T(n,d)} for d = 2..n-1, via the
    same submask-product SOS transform as s_sos but keeping every diagonal
    term instead of summing. Position i corresponds to d = i+2. Exact,
    O(n log n) time, O(n) space. Sum(terms) == s_sos(n,h)[0] and the count of
    -1 equals s_sos(n,h)[1]; passed on n=200 (and small n) against the literal
    s_direct/s_char_runs totals in code/dyadic/stratify_by_popcount.py."""
    b = [1 - 2 * h[j] for j in range(n)]             # tau_j = (-1)^{h[j]}
    barray = [b[n - 1 - t] for t in range(n)]        # b_t = tau_{n-1-t}
    size = _next_pow2(n)
    g = [1] * size
    for t in range(n):
        g[t] = barray[t]
    bit = 1
    while bit < size:
        for x in range(size):
            if x & bit:
                g[x] *= g[x ^ bit]
        bit <<= 1
    return [g[d] for d in range(2, n)]


def report(n, h, label):
    Sd, ones_d = s_direct(n, h)
    Ss, ones_s = s_sos(n, h)
    assert Sd == Ss and ones_d == ones_s, (n, Sd, Ss, ones_d, ones_s)
    nd = n - 2                       # number of d values (2..n-1)
    density = ones_d / nd if nd else 0.0
    return dict(n=n, label=label, S=Sd, ones=ones_d, nd=nd,
                density=density, absS_over_n=abs(Sd) / n)


def runs_of_downset(d):
    """Maximal runs (consecutive-integer intervals) of the digital down-set
    {o in [0,d] : o bitwise-submask of d}. From G-run-telescope:
    g = nu2(d+1) (number of trailing 1 bits of d, i.e. the position of d's
    lowest 0 bit); each run has length 2^g and there are 2^{popcount(d)-g} of
    them: blocks [m*2^g, (m+1)*2^g - 1] for the 2^{popcount(d)-g} top-bit
    choices m. Returns list of (u,v) inclusive."""
    g = 0
    while d & 1:
        g += 1
        d >>= 1
    runlen = 1 << g
    d_shifted = d                      # d after stripping the g low bits
    runs = []
    for m in range(1 << d_shifted.bit_length()):
        # top-bits choice between 0 and the remaining value of d
        if m > d_shifted:
            break
        if (m & d_shifted) != m:
            continue
        u = m * runlen
        v = u + runlen - 1
        runs.append((u, v))
    return runs


def s_char_runs(n, r):
    """S(n) via the run-endpoint character-sum form (G-run-telescope):
    (-1)^{T(n,d)} = prod_R chi(r_{a_R}) chi(r_{b_R})  since T = XOR_R I_R and
    [r_a != r_b] is 1 iff chi(r_a)chi(r_b) = -1, so (-1)^{I_R}=chi(r_a)chi(r_b).
    chi the nontrivial character mod 4 (chi(x) = -1 iff x == 3), a_R =
    n-1-d+u, b_R = n-1-d+v+1 for each run R=[u,v] of the downset of d.
    A genuinely different route (uses the residue string r directly, not h).
    Verified equal to the SOS route on n=4..59.
    Exact. Requires r of length n+1 (r[j] = q_{j+1} mod 4, j=0..n)."""
    chi = lambda x: -1 if x % 4 == 3 else 1
    total = 0
    ones = 0
    for d in range(2, n):
        runs = runs_of_downset(d)
        prod = 1
        for (u, v) in runs:
            a = n - 1 - d + u
            b = n - 1 - d + v + 1
            prod *= chi(r[a]) * chi(r[b])
        term = prod
        total += term
        if term == -1:
            ones += 1
    return total, ones
