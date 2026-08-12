#!/usr/bin/env python3
"""
PE 761 — first-principles geometry explorer for the hexagon critical speed.

Mechanism (sourced independently of stewbasic): at the critical speed V the
swimmer has staged on the boundary of the homothetic safe region (the pool
scaled by 1/v about the centre), keeping the runner centrally opposite, and
then dashes in a straight line from the stage point P to an exit point Q on
the boundary.  The escape condition at speed v is

      exists stage azimuth psi, exists exit Q :
          perim_dist(R'(psi), Q) >= v * |P_v(psi) - Q|

where
   P(psi)   = boundary point of the scale-(1/v) hexagon at azimuth psi
              (|OP| = rho(psi)/v,  rho = radial function of the hexagon)
   R'(psi)  = boundary point of the OUTER hexagon at azimuth psi + pi
   perim    = boundary distance from R' to Q along the runner's committed
              (CCW) direction  -- the swimmer exits on the far side, exactly
              as in the circle case where the run distance is pi + B.

Critical speed: the largest v for which escape is possible (bisection on
escape(v), which is monotone decreasing in v).

Validation oracle: the SAME framework on the circle (rho = 1 constant,
perim = CCW arc) must reproduce V_circle = 4.60333885 = (pi+B)/sin B,
cos B = 1/V.  This proves the framework is the right one before any hexagon
number is trusted.

Then: hexagon, circumradius 1, flat-top orientation (vertices at azimuths
30,90,150,210,270,330 deg), runner starts at the midpoint of the right edge
M0 = (sqrt3/2, 0).  Perimetre = 6.
"""
import numpy as np
import mpmath as mp

s3 = np.sqrt(3.0)
TWO, PI = 2 * np.pi, np.pi

# ---------------- circle ----------------
def circle_P(phi, v):
    return np.array([np.cos(phi), np.sin(phi)]) / v

def circle_R(phi):
    return np.array([-np.cos(phi), -np.sin(phi)])

def circle_perim(phi_R, phi_Q):
    # CCW arc length from R to Q (unit circle)
    d = (phi_Q - phi_R) % TWO
    return d

def circle_escape(v, n_phi=6000, n_q=2 * 6000):
    best = -np.inf
    for i in range(n_phi):
        phi = TWO * i / n_phi
        P = circle_P(phi, v)
        R = circle_R(phi)
        phi_R = np.arctan2(R[1], R[0])
        # Q on the circle, in the CCW sector ahead
        for j in range(n_q):
            phi_Q = TWO * j / n_q
            per = circle_perim(phi_R, phi_Q)
            if per <= 0:
                continue
            Q = np.array([np.cos(phi_Q), np.sin(phi_Q)])
            val = per - v * np.linalg.norm(P - Q)
            if val > best:
                best = val
    return best

# ---------------- regular hexagon, circumradius 1, flat-top ----------------
# vertices CCW: A1..A6 at azimuths 30,90,150,210,270,330 deg
VX = [np.array([s3/2, 0.5]), np.array([0, 1]), np.array([-s3/2, 0.5]),
      np.array([-s3/2, -0.5]), np.array([0, -1]), np.array([s3/2, -0.5])]
M0 = np.array([s3/2, 0.0])
# perimeter segments: [s_i, s_{i+1}] from P_i to P_{i+1}
PTS = [M0, VX[0], VX[1], VX[2], VX[3], VX[4], VX[5], M0]
S_EDGES = [0.0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.0]   # CCW start-s of each point

def B(s):
    """Boundary point at CCW arc length s from M0 (s mod 6 in [0,6))."""
    s = s % 6.0
    for i in range(7):
        if S_EDGES[i] <= s <= S_EDGES[i + 1]:
            t = (s - S_EDGES[i]) / (S_EDGES[i + 1] - S_EDGES[i])
            return PTS[i] + t * (PTS[i + 1] - PTS[i])
    raise ValueError(s)

