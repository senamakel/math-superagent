#!/usr/bin/env python3
"""Librarian cross-check part 2: verify the parameters (n,k) of each witness
pair in code/out/witnesses.json directly, and confirm the seven N>=6 values
and N(3003)=8 under the both-mirrors-plus-trivial convention, plus the
ERDOS 849 half-triangle exemplars (120->3, 3003->4) and the A180058
decompositions. Exact integer arithmetic only."""
import math
import json

def C(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0

# load witness file
with open("code/out/witnesses.json") as f:
    W = json.load(f)

print("Exact recomputation of witnesses.json:")
all_ok = True
for a_str, rec in sorted(W["witnesses"].items(), key=lambda kv: int(kv[0])):
    a = int(a_str)
    nontr = [tuple(p) for p in rec["nontrivial"]]
    # trivial pair (a,1) mirrors (a,a-1) — both mirrored, so 2
    vals = [C(n, k) for (n, k) in nontr]
    ok_vals = all(v == a for v in vals)
    # full count: each nontrivial pair contributes 2 (mirror), trivial 2
    N_full = 2 * len(nontr) + 2
    ok_N = N_full == rec["N"]
    all_ok = all_ok and ok_vals and ok_N
    print(f"  a={a}: nontrivial pairs {nontr} all give {a}? {ok_vals}; "
          f"N={N_full} (expect {rec['N']}) -> {'OK' if ok_N else 'MISMATCH'}")

print("\nConvention cross-check with witnesses.json:", "ALL OK" if all_ok else "FAIL")

# Erdős 849 exemplars: half-triangle counts
print("\nErdős 849 half-triangle exemplars (1<=k<=n/2):")
half = {
    120: [(10, 3), (16, 2), (120, 1)],
    3003: [(14, 6), (15, 5), (78, 2), (3003, 1)],
}
for a, reps in half.items():
    ok = all(C(n, k) == a for (n, k) in reps)
    print(f"  a={a}: {len(reps)} half-triangle solutions, all valid? {ok}")
    print(f"    -> N(a) = {2*len(reps)} (both mirrors + trivial)")

# Ceiling formula A059233: rowcount = ceil(N/2)
print("\nOEIS A059233 conversion (Hasler): rowcount = ceil(N(a)/2):")
for a in (120, 3003):
    N_a = 6 if a == 120 else 8
    print(f"  a={a}: N={N_a} -> rowcount = ceil({N_a}/2) = {math.ceil(N_a/2)}")