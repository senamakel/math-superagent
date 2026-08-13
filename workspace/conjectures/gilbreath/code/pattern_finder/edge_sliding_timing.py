#!/usr/bin/env python3
"""Verify the exact regeneration-timing mechanics on the prime rows.

Edge-sliding (proved consequence of rule-90 interior + step law):
during an erosion run from K with rightmost-2 depth D, the edge x_k = A_k[b_k]
is 0 for K <= k < K+D and 2 at k = K+D.  Machine-confirmed 0/1509 + 0/60 by
the full analysis; here we check the *timing consequence* the run actually
cares about:

  T1. The first (2,4)-event on or after K+D fires at the FIRST row k >= K+D
      with (x_k, y_k) = (2,4)  -- there is no row with (2,4) before K+D
      (early) and no row with (2,4) at K+D that fails to fire (the step law
      says (2,4) always gives b_{k+1} >= b_k, i.e. fires).

Equivalently with events counted at the (x,y)=(2,4) level (jump >= 0):
  E = first event row after K; then E >= K+D and if y at K+D == 4 then
  E == K+D.

Also report the distribution of E - (K+D) for the late cases (intruder not 4
at K+D) split by the intruder value at K+D, to see whether the wait is the
drain time to 4.

Independent implementation (own sieve, own rows, own block measure); event =
row where edge x=A_k[b_k]==2 and intruder y=A_k[b_k+1]==4, i.e. the exact
step-law regeneration condition including jump-0 stalls.
"""
import numpy as np


def primes_bool(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    return [int(i) for i in np.nonzero(sieve)[0]]


def block_len(row):
    n = 0
    for v in row[1:]:
        if v in (0, 2):
            n += 1
        else:
            break
    return n


def rightmost2_depth(row, b):
    for col in range(b, 0, -1):
        if row[col] == 2:
            return b - col
    return None


def main():
    primes = primes_bool(20_000_000)
    cur = primes
    recs = []          # (k, b, x, y)
    rows_at = {}
    for k in range(1, 162):
        row = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        b = block_len(row)
        x = row[b] if b + 1 < len(row) else None
        y = row[b + 1] if b + 2 < len(row) else None
        recs.append((k, b, x, y))
        if k == 1 or (len(recs) >= 2 and recs[-2][2] == 2 and recs[-2][3] == 4):
            rows_at[k] = row
        cur = row
    # run starts: row 1, or the row after an event row (x==2 and y==4)
    ev = [k for (k, b, x, y) in recs if x == 2 and y == 4]
    runs = []
    K = 1
    for k in ev:
        runs.append((K, k, recs[K - 1][1]))
        K = k + 1
    print(f"events (x=2,y=4, incl. jump-0 stalls): {len(ev)}")
    print(f"runs: {len(runs)}")

    early = 0
    hit = 0
    late = 0
    lates = []
    y_at_pred = {}
    profile_bad = 0
    for (K, E, bK) in runs:
        rowK = rows_at[K]
        d = rightmost2_depth(rowK, bK)
        # profile on [K, min(E,K+d)] (E may be < K+d only if the run ended
        # before the rightmost 2 surfaced -> would refute the proved core)
        end = min(E, K + d)
        for kk in range(K, end + 1):
            xk = recs[kk - 1][2]
            if kk < end and xk != 0:
                profile_bad += 1
            elif kk == end and xk != 2:
                profile_bad += 1
        yp = recs[K + d - 1][3] if K + d <= 161 else None
        y_at_pred[yp] = y_at_pred.get(yp, 0) + 1
        if E < K + d:
            early += 1
        elif E == K + d:
            hit += 1
        else:
            late += 1
            lates.append((E - (K + d), yp))
    print(f"profile-bad: {profile_bad} (must be 0: proved core)")
    print(f"timing over {len(runs)} runs: early {early}, hit-at-K+D {hit}, "
          f"late {late}")
    print(f"intruder value at K+D over runs: {dict(sorted(y_at_pred.items()))}")
    if lates:
        lates.sort()
        vals = sorted(set(v for _, v in lates))
        for v in vals:
            ws = [w for w, vv in lates if vv == v]
            print(f"  late with y at K+D = {v}: n={len(ws)} "
                  f"waits {sorted(set(ws))[:10]}... mean "
                  f"{sum(ws)/len(ws):.1f} max {max(ws)}")
    # T1: first (2,4) on/after K+D is exactly E
    t1_bad = 0
    for (K, E, bK) in runs:
        rowK = rows_at[K]
        d = rightmost2_depth(rowK, bK)
        for kk in range(K + d, E + 1):
            if kk == E:
                continue
            xk, yk = recs[kk - 1][2], recs[kk - 1][3]
            if xk == 2 and yk == 4:
                t1_bad += 1
    print(f"T1 violations ((2,4) strictly between K+D and E): {t1_bad}")
    # T2: if y at K+D == 4 then E == K+D
    t2_bad = 0
    for (K, E, bK) in runs:
        rowK = rows_at[K]
        d = rightmost2_depth(rowK, bK)
        yp = recs[K + d - 1][3] if K + d <= 161 else None
        if yp == 4 and E != K + d:
            t2_bad += 1
            print(f"  T2 FAIL K={K} E={E} K+D={K+d}")
    print(f"T2 violations (y==4 at K+D but event not there): {t2_bad}")


if __name__ == "__main__":
    main()