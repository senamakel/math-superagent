"""Check the claim in meet-join-parseval-self-duality.md:

    E_p[S^2] = F_n(1-2p) = O(n)   uniformly in p in (0,1)

where F_n(z) = sum_{d,d'} z^{|M_d △ M_{d'}|} over d,d' in [2,n-1], and
|M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d∧d')+1}  (proven meet formula).

The suspicion: as p -> 0 (so z = 1-2p -> 1), every term z^{dist} -> 1, so
F_n(z) -> (n-2)^2 = Theta(n^2), NOT O(n).  "Uniformly in p" would then be false.

Only the proven meet formula is used for distances (exact integer arithmetic).
"""


def pc(x):
    return bin(x).count("1")


def dist(d, dp):
    return (1 << pc(d)) + (1 << pc(dp)) - (1 << (pc(d & dp) + 1))


def F_at_z(n, z):
    """F_n(z) = sum_{d,d'} z^{dist(d,d')}, d,d' in [2,n-1]. Exact (floats only
    through z**int)."""
    total = 0.0
    ds = list(range(2, n))
    for d in ds:
        for dp in ds:
            total += z ** dist(d, dp)
    return total


def F_from_second_moment(n, p):
    """E_p[S^2] computed the OTHER way (independently, via the fold second
    moment under iid Bernoulli(p) input): E[S^2] = sum_{d,d'} E[eps_d eps_{d'}]
    with E[eps_d eps_{d'}] = (1-2p)^{|M_d △ M_{d'}|}.  This must equal
    F_n(1-2p).  Uses the same meet formula, so this is a consistency check of
    the Parseval claim at the z=1-2p level, and the O(n) assertion."""
    total = 0.0
    ds = list(range(2, n))
    for d in ds:
        for dp in ds:
            total += (1 - 2 * p) ** dist(d, dp)
    return total


for n in [16, 24, 32, 48, 64]:
    print(f"n={n}: (n-2)^2 = {(n-2)**2}")
    for p in [0.5, 0.585, 0.25, 0.1, 0.05, 1.0 / n, 0.01, 0.001]:
        F = F_at_z(n, 1 - 2 * p)
        print(f"   p={p:8g} z={1-2*p:8.4f}  F_n(1-2p)={F:12.4f}   ratio/n={F/n:9.4f}  ratio/n^2={F/(n*n):9.5f}")
    # consistency: parseval second moment
    print("   consistency E_p[S^2] vs F_n(1-2p):",
          abs(F_from_second_moment(n, 0.585) - F_at_z(n, 1 - 2 * 0.585)))
    print()
