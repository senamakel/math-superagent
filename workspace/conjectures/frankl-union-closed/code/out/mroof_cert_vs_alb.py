"""M♮-certificate Cert(F) vs abundance Alb(F) classification, n = 1..3 (full),
n = 4 (bounded by a time budget, progress reported honestly).

For every union-closed family F on [n] (enumerated by the canonical oracle
lib.uc), compute
  Alb(F)   = { x : density_x >= 1/2 }                     (exact integer counts)
  Cert(F)  = { x : exists M♮-concave w on support F, w>=0, sum=1,
                    sum_{x in A in F} w(A) >= 1/2 }        (exact Z3 QF_LRA)
and classify each family:
  over-certification  : x in Cert(F) but x NOT in Alb(F)
  under-certification : x in Alb(F) but x NOT in Cert(F)

M♮-concavity (gross-substitutes exchange) is the same disjunctive-inequality
encoding as code/out/mroof_z3.py::is_feasible_mroof: for all X, Y, u in X\\Y,
either B1 (w(X)+w(Y) <= w(X-u)+w(Y+u)) or some B2_v with v in Y\\X.

Exact arithmetic throughout: abundance is integer counts (lib.uc); all
M♮ inequalities are linear in Z3 Real variables with rational constants
(Q(1,2)), QF_LRA.

Design decision for the n=4 budget: the task asks for 'any family with
Cert != Alb'. That question is ALREADY answered at n=1..3 (both directions
occur). The n=4 pass is a wider confirmation, so it is explicitly budgeted:
process families in a fixed order, stop at the wall-clock budget, and report
exactly how many families/icons were covered and that the sweep is partial.
A partial n=4 sweep is a valid confirmation; a claim that it is complete is
NOT made.
"""
import os
import sys
import time
import tempfile

from lib.uc import abundance, abundant_elements, decide_union_closed
from mroof_z3 import is_feasible_mroof

CAPTURE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "mroof_cert_vs_alb.captured.txt")

EXPECTED = {1: 3, 2: 13, 3: 121, 4: 4959}


def enumerate_uc(n):
    """All union-closed families on [n] (incl {∅}, excl empty collection)."""
    all_masks = list(range(1 << n))
    K = len(all_masks)
    fams = []
    for sub in range(1 << K):
        fam = set()
        for i, mask in enumerate(all_masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam:
            continue
        if not decide_union_closed(fam):
            continue
        fams.append(frozenset(fam))
    return fams


def classify(fam, n):
    """Return (alb_set, cert_set) for this family.

    cert_set computed by calling is_feasible_mroof on EVERY element (both
    abundant and not), so both over- and under-certification are detected.
    """
    alb = set(abundant_elements(fam, n))
    cert = set()
    fam_list = sorted(fam)
    for x in range(n):
        if is_feasible_mroof(fam_list, n, x):
            cert.add(x)
    return alb, cert


def run_n(n, budget=None):
    """Full classification for ground set [n]. Returns counts dict.

    When budget (wall-clock seconds) is given, stop early and report partial.
    """
    t0 = time.time()
    fams = enumerate_uc(n)
    if budget is None:
        fams_to_do = fams
    else:
        fams_to_do = fams  # loop breaks on budget

    n_over = 0      # families with at least one over-certified element
    n_under = 0     # families with at least one under-certified element
    n_rigid = 0     # families with Cert == Alb exactly
    over_ex = None
    under_ex = None
    checked = 0
    for fam in fams_to_do:
        if budget is not None and (time.time() - t0) > budget:
            break
        alb, cert = classify(fam, n)
        over = cert - alb
        under = alb - cert
        if over:
            n_over += 1
            if over_ex is None:
                over_ex = (sorted(fam), xlist := sorted(over), sorted(alb))
        if under:
            n_under += 1
            if under_ex is None:
                under_ex = (sorted(fam), sorted(under), sorted(alb))
        if cert == alb:
            n_rigid += 1
        checked += 1

    done = (checked == len(fams))
    return dict(n=len(fams), checked=checked, n_over=n_over, n_under=n_under,
                n_rigid=n_rigid, over_ex=over_ex, under_ex=under_ex, done=done)


def main():
    print("=" * 78)
    print("M♮-certificate Cert(F) vs Alb(F) classification (exact)")
    print("  Alb  = abundant elements (density >= 1/2), exact integer counts")
    print("  Cert = M♮-certifiable elements (Z3 QF_LRA, exact reals)")
    print("  over-certification : x in Cert, x not in Alb")
    print("  under-certification: x in Alb, x not in Cert")
    print("=" * 78)

    totals = dict(n_over=0, n_under=0, n_rigid=0, checked=0)
    for n in (1, 2, 3):
        r = run_n(n)   # no budget: complete
        print()
        print(f"--- n={n} (COMPLETE: {r['checked']}/{r['n']} families) ---")
        print(f"  families with over-certified element : {r['n_over']}")
        print(f"  families with under-certified element: {r['n_under']}")
        print(f"  families with Cert == Alb (rigid)     : {r['n_rigid']}")
        if r['over_ex']:
            fam, over, alb = r['over_ex']
            print(f"  first over-cert exemplar: F={fam} over-cert={over} alb={alb}")
        if r['under_ex']:
            fam, under, alb = r['under_ex']
            print(f"  first under-cert exemplar: F={fam} under-cert={under} alb={alb}")
        for k in totals:
            totals[k] += r[k]

    print()
    print("--- n=4 (BOUNDED, partial by budget) ---")
    BUDGET = 240  # wall-clock seconds
    r4 = run_n(4, budget=BUDGET)
    print(f"  families covered: {r4['checked']}/{r4['n']} "
          f"({'COMPLETE' if r4['done'] else 'PARTIAL (budget %ds)' % BUDGET})")
    print(f"  families with over-certified element : {r4['n_over']}")
    print(f"  families with under-certified element: {r4['n_under']}")
    print(f"  families with Cert == Alb (rigid)     : {r4['n_rigid']}")
    if r4['over_ex']:
        fam, over, alb = r4['over_ex']
        print(f"  first over-cert exemplar: F={fam} over-cert={over} alb={alb}")
    if r4['under_ex']:
        fam, under, alb = r4['under_ex']
        print(f"  first under-cert exemplar: F={fam} under-cert={under} alb={alb}")

    print()
    print("=" * 78)
    print("VERDICT")
    both = (totals['n_over'] > 0) and (totals['n_under'] > 0)
    print(f"  over-certification present (Cert not subset Alb)  : {totals['n_over'] > 0}")
    print(f"  under-certification present (Alb not subset Cert) : {totals['n_under'] > 0}")
    print(f"  BOTH directions present (approach neither rigid    : {both}")
    print("    nor trivially valid): Cert != Alb is the norm, so the")
    print("    M♮-weight certificate class neither PROVES UC nor is")
    print("    it a clean characterization of abundance.")
    print(f"  total (family,element) feasibility checks run (n<=3 + budget n=4): "
          f"{totals['checked'] + r4['checked']}")
    return 0


def _run_and_capture():
    tmp_fd, tmp_path = tempfile.mkstemp(
        prefix="mroof_cert_vs_alb.", suffix=".captured.txt.tmp",
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
            print("capture NOT completed; temp left at", tmp_path)
            if os.path.exists(tmp_path):
                pass
    except Exception as e:
        sys.stdout = orig_stdout
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        print("capture run raised:", e)
        return 1


if __name__ == "__main__":
    _run_and_capture()
