#!/usr/bin/env python3
"""code/check_near_misses.py — the run's oracle checks for the 3x3 magic
square of squares, exact integer arithmetic only.

What it does, in order:

(1) Verifier sanity: is_magic_square_of_squares on known-answer cases
    (Lo Shu is not all-squares; nine 1s is magic-and-squares but not
    distinct with the strict flag and IS with the relaxed flag; a distinct
    non-magic square grid; a parametrised magic grid that is not all
    squares).

(2) Worked examples of the statement (problem.md), rerun fresh, output to
    code/out/ worked_examples.txt:
      * parametrisation identity: grid_from_params(c,u,v) has all eight
        line sums exactly 3c and centre c = M/3 — checked on every
        c in 1..40, |u|, |v| <= 60 (585,640 grids);
      * completeness: any all-lines-equal grid is
        grid_from_params(centre, a00-centre, a02-centre) — checked on
        every c in 1..25, |u|, |v| <= 25 wheel and 3000 random integer
        grids plus the Lo Shu;
      * AP structure of the four centre lines (milestone: the four diffs
        are u, v, u+v, u-v up to absolute value).

(3) Both known 7-square near-misses, by direct construction:
      * Sallows LS1 (printed in Bremner 1999 (1)): rows
        [58^2, 46^2, 127^2; 94^2, 113^2, 2^2; 97^2, 82^2, 74^2];
        expected 7 of 8 line sums equal 147^2 = 21609, failing at the
        non-principal diagonal with sum 38307.
      * Bremner's true magic square (Bremner 1999 p. 290): rows
        [373^2, 289^2, 565^2; 360721, 425^2, 23^2; 205^2, 527^2, 222121];
        expected all 8 line sums 541875 and exactly 7 square entries with
        the two non-squares exactly 360721 and 222121.
    The user-facing orientation (127,46,58 / 2,113,94 / 74,82,97) is the
    reflection/transpose of the printed one; the checks verify the printed
    grid byte-for-byte and note the orientation change.

(4) Magic-graph rank: the 8 lines x 9 cells incidence matrix over Q has
    rank 5, so the space of magic assignments has dimension 4, spanned by
    the constant grid, the u-grid and the v-grid (exact RREF nullspace).

(5) Bremner c, u, v extraction: c = M/3 must equal 425^2, and for each of
    d in {u, v, u+v, u-v} test whether BOTH c+d and c-d are perfect
    squares.  Expected outcome (steering correction): exactly TWO true —
    d = v = 138600 (both c+v = 565^2 and c-v = 205^2) and
    d = u+v = 97104 (both c+u+v = 527^2 and c-u-v = 289^2).  The other
    two fail at exactly one endpoint each:
      d = u  = -41496:   c+u = 373^2 but c-u = 222121 (not a square)
      d = u-v = -180096: c+u-v = 23^2 but c-u+v = 360721 (not a square).
    The program prints the four booleans raw; the assertion that exactly
    two are true is the checked conclusion.

(6) Pythagorean pairs realising the two satisfied relations:
      (385, 180): 385^2 + 180^2 = 425^2 and 2*385*180 = 138600 = v
      (408, 119): 408^2 + 119^2 = 425^2 and 2*408*119 = 97104  = u+v
    both verified by exact integer arithmetic.  This is the witness check
    of the c = x^2 + y^2, d = 2xy reformulation.

Everything asserted as fact is computed here (exact ints); the only
external anchors are the two printed grids in Bremner 1999, quoted in the
docstring of lib/mss.py with the source path.
"""

from fractions import Fraction
import json
import random
import sys
import time

from lib.mss import (LINE_NAMES, bremner_magic_grid, count_squares,
                     entries_of, failure_of, grid_from_params,
                     is_magic_square_of_squares, line_sums, lines_of,
                     magic_incidence_matrix, magic_params_basis,
                     magic_sum, params_from_grid, rank_fraction_matrix,
                     sallows_ls1_grid, sqrt_or_none, two_square_splits)

