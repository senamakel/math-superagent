#!/usr/bin/env python3
"""
Exploratory check: does a *general* straight-line dash from the staged point
reproduce the circle oracle 4.60333885?

Setup (unit circle, R=1):
  - Swimmer starts at center, stages by spiralling out to radius rho = 1/v,
    keeping the runner diametrically opposite, so at dash-start:
        swimmer at S = (rho, 0), runner at the antipodal boundary point (-1,0).
  - Swimmer dashes in a straight ray at angle phi (from +x axis).
        landing P = S + t*(cos phi, sin phi) with |P| = 1  =>  t = dash time.
  - Runner travels the shorter boundary arc from angle pi to angle P.

Escape iff exists phi with dash_time <= runner_time.  V = largest such v.

This is more general than the task's fixed-azimuth model (which forces the
dash ray to point exactly at the shore point); here phi is free, which is what
lets the swimmer use the optimal tangent chord.

This script is exploratory: it reports whatever V the general model yields and
compares against the oracle.  No claim that it reproduces it until it does.
"""

import math


def landing_t(rho, phi):
    """Distance t along ray S + t*u (S=(rho,0), u=(cos phi, sin phi)) that hits
    the unit circle.  Returns t>0 or None if the ray never hits the shore."""
    # |S + t u|^2 = rho^2 + 2 t rho cos(phi) + t^2 = 1
    a = 1.0
    b = 2.0 * rho * math.cos(phi)
    c = rho * rho - 1.0
    disc = b * b - 4 * a * c
    if disc < 0:
        return None
    root = math.sqrt(disc)
    # take the larger root (outer intersection)
    t = (-b + root) / (2 * a)
    return t if t > 0 else None


def runner_time(angle_p, v):
    """Shorter boundary arc from pi to angle_p, divided by v."""
    d = abs(angle_p - math.pi)
    d = min(d, 2 * math.pi - d)
    return d / v


def can_escape(v, n_phi=40000):
    rho = 1.0 / v
    for i in range(n_phi + 1):
        phi = 2 * math.pi * i / n_phi
        t = landing_t(rho, phi)
        if t is None:
            continue
        px = rho + t * math.cos(phi)
        py = 0.0 + t * math.sin(phi)
        angle_p = math.atan2(py, px) % (2 * math.pi)
        if t <= runner_time(angle_p, v):
            return True
    return False


def critical_speed(v_lo, v_hi, iters=60, **kw):
    assert can_escape(v_lo, **kw)
    assert not can_escape(v_hi, **kw)
    for _ in range(iters):
        mid = 0.5 * (v_lo + v_hi)
        if can_escape(mid, **kw):
            v_lo = mid
        else:
            v_hi = mid
    return 0.5 * (v_lo + v_hi)


if __name__ == "__main__":
    V = critical_speed(1.0, 10.0)
    print(f"general tangent-dash model  V = {V:.8f}")
    print(f"oracle                     V = 4.60333885")
    print(f"match                         = {abs(V - 4.60333885) < 5e-9}")
    print(f"pi+1 (task's radial model)    = {math.pi + 1:.8f}")
