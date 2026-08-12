"""Analyse the residue curves Q_t(d) = (c-t)*B_t + (s+t)*G_t (turns) for
(c,s,p,q)=(16,5,5,6) and count the d-solutions of the full pairwise
residue condition exactly.

Model (winning variant of tangency_enum.py):
  ring C at O radius R=c/2pi; sun S at (d,0) radius r=s/2pi.
  planet of type t radius rho=t/2pi; centre P_t(d) = (x,y) with
    |OP| = a = R-rho, |SP| = b = r+rho   ->  x=(a^2-b^2+d^2)/(2d), y=sqrt(a^2-x^2)
  B_t = atan2(y,x)/2pi (turns; angle of P about O)
  G_t = atan2(y,x-d)/2pi (turns; angle of P about S)
  residue Q_t(d) = (c-t)*B_t + (s+t)*G_t  (turns, real value)
  upper planet residue = Q_t mod 1; lower = -Q_t mod 1 (mirror identity).

  The four planets (2 of type p at +/- y, 2 of type q at +/- y) all mesh
  iff the four residues are pairwise congruent mod 1, i.e. (see side combos):
     UU/LL combos:  Q_p == Q_q (mod 1)
     UL combos:     2Q_p == 2Q_q == 0 (mod 1) and Q_p == Q_q (mod 1)
  g(c,s,p,q) = number of distinct valid d in (DL, DU].
"""
import numpy as np
from mpmath import mp, mpf, pi, atan2, sqrt

mp.dps = 60


def geom(c, s):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    return R, r


def Q_of(c, s, t, d):
    """Q_t(d) in turns as an mpf real (not modded)."""
    R, r = geom(c, s)
    rho = mpf(t) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None
    y = sqrt(y2)
    B = atan2(y, x) / (2 * pi)
    G = atan2(y, x - d) / (2 * pi)
    return (c - t) * B + (s + t) * G


def main():
    c, s, p, q = 16, 5, 5, 6
    R, r = geom(c, s)
    rp = mpf(p) / (2 * pi)
    rq = mpf(q) / (2 * pi)
    DL = max(abs(R - rp - (r + rp)), abs(R - rq - (r + rq)))
    DU = min((R - rp) + (r + rp), (R - rq) + (r + rq), R - r - 1)
    print("DL = %s  DU = %s" % (mp.nstr(DL, 10), mp.nstr(DU, 10)))

    # ---- dense sample of the curves ----
    N = 2000
    ds = [DL + (DU - DL) * mpf(i) / N for i in range(N + 1)]
    Qp = np.array([float(Q_of(c, s, p, d)) for d in ds])
    Qq = np.array([float(Q_of(c, s, q, d)) for d in ds])
    f = Qp - Qq

    print("\nQ_p range: %.6f .. %.6f" % (Qp.min(), Qp.max()))
    print("Q_q range: %.6f .. %.6f" % (Qq.min(), Qq.max()))
    print("f = Qp-Qq range: %.6f .. %.6f" % (f.min(), f.max()))
    print("2Qp range: %.6f .. %.6f" % ((2*Qp).min(), (2*Qp).max()))

    # monotonicity of Qp, Qq, f
    def n_decr(a):
        return sum(1 for i in range(1, len(a)) if a[i] < a[i-1] - 1e-12)
    print("Qp strictly-decreasing steps: %d / %d" % (n_decr(Qp), N))
    print("Qq strictly-decreasing steps: %d / %d" % (n_decr(Qq), N))
    print("f  strictly-decreasing steps: %d / %d" % (n_decr(f), N))

    # where does f cross each integer?  (solutions of Qp==Qq mod 1)
    # also where does 2Qp cross odd integers (Qp == 1/4, 3/4 mod 1)?
    def crossings(vals, level):
        """indices where vals crosses the integer level (monotone segments)."""
        out = []
        prev = vals[0] - level
        for i in range(1, len(vals)):
            cur = vals[i] - level
            if (prev < 0) != (cur < 0) and abs(prev - cur) > 0:
                out.append(i)
            prev = cur
        return out

    print("\nf crosses integers: ", [(i, f[i], f[i+1]) for i in crossings(f, 0.0)] +
          [(i, f[i]-i, f[i+1]-i) for i in crossings(f, 1.0)])
    for L in (0.0, -1.0):
        cr = crossings(f, L)
        print("f crosses level %.0f at %d places" % (L, len(cr)))
    qp = Qp % 1.0
    for hq in (0.25, 0.75):
        cr = crossings(qp, hq)
        print("Qp mod 1 crosses level %.2f at %d places" % (hq, len(cr)))
    qq = Qq % 1.0
    for hq in (0.25, 0.75):
        cr = crossings(qq, hq)
        print("Qq mod 1 crosses level %.2f at %d places" % (hq, len(cr)))

    # combined: d where BOTH 2Qp and 2Qq are odd integers (Q in {1/4,3/4})
    # and Qp == Qq mod 1.  Rather than sampling, refine by bisection later;
    # here just print the sampled Q values at the 9 known survivors.
    known = [0.1596022390254104583728889, 0.1632575743493988873478173,
             0.1710036533782917922419387, 0.1838459679405179958422423,
             0.2037141587777208939780138, 0.2343016851536968980784792,
             0.2832246016662747223335828, 0.3686314525339052794450367,
             0.5465780675574626323864891]
    print("\nknown survivors: Q_p, Q_q, Q_p-Q_q:")
    for d0 in known:
        d = mpf(str(d0))
        qp = Q_of(c, s, p, d)
        qq = Q_of(c, s, q, d)
        print("  d=%.10f  Qp=%.8f  Qq=%.8f  f=%.6f  2Qp=%.4f"
              % (d0, float(qp % 1), float(qq % 1), float(qp - qq),
                 float((2 * qp) % 2)))
    # is Qp(d)-Qq(d) really ~ -1/2 everywhere?  print sampled f at each survivor
    print("\nfull values f at survivors:")
    for d0 in known:
        d = mpf(str(d0))
        print("  f = %.12f" % float(Q_of(c, s, p, d) - Q_of(c, s, q, d)))


if __name__ == "__main__":
    main()