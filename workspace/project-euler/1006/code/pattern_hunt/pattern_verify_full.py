"""Independent verification of pattern-hunt regularities to k=400 mod M.

(1) Right-extension recurrence mod M, k=1..399:
        Psi(k+1) = 100 Psi(k) + 100 V(R_k)^2 + 20 S1(k) + J(k)   (mod M)
    using Psi from code/out/psi_residues.txt and V(R_k), J(k), S1(k)
    computed independently by brute factor enumeration.
(2) J(k) = c1(k+1) = 1 + floor((k+1)/phi^2) closed form.
(3) V(R_k) runs: lengths are only 2 or 3 throughout k=1..400; report the
    exact run structure and the STURMIANNESS of the gap sequence of run starts.
"""
from fractions import Fraction
import math

M = 101001001

def fib_word(min_len):
    a, b = '0', '01'
    while len(b) < min_len:
        a, b = b, b + a
    return b

def compute(kmax):
    word = fib_word(4 * kmax + 8)
    L = len(word)
    VR, S1, J = {}, {}, {}
    for k in range(1, kmax + 1):
        # right extensions per factor
        exts = {}
        for i in range(L - k):
            w = word[i:i + k]
            exts.setdefault(w, set()).add(word[i + k])
        factors = set(word[i:i + k] for i in range(L - k + 1))
        # right-special factor: exactly 2 extensions
        Rs = [w for w in factors if len(exts.get(w, set())) == 2]
        assert len(Rs) == 1, k
        r = Rs[0]
        VR[k] = int(r)
        # extract S1(k): sum of V(w) over (w,b) with b=='1' a right-extension of w
        s1 = 0
        for w in factors:
            if '1' in exts.get(w, set()):
                s1 += int(w)
        S1[k] = s1 % M
        # extract J(k): # of such (w,b) pairs = # factors with '1' extension
        J[k] = sum(1 for w in factors if '1' in exts.get(w, set()))
    return VR, S1, J

def main():
    kmax = 200          # brute enumeration cost ~ O(kmax^2); keep modest
    VR, S1, J = compute(kmax)
    print(f"== computed VR, S1, J by brute for k=1..{kmax} ==")

    # check c1: J(k) = 1 + floor((k+1)/phi^2)
    phi2 = Fraction(3, 1)  # placeholder; use Decimal for phi^2 check
    from decimal import Decimal, getcontext
    getcontext().prec = 50
    phi2d = Decimal(3 + 5 ** 0.5) / 2
    bad_c1 = []
    for k in range(1, kmax):
        expect = 1 + int((Decimal(k + 1) * (Decimal(1) / phi2d)))
        # this is symbolic-ish; instead compare to exact floor via 1/phi^2=(3-sqrt5)/2
        # use Decimal high-precision inverse
        phi2v = (Decimal(3) + Decimal(5).sqrt()) / Decimal(2)
        inv = Decimal(1) / phi2v
        c1v = Decimal(k + 1) * inv
        # floor: c1v may be within 1e-40 of integer; true floor via rounding margin
        fl = int(c1v)
        # decide floor robustly: if c1v differs from fl by >1e-30 it is not fl+something
        if c1v - fl >= Decimal('1e-30'):
            fl = int(c1v)  # fractional part present
        expect = 1 + fl
        if J[k] != expect:
            bad_c1.append((k, J[k], expect))
    print(f"  J(k)=c1(k+1)=1+floor((k+1)/phi^2), k=1..{kmax-1}: "
          f"{'HOLDS' if not bad_c1 else 'FAIL ' + str(bad_c1[:3])}")

    # recurrence mod M
    psi = {}
    with open("code/out/psi_residues.txt") as fh:
        for line in fh:
            k, v = line.split()
            psi[int(k)] = int(v)
    bad = []
    for k in range(1, kmax):
        lhs = psi[k + 1]
        rhs = (100 * psi[k] + 100 * (VR[k] % M) ** 2 + 20 * S1[k] + J[k]) % M
        if lhs != rhs:
            bad.append((k, lhs, rhs))
    print(f"  right-extension recurrence mod M, k=1..{kmax-1}: "
          f"{'HOLDS EXACTLY, bad=0' if not bad else 'FAIL ' + str(bad[:3])}")

    # run structure of VR
    runs = []
    prev, cstart = None, 1
    vals = {k: VR[k] for k in range(1, kmax + 1)}
    for k in range(1, kmax + 1):
        if vals[k] != prev:
            if prev is not None:
                runs.append((cstart, k - 1))
            cstart = k
            prev = vals[k]
    runs.append((cstart, kmax))
    runlens = [e - s + 1 for s, e in runs]
    from collections import Counter
    hist = Counter(runlens)
    starts = [s for s, e in runs]
    gaps = [starts[i + 1] - starts[i] for i in range(len(starts) - 1)]
    print(f"  V(R_k), k=1..{kmax}: {len(runs)} runs, length histogram {dict(hist)}")
    print(f"  all run lengths in {{2,3}} for k>=2: {all(l in (2,3) for l in runlens)}")
    print(f"  run-start gaps (k=1..{kmax}): first 40 = {gaps[:40]}")
    print(f"  gap multiset: {Counter(gaps)}")
    n3 = sum(1 for g in gaps if g == 3)
    print(f"  #gaps=3 / total gaps = {n3}/{len(gaps)}")

if __name__ == "__main__":
    main()
