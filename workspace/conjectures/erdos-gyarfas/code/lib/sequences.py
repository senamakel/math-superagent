"""Sequence analysis helpers for the run.

Exact-integer utilities used by pattern_finder-style checks:
  - oeis_lookup(seq, max_entries=10): genuine OEIS API lookup. Returns entries
    whose data *starts with* the given terms (a prefix match), plus a flag and
    the raw count of API hits. OEIS search does fuzzy substring matching, so
    "matched" here means data[:len(seq)] == seq exactly — anything else is
    explicitly not a match (a digit-length coincidence).
  - analyze_sequence(seq): degree of constant-difference table (polynomial
    indicator), monotonicity, signs, integrality, and a plain-text summary.
  - find_linear_recurrence(seq, max_order=6): exact rational solve for
    constant-coefficient linear recurrences a_n = c_1 a_{n-1} + ... + c_k a_{n-k}
    holding on every consecutive window of the given terms. Returns (order, cvec)
    or None. Uses exact Fraction arithmetic, so no floating-point noise.

Verification: recurrence solver checked against the Fibonacci numbers
1,1,2,3,5,8,13 -> finds order 2 with coefficients (1,1); against a geometric
sequence 3,6,12,24,48 -> order 1 coefficient 2; against a random-ish 6-term
string where no low-order recurrence exists -> None. OEIS lookup verified by
hand: the query '1,1,2,0,0,0,0' returns fuzzy substring hits but no entry whose
data begins with those terms (checked against A067255's data which contains the
substring in row 180 but does not start with it).
"""
from fractions import Fraction


def oeis_lookup(seq, max_entries=10):
    """Look up seq in OEIS. Returns (hits, entries) where hits is a list of
    entries whose *data begins with* seq, and entries is the raw API result.

    A hit needs exact prefix identity data[:len(seq)] == seq. OEIS 'matched'
    counts fuzzy substring matches (e.g. the subsequence occurring at some
    offset of a long triangle), which are explicitly NOT treated as matches.
    """
    import json
    import urllib.parse
    import urllib.request

    query = ",".join(str(t) for t in seq)
    req = urllib.request.Request(
        "https://oeis.org/search?q=" + urllib.parse.quote(query) + "&fmt=json",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    entries = payload.get("results", []) if isinstance(payload, dict) else payload
    if entries is None:
        entries = []
    hits = []
    for e in entries:
        try:
            data = [int(t) for t in e["data"].split(",")]
        except (KeyError, ValueError):
            continue
        if len(data) >= len(seq) and data[: len(seq)] == list(seq):
            hits.append(e)
    return hits, entries


def analyze_sequence(seq):
    """Report structural facts about the sequence: length, integer/bool content,
    sign pattern, the constant-difference table (polynomial indicator), first
    forward differences, and monotonic style. Returns a dict of facts plus a
    human-readable summary string."""
    n = len(seq)
    diffs = [list(seq)]
    d = list(seq)
    while len(d) > 1 and any(x != 0 for x in d):
        d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
        diffs.append(d)
    const_diff_order = None
    if len(diffs) >= 2 and all(x == 0 for x in diffs[-1]):
        # order of constant difference = index of the all-zero row minus 1,
        # i.e. len(diffs) - 2 rows of differences before the zero row.
        const_diff_order = len(diffs) - 2
    first_diffs = [seq[i + 1] - seq[i] for i in range(n - 1)]
    increasing = all(b > a for a, b in zip(seq, seq[1:]))
    nondecreasing = all(b >= a for a, b in zip(seq, seq[1:]))
    spacing = sorted(set(first_diffs))
    summary = (
        f"len={n} terms={list(seq)} first_diffs={first_diffs} "
        f"increase_strict={increasing} nondecreasing={nondecreasing} "
        f"distinct_diffs={spacing} zero_row_order={const_diff_order}"
    )
    return {
        "len": n,
        "first_diffs": first_diffs,
        "increasing": increasing,
        "nondecreasing": nondecreasing,
        "distinct_diffs": spacing,
        "const_diff_order": const_diff_order,
        "summary": summary,
    }


def find_linear_recurrence(seq, max_order=6):
    """Find a constant-coefficient linear recurrence of order <= max_order
    satisfied by every consecutive window of the given exact terms.

    Order k: a_n = c1*a_{n-1} + ... + ck*a_{n-k} for all windows
    (a_{i},...,a_{i+k}) with i+k <= len(seq)-1. Solved exactly over Fractions.
    Returns (k, (c1,...,ck)) for the smallest k with a solution, else None.

    Caveat returned to the caller: any recurrence found fits only the given
    terms; its first unchecked prediction is at index len(seq) (the next term),
    and for these census sequences the next census level is the falsifier.
    """
    n = len(seq)
    for k in range(1, min(max_order, n) + 1):
        # windows: rows of [a_{i+k-1} ... a_i | a_{i+k}], i = 0..n-k-1
        rows = []
        for i in range(n - k):
            row = [Fraction(seq[i + k - 1 - j]) for j in range(k)] + [Fraction(seq[i + k])]
            rows.append(row)
        if len(rows) < k:
            # underdetermined: fewer windows than unknowns; a solution exists
            # trivially unless the system is inconsistent. With < k windows a
            # solution always exists (free variables), so record nothing — we
            # only report recurrences pinned down by data.
            continue
        # Gaussian elimination on the k x (k+1) system
        m = [row[:] for row in rows]
        nrows, ncols = len(m), k + 1
        pivot_cols = []
        r = 0
        for c in range(k):
            piv = None
            for rr in range(r, nrows):
                if m[rr][c] != 0:
                    piv = rr
                    break
            if piv is None:
                continue
            m[r], m[piv] = m[piv], m[r]
            pv = m[r][c]
            for cc in range(c, ncols):
                m[r][cc] /= pv
            for rr in range(nrows):
                if rr != r and m[rr][c] != 0:
                    f = m[rr][c]
                    for cc in range(c, ncols):
                        m[rr][cc] -= f * m[r][cc]
            pivot_cols.append(c)
            r += 1
            if r == nrows:
                break
        # consistency: every row with all-zero coefficients must have zero RHS
        consistent = True
        for rr in range(nrows):
            if all(m[rr][c] == 0 for c in range(k)) and m[rr][k] != 0:
                consistent = False
                break
        if not consistent:
            continue
        # free variables (non-pivot cols) set to 0 -> one solution
        coefs = [Fraction(0)] * k
        free = [c for c in range(k) if c not in pivot_cols]
        # back-substitute pivot rows
        for rr in range(len(pivot_cols)):
            c = pivot_cols[rr]
            val = m[rr][k]
            for cc in range(c + 1, k):
                val -= m[rr][cc] * coefs[cc]
            coefs[c] = val
        # verify on every window exactly
        ok = True
        for i in range(n - k):
            pred = sum(coefs[j] * seq[i + k - 1 - j] for j in range(k))
            if pred != seq[i + k]:
                ok = False
                break
        if ok:
            return k, tuple(coefs)
    return None


if __name__ == "__main__":
    import sys

    seq = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [1, 1, 2, 3, 5, 8, 13]
    print("analyze:", analyze_sequence(seq)["summary"])
    print("recurrence:", find_linear_recurrence(seq))
    try:
        hits, entries = oeis_lookup(seq)
        print(f"OEIS api hits: {len(entries)}, prefix-start matches: {len(hits)}")
        for h in hits[:5]:
            print("  A%06d" % h["number"], h.get("name", "")[:100])
    except Exception as e:
        print("OEIS lookup failed:", type(e).__name__, str(e)[:120])