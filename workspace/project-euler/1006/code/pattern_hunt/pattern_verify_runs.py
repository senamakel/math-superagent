"""Verify the two load-bearing pattern-hunt regularities independently:

(1) The right-extension recurrence for Psi(k):
        Psi(k+1) = 100*Psi(k) + 100*V(R_k)^2 + 20*S1(k) + J(k)
    against the recorded exact Psi values (psi_exact.txt, k=1..25) and the
    recorded V(R_k), J, S1(k) (ext_recurrence.txt, k=1..40).

(2) The structure of V(R_k) (exact value of the right-special length-k
    factor, read as a decimal): constant on runs whose starts I conjecture
    are the odd-indexed Fibonacci numbers 1,2,5,13,34,89,...  Test this
    hypothesis on V(R_k) exact computed by brute force over a long word.
"""
import sys

def fib_word(min_len):
    a, b = '0', '01'
    while len(b) < min_len:
        a, b = b, b + a
    return b

def right_special_value(factors, k):
    """Among length-k distinct factors, find the unique one with both '0' and
    '1' as right extensions in the word, and return its decimal value."""
    # need the word to determine extensions; recompute here
    return None

def compute_Rk_and_recurrence(kmax=200):
    """Compute, for k=1..kmax, R_k (decimal value), whether it is exactly
    right-special, S1(k), J(k), and check the recurrence vs brute Psi."""
    word = fib_word(4 * kmax + 8)
    L = len(word)
    factors = {}
    ext = {}
    for i in range(L - kmax + 1):
        w = word[i:i + kmax]
        factors.setdefault(w, set())
        if i + kmax < L:
            nxt = word[i + kmax]
            # only meaningful while window fully in word; last window's ext unknown
    # Build right extension counts per factor properly:
    exts = {}
    for i in range(L - kmax):
        w = word[i:i + kmax]
        exts.setdefault(w, set()).add(word[i + kmax])
    factors = set(word[i:i + kmax] for i in range(L - kmax + 1))
    Rs = [w for w in factors if len(exts.get(w, set())) == 2]
    return Rs, factors, exts

def main():
    # ---- Part 1: verify recurrence over recorded data ----
    psi = {}
    with open("code/out/psi_exact.txt") as fh:
        for line in fh:
            k, v = line.split()
            psi[int(k)] = int(v)
    # ext_recurrence.txt columns: k V(R_k) J P1(k+1) S1(k)
    VR, J, S1 = {}, {}, {}
    with open("code/out/ext_recurrence.txt") as fh:
        for line in fh:
            parts = line.split()
            k = int(parts[0])
            VR[k] = int(parts[1])
            J[k] = int(parts[2])
            S1[k] = int(parts[4])
    print("== Part 1: right-extension recurrence, k=1..24 (needs Psi(k+1) exact) ==")
    bad = 0
    for k in range(1, 25):
        lhs = psi.get(k + 1)
        if lhs is None:
            continue
        rhs = 100 * psi[k] + 100 * VR[k] ** 2 + 20 * S1[k] + J[k]
        ok = (lhs == rhs)
        if not ok:
            bad += 1
            print(f"  k={k}: Psi({k+1})={lhs}  rhs={rhs}  MISMATCH")
    print(f"  k=1..24 recurrence holds exactly: {bad == 0}  (bad={bad})")

    # ---- Part 2: structure of V(R_k) exact, computed brute ----
    print("\n== Part 2: V(R_k) runs, odd-Fibonacci-start hypothesis, kmax brute ==")
    import math
    kmax = 150
    word = fib_word(4 * kmax + 8)
    L = len(word)
    RG, exts = {}, {}
    for k in range(1, kmax + 1):
        exts.clear()
        for i in range(L - k):
            w = word[i:i + k]
            exts.setdefault(w, set()).add(word[i + k])
        factors = set(word[i:i + k] for i in range(L - k + 1))
        Rs = [w for w in factors if len(exts.get(w, set())) == 2]
        assert len(Rs) == 1, f"k={k}: expected exactly 1 right-special, got {len(Rs)}"
        RG[k] = int(Rs[0])  # decimal value of the right-special factor (leading 0 ok as int)
    # runs of consecutive equal values
    starts = []
    prev = None
    cur_start = 1
    for k in range(1, kmax + 1):
        if RG[k] != prev:
            if prev is not None:
                starts.append((cur_start, k - 1, prev))
            cur_start = k
            prev = RG[k]
    starts.append((cur_start, kmax, prev))
    print(f"  runs of constant V(R_k), k=1..{kmax}: {len(starts)} runs")
    starts_list = [s for s, e, v in starts]
    print(f"  run start k values: {starts_list}")
    # Fibonacci numbers F_n: F_1=1,F_2=1,F_3=2,F_4=3,F_5=5,F_6=8,F_7=13,...
    fibs = [1, 1]
    while fibs[-1] < kmax:
        fibs.append(fibs[-1] + fibs[-2])
    # odd-indexed Fibonacci F_n (n odd, n>=3), plus F_2=1
    odd_fibs = set([1, 2])  # F_2=1, F_3=2
    for n in range(4, len(fibs) + 1, 2):  # odd n: 3,5,7,...
        if n <= len(fibs) - 1 and fibs[n - 1] <= kmax:
            odd_fibs.add(fibs[n - 1])
    runs_set = set(starts_list)
    only_in = runs_set - odd_fibs
    missing = odd_fibs - runs_set - {kmax + 1}
    print(f"  hypothesized odd-Fibonacci starts (F_2=1,F_3=2,F_5=5,F_7=13,...) <= {kmax}: {sorted(odd_fibs)}")
    print(f"  run-starts not in that set: {sorted(only_in)}")
    print(f"  odd-Fibs not run-starts (<=kmax): {sorted(missing)}")

if __name__ == "__main__":
    main()
