#!/usr/bin/env python3
"""Probe of the Lipschitz-excess functional E on ORIGINAL (un-halved) rows —
streaming version (no full-triangle memory). See lipschitz_excess_notes for
definition. For row A: e_i = max(0, |A(i)-A(i+1)|-2), E = sum_i e_i.

Exact identity: e_i=0 <=> next-row entry i in {0,2}; so the leading {0,2}
block of row k+1 = length of the leading zero-run of (e_i) in row k.

Reports over the stated depth/width only: (a) E non-increasing? first increase;
(b) identity; (c) min E over live rows; (d) E change along erosion vs events;
(e) total E vs total events.

Streams two passes: pass 1 computes E sequence + b_profile + first-increase.
Pass 2 (separate row-wise) identifies (2,4)-events and erosion steps and their
dE, keeping only the current row and the previous row.
"""
import time, sys
from lib.gilbreath import primes_up_to, rows_generator, block_profile

EXPECTED = {1:[1,2,2,4,2,4,2,4,6,2,6,4],2:[1,0,2,2,2,2,2,2,4,4,2,2],
            3:[1,2,0,0,0,0,0,2,0,2,0,0],4:[1,2,0,0,0,0,2,2,2,2,0,0],
            5:[1,2,0,0,0,2,0,0,0,2,0,2]}


def excess_info(row):
    """Return (E, leading_nonzero_pos)."""
    E = 0
    lnz = len(row) - 1
    for i in range(1, len(row) - 1):
        d = row[i] - row[i + 1]
        if d < 0:
            d = -d
        e = d - 2
        if e > 0:
            E += e
            if lnz == len(row) - 1:
                lnz = i
    return E, lnz


def analyze(primes, depth, label):
    t0 = time.time()
    # pass 1: E sequence, b_profile, first increase, min E over live
    gen = rows_generator(primes, depth)
    rows_iter = iter(gen)
    first = next(rows_iter)
    width = len(first)
    Es = []
    bprof = []
    lnz = []
    k = 0
    first_increase = None
    inc_triples = []
    for row in rows_iter:
        E, l = excess_info(row)
        Es.append(E)
        bprof.append(block_profile(row))
        lnz.append(l)
        if k >= 1:
            dE = Es[k] - Es[k - 1]
            if dE > 0 and first_increase is None:
                first_increase = k
            if dE > 0 and len(inc_triples) < 8:
                inc_triples.append((k, dE, Es[k - 1], Es[k]))
        k += 1
    nrows = len(Es)
    # identity: lnz(row k) == bprof(row k+1) for k in 0..nrows-2
    idfail = [(k, lnz[k], bprof[k + 1]) for k in range(nrows - 1)
              if lnz[k] != bprof[k + 1]]
    # live rows: b_k>=1
    live_min_E = min(Es[k] for k in range(nrows) if bprof[k] >= 1)
    live_lt1 = [k for k in range(nrows) if bprof[k] >= 1 and Es[k] < 1]
    all_min_E = min(Es)
    min_b = min(bprof)
    min_b_at = [k for k in range(nrows) if bprof[k] == min_b][:6]

    print(f"\n=== {label} ===")
    print(f"depth reached = {nrows-1}, width(row0) = {width}, time {time.time()-t0:.1f}s")
    print(f"(a) E non-increasing: first increase at row k={first_increase}"
          f"  (of {nrows-1} transitions)")
    print(f"    increase triples (k, dE, E_prev, E_k): {inc_triples}")
    print(f"    max dE over all transitions = {max(Es[k+1]-Es[k] for k in range(nrows-1))}")
    print(f"    all dE<=0 count = {sum(1 for k in range(nrows-1) if Es[k+1]-Es[k]<=0)} of {nrows-1}")
    print(f"(b) identity lnz(k)==bprof(k+1) violations = {idfail[:5]} (total {len(idfail)})")
    print(f"(c) min E over live rows (b>=1) = {live_min_E}")
    print(f"    live rows with E<1: total {len(live_lt1)} of {nrows}, first {live_lt1[:10]}")
    print(f"    min E over ALL rows = {all_min_E}")
    print(f"    min b over all rows = {min_b} at rows {min_b_at}")
    return Es, bprof, lnz, nrows, t0


