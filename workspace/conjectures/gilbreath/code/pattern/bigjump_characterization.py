#!/usr/bin/env python3
"""Characterise the giant regeneration jumps (j > 1000) in the prime
Gilbreath triangle and decide, for each, whether it is genuine prime-renewal
dynamics or a finite-width (sieve) artifact.

Data: code/out/blocks_depth1000.json  (D = 1000 rows, sieve to 2e7,
      W = 1,270,607 primes; arrays b[k], s[k], intruder[k] are 0-based:
      they describe 1-based row k+1).
Events: the 13 (2,4)-events with j > 1000 from
      code/out/surplus_renewal_table.captured.txt, listed with i = 1-based
      row of the event (the row whose (edge, intruder) pair is (2, 4)).

Width bookkeeping (1-based rows: A_0 = the primes row with W columns,
A_r has W - r columns; the block of length b occupies 0-based columns 1..b,
so 1 + b <= columns, i.e. b <= (W - r) - 1):
  event i lands on row i+1, which has columns = W - (i+1) and
  max_block = columns - 1 = W - i - 2.
  CAPPED  <=>  b_{i+1} == max_block  <=>  the block's last column is the
  finite row's last column  <=>  the landing row has NO intruder
  (row_{i+1}[b+1] does not exist: JSON intruder[i] is null).
  For a capped jump the recorded j = b_{i+1} - b_i is a LOWER BOUND on the
  true infinite jump (the {0,2} run continues past the finite edge).
  floor_distance = max_block - b_{i+1}, so capped <=> floor_distance == 0.

Verification:
  - sanity 1: the 13 jumps recomputed from the b array match the table;
  - sanity 2: the step law (b_{k+1} >= b_k  <=>  (edge,intruder)==(2,4))
    over every transition with a non-null intruder, 60 events expected;
  - sanity 3: independent recomputation of rows A_0..A_165 from the primes
    (lib.gilbreath: primes_up_to(2e7), rows_generator, block_profile),
    confirming each event row's b, edge, intruder and each landing row's b.

Complexity: O(W * 166) time, O(W) space; W = 1,270,607.
"""
import os
import sys

from lib.gilbreath import primes_up_to, rows_generator, block_profile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # code/
JSON_PATH = os.path.join(ROOT, "out", "blocks_depth1000.json")
SIEVE_LIMIT = 20_000_000
W = 1_270_607          # number of primes at sieve 2e7 (recorded in the JSON)
LIVE_RECOMPUTE = 165   # recompute rows A_0..A_165 independently

# (i, j_expected): i = 1-based row of the (2,4) event (pre-transition row);
# from code/out/surplus_renewal_table.captured.txt.
GIANTS = [
    (34, 1314), (56, 1739), (64, 17326), (68, 8237), (94, 61088),
    (96, 11354), (110, 37746), (112, 129923), (126, 53470), (130, 190810),
    (134, 217657), (146, 360698), (161, 176181),
]
GIANT_IDS = {i for i, _ in GIANTS}
LANDING_IDS = {i + 1 for i, _ in GIANTS}


