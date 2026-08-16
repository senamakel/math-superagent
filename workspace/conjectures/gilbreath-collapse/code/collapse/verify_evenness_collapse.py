"""Verify the evenness-collapse claim with the canonical oracle.

Claim: for every n and every h in F2^n, S(n,h) and S2(n,h) depend only on the
adjacent-XOR vector v(h) = (h_k XOR h_{k+1})_{k=0..n-2}.

(a) For each n in 3..12, group all 2^n strings h by v(h) and assert S, S2 are
    constant on each fiber.
(b) Report the fiber partition: each fiber must have size exactly 2 (the pair
    {h, not-h}), because ker(h -> v(h)) = {0, all-ones}.
(c) Negative control: compute S using XOR over an ODD-sized set (M_d minus its
    minimum vertex, size 2^{pc(d)} - 1 which is odd). This breaks the evenness
    that the constancy rests on, so the broken variant MUST FAIL constancy —
    proving the check measures something.  (Restricting to pc(d) odd would NOT
    break it: |M_d| = 2^{pc(d)} is still even for every d >= 2.)

Output: ../out/evenness_collapse.txt
"""

import sys
import os
from collections import Counter

from lib.collapse import downset, T, S, S2


def vvec(h):
    """Adjacent-XOR vector v(h) as a tuple of bits, length n-1."""
    return tuple(h[k] ^ h[k + 1] for k in range(len(h) - 1))


def all_strings(n):
    """All 2^n binary strings of length n, as lists of 0/1."""
    for mask in range(1 << n):
        yield [(mask >> j) & 1 for j in range(n)]


def T_odd(n, d, h):
    """Broken cell: XOR over M_d minus its min vertex => odd-sized set.
    |M_d| = 2^{pc(d)} even, so removing one vertex gives 2^{pc(d)}-1 odd.
    This destroys the evenness that makes S fiber-constant."""
    s = downset(d, n)          # frozenset, |s| = 2^{pc(d)} >= 2
    s2 = s - {min(s)}
    return sum(h[i] for i in s2) % 2


def S_broken(n, h):
    """Broken signed excess using odd-sized XOR sets."""
    w = sum(T_odd(n, d, h) for d in range(2, n))
    return (n - 2) - 2 * w


def main():
    out = []
    write = out.append

    write("=" * 72)
    write("Evenness-collapse verification using canonical oracle code/lib/collapse.py")
    write("=" * 72)

    all_ok = True

    for n in range(3, 13):
        # ---- build fibers ----
        fibers = {}   # v(h) -> list of h (as ints describing the string via bits)
        svals = {}    # v(h) -> set of S values seen
        s2vals = {}   # v(h) -> set of S2 values seen
        sbvals = {}   # v(h) -> set of broken-S values seen (negative control)

        for h in all_strings(n):
            v = vvec(h)
            fibers.setdefault(v, []).append(h)
            svals.setdefault(v, set()).add(S(n, h))
            s2vals.setdefault(v, set()).add(S2(n, h))
            sbvals.setdefault(v, set()).add(S_broken(n, h))

        nfib = len(fibers)
        sizes = Counter(len(hs) for hs in fibers.values())

        # (a) constancy of S and S2 on each fiber
        s_ok = all(len(svals[v]) == 1 for v in fibers)
        s2_ok = all(len(s2vals[v]) == 1 for v in fibers)

        # (b) fiber sizes all exactly 2
        size_ok = (len(sizes) == 1 and sizes.get(2) == nfib) and nfib == 2 ** (n - 1)

        # (c) negative control must FAIL constancy (broken S varies inside fibers)
        broken_ok = all(len(sbvals[v]) == 1 for v in fibers)

        line = (
            f"n={n:2d} | 2^n={1 << n:5d} | fibers={nfib:5d} "
            f"(expect {2 ** (n - 1):5d}) | fiber sizes={dict(sizes)} "
            f"| S const={s_ok} | S2 const={s2_ok} | size2_ok={size_ok} "
            f"| BROKEN const={broken_ok} (must be False)"
        )
        write(line)
        if not (s_ok and s2_ok and size_ok):
            all_ok = False
        if broken_ok:
            # broken variant should vary within some fiber
            all_ok = False
            write(f"    !! negative control did NOT fail at n={n} — check is meaningless")

    # ---- direct check of the fiber={h,not-h} structure on a sample ----
    write("-" * 72)
    write("Direct fiber structure: v(h) == v(not-h) and every fiber is {h, not-h}.")
    for n in (4, 8, 12):
        ok = True
        for h in all_strings(n):
            nh = [1 - b for b in h]
            if vvec(h) != vvec(nh):
                ok = False
        write(f"  n={n}: v(h)==v(not-h) for all 2^{n}={1 << n} strings: {ok}")
        if not ok:
            all_ok = False

    write("-" * 72)
    write(
        "Why (a,b) hold: ker(h->v(h))={0,all-ones} so fibers are {h,not-h}; "
        "T is invariant under h->not-h because |M_d|=2^{pc(d)} is even for d>=2. "
        "The negative control XORs over an odd-sized set (|M_d|-1), so T flips "
        "under complement and S' is anti-symmetric on each fiber — it MUST vary."
    )
    write(f"ALL CONSTANCY CHECKS PASSED: {all_ok}")
    write("(Note: a 'False' under BROKEN const is the desired negative-control outcome)")

    text = "\n".join(out) + "\n"
    print(text)

    # write to temp, then move on success
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        os.pardir, "out", "evenness_collapse.txt")
    dest = os.path.normpath(dest)
    tmp = dest + ".tmp"
    with open(tmp, "w") as f:
        f.write(text)
    os.replace(tmp, dest)
    print(f"wrote {dest}")


if __name__ == "__main__":
    main()