OUT_DIR = "code/out"

# ---------------------------------------------------------------------------
# (1) verifier sanity
# ---------------------------------------------------------------------------


def test_verifier():
    bad = 0
    cases = [
        # (label, grid, strict-expected, relaxed-expected)
        ("Lo Shu classic (integer magic square, not all squares)",
         [[4, 9, 2], [3, 5, 7], [8, 1, 6]], False, False),
        ("nine 1s (magic + squares, not distinct)",
         [[1, 1, 1], [1, 1, 1], [1, 1, 1]], False, True),
        ("distinct positive squares, not magic",
         [[1, 9, 25], [49, 81, 4], [16, 36, 64]], False, False),
        ("parametrised c=25,u=6,v=9 grid",
         grid_from_params(25, 6, 9), False, False),
        ("float entry", [[1.0, 4, 9], [16, 25, 36], [49, 64, 81]],
         False, False),
        ("wrong shape", [[1, 4], [9, 16, 25], [36, 49]], False, False),
    ]
    print("[1] verifier known-answer cases")
    for label, g, strict, relaxed in cases:
        got_s = is_magic_square_of_squares(g, require_distinct=True)
        got_r = is_magic_square_of_squares(g, require_distinct=False)
        diag = failure_of(g)
        ok = (got_s == strict) and (got_r == relaxed)
        bad += 0 if ok else 1
        print(f"    {'ok  ' if ok else 'FAIL'} {label}: "
              f"strict {got_s} / relaxed {got_r} ({diag})")
    print(f"    -> {'PASS' if bad == 0 else f'{bad} FAILURES'}")
    return bad == 0


# ---------------------------------------------------------------------------
# (2) the statement's worked examples, rerun fresh
# ---------------------------------------------------------------------------


def run_parametrisation_identity():
    n = bad = 0
    for c in range(1, 41):
        for u in range(-60, 61):
            for v in range(-60, 61):
                g = grid_from_params(c, u, v)
                n += 1
                if magic_sum(g) != 3 * c or g[1][1] != c:
                    bad += 1
    print(f"    identity: {n} grids (c in 1..40, |u|,|v| <= 60), "
          f"all magic with constant 3c and centre c: "
          f"{'PASS' if bad == 0 else f'{bad} FAILURES'}")
    return n, bad


def run_completeness():
    bad = n = 0
    for c in range(1, 26):
        for u in range(-25, 26):
            for v in range(-25, 26):
                g = grid_from_params(c, u, v)
                cc, uu, vv = params_from_grid(g)
                n += 1
                if (cc, uu, vv) != (c, u, v) or grid_from_params(cc, uu, vv) != g:
                    bad += 1
    # random integer grids, including negative centres
    rng = random.Random(20240607)
    for _ in range(3000):
        c = rng.randint(-50, 50)
        u = rng.randint(-50, 50)
        v = rng.randint(-50, 50)
        g = grid_from_params(c, u, v)
        cc, uu, vv = params_from_grid(g)
        n += 1
        if grid_from_params(cc, uu, vv) != g or magic_sum(g) != 3 * cc:
            bad += 1
    lo_shu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    cc, uu, vv = params_from_grid(lo_shu)
    n += 1
    if grid_from_params(cc, uu, vv) != lo_shu or magic_sum(lo_shu) != 15:
        bad += 1
    print(f"    completeness: {n} grids reconstruct exactly from "
          f"(centre, a00-centre, a02-centre): "
          f"{'PASS' if bad == 0 else f'{bad} FAILURES'}")
    return n, bad


