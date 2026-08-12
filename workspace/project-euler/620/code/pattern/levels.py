"""Level-range diagnostic: for each tuple, print kmin, kmax, n_p at the
endpoints, and which geometric bound (|a-b| pinches / 1cm gap / a+b) sets
DL and DU.  Goal: closed form for g = #integer levels of n_p crossed."""
import math
import os

PI = math.pi
OUT = "/workspace/code/out/levels.txt"


def geom(c, s, t, d):
    R = c / (2.0 * PI)
    r = s / (2.0 * PI)
    rho = t / (2.0 * PI)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2.0 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None
    return R, r, a, b, x, math.sqrt(y2)


def n_t(c, s, t, d):
    g = geom(c, s, t, d)
    if g is None:
        return None
    R, r, a, b, x, y = g
    beta = math.atan2(y, x - d)   # angle at O (ring centre)
    gamma = math.atan2(y, x)      # angle at S (sun centre)
    return ((c - t) * beta + (s + t) * gamma) / PI


def bounds_detail(c, s, p, q):
    R = c / (2.0 * PI)
    r = s / (2.0 * PI)
    items = []
    for t in (p, q):
        rho = t / (2.0 * PI)
        a = R - rho
        b = r + rho
        items.append(('|a-b| t=%d' % t, abs(a - b)))
        items.append(('a+b t=%d' % t, a + b))
    items.append(('gap R-r-1', R - r - 1.0))
    DL, DLsrc = min((v for _, v in items)), None
    DU, DUsrc = min((v for _, v in items)), None
    for name, v in items:
        if v <= DL + 1e-12:
            DLsrc = name
        if v >= DU - 1e-12:
            DUsrc = name
    return DL, DU, DLsrc, DUsrc


def main():
    lines = []
    def emit(s=""):
        print(s, flush=True)
        lines.append(s)

    emit("level-range diagnostic: c s p q g kmin kmax nlo nhi DLsrc DUsrc")
    emit("=" * 90)
    for c in range(16, 28):
        for s in range(5, c - 10):
            for p in range(5, (c - s - 1) // 2 + 1):
                q = c - s - p
                DL, DU, DLsrc, DUsrc = bounds_detail(c, s, p, q)
                eps = (DU - DL) / 1e6
                nlo = n_t(c, s, p, DL + eps)
                nhi = n_t(c, s, p, DU - eps)
                if nlo is None or nhi is None or nlo > nhi:
                    continue
                kmin = int(math.ceil(nlo))
                kmax = int(math.floor(nhi))
                g = max(0, kmax - kmin + 1)
                emit("%3d %2d %2d %2d %3d  %3d %3d  %9.5f %9.5f  %-10s %-10s"
                     % (c, s, p, q, g, kmin, kmax, nlo, nhi, DLsrc, DUsrc))
    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    emit("saved %s" % OUT)


if __name__ == "__main__":
    main()