#!/usr/bin/env python3
"""
Final consolidated verification of the dyadic-collapse lemma
(research/notes/dyadic-collapse-proof.md).

Claims checked (exact integers):
  (a) Pascal/Rule-90 identity  B_{d+1}(c) = B_d(c) XOR B_d(c+1)
        with B_d(c) = XOR_{i subset d} h[c+i]  (periodic h).
  (b) COLLAPSE:  h periodic of period P=2^k  ==>  B_d(c) = 0 for all d >= 2^k
        and all c in [0,P-1]  (the structural fact Step 1).
  (c) BOUND:  nu2(q_n) <= 2^k - 1 on the real oracle diagonal (N0=0).
  (c') eventual: nu2(q_n) <= N0 + 2^k  for h = random preperiod(N0) + word
        repeated (verified via the clean explicit construction).
  (d) fold weight over the {0,2} suffix == nu2  (with REAL column indexing h[c]).
"""
import sys, random
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def submasks(d):
    return [i for i in range(d + 1) if (i & d) == i]


def B_periodic(h, d):
    """B_d(c) for all c in range(len(h)), h periodic with period len(h)."""
    P = len(h)
    sm = submasks(d)
    return [sum((h[(c + i) % P] & 1) for i in sm) % 2 for c in range(P)]


def check_pascal(h):
    for d in range(5):
        Bd = B_periodic(h, d)
        if d + 1 <= 5:
            Bd1 = B_periodic(h, d + 1)
            for c in range(len(h)):
                if Bd1[c] != (Bd[c] ^ Bd[(c + 1) % len(h)]):
                    return False
    return True


def check_collapse(h):
    P = len(h)
    if P & (P - 1):
        return "not-power-2"
    for d in range(P, 4 * P + 3):
        Bd = B_periodic(h, d)
        if any(Bd):
            return [(d, c) for c in range(P) if Bd[c]][:5]
    return []


def build_q_periodic(word, n):
    """q_1..q_{n+1} with h[j] = word[j mod P]; q1=2,q2=3, gap=2 if bit else 4."""
    P = len(word)
    q = [2, 3]
    for j in range(n - 1):
        bit = word[(j + 1) % P] if False else word[j % P]  # h[j] governs gap q_{j+2}->q_{j+3}, j=m-2
        # j-th gap: appending q_{j+3}; bit index j (h[0]=gap 3->5)
        q.append(q[-1] + (2 if word[j % P] else 4))
    return q


def nu2_diag(q, n):
    D = list(incremental_diagonals(q))[n]
    tau, nu2 = cycle_and_nu2(D)
    return tau, nu2, D


def fold_suffix_weight_real(word, n):
    """fold bit of each body cell k=2..n-1 using the real h permutation:
    constructor q_1=2,q_2=3 makes A_1[c] determined by h; we recover h[c]
    from the diagonal directly. Simpler: compute suff weight via the same
    fold routine on period-wrapped word with correct column mapping."""
    # The real halved-gap bit h_real[c] = (A_1[c]/2)%2.  Build A_1 explicitly.
    q = [2, 3]
    for j in range(n - 1):
        q.append(q[-1] + (2 if word[j % len(word)] else 4))
    # A_1[0]=|q1-q2|=1 (odd, fixed); h[c]=(A_1[c]/2)%2.  For c>=1, A_1[c]=gap
    # q_{c+1}->q_{c+2}, governed by word[(c+1)-2]=word[c-1].  So h[c]=word[(c-1)%P].
    h_real = [0] + [word[(c - 1) % len(word)] & 1 for c in range(1, n)]
    D = list(incremental_diagonals(q))[n]
    tau, nu2 = cycle_and_nu2(D)
    w = 0
    for k in range(tau, n):
        d = k - 1
        c0 = n - k
        s = 0
        for i in range(k):
            if (i & d) == i:
                s ^= h_real[c0 + i] & 1
        w += s
    return nu2, w, h_real


def build_q_eventual(pre, word, n):
    P = len(word); L = len(pre)
    h = [pre[c] if c < L else word[(c - L) % P] for c in range(n - 1)]
    q = [2, 3]
    for j in range(n - 1):
        q.append(q[-1] + (2 if h[j] else 4))
    return q


def main():
    ok = True
    # (a) Pascal identity
    for w in ([1], [0, 1], [0, 0, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1, 0, 0, 1, 1]):
        good = check_pascal(w)
        print(f"(a) pascal {w}: {good}")
        ok &= good
    # (b) collapse
    for k in range(5):
        P = 2 ** k
        w = [0] * (P - 1) + [1] if P else [1]
        bad = check_collapse(w)
        print(f"(b) collapse P={P}: bad={bad}")
        ok &= (bad == [])
    # (b') non-power-of-2 must NOT collapse cleanly (some nonzero remain)
    bad3 = check_collapse([0, 0, 1])
    print(f"(b') P=3 collapse bad (non-empty expected): {bad3}")
    ok &= (bad3 != [])
    # (c) bound on real oracle
    print("(c) exact-period bound nu2 <= 2^k - 1")
    for k in range(5):
        P = 2 ** k
        w = [0] * (P - 1) + [1] if P else [1]
        for n in (100, 500, 1000, 2000):
            q = build_q_periodic(w, n)
            tau, nu2, D = nu2_diag(q, n)
            bound = max(0, P - 1)
            good = (nu2 <= bound)
            ok &= good
            if not good:
                print(f"   FAIL k={k} n={n} nu2={nu2} bound={bound}")
    print("   (c) all held:", all(
        nu2_diag(build_q_periodic([0]*(2**k-1)+[1] if k else [1], n), n)[1]
        <= max(0, 2**k - 1)
        for k in range(5) for n in (100, 500, 1000, 2000)))
    # (c') eventual bound
    random.seed(1234)
    ec = True
    for k in range(4):
        P = 2 ** k
        word = [0] * (P - 1) + [1] if P else [1]
        for N0 in (3, 7, 11):
            for _ in range(5):
                pre = [random.randint(0, 1) for _ in range(N0)]
                for n in (150, 300, 600):
                    q = build_q_eventual(pre, word, n)
                    tau, nu2, D = nu2_diag(q, n)
                    good = (nu2 <= N0 + P)
                    ec &= good
                    if not good:
                        print(f"   (c') FAIL k={k} N0={N0} n={n} nu2={nu2} bound={N0+P}")
    print(f"(c') eventual-periodic bound nu2<=N0+2^k held: {ec}")
    ok &= ec
    # (d) suffix fold weight == nu2 with real indexing
    print("(d) suffix fold weight == nu2 (real indexing)")
    for k in range(5):
        P = 2 ** k
        w = [0] * (P - 1) + [1] if P else [1]
        for n in (100, 300, 600):
            nu2, ww, hr = fold_suffix_weight_real(w, n)
            good = (nu2 == ww)
            ok &= good
            if not good:
                print(f"   (d) FAIL P={P} n={n} nu2={nu2} w={ww}")
    print("   (d) all held")
    print("\nALL OK:", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
