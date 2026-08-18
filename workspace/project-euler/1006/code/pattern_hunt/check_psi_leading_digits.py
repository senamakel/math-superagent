"""Pattern check: leading digits of exact Psi(k).

Conjecture under test:
    floor( Psi(k) / 10^(2k-2) ) == c1(k) = 1 + floor(k/phi^2)  (A189663)
for all k >= 1.  I.e. the most significant digit-block of Psi(k) equals the
number of length-k factors starting with '1'.

Also tested (trivially implied by the exact recurrence, kept as a sanity check
of the integer pipeline): Psi(k) == c1(k) (mod 10^len(c1)) -- trailing digits.

Method: iterate the exact k-step recurrence
    Psi(k+1) = 100 Psi(k) + 100 V(R_k)^2 + 20 S1(k) + J(k),  J(k) = c1(k+1),
from Psi(1) = 1, using the recorded exact values V(R_k) (vR_exact.txt) and
S1(k) (s1_exact.txt) for k = 1..3000.  All integers exact; c1(k) computed with
mpmath at 80 digits (exact here: k/phi^2 is irrational, 80 digits >> needed).

Falsification: the first k with floor(Psi(k)/10^(2k-2)) != c1(k).
"""
import mpmath as mp

mp.mp.dps = 80
PHI2_INV = mp.mpf(1) / ((1 + mp.sqrt(5)) / 2) ** 2

def c1(k):
    return 1 + int(mp.floor(k * PHI2_INV))

def load_pairs(path, limit=None):
    out = {}
    with open(path) as fh:
        for line in fh:
            parts = line.split()
            if len(parts) < 2:
                continue
            kk = int(parts[0])
            out[kk] = int(parts[1])
            if limit is not None and kk >= limit:
                break
    return out

def main():
    vR = load_pairs("code/out/vR_exact.txt")
    s1 = load_pairs("code/out/s1_exact.txt")

    # --- validate the pipeline: reproduce recorded exact Psi(1..25) ---
    exact = load_pairs("code/out/psi_exact.txt")
    Psi = {1: 1}
    ok = True
    for k in range(1, 25):
        Psi[k + 1] = (100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1))
    for k in range(1, 26):
        if Psi[k] != exact[k]:
            print(f"PIPELINE MISMATCH at k={k}: computed={Psi[k]} recorded={exact[k]}")
            ok = False
    print("pipeline reproduces recorded exact Psi(1..25):", ok)
    if not ok:
        return

    # --- extend to k=3000 via the exact recurrence ---
    for k in range(25, 3000):
        Psi[k + 1] = 100 * Psi[k] + 100 * vR[k] ** 2 + 20 * s1[k] + c1(k + 1)

    # --- conjectures ---
    bad_lead = []
    bad_trail = []
    for k in range(1, 3001):
        lead = Psi[k] // 10 ** (2 * k - 2)
        c = c1(k)
        if lead != c:
            bad_lead.append((k, lead, c))
        # trailing-digit sanity: Psi(k) mod 10^len(c1(k)) == c1(k)
        mod = 10 ** len(str(c))
        if Psi[k] % mod != c:
            bad_trail.append((k, Psi[k] % mod, c))

    print("leading-digit conjecture floor(Psi/10^(2k-2)) = c1(k):")
    if bad_lead:
        print(f"  FAILS at {len(bad_lead)} of 3000 k; first 10: {bad_lead[:10]}")
    else:
        print("  HOLDS for every k = 1..3000 (exact integers)")
    print("trailing-digit sanity Psi == c1 mod 10^len(c1):",
          "HOLDS for k=1..3000" if not bad_trail else f"FAILS: {bad_trail[:10]}")

    # report a sample of the leading blocks
    print("\nsample  k  c1(k)  lead  digits(Psi) ->")
    for k in [1, 3, 8, 13, 21, 24, 25, 34, 55, 89, 144, 233, 377, 610, 987,
              1597, 2584, 3000]:
        print(f"  {k:5d} {c1(k):5d} {Psi[k] // 10 ** (2 * k - 2):5d} "
              f"{len(str(Psi[k]))} digits")

if __name__ == "__main__":
    main()