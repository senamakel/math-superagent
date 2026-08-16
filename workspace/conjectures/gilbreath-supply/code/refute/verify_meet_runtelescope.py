#!/usr/bin/env python3
"""Independent brute-force verification of the two load-bearing structural
identities the adopted approach rests on, done adversarially (hunt for any
counterexample):

1. Run-telescope (G-run-telescope): over a maximal run [u,v] of the digital
   down-set of d, XOR_{o in [u,v]} h[pos+o] == [ r_{pos+u} != r_{pos+v+1} ],
   for two-valued boundary r with h[j]=[r_j!=r_{j+1}]. And the multi-run
   reduction: T(n,d) == XOR over the per-run mismatches.

2. Meet formula (downset-row-intersection-meet-formula): M_d ∩ M_d' == M_{d∧d'},
   equivalently |M_d △ M_d'| == 2^pc(d)+2^pc(d')-2^{pc(d∧d')+1}.

Exhaustive over small sizes on real prime residues r and on random two-valued r.
complexity_class: exponential in n for the exhaustive r-cubes at tiny n only
(oracle_bound: n <= 8 for the full cube); polynomial (O(n^2)) for the run/mom
checks to moderate n.
"""
from itertools import product
from lib.primes import mod4_string

def prime_r(n):
    """r_j = q_j mod 4, length n (r[0]=2, odds in {1,3})."""
    return mod4_string(n)

def submasks(d):
    s = d
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & d

def runs_of_downset(d):
    """Maximal consecutive runs of the down-set {o<=d submask}. g=nu2(d+1)."""
    # g = trailing ones of d
    t = d
    g = 0
    while t & 1:
        g += 1
        t >>= 1
    runlen = 1 << g
    dsh = d >> g
    runs = []
    for m in range(1 << dsh.bit_length()):
        if m > dsh:
            break
        if (m & dsh) != m:
            continue
        u = m * runlen
        runs.append((u, u + runlen - 1))
    return runs

def check_runtelescope_prime(n_hi, r):
    """For each (n,d), pos=n-1-d; verify T = XOR over per-run mismatches."""
    bad = []
    for d in range(2, n_hi):
        runs = runs_of_downset(d)
        # need r long enough: max index reached is pos+v+1
        maxneed = (n_hi - 1 - d) + runs[-1][1] + 1  # approximate
        for n in range(d + 1, n_hi + 1):
            pos = n - 1 - d
            # h bits needed
            T = 0
            for o in range(d + 1):
                if (o & d) == o:
                    T ^= _h(r, pos + o)
            m = 0
            for (u, v) in runs:
                m ^= (1 if r[pos + u] % 4 != r[pos + v + 1] % 4 else 0)
            if T != m:
                bad.append((n, d, T, m))
                if len(bad) >= 10:
                    return bad
    return bad

def _h(r, j):
    """h[j] = [r_j != r_{j+1}].  r values in Z/4."""
    return 1 if r[j] % 4 != r[j + 1] % 4 else 0

def check_meet_formula(n_hi):
    bad = []
    for n in range(3, n_hi + 1):
        for d in range(2, n):
            for dp in range(2, n):
                if d == dp:
                    continue
                Md = set()
                for o in submasks(d):
                    Md.add(n - 1 - d + o)
                Mdp = set()
                for o in submasks(dp):
                    Mdp.add(n - 1 - dp + o)
                inter = Md & Mdp
                # M_{d∧dp}
                dd = d & dp
                Mdd = set()
                for o in submasks(dd):
                    Mdd.add(n - 1 - dd + o)
                if inter != Mdd:
                    bad.append(("intersection", n, d, dp, inter, Mdd))
                # distance formula
                dist = len(Md ^ Mdp)
                pred = (1 << bin(d).count('1')) + (1 << bin(dp).count('1')) \
                       - (1 << (bin(dd).count('1') + 1))
                if dist != pred:
                    bad.append(("distance", n, d, dp, dist, pred))
                if len(bad) >= 10:
                    return bad
    return bad

def check_runtelescope_random(n_hi, trials):
    """Random two-valued r: verify run-telescope over all (n,d) with r length
    sufficient.  Uses r in {1,3} (residue set) and also {0,1} to ensure the
    identity is not specific to residues."""
    bad = []
    import random
    rng = random.Random(0)
    for resid in ({1, 3}, {0, 1}):
        for _ in range(trials):
            L = n_hi + 4
            r = [rng.choice(sorted(resid)) for _ in range(L)]
            for d in range(2, n_hi):
                runs = runs_of_downset(d)
                for n in range(d + 1, n_hi + 1):
                    pos = n - 1 - d
                    if pos + runs[-1][1] + 1 >= len(r):
                        continue
                    T = 0
                    for o in range(d + 1):
                        if (o & d) == o:
                            T ^= (1 if r[pos + o] != r[pos + o + 1] else 0)
                    m = 0
                    for (u, v) in runs:
                        m ^= (1 if r[pos + u] != r[pos + v + 1] else 0)
                    if T != m:
                        bad.append((resid, n, d, T, m))
                        if len(bad) >= 10:
                            return bad
    return bad


def main():
    print("=== 1. Meet formula / distance formula (exhaustive n=3..40) ===")
    bad = check_meet_formula(40)
    if bad:
        print("  REFUTED:", bad[:4])
    else:
        print("  no counterexample, n=3..40 exhaustive (all d,d')")

    print("\n=== 2. Run-telescope on real prime residues r, n=3..200 ===")
    r = prime_r(222)  # r_j = q_j mod 4, need length ~ n_hi+2
    bad = check_runtelescope_prime(200, r)
    if bad:
        print("  REFUTED:", bad[:4])
    else:
        print("  no counterexample, (n,d) with n<=200, real prime residues")

    print("\n=== 3. Run-telescope on random two-valued r (30 trials each) ===")
    bad = check_runtelescope_random(60, 30)
    if bad:
        print("  REFUTED:", bad[:4])
    else:
        print("  no counterexample over random {1,3} and {0,1} boundary strings")


if __name__ == "__main__":
    main()
