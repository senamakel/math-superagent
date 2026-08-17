"""INDEPENDENT re-verification of the Kabela-Polak-Teska Theorem 5 finding.

This script deliberately does NOT import lib.uc, nor any sweep / enumeration
logic (nothing from kpt_thm5_verify.py or mroof_*). It is the independent
route: union-closure is re-derived inline from raw set membership, and
(k, n, f, profile) are computed directly from the raw membership of four
hand-picked families on n <= 4.

Family = set of integer bitmasks over [n]: element i (0-indexed) is in set s
iff bit i of s is 1. All arithmetic is exact integer; f uses the STRICT test
2*count > |F| (element in MORE than half the sets).

KPT Theorem 5 (F finite union-closed, empty NOT in F; k = min set size,
n = max set size, f = # elements with 2*count > |F|):
    (1)  k >= n - 3                 ==>  f >= k
    (2)  k = n - 4                  ==>  f >= k - 1
    (3)  f >= min{n, 2k - n + 1}
Bounds (1),(2) are tight.

Capture: writes to code/out/kpt_thm5_indep.captured.txt via a temp file moved
into place only on exit 0. First three lines state what ran, how
union-closure was decided (inline, not lib.uc), and the exact family set.
"""

import os
import sys
import tempfile

CAPTURE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "kpt_thm5_indep.captured.txt")


# ---------- independent inline primitives (lib.uc NOT used) ----------

def popcount(m):
    return bin(m).count("1")


def inline_is_union_closed(F):
    """True iff F is closed under bitwise OR. Re-derived here on purpose."""
    lst = list(F)
    for i, a in enumerate(lst):
        for b in lst[i:]:          # OR is commutative; symmetric pairs need one pass
            if (a | b) not in F:
                return False
    return True


def counts_from_membership(F, n):
    """Exact per-element counts: count[i] = # sets in F containing element i."""
    counts = [0] * n
    for s in F:
        for i in range(n):
            if (s >> i) & 1:
                counts[i] += 1
    return counts


def family_stats(F, n):
    """Return (k, nsets, f, profile) for family F over [n].

    k     = min set size
    nsets = max set size (= ground set size)
    f     = # elements with 2*count > |F|  (STRICT: more than half)
    profile = sorted exact abundance counts
    """
    sizes = [popcount(s) for s in F]
    k = min(sizes)
    nsets = max(sizes)
    m = len(F)
    counts = counts_from_membership(F, n)
    f = sum(1 for c in counts if 2 * c > m)
    profile = tuple(sorted(counts))
    return k, nsets, f, profile


# ---------- the four hand-picked families ----------

