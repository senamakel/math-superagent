"""TASK B - eventual periodicity of r(k) = Psi(k) mod M over the oracle range.

Loads the exact Psi(k) for k=1..150 from code/out/psi_data_1_150.txt (verified
against the brute oracle), reduces mod M=101001001, and searches for an
eventual period: a preperiod p0 and period T such that r(k+T)=r(k) for all
k >= p0 in the available range.

The structural motivation: value(w) mod M of a length-k factor depends on
(k-1-i) mod ord_10(M) for each 1-bit at string position i, and the set of
factors is Fibonacci/rotation periodic. If r(k) is eventually periodic with a
period that fits within our 150-point range, we can reduce 10^18 into the
periodic range and report r(10^18) exactly.

We search all candidate periods up to a bound that fits in the data (<= 75,
so at least a full period is observed) and report the smallest (preperiod,
period) that holds, plus how far the pattern extends.

All exact integer arithmetic.
"""

import os
import re

MOD = 101001001


def load_psi(path):
    """Return list psi[k] with index 0 unused; psi[k] = Psi(k) exact int."""
    psi = [0]
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            m = re.match(r"(\d+)\s*:\s*True\s*:\s*n=\s*\d+,\|S\|=\s*\d+\s*:\s*(\d+)", line)
            if m:
                k = int(m.group(1))
                val = int(m.group(2))
                if k == len(psi):
                    psi.append(val)
                else:
                    raise ValueError(f"non-sequential k={k} at list len {len(psi)}")
    return psi


def find_eventual_period(arr, kstart, kmax, maxperiod):
    """Find the smallest (preperiod, period) with r(k+T)=r(k) for all
    preperiod <= k < kmax-T. arr is 1-indexed; search k in [kstart, kmax]."""
    results = []
    for T in range(1, maxperiod + 1):
        # try every preperiod starting point
        for p0 in range(kstart, kmax - T + 2):
            ok = True
            k = p0
            while k + T <= kmax:
                if arr[k] != arr[k + T]:
                    ok = False
                    break
                k += 1
            if ok:
                results.append((p0, T))
                break  # smallest preperiod for this T
    return results


def main():
    base = os.path.join(os.path.dirname(__file__), "..", "out", "psi_data_1_150.txt")
    psi = load_psi(base)
    kmax = len(psi) - 1
    print(f"loaded Psi(k) for k=1..{kmax}")

    # sanity: the two given checkpoints
    assert psi[3] == 20302, psi[3]
    assert psi[10] % MOD == 10699667, psi[10] % MOD
    print(f"sanity: Psi(3)={psi[3]} ; Psi(10) mod M = {psi[10] % MOD} (expected 10699667)")

    r = [0] + [psi[k] % MOD for k in range(1, kmax + 1)]
    print(f"r(3) = Psi(3) mod M = {r[3]}")
    print(f"r(10) = {r[10]}")

    out = []
    out.append(f"r(k)=Psi(k) mod M for k=1..{kmax}:")
    for k in range(1, kmax + 1, 10):
        out.append("  k=" + ",".join(f"{kk}:{r[kk]}" for kk in range(k, min(k+10, kmax+1))))
    out.append("")

    # search eventual periodicity
    maxperiod = kmax // 2  # at most this so a full period is visible
    print()
    print(f"searching eventual period with preperiod in [1,{kmax}], period in [1,{maxperiod}]")
    results = find_eventual_period(r, 1, kmax, maxperiod)
    # find the smallest period among all
    if results:
        smallest = min(results, key=lambda pr: pr[1])
        out.append(f"smallest (preperiod, period) found: {smallest}")
        print("candidate (preperiod, period):", smallest)
        # verify how far the pattern extends by checking period >= kmax
    else:
        out.append("NO constant period found in range (no T<=75 holds for all k up to 150)")
        print("NO period found.")

    text = "\n".join(out) + "\n"
    print(text)
    with open("code/out/mod_B.txt", "w") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
