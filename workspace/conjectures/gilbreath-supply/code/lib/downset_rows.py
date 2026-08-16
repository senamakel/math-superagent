"""The fold's row set: the translated digital down-set and its distance code.

For the SUPPLY fold Phi_n the depth-d row is

    M_d = { n-1-d+o : o a bitwise submask of d },      d in [2, n-1].

Each M_d is a subset of the n-window (positions 0..n-1) with even size
|M_d| = 2^popcount(d). We expose the row as an n-bit integer mask, the
symmetric-difference distance between rows (= popcount of the XOR of the two
masks), and the distance distribution A_k of the pair family together with the
distance enumerator F_n(z) = sum_{d,d'} z^{dist(d,d')}.

All arithmetic exact (non-negative ints / Fractions). Everything here is a pure
function of Phi_n -- no input h enters.
"""


def popcount(x):
    """Number of 1-bits of a non-negative int."""
    return bin(x).count("1")


def row_positions(n, d):
    """Positions j in [0, n-1] of row M_d of Phi_n (the translated down-set).

    j in M_d iff j = n-1-d+o for some o that is a bitwise submask of d and
    o in [0, d]. Since d < n, these j land in [n-1-d, n-1] subset [0, n-1].
    """
    pos = set()
    for o in range(d + 1):
        if (o & d) == o:            # o bitwise submask of d
            pos.add(n - 1 - d + o)
    return pos


def row_mask(n, d):
    """n-bit integer mask of row M_d: bit j set iff j in M_d."""
    m = 0
    for o in range(d + 1):
        if (o & d) == o:
            m |= 1 << (n - 1 - d + o)
    return m


def row_masks(n):
    """List of row masks for d = 2..n-1 (length n-2), in d order."""
    return [row_mask(n, d) for d in range(2, n)]


def row_size(n, d):
    """|M_d| = 2^popcount(d); row has even size."""
    return 1 << popcount(d)


def row_dist(mask_a, mask_b):
    """Symmetric-difference distance |M_a XOR M_b| = popcount of XOR of masks."""
    return (mask_a ^ mask_b).bit_count()


def distance_distribution(n):
    """Distance distribution A_k = #{ d != d' in [2,n-1] : dist(d,d') = k }.

    Returns a dict {k: count} for k >= 1 (off-diagonal only), the number of
    rows (n-2), and the full list of masks. A_0 would be the diagonal (n-2),
    A_1 = 0 (all rows even => distances even, >= 2).
    """
    masks = row_masks(n)
    A = {}
    for i in range(len(masks)):
        for j in range(i + 1, len(masks)):
            k = row_dist(masks[i], masks[j])
            A[k] = A.get(k, 0) + 1
    return A, len(masks), masks


def enumerator(n, z, masks=None):
    """F_n(z) = sum_{d,d'} z^{dist(d,d')} over all pairs of rows (incl. diagonal).

    z may be an int, Fraction, or float. Diagonal (d=d') contributes n-2 terms
    of z^0 = 1. Uses the given masks, or computes them from n.
    """
    if masks is None:
        masks = row_masks(n)
    total = len(masks)              # diagonal: (n-2) terms, each z^0 = 1
    for i in range(len(masks)):
        for j in range(i + 1, len(masks)):
            k = row_dist(masks[i], masks[j])
            total += 2 * (z ** k)
    return total


def cross_character_sum(n, masks=None):
    """Walsh spectrum of the row set: C_n^hat(omega) = sum_d (-1)^{<omega, 1_M_d>}.

    Returns a dict {omega: C} for omega in [0, 2^n). <omega, 1_M_d> =
    popcount(omega & mask_d). Exact ints. n must be small enough that 2^n is
    feasible.
    """
    if masks is None:
        masks = row_masks(n)
    spec = {}
    for omega in range(1 << n):
        c = 0
        for m in masks:
            if (omega & m).bit_count() & 1:
                c -= 1
            else:
                c += 1
        spec[omega] = c
    return spec


def krawtchouk_enumerator(n, z, spec=None):
    """Krawtchouk diagonalization of F_n(z):
        F_n(z) = 2^{-n} sum_omega (1-z)^{wt(omega)} (1+z)^{n-wt(omega)} C_n^hat(omega)^2.
    Exact if z is exact (int/Fraction). Returns a Fraction.
    """
    from fractions import Fraction
    z = Fraction(z)
    if spec is None:
        spec = cross_character_sum(n)
    total = Fraction(0)
    for omega, c in spec.items():
        w = popcount(omega)
        total += Fraction(((1 - z) ** w) * ((1 + z) ** (n - w)) * (c * c))
    return total / (1 << n)
