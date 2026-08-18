"""Refutation check of the latest steering directive's Claims 1-3.

The directive (best read in config/directives.jsonl, but stated in CONTEXT.md
and the psi-to-ueuclid-reduction note) asserts, verified outside the container:

  Claim 1: For every k with F_n > k, the k+1 DISTINCT length-k factors are
           EXACTLY the k+1 CONTIGUOUS windows at positions
           r = F_n - k - 1 .. F_n - 1 of the doubled standard word q_n q_n.
           (As sets of words, equal, every time -> Psi(k) = sum over that
           contiguous window range of v_r^2, no dedup.)
  Claim 2: Psi(k) = (full cyclic sum over all F_n windows)
                    - (sum over the FIRST F_n - k - 1 windows).
  Claim 3: The full cyclic sum over all F_n windows = sum over j,jp of
           A(jp-j)*10^(2k-2-j-jp), A = cyclic autocorrelation of q_n, for
           ANY k < F_n (the Toeplitz/autocorrelation collapse holds for the
           CYCLIC sum at general k, even though it does not equal Psi).

Reference truth for these tests is code/mech/mech_psi.py, which is verified
in-container == brute string oracle k<=50, == recorded exact k<=25, ==
recorded residues k<=400 (mech_psi.captured.txt).  mech_psi computes Psi(k)
as the sum of squares of the k+1 distinct factors directly, with two
independent formulations (A and B) that agree in every case.

So: Claim 1/2 assert that Psi(k) computed from the window/cyclic-sum recipe
equals mech_psi(k).  Claim 3 asserts the autocorrelation collapse of the
cyclic sum.
"""
from fractions import Fraction
import sys, itertools
sys.path.insert(0, "/workspace/code")
from mech.mech_psi import mech_psi
from lib.fibword import fibs_upto, fib_prefix

M = 101001001


# ---- Fibonacci word digits and the standard word q_n ----
def fib_digits(L):
    """First L digits of the infinite Fibonacci word 0100101001001... as ints."""
    w = fib_prefix(L)
    return [1 if c == '1' else 0 for c in w]


# Standard word q_n: length F_n.  We build it by the same recurrence as the
# problem's S_n: S_0 = '0', S_1 = '01', S_n = S_{n-1}S_{n-2}.  |S_n| = F_{n+2}.
def fib_word_kth_prefix(n):
    a, b = '0', '01'
    for _ in range(n - 1):
        a, b = b, b + a
    return b  # this is S_{n+1} in 0-based -> length F_{n+3}

def standard_word_qn(n):
    """q_n: the standard word of length F_n (n-th Fibonacci).  We use the
    doubled word q_n q_n where q_n is the length-F_n period block equal to the
    Fibonacci word '0' and '01' concatenation.  For the claim we need the
    length-F_n block whose rotations are the F_n windows; any standard word
    with period F_n works, and the contiguous-window set only depends on the
    infinite word, so we build the first F_n + k digits of the infinite
    Fibonacci word and take windows of it."""
    return None  # we operate directly on the infinite word, below


INF_CACHE = {}
def inf_digit(i):
    """i-th digit (0-based) of the infinite Fibonacci word."""
    if i not in INF_CACHE:
        W = fib_prefix(10 * 10000 + 30)  # long enough for our tests
        INF_CACHE.clear()
        INF_CACHE.update({t: (1 if c == '1' else 0) for t, c in enumerate(W)})
    return INF_CACHE[i]


def window_value(pos, k):
    """Decimal value of the length-k window of the infinite Fibonacci word
    starting at position pos (leading zeros vanish)."""
    v = 0
    for j in range(k):
        v = v * 10 + inf_digit(pos + j)
    return v


# ---- cyclic autocorrelation A(d) of the standard word q_n ----
def cyclic_autocorr(qn, d, N, m):
    """A(d) = max(0,m-t) + max(0,m-(N-t)), t=(d*m) mod N.  qn = bit list length N,
    m = number of ones."""
    t = (d * m) % N
    return max(0, m - t) + max(0, m - (N - t))