def run_ap_structure():
    bad = n = 0
    for c in range(1, 26):
        for u in range(-25, 26):
            for v in range(-25, 26):
                g = grid_from_params(c, u, v)
                centre_lines = [g[1], [g[0][1], g[1][1], g[2][1]],
                                [g[0][0], g[1][1], g[2][2]],
                                [g[0][2], g[1][1], g[2][0]]]
                diffs = []
                for line in centre_lines:
                    d = line[1] - line[0]
                    if line[2] - line[1] != d:
                        bad += 1
                        break
                    diffs.append(abs(d))
                else:
                    n += 1
                    if sorted(diffs) != sorted([abs(u), abs(v), abs(u + v),
                                                abs(u - v)]):
                        bad += 1
    print(f"    AP structure: {n} grids (c in 1..25, |u|,|v| <= 25), the "
          f"four centre lines in AP with differences u-v, u+v, u, v up to "
          f"sign: {'PASS' if bad == 0 else f'{bad} FAILURES'}")
    return n, bad


def worked_examples():
    print("[2] statement worked examples, rerun fresh")
    n1, b1 = run_parametrisation_identity()
    n2, b2 = run_completeness()
    n3, b3 = run_ap_structure()
    ok = b1 == b2 == b3 == 0
    print(f"    -> {'PASS' if ok else 'FAILURES PRESENT'}")
    return {
        "parametrisation_identity": {"grids_checked": n1,
                                     "mismatches": b1},
        "completeness": {"grids_checked": n2, "mismatches": b2},
        "ap_structure": {"grids_checked": n3, "mismatches": b3},
        "pass": ok,
    }


# ---------------------------------------------------------------------------
# (3) the two known near-misses
# ---------------------------------------------------------------------------


def check_sallows():
    g = sallows_ls1_grid()
    sums = line_sums(g)
    distinct_ok = len(set(entries_of(g))) == 9
    all_squares = all(sqrt_or_none(x) is not None for x in entries_of(g))
    good = [s for s in sums if s == sums[0]]
    n_good = len(good)
    fail_idx = [i for i, s in enumerate(sums) if s != sums[0]]
    expected = {
        "n_good_sum": n_good == 7,
        "common_sum_21609": sums[0] == 21609,
        "fails_non_principal": fail_idx == [7],
        "bad_sum_38307": (sums[7] if fail_idx == [7] else None) == 38307,
        "all_squares": all_squares,
        "distinct": distinct_ok,
    }
    print("[3a] Sallows LS1 (Bremner 1999 (1)) — printed orientation")
    for r in g:
        print("      " + " | ".join(f"{x:>5} = {sqrt_or_none(x)!s:>3}^2"
                                    if sqrt_or_none(x) is not None
                                    else f"{x:>5}      " for x in r))
    print(f"      line sums: {sums}")
    print(f"      {7 if expected['n_good_sum'] else n_good} of 8 lines equal "
          f"{sums[0]} = 147^2 = 21609; "
          f"failing line: {LINE_NAMES[fail_idx[0]] if len(fail_idx) == 1 else fail_idx}, "
          f"sum {sums[fail_idx[0]] if len(fail_idx) == 1 else '?'}")
    print(f"      all entries squares: {all_squares}, distinct: {distinct_ok}")
    ok = all(expected.values())
    print(f"      -> {'PASS' if ok else 'FAIL ' + str(expected)}")
    return g, ok, expected


def check_bremner():
    g = bremner_magic_grid()
    sums = line_sums(g)
    entries = entries_of(g)
    non_squares = [x for x in entries if sqrt_or_none(x) is None]
    expected = {
        "magic_constant_541875": magic_sum(g) == 541875,
        "exactly_7_squares": count_squares(g) == 7,
        "non_squares_exact": sorted(non_squares) == [222121, 360721],
        "distinct": len(set(entries)) == 9,
        "positive": all(x > 0 for x in entries),
        "centre_425_squared": g[1][1] == 425 ** 2,
    }
    print("[3b] Bremner's true magic square (Bremner 1999 p. 290)")
    for r in g:
        print("      " + " | ".join(f"{x:>6} = {sqrt_or_none(x)!s:>3}^2"
                                    if sqrt_or_none(x) is not None
                                    else f"{x:>6} (non-square)" for x in r))
    print(f"      magic sum M = {magic_sum(g)} (all 8 lines), "
          f"centre = {g[1][1]} = 425^2 = M/3: "
          f"{3 * g[1][1] == magic_sum(g)}")
    print(f"      square entries: {count_squares(g)}; non-squares: "
          f"{sorted(non_squares)}")
    ok = all(expected.values())
    print(f"      -> {'PASS' if ok else 'FAIL ' + str(expected)}")
    return g, ok, expected


