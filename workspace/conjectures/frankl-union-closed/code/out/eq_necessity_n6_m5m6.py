"""Extend the EQ structural-lemma necessity check at n=6 beyond |F|<=4
(code/out/eq_necessity_n6.py covered |F| in 2..4) to |F| = 5 and |F| = 6.

Lemma (crux of EQ(n) = A053221): an empty-free union-closed family with
f == min{N, 2k-N+1} (f = # strict-abundant elements 2c > |F|, k = min set
size, N = max set size) is a SINGLETON or a STRICT TWO-CHAIN {A, A u {x}}.
Equivalently NO family with >= 3 sets achieves the KPT equality.

First falsifier of the surviving regularity EQ(n) = (n+2)2^{n-1} - n - 1:
an empty-free UC family on n>=6 with >= 3 sets achieving the equality.
At n=6 the closed form gives EQ(6)=249 = singletons(63) + two-chains(186),
so any >=3-set EQ family at n=6 refutes the lemma outright.

Exhaustive enumeration of ALL subfamilies of size 5 and 6 of the 63 nonempty
subsets of [6]: C(63,5)=7,028,847 and C(63,6)=67,945,521 subfamilies,
each tested for union-closure via lib.uc and checked for the equality.
Exact integers throughout.

Capture policy: writes to code/out/eq_necessity_n6_m5m6.captured.txt via a
temp file moved into place only on exit 0.
"""
import os
import sys
import tempfile
import time
from itertools import combinations

from lib.uc import decide_union_closed, abundance

CAPTURE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "eq_necessity_n6_m5m6.captured.txt")


def popcount(x):
    return bin(x).count("1")


def main():
    n = 6
    masks = list(range(1 << n))
    nz = [x for x in masks if x != 0]
    print("extend EQ necessity check at n=6 to |F|=5,6 (small families)")
    print("oracle: lib.uc (decide_union_closed, abundance), exact integers")
    print("range : ALL empty-free UC families on [6] with |F| in {5,6,7}, exhaustive")
    bad = []
    total_eq = 0
    for m in [5, 6, 7]:
        t0 = time.time()
        total_uc = 0
        eq_here = 0
        bad_here = 0
        for combo in combinations(nz, m):
            F = set(combo)
            if not decide_union_closed(F):
                continue
            total_uc += 1
            counts = abundance(F, n)
            f = sum(1 for c in counts if 2 * c > m)
            ks = sorted(popcount(s) for s in F)
            k = ks[0]
            N = ks[-1]
            if f == min(N, 2 * k - N + 1):
                eq_here += 1
                total_eq += 1
                # an EQ family with m>=3 sets is a counterexample to the lemma
                if m >= 3:
                    bad_here += 1
                    if len(bad) < 10:
                        bad.append((m, sorted(F), k, N, f))
        print(f"  |F|={m}: UC families={total_uc}  eq={eq_here}  "
              f"non-single/twochain-equality={bad_here}  ({time.time()-t0:.1f}s)")
    print(f"\nTOTAL EQ families (|F|=5,6, n=6): {total_eq}")
    print(f"counterexamples to lemma (>=3-set EQ family): {len(bad)}")
    for b in bad:
        print(f"   BAD: |F|={b[0]} k={b[2]} N={b[3]} f={b[4]} masks={sorted(b[1])}")
    # Combined verdict: no >=3-set EQ family at n=6 across all sizes 2..6
    print(f"\nverdict: {0 if len(bad)==0 else 'FAIL'} "
          f"(0 = no >=3-set EQ family among all |F|<=6 at n=6)")
    return 0


def _run_and_capture():
    tmp_fd, tmp_path = tempfile.mkstemp(
        prefix="eq_necessity_n6_m5m6.", suffix=".captured.txt.tmp",
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
            print("capture NOT completed (non-zero exit or empty output)")
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
