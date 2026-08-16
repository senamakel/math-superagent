"""Auto-generated candidate module: es_aff11."""
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
    return _aff(_es_int(k), 1,2,100, 3,1,-50)


if __name__ == '__main__':
    import sys
    k=int(sys.argv[1]) if len(sys.argv)>1 else 7
    print('points(%d)->%d'%(k,len(points(k))))
