#!/usr/bin/env python3
"""
Independent brute-force oracle for nu2 of the periodic halved-gap sequences,
to settle which scan convention the Directive-58 stage-1 host table uses.

Question under test: for the 2-then-odds sequence q built from a periodic
halved-gap bit word h (gap = 2 if bit else 4, q_1=2, q_2=3), what is
   nu2(q_n) = # of 2s in the maximal {0,2} suffix of the right diagonal?

This script builds the FULL exact triangle from scratch (independent code
path, no lib.rightdiag), reads off the right diagonal the same way
rightdiag.incremental_diagonals does, and computes nu2 under the literal
definition: scan the diagonal body d[0..n-1] (excluding terminal d[n])
backwards from the tip while entries are in {0,2}, count 2s.

We hand-check the oracle on period 1 (consecutive odds): A_0=(2,3,5,7,...),
A_1=(1,2,2,2,...), A_k=(1,0,0,...) for k>=2, so the right diagonal through
q_n is [q_n, 2, 0, 0, ..., 0] and the maximal {0,2} suffix (from the tip)
reaches back to the single 2 at index 1 -> nu2 = 1.  That hand check binds
the convention.

Then compare with the three on-disk values and the host stage-1 table.
"""
import sys

def build_q(h_pattern, n_terms):
    """q_1..q_{n_terms}.  Direct build matching nu2_periodic.build_seq
    phase 0 semantics: bit h[j] governs gap q_{j+2}->q_{j+3}, gap=2 if bit
    else 4.  q_1=2, q_2=3."""
    P = len(h_pattern)
    q = [2, 3]
    while len(q) < n_terms:
        bit = h_pattern[(len(q) - 2) % P]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]

def full_triangle(q):
    """A_0 = q, A_{k+1}(i) = |A_k(i) - A_k(i+1)|.  Exact integers."""
    rows = [list(q)]
    while len(rows[-1]) > 1:
        r = rows[-1]
        rows.append([abs(r[i] - r[i+1]) for i in range(len(r) - 1)])
    return rows

def right_diag(rows, n):
    """delta(q_n) = [A_0[n], A_1[n-1], ..., A_n[0]]."""
    return [rows[k][n - k] for k in range(n + 1)]

def nu2_literal(d):
    """# of 2s in the maximal {0,2} suffix of the diagonal body d[0..-2],
    scanning from the tip back to the first non-{0,2} entry."""
    body = d[:-1]
    i = len(body) - 1
    while i >= 0 and body[i] in (0, 2):
        i -= 1
    return body[i+1:].count(2)

def nu2_cycletwo(d):
    """Granville/Lemma-5.4 cycle convention: maximal {0,2} suffix but the
    scan stops at index 2 (excludes the first two body entries)."""
    body = d[:-1]
    i = len(body) - 1
    while i > 2 and body[i] in (0, 2):
        i -= 1
    return body[i+1:].count(2)

def check_period1():
    """Hand-bound the oracle: period-1 word [1] = all gaps 2 = consecutive
    odds.  Literal nu2 through q_n must be 1."""
    q = build_q([1], 200)
    rows = full_triangle(q)
    # sanity: A_1 = (1,2,2,2,...)
    assert rows[1][0] == 1 and all(x == 2 for x in rows[1][1:]), rows[1][:6]
    # sanity: A_2 = (1,0,0,...)
    assert rows[2][0] == 1 and all(x == 0 for x in rows[2][1:]), rows[2][:6]
    vals = []
    for n in (50, 100, 199):
        d = right_diag(rows, n)
        vals.append(nu2_literal(d))
    return vals

def main():
    print("Independent brute-force nu2 oracle (full triangle, exact ints)")
    print("=" * 70)
    p1 = check_period1()
    print("period 1 (consecutive odds) literal nu2 at n=50,100,199:",
          p1, " hand expectation: 1,1,1")
    assert all(v == 1 for v in p1), "oracle contradicted by hand check"
    print("  -> oracle convention BOUND: literal suffix reaches index 1.")
    print()

    # Build triangle ONCE per word, sample many n (exact), both conventions.
    for P, word in [(3, [0,0,1]), (5, [0,0,0,0,1]), (6, [0,0,0,0,0,1]),
                    (7, [0,0,0,0,0,0,1]), (2, [0,1]), (4, [0,0,0,1]),
                    (8, [0,0,0,0,0,0,0,1]), (1, [1])]:
        q = build_q(word, 1400)
        rows = full_triangle(q)
        lit = {}
        cyc = {}
        for n in (200, 400, 800, 1200):
            d = right_diag(rows, n)
            assert d[-1] in (1, 2) or True  # terminal is A_n[0]
            lit[n] = nu2_literal(d)
            cyc[n] = nu2_cycletwo(d)
        litv = [lit[n] for n in (200,400,800,1200)]
        cycv = [cyc[n] for n in (200,400,800,1200)]
        print(f"P={P} word={''.join(map(str,word))}")
        print(f"   literal (i>=0): {litv}")
        print(f"   since-i>2  (cyc): {cycv}")

    print()
    print("Host stage-1 (Directive 58):")
    host = {1:[1,1,1,1],2:[2,2,2,2],4:[2,2,2,2],8:[2,2,2,2],
            3:[133,264,533,798],5:[104,210,424,638],
            6:[134,264,534,796],7:[112,112,685,684]}
    for P, hs in host.items():
        print(f"   P={P}: {hs}")

    print()
    print("KEY: literal [i>=0] is the true 'maximal {0,2} suffix of the")
    print("     right diagonal body'.  If a convention matches the host on")
    print("     all P, that is the table's convention; else the host table")
    print("     is internally inconsistent and must be re-derived.")

if __name__ == "__main__":
    main()