# ---------------------------------------------------------------------------
# (4) magic-graph incidence algebra over Q
# ---------------------------------------------------------------------------


def check_magic_graph():
    inc = magic_incidence_matrix()
    rank = rank_fraction_matrix(inc)
    kernel, witness = magic_params_basis()
    print(f"[4] magic graph: 8 lines x 9 cells incidence matrix over Q, "
          f"rank = {rank}, so dim kernel = {9 - rank}")
    print(f"    kernel basis (exact Fractions):")
    for vec in kernel:
        print("      " + ", ".join(str(x) for x in vec))
    # the single Q-relation among the eight line equations (computed by
    # an independent Fraction LDU in nullspace_fraction_matrix on the
    # transpose; cross-checked with sympy in the scratch probe)
    from lib.mss import nullspace_fraction_matrix
    transposed = [[inc[r][c] for r in range(8)] for c in range(9)]
    row_rel = nullspace_fraction_matrix(transposed)
    rel = [int(x) for x in row_rel[0]] if row_rel else None
    if rel:
        print(f"    single Q-relation among the 8 line vectors: {rel} "
              f"i.e. col sums 1+2+3 == row sums 1+2+3 (diagonals free)")
    else:
        print("    no row relation found")
    # structure of the two parametric grids
    u_g = entries_of(grid_from_params(0, 1, 0))
    v_g = entries_of(grid_from_params(0, 0, 1))
    print(f"    u-grid pattern   {u_g}")
    print(f"    v-grid pattern   {v_g}")
    # all line sums of witness equal?
    ws = line_sums(grid_from_params(1, 3, -5))
    print(f"    witness grid_from_params(1,3,-5) line sums all equal: "
          f"{len(set(ws)) == 1} (sums {ws})")
    # affine dimension: rank of the 7x9 matrix of differences L2-L1..L8-L1
    diff_rows = [[inc[i][j] - inc[0][j] for j in range(9)]
                 for i in range(1, 8)]
    diff_rank = rank_fraction_matrix(diff_rows)
    affine_dim = 9 - diff_rank
    ok = (rank == 7 and len(kernel) == 2 and affine_dim == 3)
    print(f"    affine magic space: rank(differences L2-L1..L8-L1) = "
          f"{diff_rank} over 9 cells -> dimension {affine_dim} = "
          f"1 (constant) + 2 (u,v), matching grid_from_params(c,u,v)")
    msg = ("PASS: kernel dim 2 = u,v vectors; affine dim 3 = c,u,v basis"
           if ok else "FAIL")
    print(f"    -> {msg}")
    return {"incidence_rank": rank,
            "kernel_dimension": 9 - rank,
            "kernel_basis_vectors": len(kernel),
            "line_relation": rel,
            "affine_magic_dimension": affine_dim,
            "pass": ok}


# ---------------------------------------------------------------------------
# (5) Bremner (c, u, v) extraction and the four d-tests
# ---------------------------------------------------------------------------


