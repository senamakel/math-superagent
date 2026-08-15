#!/usr/bin/env python3
from hminus_exact_check import hminus_exact, KNOWN

all_ok = True
for p in sorted(KNOWN):
    r, i, g = hminus_exact(p)
    ok = (i == 0) and (r == KNOWN[p])
    all_ok = all_ok and ok
    print(f"p={p:3d} root={g}  hmin(claim)={KNOWN[p]:>5}  exact_real={r}  imag={i}  match={ok}")
print("ALL_MATCH:", all_ok)
