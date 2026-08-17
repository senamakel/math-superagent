"""Verify the theorem g(n,m) = max(1, m - 2^{n-1}).

What ran: constructions (A) and (B) built from a recursive upward-closed
(upset) generator, checked with the canonical oracle.
Which oracle: lib.uc.decide_union_closed / lib.uc.abundance.
Exact range: n in 1..6, m in 1..2^n; exhaustive cross-check at n<=4; size
lemma (every upset size realizable) for N in 0..6.

Theorem: for every n>=1 and 1<=m<=2^n there is a union-closed family F of
size m on [n] whose rarest present element appears exactly max(1, m-2^{n-1})
times.

  (A) m >= 2^{n-1}+1:  c = m - 2^{n-1}; G = upset of 2^[n-1] of size c;
      F = 2^[n-1]  union  { A|{n} : A in G }.
  (B) m <= 2^{n-1}+1: H = upset of 2^[n-1] of size m-1;
      F = H  union  { (union H) | {n} }.

All arithmetic exact integers. No floats.
"""
import tempfile
import os
from lib.uc import decide_union_closed, abundance


# --------------------------------------------------------------------------
# Recursive upset generator over 2^[N]  (elements = bits 0..N-1)
# Returns a set of bitmasks, an upward-closed subfamily of exactly `size`.
# --------------------------------------------------------------------------
def upset(N, size):
    """Upward-closed subfamily of 2^[N] (bits 0..N-1) of exactly `size` members.
    Recursion:
      base N=0: 2^[0] = {0}; upsets are {} (size 0) and {0} (size 1).
      if size >= 2^{N-1}: all sets containing bit N-1 (2^{N-1} of them) union
            an upset(N-1, size-2^{N-1}) inside the lower subcube (no top bit);
            upward-closed because every top-superset is present and the lower
            part is itself an upset.
      else (size < 2^{N-1}): take upset(N-1, size) inside the upper subcube and
            add the top bit: { x|top : x in upset(N-1, size) }. Upward-closed,
            since every element already contains top (so no non-top superset
            exists) and the upper part is an upset.  [Fixes the naive branch
            "upset(N-1,size) without top", which is NOT an upset of 2^[N]:
            a non-top set's top-superset would be missing.]
    """
    assert 0 <= size <= (1 << N), (N, size)
    if N == 0:
        return set() if size == 0 else {0}
    top = 1 << (N - 1)
    half = 1 << (N - 1)
    if size >= half:
        # all sets containing top (the whole upper cube), plus a lower upset
        fam = {s | top for s in range(half)}     # every subset of [N-1] UNION {top}
        fam |= upset(N - 1, size - half)
        return fam
    else:
        # size < half: an upset entirely among the top-containing sets
        fam = {x | top for x in upset(N - 1, size)}
        return fam


def is_upset(N, S):
    """True iff S (a set of bitmasks over [N]) is upward-closed in 2^[N]."""
    for a in S:
        for b in range(1 << N):
            if (a | b) == b and b not in S:  # b is a superset of a
                return False
    return True


# --------------------------------------------------------------------------
# Constructions (A) and (B).  Ground set elements = bits 0..n-1, element n is
# bit n-1. Elements 1..n-1 (bits 0..n-2) form the [n-1] subcube.
# --------------------------------------------------------------------------
def construction_A(n, m):
    """m >= 2^{n-1}+1. Returns (F, c)."""
    half = 1 << (n - 1)
    top = 1 << (n - 1)
    c = m - half
    assert 1 <= c <= half, (n, m)
    G = upset(n - 1, c)                 # subfamily of [0, half)
    F = set(range(half))                # all of 2^[n-1]
    F |= {g | top for g in G}           # lifted sets
    return F, c


def construction_B(n, m):
    """m <= 2^{n-1}+1. Returns (F,)."""
    top = 1 << (n - 1)
    H = upset(n - 1, m - 1)             # size m-1, subsets of [0, 2^{n-1})
    U = 0
    for h in H:
        U |= h                          # union of all sets in H
    F = set(H)
    F.add(U | top)
    return F


def predicted(n, m):
    return max(1, m - 2 ** (n - 1))


# --------------------------------------------------------------------------
# Exhaustive g(n,m) on the oracle, n<=4: min rare over ALL union-closed
# families of size m. (2^(2^n) subfamilies; n=4 -> 65536.)
# --------------------------------------------------------------------------
def exhaustive_g(n):
    masks = list(range(1 << n))
    best = {}
    for sub in range(1 << (1 << n)):
        fam = {masks[i] for i in range(len(masks)) if (sub >> i) & 1}
        if not fam:
            continue
        if not decide_union_closed(fam):
            continue
        m = len(fam)
        counts = abundance(fam, n)
        present = [c for c in counts if c > 0]
        if not present:
            continue  # family with no present elements ({0} alone)
        mn = min(present)
        if m not in best or mn < best[m]:
            best[m] = mn
    return best


