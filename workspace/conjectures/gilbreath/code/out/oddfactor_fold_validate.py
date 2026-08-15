#!/usr/bin/env python3
"""Validate the F2 fold density against the GROUND-TRUTH right-diagonal nu2,
for a few words of odd-factor period.  Ensures the 'density = (sigma^d h)_0'
formula really matches nu2(q_n)/n on the true dynamics before trusting the
min-over-words falsifier."""
from lib.rightdiag import cycle_and_nu2


def build_seq_from_bits(word, reps):
    """2-then-odds sequence: q1=2, q2=3; then gaps: gap=2 if bit else 4."""
    bits = word * reps
    q = [2, 3]
    for b in bits:
        q.append(q[-1] + (2 if b else 4))
    return q


def true_nu2(word, n):
    """nu2(q_n) from the ground-truth diagonal recurrence (maximal {0,2} suffix)."""
    reps = (n + 2) // len(word) + 2
    q = build_seq_from_bits(word, reps)
    # incremental diagonals up to n
    D = [q[0]]
    for i in range(1, n + 1):
        newD = [0] * (i + 1)
        newD[0] = q[i]
        for k in range(1, i + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
    # D = delta(q_n) has entries 0..n; terminal D[n].  nu2 from cycle_and_nu2 on D
    # but cycle scans body = D[:-1] (0..n-1); for a 2-then-odds the {0,2} tail
    # lives in body indices >=1; match the run's convention.
    return cycle_and_nu2(D)[1]


def main():
    print("Validate fold-density vs true nu2(n)/n on concrete odd-factor words.")
    print("=" * 74)
    n = 2000
    for word in [[0,0,1], [1,0,1], [0,1,1], [0,0,0,1], [1,1,0]]:
        P = len(word)
        # fold density via the sigma iteration (matches code/out falsifier)
        v = word[:]
        cnt = 0
        for d in range(1, n + 1):
            v = [v[c] ^ v[(c + 1) % P] for c in range(P)]
            cnt += v[0]
        fold_density = cnt / n
        tn = true_nu2(word, n)
        print(f"  word {word} (P={P}): fold-density={fold_density:.6f}  "
              f"true nu2({n})/n={tn/n:.6f}  true nu2={tn}")


if __name__ == "__main__":
    main()