def bremner_params_test():
    g = bremner_magic_grid()
    M = magic_sum(g)
    c, u, v = params_from_grid(g)
    print("[5] Bremner grid: extract (c, u, v) from entries, "
          "c = M/3, and test the four centre-line AP differences")
    print(f"    M = {M}, c = M/3 = {M // 3}, extracted from entries: "
          f"{c} (grid[1][1])")
    print(f"    u = a00 - c = {u}, v = a02 - c = {v}")
    print(f"    c == 425^2: {c == 425 ** 2}")

    d_values = [("u", u), ("v", v), ("u+v", u + v), ("u-v", u - v)]
    results = []
    for name, d in d_values:
        cp, cm = c + d, c - d
        s_cp, s_cm = sqrt_or_none(cp), sqrt_or_none(cm)
        both = s_cp is not None and s_cm is not None
        results.append((name, d, cp, cm, s_cp, s_cm, both))
        print(f"    d = {name:>3} = {d:>9}: "
              f"c+d = {cp:>10} {'= ' + str(s_cp) + '^2' if s_cp is not None else '(non-square)'}"
              f", c-d = {cm:>10} {'= ' + str(s_cm) + '^2' if s_cm is not None else '(non-square)'}"
              f" -> both squares: {both}")
    n_both = sum(1 for r in results if r[6])
    names_both = [r[0] for r in results if r[6]]
    print(f"    booleans: {[(r[0], r[6]) for r in results]}")
    print(f"    exactly TWO true, namely {names_both}: "
          f"{n_both == 2 and set(names_both) == {'v', 'u+v'}}")
    ok = (c == 425 ** 2 and n_both == 2
          and set(names_both) == {"v", "u+v"})
    return {"c": c, "u": u, "v": v, "M_over_3_equals_425_sq": c == 425 ** 2,
            "d_results": [{"d": name, "value": d, "c+d": cp, "c-d": cm,
                           "both_squares": both}
                          for name, d, cp, cm, s_cp, s_cm, both in results],
            "both_square_booleans_ordered_u_v_uv_umv":
                [r[6] for r in results],
            "exactly_two": n_both == 2, "names": names_both, "pass": ok}


# ---------------------------------------------------------------------------
# (6) Pythagorean pairs realising the two satisfied relations
# ---------------------------------------------------------------------------


def pythagorean_pairs_test():
    c = 425 ** 2
    splits = two_square_splits(c)
    print("[6] Pythagorean split pairs of c = 425^2 = x^2 + y^2 "
          f"(x >= y > 0): {splits}")
    g = bremner_magic_grid()
    _, u, v = params_from_grid(g)
    targets = {"v": v, "u+v": u + v}
    checks = []
    for name, want in targets.items():
        hit = False
        for (a, b) in splits:
            if 2 * a * b == want:
                hit = True
                checks.append((name, want, (a, b),
                               a * a + b * b == c, 2 * a * b == want))
                print(f"    d = {name} = {want} realised by ({a}, {b}): "
                      f"{a}^2 + {b}^2 = {a * a + b * b} = 425^2: "
                      f"{a * a + b * b == c}; "
                      f"2*{a}*{b} = {2 * a * b} = d: {2 * a * b == want}")
        if not hit:
            checks.append((name, want, None, False, False))
            print(f"    d = {name} = {want}: NO split pair realises it "
                  f"(expected — not a satisfied relation)")
    # the two named pairs, verified independently of the split enumeration
    direct = [
        ("(385, 180) -> v", 385, 180, v),
        ("(408, 119) -> u+v", 408, 119, u + v),
    ]
    for label, a, b, want in direct:
        ok_ab = (a * a + b * b == c) and (2 * a * b == want)
        checks.append((label, want, (a, b), a * a + b * b == c, ok_ab))
        print(f"    direct {label}: 385-style check "
              f"{a}^2 + {b}^2 = {a * a + b * b} (== {c}: "
              f"{a * a + b * b == c}), 2ab = {2 * a * b} (== {want}: "
              f"{2 * a * b == want})")
    ok = all(b[3] and b[4] for b in checks)
    print(f"    -> {'PASS: c = x^2 + y^2, d = 2xy realised exactly twice' if ok else 'FAIL'}")
    return {"c": c, "split_pairs": splits, "checks": [list(t) for t in checks],
            "pass": ok}


# ---------------------------------------------------------------------------
# assemble everything
# ---------------------------------------------------------------------------


