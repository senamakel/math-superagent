"""Small exact oracle for the current G4 thesis attack.
complexity_class: exponential; oracle_bound: k <= 10.

Reproduces the two official examples, then computes exact factor values for
small k and tests the two candidate bounded summaries already refuted by this
workspace (appending-digit closure collision; single-intercept replacement).
"""
from collections import defaultdict
from lib.fibword import fib_prefix


def factors(k):
    w = fib_prefix(200)
    return sorted({w[i:i+k] for i in range(len(w)-k+1)})


def value(s):
    return int(s, 10)


def oracle(k):
    fs = factors(k)
    return fs, sum(value(s)**2 for s in fs)


def summary(s, k):
    vals = [value(s[i:i+k]) for i in range(len(s)-k+1)]
    return len(vals), sum(vals), sum(v*v for v in vals)


def collision():
    for k in range(1, 4):
        for n in range(k, 8):
            buckets = defaultdict(list)
            for mask in range(1 << n):
                s = ''.join(str((mask >> i) & 1) for i in range(n))
                buckets[summary(s, k)].append(s)
            for state, words in buckets.items():
                for a in words:
                    for b in words:
                        if a != b and summary(a + '0', k) != summary(b + '0', k):
                            return k, state, a, b, summary(a+'0', k), summary(b+'0', k)
    return None


def main():
    fs3, p3 = oracle(3)
    _, p10 = oracle(10)
    print('F3=', fs3)
    print('Psi(3)=', p3)
    print('Psi(10) mod M=', p10 % 101001001)
    print('summary collision=', collision())


if __name__ == '__main__':
    main()
