#!/usr/bin/env python3
"""Task C: checker-soundness self-test of is_magic_square_of_squares.

Goal: exercise the True branch of the decision oracle on a genuine 3x3
magic square of squares.  A DISTINCT-entry example cannot be exhibited:
no 3x3 magic square of squares with nine distinct positive entries is
known at all — that IS the open conjecture (the run's catalogue,
research/summaries/morgenstern-smallest-entry-8-digit.md, records that
every entry of any such square is at least the square of an 8-digit
number, so no small example exists).  Per the task's stated fallback we
state that plainly and instead verify the checker on genuine magic
squares of squares WITH repeated entries, plus the rejection cases.

Cases:
  1. {1,25,49} family grid A: [[1,49,25],[49,25,1],[25,1,49]] — a true
     magic square (constant 75 = 3*25, centre 25) whose nine entries
     are the squares 1^2, 5^2, 7^2 (each three times): relaxed True,
     strict False (not-distinct).
  2. Same family via the parametrisation (c,u,v) = (25,0,-24):
     [[25,49,1],[1,25,49],[49,1,25]] — magic (constant 75), entries
     {1,25,49} each three times: relaxed True, strict False.
  3. nine 1s: relaxed True (all squares, magic), strict False.
  4. negative control: (c,u,v) = (25,0,24) gives
     [[49,1,49],[49,25,1],[1,49,25]] — all entries squares with
     repeats but NOT magic (principal diagonal 99 vs constant 75);
     relaxed must be False, strict False.
  5. distinct positive squares, not magic: strict/relaxed False.
  6. Lo Shu (magic, not all squares): strict/relaxed False.
  7. Sallows LS1 near-miss: strict/relaxed False, diagnosed not-magic
     (7 of 8 lines equal — checker catches the failing diagonal).
  8. Bremner's 7-square magic square: strict/relaxed False, diagnosed
     not-a-square (exactly 360721, 222121 are non-squares).

Soundness reading: the relaxed branch is the only exhibitable True
branch; strict adds exactly the distinctness condition.  Nothing in the
known witness set passes strict, and every rejection is diagnosed for
the right reason.  All arithmetic exact (math.isqrt via lib/mss.py).
"""
from lib.mss import (bremner_magic_grid, failure_of,
                     is_magic_square_of_squares, line_sums, magic_sum,
                     sallows_ls1_grid)


def show(label, g, exp_strict, exp_relaxed):
    s = is_magic_square_of_squares(g, require_distinct=True)
    r = is_magic_square_of_squares(g, require_distinct=False)
    diag = failure_of(g, require_distinct=True)
    ok = (s == exp_strict) and (r == exp_relaxed)
    print(f"  {'ok  ' if ok else 'FAIL'} {label}")
    print(f"       strict {s} (expected {exp_strict}) / "
          f"relaxed {r} (expected {exp_relaxed}); diagnosis: {diag}")
    return ok


def main():
    print("#" * 78)
    print("# Task C: checker-soundness self-test of")
    print("# is_magic_square_of_squares (code/lib/mss.py, exact isqrt)")
    print("#" * 78)

    print("[0] statement: a distinct-entry 3x3 magic square of squares")
    print("    cannot be exhibited, so the True-branch oracle test uses")
    print("    genuine magic squares of squares with REPEATED entries.")
    print("    (None with distinct entries is known: that is the open")
    print("    conjecture; catalogue bound: every entry >= 8-digit")
    print("    square, Morgenstern, source summary in research/.)")

    ok = True

    fam_a = [[1, 49, 25], [49, 25, 1], [25, 1, 49]]
    print("\n[1] genuine magic square of squares with repeats "
          "({1,25,49} AP family):")
    print(f"    grid {fam_a}")
    m = magic_sum(fam_a)
    print(f"    magic constant {m}, centre {fam_a[1][1]} = M/3: "
          f"{3 * fam_a[1][1] == m}; entries are 1^2, 5^2, 7^2")
    ok &= show("    strict False (not-distinct) / relaxed True (accept)",
               fam_a, False, True)

    fam_b = [[25, 49, 1], [1, 25, 49], [49, 1, 25]]   # (c,u,v)=(25,0,-24)
    print("\n[2] same family via parametrisation (c,u,v)=(25,0,24):")
    print("    grid [[25,49,1],[1,25,49],[49,1,25]] (magic, constant 75 =")
    print("    3*25; entries 1,25,49 each three times)")
    mb = magic_sum(fam_b)
    print(f"    magic constant {mb}, centre {fam_b[1][1]} = M/3: "
          f"{3 * fam_b[1][1] == mb}")
    ok &= show("    strict False / relaxed True", fam_b, False, True)

    ones = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print("\n[3] nine 1s (magic + all squares, heavily repeated):")
    ok &= show("    strict False / relaxed True", ones, False, True)

    neg = [[49, 1, 49], [49, 25, 1], [1, 49, 25]]   # (c,u,v)=(25,0,24)
    print("\n[4] negative control: all squares with repeats but NOT")
    print("    magic (c,u,v)=(25,0,24): rows 99/75/75, cols 99/75/75,")
    print("    diagonal 49+25+25=99 != 75): relaxed must be False")
    ok &= show("    strict False / relaxed False", neg, False, False)

    not_magic = [[1, 9, 25], [49, 81, 4], [16, 36, 64]]
    print("\n[5] distinct positive squares, not magic"
          " (sums 35/134/116):")
    ok &= show("    strict False / relaxed False", not_magic, False, False)

    lo_shu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    print("\n[6] Lo Shu (magic constant 15, entries not all squares):")
    ok &= show("    strict False / relaxed False", lo_shu, False, False)

    print("\n[7] Sallows LS1 7-square near-miss (7 of 8 sums 21609,")
    print("    failing non-principal diagonal 38307):")
    ok &= show("    strict False / relaxed False (not-magic)",
               sallows_ls1_grid(), False, False)

    print("\n[8] Bremner's true 7-square magic square (all 8 sums")
    print("    541875; non-squares 360721, 222121):")
    ok &= show("    strict False / relaxed False (not-a-square)",
               bremner_magic_grid(), False, False)

    print()
    print("[9] soundness reading")
    print("    * relaxed True  <=>  all 8 line sums equal AND all 9")
    print("      entries positive squares (distinctness waived):")
    print("      exhibited on cases [1]-[3]")
    print("    * strict False on the same grids for exactly the")
    print("      distinctness reason (diagnosis not-distinct), not")
    print("      because of magic or squares: above")
    print("    * the all-square repeated but NOT-magic grid is rejected")
    print("      in the relaxed branch too (diagonal 99 != 75): case [4]")
    print("    * both literature near-misses rejected with correct")
    print("      diagnoses (not-magic / not-a-square): above")
    print("    * a distinct-entry True instance remains unexhibited:")
    print("      it is the open conjecture, not a checker gap.")

    print("#" * 78)
    print(f"# CHECKER SELF-TEST: {'ALL CASES AS EXPECTED' if ok else 'FAILURES PRESENT'}")
    print("#" * 78)


if __name__ == "__main__":
    main()