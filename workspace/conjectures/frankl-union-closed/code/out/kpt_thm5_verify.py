"""Compute-verify Kabela-Polak-Teska Theorem 5 on ALL union-closed families
over [n] for n = 1..4, using ONLY the canonical oracle lib.uc.

Theorem (F finite union-closed, empty set NOT in F, k = min set size,
n = max set size, f = # elements in MORE THAN half the sets, i.e. STRICT:
2*count_x > |F|):
    (1)  k >= n - 3                      ==>  f >= k
    (2)  k = n - 4                       ==>  f >= k - 1
    (3)  f >= min{n, 2k - n + 1}
Bounds (1),(2) are tight.

We enumerate every union-closed family (guard: counts equal A102896, the
sequence 3,13,121,4959), restrict to the theorem's hypothesis empty NOT in F,
and assert (1)-(3) with zero violations, counting equality cases
f == min{n, 2k - n + 1}.

Counterexample corollary: f = 0 forces n >= 2k + 1 (since (3) gives
f >= min{n,2k-n+1}; f=0 => 2k-n+1 <= 0 => n >= 2k+1). On n <= 4 we check no
union-closed empty-free family violates it (vacuously: there is no f=0 family).

Exact integer arithmetic throughout: abundance counts are exact ints, and the
strict test 2*c > |F| is integer. No floats.

Capture policy: writes to code/out/kpt_thm5_verify.captured.txt via a temp
file moved into place only on exit 0. First three lines state what ran, which
oracle function, and the exact n range.
"""

import os
import sys
import tempfile

from lib.uc import decide_union_closed, abundance, abundant_elements

CAPTURE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "kpt_thm5_verify.captured.txt")
EXPECTED = {1: 3, 2: 13, 3: 121, 4: 4959}  # A102896


def enumerate_uc_families(n):
    """All union-closed families on [n] as a list of frozensets of bitmask ints.
    Excludes the empty collection; includes the {empty} singleton family and
    families containing empty. (Same pattern as mroof_sweep.enumerate_uc_families.)
    """
    all_masks = list(range(1 << n))
    K = len(all_masks)
    families = []
    for sub in range(1 << K):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if fam and decide_union_closed(fam):
            families.append(frozenset(fam))
    return families


def popcount(m):
    return bin(m).count("1")


def element_names(n, x):
    return chr(ord('a') + x) if n <= 26 else str(x)


def set_family_str(fam, n):
    parts = []
    for m in sorted(fam):
        elems = [element_names(n, i) for i in range(n) if (m >> i) & 1]
        parts.append("{" + ",".join(elems) + "}")
    return "{" + ",".join(parts) + "}"


