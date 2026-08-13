#!/usr/bin/env python3
"""Check how far the mod-2^t linearization of the absolute-difference operator
lifts. Odlyzko's mod-4 linearization says: for even a,b, |a-b| == a+b (mod 4).
The candidate in research/approaches/mod4-pascal-invariant.md claims this
lifts to mod 2^t for all t (to track the halved value). Test for t=1..8 over
all even residues mod 2^t and report the first t where the linearization fails.
"""
import itertools

for t in range(1, 9):
    m = 1 << t
    residues = [r for r in range(m) if r % 2 == 0]  # even residues mod m
    violations = []
    for A in residues:
        for B in residues:
            linsum = (A + B) % m
            absdiff = abs(A - B) % m
            if linsum != absdiff:
                violations.append((A, B, absdiff, linsum))
                break
        if violations:
            break
    if violations:
        print(f"t={t} mod {m}: LIFT FAILS, first violation {violations[0]}")
    else:
        print(f"t={t} mod {m}: linearization OK over all even residues")
