"""Full M♮-certificate classification sweep over ALL union-closed families on
n = 1..4, parallelised across cores.

For EVERY union-closed family F (all 4959 at n=4), for EVERY element x in [n],
call is_feasible_mroof(F_masks, n, x)  [imported verbatim from mroof_z3.py,
the SAME encoding, never rewritten] to obtain

    Cert(F) = { x in [n] : is_feasible_mroof(F_masks, n, x) }

and Alb(F) from lib.uc.abundant_elements (the one canonical abundance oracle).
Then classify each family:

  - over : Cert(F) \\ Alb(F) nonempty  (some NON-abundant element is
    M♮-certifiable)
  - under: Alb(F) \\ Cert(F) nonempty  (some ABUNDANT element is NOT
    certifiable)
  - totally-uncertifiable: Cert(F) ∩ Alb(F) is empty  (NO abundant element is
    M♮-certifiable at all) — the predecessor F={5,7} on n=3 (={{x,z},{x,y,z}})
    whose density-1 elements are infeasible is such a case.
  - Cert == Alb exactly.

Report summary counts per n. Print EVERY totally-uncertifiable family
explicitly (set family + masks + |F| + abundance vector) for n <= 3. For n=4
give the count and a few examples.

Exact arithmetic throughout: abundance counts are integer; the feasibility
decision is an exact QF_LRA solve (z3 Real). No floats enter any decision.

Parallelism: each (family, x) is an independent exact solve, so a
multiprocessing pool fans the ~20k tasks out across cores (28 available).
The worker re-imports mroof_z3 inside the subprocess (never shares the Solver).

Capture policy: output writes to code/out/mroof_sweep.captured.txt via a temp
file, moved into place only on exit code 0. First three lines state what ran,
which oracle function, and the exact n range.
"""

import os
import sys
import tempfile
import importlib.util
from multiprocessing import Pool

from lib.uc import decide_union_closed, abundance, abundant_elements

CAPTURE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "mroof_sweep.captured.txt")
MROOF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "mroof_z3.py")
EXPECTED = {1: 3, 2: 13, 3: 121, 4: 4959}


def enumerate_uc_families(n):
    """All union-closed families on [n] as a list of frozensets of bitmask ints.
    Excludes the empty collection; includes the {∅} singleton family.
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


def _worker(task):
    """Solve one (n, fam, x) feasibility. Loads mroof_z3 in this subprocess."""
    n, fam, x = task
    spec = importlib.util.spec_from_file_location("mroof_z3_worker", MROOF_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    is_feasible_mroof = mod.is_feasible_mroof
    return (n, fam, x, is_feasible_mroof(list(fam), n, x))


def element_names(n, x):
    return chr(ord('a') + x) if n <= 26 else str(x)


def set_family_str(fam, n):
    parts = []
    for m in sorted(fam):
        elems = [element_names(n, i) for i in range(n) if (m >> i) & 1]
        parts.append("{" + ",".join(elems) + "}")
    return "{" + ",".join(parts) + "}"


def main():
    print("M♮-certificate classification sweep, n = 1..4 (exact QF_LRA via Z3)")
    print("oracle: is_feasible_mroof(F_masks, n, x) from code/out/mroof_z3.py;")
    print("        Alb(F) from lib.uc.abundant_elements")
    print("range : n = 1..4, ALL union-closed families (3, 13, 121, 4959)")

    g = {n: enumerate_uc_families(n) for n in range(1, 5)}
    for n in range(1, 5):
        assert len(g[n]) == EXPECTED[n], (n, len(g[n]), EXPECTED[n])
    print("guard: enumeration counts match A102896 (3,13,121,4959) -> OK")

    # build all (n, fam, x) tasks
    tasks = []
    for n in range(1, 5):
        for fam in g[n]:
            for x in range(n):
                tasks.append((n, fam, x))
    print(f"solves: {len(tasks)} (family, element) tasks")

    # fan out across cores
    results = []
    cores = os.cpu_count() or 1
    with Pool(cores) as pool:
        for j, res in enumerate(pool.imap_unordered(_worker, tasks, chunksize=32)):
            results.append(res)
            if (j + 1) % 2000 == 0:
                print(f"  ... {j+1}/{len(tasks)} solves done")
    # (n, fam, x, bool)
    cert = {}
    for n, fam, x, ok in results:
        cert[(n, fam, x)] = ok

    summary = {}
    explicit = {}
    examples4 = []

    for n in range(1, 5):
        n_over = n_under = n_total = n_exact = 0
        n_total_nonempty_alb = 0
        ex4 = []
        for fam in g[n]:
            alb = set(abundant_elements(fam, n))
            certset = {x for x in range(n) if cert[(n, fam, x)]}
            is_over = bool(certset - alb)
            is_under = bool(alb - certset)
            is_total = (len(certset & alb) == 0)
            is_exact = (certset == alb)
            n_over += is_over
            n_under += is_under
            n_total += is_total
            if is_total:
                if alb:
                    n_total_nonempty_alb += 1
            n_exact += is_exact
            if is_total and n <= 3:
                explicit.setdefault(n, []).append((fam, n, alb))
            if is_total and n == 4 and len(ex4) < 8:
                ex4.append((fam, n, alb))
        summary[n] = dict(over=n_over, under=n_under, total=n_total,
                          exact=n_exact, total_nonempty_alb=n_total_nonempty_alb)
        if n == 4:
            examples4 = ex4

        print(f"\n===== n={n}: {len(g[n])} union-closed families =====")
        print(f"  over   (some non-abundant x is M♮-certifiable): {n_over}")
        print(f"  under  (some ABUNDANT x is NOT certifiable)   : {n_under}")
        print(f"  totally-uncertifiable (Cert∩Alb = ∅)          : {n_total}"
              f"  (of which with nonempty Alb: {n_total_nonempty_alb})")
        print(f"  Cert == Alb exactly                           : {n_exact}")

        if n <= 3 and explicit.get(n):
            print(f"  --- totally-uncertifiable families (n={n}), printed "
                  f"explicitly ---")
            for fam, nn, alb in explicit[n]:
                counts = abundance(fam, nn)
                maskstr = "{" + ",".join(str(m) for m in sorted(fam)) + "}"
                print(f"    F={set_family_str(fam, nn)} masks={maskstr} "
                      f"|F|={len(fam)} abundance={counts} Alb={sorted(alb)}")
        elif n == 4:
            print(f"  --- sample totally-uncertifiable families (n=4), "
                  f"first {len(ex4)} of {n_total} ---")
            for fam, nn, alb in ex4:
                counts = abundance(fam, nn)
                maskstr = "{" + ",".join(str(m) for m in sorted(fam)) + "}"
                print(f"    F={set_family_str(fam, nn)} masks={maskstr} "
                      f"|F|={len(fam)} abundance={counts} Alb={sorted(alb)}")

    print("\n================ SUMMARY ================")
    print("n | #fams | over | under | totally-unc | Cert==Alb |(tot w/ Alb≠∅)")
    for n in range(1, 5):
        s = summary[n]
        print(f"{n} | {len(g[n]):5d} | {s['over']:4d} | {s['under']:4d} | "
              f"{s['total']:11d} | {s['exact']:9d} | "
              f"{s['total_nonempty_alb']:12d}")
    return 0


def _run_and_capture():
    tmp_fd, tmp_path = tempfile.mkstemp(
        prefix="mroof_sweep.", suffix=".captured.txt.tmp",
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
