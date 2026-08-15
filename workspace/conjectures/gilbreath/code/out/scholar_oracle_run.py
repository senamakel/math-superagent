#!/usr/bin/env python3
import sys
sys.path.insert(0, "/workspace/code")
from lib.gilbreath import primes_up_to, rows_generator

EXPECTED = {
    1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4],
    2: [1, 0, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2],
    3: [1, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
    4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0],
    5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
}
p = primes_up_to(60)
rows = list(rows_generator(p, 5))
ok = True
for k in range(1, 6):
    m = rows[k][:12] == EXPECTED[k]
    ok = ok and m
    print(f"A_{k} first12={rows[k][:12]} match={m}")
print("SCHOLAR_ORACLE_CHECK:", ok)
# also verify the parity/block shape to depth 100
p2 = primes_up_to(400000)
g = rows_generator(p2, 100)
next(g)
ok_shape = True
for k in range(1, 101):
    r = next(g)
    if r[0] != 1 or r[1] not in (0, 2):
        ok_shape = False
        print("shape fail at", k)
print("SCHOLAR_SHAPE_DEPTH100:", ok_shape)