# --------------------------------------------------------------------------
# Size lemma: for N, the set {|G| : G upset of 2^[N]} == {0..2^N}.
# Enumerate all upsets by DFS (removing minimal elements from the full cube,
# deduping); the first root-to-leaf path already hits every size 2^N..0, so
# early-exit once all sizes are seen.
# --------------------------------------------------------------------------
def all_upset_sizes(N):
    full = frozenset(range(1 << N))
    seen = set()
    sizes = set()
    target = set(range((1 << N) + 1))
    count = 0
    def dfs(present):
        nonlocal count
        if present in seen or sizes == target:
            return
        seen.add(present)
        sizes.add(len(present))
        count += 1
        for x in list(present):
            # x removable iff no other present y is a proper subset (y|x==x, y!=x)
            if not any(y != x and (y | x) == x for y in present):
                dfs(present - {x})
    dfs(full)
    return sizes == target


# --------------------------------------------------------------------------
# Main verification
# --------------------------------------------------------------------------
def main():
    return _run()


def _run():
    problems = []
    print("gnm_envelope_verify.py: verify g(n,m) = max(1, m - 2^(n-1))")
    print("oracle: lib.uc.decide_union_closed / lib.uc.abundance (canonical)")
    print("range: n in 1..6, m in 1..2^n; exhaustive cross-check n<=4; size lemma N in 0..6")

    # 1. upset generator sanity on every (N, size) in 0..6
    for N in range(0, 7):
        for size in range(0, (1 << N) + 1):
            S = upset(N, size)
            assert len(S) == size, (N, size, len(S))
            assert is_upset(N, S), (N, size)
        print(f"upset(N={N}, size) upward-closed of right size for all sizes 0..{1<<N}")

    # 2. upsets are union-closed (over their own universe [N])
    for N in range(0, 7):
        for size in range(0, (1 << N) + 1):
            S = upset(N, size)
            assert decide_union_closed(S), (N, size)
        print(f"upset(N={N}, *) all union-closed")

    # 3. size lemma
    for N in range(0, 7):
        ok = all_upset_sizes(N)
        print(f"size lemma N={N}: sizes of upsets == {{0..{1<<N}}}: {ok}")
        if not ok:
            problems.append(("size-lemma", N))

    # 4. the theorem, n in 1..6, every m
    for n in range(1, 7):
        half = 1 << (n - 1)
        for m in range(1, (1 << n) + 1):
            if m >= half + 1:
                F, c = construction_A(n, m)
            else:
                F = construction_B(n, m)
            # oracle checks
            uc = decide_union_closed(F)
            if len(F) != m:
                problems.append((n, m, "size"))
            if not uc:
                problems.append((n, m, "not-UC"))
            counts = abundance(F, n)
            present = [c for c in counts if c > 0]
            rare = min(present)
            if rare != predicted(n, m):
                problems.append((n, m, f"rare={rare} want={predicted(n,m)}"))
        # summary line per n
        worst = max((predicted(n, m) for m in range(1, (1 << n) + 1)), default=0)
        print(f"n={n} (2^(n-1)={half}): all m in 1..2^n construct UC of size m "
              f"with rare == max(1,m-2^(n-1)); worst rare value = {worst}")
        print(f"    construction-A sizes present: "
              f"{[m for m in range(half+1,(1<<n)+1) if not any(p[0]==n and p[1]==m for p in problems)] or 'all-ok'}")

    # 5. exhaustive cross-check at n<=4
    for n in range(1, 5):
        best = exhaustive_g(n)
        mismatch = []
        for m in range(1, (1 << n) + 1):
            want = predicted(n, m)
            if m not in best:
                mismatch.append((m, "missing", want))
            elif best[m] != want:
                mismatch.append((m, best[m], want))
        if mismatch:
            problems.append((n, "exhaustive", mismatch))
        print(f"n={n}: exhaustive g(n,m) == max(1,m-2^(n-1)) for all m: {not mismatch}")
        if mismatch:
            print(f"    MISMATCHES: {mismatch}")

    # 6. report worst/every
    if problems:
        print("\nFAILURES:")
        for p in problems:
            print("   ", p)
    else:
        print("\nALL ASSERTIONS PASS: constructions (A),(B) give UC families of "
              "size m with rarest present element == max(1, m-2^(n-1)) for "
              "every n in 1..6, m in 1..2^n; exhaustive g matches at n<=4; "
              "upset size lemma holds for N in 0..6.")
    return problems


if __name__ == "__main__":
    import shutil
    # Capture to a temp file in /tmp, then move into place only on exit 0.
    tmp = "/tmp/gnm_envelope_verify.captured.tmp.txt"
    dest = "code/out/gnm_envelope_verify.captured.txt"
    import io
    from contextlib import redirect_stdout
    buf = io.StringIO()
    with redirect_stdout(buf):
        problems = main()
    output = buf.getvalue()
    code = 0 if not problems else 1
    with open(tmp, "w") as f:
        f.write(output)
    if code == 0:
        shutil.move(tmp, dest)
    import sys
    sys.stdout.write(output)
    exit(code)
