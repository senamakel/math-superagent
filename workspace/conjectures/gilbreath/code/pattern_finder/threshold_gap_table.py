#!/usr/bin/env python3
"""Threshold-gap table for (2,4)-regeneration events, exact from
code/out/blocks_depth1000.json (depth 1000, sieve 20M, 1,270,607 primes).

Event at row k (1-based)  : b_{k+1} >= b_k, jump j = b_{k+1} - b_k.
Genuine regime            : k = 1..161 (beyond row 161 the block is glued to
                            the finite row width and jumps are lower bounds).

For each threshold J reports:
  rows (1-based) of events with jump > J,
  count, max gap between consecutive such rows (in rows),
  and whether the max gap is attained inside the genuine regime.
Also:
  - does each event land at a new all-time maximum of b?  (strictly greater)
  - record-max sequence values
  - boundary-bit regeneration restatement: event  <=>  e_bits==1 and c==4
  - s_k = s_{k-1} XOR t_{k-1} check (s=A_k(1)/2, t=A_k(2)/2)
"""
import json


def main():
    rec = json.load(open("code/out/blocks_depth1000.json"))
    b = rec["b"]  # b[k-1] = b_k, 1-based row k
    D = len(b)
    events = []  # (row k 1-based, jump, b_k)  for k = 1..D-1
    for k in range(1, D):
        d = b[k] - b[k - 1]
        if d >= 0:
            events.append((k, d, b[k - 1]))
    print(f"depth {D}, events total: {len(events)}")
    genuine = [(k, j, bk) for (k, j, bk) in events if k <= 161]
    print(f"genuine events (k<=161): {len(genuine)} (incl. j=0 stalls: "
          f"{sum(1 for _, j, _ in genuine if j == 0)})")
    print()
    prows = [k for (k, _, _) in events if k <= 161]
    maxgap = max(prows[i + 1] - prows[i] for i in range(len(prows) - 1))
    print(f"max gap between consecutive events (genuine): {maxgap} rows")
    print()
    print("== threshold table T(J): max gap between consecutive events with jump > J ==")
    thresholds = [100, 300, 1000, 3000, 10000, 30000, 100000, 200000]
    for J in thresholds:
        rows = [k for (k, j, _) in events if j > J and k <= 161]
        if len(rows) < 2:
            print(f"J={J:>7}: rows {rows}  count {len(rows)}  max-gap n/a")
            continue
        gaps = [rows[i + 1] - rows[i] for i in range(len(rows) - 1)]
        print(f"J={J:>7}: rows {rows}")
        print(f"          count {len(rows):2d}  gaps {gaps}  max-gap {max(gaps)}")
    print()
    print("== all 13 giants (jump > 1000), with cap flag ==")
    for (k, j, bk) in events:
        if j > 1000:
            cap = "" if k <= 161 else "  [width-capped: true jump >= this]"
            print(f"  row {k:3d}: jump {j:8d}  b_k={bk:8d}{cap}")
    print()
    print("== record maximum of b at each event (genuine) ==")
    recmax = 0
    recset = []       # events that set a strictly greater all-time max
    nongiant_fail = []
    giant_rows = [k for (k, j, _) in events if j > 1000]
    for (k, j, bk) in events:
        if k > 161:
            break
        land = bk + j
        if land > recmax:
            recmax = land
            recset.append(k)
        else:
            if k in giant_rows:
                print(f"  !!! giant row {k} did NOT set record (land {land} <= {recmax})")
            nongiant_fail.append((k, j, land, recmax))
    print(f"events setting a new all-time max: {len(recset)} of {len(genuine)}")
    print(f"events NOT setting a record: {[(k, j) for (k, j, land, r) in nongiant_fail]}")
    print(f"all {len(giant_rows)} giants set a new all-time max: "
          f"{all(k in recset for k in giant_rows)}")
    print()
    print("== boundary-bit restatement: event <=> e_bits==1 and c==4 (rows 1..161) ==")
    c = json.load(open("code/out/blocks_depth1000.json"))["intruder"]
    eb = [int(x) for x in open("code/out/pattern_finder_outputs/e_bits.txt").read().split()]
    misses = 0
    for k in range(1, 161):
        is_event = b[k] >= b[k - 1]
        pred = (k <= len(eb) and eb[k - 1] == 1 and c[k - 1] == 4)
        if is_event != pred:
            print(f"  MISMATCH row {k}: event={is_event} pred={pred}")
            misses += 1
    print(f"  mismatches: {misses}")
    print()
    print("== left-boundary halved law: s_{k+1} = s_k XOR t_k for k=1..160 ==")
    sb = [int(x) for x in open("code/out/pattern_finder_outputs/s_bits.txt").read().split()]
    tb = [int(x) for x in open("code/out/pattern_finder_outputs/t_bits.txt").read().split()]
    bad = [(k, sb[k], tb[k - 1] ^ sb[k - 1])
           for k in range(1, min(len(sb), len(tb) + 1))
           if sb[k] != (tb[k - 1] ^ sb[k - 1])]
    print(f"  mismatches over k=1..{min(len(sb), len(tb)) - 1}: {len(bad)}"
          + (f"  first: {bad[:3]}" if bad else ""))


if __name__ == "__main__":
    main()