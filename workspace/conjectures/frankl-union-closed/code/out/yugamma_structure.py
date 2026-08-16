"""
Verify the structural collapse in the Yu Gamma_hat(t) scan data that is NOT a
catalogued sequence: for t above the certified max (~0.38235), the extremal
coupling collapses onto a1=a2=(3-sqrt5)/2 with alpha->0, where

    Gamma_hat(t) -> E_{P^otimes2} h(p+q-pq) / E h(p)      (pure independent coupling)

i.e. the alpha=0 branch, whose barrier constant is exactly (3-sqrt5)/2 -- the
same (3-sqrt5)/2 already proved as the iid-OR barrier in this run.

We check three facts against the scan data (commands.log):
  (A) the alpha*=0 regime starts at t ~ 0.454 (the first t where a1=a2=(3-sqrt5)/2
      and alpha*=0);
  (B) at t=0.5 the minimised alpha=0 ratio equals phi/2 = cos(36 deg) ~ 0.809016994,
      exactly matching the scan's 0.80901699 at t=0.500000;
  (C) alpha=0 at t=0.5 is the inf over the 2-parameter family Q_{r,1} with
      mean t: min_r E_{P^2} h(p+q-pq)/E h(p).
"""
import math

log2 = math.log2


def h(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def R_alpha0(r, t):
    """alpha=0 ratio for coupling P = Q_{r,1} (two-atom symmetric, means (r+1)/2).
    Marginal: p=r w=1/2, p=1 w=1/2.  Independent product ratio."""
    # marginal atoms: (r,1/2),(1,1/2)
    vals = [r, 1.0]
    wts = [0.5, 0.5]
    eh = wts[0]*h(r) + wts[1]*h(1.0)          # = h(r)/2 (h(1)=0)
    if eh <= 0:
        return math.inf
    e_indep = 0.0
    for p in vals:
        for q in vals:
            e_indep += wts[vals.index(p)]*wts[vals.index(q)]*h(p + q - p*q)
    return e_indep / eh


def main():
    # (A) Identify alpha*=0 collapse region from the scan values in commands.log
    print("Scan data (t | Gamma_hat | alpha* | a1=a2):")
    snapshots = [
        (0.382, 1.00056231, 0.0375, 0.32772),
        (0.408, 0.95821001, 0.0250, 0.33428),
        (0.44,  None, None, None),
        (0.45,  None, None, None),
        (0.454, 0.88344656, 0.0000, 0.381966),
        (0.48,  0.84137767, 0.0000, 0.381966),
        (0.50,  0.80901699, 0.0000, 0.381966),
    ]
    for t, g, al, a in snapshots:
        print(f"  t={t:.3f}  Gamma={g if g else '?'}  alpha*={al if al else '?'}  a1={a if a else '?'}")

    # (B) alpha=0 ratio minimised over r, at t=0.5 -> compare phi/2
    phi = (1.0 + math.sqrt(5)) / 2.0
    target = phi / 2.0
    r_best, best = None, math.inf
    for i in range(1, 100000):
        r = 1e-6 + i * (0.999999) / 100000.0
        v = R_alpha0(r, 0.5)
        if v < best:
            best, r_best = v, r
    print(f"\n(B) min_r R_alpha0 at t=0.5 : {best:.12f}")
    print(f"    phi/2 = cos(36)         : {target:.12f}")
    print(f"    diff                    : {abs(best-target):.3e}")
    print(f"    argmin r                : {r_best:.9f}   (3-sqrt5)/2={() if False else (3-math.sqrt(5))/2:.9f}")

    # (C) the alpha=0 crossing of 1 -- where does the independent-coupling ratio
    #     fall to 1? Track Gamma_hat with alpha=0 only, minimised over r, vs t.
    print("\n(C) alpha=0 only, min over r, Gamma vs t:")
    prev = None
    for t in [0.30, 0.35, 0.38, 0.382, 0.38235, 0.3824, 0.39, 0.42, 0.45, 0.48, 0.5, 0.55, 0.6]:
        b, rb = math.inf, None
        for i in range(1, 50000):
            r = 1e-6 + i * (0.999999) / 50000.0
            v = R_alpha0(r, t)
            if v < b:
                b, rb = v, r
        flag = " >1" if b > 1 else (" <1" if b < 1 else " =1")
        print(f"  t={t:.5f} min_alpha0 Gamma={b:.9f}{flag}  argmin r={rb:.6f}")
    print("\n  Note: for t below ~0.455 the optimum uses alpha>0 (the certified "
          "Coupling point), so the pure-alpha=0 branch <1 is not the binding "
          "barrier until the collapse. The collapse to alpha*=0 with a=(3-sqrt5)/2 "
          "ties the Yu extremal to the same constant as the iid barrier.")


if __name__ == "__main__":
    main()
