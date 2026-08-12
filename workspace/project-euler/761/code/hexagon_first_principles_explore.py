#!/usr/bin/env python3
"""
PE 761 — first-principles geometry explorer for the hexagon critical speed.

Framework (independent of the stewbasic K/alpha formula):
at speed v the swimmer stages on the boundary of the pool scaled by 1/v about
the centre, keeping the runner centrally opposite (stage point P at azimuth
psi, runner R' at azimuth psi+pi on the OUTER boundary), then dashes straight
to an exit point Q.  Escape iff

      max over psi, Q of [ perim_(R'->Q) - v * |P - Q| ]  >=  0.

Critical speed = largest v with escape possible.  The circle case of the SAME
framework must reproduce V_circle = 4.60333885 (validation oracle), then the
hexagon number is produced.

Hexagon: circumradius 1, flat-top (vertices at 30,90,...,330 deg), runner
starts at midpoint of the right edge M0 = (sqrt3/2, 0); perimeter 6.
"""
import numpy as np
import mpmath as mp

s3 = np.sqrt(3.0)
TWO, PI = 2 * np.pi, np.pi

# ---------------- circle (validation oracle) ----------------
def circle_escape_vec(v, n_psi=6000, n_q=6000, zoom=None):
    """Return (best, (psi_best, sQ_best, P, R_az, Q))."""
    best = -np.inf; b = None
    psi_grid = TWO * np.arange(n_psi) / n_psi
    sq_grid = TWO * np.arange(n_q) / n_q
    rr = 1.0 / v
    for ps in psi_grid:
        P = rr * np.array([np.cos(ps), np.sin(ps)])
        phi_R = (ps + PI) % TWO
        per = (sq_grid - phi_R) % TWO          # CCW arc length R'->Q
        mask = per > 1e-9
        if not mask.any():
            continue
        Qx, Qy = np.cos(sq_grid), np.sin(sq_grid)
        d = np.sqrt((P[0] - Qx) ** 2 + (P[1] - Qy) ** 2)
        val = per - v * d
        i = np.argmax(val)
        if val[i] > best:
            best = val[i]
            b = (ps, sq_grid[i], P, phi_R)
    return best, b

# ---------------- regular hexagon, circumradius 1, flat-top ----------------
VX = [np.array([s3/2, 0.5]), np.array([0, 1]), np.array([-s3/2, 0.5]),
      np.array([-s3/2, -0.5]), np.array([0, -1]), np.array([s3/2, -0.5])]
M0 = np.array([s3/2, 0.0])
PTS = [M0, VX[0], VX[1], VX[2], VX[3], VX[4], VX[5], M0]
S_EDGES = np.array([0.0, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.0])

def B_pts(s_arr):
    """Boundary points for array of CCW arc lengths s (s mod 6)."""
    s = np.mod(s_arr, 6.0)
    out = np.zeros((len(s), 2))
    idx = np.searchsorted(S_EDGES, s, side="right") - 1
    idx = np.clip(idx, 0, 6)
    t = (s - S_EDGES[idx]) / (S_EDGES[idx+1] - S_EDGES[idx])
    for k in range(7):
        m = idx == k
        if m.any():
            out[m] = PTS[k] + t[m, None] * (PTS[k+1] - PTS[k])
    return out

def rho(phi):
    phi = phi % TWO
    phi_norm = ((phi - PI/6) % (PI/3)) + PI/6
    return s3 / (2 * np.sin(phi_norm + PI/6))

def az_of_s(s):
    p = B_pts(np.atleast_1d(s))
    return np.arctan2(p[:, 1], p[:, 0])

def s_at_az(phi):
    """CCW arc length of hexagon boundary point at azimuth phi (scalar)."""
    phi = phi % TWO
    lo, hi = 0.0, 6.0
    for _ in range(90):
        mid = 0.5*(lo+hi)
        if (az_of_s(mid)[0] - phi) % TWO < PI:
            hi = mid
        else:
            lo = mid
    return 0.5*(lo+hi)

