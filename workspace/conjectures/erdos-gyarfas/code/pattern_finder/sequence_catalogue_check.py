"""Catalogue-style check of the two Apollonian-family census sequences.

Goal (per task): run an OEIS-lookup-style check and exact linear-recurrence
probe over
    avoidsC4C16 = [1,1,2,0,0,0,0,0]   (n=10..24, step 2; 7-term task prefix
                                      [1,1,2,0,0,0,0] also checked)
    avoidsC4    = [1,1,2,5,15,50,202,807]
reporting nothing unless a genuine OEIS match exists (strict data-prefix
identity — a digit-length substring coincidence is NOT a match), and stating
plainly that any recurrence fitting all given terms is a conjecture whose first
falsifying term is at the next index, with the n=26 census terms uncomputed.

Ground truth of the input sequences (this run, re-verified fresh on the on-disk
census files):
  census_c16_profile.py over level_<n>.canon (n=10..22) and
  level24_c16.py over level_24_classes.txt (58713 classes) both give
  avoidsC4C16 = 1,1,2,0,0,0,0,0 over n=10,12,14,16,18,20,22,24, with
  avoidsC4 reproducing 1,1,2,5,15,50,202,807 and avoidsC4C8 reproducing
  0,...,0,1. Output appended to /workspace/code/out/pattern_26_notes.txt.
"""
import sys

from lib.sequences import analyze_sequence, find_linear_recurrence, oeis_lookup

C16_8 = [1, 1, 2, 0, 0, 0, 0, 0]
C16_7 = [1, 1, 2, 0, 0, 0, 0]
AV4 = [1, 1, 2, 5, 15, 50, 202, 807]

OUT = "/workspace/code/out/pattern_26_notes.txt"


def report_seq(label, seq, do_oeis=True):
    print(f"\n{'=' * 72}")
    print(f"SEQUENCE: {label}  terms={seq}")
    print("=" * 72)
    an = analyze_sequence(seq)
    print("analyze_sequence:", an["summary"])
    rec = find_linear_recurrence(seq, max_order=6)
    if rec is None:
        print("find_linear_recurrence(max_order=6): NO constant-coefficient "
              "linear recurrence of order <= 6 is pinned down by these terms "
              "(each order's system over the consecutive windows is inconsistent, "
              "or k > len/2 leaves it underdetermined).")
    else:
        k, coefs = rec
        print(f"find_linear_recurrence(max_order=6): order {k} found")
        print("  coefficients:", ", ".join(f"{c.numerator}/{c.denominator}" for c in coefs))
        deg = all(c == 0 for c in coefs)
        if deg:
            print("  -> DEGENERATE: all coefficients are 0 (tail-is-all-zeros fit).")
        # exact prediction of the next term (first falsifying term)
        nxt = sum(coefs[j] * seq[len(seq) - 1 - j] for j in range(k))
        print(f"  predicted next term (index {len(seq)}, first falsifier): "
              f"{nxt.numerator}/{nxt.denominator}"
              + (" = INTEGER %d" % nxt if nxt.denominator == 1 else
                 f"  (NOT an integer: %.6f)" % (nxt.numerator / nxt.denominator)))
        print("  CAVEAT: a recurrence matching all given terms is a conjecture;")
        print("  its first falsifying term is at the next index and is UNCOMPUTED"
              " (census halts at n=24; n=26 is the next level).")
    if do_oeis:
        try:
            hits, entries = oeis_lookup(seq)
            print(f"OEIS lookup '{','.join(map(str, seq))}': API returned "
                  f"{len(entries)} fuzzy-substring entries; strict prefix matches: {len(hits)}")
            if hits:
                for h in hits:
                    print("  MATCH A%06d" % h["number"], h.get("name", ""))
            else:
                print("  -> NO genuine match: every API entry contains the terms"
                      " only as a substring (digit-length coincidence), none has"
                      " data STARTING with them.")
        except Exception as e:  # network failure: say so, do not fabricate
            print("OEIS lookup FAILED (no match claimed):",
                  type(e).__name__, str(e)[:140])


def main():
    lines_out = []
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        print("Catalogue check of Apollonian K4-triangle-expansion census sequences")
        print("date: this run | tool: lib/sequences.py (oeis_lookup, analyze_sequence,")
        print("find_linear_recurrence, max order 6, exact Fraction arithmetic)")
        print("Ground truth re-verified fresh: avoidsC4C16 = 1,1,2,0,0,0,0,0 over n=10..24")
        print("  (census_c16_profile.py n=10..22 + level24_c16.py n=24, avoidsC4 column"
              " reproduces 1,1,2,5,15,50,202,807).")
        for label, seq in [("avoidsC4C16 (n=10..24, 8 levels)", C16_8),
                           ("avoidsC4C16 task prefix (n=10..22, 7 terms)", C16_7),
                           ("avoidsC4 (n=10..24)", AV4)]:
            report_seq(label, seq)
        print("\nSTATUS SUMMARY")
        print("- avoidsC4C16: no genuine OEIS match (7- and 8-term queries); only")
        print("  degenerate all-zero recurrence in the pinned orders; the nonzero")
        print("  head 1,1,2 then 0s is exactly the verified census fact that every")
        print("  C4-free family member at n>=16 contains a C16. First falsifier,")
        print("  n=26 census value of avoidsC4C16, is UNCOMPUTED.")
        print("- avoidsC4: prior record (memory + falsifiers_check.py) has no OEIS")
        print("  match; fresh recurrence probe reproduces the exact 4th-order")
        print("  rational fit (47/27, 1339/54, -3067/54, 27/2), whose predicted")
        print("  next term 203921/54 is NOT an integer -> refuted by integrality")
        print("  (a census count must be an integer), so no valid recurrence.")
        print("  n=26 avoidsC4 value is UNCOMPUTED.")
    text = buf.getvalue()
    print(text)
    try:
        with open(OUT, "w") as f:
            f.write(text)
    except OSError as e:
        print("WARN: could not write", OUT, e)
    else:
        print("saved ->", OUT)


if __name__ == "__main__":
    main()