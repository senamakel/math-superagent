#!/usr/bin/env python3
"""Verify the identity A_k(i) = |Δ_k(i)| on the Gilbreath triangle of the primes.

Δ_k(i) = Σ_{j=0}^k (-1)^{k-j} C(k,j) A_0(i+j)   (standard k-th forward difference,
signed, alternating signs as stated).

The identity can only hold while the signed difference triangle D (D_k(i) =
D_{k-1}(i) - D_{k-1}(i+1), D_0 = A_0) has no adjacent pair of opposite signs at
the levels involved: |u - v| = ||u| - |v|| holds iff u·v >= 0, so each absolute
value taken in the Gilbreath row build erases exactly the sign information the
forward-difference convention keeps. First failure anywhere, and first failure
of the k=1..6 position-1 series, are the outputs.

Exact integer arithmetic throughout. The A-rows must reproduce the worked
example in problem.md before anything is trusted.
"""

import json


def primes_up_to(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def binom_row(k):
    row = [1]
    for j in range(1, k + 1):
        row.append(row[-1] * (k - j + 1) // j)
    return row


def main():
    DEPTH = 20          # rows A_0..A_DEPTH
    WIDTH = DEPTH + 20  # enough columns that no row is truncated at the right

    A0 = primes_up_to(400000)[:WIDTH]
    # sanity: A0 must start 2,3,5,7,11,13,...
    assert A0[:7] == [2, 3, 5, 7, 11, 13, 17], A0[:7]

    # ---- Gilbreath rows (iterated absolute differences) ----
    A = [A0]
    for _ in range(DEPTH):
        A.append([abs(A[-1][i] - A[-1][i + 1]) for i in range(len(A[-1]) - 1)])

    # ---- oracle check: rows 1..5 must match problem.md / witnesses.json ----
    EXPECTED = {
        1: [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4],
        2: [1, 0, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2],
        3: [1, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0],
        4: [1, 2, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0],
        5: [1, 2, 0, 0, 0, 2, 0, 0, 0, 2, 0, 2],
    }
    oracle_ok = all(A[k][:12] == EXPECTED[k] for k in range(1, 6))
    print("oracle: rows A_1..A_5 reproduce problem.md:", oracle_ok)

    # ---- signed forward-difference triangle D ----
    # D_k(i) = sum_j (-1)^{k-j} C(k,j) A_0(i+j); satisfies D_{k+1}(i) = D_k(i) - D_k(i+1)
    D = [A0]
    for _ in range(DEPTH):
        D.append([D[-1][i] - D[-1][i + 1] for i in range(len(D[-1]) - 1)])
    # check D_k against the closed form at a few points
    for k in range(DEPTH + 1):
        bc = binom_row(k)
        for i in range(0, 6):
            direct = sum(
                ((-1) ** (k - j)) * bc[j] * A0[i + j] for j in range(k + 1)
            )
            assert D[k][i] == direct, (k, i, D[k][i], direct)
    print("signed triangle D matches closed form Σ (-1)^{k-j} C(k,j) A_0(i+j): True")

    # ---- the identity, position 1, k = 1..6 ----
    print("\nposition 1: |Δ_k(1)| vs A_k(1)")
    for k in range(1, 7):
        print(f"  k={k}: Δ_k(1) = {D[k][1]:>4}   |Δ_k(1)| = {abs(D[k][1]):>3}"
              f"   A_k(1) = {A[k][1]:>3}   match={abs(D[k][1]) == A[k][1]}")

    # ---- first failure anywhere ----
    first_any = None
    for k in range(1, DEPTH + 1):
        for i in range(len(A[k])):
            if abs(D[k][i]) != A[k][i]:
                first_any = (k, i, D[k][i], A[k][i])
                break
        if first_any:
            break
    print(f"\nfirst failure anywhere: k={first_any[0]}, i={first_any[1]}:"
          f" Δ_k(i) = {first_any[2]}, A_k(i) = {first_any[3]}")

    # first failure at position 1
    first_pos1 = None
    for k in range(1, DEPTH + 1):
        if abs(D[k][1]) != A[k][1]:
            first_pos1 = (k, D[k][1], A[k][1])
            break
    print(f"first failure at position 1: k={first_pos1[0]}: Δ_k(1) = {first_pos1[1]},"
          f" A_k(1) = {first_pos1[2]}")

    # ---- mechanism: opposite-sign adjacent pairs in the signed triangle ----
    print("\nmechanism: |u - v| = ||u| - |v|| holds iff u*v >= 0.")
    print("first adjacent opposite-sign pair of D_{k-1} feeding a D_k:")
    found = None
    for k in range(1, DEPTH + 1):      # D_k uses pair (D_{k-1}(i), D_{k-1}(i+1))
        for i in range(len(D[k - 1]) - 1):
            if D[k - 1][i] * D[k - 1][i + 1] < 0:
                found = (k, i, D[k - 1][i], D[k - 1][i + 1], D[k][i])
                break
        if found:
            break
    print(f"  k={found[0]} (row D_{found[0]}): adjacent pair i={found[1]},i+1="
          f"{found[1]+1} = ({found[2]}, {found[3]}), product < 0; "
          f"D_k(i) = {found[4]}")

    # local neighbourhood of the position-1 failure
    print("\nneighbourhood of the position-1 failure (k=4):")
    print("  signed row D_3, positions 1..5 :", D[3][1:6])
    print("  abs-value row A_3, positions 1..5:", A[3][1:6])
    print("  D_4(1) = D_3(1) - D_3(2) =", D[3][1] - D[3][2],
          ";  A_4(1) = |A_3(1) - A_3(2)| =", abs(A[3][1] - A[3][2]))
    print("  signed D_2, positions 1..5    :", D[2][1:6])

    # ---- how far would the failure propagate if no abs-correction existed ----
    print("\nwhere the identity still holds at position 1 for k = 1..DEPTH:")
    fails_pos1 = [k for k in range(1, DEPTH + 1) if abs(D[k][1]) != A[k][1]]
    print("  failing k:", fails_pos1[:12], "...", "count:", len(fails_pos1))

    # summary line for the ledger
    print("\nSUMMARY: first k where A_k(1) != |Δ_k(1)| is", first_pos1[0])
    print(f"  Δ_{first_pos1[0]}(1) = {first_pos1[1]}, A_{first_pos1[0]}(1) = {first_pos1[2]}")


if __name__ == "__main__":
    main()