def hex_escape(v, n_psi=6000, n_q=12000, zoom=None, verbose=False):
    """max over psi,s_Q of perim - v|P-Q|; return (best, arg)."""
    best = -np.inf; b = None
    psi_grid = np.linspace(0, TWO, n_psi, endpoint=False)
    for ps in psi_grid:
        rp = rho(ps)
        P = (rp / v) * np.array([np.cos(ps), np.sin(ps)])
        s_R = s_at_az(ps + PI)
        # Q: CCW from s_R, up to one full perimeter ahead
        sq = s_R + 6.0 * np.arange(1, n_q+1) / n_q
        per = sq - s_R
        Q = B_pts(sq)
        d = np.sqrt((P[0]-Q[:,0])**2 + (P[1]-Q[:,1])**2)
        val = per - v*d
        i = np.argmax(val)
        if val[i] > best:
            best = val[i]
            b = (ps, sq[i], s_R, P, Q[i])
    if verbose:
        ps, s_Q, s_R, P, Q = b
        print(f"    psi={np.degrees(ps):10.4f} deg  s_R={s_R:8.5f}  s_Q={s_Q:8.5f}"
              f"  perim={s_Q-s_R:8.5f}  |PQ|={np.linalg.norm(P-Q):8.5f}"
              f"  ratio={(s_Q-s_R)/np.linalg.norm(P-Q):9.5f}  Q-az={np.degrees(az_of_s([s_Q])[0]):8.3f}")
    return best, b

def bisect(esc, v_lo=1.001, v_hi=30.0, iters=45, quiet=False, **kw):
    lo_ok = esc(v_lo, **kw)[0]
    # if not lo_ok, widen
    guard = 0
    while lo_ok <= 0 and guard < 30:
        v_lo = max(1.0001, v_lo * 0.5)
        lo_ok = esc(v_lo, **kw)[0]
        guard += 1
    hi_ok = esc(v_hi, **kw)[0]
    while hi_ok > 0 and guard < 30:
        v_hi = v_hi * 2
        hi_ok = esc(v_hi, **kw)[0]
        guard += 1
    assert lo_ok > 0 and hi_ok < 0, (v_lo, lo_ok, v_hi, hi_ok)
    for _ in range(iters):
        mid = 0.5*(v_lo+v_hi)
        if esc(mid, **kw)[0] > 0:
            v_lo = mid
        else:
            v_hi = mid
    return 0.5*(v_lo+v_hi)

if __name__ == "__main__":
    mp.mp.dps = 50
    print("=" * 72)
    print("STAGE 1: circle — validation of the staging+dash framework")
    print("=" * 72)
    Vc = bisect(circle_escape_vec, v_lo=1.1, v_hi=10.0, iters=40,
                n_psi=9000, n_q=9000)
    print(f"  circle critical v (single-frame framework): {Vc:.8f}")
    print(f"  Ponder-This oracle                         : 4.60333885")
    Bc = mp.findroot(lambda b: mp.sin(b) - (mp.pi+b)*mp.cos(b), 1.35)
    print(f"  exact identity 1/cos B, sinB=(pi+B)cosB    : {mp.nstr(1/mp.cos(Bc), 10)}")
    print(f"  match? {abs(Vc - 4.60333885) < 5e-6}")
    # profile at the critical v: where is the max?
    print("  profile at v = Vc (psi of max should be ~0: stage at azimuth 0):")
    _, b = circle_escape_vec(Vc, n_psi=9000, n_q=9000)
    print(f"    best psi={np.degrees(b[0]):.4f} deg  Q-az={np.degrees(b[1]):.4f} deg")

    print()
    print("=" * 72)
    print("STAGE 2: hexagon — critical speed of the same framework")
    print("=" * 72)
    Vh = bisect(hex_escape, v_lo=2.0, v_hi=20.0, iters=40,
                n_psi=9000, n_q=18000)
    print(f"  hexagon critical v (framework) : {Vh:.8f}")
    print(f"  known answer 2+2 sqrt21/3      : {2 + 2*mp.sqrt(21)/3:.8f}")
    print()
    print("  geometry at v = Vh:")
    val, arg = hex_escape(Vh, n_psi=9000, n_q=18000, verbose=True)
    print(f"  residual = {val:.6f}  (0 at critical)")