def analyze_events(primes, depth, label, Es, bprof, nrows):
    """Stream rows, identify (2,4)-events and erosion steps, tally dE."""
    t0 = time.time()
    gen = rows_generator(primes, depth)
    it = iter(gen)
    row_prev = next(it)   # row 0
    ero = {"up": 0, "down": 0, "flat": 0}
    ev = {"up": 0, "down": 0, "flat": 0, "total": 0}
    event_rows = []
    for k in range(nrows - 1):
        row_k1 = next(it)   # row k+1
        rk = row_prev       # row k
        bk = bprof[k]
        bnext = bprof[k + 1]
        edge = rk[bk] if bk < len(rk) else None
        intr = rk[bk + 1] if bk + 1 < len(rk) else None
        is_event = (bk >= 1 and edge == 2 and intr == 4 and bnext >= bk)
        dE = Es[k + 1] - Es[k]
        if is_event:
            ev["total"] += 1
            event_rows.append((k, bnext - bk, dE))
            if dE > 0: ev["up"] += 1
            elif dE < 0: ev["down"] += 1
            else: ev["flat"] += 1
        else:
            if dE > 0: ero["up"] += 1
            elif dE < 0: ero["down"] += 1
            else: ero["flat"] += 1
        row_prev = row_k1

    print(f"\n=== {label} (events) ===")
    print(f"(d) EROSION steps: up={ero['up']} down={ero['down']} flat={ero['flat']}")
    print(f"    (2,4)-EVENT steps: up={ev['up']} down={ev['down']} flat={ev['flat']}"
          f"  total events={ev['total']}")
    # negative dE at events = excess consumed by regeneration
    ev_down_amt = sum(abs(Es[k+1]-Es[k]) for k,_,dE in [] )  # placeholder
    ev_dE_vals = [dE for _, _, dE in event_rows]
    print(f"    dE at events: min={min(ev_dE_vals) if ev_dE_vals else None} "
          f"max={max(ev_dE_vals) if ev_dE_vals else None}")
    print(f"    sum dE at events = {sum(ev_dE_vals)}")
    # (e) excess budget
    total_E = sum(Es)
    print(f"(e) total E over all rows = {total_E}, total events = {ev['total']}")
    print(f"    (excess 'budget' reading: E(row k) is the store that a regeneration")
    print(f"     must draw on; total E across rows vs total events)"
    print(f"    time {time.time()-t0:.1f}s")


if __name__ == "__main__":
    # oracle check
    depth = 5
    primes = primes_up_to(60)
    gen = rows_generator(primes, depth)
    got = [next(gen) for _ in range(depth + 1)]
    ok = all(got[k][:12] == EXPECTED[k] for k in range(1, depth + 1))
    print("ORACLE: all five worked rows match =", ok)
    for k in range(1, depth):
        E, l = excess_info(got[k])
        bl = block_profile(got[k + 1])
        print(f"  row{k}: E={E} lnz_ex={l} block_profile(row{k+1})={bl} match={l==bl}")

    Es, bprof, lnz, nrows, _ = analyze(primes_up_to(20_000_000), 1000, "SIEVE 2e7 depth 1000")
    analyze_events(primes_up_to(20_000_000), 1000, "SIEVE 2e7 depth 1000", Es, bprof, nrows)
    sys.stdout.flush()
    Es2, bprof2, lnz2, nrows2, _ = analyze(primes_up_to(300_000_000), 240, "SIEVE 3e8 depth 240")
    analyze_events(primes_up_to(300_000_000), 240, "SIEVE 3e8 depth 240", Es2, bprof2, nrows2)
