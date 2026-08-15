"""Verify the record-low index recurrence for Project Euler 700.

Sequence: c_n = A*n mod M, with
    A = 1504170715041707
    M = 4503599627370517
An Eulercoin is a term strictly smaller than every earlier term: the record low
(prefix minimum) of the sequence.

The recurrence (sourced -- research/summaries/record-low-recurrence.md, method
of brob26 from the PE700 thread):

    n_{k+2} = ceil(c_{n_k} / c_{n_{k+1}}) * n_{k+1} - n_k

gives successive record-low indices, starting from n_1 = 1 and n_2 = first
index after 1 whose value is below A (on the real pair, n_2 = 3). Because
gcd(A,M)=1 the sequence is a permutation of the residues, the values strictly
decrease at each step of the recurrence, and the iteration terminates at value 0.

Checks performed here:
 1. On several small (A,M) pairs, the recurrence iterated to termination exactly
    reproduces the forward brute-force running-minimum scan (incl. the given
    coin lists, e.g. A=7,M=17 -> 7@1, 4@3, 1@5, 0@17, sum 12).
 2. On the actual (A,M), the first len(brute) recurrence coins match the coins
    a forward scan up to n ~ 10^6 actually finds.
 3. The recurrence reproduces the statement's a_1 = 1504170715041707,
    a_3 = 8912517754604, and the first-two sum 1513083232796311.
 4. Prints math.gcd(A, M).

Output should be captured to code/out/verify_recurrence.txt.
"""
from math import gcd, ceil

A = 1504170715041707
M = 4503599627370517


def record_lows_brute(A, M, limit_n):
    """Forward scan of c_n = A*n mod M for n = 1..limit_n.

    Returns the record lows (prefix minima) as [(n, c_n), ...] in order of
    occurrence. This is the naive oracle: one modular multiply per step, keep a
    coin whenever the value drops below the running minimum.
    """
    coins = []
    running_min = None
    for n in range(1, limit_n + 1):
        c = (A * n) % M
        if running_min is None or c < running_min:
            coins.append((n, c))
            running_min = c
    return coins


def first_record_low_after_one(A, M):
    """Smallest n > 1 with A*n mod M < A mod M (= A, since A < M)."""
    low = A % M
    n = 2
    while True:
        if (A * n) % M < low:
            return n
        n += 1


def record_lows_recurrence(A, M, n2=None, max_steps=None):
    """Generate record lows via the index recurrence.

    n_1 = 1 with value A%M. n_2 defaults to first_record_low_after_one(A, M)
    (pass it when already known). Then iterates
        n_{k+2} = ceil(c_{n_k}/c_{n_{k+1}}) * n_{k+1} - n_k
    until a value hits 0 (the final Eulercoin), or max_steps steps.
    Returns [(n, c_n), ...].
    """
    c1 = A % M
    if n2 is None:
        n2 = first_record_low_after_one(A, M)
    c2 = (A * n2) % M
    res = [(1, c1), (n2, c2)]
    steps = 0
    while True:
        nk, ck = res[-2]
        nk1, ck1 = res[-1]
        if ck1 == 0:
            break
        alpha = ceil(ck / ck1)
        nk2 = alpha * nk1 - nk
        ck2 = (A * nk2) % M
        res.append((nk2, ck2))
        steps += 1
        if max_steps is not None and steps >= max_steps:
            break
    return res


def check_small_pair(A, M, expected_coins=None, expected_sum=None):
    """Compare recurrence vs brute on a small (A,M) where a full scan to M is
    cheap. Returns (ok, message)."""
    msgs = []
    brute = record_lows_brute(A, M, M)          # scan all the way to 0/index M
    rec = record_lows_recurrence(A, M)          # iterate to value 0
    ok_scan = rec == brute
    msgs.append(f"recurrence==brute(full scan to n=M): {ok_scan}")
    # strip the trailing value-0 entry when comparing sums, as in the statement
    nonzero = [c for _, c in brute if c != 0]
    sumvals = sum(nonzero)
    msgs.append(f"coins (n,val): {brute}")
    msgs.append(f"sum of nonzero coins: {sumvals}")
    ok_all = ok_scan
    if expected_coins is not None:
        ok_coins = brute == expected_coins
        msgs.append(f"matches given coin list {expected_coins}: {ok_coins}")
        ok_all = ok_all and ok_coins
    if expected_sum is not None:
        ok_sum = sumvals == expected_sum
        msgs.append(f"matches given sum {expected_sum}: {ok_sum}")
        ok_all = ok_all and ok_sum
    # also require the recurrence's first term to be A and second to be the
    # small-pair record low
    if len(rec) >= 2:
        ok_first = rec[0] == (1, A % M) and rec[1][1] == brute[1][1]
        msgs.append(f"first two recurrence coins consistent with brute: {ok_first}")
        ok_all = ok_all and ok_first
    return ok_all, "; ".join(msgs)


