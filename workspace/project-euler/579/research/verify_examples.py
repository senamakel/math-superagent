import itertools, math, sys
from functools import lru_cache

def brute_cubes(n):
    """Enumerate all distinct lattice cubes inside [0,n]^3.
    A cube = {P0 + a u + b v + c w : a,b,c in {0,1}} with u,v,w pairwise
    orthogonal equal-norm nonzero integer vectors. We enumerate and dedupe
    by canonical sorted set of the 8 vertices.
    """
    seen = set()
    # integer vectors with |v|^2 <= n^2 (side length <= n) and each coord in [-n, n]
    vecs = []
    for x in range(-n, n+1):
        for y in range(-n, n+1):
            for z in range(-n, n+1):
                n2 = x*x+y*y+z*z
                if n2 >= 1 and n2 <= n*n:
                    vecs.append((x,y,z,n2))
    vmap = {}
    for (x,y,z,n2) in vecs:
        vmap.setdefault(n2, []).append((x,y,z))
    # precompute dot products quickly
    # iterate over u, v orthogonal with equal norm, w orthogonal to both with equal norm
    pts = set()
    for (ux,uy,uz,un2) in vecs:
        for (vx,vy,vz) in vmap.get(un2, []):
            if ux*vx+uy*vy+uz*vz != 0:
                continue
            # w orthogonal to both u,v with same norm
            # cross product u x v is orthogonal to both; w must be parallel to u x v
            cx = uy*vz - uz*vy
            cy = uz*vx - ux*vz
            cz = ux*vy - uy*vx
            if cx==0 and cy==0 and cz==0:
                continue
            # norm of cross = |u|^2 |v|^2 = un2^2
            # w = t*(cx,cy,cz) must have norm^2 = un2 and be integer
            # need t*|cross| = |u|, |cross| = |u|^2 -> t = |u|/|u|^2 = 1/|u|
            # so integer w parallel to cross only if cross divides properly
            cn2 = cx*cx+cy*cy+cz*cz
            # w integer parallel to (cx,cy,cz): (cx,cy,cz) = g*(cx,cy,cz)/g
            import math
            g = math.gcd(math.gcd(abs(cx),abs(cy)),abs(cz))
            base = (cx//g, cy//g, cz//g)
            bn2 = base[0]**2+base[1]**2+base[2]**2
            # w = k*base, need k^2*bn2 = un2 -> un2 must be divisible by bn2 and quotient square
            if un2 % bn2 != 0:
                continue
            q = un2 // bn2
            import math as m
            r = m.isqrt(q)
            if r*r != q:
                continue
            k1 = r
            for w in [ (k1*base[0], k1*base[1], k1*base[2]),
                       (-k1*base[0],-k1*base[1],-k1*base[2]) ]:
                wn2 = w[0]**2+w[1]**2+w[2]**2
                if wn2 != un2: 
                    continue
                # corner P0 so that all 8 vertices in box
                for px in range(0, n+1):
                    for py in range(0, n+1):
                        for pz in range(0, n+1):
                            ok=True
                            verts=[]
                            for a in (0,1):
                                for b in (0,1):
                                    for c in (0,1):
                                        V=(px+a*ux+b*vx+c*w[0],
                                           py+a*uy+b*vy+c*w[1],
                                           pz+a*uz+b*vz+c*w[2])
                                        if not (0<=V[0]<=n and 0<=V[1]<=n and 0<=V[2]<=n):
                                            ok=False;break
                                        verts.append(V)
                                    if not ok: break
                                if not ok: break
                            if not ok: continue
                            seen.add(tuple(sorted(verts)))
    return len(seen)

if __name__=="__main__":
    for n in [1,2,4]:
        print(n, brute_cubes(n))
