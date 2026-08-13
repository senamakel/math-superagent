#!/usr/bin/env python3
"""Extract exact structural sequences from the genuine regime (k=1..161)
of the prime block-length record code/out/blocks_depth1000.json.

Quantities:
  b_k          : leading {0,2} block length of row k
  events       : k with b_{k+1} >= b_k  ((2,4)-events, jump j = b_{k+1}-b_k >= 0)
  erosion runs : maximal stretches of k with b_{k+1} = b_k - 1
  cycle floor  : minimum b over the erosion era ending at each event
  floor record : running record-low of cycle floors

Checks:
  A. cycle floors are strictly increasing (monotone minima)
  B. event gaps: max, and whether any gap exceeds (max erosion run + 1)
  C. jump j vs preceding floor, Spearman/Pearson
  D. erosion-run lengths vs following jump magnitude
"""
import json


def main():
    b = json.load(open("code/out/blocks_depth1000.json"))["b"]
    # genuine regime: rows 1..161 (0-based index 0..160). Beyond row 161 the
    # block fills the finite width and the record is an artifact.
    bg = b[:161]  # bg[0] = b_1
    n = len(bg)
    events = []
    erosion = []
    j = 0
    for k in range(n - 1):
        d = bg[k + 1] - bg[k]
        if d >= 0:
            events.append((k + 1, d, bg[k]))  # 1-based event row, jump, b before
        elif d == -1:
            if erosion and erosion[-1][1] == j - 1:
                erosion[-1] = (erosion[-1][0], j)
            else:
                erosion.append((k + 1, j))  # start row, length so far
            j += 1
    # erosion runs: contiguous stretches with d == -1
    runs = []
    i = 0
    while i < n - 1:
        if bg[i + 1] == bg[i] - 1:
            start = i + 1
            end = start
            while end < n - 1 and bg[end + 1] == bg[end] - 1:
                end += 1
            runs.append((start, end - start + 1))
            i = end
        else:
            i += 1
    print("== events (1-based row, jump, b_k) ==")
    print(events)
    print("num events:", len(events))
    gaps = [events[i + 1][0] - events[i][0] for i in range(len(events) - 1)]
    print("event gaps:", gaps)
    print("max event gap:", max(gaps))
    print("== erosion runs (start row, length) ==")
    print(runs)
    print("erosion run lengths:", [r[1] for r in runs])
    print("max erosion run:", max(r[1] for r in runs))
    # A. cycle floors: min b between successive events (the era ending at event e_i)
    floors = []
    prev = 0  # row index of previous event (0-based row of b value)
    for e in events:
        r = e[0]  # 1-based event row; era rows are prev_event_row+1 .. r
        lo = min(bg[prev:r])  # bg[prev] included: b at previous event row
        floors.append(lo)
        prev = r
    # also include floor after last event through row 161
    floors.append(min(bg[prev:n]))
    print("cycle floors:", floors)
    strict = all(floors[i + 1] > floors[i] for i in range(len(floors) - 1))
    print("A. cycle floors strictly increasing:", strict)
    # record minima of the era floors
    rec = []
    for f in floors:
        if not rec or f > rec[-1]:
            rec.append(f)
    print("floor record:", rec)
    # B. max gap vs max erosion run
    print("B. max gap =", max(gaps), " max erosion run =", max(r[1] for r in runs),
          " (gap_limit = maxrun+1 holds:", max(gaps) <= max(r[1] for r in runs) + 1, ")")
    # C. jump vs floor of era it ends
    jumps = [e[1] for e in events]
    print("jumps:", jumps)
    import math
    # Pearson r between log1p(jump) and floor
    fs = floors[:len(events)]
    xs = [math.log1p(j) for j in jumps]
    xs = [math.log1p(max(j, 1)) for j in jumps]
    ys = [float(f) for f in fs]
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
    print("C. Pearson r(log1p(jump), floor):", num / den if den else float("nan"))
    # D. erosion-run length immediately preceding event e_i vs jump j_i
    #    run ending at row r-1 (erosion rows immediately before event row r)
    pairs = []
    for idx, e in enumerate(events):
        r = e[0]
        # find erosion run ending at r-1
        run_len = 0
        # walk back from r-1 while b decreases by 1
        k = r - 1
        while k >= 1 and bg[k] == bg[k - 1] - 1:  # 0-based careful
            run_len += 1
            k -= 1
        pairs.append((run_len, e[1]))
    print("D. (erosion run before event, jump):", pairs)


if __name__ == "__main__":
    main()