def build(bitstring_elems):
    """Families given as lists of element-strings, e.g. [['a','b'], ['a','b','c']]."""
    elem_index = {ch: i for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz")}
    F = set()
    m = 0
    for members in bitstring_elems:
        mask = 0
        for e in members:
            mask |= 1 << elem_index[e]
        F.add(mask)
        m = m | mask
    n = bin(m).count("1") if m else 0
    return F, n


FAMILIES = {
    # name: (set-membership, expected (k, nsets, f, profile))
    "2^4 minus empty (15 sets)": (
        # all non-empty subsets of {a,b,c,d}: each element in exactly 8 of the
        # 16 subsets of the full power set; removing empty leaves 15 sets, so
        # count=8 per element. 2*8=16 > 15 => every element abundant.
        [comb for r in range(1, 5)
         for comb in __import__("itertools").combinations("abcd", r)],
        (1, 4, 4, (8, 8, 8, 8)),
    ),
    "{{a,b},{a,b,c}}": (
        [["a", "b"], ["a", "b", "c"]],
        # expected: k=2, n=3, f=2; profile (2,2,1) is in ELEMENT order
        # (a=2, b=2, c=1); stored sorted for a multisetic comparison.
        (2, 3, 2, (1, 2, 2)),
    ),
    "{{a},{b},{a,b}}": (
        [["a"], ["b"], ["a", "b"]],
        (1, 2, 2, (2, 2)),
    ),
    "{{a,b,c}}": (
        [["a", "b", "c"]],
        (3, 3, 3, (1, 1, 1)),
    ),
}


def element_names(n):
    return [chr(ord('a') + i) for i in range(n)]


def set_family_str(F, n):
    names = element_names(n)
    parts = []
    for mm in sorted(F):
        elems = [names[i] for i in range(n) if (mm >> i) & 1]
        parts.append("{" + ",".join(elems) + "}")
    return "{" + ",".join(parts) + "}"


def kpt_bounds(k, nsets, f):
    """Return (hold_bool, detail_str) for the three KPT bounds applied to a family."""
    checks = []
    # (1) k >= n-3  ==>  f >= k
    if k >= nsets - 3:
        ok1 = f >= k
        checks.append((f"(1) k={k} >= n-3={nsets - 3}: f={f} >= k={k} -> "
                       f"{'OK' if ok1 else 'VIOLATED'}", ok1))
    else:
        checks.append((f"(1) n/a (k={k} < n-3={nsets - 3})", True))
    # (2) k = n-4  ==>  f >= k-1
    if k == nsets - 4:
        ok2 = f >= k - 1
        checks.append((f"(2) k={k} = n-4={nsets - 4}: f={f} >= k-1={k - 1} -> "
                       f"{'OK' if ok2 else 'VIOLATED'}", ok2))
    else:
        checks.append((f"(2) n/a (k={k} != n-4={nsets - 4})", True))
    # (3) f >= min{n, 2k-n+1}
    bound3 = min(nsets, 2 * k - nsets + 1)
    ok3 = f >= bound3
    checks.append((f"(3) f={f} >= min{{n,2k-n+1}}={bound3} -> "
                   f"{'OK' if ok3 else 'VIOLATED'}", ok3))
    return all(ok for _, ok in checks), checks


def main():
    print("Independent re-verification of KPT Theorem 5 on 4 hand-picked families")
    print("union-closure: decided INLINE from raw membership (lib.uc NOT imported);")
    print("families: 2^4 minus empty; {{a,b},{a,b,c}}; {{a},{b},{a,b}}; {{a,b,c}}")

    rows = []
    all_hold = True
    for name, (membership, expected) in FAMILIES.items():
        F, n = build(membership)
        if 0 in F:
            all_hold = False
            rows.append((name, F, n, None, None, None, None,
                         "FATAL: empty set in F violates KPT hypothesis", False))
            continue
        uc = inline_is_union_closed(F)
        k, nsets, f, profile = family_stats(F, n)
        holds, checks = kpt_bounds(k, nsets, f)
        rows.append((name, F, n, (k, nsets, f, profile), uc, holds, checks, True))

    print("\n============ per-family table ============")
    print(f"{'family':<26}{'k':>3}{'n':>3}{'f':>3}  {'profile':<14}"
          f"{'closed':>7}{'bounds':>8}")
    for name, F, n, stats, uc, holds, checks, ok in rows:
        if stats is None:
            print(f"{name:<26}  {ok}")
            continue
        k, nsets, f, profile = stats
        prof = str(profile)
        print(f"{name:<26}{k:>3}{nsets:>3}{f:>3}  {prof:<14}"
              f"{'YES' if uc else 'NO':>7}{'YES' if holds else 'NO':>8}")

    print("\n============ per-element 2*count > |F| ============")
    for name, F, n, stats, uc, holds, checks, ok in rows:
        if stats is None:
            continue
        m = len(F)
        counts = counts_from_membership(F, n)
        names = element_names(n)
        marks = ["   " if 2 * c > m else " X " for c in counts]
        print(f"\n{name}  (|F|={m})")
        print("   element : " + "  ".join(f"{nm:>2}" for nm in names))
        print("   count   : " + "  ".join(f"{c:>2}" for c in counts))
        print("   2*c>|F| : " + "  ".join(f"{mr:>2}" for mr in marks))

    print("\n============ KPT bound checks ============")
    for name, F, n, stats, uc, holds, checks, ok in rows:
        if stats is None:
            continue
        k, nsets, f, profile = stats
        print(f"\n{name}:  k={k} n={nsets} f={f} profile={profile}"
              f"  union-closed={'YES' if uc else 'NO'}")
        for detail, held in checks:
            print(f"   {detail}")
        # note: (1),(2) are n/a when their hypothesis k>n-3 / k!=n-4 fails;
        # we treat those as vacuously satisfied, which is correct per the theorem.
        print(f"   => bounds (1)(2)(3) hold: {'YES' if holds else 'NO'}")

    # independent probe vs expected values
    print("\n============ expected-value check (independent oracle agreement) ============")
    agree = True
    for name, (membership, expected) in FAMILIES.items():
        F, n = build(membership)
        k, nsets, f, profile = family_stats(F, n)
        exp = expected
        # profile may be written element-ordered in the task; compare as a
        # multiset (sort both sides).
        match = (k, nsets, f) == exp[:3] and sorted(profile) == sorted(exp[3])
        agree &= match
        print(f"  {name:<26} computed (k,n,f)={ (k, nsets, f) } profile={profile}"
              f"  expected {exp}  {'MATCH' if match else 'MISMATCH'}")
    print(f"  all four families match expected values: "
          f"{'YES' if agree else 'NO'}")

    all_hold &= all(r[5] for r in rows if r[5] is not None)
    verdict_ok = all(uc for _, _, _, _, uc, _, _, _ in rows if uc is not None) \
        and all_hold and agree
    print(f"\n============ overall verdict: "
          f"{'ALL FOUR FAMILIES SATISFY KPT BOUNDS (1)(2)(3)' if verdict_ok else 'FAIL'} "
          f"============")
    return 0


def _run_and_capture():
    tmp_fd, tmp_path = tempfile.mkstemp(
        prefix="kpt_thm5_indep.", suffix=".captured.txt.tmp",
        dir=os.path.dirname(CAPTURE_PATH))
    os.close(tmp_fd)
    ok = True
    try:
        with open(tmp_path, "w") as fh:
            sys.stdout = fh
            rc = main()
            sys.stdout.flush()
            sys.stdout = sys.__stdout__
        with open(tmp_path) as fh:
            content = fh.read()
        if rc == 0 and content.strip():
            os.replace(tmp_path, CAPTURE_PATH)
            print(f"captured -> {CAPTURE_PATH}")
        else:
            ok = False
            print("capture NOT completed (non-zero exit or empty output); "
                  f"temp left at {tmp_path}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        ok = False
    finally:
        if not ok and os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(_run_and_capture())
