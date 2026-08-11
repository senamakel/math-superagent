import math, sys
sys.path.insert(0, "/workspace")
from toolkit import count_points

def brute_cubes_and_S(n):
    """Enumerate all distinct lattice cubes inside [0,n]^3 by an independent
    parametrization (cross-product divisor decomposition) from verify_examples.
    Returns (C, S) where S sums lattice points in each closed cube."""
    seen = {}
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

    for (ux,uy,uz,un2) in vecs:
        for (vx,vy,vz) in vmap.get(un2, []):
            if ux*vx+uy*vy+uz*vz != 0:
                continue
            cx = uy*vz - uz*vy
            cy = uz*vx - ux*vz
            cz = ux*vy - uy*vx
            if cx==0 and cy==0 and cz==0:
                continue
            cn2 = cx*cx+cy*cy+cz*cz
            g = math.gcd(math.gcd(abs(cx),abs(cy)),abs(cz))
            base = (cx//g, cy//g, cz//g)
            bn2 = base[0]**2+base[1]**2+base[2]**2
            if un2 % bn2 != 0:
                continue
            q = un2 // bn2
            r = math.isqrt(q)
            if r*r != q:
                continue
            for w in [ (r*base[0], r*base[1], r*base[2]),
                       (-r*base[0],-r*base[1],-r*base[2]) ]:
                wn2 = w[0]**2+w[1]**2+w[2]**2
                if wn2 != un2:
                    continue
                for px in range(0, n+1):
                    for py in range(0, n+1):
                        for pz in range(0, n+1):
                            verts=[]
                            ok=True
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
                            if not ok:
                                continue
                            seen[tuple(sorted(verts))] = verts
    C = len(seen)
    S = sum(count_points(cube)[0] for cube in seen.values())
    return C, S

if __name__=="__main__":
    C_oracle = {1:1, 2:9, 4:100, 5:229, 10:4469}
    S_oracle = {1:8, 2:91, 4:1878, 5:5832, 10:387003}
    for n in [5]:
        C, S = brute_cubes_and_S(n)
        print(f"n={n}: C={C} S={S}  "
              f"[C {'OK' if C==C_oracle.get(n) else '?'} S {'OK' if S==S_oracle.get(n) else '?'}]")
