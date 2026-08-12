"""Probe: which least-mesh-angle discrete model reproduces g(16,5,5,6)=9?

The continuous single-d model (lib/gears.py) found no valid offset d, so the
tooth-phase picture needs a discrete partner.  The sourced claims say legal
planet angular positions are multiples of the least mesh angle 2*pi/(c+s)
(multiples of one slot).  Two natural centres for that lattice:
  * about O (ring centre),  * about S (sun centre).
For a planet of circumference m, tangency to C (dist a = R - rho_m from O) and
to S (dist b = r + rho_m from S) with S at (d,0) gives, for a fixed slot angle
ang, a quadratic in d; a planet centre at slot ang exists iff that d satisfies
the gap constraint R - r - d >= 1 and |a-b| <= d <= a+b.

A configuration (one d) has 2 candidate positions per type (mirror pair).  The
four planets mesh iff the 8 tooth-phase congruences are solvable, which (6
phases, 8 congruences; each planet's own phase eliminated) reduces to
    F_pU == F_pL == F_qU == F_qL  (mod 1),
with F_m = R*beta - r*gamma + xi*T_m, T_m = rho_m*(gamma+pi-beta) mod 2pi,
and the mirror pair satisfies F_L = -F_U (mod 1), so the conditions are
    2F_p in Z, 2F_q in Z, F_p - F_q in Z  (mod 1).
xi = +1 is the geometric convention; -1 is the sign-flipped alternative.

This probe enumerates every candidate d for each lattice model, checks the
phase congruences at high precision, and reports which (model, xi) reproduces
the oracle 9, then runs G(16) and G(20) for the winner.
"""
from collections import defaultdict
from mpmath import mp, mpf, pi, cos, sin, atan2, sqrt, fabs
mp.dps = 60


def phase_at(c, s, m, d, rho, R, r, xi):
    """Upper-intersection F value and angles for one planet type."""
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y = sqrt(a * a - x * x)
    beta = atan2(y, x)          # angle of centre about O
    gamma = atan2(y, x - d)     # angle of centre about S
    psi = (gamma + pi - beta) % (2 * pi)
    T = rho * psi
    F = R * beta - r * gamma + xi * T
    return F, beta, gamma, x, y


def nearint(v, tol=mpf('1e-20')):
    v = v % 1
    return min(v, 1 - v) <= tol


def probe_case(c, s, p, q, centers, xis):
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    slots = c + s
    rho = {m: mpf(m) / (2 * pi) for m in (p, q)}
    a_m = {m: R - rho[m] for m in (p, q)}
    b_m = {m: r + rho[m] for m in (p, q)}
    gap = R - r - mpf(1)
    DL = max(abs(a_m[m] - b_m[m]) for m in (p, q))
    DU = min(a_m[p] + b_m[p], a_m[q] + b_m[q], gap)
    if DL > DU:
        return {}

    def d_from_slot(m, k, center):
        ang = 2 * pi * k / slots
        a, b = a_m[m], b_m[m]
        if center == 'O':
            A, B, C = mpf(1), -2 * a * cos(ang), a * a - b * b
        else:
            A, B, C = mpf(1), 2 * b * cos(ang), b * b - a * a
        disc = B * B - 4 * A * C
        if disc < 0:
            return []
        sd = sqrt(disc)
        out = []
        for sgn in (mpf(1), mpf(-1)):
            d = (-B + sgn * sd) / (2 * A)
            if DL - mpf('1e-40') <= d <= DU + mpf('1e-40'):
                out.append(d)
        return out

    results = {}   # (center_p, center_q, xi) -> list of valid d's
    for cp in centers:
        for cq in centers:
            # candidate d from p-slots (center cp) and q-slots (center cq)
            cand = defaultdict(set)
            for m, center in ((p, cp), (q, cq)):
                for k in range(slots):
                    for d in d_from_slot(m, k, center):
                        cand[mpf(d)].add((m, k))
            for xi in xis:
                valid = []
                for d, mks in sorted(cand.items()):
                    ks_p = [k for (m, k) in mks if m == p]
                    ks_q = [k for (m, k) in mks if m == q]
                    if not ks_p or not ks_q:
                        continue
                    Fp, bp, gp, xp, yp = phase_at(c, s, p, d, rho[p], R, r, xi)
                    Fq, bq, gq, xq, yq = phase_at(c, s, q, d, rho[q], R, r, xi)
                    if nearint(2 * Fp) and nearint(2 * Fq) and nearint(Fp - Fq):
                        valid.append((d, Fp, Fq, ks_p, ks_q, abs(yp) < mpf('1e-35'),
                                      abs(yq) < mpf('1e-35')))
                results[(cp, cq, xi)] = valid
    return results


def main():
    oracle = [(16, 5, 5, 6, 9)]
    centers = ('O', 'S')
    xis = (mpf(1), mpf(-1))
    for c, s, p, q, g_expected in oracle:
        print(f"=== g({c},{s},{p},{q}) oracle {g_expected} ===")
        res = probe_case(c, s, p, q, centers, xis)
        for (cp, cq, xi), valid in sorted(res.items(), key=lambda kv: str(kv[0][2])):
            tag = f"center_p={cp} center_q={cq} xi={mp.nstr(xi, 2)}"
            print(f"  {tag}: {len(valid)} valid d")
            for d, Fp, Fq, ksp, ksq, op, oq in valid:
                print(f"      d={mp.nstr(d, 25)}  kp={ksp} kq={ksq} "
                      f"Fp%1={mp.nstr(Fp % 1, 14)} Fq%1={mp.nstr(Fq % 1, 14)} "
                      f"onaxis_p={op} onaxis_q={oq}")


if __name__ == '__main__':
    main()