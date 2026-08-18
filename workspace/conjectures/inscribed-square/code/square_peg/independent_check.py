"""Independent exact verification route for the square oracle."""
from itertools import combinations
from fractions import Fraction
from square_peg.oracle import point, sub, dot, _canonical_cycle, on_segment


def independent_squares(vertices):
    """Enumerate all edge-pair parameters, then test six exact distances."""
    vs = [point(*p) for p in vertices]
    edges = [(vs[i], vs[(i + 1) % len(vs)]) for i in range(len(vs))]
    out = set()
    for i, (a, b) in enumerate(edges):
        for j, (c, d) in enumerate(edges):
            if i == j:
                continue
            for k, (e, f) in enumerate(edges):
                if k in (i, j):
                    continue
                for l, (g, h) in enumerate(edges):
                    if l in (i, j, k):
                        continue
                    # Candidate endpoint u,v on first two edges; derive x,y
                    # from the two square orientations and require them on e,f/g,h.
                    for p in range(2):
                        u0, u1 = (a, b) if p == 0 else (b, a)
                        for q in range(2):
                            v0, v1 = (c, d) if q == 0 else (d, c)
                            for s in (Fraction(1), Fraction(-1)):
                                du, dv = sub(u1, u0), sub(v1, v0)
                                r = (-du[1], du[0])
                                det = (dv[0] * (du[1] - s*r[1]) -
                                       dv[1] * (du[0] - s*r[0]))
                                if not det:
                                    continue
                                rhs = sub(u0, v0)
                                t = (dv[0]*rhs[1] - dv[1]*rhs[0]) / det
                                z = (rhs[0]*(du[1]-s*r[1]) - rhs[1]*(du[0]-s*r[0])) / det
                                if not (0 <= t <= 1 and 0 <= z <= 1):
                                    continue
                                u = (u0[0]+t*du[0], u0[1]+t*du[1])
                                v = (v0[0]+z*dv[0], v0[1]+z*dv[1])
                                x = (u[0]+s*-(v[1]-u[1]), u[1]+s*(v[0]-u[0]))
                                y = (v[0]+s*-(u[1]-v[1]), v[1]+s*(u[0]-v[0]))
                                if on_segment(x,e,f) and on_segment(y,g,h):
                                    ds = sorted(dot(sub(P,Q),sub(P,Q)) for P,Q in combinations((u,v,x,y),2))
                                    if ds[0] and ds[:4] == [ds[0]]*4 and ds[4:] == [2*ds[0]]*2:
                                        out.add(_canonical_cycle((u,v,x,y)))
    return sorted(out)