def main():
    t0 = time.time()
    print("=" * 78)
    print("check_near_misses.py — exact-integer oracle checks:")
    print("verifier, statement worked examples, the two 7-square"
          " near-misses,")
    print("magic-graph rank, (c,u,v) extraction, Pythagorean pairs.")
    print("=" * 78)

    results = {}
    results["verifier"] = test_verifier()
    results["worked_examples"] = worked_examples()
    sallows, s_ok, s_exp = check_sallows()
    bremner, b_ok, b_exp = check_bremner()
    results["sallows_ls1"] = s_exp
    results["bremner_magic"] = b_exp
    results["magic_graph"] = check_magic_graph()
    results["bremner_params"] = bremner_params_test()
    results["pythagorean_pairs"] = pythagorean_pairs_test()

    all_ok = (results["verifier"] and results["worked_examples"]["pass"]
              and s_ok and b_ok and results["magic_graph"]["pass"]
              and results["bremner_params"]["pass"]
              and results["pythagorean_pairs"]["pass"])

    # ---------------------------------------------------------------
    # JSON with provenance, one entry per near-miss (GOAL.md contract)
    # ---------------------------------------------------------------
    def grid_json(g):
        return {"grid": g,
                "all_entries_squares": all(
                    sqrt_or_none(x) is not None for x in entries_of(g)),
                "non_squares": [x for x in entries_of(g)
                                if sqrt_or_none(x) is None],
                "line_sums": line_sums(g)}

    sallows_entries = grid_json(sallows)
    bremner_entries = grid_json(bremner)

    near_misses = {
        "generated_by": "code/check_near_misses.py (direct construction "
                        "from the printed grids, exact integer arithmetic)",
        "run_time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                      time.gmtime()),
        "provenance": {
            "sallows_ls1": "Sallows, \"The Lost Theorem\", Math. "
                           "Intelligencer 19.4 (1997); printed as (1) in "
                           "A. Bremner, \"On squares of squares\", Acta "
                           "Arithmetica 88 (1999) p. 290 — local copy "
                           "research/sources/bremner-on-squares-of-squares-"
                           "1999.full.md; user brief calls this grid LS1 "
                           "and orients it as [127,46,58; 2,113,94; "
                           "74,82,97] — the transpose of the printed "
                           "orientation used here; squares identical.",
            "bremner_magic": "A. Bremner, \"On squares of squares\", "
                             "Acta Arithmetica 88 (1999) p. 290 — local "
                             "copy research/sources/bremner-on-squares-of-"
                             "squares-1999.full.md; said in the same "
                             "paragraph to have seven square entries and "
                             "that an example with eight distinct square "
                             "entries is unknown.",
        },
        "verified_by": {
            "all_checks_passed": all_ok,
            "verifier_used": "is_magic_square_of_squares from "
                             "code/lib/mss.py (exact math.isqrt)",
        },
        "near_misses": {
            "sallows_ls1": {
                "description": "7-square near-miss: 7 of 8 line sums "
                               "equal 147^2 = 21609; fails at the "
                               "non-principal diagonal (sum 38307)",
                "orientation_note": "user's orientation "
                                    "[127,46,58; 2,113,94; 74,82,97] is "
                                    "the transpose of Bremner's printed "
                                    "orientation [58,46,127; 94,113,2; "
                                    "97,82,74]",
                **sallows_entries,
            },
            "bremner_magic": {
                "description": "true 3x3 magic square with exactly 7 "
                               "square entries: all 8 line sums equal "
                               "541875; non-squares are 360721 and 222121",
                **bremner_entries,
            },
        },
        "falsifier_note": "GOAL.md: every impossibility lemma this run "
                          "produces must be run against BOTH entries of "
                          "this witness set.",
    }

    out_path = f"{OUT_DIR}/near_misses.json"
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(near_misses, fh, indent=2)
        fh.write("\n")
    print(f"\nWrote {out_path}")

    print("=" * 78)
    print(f"Overall: {'ALL CHECKS PASSED' if all_ok else 'FAILURES PRESENT'}"
          f" ({time.time() - t0:.2f}s)")
    print("=" * 78)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())