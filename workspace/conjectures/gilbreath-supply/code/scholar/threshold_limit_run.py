#!/usr/bin/env python3
"""Third-pass limit question (GOAL.md): does the minimum weight ratio w/n at
which linear supply becomes 'typical' tend to 0, or plateau near 1/8?

PART A (main, EXACT, no sampling): the MEAN half of 'typical' is computable
exactly over the whole weight-w layer with zero sampling.  By symmetry, for a
fixed depth d the fold cell T(n,d) is the XOR of the k = 2^popcount(d)
positions in row M_d, and over all weight-w strings the probability the XOR is
odd is

    P_d(w) = ( C(n,w) - c_w ) / ( 2 C(n,w) ),
    c_w = [z^w] (1-z)^k (1+z)^{n-k}.

(Proof: count weight-w strings with an odd number of ones in M_d as
sum_{r odd} C(k,r) C(n-k,w-r); the alternating total is c_w, so the odd count
is (C(n,w)-c_w)/2.)

mean_n(w) = (1/n) * sum_{d=2}^{n-1} P_d(w).

== STRUCTURAL REDUCTION ==  P_d(w) depends on d only through k=2^popcount(d),
so group depths by popcount: with N_p = #{d in [2,n-1]: popcount(d)=p} and
k_p = 2^p,  c_{w,p} = [z^w](1-z)^{k_p}(1+z)^{n-k_p}:

    mean_n(w) = (1/n)(1/(2*C(n,w))) * sum_p N_p ( C(n,w) - c_{w,p} ).

This is O(log n) coefficient computations per w instead of O(n), exact, no
sampling.  The comparison mean >= 2/5 is done in pure integers:
    mean >= 2/5  <=>  5 * sum_p N_p (C - c_{w,p}) >= 4 * n * C.

PART B (sampled, fraction half): 'typical' also needs fraction of weight-w
strings with nu2/n >= 0.40 to be >= 0.5.  At n = 256, 512 we sample >= 2000
random weight-w strings per (n, w/n) and estimate mean and fraction, computing
nu2 via lib.supply_fold.s_sos.
"""
from math import comb
from random import sample

# ---------------------------------------------------------------------------
# exact helpers (integer arithmetic, no floating point in the decision)
# ---------------------------------------------------------------------------


def factorial_table(n):
    f = [1] * (n + 1)
    for i in range(1, n + 1):
        f[i] = f[i - 1] * i
    return f


def make_comb(fact):
    def C(a, b):
        if b < 0 or b > a:
            return 0
        return fact[a] // (fact[b] * fact[a - b])
    return C


def popcount_distribution(n):
    """N_p = #{d in [2, n-1] : popcount(d) = p}."""
    from collections import Counter
    c = Counter()
    for d in range(2, n):
        c[bin(d).count("1")] += 1
    return c


def coeff_cw(C, k, n, w):
    """[z^w] (1-z)^k (1+z)^(n-k) = sum_j (-1)^j C(k,j) C(n-k,w-j).  Exact int."""
    c = 0
    lo = max(0, w - (n - k))
    hi = min(k, w)
    for j in range(lo, hi + 1):
        term = C(k, j) * C(n - k, w - j)
        c += -term if (j & 1) else term
    return c


class ExactMean:
    """Exact mean of nu2/n over all weight-w strings for one n, integer core.

    mean >= 2/5  <=>  5*sum_p N_p (C-c_wp) >= 4*n*C.
    """

    def __init__(self, n):
        self.n = n
        self.fact = factorial_table(n)
        self.C = make_comb(self.fact)
        self.Np = popcount_distribution(n)
        self.classes = [(pc, 1 << pc, cnt) for pc, cnt in sorted(self.Np.items())]

    def _sumCNw(self, w):
        """C(n,w)."""
        return self.C(self.n, w)

    def sum_Np_C_minus_cw(self, w):
        """S = sum_p N_p (C(n,w) - c_{w,p}); numerator of 2nC * mean."""
        C = self.C(self.n, w)
        S = 0
        for pc, kp, cnt in self.classes:
            cw = coeff_cw(self.C, kp, self.n, w)
            S += cnt * (C - cw)
        return S  # integer

    def mean_ge_025(self, w):
        """mean_n(w) >= 1/4  <=>  S >= (1/2) n C  <=>  2S >= n C."""
        C = self.C(self.n, w)
        S = self.sum_Np_C_minus_cw(w)
        return 2 * S >= self.n * C

    def mean_ge_040(self, w):
        """mean_n(w) >= 2/5  <=>  S/(2nC) >= 2/5  <=>  5S >= 4 n C."""
        C = self.C(self.n, w)
        S = self.sum_Np_C_minus_cw(w)
        return 5 * S >= 4 * self.n * C

    def mean_as_float(self, w):
        """Exact rational mean, returned as float for display only."""
        from fractions import Fraction
        C = self.nC = self.C(self.n, w)
        S = self.sum_Np_C_minus_cw(w)
        return Fraction(S, 2 * self.n * C)


def first_w_mean_ge(em, thr_want):
    """Smallest w in [1, n-1] with mean_n(w) >= threshold (0.25 or 0.40)."""
    n = em.n
    for w in range(1, n):
        if thr_want == 0.40 and em.mean_ge_040(w):
            return w
        if thr_want == 0.25 and em.mean_ge_025(w):
            return w
    return None


