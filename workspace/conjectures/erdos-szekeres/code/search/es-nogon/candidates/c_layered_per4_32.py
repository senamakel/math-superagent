"""Auto-generated candidate module: layered_per4_32."""
import math
from fractions import Fraction
from lib.es_construct import es_set

def _to_int(points):
    if not points: return []
    den=1
    for (x,y) in points:
        den=math.lcm(den,Fraction(x).denominator)
        den=math.lcm(den,Fraction(y).denominator)
    return [(Fraction(x).numerator*(den//Fraction(x).denominator),
             Fraction(y).numerator*(den//Fraction(y).denominator))
            for (x,y) in points]
def _es_int(k):
    return _to_int(es_set(k))
def _aff(pts,a,b,c,d,e,f):
    return [(a*x+b*y+c, d*x+e*y+f) for (x,y) in pts]
def points(k):
    import math, random
    r=random.Random('layered_per4_32')
    pts=[]; layer=0
    while len(pts)<32:
        R=10*(layer+1)
        ang0=r.random()*2*math.pi
        n=4
        for i in range(n):
            a=ang0+2*math.pi*i/n+(layer%2)*(math.pi/n)
            pts.append((int(R*math.cos(a)), int(R*math.sin(a))))
        layer+=1
    return pts[:32]


if __name__ == '__main__':
    import sys
    k=int(sys.argv[1]) if len(sys.argv)>1 else 7
    print('points(%d)->%d'%(k,len(points(k))))