def rho(phi):
    """Radial distance from O to hexagon boundary at azimuth phi."""
    phi = phi % TWO
    phi_norm = ((phi - PI / 6) % (PI / 3)) + PI / 6   # in [pi/6, pi/2]
    return s3 / (2 * np.sin(phi_norm + PI / 6))

def az_of(s):
    p = B(s)
    return np.arctan2(p[1], p[0])

def s_at_az(phi):
    """CCW arc length of the boundary point at azimuth phi."""
    phi = phi % TWO
    lo, hi = 0.0, 6.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if (az_of(mid) - phi) % TWO < PI:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)

def hex_escape(v, n_psi=4000, n_q=12000, verbose=False):
    """max over psi, s_Q of perim - v|P-Q| ; escape iff >= 0."""
    best = -np.inf
    best_arg = None
    for i in range(n_psi):
        psi = TWO * i / n_psi
        P = np.array([np.cos(psi), np.sin(psi)]) * rho(psi) / v
        s_R = s_at_az((psi + PI) % TWO)
        # Q anywhere CCW-ahead of R'
        for j in range(n_q):
            s_Q = s_R + 6.0 * (j + 1) / n_q
            per = s_Q - s_R
            Q = B(s_Q)
            val = per - v * np.linalg.norm(P - Q)
            if val > best:
                best = val
                best_arg = (psi, s_Q, s_R, P, Q)
    if verbose:
        psi, s_Q, s_R, P, Q = best_arg
        print(f"  best: psi={psi:.6f} rad ({np.degrees(psi):.3f} deg), "
              f"s_R={s_R:.6f}, s_Q={s_Q:.6f}, perim={s_Q-s_R:.6f}, "
              f"|P-Q|={np.linalg.norm(P-Q):.6f}, ratio={(s_Q-s_R)/np.linalg.norm(P-Q):.6f}")
        print(f"  Q azimuth = {np.degrees(az_of(s_Q)):.3f} deg, "
              f"|OP| = {np.linalg.norm(P):.6f} (rho(psi)={rho(psi):.6f}, /v={rho(psi)/v:.6f})")
    return best, best_arg

def bisect_critical(escape_fn, v_lo=1.0, v_hi=20.0, iters=60, **kw):
    assert escape_fn(v_lo, **kw)[0] > 0, "escape at low v must be possible"
    assert escape_fn(v_hi, **kw)[0] < 0, "escape at high v must fail"
    for _ in range(iters):
        mid = 0.5 * (v_lo + v_hi)
        if escape_fn(mid, **kw)[0] > 0:
            v_lo = mid
        else:
            v_hi = mid
    return 0.5 * (v_lo + v_hi)

if __name__ == "__main__":
    mp.mp.dps = 50
    print("=" * 70)
    print("STAGE 1: circle validation of the framework")
    print("=" * 70)
    Vc = bisect_critical(circle_escape)
    print(f"  circle critical v (framework)      : {Vc:.8f}")
    print(f"  Ponder-This oracle                 : 4.60333885")
    print(f"  framework reproduces oracle?       : "
          f"{abs(Vc - 4.60333885) < 5e-6}")
    # exact circle identity
    Bc = mp.findroot(lambda b: mp.sin(b) - (mp.pi + b) * mp.cos(b), 1.35)
    print(f"  exact crossing (sinB=(pi+B)cosB): V = {mp.nstr(1/mp.cos(Bc), 10)}")

    print()
    print("=" * 70)
    print("STAGE 2: hexagon critical speed (framework)")
    print("=" * 70)
    Vh = bisect_critical(hex_escape, n_psi=20000, n_q=24000)
    print(f"  hexagon critical v (framework) : {Vh:.8f}")
    print(f"  known answer 2+2 sqrt21/3      : {2 + 2*mp.sqrt(21)/3:.8f}")
    print()
    print("  geometry at v = Vh:")
    val, arg = hex_escape(Vh, n_psi=20000, n_q=24000, verbose=True)
    print()
    print("  residual perim - v|P-Q| =", f"{val:.6f}")