def main():
    with open(JSON_PATH) as f:
        data = json_load(f)
    assert data["sieve_limit"] == SIEVE_LIMIT, "sieve limit mismatch"
    assert data["num_primes"] == W, "prime count mismatch"
    b, s, intr = data["b"], data["s"], data["intruder"]
    D = data["D"]
    # arrays hold rows A_1..A_D (array index r-1 == row r), so length == D
    assert len(b) == D and len(s) == D and len(intr) == D, "array lengths"
    print(f"sieve limit = {data['sieve_limit']:,},  W = {W:,} primes,  "
          f"D = {D} rows (A_0..A_{D})")
    print(f"JSON: b[0] = b_1 = {b[0]:,},  max b = {data.get('max_block'):,},  "
          f"min b = {data.get('min_block'):,}")

    # ---- sanity 1: the 13 jumps recomputed from the b array ----------------
    print("\n== sanity 1: jumps recomputed from the b array vs renewal table ==")
    for i, j_exp in GIANTS:
        j_got = b[i] - b[i - 1]
        flag = "OK" if j_got == j_exp else "MISMATCH"
        assert j_got == j_exp, f"jump mismatch at i={i}"
        print(f"  i={i:3d}  table j={j_exp:7d}   recomputed j={j_got:7d}   {flag}")

    # ---- sanity 2: step law over every transition with an intruder ---------
    print("\n== sanity 2: step law from JSON over all transitions ==")
    fails = 0
    nevents = 0
    event_rows = []
    for k in range(1, len(b)):
        if intr[k - 1] is None:
            if b[k] != b[k - 1] - 1:      # no intruder => exact erosion
                fails += 1
        else:
            event = b[k] >= b[k - 1]
            pair = (s[k - 1] == 2 and intr[k - 1] == 4)
            if event != pair:
                fails += 1
            if event:
                nevents += 1
                event_rows.append(k)
    print(f"  events detected from the b array = {nevents} (expect 60)")
    print(f"  step-law / erosion violations = {fails} (expect 0)")
    assert nevents == 60 and fails == 0

    # ---- sanity 3: independent recompute of rows A_0..A_165 ----------------
    print(f"\n== sanity 3: independent recompute "
          f"(primes_up_to({SIEVE_LIMIT:,}), rows A_0..A_{LIVE_RECOMPUTE}) ==")
    primes = primes_up_to(SIEVE_LIMIT)
    print(f"  regenerated {len(primes):,} primes (expect {W:,})")
    assert len(primes) == W
    gen = rows_generator(primes, LIVE_RECOMPUTE)
    row0 = next(gen)
    assert len(row0) == W
    mism = 0
    for k in range(1, LIVE_RECOMPUTE + 1):
        row = next(gen)
        prof = block_profile(row)
        if prof != b[k - 1]:
            print(f"  b mismatch at row {k}: fresh {prof:,}, JSON {b[k-1]:,}")
            mism += 1
        if k in GIANT_IDS:
            e, c = row[b[k - 1]], row[b[k - 1] + 1]
            if not (e == s[k - 1] == 2 and c == intr[k - 1] == 4):
                print(f"  (edge,intruder) mismatch at event row {k}: "
                      f"fresh ({e},{c}), JSON ({s[k-1]},{intr[k-1]})")
                mism += 1
    print(f"  recompute mismatches = {mism} (expect 0); all 13 event rows and "
          f"13 landing rows covered")
    assert mism == 0

    # ---- the verdict table ---------------------------------------------------
    print("\n== giant jumps (j > 1000): cap test ==")
    print("rows are 1-based; event i sits on row i, lands on row i+1, which has")
    print(f"columns = W - (i+1) and max possible block max_block = columns - 1")
    print("= W - i - 2 (one column holds the leading 1).")
    print("CAPPED <=> b_{i+1} == max_block <=> floor_distance = 0: the {0,2}")
    print("run ends at the finite row's right edge (landing row has no")
    print("intruder; recorded j is a lower bound on the true jump).")
    print()
    print(f"{'i':>4} {'j':>8} {'b_i':>9} {'b_{i+1}':>9} {'edge':>4} {'intr':>4}"
          f" {'cols':>9} {'maxblk':>9} {'floor':>9}  verdict")
    capped_rows = []
    total_giant_j = 0
    genuine_giant_j = 0
    for i, _ in GIANTS:
        j = b[i] - b[i - 1]
        total_giant_j += j
        b_i = b[i - 1]
        b_land = b[i]
        edge, intruder_v = s[i - 1], intr[i - 1]
        cols = W - (i + 1)
        max_block = cols - 1
        floor_d = max_block - b_land
        if floor_d == 0 and intr[i] is None:
            verdict = "CAPPED-ARTIFACT"
            capped_rows.append(i)
            note = (f"  [landing row A_{i+1} fills finite width: intruder null; "
                    f"true j >= {j:,}]")
        else:
            verdict = "GENUINE"
            genuine_giant_j += j
            note = ""
        print(f"{i:>4} {j:>8,} {b_i:>9,} {b_land:>9,} {edge:>4} {intruder_v:>4}"
              f" {cols:>9,} {max_block:>9,} {floor_d:>9,}  {verdict}{note}")

    # prove the classification exhaustive: every event's landing row either
    # has an intruder (floor >= 1, genuine) or is the unique capped row 162.
    other_capped = [k for k in event_rows
                    if intr[k] is None and k not in capped_rows]
    assert other_capped == [], f"unexpected capped events: {other_capped}"
    assert len(capped_rows) <= 1 or True
    assert capped_rows == [161], f"capped set = {capped_rows}"

    # ---- summary ------------------------------------------------------------
    tail_ids = {i for i, _ in GIANTS if b[i] - b[i - 1] > 10_000}
    big3 = [(i, b[i] - b[i - 1]) for i, _ in GIANTS
            if i in (134, 146, 161)]
    big3.sort(key=lambda t: -t[1])
    print("\n== summary ==")
    print(f"giants with j > 1000: {len(GIANTS)}  "
          f"GENUINE = {len(GIANTS) - len(capped_rows)}  "
          f"CAPPED-ARTIFACT = {len(capped_rows)}  (capped rows: {capped_rows})")
    print(f"heavy tail j > 10^4: {len(tail_ids)} events  "
          f"genuine = {len(tail_ids - set(capped_rows))},  "
          f"capped = {len(tail_ids & set(capped_rows))}")
    print(f"largest three: " + ", ".join(f"i={i} j={j:,} ({'CAPPED' if i in capped_rows else 'GENUINE'})" for i, j in big3))
    print(f"sum of giant-jump j over the 13 = {total_giant_j:,}; "
          f"genuine part (12 events) = {genuine_giant_j:,} "
          f"({100.0 * genuine_giant_j / total_giant_j:.2f}%); "
          f"capped part = {total_giant_j - genuine_giant_j:,} "
          f"(recorded; true value >= that)")
    S_1000 = data.get("S_1000") or sum(j + 1 for k, j in zip(
        event_rows, [b[k] - b[k - 1] for k in event_rows]))
    print(f"(the 13 giants carry {100.0 * (total_giant_j + 13) / S_1000:.2f}% "
          f"of the full recharge surplus S_1000 = {S_1000:,})")


def json_load(f):
    import json
    return json.load(f)


if __name__ == "__main__":
    main()