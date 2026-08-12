"""Small integer factorization helpers for the PE763 per-histogram structure
study: extracting the 2- and 3-adic valuations and the remaining cofactor."""


def f23(v):
    """Factor a positive integer v into (v2, v3, rest) where
    v = 2**v2 * 3**v3 * rest and rest is divisible by neither 2 nor 3.

    Used by the per-histogram multiplicity probes to write
    mult(hist) = 2**(2*n4) * 3**b * rest, testing the conjectured closed form
    for the 3-exponent b of each level-histogram's config-count.

    This is the single CANONICAL shared definition, consolidated verbatim
    from four identical copies formerly in code/pattern/check_3exp.py,
    code/pattern/check_b_multiset.py, code/pattern/multiset_to_b.py and
    code/pattern/tabulate_3exp.py.  The four copies had NOT diverged — each
    was exactly this loop — so no definition had to be chosen over another.
    Correctness established by those four probes agreeing with the
    authoritative whole-range check verify_mult_structure.py / the
    verify_mult_closedform.py closed-form test over the whole N=2..12 dump.
    """
    a = b = 0
    while v % 2 == 0:
        v //= 2
        a += 1
    while v % 3 == 0:
        v //= 3
        b += 1
    return a, b, v