def main():
    print("=" * 72)
    print("Verify record-low recurrence for Project Euler 700")
    print("=" * 72)

    # ---- print gcd(A,M) ------------------------------------------------
    g = gcd(A, M)
    print("\ngcd(A, M) =", g)
    assert g == 1, "recurrence needs gcd(A,M)=1"
    assert 0 < A < M, "need 0 < A < M"
    print("PASS: gcd(A,M)=1 and 0 < A < M (hypotheses of the theorem hold)")

    # ---- worked-example / statement checks on the real pair -------------
    rec_full = record_lows_recurrence(A, M, n2=3)
    a1 = rec_full[0][1]
    a3 = rec_full[1][1]
    sum_two = a1 + a3
    print("\n-- Statement values from recurrence --")
    print("a_1 (recurrence) =", a1)
    print("a_3 (recurrence) =", a3)
    print("sum a_1 + a_3   =", sum_two)
    assert a1 == 1504170715041707, f"a_1 mismatch: {a1}"
    assert a3 == 8912517754604, f"a_3 mismatch: {a3}"
    assert sum_two == 1513083232796311, f"sum mismatch: {sum_two}"
    print("PASS: recurrence gives a_1=1504170715041707, "
          "a_3=8912517754604, first-two sum=1513083232796311")

    # ---- small test pairs ----------------------------------------------
    print("\n-- Small test moduli --")
    results = []
    small = [
        (7, 17, [(1, 7), (3, 4), (5, 1), (17, 0)], 12),
        (3, 23, None, None),
        (5, 13, None, None),
    ]
    for A_s, M_s, coins, ssum in small:
        ok, msg = check_small_pair(A_s, M_s, coins, ssum)
        results.append((f"A={A_s}, M={M_s}", ok))
        print(f"A={A_s}, M={M_s}: {'PASS' if ok else 'FAIL'}  ({msg})")
        assert ok, f"small pair A={A_s}, M={M_s} FAILED"

    # ---- real pair: forward scan up to n ~ 1e6 --------------------------
    LIMIT = 10**6
    print(f"\n-- Real pair: forward scan to n = {LIMIT} vs recurrence --")
    brute_real = record_lows_brute(A, M, LIMIT)
    # take only as many recurrence coins as the forward scan reached
    rec_prefix = rec_full[:len(brute_real)]
    print(f"coins found by forward scan up to n={LIMIT}: {len(brute_real)}")
    match = rec_prefix == brute_real
    print(f"recurrence[:{len(brute_real)}] == brute scan: {match}")
    if not match:
        for i, (r, b) in enumerate(zip(rec_prefix, brute_real)):
            if r != b:
                print(f"  first mismatch at index {i}: rec={r} brute={b}")
    assert match, "recurrence disagrees with forward scan on the real pair!"
    print("PASS: recurrence matches forward scan on the real pair "
          f"(first {len(brute_real)} coins, indices <= {LIMIT})")

    # ---- first ~10 Eulercoins from the recurrence ------------------------
    print("\n-- First 10 Eulercoins (index, value) from recurrence --")
    for nk, ck in rec_full[:10]:
        print(f"   n = {nk:>4}   c_n = {ck}")

    # ---- summary ---------------------------------------------------------
    print("\n" + "=" * 72)
    all_ok = all(ok for _, ok in results) and True  # everything asserted above
    print("ALL CHECKS:", "PASS" if all_ok else "FAIL")
    print("=" * 72)
    return 0 if all_ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
