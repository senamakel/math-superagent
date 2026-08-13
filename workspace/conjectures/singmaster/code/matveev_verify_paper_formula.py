"""Independent verification of lib.matveev's Thm 2.2 constant evaluation.

Second route: transcribe the paper's displayed formulas (2.4), (2.5), (2.14),
(2.15), (2.16) directly here with no shared code, evaluate for two sample
forms, and compare against lib.matveev.matveev_constants.  Also verify the
Lambda values by high-precision mpmath logs.

Forms checked:
  F1: n=3, primes [2,3,5], bs [1,1,1]        (Lambda = ln 120)
  F2: n=4, primes [2,3,7,11], bs [1,1,-1,-1] (Lambda = ln(720/9240))
"""
import math
from lib.matveev import matveev_constants


def paper_formula(theta, n, primes, bs):
    """Direct transcription of Matveev 2000 §2 formulas, K=Q real:
    D = D_K/kappa = 1, rho = rank_R{ln alpha_j} = 1, C3 = n/rho = n.
    (2.4)-(2.5), (2.14)-(2.16)."""
    rho, D = 1.0, 1.0
    C3 = n / rho
    C1 = (1 + math.exp(-2 * n) / 148) * (n * math.log(2) + 2) * (1 + 1 / n) * C3
    C2 = 4 * (n + 1) * (6 + 5 / (n * math.log(2) + 2)) * math.exp(2 * n) * math.sqrt(n) * C3
    A = [math.log(p) for p in primes]
    Omega = math.prod(A)
    E = 1.0
    omega = Omega * (C1 * D * theta / math.e) ** n * (C3 * math.exp(C3) * E * math.exp(2 * theta)) ** rho
    An = A[-1]
    C0prime = math.log(C2 * D * omega / (C1 * An))
    B = max(abs(b) * a / An for (b, a) in zip(bs, A))
    exponent = -112 * 2 ** n * C2 * C0prime * D ** 2 * omega * math.log(2 * math.e * B)
    return dict(C1=C1, C2=C2, C3=C3, Omega=Omega, omega=omega, C0prime=C0prime, B=B, exponent=exponent)


def main():
    ok_all = True
    cases = [
        ("F1 ln120", 1.0, [2, 3, 5], [1, 1, 1]),
        ("F2 ln(720/9240)", 1.0, [2, 3, 7, 11], [1, 1, -1, -1]),
        ("F2 Thm2.3(ii)", 1.0 / (2.0 - 2.0 / (4 * math.e ** 5)), [2, 3, 7, 11], [1, 1, -1, -1]),
    ]
    for name, theta, primes, bs in cases:
        n = len(primes)
        p = paper_formula(theta, n, primes, bs)
        c = matveev_constants(primes, bs, theta=theta, Eval=1.0)
        keys = ["C1", "C2", "C3", "Omega", "omega", "C0prime", "B", "exponent"]
        rel = {k: abs(p[k] - c[k]) / max(1.0, abs(p[k])) for k in keys}
        ok = all(r < 1e-12 for r in rel.values())
        ok_all &= ok
        print(f"{name}: n={n}, theta={theta!r}")
        for k in keys:
            print(f"    {k:>9}: paper={p[k]:.10e}  lib={c[k]:.10e}  relerr={rel[k]:.2e}")
        print(f"    MATCH: {ok}")
    # high-precision Lambda value via mpmath
    from mpmath import mp, log
    mp.dps = 50
    L = log(mp.mpf(2)) + log(mp.mpf(3)) - log(mp.mpf(7)) - log(mp.mpf(11))
    print(f"\nmpmath Lambda(2,3,-7,-11) = {L}")
    print(f"float value                = {math.log(720) - math.log(9240)!r}")
    print(f"diff                       = {abs(float(L) - (math.log(720) - math.log(9240))):.3e}")
    print(f"\nALL MATCH: {ok_all}")


if __name__ == "__main__":
    main()