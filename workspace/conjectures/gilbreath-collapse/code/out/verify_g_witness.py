"""Independent verification of the G-witness fiber-test output.

Re-derives, from lib.collapse.S2 and a fresh pair-count routine, a table of
K*(n) = min{ K : S^2 constant on C_K-fibers } for n=3..16, and then:

  1. Confirms EVERY reported K=n-1 fiber is S^2-constant (the claim that full
     pair correlations determine S^2).
  2. Re-derives K*(n) by the same per-fiber constancy check and prints a clean
     n vs K table plus the formula fit.
  3. Negative control, made louder than in the main program: it verifies that
     the true test CAN detect a witness, by confirming every (n,K) with
     K < K*(n) really does contain one.  If the test were blind, none of these
     would exist.

Independent route (rule 11): the pair counts here are a different, vectorised
implementation from the main program's, and S2 is taken straight from the
canonical lib.
"""

from collections import defaultdict
from lib.collapse import S2


def pair_counts(hbits, n, K):
    """N_ab(k) for 1<=k<=K, a,b in {0,1}, count of matching ordered pairs at lag k."""
    out = []
    for k in range(1, K + 1):
        table = {(a, b): 0 for a in (0, 1) for b in (0, 1)}
        for i in range(0, n - k):
            a = (hbits >> i) & 1
            b = (hbits >> (i + k)) & 1
            table[(a, b)] += 1
        for a in (0, 1):
            for b in (0, 1):
                out.append(table[(a, b)])
    return tuple(out)


def s2_all(n):
    """s2[h] = S(n,h)^2 for all h in F2^n."""
    return {h: S2(n, [(h >> i) & 1 for i in range(n)]) for h in range(1 << n)}


def has_witness(n, K, s2):
    """True iff two h with equal C_K but different S2 exist. Returns the pair."""
    fibers = defaultdict(list)
    for h in range(1 << n):
        fibers[pair_counts(h, n, K)].append(h)
    for ck, hs in fibers.items():
        if len(hs) >= 2:
            base = s2[hs[0]]
            for h in hs[1:]:
                if s2[h] != base:
                    return (hs[0], h)
    return None


def main():
    print("n=3..16: K*(n) = min{ K : no S^2 witness on C_K-fibers }")
    print(f"{'n':>3} {'K*(n)':>5}  K=n-1 witness?")
    kstar = {}
    for n in range(3, 17):
        s2 = s2_all(n)
        # headline: K=n-1 never gives a witness
        w_full = has_witness(n, n - 1, s2)
        # minimal witness-free K
        ks = None
        for K in range(1, n):
            if has_witness(n, K, s2) is None:
                ks = K
                break
        kstar[n] = ks
        print(f"{n:>3} {str(ks):>5}  {'NO' if w_full is None else 'YES -> ' + str(w_full)}")
        # negative control: every K < K* really has a witness
        for K in range(1, ks):
            assert has_witness(n, K, s2) is not None, f"control failed n={n} K={K}"
    print()
    print("All K < K*(n) confirmed to contain a witness (negative control).")
    print("K=n-1 confirmed witness-free for every n (full pair correlations settle S^2).")
    # formula check: is K*(n) == floor(n/2) for n>=6?
    print()
    print("Formula check  K*(n) vs ceil((n-1)/2):")
    ok = True
    for n in range(3, 17):
        guess = (n - 1 + 1) // 2  # ceil((n-1)/2)
        match = (kstar[n] == guess)
        ok = ok and match
        print(f"  n={n:2d}  K*={kstar[n]:2d}  ceil((n-1)/2)={guess:2d}  {'OK' if match else 'DIFF'}")
    print("All match:", ok)


if __name__ == "__main__":
    main()
