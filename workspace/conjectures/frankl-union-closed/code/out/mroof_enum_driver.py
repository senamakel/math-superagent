"""Driver for the M♮-certificate enumeration on ground set [n], n = 1..4.

Uses the ONE canonical oracle code/lib/uc.py (decide_union_closed,
abundance, abundant_elements) for every union-closure / abundance decision.

Three jobs, in order:

(1) build_enumeration(n): enumerate EVERY union-closed family on [n] as a set
    of bitmask ints (subsets of [n], masks 0..2^n-1), using
    decide_union_closed to filter. Count them. The count for n=1..4 must be
    3, 13, 121, 4959 (these are the counts of union-closed families on an
    n-element ground set, incl. the {empty} singleton family, excl. the empty
    collection — the same convention as lib.uc.verify_uc_exhaustive and the
    abundance_profile scan). The [n] enumerations include {∅}; the task asks
    for counts on the whole ground set, so each subfamily is a candidate.

    Negative control: decide_union_closed must REJECT a genuinely non-UC
    family. NOTE: the task's suggested example {{x,y},{x,y,z}} (masks {3},{7})
    is actually *union-closed* (3|7 = 7, which is in the family), so it is the
    wrong control. We use the genuinely non-UC antichain {{x},{y}} (masks
    {1},{2}) over n=2 whose missing union is {x,y} (mask 3), and assert it is
    rejected. This is exactly the negative control required: non-UC families
    are excluded from the enumeration.

(2) For each enumerated UC family compute Alb(F) = abundant_elements(F,n) and
    print a small table (n -> sample of families with their Alb).

(3) sweep(): for each family and each element x NOT in Alb(F), call
    is_feasible_mroof(F_masks, n, x) imported from code/out/mroof_z3.py, to
    test whether x is (over-)certifiable, and record any hit (a family+element
    where a non-abundant x becomes M♮-certifiable). Until mroof_z3.py exists,
    sweep() imports it lazily inside try/except, reports the module is not yet
    available, and counts the candidate (family, x) pairs that would be probed.

Exact integer arithmetic throughout: abundance is integer counts; no floats
are used for any decision.

Capture policy: output writes to code/out/mroof_enum.captured.txt via a temp
file, moved into place only on exit code 0.
"""

import os
import sys
import tempfile

from lib.uc import decide_union_closed, abundance, abundant_elements

CAPTURE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "mroof_enum.captured.txt")

# Expected count of union-closed families on [n] (incl. {∅}, excl. empty
# collection) — OEIS A121921 / A102896 first four terms.
EXPECTED = {1: 3, 2: 13, 3: 121, 4: 4959}


def build_enumeration(n):
    """Return the list of ALL union-closed families on [n], each as a frozenset
    of bitmask ints (masks 0..2^n-1). Excludes the empty collection ({}).
    Includes the {∅} singleton family (mask 0). Uses lib.uc.decide_union_closed.
    """
    all_masks = list(range(1 << n))
    K = len(all_masks)
    families = []
    for sub in range(1 << K):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam:
            continue
        if not decide_union_closed(fam):
            continue
        families.append(frozenset(fam))
    return families


def run_negative_control():
    """Reject a genuinely non-UC family via the oracle.

    {{x},{y}} as masks {1,2} over n=2 is an antichain; {x}|{y} = {x,y} = mask 3
    is NOT in the family, so it is not union-closed. decide_union_closed must
    return False. (Also verifies the task's suggested {{x,y},{x,y,z}} = {3,7}
    IS union-closed, so it would be a bogus control.)
    """
    # genuinely non-UC: masks {1,2}, missing union mask 3
    bad = {1, 2}
    uc_bad = decide_union_closed(bad)
    assert not uc_bad, "{{x},{y}} must be REJECTED by decide_union_closed"

    # task's suggested example is actually UC: masks {3,7}, 3|7=7 in family
    task_ex = {3, 7}
    uc_task = decide_union_closed(task_ex)

    print("[negative control] {{x},{y}}={1,2}: decide_union_closed ->",
          uc_bad, "(expected False, REJECTED)")
    print("[note] task example {{x,y},{x,y,z}}={3,7} is actually union-closed"
          " (3|7=7 in F); used {1,2} as the genuine non-UC control instead. ->",
          uc_task)
    return (not uc_bad)


def enumeration_and_counts():
    """Enumerate all UC families on n=1..4, check counts against A102896."""
    print("=== (1) enumeration counts (union-closed families on [n]) ===")
    ok_all = True
    per_n = {}
    for n in range(1, 5):
        fams = build_enumeration(n)
        per_n[n] = fams
        count = len(fams)
        exp = EXPECTED[n]
        good = (count == exp)
        ok_all &= good
        print(f"n={n}: {count} union-closed families (expected {exp})"
              f"  {'OK' if good else 'MISMATCH'}")
    print(f"counts: {[len(per_n[n]) for n in range(1,5)]}")
    print(f"matches A102896 first four terms (3,13,121,4959): {ok_all}")
    return per_n, ok_all