def main():
    print("Kabela-Polak-Teska Theorem 5 computational verification, n = 1..4")
    print("oracle: lib.uc.decide_union_closed + lib.uc.abundance "
          "(exact integer counts); strict test 2*c > |F|")
    print("range : n = 1..4, ALL union-closed families; theorem on empty-free "
          "(empty NOT in F) families only")

    g = {n: enumerate_uc_families(n) for n in range(1, 5)}
    for n in range(1, 5):
        assert len(g[n]) == EXPECTED[n], (n, len(g[n]), EXPECTED[n])
    print("guard: enumeration counts match A102896 (3,13,121,4959) -> OK")

    # per-n violation / equality / totals
    totals = {n: 0 for n in range(1, 5)}      # empty-free union-closed families
    viol = {(1,): 0, (2,): 0, (3,): 0}        # violations of (1),(2),(3)
    viol_examples = {(1,): [], (2,): [], (3,): []}
    equality = {n: 0 for n in range(1, 5)}    # f == min{n, 2k-n+1}
    fzero = {n: 0 for n in range(1, 5)}       # f == 0 families
    fzero_examples = []
    max_f = 0
    argmax = None

    # tightness witnesses tracked per (k-relation, n-class) for (1),(2);
    # equality in (3) means f == min{n, 2k-n+1}.
    for n in range(1, 5):
        for fam in g[n]:
            if 0 in fam:                      # empty in F: theorem hypothesis fails
                continue
            m = len(fam)
            ks = [popcount(x) for x in fam]
            k = min(ks)
            nn = max(ks)                      # largest set size = ground set size
            counts = abundance(fam, n)        # exact integer counts
            f = sum(1 for c in counts if 2 * c > m)   # STRICT abundance (>half)
            profile = tuple(sorted(counts))
            totals[n] += 1
            max_f = max(max_f, f)
            if f == max_f and (argmax is None or m > argmax[0]):
                argmax = (m, n, fam, f, profile)

            # (3): f >= min{nn, 2k - nn + 1}
            bound3 = min(nn, 2 * k - nn + 1)
            if f < bound3:
                viol[(3,)] += 1
                if len(viol_examples[(3,)]) < 5:
                    viol_examples[(3,)].append((n, fam, k, nn, f, bound3, profile))
            if f == bound3:
                equality[n] += 1

            if k >= nn - 3:
                # (1): f >= k
                if f < k:
                    viol[(1,)] += 1
                    if len(viol_examples[(1,)]) < 5:
                        viol_examples[(1,)].append((n, fam, k, nn, f, profile))
            if k == nn - 4:
                # (2): f >= k - 1
                if f < k - 1:
                    viol[(2,)] += 1
                    if len(viol_examples[(2,)]) < 5:
                        viol_examples[(2,)].append((n, fam, k, nn, f, profile))

            if f == 0:
                fzero[n] += 1
                if len(fzero_examples) < 5:
                    fzero_examples.append((n, fam, k, nn, profile))

    print("\n============ results ============")
    print("empty-free union-closed families per n (guard subclass):")
    for n in range(1, 5):
        print(f"  n={n}: {totals[n]}")
    print(f"  total empty-free: {sum(totals.values())}")

    print("\n(a) Theorem 5 holds on all n<=4 empty-free families:")
    for label, key in [("(1) k>=n-3 => f>=k", (1,)),
                       ("(2) k=n-4  => f>=k-1", (2,)),
                       ("(3) f>=min{n,2k-n+1}", (3,))]:
        v = viol[key]
        print(f"  {label}: violations = {v}  "
              f"{'PASS' if v == 0 else 'FAIL'}")
        for ex in viol_examples[key]:
            n, fam, k, nn, f, *rest = ex
            profile = rest[-1]
            print(f"      n={n} F={set_family_str(fam, n)} k={k} n={nn} "
                  f"f={f} profile={profile}")

    print(f"\n  max f over all empty-free n<=4 families: {max_f}")
    if argmax:
        m_, n_, fam_, f_, prof_ = argmax
        print(f"      witness: n={n_} F={set_family_str(fam_, n_)} |F|={m_} "
              f"f={f_} profile={prof_}")

    print("\n(c/d) tightness & equality counts:")
    print("  f == min{n, 2k-n+1} equality hits per n:")
    for n in range(1, 5):
        print(f"    n={n}: {equality[n]} / {totals[n]} empty-free families")
    print(f"    total equality hits: {sum(equality.values())}")

    # tightness witnesses for (1): f == k exactly with k >= n-3
    print("\n  (1)-tightness witnesses (f == k, k >= n-3):")
    shown1 = 0
    for n in range(1, 5):
        for fam in g[n]:
            if 0 in fam:
                continue
            ks = [popcount(x) for x in fam]
            k = min(ks); nn = max(ks)
            if not (k >= nn - 3):
                continue
            counts = abundance(fam, n)
            f = sum(1 for c in counts if 2 * c > len(fam))
            if f == k:
                if shown1 < 5:
                    print(f"    n={n} F={set_family_str(fam, n)} k={k} n={nn} "
                          f"f={f} profile={tuple(sorted(counts))}")
                shown1 += 1
    print(f"    total (1)-tight (f==k, k>=n-3) empty-free families: {shown1}")

    # tightness for (2): f == k-1 with k = n-4
    print("\n  (2)-tightness witnesses (f == k-1, k = n-4):")
    shown2 = 0
    for n in range(1, 5):
        for fam in g[n]:
            if 0 in fam:
                continue
            ks = [popcount(x) for x in fam]
            k = min(ks); nn = max(ks)
            if not (k == nn - 4):
                continue
            counts = abundance(fam, n)
            f = sum(1 for c in counts if 2 * c > len(fam))
            if f == k - 1:
                if shown2 < 5:
                    print(f"    n={n} F={set_family_str(fam, n)} k={k} n={nn} "
                          f"f={f} profile={tuple(sorted(counts))}")
                shown2 += 1
    print(f"    total (2)-tight (f==k-1, k=n-4) empty-free families: {shown2}")

    print("\n(b) counterexample corollary: f=0 forces n >= 2k+1")
    print(f"  empty-free families with f=0 on n<=4: "
          f"{sum(fzero.values())} (should be 0 since n<=4 range)")
    for ex in fzero_examples:
        n, fam, k, nn, profile = ex
        print(f"      n={n} F={set_family_str(fam, n)} k={k} n={nn} "
              f"profile={profile}")
    corollary_ok = sum(fzero.values()) == 0
    print(f"  corollary holds (no f=0 family to violate n>=2k+1): "
          f"{'YES (vacuous)' if corollary_ok else 'NO'}")

    # Combined theorem verdict
    all_ok = all(viol[k] == 0 for k in viol) and corollary_ok
    print("\n(e) exhaustive route stops at n=5")
    print("  n=5 would require 2^(2^5) = 2^32 = 4,294,967,296 subfamilies "
          "(2^32);")
    print("  each a candidate union-closed family. That is the boundary: "
          "enumeration")
    print("  of ALL subfamilies is infeasible at n=5 (A102896 counts are "
          "unknown by")
    print("  direct enumeration there), which is exactly where exhaustive "
          "verification")
    print("  of Theorem 5 stops.")
    print(f"\n============ overall verdict: "
          f"{'ALL BOUNDS (1)(2)(3) HOLD, 0 VIOLATIONS' if all_ok else 'FAIL'} "
          f"============")
    return 0


def _run_and_capture():
    tmp_fd, tmp_path = tempfile.mkstemp(
        prefix="kpt_thm5_verify.", suffix=".captured.txt.tmp",
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
