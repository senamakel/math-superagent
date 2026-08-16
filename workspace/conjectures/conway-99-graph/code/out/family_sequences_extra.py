"""Additional family sequences for srg(v,k,1,2), k=u^2+u+2.
- pentagons p5 = (1/5) n k (k-2)(k-4)  (Reimbayev, order-6 body)
- triangles p3 = n k / 6
- hexagon closed form (already known) for reference
- coclique bound alpha family: verify distinctness and closed form.
All exact integers."""
import math

def fam(u):
    k = u*u+u+2
    n = 1 + k*k//2
    return k,n

print("u   k     v        triangles       pentagons p5          coclique alpha")
for u in (1,3,4,10,31):
    k,n = fam(u)
    p3 = n*k//6
    p4 = None
    p5 = n*k*(k-2)*(k-4)//5
    d = math.isqrt(4*k-7); s=(-1-d)//2
    alpha = n*(-s)//(k-s)
    print(f"{u:>2} {k:>4} {n:>7} {p3:>12} {p5:>18} {alpha:>10}")

print()
print("pentagon sequence (feasible u): ",
      [fam(u)[1]*fam(u)[0]*(fam(u)[0]-2)*(fam(u)[0]-4)//5 for u in (1,3,4,10,31)])
print("triangle sequence:               ",
      [fam(u)[1]*fam(u)[0]//6 for u in (1,3,4,10,31)])
print("coclique-alpha sequence:         ",
      [(lambda k,n: n*(( -(1+math.isqrt(4*k-7))//2 )*(-1))//(k-(-(1+math.isqrt(4*k-7))//2)))(*fam(u)) for u in (1,3,4,10,31)])
