#!/usr/bin/env python3
"""
TASK: counting model with CORRECT (aggregated) skip semantics on (A,B),
where A = total # of 1-bits, B = total # of 0-bits over the whole board.

Semantics (single surrogate state (A,B); this is the *counting approximation*
of the real multiset game - it ignores the fact that deleting a leading 1 can
also drop trailing 0-bits, e.g. "100" -> 0):

  One to move:
    if A==0: Zero has already won (One cannot move) -> cost 0.
    else: One consumes one 1-bit -> (A-1,B), Zero's turn.
  Zero to move:
    - delete a 0-bit -> (A,B-1) [requires B>=1], One's turn; or
    - skip -> (A,B), One's turn, costing 1 skip (always allowed, even B==0).

O(A,B) = minimal skips Zero needs from (A,B) One-to-move (unlimited budget).
Z(A,B) = minimal skips Zero needs from (A,B) Zero-to-move (unlimited budget).

Recurrences (exact integers; well-founded in A because a One-move lowers A,
and Z uses O on the same A via the skip who merely passes the turn):

  O(0,B) = 0
  O(A,B) = Z(A-1,B)                     for A>=1   (One has no choice: one move)
  Z(0,0) = 1                            (no 0-bit to delete; must skip once)
  Z(0,B) = 0                            for B>=1   (delete 0-bits straight to win)
  Z(A,B) = min( Z(A-1,B-1) if B>=1 else +inf,  1 + Z(A-1,B) )   for A>=1

This is well-founded: every term on the right has strictly smaller A.
"""
import sys

def build(N):
    # Z as dict (A,B) -> value; O derived.  N = max A (and max B).
    Z = {}
    # A = 0 row
    Z[(0, 0)] = 1
    for B in range(1, N + 1):
        Z[(0, B)] = 0
    for A in range(1, N + 1):
        for B in range(0, N + 1):
            opts = []
            if B >= 1:
                opts.append(Z[(A - 1, B - 1)])
            opts.append(1 + Z[(A - 1, B)])
            Z[(A, B)] = min(opts)
    return Z

def O(A, B, Z):
    if A == 0:
        return 0
    return Z[(A - 1, B)]

def main():
    N = 2000
    Z = build(N)

    lines = []
    lines.append("O(A,B) table, A,B in 0..24 (O = minimal skips Zero needs, One-to-move):")
    header = "A\\B " + " ".join(f"{b:4d}" for b in range(0, 25))
    lines.append(header)
    for A in range(0, 25):
        row = f"{A:3d} " + " ".join(f"{O(A, B, Z):4d}" for B in range(0, 25))
        lines.append(row)
    lines.append("")

    # S_counting(n) = O(A(n), B(n)); A(n)=sum_k k*popcount(k), B(n)=sum_k k*zerocount(k)
    lines.append("S_counting(n) = O(A(n),B(n)) for n=1..30:")
    lines.append("  n    A(n)    B(n)  S_counting   real-oracle(if known)")
    real = {1: 1, 2: 2, 3: 8, 4: 9, 5: 17}
    matched = []
    mismatched = []
    Aacc = Bacc = 0
    for n in range(1, 31):
        # add contribution of k = n
        Aacc += n * bin(n).count("1")
        Bacc += n * (len(bin(n)) - 2 - bin(n).count("1"))
        sc = O(Aacc, Bacc, Z)
        tag = ""
        if n in real:
            tag = f"  real={real[n]}  {'MATCH' if sc == real[n] else 'MISMATCH'}"
            (matched if sc == real[n] else mismatched).append(n)
        lines.append(f"{n:3d}  {Aacc:6d}  {Bacc:6d}  {sc:10d}{tag}")

    lines.append("")
    lines.append(f"Real-game matched at n = {matched}")
    lines.append(f"Real-game mismatched at n = {mismatched}")

    out = "\n".join(lines)
    print(out)
    with open("code/out/counting_proper.txt", "w") as f:
        f.write(out + "\n")
    print("\n(wrote code/out/counting_proper.txt)")

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    main()