def alb_table(per_n):
    """Print a small table of Alb(F) for the enumerated families."""
    print()
    print("=== (2) Alb(F) sample table ===")
    for n in range(1, 5):
        fams = per_n[n]
        # print the first few families (1..3) with their Alb, then a summary
        print(f"--- n={n}: {len(fams)} families ---")
        for fi, fam in enumerate(fams[:3]):
            m = len(fam)
            counts = abundance(fam, n)
            alb = abundant_elements(fam, n)
            print(f"  F={sorted(fam)} |F|={m} counts={counts} Alb={alb}")
        # summary: distribution of |Alb|
        import collections
        alb_dist = collections.Counter(len(abundant_elements(f, n)) for f in fams)
        print(f"  |Alb| distribution over all {len(fams)} families: "
              f"{dict(sorted(alb_dist.items()))}")
    return True


def sweep(per_n):
    """For each family and each element x NOT in Alb(F), test is_feasible_mroof.

    Imports is_feasible_mroof(F_masks, n, x) lazily from code/out/mroof_z3.py.
    Until that module exists, reports the module is not yet available and
    records how many (family, x) candidate pairs WOULD be probed. Any family+
    element where a non-abundant x becomes M♮-certifiable is a 'hit' (an
    over-certification: the M♮-class would certify an element UC says is not
    abundant).
    """
    print()
    print("=== (3) sweep: M♮-certifiability of non-abundant x ===")
    import importlib.util
    mroof_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "mroof_z3.py")
    if os.path.exists(mroof_path):
        # load mroof_z3.py by explicit file path (it lives in code/out, which
        # is a data folder, not a package, so importlib loads it directly).
        spec = importlib.util.spec_from_file_location("mroof_z3", mroof_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        is_feasible_mroof = mod.is_feasible_mroof
        mroof_ready = True
    else:
        mroof_ready = False
        print("mroof_z3.py not yet available; sweep() cannot run. "
              f"(missing: {mroof_path})")

    hits = []
    total_candidates = 0
    for n in range(1, 5):
        for fam in per_n[n]:
            alb = set(abundant_elements(fam, n))
            for x in range(n):
                if x in alb:
                    continue  # only non-abundant x
                total_candidates += 1
                if mroof_ready:
                    ok = is_feasible_mroof(list(fam), n, x)
                    if ok:
                        hits.append((sorted(fam), n, x))
    print(f"non-abundant (family, x) candidate pairs across n=1..4: "
          f"{total_candidates}")
    if mroof_ready:
        print(f"M♮-over-certification hits: {len(hits)}")
        for h in hits[:20]:
            print("  HIT:", h)
        if len(hits) > 20:
            print(f"  ... and {len(hits)-20} more")
    else:
        print("sweep: SKIPPED (mroof_z3.py missing); recorded candidate count only.")
    return hits


def main():
    ok_control = run_negative_control()
    per_n, ok_counts = enumeration_and_counts()
    ok_alb = alb_table(per_n)
    hits = sweep(per_n)

    print()
    ok = ok_control and ok_counts and ok_alb
    print("negative_control:", "PASS" if ok_control else "FAIL")
    print("counts A102896 (3,13,121,4959):", "PASS" if ok_counts else "FAIL")
    print("Alb table computed:", "PASS" if ok_alb else "FAIL")
    if not ok:
        print("SOME CHECKS FAILED")
        return 1
    print("ALL ENUMERATION + COUNT + Alb CHECKS PASSED")
    return 0


def _run_and_capture():
    """Run main(), teeing stdout to a temp file, moving it to CAPTURE_PATH
    only if the run exits 0. An empty capture (no rows) is a failed run.
    """
    tmp_fd, tmp_path = tempfile.mkstemp(
        prefix="mroof_enum.", suffix=".captured.txt.tmp",
        dir=os.path.dirname(CAPTURE_PATH))
    os.close(tmp_fd)
    orig_stdout = sys.stdout
    rc = 1
    try:
        with open(tmp_path, "w") as fh:
            sys.stdout = fh
            rc = main()
            sys.stdout.flush()
        sys.stdout = orig_stdout
        with open(tmp_path) as fh:
            content = fh.read()
        if rc == 0 and content.strip():
            os.replace(tmp_path, CAPTURE_PATH)
            print(f"captured -> {CAPTURE_PATH}")
        else:
            print("capture NOT completed (non-zero exit or empty output); "
                  f"temp left at {tmp_path}")
            if os.path.exists(tmp_path) and '\n' in content and rc != 0:
                pass
    except Exception as e:  # ensure stdout is restored, temp never becomes final
        sys.stdout = orig_stdout
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        print("capture run raised:", e)
        return 1


if __name__ == "__main__":
    _run_and_capture()