# ---------------------------------------------------------------------------
# brute validation of the grouped integer formula (small n, exhaustive)
# ---------------------------------------------------------------------------
def brute_mean_exact(n, w):
    from fractions import Fraction
    from lib.supply_fold import s_sos
    from itertools import combinations
    tot = 0
    cnt = 0
    for ones in combinations(range(n), w):
        h = [0] * n
        for j in ones:
            h[j] = 1
        _, c1 = s_sos(n, h)
        tot += c1
        cnt += 1
    return Fraction(tot, cnt) / n


def cross_check():
    print("Cross-check grouped-integer mean vs exhaustive s_sos (small n):")
    ok = True
    for n, w in [(6, 1), (6, 2), (8, 1), (8, 3), (10, 2), (12, 3), (12, 5), (14, 4)]:
        em = ExactMean(n)
        from fractions import Fraction
        mine = em.mean_as_float(w)
        brute = brute_mean_exact(n, w)
        same = (mine == brute)
        ok = ok and same
        # also verify the integer-ge threshold is consistent with the Fraction
        g040 = em.mean_ge_040(w)
        f040 = brute >= Fraction(2, 5)
        same_t = (g040 == f040)
        ok = ok and same_t
        print(f"  n={n} w={w}: formula={float(mine):.4f} brute={float(brute):.4f} "
              f"match={same} ge040={g040}(={f040})")
    return ok


# ---------------------------------------------------------------------------
# PART B: sampled fraction half
# ---------------------------------------------------------------------------
def sample_fraction(n, w, trials=2000, seed=12345):
    """Sample `trials` random weight-w strings of length n, compute nu2/n via
    lib.supply_fold.s_sos, return (mean_nu2_over_n, fraction_with_nu2n_ge_040)."""
    import random
    from lib.supply_fold import s_sos
    rng = random.Random(seed)
    tot = 0
    frac = 0
    for _ in range(trials):
        ones = rng.sample(range(n), w)
        h = [0] * n
        for j in ones:
            h[j] = 1
        _, c1 = s_sos(n, h)
        v = c1 / n
        tot += v
        if v >= 0.40:
            frac += 1
    return tot / trials, frac / trials


def main():
    print("=" * 78)
    print("sequence = weight-w binary strings over F2^n (all weights, exact mean)")
    print("oracle   = Krawtchouk closed form (grouped by popcount) cf lib.supply_fold.s_sos")
    print("range    = n in {8,10,12,14,16,32,64,128,256,512,1024,2048,4096}")
    print("=" * 78)

    all_ok = cross_check()
    print(f"  cross-check {'PASS' if all_ok else 'FAIL'}")

    ns = [8, 10, 12, 14, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

    print("\n" + "=" * 78)
    print("PART A (exact mean half): min w/n with mean_n(w) >= 0.40  [theta(w/n)]")
    print("=" * 78)
    print(f"{'n':>6} {'first w':>8} {'theta=w/n':>10} {'first w (0.25)':>14} {'w/n@0.25':>9}")
    theta_rows = []
    for n in ns:
        em = ExactMean(n)
        w40 = first_w_mean_ge(em, 0.40)
        w25 = first_w_mean_ge(em, 0.25)
        t40 = f"{w40 / n:.4f}" if w40 is not None else "-"
        t25 = f"{w25 / n:.4f}" if w25 is not None else "-"
        print(f"{n:>6} {str(w40):>8} {t40:>10} {str(w25):>14} {t25:>9}")
        theta_rows.append((n, w40, w40 / n if w40 else None))

    print("\n" + "=" * 78)
    print("PART A (exact): mean_n(w) at fixed alpha = w/n")
    print("=" * 78)
    alphas = [0.05, 0.075, 0.10, 0.125, 0.15]
    print(f"{'n':>6} " + " ".join(f"a={a:<6}" for a in alphas))
    for n in ns:
        em = ExactMean(n)
        row = []
        for a in alphas:
            w = int(round(a * n))
            w = max(1, min(w, n - 1))
            row.append(f"{float(em.mean_as_float(w)):.4f}")
        print(f"{n:>6} " + " ".join(f"{x:>9}" for x in row))
        # also allow a memory-friendly recompute for parity with PART A column above

    print("\n" + "=" * 78)
    print("PART B (sampled fraction half): n=256,512, w/n ratios, sample>=2000")
    print("oracle = lib.supply_fold.s_sos ; reporting mean nu2/n and frac(nu2/n>=0.40)")
    print("=" * 78)
    ratios_b = [0.03, 0.05, 0.075, 0.10, 0.125, 0.15]
    trials_b = 2000
    print(f"{'n':>6} {'ratio':>6} {'w':>4} {'mean':>7} {'frac>=0.40':>10}")
    for n in [256, 512]:
        for r in ratios_b:
            w = int(round(r * n))
            w = max(1, min(w, n - 1))
            m, f = sample_fraction(n, w, trials=trials_b)
            print(f"{n:>6} {r:>6.3f} {w:>4} {m:>7.4f} {f:>10.4f}")

    # summary of the supported behaviour
    print("\n" + "=" * 78)
    print("SUMMARY of theta(w/n) column (exact mean half):")
    print("=" * 78)
    for n, w, t in theta_rows:
        print(f"  n={n:>6}  theta = {t:.4f}" if t is not None else f"  n={n:>6}  theta = (none)")
    print("\nThis is exact-mean / numerical evidence over the sampled n-list, NOT a")
    print("proof of the limit.  It shows the per-n trend only.")
    print("cross-check overall:", "PASS" if all_ok else "FAIL")


if __name__ == "__main__":
    main()
