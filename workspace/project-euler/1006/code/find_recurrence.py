"""Find a constant-coefficient linear recurrence for Psi(k), k=1..150.

Loads exact Psi(1..150) from out/psi_data_1_150.txt, runs Berlekamp–Massey
over several primes to get the minimal LFSR order, reconstructs rational
coefficients, and verifies the recurrence reproduces all 150 exact terms.
"""
import os

from lib.recurrences import (
    berlekamp_massey,
    verify_recurrence,
    rational_reconstruct,
)

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "..")
OUT_DIR = os.path.normpath(OUT_DIR)
DATA = os.path.join(OUT_DIR, "out", "psi_data_1_150.txt")

PRIMES = [1000003, 1000000007, 998244353]


def load_psi(path):
    psi = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            try:
                k = int(line.split(":")[0].strip())
            except ValueError:
                continue
            parts = line.split(":")
            if len(parts) < 4:
                continue
            val = parts[-1].strip()
            try:
                psi[k] = int(val)
            except ValueError:
                continue
    return psi


def main():
    psi = load_psi(DATA)
    ks = sorted(psi)
    print("Loaded Psi(k) for k =", ks[0], "..", ks[-1], "count =", len(ks))
    assert ks == list(range(1, 151)), "expected exactly k=1..150"
    seq = [psi[k] for k in ks]

    # --- Berlekamp–Massey over several primes ---
    orders = {}
    for p in PRIMES:
        red = [x % p for x in seq]
        L, C = berlekamp_massey(red, p)
        orders[p] = L
        ok, bad = verify_recurrence(red, C, p=p)
        print(f"prime {p}: order = {L}, self-check reproduces {len(seq)-L} terms: {ok and bad is None}")
    print("orders across primes:", orders)

    # If all primes agree, take the smallest-common / a representative
    L_common = None
    if len(set(orders.values())) == 1:
        L_common = list(orders.values())[0]
        print("All primes agree on order:", L_common)
    else:
        L_common = min(orders.values())
        print("Primes disagree; using min order:", L_common)

    # Reconstruct rational coefficients over the largest prime (most headroom for
    # rational reconstruction), with the true sequence to check exactness.
    p = PRIMES[1]  # 1e9+7, largest
    red = [x % p for x in seq]
    L, C = berlekamp_massey(red, p)
    coeffs = [rational_reconstruct(c, p) for c in C]
    print()
    print(f"order d = {L}")
    print("reconstructed (num, den) coefficients c_0..c_{d-1}:")
    for i, cr in enumerate(coeffs):
        print(f"  c_{i} = {cr}")

    # Build exact rational coefficients as fractions; verify recurrence on exact ints
    from fractions import Fraction
    C_frac = [Fraction(n, d) if d else None for (n, d) in coeffs]
    if any(c is None for c in C_frac):
        print("Some coefficient did not reconstruct: cannot verify exactly.")
        return

    # Verify exact: seq[k] == sum c_j * seq[k-1-j], using Fraction arithmetic
    ok = True
    first_bad = None
    for k in range(L, len(seq)):
        total = Fraction(0)
        for j in range(L):
            total += C_frac[j] * seq[k - 1 - j]
        if total != seq[k]:
            ok = False
            first_bad = k
            break
    print()
    print(f"Exact verification over all {len(seq)-L} terms (k={L+1}..{len(seq)}):")
    print("  reproduced EXACTLY:", ok, " first_bad =", first_bad)

    return L, C_frac, ok


if __name__ == "__main__":
    main()
