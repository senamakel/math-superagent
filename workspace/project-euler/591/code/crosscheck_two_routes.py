#!/usr/bin/env python3
"""Final mechanical cross-check of the two full-scale PE591 result files.

Parses both:
    /workspace/results_full_bothsides.txt      (Cabanillas-candidate solver)
    /workspace/results_ostrowski_n13.txt       (Ostrowski-numeration solver)

Each file carries 90 numeric rows (d, b, a, |a|) followed by an "S <sum>" line.
This script:
  (1) parses each file and asserts exactly 90 numeric rows,
  (2) asserts (b, a) identical on every d across the two files,
  (3) asserts |a| <= 1e13 and |b| <= 1e13 on every row of both files,
  (4) sums the |a| column of each independently with exact ints,
  (5) prints both sums and whether they are equal and equal to
      526007984625966.

Touches no solver code: this is purely a file-to-file reconciliation plus
bounds and re-sum, all in exact integer arithmetic.
"""

N_ROWS = 90
LIM = 10**13
EXPECTED_SUM = 526007984625966
FILES = [
    "/workspace/results_full_bothsides.txt",
    "/workspace/results_ostrowski_n13.txt",
]


def parse(path):
    rows = []      # list of (d, b, a, absa)
    endsum = None  # the trailing "S <value>" line if present
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) == 2 and parts[0] == "S":
                endsum = int(parts[1])
                continue
            if len(parts) != 4:
                raise ValueError(f"{path}: bad row {line!r}")
            rows.append(tuple(int(p) for p in parts))
    return rows, endsum


def main():
    parsed = {}
    for path in FILES:
        rows, endsum = parse(path)
        parsed[path] = (rows, endsum)
        print(f"parsed {path}: {len(rows)} numeric rows, S line = {endsum}")
        assert len(rows) == N_ROWS, \
            f"{path}: expected {N_ROWS} rows, got {len(rows)}"

    fine = True

    # Bounds on both files.
    for path in FILES:
        rows, _ = parsed[path]
        for d, b, a, aa in rows:
            if abs(a) > LIM or abs(b) > LIM:
                print(f"  FAIL bounds {path} d={d}: a={a} b={b}")
                fine = False
    print("bounds |a|<=1e13 and |b|<=1e13 on every row of both files: "
          + ("PASS" if fine else "FAIL"))

    # Cross-file (b, a) identity per d.
    (rA, sA), (rB, sB) = parsed[FILES[0]], parsed[FILES[1]]
    byd_A = {r[0]: r for r in rA}
    byd_B = {r[0]: r for r in rB}
    if byd_A.keys() != byd_B.keys():
        print("  FAIL: d-sets differ",
              sorted(set(byd_A) ^ set(byd_B)))
        fine = False
    same = all(byd_A[d][1] == byd_B[d][1] and byd_A[d][2] == byd_B[d][2]
               for d in byd_A)
    print("(b, a) identical on every d across both files: "
          + ("PASS" if same else "FAIL"))
    if not same:
        for d in byd_A:
            if (byd_A[d][1], byd_A[d][2]) != (byd_B[d][1], byd_B[d][2]):
                print(f"  differ d={d}: A={byd_A[d]} B={byd_B[d]}")
        fine = False

    # Independent exact re-sums of the |a| column.
    sumA = sum(r[3] for r in byd_A.values())
    sumB = sum(r[3] for r in byd_B.values())
    print(f"sum |a| (full_bothsides)  = {sumA}")
    print(f"sum |a| (ostrowski_n13)   = {sumB}")
    print(f"equal to each other      : {sumA == sumB}")
    print(f"equal to 526007984625966 : {sumA == EXPECTED_SUM and sumB == EXPECTED_SUM}")

    # Sanity: S line in each file matches the re-sum.
    print(f"S line matches re-sum     : {sA == sumA and sB == sumB}")

    if sumA != EXPECTED_SUM or sumB != EXPECTED_SUM:
        fine = False

    print("RESULT:", "ALL CHECKS PASS" if fine else "FAILURES FOUND")
    return 0 if fine else 1


if __name__ == "__main__":
    raise SystemExit(main())
