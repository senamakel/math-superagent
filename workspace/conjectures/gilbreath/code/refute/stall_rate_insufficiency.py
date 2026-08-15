#!/usr/bin/env python3
"""
Refute R-stall-rate-insufficiency (recharge-balance-ladder, stance: open).

Statement:
  For ANY absolute-difference array with b_1 = 2, if (2,4)-events occur with
  bounded row gap  tau_{i+1} - tau_i <= G  for some fixed G, then
  A_k(0) = 1 for all k  (leading 1 persists forever).

The rung's OWN text predicts this is false (it "is the rung expected to bite on
zero-jump-stalls"; the arithmetic: an all-stall array with event-gap >= 2 gives
sum (j_i+1) ~ k/G < k-2, forcing b_k -> 0).  We make that concrete: find a
2-then-odds sequence (general class, gaps from a small even set) whose triangle
DIES (A_k(1) not in {0,2} for some k) even though every (2,4)-event is a STALL
(j=0) and the row-gap between events is bounded by a fixed small G.

Method: small brute force over gap words (refutation = find ONE dying array with
bounded event gap; this is a counterexample search, not the full-size method).
For each sequence, build rows exactly (integer |a-b|), track b_k (leading {0,2}
block length), and the (2,4)-event stream (edge A_k(b_k)=2, intruder A_k(b_k+1)=4,
giving b_{k+1} >= b_k; jump j = b_{k+1}-b_k).  If the triangle dies (A_k(1) not in
{0,2}) with all event row-gaps <= G and all stalls, report it.
"""
import itertools

def diff(row):
    return [abs(row[i]-row[i+1]) for i in range(len(row)-1)]

def block_len(row):
    L = 0
    for x in row[1:]:
        if x in (0,2): L += 1
        else: break
    return L

def run(seq, depth, G):
    """Return (survived, event_list) where event_list has (row_index, jump, gap_since_prev).
    b_1 = block_len of row 1."""
    cur = [int(x) for x in seq]
    b_prev = None
    events = []
    prev_event_row = None
    for k in range(1, depth+1):
        if k >= 2:
            # transition from row k-1 to row k was already computed; recompute b
            pass
        # compute b_k of current row
        bk = block_len(cur)
        if k == 1:
            b_first = bk
        # check second entry in {0,2}
        if k >= 1 and cur[1] not in (0,2):
            return (False, events, cur[:6], b_first, k)
        # next row
        nxt = diff(cur)
        # event at row k? (edge, intruder) -> growth
        if bk >= 1 and len(cur) > bk+1:
            edge = cur[bk]
            intr = cur[bk+1]
            if (edge, intr) == (2,4):
                b_next = block_len(nxt)
                j = b_next - bk
                gap = (k - prev_event_row) if prev_event_row is not None else None
                events.append((k, j, gap))
                prev_event_row = k
        cur = nxt
    return (True, events, None, b_first, depth)

def main():
    G = 2   # bounded row gap we seek to satisfy
    depth = 60
    # gap words over {2,4,6} (gaps after first; first gap = 2 so A_1=(1,even,...))
    # sequence: 2,3, 3+g1, 3+g1+g2, ...
    found = None
    for L in range(2, 9):
        for gaps in itertools.product([2,4,6], repeat=L):
            seq = [2,3]
            for g in gaps:
                seq.append(seq[-1]+g)
            surv, events, head, b_first, where = run(seq, depth, G)
            if not surv:
                # died. check event gap bound and all stalls
                gaps_list = [e[2] for e in events if e[2] is not None]
                all_stall = all(e[1]==0 for e in events)
                maxgap = max(gaps_list) if gaps_list else 0
                if all_stall and maxgap <= G:
                    found = (seq, events, head, b_first, where)
                    print("FOUND dying array with all-stall, event-gap <= %d:" % G)
                    print("  seq =", seq)
                    print("  b_1 =", b_first)
                    print("  died at row k=%d, head row = %s" % (where, head))
                    print("  events (row, jump, gap_since_prev) =", events)
                    print()
                    print("VERDICT: R-stall-rate-insufficiency REFUTED (bounded event")
                    print("gap <= %d with all jumps 0 still yields death)." % G)
                    raise SystemExit(0)
        # report progress
        print("length %d: %d sequences, none all-stall-bounded-gap dying yet" %
              (L, (3**L)))
    print("No all-stall bounded-gap dying array found up to these lengths/set. "
          "Try larger alphabet or include small jump.")

if __name__ == "__main__":
    main()