def main():
    # q_n length: use F_n > k.  In fib index terms |S_fibidx| etc are messy;
    # we just pick the doubled window from the infinite word and use N = F_n
    # = smallest fib > k (so N bits of word span a full period of the standard
    # word truncated to length k).  For the autocorrelation formula we take
    # q_n as the first N bits and m = number of ones in it.
    all_ok = True

    for k in [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 20]:
        # mech_psi reference
        refA, refB, vA, vB = mech_psi(k)
        if refA != refB or vA != vB:
            print(f"k={k}: mech_psi internal inconsistency!"); all_ok = False
        ref = refA  # exact Psi(k)

        # N = smallest Fibonacci strictly > k  (this is F_n with F_n > k)
        fibs = fibs_upto(k)
        N = fibs[bisect_right(fibs, k)]

        # Claim 1: contiguous windows at r = N-k-1 .. N-1 of the inf word
        c1_vals = [window_value(r, k) for r in range(N - k - 1, N)]
        # distinct factors -> dedupe by word (not just value) to be safe
        seen = {}
        for r in range(N - k - 1, N):
            key = tuple(inf_digit(r + j) for j in range(k))
            seen[key] = window_value(r, k)
        c1_key_values = list(seen.values())
        c1_psi = sum(v * v for v in c1_key_values)

        # Claim 2: full cyclic sum over all N windows minus first N-k-1
        full_cyclic = sum(window_value(r, k) ** 2 for r in range(N))
        first_part = sum(window_value(r, k) ** 2 for r in range(N - k - 1))
        c2_psi = full_cyclic - first_part

        # Claim 3: cyclic autocorrelation collapse of the full cyclic sum
        # q_n = the N-bit standard block = first N digits of inf word
        qn = [inf_digit(i) for i in range(N)]
        m = sum(qn)
        # full cyclic sum = sum over all N windows of v_r^2.  Each window has
        # digits; v_r = sum_j dig_j(r) 10^(k-1-j).  Diagonal+off-diagonal in
        # the two-fold sum over j,jp: contribution dig_j(r)*dig_jp(r)*
        # 10^(2k-2-j-jp).  Sum over r=0..N-1 of dig_j(r)*dig_jp(r) =
        # C(j,jp).  Claim 3 says C(j,jp)=A(jp-j) (N-periodic in the lag).
        C = {}
        for j in range(k):
            for jp in range(k):
                s = 0
                for r in range(N):
                    s += (window_value(r, k) >> (k - 1 - j)) % 10  # leading digit...  careful
                C[(j, jp)] = None  # placeholder, computed properly below
        # Correct: digit_j(r) = inf_digit(r+j)
        C = {}
        for j in range(k):
            for jp in range(k):
                s = sum(inf_digit(r + j) * inf_digit(r + jp) for r in range(N))
                C[(j, jp)] = s
        # claim3 cyclic sum
        cs = 0
        for j in range(k):
            for jp in range(k):
                d = (jp - j) % N
                A = cyclic_autocorr(qn, d, N, m)
                # A(d) is the claim's predicted C(j,jp)
                cs += A * 10 ** (2 * k - 2 - j - jp)
        c3_cyclic = cs

        print(f"k={k:3d} N={N:3d} ref={ref:12d}  c1(distinct windows)={c1_psi:12d} "
              f"c2(cycl-first)={c2_psi:12d}  full_cyclic={full_cyclic:12d}")
        ok1 = (c1_psi == ref)
        ok2 = (c2_psi == ref)
        ok3 = (c3_cyclic == full_cyclic)
        # Also check C(j,jp)==A(jp-j) exactly
        ok3d = all(C[(j, jp)] == cyclic_autocorr(qn, (jp - j) % N, N, m)
                   for j in range(k) for jp in range(k))
        print(f"   claim1 distinct-window sets==Psi: {ok1}   claim2 cycl-first==Psi: {ok2}   "
              f"claim3 cyclic==autocorr: {ok3} (C==A pointwise: {ok3d})")
        if not (ok1 and ok2 and ok3d):
            all_ok = False

    print()
    print("ALL CLAIMS HOLD:" , all_ok)


from bisect import bisect_right

if __name__ == "__main__":
    main()
